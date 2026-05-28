"""Signal-Constraint Spine specimen for ordered state-change routing."""

from __future__ import annotations

from collections.abc import Iterable, Mapping

from spinaltap.contract_kernel import (
    ContractRef,
    DeltaPacket,
    GateRef,
    RefusalCode,
    SignalBundle,
    refuse,
)


class SignalConstraintSpine:
    def route(
        self,
        *,
        owner: str,
        channel: str,
        delta_packets: Iterable[DeltaPacket],
        constraint_envelope: Mapping[str, object],
        validation_hook: str,
    ) -> SignalBundle:
        missing = _missing_fields(owner, channel, validation_hook)
        if missing:
            return _refusal_bundle(
                owner=owner,
                channel=channel,
                constraint_envelope=constraint_envelope,
                reason=f"missing signal metadata: {', '.join(missing)}",
            )

        return SignalBundle(
            owner=owner,
            channel=channel,
            ordered_signal_bundle=tuple(delta_packets),
            constraint_envelope=dict(constraint_envelope),
            validation_hook=validation_hook,
            residual_risk=None,
        )

    def publish_direct(
        self,
        *,
        owner: str,
        channel: str,
        global_mutation: Mapping[str, object],
    ) -> SignalBundle:
        return _refusal_bundle(
            owner=owner,
            channel=channel,
            constraint_envelope={"global_mutation": dict(global_mutation)},
            reason="direct global mutation refused before aggregation",
        )


def _missing_fields(owner: str, channel: str, validation_hook: str) -> tuple[str, ...]:
    missing: list[str] = []
    if not owner:
        missing.append("owner")
    if not channel:
        missing.append("channel")
    if not validation_hook:
        missing.append("validation hook")
    return tuple(missing)


def _refusal_bundle(
    *,
    owner: str,
    channel: str,
    constraint_envelope: Mapping[str, object],
    reason: str,
) -> SignalBundle:
    return SignalBundle(
        owner=owner,
        channel=channel,
        ordered_signal_bundle=(),
        constraint_envelope=dict(constraint_envelope),
        validation_hook="VG03",
        residual_risk=refuse(
            ContractRef.DC03,
            GateRef.VG03,
            RefusalCode.DIRECT_GLOBAL_MUTATION,
            reason,
        ),
    )
