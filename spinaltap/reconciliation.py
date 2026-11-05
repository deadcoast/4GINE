"""Minimal spinal reconciliation harness for worker-to-spine flow."""

from __future__ import annotations

from collections.abc import Mapping

from spinaltap.contract_kernel import SignalBundle, TimePacket
from spinaltap.contract_validation import ContractValidationError
from spinaltap.signal_spine import SignalConstraintSpine
from spinaltap.vertebra_delta import VertebraDeltaWorker


class SpinalReconciliationHarness:
    def __init__(self, spine: SignalConstraintSpine | None = None) -> None:
        self.spine = spine or SignalConstraintSpine()

    def reconcile(
        self,
        *,
        worker: VertebraDeltaWorker,
        owner: str,
        channel: str,
        local_state_slice: Mapping[str, object],
        constraint_set: Mapping[str, object],
        time_packet: TimePacket,
        proposed_delta: Mapping[str, object],
        validation_hook: str,
    ) -> SignalBundle:
        try:
            delta = worker.propose(
                local_state_slice=local_state_slice,
                constraint_set=constraint_set,
                time_packet=time_packet,
                proposed_delta=proposed_delta,
            )
        except ContractValidationError as error:
            return SignalBundle(
                owner=owner,
                channel=channel,
                ordered_signal_bundle=(),
                constraint_envelope=(
                    dict(constraint_set) if isinstance(constraint_set, Mapping) else {}
                ),
                validation_hook=validation_hook,
                residual_risk=error.refusal,
            )

        if delta.residual_risk is not None:
            return SignalBundle(
                owner=owner,
                channel=channel,
                ordered_signal_bundle=(),
                constraint_envelope=dict(constraint_set),
                validation_hook=validation_hook,
                residual_risk=delta.residual_risk,
            )

        return self.spine.route(
            owner=owner,
            channel=channel,
            delta_packets=(delta,),
            constraint_envelope=constraint_set,
            validation_hook=validation_hook,
        )
