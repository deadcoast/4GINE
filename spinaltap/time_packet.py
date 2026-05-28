"""Time Packet Pump specimen for fixed solver-facing time packets."""

from __future__ import annotations

from spinaltap.contract_kernel import TimePacket


class TimePacketPump:
    def __init__(self, fixed_packet_size: float, max_packets: int) -> None:
        if fixed_packet_size <= 0:
            raise ValueError("fixed_packet_size must be positive")
        if max_packets < 1:
            raise ValueError("max_packets must be at least one")
        self.fixed_packet_size = fixed_packet_size
        self.max_packets = max_packets

    def step(
        self,
        *,
        elapsed_time: float,
        accumulator_remainder: float,
    ) -> TimePacket:
        accumulated = elapsed_time + accumulator_remainder
        requested_packets = int(accumulated // self.fixed_packet_size)
        packet_count = min(requested_packets, self.max_packets)
        consumed = packet_count * self.fixed_packet_size
        remainder = max(0.0, accumulated - consumed)
        overflow_risk = None

        if requested_packets > self.max_packets:
            overflow_risk = "elapsed_time_exceeded_packet_budget"

        interpolation_state = min(1.0, remainder / self.fixed_packet_size)

        return TimePacket(
            elapsed_time=elapsed_time,
            fixed_packet_size=self.fixed_packet_size,
            packet_count=packet_count,
            accumulator_remainder=remainder,
            interpolation_state=interpolation_state,
            overflow_risk=overflow_risk,
        )

    def solver_packets(self, packet: TimePacket) -> tuple[float, ...]:
        return (float(packet.fixed_packet_size),) * int(packet.packet_count)
