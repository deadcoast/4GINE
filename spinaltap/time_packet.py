"""Time Packet Pump specimen for fixed solver-facing time packets."""

from __future__ import annotations

from math import isfinite, ulp

from spinaltap.contract_kernel import ContractRef, RefusalCode, TimePacket
from spinaltap.contract_validation import ContractValidationError, parse_contract


MAX_PACKET_BUDGET = 4096


def _invalid(field: str, reason: str) -> ContractValidationError:
    return ContractValidationError(ContractRef.DC02, f"DC02.{field}", reason)


def _nonnegative_number(value: object, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (float, int)):
        raise _invalid(field, "expected a finite nonnegative number")
    try:
        number = float(value)
    except OverflowError:
        raise _invalid(field, "number is too large") from None
    if not isfinite(number) or number < 0:
        raise _invalid(field, "expected a finite nonnegative number")
    return number


def _checked_packet(packet: object) -> TimePacket:
    if not isinstance(packet, TimePacket):
        raise ContractValidationError(
            ContractRef.DC02,
            "DC02.time_packet",
            "raw time is not a solver packet; convert it with TimePacketPump",
            code=RefusalCode.RAW_DT,
        )
    checked = parse_contract(ContractRef.DC02, packet)
    assert isinstance(checked, TimePacket)
    return checked


def require_solver_step(packet: object) -> TimePacket:
    """Require one fixed step with no render-frame timing or pending backlog."""
    checked = _checked_packet(packet)
    if (
        checked.packet_count != 1
        or checked.elapsed_time != checked.fixed_packet_size
        or checked.accumulator_remainder != 0
        or checked.interpolation_state != 0
        or checked.overflow_risk is not None
    ):
        raise _invalid(
            "time_packet", "worker requires one fixed step; use pump.solver_steps"
        )
    return checked


class TimePacketPump:
    def __init__(self, fixed_packet_size: float, max_packets: int) -> None:
        size = _nonnegative_number(fixed_packet_size, "fixed_packet_size")
        if size == 0:
            raise _invalid("fixed_packet_size", "must be positive")
        if (
            isinstance(max_packets, bool)
            or not isinstance(max_packets, int)
            or not 1 <= max_packets <= MAX_PACKET_BUDGET
        ):
            raise _invalid(
                "max_packets", f"expected an integer in 1..{MAX_PACKET_BUDGET}"
            )
        self.fixed_packet_size = size
        self.max_packets = max_packets

    def step(
        self,
        *,
        elapsed_time: float,
        accumulator_remainder: float,
    ) -> TimePacket:
        elapsed_time = _nonnegative_number(elapsed_time, "elapsed_time")
        accumulator_remainder = _nonnegative_number(
            accumulator_remainder, "accumulator_remainder"
        )
        accumulated = elapsed_time + accumulator_remainder
        if not isfinite(accumulated):
            raise _invalid("accumulator_remainder", "accumulated time overflowed")
        requested_packets, fractional = divmod(accumulated, self.fixed_packet_size)
        # Binary float division can put an exact decimal boundary one step low.
        # Snap only within four ULPs, and only when this affects the emitted count.
        tolerance = min(
            4 * max(ulp(accumulated), ulp(self.fixed_packet_size)),
            self.fixed_packet_size * 1e-9,
        )
        if (
            requested_packets <= self.max_packets
            and fractional > 0
            and self.fixed_packet_size - fractional <= tolerance
        ):
            requested_packets += 1
        packet_count = (
            self.max_packets
            if requested_packets >= self.max_packets
            else int(requested_packets)
        )
        consumed = packet_count * self.fixed_packet_size
        if not isfinite(consumed):
            raise _invalid("fixed_packet_size", "consumed time overflowed")
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
        """Compatibility projection; workers should receive solver_steps records."""
        return tuple(step.fixed_packet_size for step in self.solver_steps(packet))

    def solver_steps(self, packet: TimePacket) -> tuple[TimePacket, ...]:
        checked = _checked_packet(packet)
        if checked.fixed_packet_size != self.fixed_packet_size:
            raise _invalid(
                "fixed_packet_size", "packet belongs to a different fixed timestep"
            )
        if checked.packet_count > self.max_packets:
            raise _invalid(
                "packet_count", "packet exceeds this pump's execution budget"
            )
        step = TimePacket(
            self.fixed_packet_size, self.fixed_packet_size, 1, 0.0, 0.0, None
        )
        return (step,) * checked.packet_count
