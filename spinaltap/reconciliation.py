"""Worker routing and atomic scalar step reconciliation."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, replace
from math import isfinite
from types import MappingProxyType

from spinaltap.contract_kernel import (
    ContractRef,
    GateRef,
    RefusalCode,
    RefusalState,
    SignalBundle,
    TimePacket,
    refuse,
)
from spinaltap.contract_validation import ContractValidationError
from spinaltap.signal_spine import SignalConstraintSpine
from spinaltap.time_packet import require_solver_step
from spinaltap.vertebra_delta import VertebraDeltaWorker


@dataclass(frozen=True)
class WorkerUpdate:
    """One owner's proposed update; state and time are supplied by the step."""

    worker: VertebraDeltaWorker
    owner: str
    channel: str
    constraint_set: Mapping[str, object]
    proposed_delta: Mapping[str, object]
    validation_hook: str = "VG03"


@dataclass(frozen=True)
class StepResult:
    """A complete candidate state or a refusal with no publishable partial work."""

    next_state: Mapping[str, float] | None
    ordered_bundles: tuple[SignalBundle, ...]
    refusal: RefusalState | None
    failed_owner: str | None = None


class SpinalReconciliationHarness:
    def __init__(self, spine: SignalConstraintSpine | None = None) -> None:
        self.spine = spine or SignalConstraintSpine()

    def reconcile_step(
        self,
        *,
        state: Mapping[str, float],
        time_packet: TimePacket,
        updates: list[WorkerUpdate] | tuple[WorkerUpdate, ...],
    ) -> StepResult:
        """Read one snapshot, route in caller order, and return all-or-nothing state.

        This synchronous method never writes the caller's state. It rejects
        overlapping writes instead of choosing a winner or summing them. Worker
        and hook code is trusted; its external side effects cannot be rolled back.
        """
        try:
            step = require_solver_step(time_packet)
            snapshot = {
                key: _scalar(value, f"state.{key}")
                for key, value in _snapshot_mapping(state, "state").items()
            }
            prepared = _prepare_updates(updates)
            schedule = tuple(
                (
                    update,
                    MappingProxyType(
                        {
                            key: snapshot[key]
                            for key in sorted(update.worker.local_keys)
                            if key in snapshot
                        }
                    ),
                )
                for update in prepared
            )
        except ContractValidationError as error:
            return _blocked_step(error.refusal)

        staged: dict[str, float] = {}
        bundles: list[SignalBundle] = []
        for update, local_state in schedule:
            try:
                bundle = self.reconcile(
                    worker=update.worker,
                    owner=update.owner,
                    channel=update.channel,
                    local_state_slice=local_state,
                    constraint_set=update.constraint_set,
                    time_packet=step,
                    proposed_delta=update.proposed_delta,
                    validation_hook=update.validation_hook,
                )
            except Exception as error:
                return _blocked_step(
                    refuse(
                        ContractRef.DC03,
                        GateRef.VG03,
                        RefusalCode.VALIDATION_FAILED,
                        f"worker {update.owner} raised {type(error).__name__}",
                    ),
                    update.owner,
                )
            if bundle.residual_risk is not None:
                return _blocked_step(bundle.residual_risk, update.owner)

            # An accepted proposal must retain the state and intent scheduled
            # for this step, including when a worker implementation is extended.
            if len(bundle.ordered_signal_bundle) != 1:
                return _blocked_step(
                    _invalid("bundle", "expected one delta per worker").refusal,
                    update.owner,
                )
            delta = bundle.ordered_signal_bundle[0]
            if (
                delta.local_state_slice != local_state
                or delta.time_packet != step
                or delta.bounded_delta != update.proposed_delta
                or delta.constraint_set != update.constraint_set
            ):
                return _blocked_step(
                    _invalid(
                        "bundle",
                        "worker output changed the scheduled state, time, constraints, or proposal",
                    ).refusal,
                    update.owner,
                )
            try:
                for key, value in delta.bounded_delta.items():
                    if key not in local_state:
                        raise _invalid(
                            "bundle",
                            f"write outside scheduled local state: {key}",
                            code=RefusalCode.OUTSIDE_LOCAL_SLICE,
                        )
                    if key in staged:
                        raise _invalid(
                            "bundle",
                            f"repeated write to {key}",
                            code=RefusalCode.WRITE_CONFLICT,
                        )
                    staged[key] = _scalar(
                        snapshot[key] + _scalar(value, f"delta.{key}"),
                        f"next_state.{key}",
                    )
            except ContractValidationError as error:
                return _blocked_step(error.refusal, update.owner)
            bundles.append(bundle)

        candidate = MappingProxyType({**snapshot, **staged})
        return StepResult(candidate, tuple(bundles), None)

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


def _invalid(
    field: str,
    reason: str,
    *,
    code: RefusalCode = RefusalCode.INVALID_PAYLOAD,
) -> ContractValidationError:
    return ContractValidationError(
        ContractRef.DC03, f"reconciliation.{field}", reason, code=code
    )


def _blocked_step(risk: RefusalState, owner: str | None = None) -> StepResult:
    return StepResult(None, (), risk, owner)


def _snapshot_mapping(value: object, field: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise _invalid(field, "expected a mapping")
    snapshot: dict[str, object] = {}
    for key, item in value.items():
        if not isinstance(key, str) or not key.strip():
            raise _invalid(field, "keys must be nonblank strings")
        snapshot[key] = item
    return MappingProxyType(snapshot)


def _scalar(value: object, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise _invalid(field, "expected a finite scalar number, excluding booleans")
    try:
        number = float(value)
    except OverflowError:
        raise _invalid(field, "number is too large") from None
    if not isfinite(number):
        raise _invalid(field, "expected a finite scalar number")
    return number


def _prepare_updates(value: object) -> tuple[WorkerUpdate, ...]:
    if not isinstance(value, (list, tuple)):
        raise _invalid(
            "updates", "expected an ordered list or tuple of WorkerUpdate records"
        )
    owners: set[str] = set()
    writers: dict[str, str] = {}
    prepared: list[WorkerUpdate] = []
    for index, update in enumerate(value):
        path = f"updates[{index}]"
        if not isinstance(update, WorkerUpdate):
            raise _invalid(path, "expected a WorkerUpdate record")
        if not isinstance(update.worker, VertebraDeltaWorker):
            raise _invalid(f"{path}.worker", "expected a VertebraDeltaWorker")
        for name, text in (
            ("owner", update.owner),
            ("channel", update.channel),
            ("validation_hook", update.validation_hook),
        ):
            if not isinstance(text, str) or not text.strip():
                raise _invalid(f"{path}.{name}", "expected a nonblank string")
        if update.owner in owners:
            raise _invalid(f"{path}.owner", f"duplicate owner: {update.owner}")
        owners.add(update.owner)
        constraints = _snapshot_mapping(update.constraint_set, f"{path}.constraint_set")
        delta = _snapshot_mapping(update.proposed_delta, f"{path}.proposed_delta")
        for key in delta:
            if key in writers:
                raise _invalid(
                    f"{path}.proposed_delta.{key}",
                    f"write conflict between {writers[key]} and {update.owner} on {key}",
                    code=RefusalCode.WRITE_CONFLICT,
                )
            writers[key] = update.owner
        prepared.append(
            replace(update, constraint_set=constraints, proposed_delta=delta)
        )
    return tuple(prepared)
