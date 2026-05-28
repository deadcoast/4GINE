"""Vertebra Delta Worker specimen for local-slice bounded deltas."""

from __future__ import annotations

from collections.abc import Mapping

from spinaltap.contract_kernel import (
    ContractRef,
    DeltaPacket,
    GateRef,
    RefusalCode,
    TimePacket,
    refuse,
)


class VertebraDeltaWorker:
    def __init__(self, local_keys: set[str]) -> None:
        self.local_keys = frozenset(local_keys)

    def propose(
        self,
        *,
        local_state_slice: Mapping[str, object],
        constraint_set: Mapping[str, object],
        time_packet: TimePacket,
        proposed_delta: Mapping[str, object],
    ) -> DeltaPacket:
        allowed_keys = self.local_keys.intersection(local_state_slice.keys())
        outside_keys = tuple(
            sorted(key for key in proposed_delta if key not in allowed_keys)
        )

        if outside_keys:
            refusal = refuse(
                ContractRef.DC04,
                GateRef.VG04,
                RefusalCode.OUTSIDE_LOCAL_SLICE,
                f"delta keys outside local state slice: {', '.join(outside_keys)}",
            )
            return DeltaPacket(
                local_state_slice=dict(local_state_slice),
                constraint_set=dict(constraint_set),
                time_packet=time_packet,
                bounded_delta={},
                residual_risk=refusal,
            )

        return DeltaPacket(
            local_state_slice=dict(local_state_slice),
            constraint_set=dict(constraint_set),
            time_packet=time_packet,
            bounded_delta=dict(proposed_delta),
            residual_risk=None,
        )
