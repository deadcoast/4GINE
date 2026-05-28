import unittest

from spinaltap.contract_kernel import RefusalCode, RefusalState, SignalBundle, TimePacket
from spinaltap.reconciliation import SpinalReconciliationHarness
from spinaltap.vertebra_delta import VertebraDeltaWorker


class SpinalReconciliationHarnessTests(unittest.TestCase):
    def test_worker_delta_is_ordered_through_signal_spine(self):
        harness = SpinalReconciliationHarness()
        worker = VertebraDeltaWorker(local_keys={"x", "y"})

        bundle = harness.reconcile(
            worker=worker,
            owner="vertebra:motion",
            channel="motion.delta",
            local_state_slice={"x": 4, "y": 8},
            constraint_set={"max_delta": 2},
            time_packet=self._time_packet(),
            proposed_delta={"x": 1},
            validation_hook="VG03",
        )

        self.assertIsInstance(bundle, SignalBundle)
        self.assertEqual(bundle.owner, "vertebra:motion")
        self.assertEqual(bundle.channel, "motion.delta")
        self.assertEqual(len(bundle.ordered_signal_bundle), 1)
        self.assertEqual(bundle.ordered_signal_bundle[0].bounded_delta, {"x": 1})
        self.assertIsNone(bundle.residual_risk)

    def test_worker_refusal_stops_before_signal_aggregation(self):
        harness = SpinalReconciliationHarness()
        worker = VertebraDeltaWorker(local_keys={"x", "y"})

        bundle = harness.reconcile(
            worker=worker,
            owner="vertebra:motion",
            channel="motion.delta",
            local_state_slice={"x": 4, "y": 8},
            constraint_set={"max_delta": 2},
            time_packet=self._time_packet(),
            proposed_delta={"z": 1},
            validation_hook="VG03",
        )

        self.assertEqual(bundle.ordered_signal_bundle, ())
        risk = bundle.residual_risk
        assert isinstance(risk, RefusalState)
        self.assertEqual(risk.code, RefusalCode.OUTSIDE_LOCAL_SLICE)
        self.assertIn("z", risk.reason)

    def _time_packet(self):
        return TimePacket(
            elapsed_time=0.016,
            fixed_packet_size=0.016,
            packet_count=1,
            accumulator_remainder=0.0,
            interpolation_state=0.0,
            overflow_risk=None,
        )


if __name__ == "__main__":
    unittest.main()
