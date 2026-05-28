import unittest

from spinaltap.contract_kernel import (
    DeltaPacket,
    RefusalCode,
    RefusalState,
    SignalBundle,
    TimePacket,
)
from spinaltap.signal_spine import SignalConstraintSpine


class SignalConstraintSpineTests(unittest.TestCase):
    def test_bounded_delta_routes_through_ordered_signal_bundle(self):
        spine = SignalConstraintSpine()
        delta = self._delta({"x": 1})

        bundle = spine.route(
            owner="vertebra:motion",
            channel="motion.delta",
            delta_packets=[delta],
            constraint_envelope={"max_delta": 2},
            validation_hook="VG03",
        )

        self.assertIsInstance(bundle, SignalBundle)
        self.assertEqual(bundle.owner, "vertebra:motion")
        self.assertEqual(bundle.channel, "motion.delta")
        self.assertEqual(bundle.ordered_signal_bundle, (delta,))
        self.assertEqual(bundle.constraint_envelope, {"max_delta": 2})
        self.assertEqual(bundle.validation_hook, "VG03")
        self.assertIsNone(bundle.residual_risk)

    def test_missing_validation_hook_is_refused_before_aggregation(self):
        spine = SignalConstraintSpine()

        bundle = spine.route(
            owner="vertebra:motion",
            channel="motion.delta",
            delta_packets=[self._delta({"x": 1})],
            constraint_envelope={"max_delta": 2},
            validation_hook="",
        )

        self.assertEqual(bundle.ordered_signal_bundle, ())
        risk = bundle.residual_risk
        assert isinstance(risk, RefusalState)
        self.assertEqual(
            risk.code,
            RefusalCode.DIRECT_GLOBAL_MUTATION,
        )
        self.assertIn("validation hook", risk.reason)

    def test_direct_global_mutation_is_refused_before_aggregation(self):
        spine = SignalConstraintSpine()

        bundle = spine.publish_direct(
            owner="vertebra:motion",
            channel="motion.delta",
            global_mutation={"world.x": 1},
        )

        self.assertEqual(bundle.ordered_signal_bundle, ())
        risk = bundle.residual_risk
        assert isinstance(risk, RefusalState)
        self.assertEqual(
            risk.code,
            RefusalCode.DIRECT_GLOBAL_MUTATION,
        )
        self.assertIn("direct global mutation", risk.reason)

    def _delta(self, bounded_delta):
        return DeltaPacket(
            local_state_slice={"x": 4},
            constraint_set={"max_delta": 2},
            time_packet=TimePacket(
                elapsed_time=0.016,
                fixed_packet_size=0.016,
                packet_count=1,
                accumulator_remainder=0.0,
                interpolation_state=0.0,
                overflow_risk=None,
            ),
            bounded_delta=bounded_delta,
            residual_risk=None,
        )


if __name__ == "__main__":
    unittest.main()
