"""Contract records and refusal primitives for the SPINALTAP kernel."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum


class ContractRef(StrEnum):
    DC01 = "DC01"
    DC02 = "DC02"
    DC03 = "DC03"
    DC04 = "DC04"
    DC05 = "DC05"
    DC06 = "DC06"


class GateRef(StrEnum):
    VG01 = "VG01"
    VG02 = "VG02"
    VG03 = "VG03"
    VG04 = "VG04"
    VG05 = "VG05"
    VG06 = "VG06"


class PromotionState(StrEnum):
    CANDIDATE = "candidate"
    BLOCKED = "blocked"
    IMPLEMENTATION_READY = "implementation_ready"


class RefusalCode(StrEnum):
    HIDDEN_INFLUENCE = "hidden_influence"
    RAW_DT = "raw_dt"
    DIRECT_GLOBAL_MUTATION = "direct_global_mutation"
    OUTSIDE_LOCAL_SLICE = "outside_local_slice"
    VAGUE_STYLE = "vague_style"
    MISSING_SPECIMEN = "missing_specimen"
    MISSING_FAILURE_PATH = "missing_failure_path"


_CONTRACT_FIELDS: dict[ContractRef, tuple[str, ...]] = {
    ContractRef.DC01: (
        "source_ref",
        "claim_text",
        "source_authority",
        "claim_fit",
        "originality_distance",
        "validation_reach",
        "influence_weight",
        "risk_flag",
        "governor_decision",
    ),
    ContractRef.DC02: (
        "elapsed_time",
        "fixed_packet_size",
        "packet_count",
        "accumulator_remainder",
        "interpolation_state",
        "overflow_risk",
    ),
    ContractRef.DC03: (
        "owner",
        "channel",
        "ordered_signal_bundle",
        "constraint_envelope",
        "validation_hook",
        "residual_risk",
    ),
    ContractRef.DC04: (
        "local_state_slice",
        "constraint_set",
        "time_packet",
        "bounded_delta",
        "residual_risk",
    ),
    ContractRef.DC05: (
        "geometry_limit",
        "lighting_limit",
        "texture_limit",
        "color_limit",
        "fog_limit",
        "alpha_limit",
        "depth_limit",
        "camera_limit",
        "animation_cadence",
        "artifact_limits",
    ),
    ContractRef.DC06: (
        "claim_ref",
        "contract_ref",
        "specimen_plan",
        "failure_path",
        "promotion_state",
        "evidence_tier",
    ),
}


@dataclass(frozen=True)
class RefusalState:
    contract: ContractRef
    gate: GateRef
    code: RefusalCode
    reason: str
    promotion_state: PromotionState = PromotionState.BLOCKED


@dataclass(frozen=True)
class SpecimenResult:
    contract: ContractRef
    gate: GateRef
    promotion_state: PromotionState
    refusal: RefusalState | None = None


@dataclass(frozen=True)
class SpecimenHook:
    contract: ContractRef
    gate: GateRef

    @classmethod
    def for_contract(cls, contract: ContractRef, gate: GateRef) -> SpecimenHook:
        return cls(contract=contract, gate=gate)

    def evaluate(self, record: Mapping[str, object]) -> SpecimenResult:
        if self.contract == ContractRef.DC06:
            return _evaluate_proof_record(self.contract, self.gate, record)

        return SpecimenResult(
            contract=self.contract,
            gate=self.gate,
            promotion_state=PromotionState.CANDIDATE,
        )


def contract_fields(contract: ContractRef) -> tuple[str, ...]:
    return _CONTRACT_FIELDS[contract]


@dataclass(frozen=True)
class SourceClaim:
    source_ref: str | None
    claim_text: str
    source_authority: float
    claim_fit: float
    originality_distance: float
    validation_reach: float
    influence_weight: float | None
    risk_flag: str | None
    governor_decision: str | None

    @classmethod
    def fields(cls) -> tuple[str, ...]:
        return contract_fields(ContractRef.DC01)


@dataclass(frozen=True)
class TimePacket:
    elapsed_time: float
    fixed_packet_size: float
    packet_count: int
    accumulator_remainder: float
    interpolation_state: float
    overflow_risk: str | None

    @classmethod
    def fields(cls) -> tuple[str, ...]:
        return contract_fields(ContractRef.DC02)


@dataclass(frozen=True)
class SignalBundle:
    owner: str
    channel: str
    ordered_signal_bundle: tuple[DeltaPacket, ...]
    constraint_envelope: Mapping[str, object]
    validation_hook: str
    residual_risk: RefusalState | None

    @classmethod
    def fields(cls) -> tuple[str, ...]:
        return contract_fields(ContractRef.DC03)


@dataclass(frozen=True)
class DeltaPacket:
    local_state_slice: Mapping[str, object]
    constraint_set: Mapping[str, object]
    time_packet: TimePacket
    bounded_delta: Mapping[str, object]
    residual_risk: RefusalState | None

    @classmethod
    def fields(cls) -> tuple[str, ...]:
        return contract_fields(ContractRef.DC04)


@dataclass(frozen=True)
class StyleLimits:
    geometry_limit: str
    lighting_limit: str
    texture_limit: str
    color_limit: str
    fog_limit: str
    alpha_limit: str
    depth_limit: str
    camera_limit: str
    animation_cadence: str
    artifact_limits: str

    @classmethod
    def fields(cls) -> tuple[str, ...]:
        return contract_fields(ContractRef.DC05)


@dataclass(frozen=True)
class ProofRecord:
    claim_ref: str
    contract_ref: ContractRef
    specimen_plan: str
    failure_path: str
    promotion_state: PromotionState
    evidence_tier: str

    @classmethod
    def fields(cls) -> tuple[str, ...]:
        return contract_fields(ContractRef.DC06)


def refuse(
    contract: ContractRef,
    gate: GateRef,
    code: RefusalCode,
    reason: str,
) -> RefusalState:
    return RefusalState(contract=contract, gate=gate, code=code, reason=reason)


def _evaluate_proof_record(
    contract: ContractRef,
    gate: GateRef,
    record: Mapping[str, object],
) -> SpecimenResult:
    if not record.get("specimen_plan"):
        refusal = refuse(
            contract,
            gate,
            RefusalCode.MISSING_SPECIMEN,
            "claim lacks a runnable specimen plan",
        )
        return SpecimenResult(contract, gate, PromotionState.BLOCKED, refusal)

    if not record.get("failure_path"):
        refusal = refuse(
            contract,
            gate,
            RefusalCode.MISSING_FAILURE_PATH,
            "claim lacks an explicit failure path",
        )
        return SpecimenResult(contract, gate, PromotionState.BLOCKED, refusal)

    return SpecimenResult(
        contract=contract,
        gate=gate,
        promotion_state=PromotionState.IMPLEMENTATION_READY,
    )
