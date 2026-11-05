"""Strict mapping ingress for DC01-DC06; semantic gates still own acceptance.

Direct dataclass constructors are trusted internal APIs. External mappings must
pass through parse_contract before use. No string-to-number or bool-to-number
coercion is performed, and unknown fields are refused rather than discarded.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import fields
from enum import StrEnum
from math import isfinite
from types import MappingProxyType
from typing import NoReturn, TypeVar

from spinaltap.contract_kernel import (
    ContractRef,
    DeltaPacket,
    GateRef,
    PromotionState,
    ProofRecord,
    RefusalCode,
    RefusalState,
    SignalBundle,
    SourceClaim,
    StyleLimits,
    TimePacket,
    contract_fields,
    contract_gate,
    refuse,
)


ContractRecord = (
    SourceClaim | TimePacket | SignalBundle | DeltaPacket | StyleLimits | ProofRecord
)
_Enum = TypeVar("_Enum", bound=StrEnum)


class ContractValidationError(ValueError):
    """An invalid field with its owning contract, gate, and blocked refusal."""

    def __init__(
        self,
        contract: ContractRef,
        field: str,
        reason: str,
        *,
        code: RefusalCode = RefusalCode.INVALID_PAYLOAD,
    ) -> None:
        self.field = field
        self.refusal = refuse(
            contract,
            contract_gate(contract),
            code,
            f"{field}: {reason}",
        )
        super().__init__(self.refusal.reason)


class _Payload:
    def __init__(
        self,
        contract: ContractRef,
        payload: object,
        expected: tuple[str, ...],
        path: str,
    ) -> None:
        self.contract = contract
        self.path = path
        self.data = self.mapping_value(payload, "")
        for name in expected:
            if name not in self.data:
                self.fail(name, "required field is missing")
        unknown = sorted(set(self.data) - set(expected))
        if unknown:
            self.fail(unknown[0], "unknown field")

    def location(self, field: str) -> str:
        return f"{self.path}.{field}" if field else self.path

    def fail(self, field: str, reason: str) -> NoReturn:
        raise ContractValidationError(self.contract, self.location(field), reason)

    def mapping_value(self, value: object, field: str) -> Mapping[str, object]:
        if not isinstance(value, Mapping):
            self.fail(field, "expected a mapping")
        snapshot: dict[str, object] = {}
        for key, item in value.items():
            if not isinstance(key, str) or not key.strip():
                self.fail(field, "mapping keys must be nonblank strings")
            snapshot[key] = item
        return MappingProxyType(snapshot)

    def mapping(self, field: str) -> Mapping[str, object]:
        return self.mapping_value(self.data[field], field)

    def text(self, field: str, *, allow_blank: bool = False) -> str:
        value = self.data[field]
        if not isinstance(value, str):
            self.fail(field, "expected a string")
        if not allow_blank and not value.strip():
            self.fail(field, "expected a nonblank string")
        return value

    def optional_text(self, field: str, *, allow_blank: bool = False) -> str | None:
        if self.data[field] is None:
            return None
        return self.text(field, allow_blank=allow_blank)

    def number(
        self, field: str, *, minimum: float = 0.0, maximum: float | None = None
    ) -> float:
        value = self.data[field]
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            self.fail(field, "expected a finite number, excluding booleans")
        try:
            number = float(value)
        except OverflowError:
            self.fail(field, "number is too large")
        if not isfinite(number):
            self.fail(field, "expected a finite number")
        if number < minimum:
            self.fail(field, f"number must be at least {minimum}")
        if maximum is not None and number > maximum:
            self.fail(field, f"number must be at most {maximum}")
        return number

    def count(self, field: str) -> int:
        value = self.data[field]
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            self.fail(field, "expected a nonnegative integer, excluding booleans")
        return value

    def enum(self, field: str, enum_type: type[_Enum]) -> _Enum:
        value = self.text(field)
        try:
            return enum_type(value)
        except ValueError:
            self.fail(field, f"unknown {enum_type.__name__} value")


def parse_contract(contract: ContractRef, payload: object) -> ContractRecord:
    """Decode a complete mapping or raise ContractValidationError.

    Nested records may be mappings or existing matching dataclasses; both are
    validated. Mapping fields receive shallow, read-only snapshots. Their values
    remain opaque until module-specific value schemas are defined.
    """
    return _parse(contract, payload, contract.value)


def _parse(contract: ContractRef, payload: object, path: str) -> ContractRecord:
    record_type, decoder = _DECODERS[contract]
    if isinstance(payload, record_type):
        payload = {
            field.name: getattr(payload, field.name) for field in fields(payload)
        }
    reader = _Payload(contract, payload, contract_fields(contract), path)
    return decoder(reader)


def _source_claim(reader: _Payload) -> SourceClaim:
    decision = reader.optional_text("governor_decision")
    if decision is not None and decision not in {"allow", "down_weight", "block"}:
        reader.fail("governor_decision", "unknown governor decision")
    weight = (
        None
        if reader.data["influence_weight"] is None
        else reader.number("influence_weight", maximum=1.0)
    )
    return SourceClaim(
        source_ref=reader.optional_text("source_ref", allow_blank=True),
        claim_text=reader.text("claim_text"),
        source_authority=reader.number("source_authority", maximum=1.0),
        claim_fit=reader.number("claim_fit", maximum=1.0),
        originality_distance=reader.number("originality_distance", maximum=1.0),
        validation_reach=reader.number("validation_reach", maximum=1.0),
        influence_weight=weight,
        risk_flag=reader.optional_text("risk_flag"),
        governor_decision=decision,
    )


def _time_packet(reader: _Payload) -> TimePacket:
    size = reader.number("fixed_packet_size")
    if size == 0:
        reader.fail("fixed_packet_size", "must be positive")
    return TimePacket(
        elapsed_time=reader.number("elapsed_time"),
        fixed_packet_size=size,
        packet_count=reader.count("packet_count"),
        accumulator_remainder=reader.number("accumulator_remainder"),
        interpolation_state=reader.number("interpolation_state", maximum=1.0),
        overflow_risk=reader.optional_text("overflow_risk"),
    )


def _residual_risk(reader: _Payload) -> RefusalState | None:
    value = reader.data["residual_risk"]
    if value is None:
        return None
    if isinstance(value, RefusalState):
        value = {field.name: getattr(value, field.name) for field in fields(value)}
    risk = _Payload(
        reader.contract,
        value,
        ("contract", "gate", "code", "reason", "promotion_state"),
        reader.location("residual_risk"),
    )
    contract = risk.enum("contract", ContractRef)
    gate = risk.enum("gate", GateRef)
    if gate != contract_gate(contract):
        risk.fail("gate", "gate does not belong to the refusal contract")
    if risk.enum("promotion_state", PromotionState) != PromotionState.BLOCKED:
        risk.fail("promotion_state", "a refusal must remain blocked")
    return refuse(contract, gate, risk.enum("code", RefusalCode), risk.text("reason"))


def _delta_packet(reader: _Payload) -> DeltaPacket:
    time_packet = _parse(
        ContractRef.DC02, reader.data["time_packet"], reader.location("time_packet")
    )
    assert isinstance(time_packet, TimePacket)
    return DeltaPacket(
        local_state_slice=reader.mapping("local_state_slice"),
        constraint_set=reader.mapping("constraint_set"),
        time_packet=time_packet,
        bounded_delta=reader.mapping("bounded_delta"),
        residual_risk=_residual_risk(reader),
    )


def _signal_bundle(reader: _Payload) -> SignalBundle:
    raw_signals = reader.data["ordered_signal_bundle"]
    if not isinstance(raw_signals, (list, tuple)):
        reader.fail("ordered_signal_bundle", "expected an ordered list or tuple")
    signals: list[DeltaPacket] = []
    for index, value in enumerate(raw_signals):
        delta = _parse(
            ContractRef.DC04,
            value,
            reader.location(f"ordered_signal_bundle[{index}]"),
        )
        assert isinstance(delta, DeltaPacket)
        signals.append(delta)
    risk = _residual_risk(reader)
    return SignalBundle(
        # Refusal bundles may preserve the missing metadata that caused refusal.
        owner=reader.text("owner", allow_blank=risk is not None),
        channel=reader.text("channel", allow_blank=risk is not None),
        ordered_signal_bundle=tuple(signals),
        constraint_envelope=reader.mapping("constraint_envelope"),
        validation_hook=reader.text("validation_hook", allow_blank=risk is not None),
        residual_risk=risk,
    )


def _style_limits(reader: _Payload) -> StyleLimits:
    return StyleLimits(**{name: reader.text(name) for name in StyleLimits.fields()})


def _proof_record(reader: _Payload) -> ProofRecord:
    return ProofRecord(
        claim_ref=reader.text("claim_ref"),
        contract_ref=reader.enum("contract_ref", ContractRef),
        specimen_plan=reader.text("specimen_plan", allow_blank=True),
        failure_path=reader.text("failure_path", allow_blank=True),
        promotion_state=reader.enum("promotion_state", PromotionState),
        evidence_tier=reader.text("evidence_tier"),
    )


_DECODERS: dict[
    ContractRef, tuple[type[ContractRecord], Callable[[_Payload], ContractRecord]]
] = {
    ContractRef.DC01: (SourceClaim, _source_claim),
    ContractRef.DC02: (TimePacket, _time_packet),
    ContractRef.DC03: (SignalBundle, _signal_bundle),
    ContractRef.DC04: (DeltaPacket, _delta_packet),
    ContractRef.DC05: (StyleLimits, _style_limits),
    ContractRef.DC06: (ProofRecord, _proof_record),
}
