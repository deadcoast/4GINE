import unittest
from collections.abc import Mapping, MutableMapping
from dataclasses import replace
from typing import cast

from spinaltap.contract_kernel import (
    ContractRef,
    DeltaPacket,
    GateRef,
    RefusalCode,
    SignalBundle,
    TimePacket,
    refuse,
)
from spinaltap.contract_validation import ContractValidationError
from spinaltap.reconciliation import SpinalReconciliationHarness
from spinaltap.signal_spine import SignalConstraintSpine, SignalValidationHook
from spinaltap.time_packet import TimePacketPump
from spinaltap.vertebra_delta import VertebraDeltaWorker


def fixed_step() -> TimePacket:
    return TimePacket(0.016, 0.016, 1, 0.0, 0.0, None)


def delta_packet(value=1.0) -> DeltaPacket:
    return DeltaPacket({"x": 0.0}, {"max_delta": 2.0}, fixed_step(), {"x": value}, None)


class SolverTimeTests(unittest.TestCase):
    def test_subnormal_time_does_not_round_a_fraction_into_a_whole_step(self):
        pump = TimePacketPump(2e-323, 4)
        packet = pump.step(elapsed_time=5e-324, accumulator_remainder=0)
        self.assertEqual(packet.packet_count, 0)
        self.assertEqual(packet.accumulator_remainder, 5e-324)

    def test_worker_rejects_raw_time_and_unexpanded_frame_packet(self):
        worker = VertebraDeltaWorker({"x"})
        values = (
            (0.04, RefusalCode.RAW_DT),
            (
                replace(fixed_step(), elapsed_time=0.04, packet_count=2),
                RefusalCode.INVALID_PAYLOAD,
            ),
            (replace(fixed_step(), packet_count=0), RefusalCode.INVALID_PAYLOAD),
            (
                replace(fixed_step(), fixed_packet_size=float("nan")),
                RefusalCode.INVALID_PAYLOAD,
            ),
        )
        for value, code in values:
            with (
                self.subTest(value=value),
                self.assertRaises(ContractValidationError) as caught,
            ):
                worker.propose(
                    local_state_slice={"x": 0},
                    constraint_set={"max_delta": 2},
                    time_packet=cast(TimePacket, value),
                    proposed_delta={"x": 1},
                )
            self.assertEqual(caught.exception.refusal.code, code)

    def test_frame_expansion_delivers_only_fixed_time_to_workers(self):
        pump = TimePacketPump(0.016, 4)
        frame = pump.step(elapsed_time=0.04, accumulator_remainder=0)
        steps = pump.solver_steps(frame)
        self.assertEqual(len(steps), 2)
        self.assertEqual(steps, (fixed_step(), fixed_step()))
        self.assertEqual(frame.elapsed_time, 0.04)
        self.assertAlmostEqual(frame.accumulator_remainder, 0.008)

    def test_pump_rejects_bad_configuration_and_elapsed_values(self):
        for size in (0, -1, True, float("nan"), float("inf")):
            with self.subTest(size=size), self.assertRaises(ValueError):
                TimePacketPump(size, 4)
        for count in (0, -1, True, 1.5, 4097):
            with self.subTest(count=count), self.assertRaises(ValueError):
                TimePacketPump(0.016, cast(int, count))
        pump = TimePacketPump(0.016, 4)
        for value in (-1, True, float("nan"), float("inf")):
            with self.subTest(value=value), self.assertRaises(ValueError):
                pump.step(elapsed_time=value, accumulator_remainder=0)
            with self.subTest(remainder=value), self.assertRaises(ValueError):
                pump.step(elapsed_time=0, accumulator_remainder=value)
        with self.assertRaises(ValueError):
            pump.step(elapsed_time=1e308, accumulator_remainder=1e308)

    def test_exact_decimal_boundary_does_not_lose_a_step(self):
        pump = TimePacketPump(0.1, 4)
        frame = pump.step(elapsed_time=0.3, accumulator_remainder=0)
        self.assertEqual(frame.packet_count, 3)
        self.assertAlmostEqual(frame.accumulator_remainder, 0)
        below = pump.step(elapsed_time=0.3 - 1e-10, accumulator_remainder=0)
        self.assertEqual(below.packet_count, 2)

    def test_accumulator_conserves_time_over_many_frames_and_drains_backlog(self):
        pump = TimePacketPump(0.016, 4)
        remainder = consumed = total = 0.0
        samples = [0.005, 0.011, 0.04, 0.0, 0.2] * 200
        for elapsed in samples:
            frame = pump.step(elapsed_time=elapsed, accumulator_remainder=remainder)
            remainder = frame.accumulator_remainder
            total += elapsed
            consumed += frame.packet_count * frame.fixed_packet_size
            self.assertLessEqual(frame.packet_count, 4)
            self.assertGreaterEqual(remainder, 0)
            self.assertAlmostEqual(consumed + remainder, total, places=9)
        for _ in range(1000):
            if remainder < 0.016:
                break
            frame = pump.step(elapsed_time=0, accumulator_remainder=remainder)
            remainder = frame.accumulator_remainder
            consumed += frame.packet_count * frame.fixed_packet_size
        self.assertLess(remainder, 0.016)
        self.assertAlmostEqual(consumed + remainder, total, places=9)

    def test_solver_expansion_rejects_foreign_or_oversized_packets(self):
        pump = TimePacketPump(0.016, 4)
        for packet in (
            replace(fixed_step(), fixed_packet_size=0.02),
            replace(fixed_step(), packet_count=10**20),
            0.016,
        ):
            with (
                self.subTest(packet=packet),
                self.assertRaises(ContractValidationError),
            ):
                pump.solver_steps(cast(TimePacket, packet))


class WorkerConstraintTests(unittest.TestCase):
    def propose(self, delta, constraints=None, state=None):
        return VertebraDeltaWorker({"x", "y"}).propose(
            local_state_slice={"x": 0, "y": 0} if state is None else state,
            constraint_set={"max_delta": 2} if constraints is None else constraints,
            time_packet=fixed_step(),
            proposed_delta=delta,
        )

    def test_per_component_limit_accepts_boundary_and_refuses_whole_proposal(self):
        accepted = self.propose({"x": -2, "y": 2})
        self.assertIsNone(accepted.residual_risk)
        refused = self.propose({"x": 1, "y": 2.01})
        self.assertEqual(refused.bounded_delta, {})
        assert refused.residual_risk is not None
        self.assertEqual(refused.residual_risk.code, RefusalCode.CONSTRAINT_VIOLATION)
        self.assertIn("y", refused.residual_risk.reason)

    def test_zero_budget_only_accepts_zero_delta(self):
        self.assertIsNone(self.propose({"x": 0}, {"max_delta": 0}).residual_risk)
        self.assertIsNotNone(self.propose({"x": 0.001}, {"max_delta": 0}).residual_risk)

    def test_bad_or_unknown_constraints_are_refused(self):
        for constraints in (
            {},
            {"max_delta": -1},
            {"max_delta": True},
            {"max_delta": float("nan")},
            {"max_delta": "2"},
            {"max_delta": 2, "unknown_rule": 3},
        ):
            with self.subTest(constraints=constraints):
                result = self.propose({"x": 1}, constraints)
                self.assertEqual(result.bounded_delta, {})
                assert result.residual_risk is not None
                self.assertEqual(result.residual_risk.code, RefusalCode.INVALID_PAYLOAD)

    def test_nonnumeric_or_nonfinite_delta_is_refused(self):
        for value in (True, "1", None, float("nan"), float("inf"), 10**1000):
            with self.subTest(value=repr(value)[:30]):
                result = self.propose({"x": value})
                self.assertEqual(result.bounded_delta, {})
                self.assertIsNotNone(result.residual_risk)

    def test_worker_cannot_read_state_outside_its_registered_keys(self):
        result = self.propose({"x": 1}, state={"x": 0, "world.secret": 7})
        assert result.residual_risk is not None
        self.assertEqual(result.residual_risk.code, RefusalCode.OUTSIDE_LOCAL_SLICE)
        self.assertEqual(result.bounded_delta, {})


class SignalHookTests(unittest.TestCase):
    def test_empty_bundle_still_requires_a_valid_constraint_envelope(self):
        result = self.route(SignalConstraintSpine(), deltas=[], envelope={})
        assert result.residual_risk is not None
        self.assertEqual(result.residual_risk.code, RefusalCode.INVALID_PAYLOAD)

    def test_invalid_mappings_are_refused_without_crashing_the_refusal_path(self):
        spine = SignalConstraintSpine()
        result = spine.route(
            owner="worker",
            channel="motion",
            delta_packets=[],
            constraint_envelope=cast(Mapping[str, object], None),
            validation_hook="VG03",
        )
        self.assertIsNotNone(result.residual_risk)
        result = SpinalReconciliationHarness().reconcile(
            worker=VertebraDeltaWorker({"x"}),
            owner="worker",
            channel="motion",
            local_state_slice={"x": 0},
            constraint_set=cast(Mapping[str, object], None),
            time_packet=fixed_step(),
            proposed_delta={"x": 1},
            validation_hook="VG03",
        )
        self.assertIsNotNone(result.residual_risk)
        self.assertEqual(result.ordered_signal_bundle, ())

    def test_hook_registration_rejects_blank_duplicate_and_noncallable_entries(self):
        spine = SignalConstraintSpine()
        for name, hook in (
            (" ", lambda bundle: None),
            ("VG03", lambda bundle: None),
            ("invalid", None),
        ):
            with self.subTest(name=name), self.assertRaises(ValueError):
                spine.register_validation_hook(name, cast(SignalValidationHook, hook))

    def route(self, spine, *, hook="VG03", deltas=None, envelope=None):
        return spine.route(
            owner="worker:motion",
            channel="motion.delta",
            delta_packets=[delta_packet()] if deltas is None else deltas,
            constraint_envelope={"max_delta": 2} if envelope is None else envelope,
            validation_hook=hook,
        )

    def test_registered_hook_runs_once_before_acceptance(self):
        seen = []

        def validate(bundle):
            seen.append(bundle)
            return None

        spine = SignalConstraintSpine(validation_hooks={"motion": validate})
        result = self.route(spine, hook="motion")
        self.assertIsNone(result.residual_risk)
        self.assertEqual(seen, [result])

    def test_unknown_hook_is_refused(self):
        result = self.route(SignalConstraintSpine(), hook="missing")
        self.assertEqual(result.ordered_signal_bundle, ())
        assert result.residual_risk is not None
        self.assertEqual(result.residual_risk.code, RefusalCode.VALIDATION_FAILED)

    def test_hook_refusal_exception_and_invalid_return_fail_closed(self):
        refusal = refuse(
            ContractRef.DC03,
            GateRef.VG03,
            RefusalCode.VALIDATION_FAILED,
            "channel closed",
        )

        def rejecting(bundle):
            return refusal

        def raising(bundle):
            raise RuntimeError("hook failed")

        def invalid(bundle):
            return True

        for validator in (rejecting, raising, invalid):
            with self.subTest(validator=validator.__name__):
                spine = SignalConstraintSpine(
                    validation_hooks={"custom": cast(SignalValidationHook, validator)}
                )
                result = self.route(spine, hook="custom")
                self.assertEqual(result.ordered_signal_bundle, ())
                assert result.residual_risk is not None
                self.assertEqual(
                    result.residual_risk.code, RefusalCode.VALIDATION_FAILED
                )

    def test_hook_cannot_mutate_top_level_delta_snapshot(self):
        def mutate(bundle: SignalBundle):
            cast(
                MutableMapping[str, object],
                bundle.ordered_signal_bundle[0].bounded_delta,
            )["x"] = 9

        spine = SignalConstraintSpine(validation_hooks={"mutation": mutate})
        result = self.route(spine, hook="mutation")
        self.assertEqual(result.ordered_signal_bundle, ())
        self.assertIsNotNone(result.residual_risk)

    def test_mandatory_checks_run_before_custom_hook_and_preserve_worker_refusal(self):
        called = []

        def validate(bundle):
            called.append(bundle)

        spine = SignalConstraintSpine(validation_hooks={"custom": validate})
        risk = refuse(
            ContractRef.DC04,
            GateRef.VG04,
            RefusalCode.OUTSIDE_LOCAL_SLICE,
            "z outside worker",
        )
        refused = replace(delta_packet(), bounded_delta={}, residual_risk=risk)
        result = self.route(spine, hook="custom", deltas=[delta_packet(), refused])
        self.assertEqual(result.ordered_signal_bundle, ())
        self.assertEqual(result.residual_risk, risk)
        self.assertEqual(called, [])
        oversized = self.route(spine, hook="custom", deltas=[delta_packet(20)])
        self.assertIsNotNone(oversized.residual_risk)
        self.assertEqual(called, [])

    def test_spine_enforces_the_envelope_even_if_worker_limit_is_looser(self):
        result = self.route(
            SignalConstraintSpine(),
            deltas=[delta_packet(1.5)],
            envelope={"max_delta": 1},
        )
        self.assertEqual(result.ordered_signal_bundle, ())
        assert result.residual_risk is not None
        self.assertEqual(result.residual_risk.code, RefusalCode.CONSTRAINT_VIOLATION)

    def test_harness_turns_invalid_solver_input_into_a_refused_bundle(self):
        result = SpinalReconciliationHarness().reconcile(
            worker=VertebraDeltaWorker({"x"}),
            owner="worker:motion",
            channel="motion.delta",
            local_state_slice={"x": 0},
            constraint_set={"max_delta": 2},
            time_packet=cast(TimePacket, 0.04),
            proposed_delta={"x": 1},
            validation_hook="VG03",
        )
        self.assertEqual(result.ordered_signal_bundle, ())
        assert result.residual_risk is not None
        self.assertEqual(result.residual_risk.code, RefusalCode.RAW_DT)


if __name__ == "__main__":
    unittest.main()
