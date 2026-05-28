import unittest

from spinaltap.contract_kernel import (
    DeltaPacket,
    RefusalCode,
    RefusalState,
    TimePacket,
)
from spinaltap.vertebra_delta import VertebraDeltaWorker


class VertebraDeltaWorkerTests(unittest.TestCase):
    def test_worker_emits_bounded_delta_for_declared_local_slice(self):
        worker = VertebraDeltaWorker(local_keys={"x", "y"})
        time_packet = TimePacket(
            elapsed_time=0.016,
            fixed_packet_size=0.016,
            packet_count=1,
            accumulator_remainder=0.0,
            interpolation_state=0.0,
            overflow_risk=None,
        )

        delta = worker.propose(
            local_state_slice={"x": 4, "y": 8},
            constraint_set={"max_delta": 2},
            time_packet=time_packet,
            proposed_delta={"x": 1},
        )

        self.assertIsInstance(delta, DeltaPacket)
        self.assertEqual(delta.local_state_slice, {"x": 4, "y": 8})
        self.assertEqual(delta.constraint_set, {"max_delta": 2})
        self.assertEqual(delta.time_packet, time_packet)
        self.assertEqual(delta.bounded_delta, {"x": 1})
        self.assertIsNone(delta.residual_risk)

    def test_worker_refuses_delta_outside_declared_local_slice(self):
        worker = VertebraDeltaWorker(local_keys={"x", "y"})
        time_packet = TimePacket(
            elapsed_time=0.016,
            fixed_packet_size=0.016,
            packet_count=1,
            accumulator_remainder=0.0,
            interpolation_state=0.0,
            overflow_risk=None,
        )

        delta = worker.propose(
            local_state_slice={"x": 4, "y": 8},
            constraint_set={"max_delta": 2},
            time_packet=time_packet,
            proposed_delta={"z": 1},
        )

        self.assertEqual(delta.bounded_delta, {})
        risk = delta.residual_risk
        assert isinstance(risk, RefusalState)
        self.assertEqual(
            risk.code,
            RefusalCode.OUTSIDE_LOCAL_SLICE,
        )
        self.assertIn("z", risk.reason)


if __name__ == "__main__":
    unittest.main()
