import unittest

from spinaltap.contract_kernel import TimePacket
from spinaltap.time_packet import TimePacketPump


class TimePacketPumpTests(unittest.TestCase):
    def test_elapsed_time_becomes_fixed_packets_before_solver_access(self):
        pump = TimePacketPump(fixed_packet_size=0.016, max_packets=4)

        packet = pump.step(elapsed_time=0.040, accumulator_remainder=0.0)

        self.assertIsInstance(packet, TimePacket)
        self.assertEqual(packet.elapsed_time, 0.040)
        self.assertEqual(packet.fixed_packet_size, 0.016)
        self.assertEqual(packet.packet_count, 2)
        self.assertAlmostEqual(packet.accumulator_remainder, 0.008)
        self.assertAlmostEqual(packet.interpolation_state, 0.5)
        self.assertIsNone(packet.overflow_risk)
        self.assertEqual(pump.solver_packets(packet), (0.016, 0.016))

    def test_elapsed_time_over_budget_emits_overflow_risk(self):
        pump = TimePacketPump(fixed_packet_size=0.016, max_packets=4)

        packet = pump.step(elapsed_time=0.200, accumulator_remainder=0.0)

        self.assertEqual(packet.packet_count, 4)
        self.assertEqual(
            packet.overflow_risk,
            "elapsed_time_exceeded_packet_budget",
        )
        self.assertNotIn(packet.elapsed_time, pump.solver_packets(packet))


if __name__ == "__main__":
    unittest.main()
