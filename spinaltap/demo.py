"""Deterministic multi-worker demonstration of atomic scalar reconciliation."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass, replace
from math import isfinite

from spinaltap.contract_kernel import (
    ContractRef,
    GateRef,
    RefusalCode,
    RefusalState,
    SignalBundle,
    TimePacket,
    refuse,
)
from spinaltap.reconciliation import SpinalReconciliationHarness, WorkerUpdate
from spinaltap.signal_spine import SignalConstraintSpine
from spinaltap.time_packet import TimePacketPump
from spinaltap.vertebra_delta import VertebraDeltaWorker


@dataclass(frozen=True)
class DemoFrame:
    index: int
    elapsed_time: float
    fixed_steps: int
    accepted_steps: int
    refused_steps: int
    remainder: float
    overflow: bool


@dataclass(frozen=True)
class DemoReport:
    frames: tuple[DemoFrame, ...]
    final_position: float
    final_state: dict[str, float]
    worker_order: tuple[str, ...]
    oversized_delta_refused: bool
    guard_refusal_code: str
    conflicting_writes_refused: bool
    conflict_refusal_code: str


def _position_hook(bundle: SignalBundle) -> RefusalState | None:
    for delta in bundle.ordered_signal_bundle:
        for key, change in delta.bounded_delta.items():
            position = delta.local_state_slice[key]
            if not isinstance(position, (int, float)) or not isinstance(
                change, (int, float)
            ):
                return refuse(
                    ContractRef.DC03,
                    GateRef.VG03,
                    RefusalCode.VALIDATION_FAILED,
                    "demo position must be numeric",
                )
            if abs(position + change) > 1.0:
                return refuse(
                    ContractRef.DC03,
                    GateRef.VG03,
                    RefusalCode.VALIDATION_FAILED,
                    f"demo position {key} must remain in -1..1",
                )
    return None


def run_demo(
    elapsed_times: Sequence[float] = (0.010, 0.022, 0.200, 0.0, 0.0, 0.0),
    *,
    velocity: float = 3.0,
) -> DemoReport:
    """Adopt only complete two-worker steps; refused steps consume time but publish nothing."""
    if (
        isinstance(velocity, bool)
        or not isinstance(velocity, (int, float))
        or not isfinite(velocity)
    ):
        raise ValueError("velocity must be a finite number")
    pump = TimePacketPump(fixed_packet_size=0.016, max_packets=4)
    motion = VertebraDeltaWorker(local_keys={"x"})
    lateral = VertebraDeltaWorker(local_keys={"y"})
    spine = SignalConstraintSpine(validation_hooks={"demo.position": _position_hook})
    harness = SpinalReconciliationHarness(spine)
    state: Mapping[str, float] = {"x": 0.0, "y": 0.0}
    remainder = 0.0
    frames: list[DemoFrame] = []

    def updates_for(step: TimePacket, motion_delta: float) -> tuple[WorkerUpdate, ...]:
        return (
            WorkerUpdate(
                worker=lateral,
                owner="vertebra:demo-lateral",
                channel="motion.delta",
                constraint_set={"max_delta": 0.25},
                proposed_delta={"y": -1.5 * step.fixed_packet_size},
                validation_hook="demo.position",
            ),
            WorkerUpdate(
                worker=motion,
                owner="vertebra:demo-motion",
                channel="motion.delta",
                constraint_set={"max_delta": 0.25},
                proposed_delta={"x": motion_delta},
                validation_hook="demo.position",
            ),
        )

    for index, elapsed in enumerate(elapsed_times):
        frame = pump.step(elapsed_time=elapsed, accumulator_remainder=remainder)
        remainder = frame.accumulator_remainder
        accepted = refused = 0
        for step in pump.solver_steps(frame):
            result = harness.reconcile_step(
                state=state,
                time_packet=step,
                updates=updates_for(step, velocity * step.fixed_packet_size),
            )
            if result.refusal is not None:
                refused += 1
                continue
            assert result.next_state is not None
            state = result.next_state
            accepted += 1
        frames.append(
            DemoFrame(
                index,
                elapsed,
                frame.packet_count,
                accepted,
                refused,
                remainder,
                frame.overflow_risk is not None,
            )
        )

    # Guard specimens leave state unchanged and expose no partial candidate.
    guard_step = pump.solver_steps(
        pump.step(elapsed_time=0.016, accumulator_remainder=0)
    )[0]
    lateral_guard, motion_guard = updates_for(guard_step, 1.0)
    guard = harness.reconcile_step(
        state=state,
        time_packet=guard_step,
        updates=(replace(lateral_guard, proposed_delta={"y": 0.0}), motion_guard),
    )
    motion_update = updates_for(guard_step, 0.01)[1]
    conflict = harness.reconcile_step(
        state=state,
        time_packet=guard_step,
        updates=(motion_update, replace(motion_update, owner="vertebra:demo-conflict")),
    )
    risk = guard.refusal
    conflict_risk = conflict.refusal
    return DemoReport(
        frames=tuple(frames),
        final_position=state["x"],
        final_state=dict(state),
        worker_order=tuple(update.owner for update in updates_for(guard_step, 0)),
        oversized_delta_refused=(
            risk is not None
            and risk.code == RefusalCode.CONSTRAINT_VIOLATION
            and guard.next_state is None
            and not guard.ordered_bundles
        ),
        guard_refusal_code="" if risk is None else risk.code.value,
        conflicting_writes_refused=(
            conflict_risk is not None
            and conflict_risk.code == RefusalCode.WRITE_CONFLICT
            and conflict.next_state is None
            and not conflict.ordered_bundles
        ),
        conflict_refusal_code="" if conflict_risk is None else conflict_risk.code.value,
    )
