"""Vertebra Delta Worker specimen for local-slice bounded deltas."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import replace
from math import isfinite
from types import MappingProxyType

from spinaltap.contract_kernel import (
    ContractRef,
    DeltaPacket,
    GateRef,
    RefusalCode,
    RefusalState,
    TimePacket,
    contract_gate,
    refuse,
)
from spinaltap.contract_validation import parse_contract
from spinaltap.time_packet import require_solver_step


def constraint_refusal(
    delta: DeltaPacket,
    *,
    local_keys: frozenset[str] | None = None,
) -> RefusalState | None:
    """Validate per-component numeric deltas; no partial acceptance or clamping."""
    if delta.residual_risk is not None:
        return delta.residual_risk
    allowed = set(delta.local_state_slice)
    if local_keys is not None:
        outside_state = allowed - local_keys
        if outside_state:
            return refuse(
                ContractRef.DC04,
                GateRef.VG04,
                RefusalCode.OUTSIDE_LOCAL_SLICE,
                f"state keys outside worker ownership: {', '.join(sorted(outside_state))}",
            )
    outside_delta = set(delta.bounded_delta) - allowed
    if outside_delta:
        return refuse(
            ContractRef.DC04,
            GateRef.VG04,
            RefusalCode.OUTSIDE_LOCAL_SLICE,
            f"delta keys outside local state slice: {', '.join(sorted(outside_delta))}",
        )
    return magnitude_refusal(delta.constraint_set, delta.bounded_delta)


def magnitude_refusal(
    constraints: Mapping[str, object],
    values: Mapping[str, object],
    *,
    contract: ContractRef = ContractRef.DC04,
) -> RefusalState | None:
    """Check the scalar budget schema even when there are no proposed values."""
    gate = contract_gate(contract)
    if set(constraints) != {"max_delta"}:
        return refuse(
            contract,
            gate,
            RefusalCode.INVALID_PAYLOAD,
            "constraints must specify exactly max_delta; unsupported rules cannot be ignored",
        )
    limit = _finite_number(constraints["max_delta"])
    if limit is None or limit < 0:
        return refuse(
            contract,
            gate,
            RefusalCode.INVALID_PAYLOAD,
            "max_delta must be a finite nonnegative number, excluding booleans",
        )
    for key, value in values.items():
        numeric = _finite_number(value)
        if numeric is None:
            return refuse(
                contract,
                gate,
                RefusalCode.INVALID_PAYLOAD,
                f"bounded_delta.{key} must be a finite number, excluding booleans",
            )
        if abs(numeric) > limit:
            return refuse(
                contract,
                gate,
                RefusalCode.CONSTRAINT_VIOLATION,
                f"bounded_delta.{key} exceeds max_delta {limit}",
            )
    return None


def _finite_number(value: object) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    try:
        number = float(value)
    except OverflowError:
        return None
    return number if isfinite(number) else None


class VertebraDeltaWorker:
    def __init__(self, local_keys: set[str]) -> None:
        if any(not isinstance(key, str) or not key.strip() for key in local_keys):
            raise ValueError("local_keys must contain nonblank strings")
        self.local_keys = frozenset(local_keys)

    def propose(
        self,
        *,
        local_state_slice: Mapping[str, object],
        constraint_set: Mapping[str, object],
        time_packet: TimePacket,
        proposed_delta: Mapping[str, object],
    ) -> DeltaPacket:
        step = require_solver_step(time_packet)
        delta = parse_contract(
            ContractRef.DC04,
            {
                "local_state_slice": local_state_slice,
                "constraint_set": constraint_set,
                "time_packet": step,
                "bounded_delta": proposed_delta,
                "residual_risk": None,
            },
        )
        assert isinstance(delta, DeltaPacket)
        risk = constraint_refusal(delta, local_keys=self.local_keys)
        if risk is not None:
            return replace(
                delta,
                bounded_delta=MappingProxyType({}),
                residual_risk=risk,
            )
        return delta
