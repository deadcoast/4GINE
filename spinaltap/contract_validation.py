"""Strict mapping ingress for DC01-DC06; semantic gates still own acceptance.

Versioned external mappings use parse_contract_envelope. parse_contract remains
the unversioned legacy/internal API; neither path guesses the other's format.
Direct dataclass and identity constructors are trusted internal APIs. Snapshots
are shallow, and ingress acceptance does not authorize domain operations.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass, fields
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
        *,
        nested_parser: Callable[[ContractRef, object, str], ContractRecord] | None = None,
        enum_values: Mapping[type[StrEnum], frozenset[str]] | None = None,
    ) -> None:
        self.contract = contract
        self.path = path
        self.expected = expected
        self.nested_parser = nested_parser
        self.enum_values = enum_values
        self.data = self.mapping_value(payload, "")
        for name in expected:
            if name not in self.data:
                self.fail(name, "required field is missing")
        unknown = sorted(set(self.data) - set(expected))
        if unknown:
            self.fail(unknown[0], "unknown field")

    def location(self, field: str) -> str:
        return f"{self.path}.{field}" if field else self.path

    def nested(self, contract: ContractRef, value: object, field: str) -> ContractRecord:
        parser = self.nested_parser or _parse
        return parser(contract, value, self.location(field))

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
        if self.enum_values is not None and value not in self.enum_values[enum_type]:
            self.fail(field, f"unsupported {enum_type.__name__} for this schema revision")
        try:
            return enum_type(value)
        except ValueError:
            self.fail(field, f"unknown {enum_type.__name__} value")


def parse_contract(contract: ContractRef, payload: object) -> ContractRecord:
    """Decode an unversioned legacy/internal record without assigning identity.

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
        enum_values=reader.enum_values,
    )
    contract = risk.enum("contract", ContractRef)
    gate = risk.enum("gate", GateRef)
    if gate != contract_gate(contract):
        risk.fail("gate", "gate does not belong to the refusal contract")
    if risk.enum("promotion_state", PromotionState) != PromotionState.BLOCKED:
        risk.fail("promotion_state", "a refusal must remain blocked")
    return refuse(contract, gate, risk.enum("code", RefusalCode), risk.text("reason"))


def _delta_packet(reader: _Payload) -> DeltaPacket:
    time_packet = reader.nested(
        ContractRef.DC02, reader.data["time_packet"], "time_packet"
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
        delta = reader.nested(
            ContractRef.DC04,
            value,
            f"ordered_signal_bundle[{index}]",
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
    return StyleLimits(**{name: reader.text(name) for name in reader.expected})


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


@dataclass(frozen=True)
class ContractIdentity:
    """Exact schema identity; construction alone does not validate a record."""

    contract: ContractRef
    schema_revision: int


@dataclass(frozen=True)
class DecodedContract:
    identity: ContractIdentity
    record: ContractRecord


@dataclass(frozen=True)
class ContractSchema:
    identity: ContractIdentity
    body_fields: tuple[str, ...]
    nested_contracts: tuple[ContractIdentity, ...]
    document_ref: str
    decoder: Callable[[_Payload], ContractRecord]
    enum_values: Mapping[type[StrEnum], frozenset[str]]


# Revision 1 is a fixed compatibility boundary, not a view of future kernel
# fields or enum members. Shared body validators above implement its accepted
# meanings; incompatible changes must add a new decoder and registry entry.
_REVISION_1_FIELDS: Mapping[ContractRef, tuple[str, ...]] = MappingProxyType({
    ContractRef.DC01: (
        "source_ref", "claim_text", "source_authority", "claim_fit",
        "originality_distance", "validation_reach", "influence_weight",
        "risk_flag", "governor_decision",
    ),
    ContractRef.DC02: (
        "elapsed_time", "fixed_packet_size", "packet_count",
        "accumulator_remainder", "interpolation_state", "overflow_risk",
    ),
    ContractRef.DC03: (
        "owner", "channel", "ordered_signal_bundle", "constraint_envelope",
        "validation_hook", "residual_risk",
    ),
    ContractRef.DC04: (
        "local_state_slice", "constraint_set", "time_packet", "bounded_delta",
        "residual_risk",
    ),
    ContractRef.DC05: (
        "geometry_limit", "lighting_limit", "texture_limit", "color_limit",
        "fog_limit", "alpha_limit", "depth_limit", "camera_limit",
        "animation_cadence", "artifact_limits",
    ),
    ContractRef.DC06: (
        "claim_ref", "contract_ref", "specimen_plan", "failure_path",
        "promotion_state", "evidence_tier",
    ),
})
_REVISION_1_REFUSAL_CODES = frozenset({
    "invalid_payload", "constraint_violation", "validation_failed",
    "write_conflict", "hidden_influence", "raw_dt", "direct_global_mutation",
    "outside_local_slice", "vague_style", "missing_specimen", "missing_failure_path",
})
_REVISION_1_ENUMS: Mapping[type[StrEnum], frozenset[str]] = MappingProxyType({
    ContractRef: frozenset({"DC01", "DC02", "DC03", "DC04", "DC05", "DC06"}),
    GateRef: frozenset({"VG01", "VG02", "VG03", "VG04", "VG05", "VG06"}),
    PromotionState: frozenset({"candidate", "blocked", "implementation_ready"}),
    RefusalCode: _REVISION_1_REFUSAL_CODES,
})
_REVISION_1_NESTED = {
    ContractRef.DC03: (ContractIdentity(ContractRef.DC04, 1),),
    ContractRef.DC04: (ContractIdentity(ContractRef.DC02, 1),),
}
CONTRACT_SCHEMAS: Mapping[ContractIdentity, ContractSchema] = MappingProxyType({
    ContractIdentity(contract, 1): ContractSchema(
        identity=ContractIdentity(contract, 1),
        body_fields=body_fields,
        nested_contracts=_REVISION_1_NESTED.get(contract, ()),
        document_ref="docs/decisions/contract_identity.md",
        decoder=_DECODERS[contract][1],
        enum_values=_REVISION_1_ENUMS,
    )
    for contract, body_fields in _REVISION_1_FIELDS.items()
})


def _check_expected_contract(expected_contract: ContractRef) -> None:
    if not isinstance(expected_contract, ContractRef):
        raise TypeError("expected_contract must be a ContractRef")


def parse_contract_envelope(
    expected_contract: ContractRef, envelope: object
) -> DecodedContract:
    """Decode an explicitly versioned envelope; never infer or migrate identity.

    Untrusted envelope failures raise ContractValidationError with wire paths.
    The expected contract is a trusted programmer argument (TypeError if invalid).
    """
    _check_expected_contract(expected_contract)
    return _parse_envelope(expected_contract, envelope, expected_contract.value)


def _parse_envelope(
    expected_contract: ContractRef,
    envelope: object,
    path: str,
    required_revision: int | None = None,
) -> DecodedContract:
    header = _Payload(
        expected_contract, envelope, ("contract", "schema_revision", "payload"), path
    )
    if header.text("contract") != expected_contract.value:
        header.fail("contract", f"expected {expected_contract.value}")
    revision = header.data["schema_revision"]
    if isinstance(revision, bool) or not isinstance(revision, int) or revision <= 0:
        header.fail("schema_revision", "expected a positive integer, excluding booleans")
    if required_revision is not None and revision != required_revision:
        header.fail("schema_revision", f"parent requires revision {required_revision}")
    identity = ContractIdentity(expected_contract, revision)
    schema = CONTRACT_SCHEMAS.get(identity)
    if schema is None:
        header.fail("schema_revision", "unsupported schema revision")

    def nested(contract: ContractRef, value: object, child_path: str) -> ContractRecord:
        for pin in schema.nested_contracts:
            if pin.contract == contract:
                return _parse_envelope(
                    contract, value, child_path, pin.schema_revision
                ).record
        raise RuntimeError(f"schema {identity} has no declared dependency on {contract}")

    reader = _Payload(
        expected_contract,
        header.data["payload"],
        schema.body_fields,
        header.location("payload"),
        nested_parser=nested,
        enum_values=schema.enum_values,
    )
    return DecodedContract(identity, schema.decoder(reader))


LEGACY_BASELINE_REVISION = "d7c789bc8090f4290163534317939a752aafaeab"
LEGACY_ADAPTER_ID = "legacy-d7c789b-to-r1"


@dataclass(frozen=True)
class LegacyContractIdentity:
    """Audit label only; legacy-0 is never a valid envelope revision."""

    contract: ContractRef
    schema_revision: str = "legacy-0"


@dataclass(frozen=True)
class MigrationReceipt:
    source_ref: str
    source_revision: str
    source_identity: LegacyContractIdentity
    target_identity: ContractIdentity
    adapter_id: str


@dataclass(frozen=True)
class MigratedContract:
    decoded: DecodedContract
    receipt: MigrationReceipt


def migrate_legacy_contract(
    expected_contract: ContractRef,
    payload: object,
    source_revision: str,
    source_ref: str,
) -> MigratedContract:
    """Explicitly migrate the registered legacy baseline to revision 1.

    Attribution is caller supplied, not verified provenance. Keep the original
    artifact separately. Opaque values stay shared; no deep copy, promotion,
    execution evidence, timestamps, or subject revisions are invented.
    """
    _check_expected_contract(expected_contract)
    metadata = _Payload(
        expected_contract,
        {"source_revision": source_revision, "source_ref": source_ref},
        ("source_revision", "source_ref"),
        expected_contract.value,
    )
    if metadata.text("source_revision") != LEGACY_BASELINE_REVISION:
        metadata.fail("source_revision", "no adapter registered for this baseline")
    metadata.text("source_ref")
    record = parse_contract(expected_contract, payload)
    decoded = parse_contract_envelope(
        expected_contract, _legacy_envelope(expected_contract, record)
    )
    return MigratedContract(
        decoded,
        MigrationReceipt(
            source_ref, source_revision, LegacyContractIdentity(expected_contract),
            decoded.identity, LEGACY_ADAPTER_ID,
        ),
    )


def _legacy_envelope(contract: ContractRef, record: ContractRecord) -> dict[str, object]:
    # Never use dataclasses.asdict: it would deepcopy opaque application values.
    body = {field.name: getattr(record, field.name) for field in fields(record)}
    if isinstance(record, SignalBundle):
        body["ordered_signal_bundle"] = [
            _legacy_envelope(ContractRef.DC04, delta)
            for delta in record.ordered_signal_bundle
        ]
    elif isinstance(record, DeltaPacket):
        body["time_packet"] = _legacy_envelope(ContractRef.DC02, record.time_packet)
    return {"contract": contract.value, "schema_revision": 1, "payload": body}
