"""Deterministic one-worker demonstration of the validated prototype pipeline."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from math import isfinite

from spinaltap.contract_kernel import (
    ContractRef,
    GateRef,
    RefusalCode,
    RefusalState,
    SignalBundle,
    refuse,
)
from spinaltap.reconciliation import SpinalReconciliationHarness
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
    oversized_delta_refused: bool
    guard_refusal_code: str


def _position_hook(bundle: SignalBundle) -> RefusalState | None:
    for delta in bundle.ordered_signal_bundle:
        position = delta.local_state_slice["x"]
        change = delta.bounded_delta["x"]
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
                "demo position must remain in -1..1",
            )
    return None


def run_demo(
    elapsed_times: Sequence[float] = (0.010, 0.022, 0.200, 0.0, 0.0, 0.0),
    *,
    velocity: float = 3.0,
) -> DemoReport:
    """Apply accepted bundles to demo-owned scalar state; retain refused steps as evidence."""
    if (
        isinstance(velocity, bool)
        or not isinstance(velocity, (int, float))
        or not isfinite(velocity)
    ):
        raise ValueError("velocity must be a finite number")
    pump = TimePacketPump(fixed_packet_size=0.016, max_packets=4)
    worker = VertebraDeltaWorker(local_keys={"x"})
    spine = SignalConstraintSpine(validation_hooks={"demo.position": _position_hook})
    harness = SpinalReconciliationHarness(spine)
    position = remainder = 0.0
    frames: list[DemoFrame] = []
    for index, elapsed in enumerate(elapsed_times):
        frame = pump.step(elapsed_time=elapsed, accumulator_remainder=remainder)
        remainder = frame.accumulator_remainder
        accepted = refused = 0
        for step in pump.solver_steps(frame):
            bundle = harness.reconcile(
                worker=worker,
                owner="vertebra:demo-motion",
                channel="motion.delta",
                local_state_slice={"x": position},
                constraint_set={"max_delta": 0.25},
                time_packet=step,
                proposed_delta={"x": velocity * step.fixed_packet_size},
                validation_hook="demo.position",
            )
            if bundle.residual_risk is not None:
                refused += 1
                continue
            for delta in bundle.ordered_signal_bundle:
                change = delta.bounded_delta["x"]
                assert isinstance(change, (int, float))
                position += change
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

    # A separate guard specimen proposes an oversized update and never applies it.
    guard_step = pump.solver_steps(
        pump.step(elapsed_time=0.016, accumulator_remainder=0)
    )[0]
    guard = harness.reconcile(
        worker=worker,
        owner="vertebra:demo-motion",
        channel="motion.delta",
        local_state_slice={"x": position},
        constraint_set={"max_delta": 0.25},
        time_packet=guard_step,
        proposed_delta={"x": 1.0},
        validation_hook="demo.position",
    )
    risk = guard.residual_risk
    return DemoReport(
        tuple(frames),
        position,
        risk is not None
        and risk.code == RefusalCode.CONSTRAINT_VIOLATION
        and not guard.ordered_signal_bundle,
        "" if risk is None else risk.code.value,
    )
