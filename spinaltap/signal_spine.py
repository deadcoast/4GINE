"""Signal-Constraint Spine specimen for ordered state-change routing."""

from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping
from dataclasses import replace

from spinaltap.contract_kernel import (
    ContractRef,
    DeltaPacket,
    GateRef,
    RefusalCode,
    RefusalState,
    SignalBundle,
    refuse,
)
from spinaltap.contract_validation import ContractValidationError, parse_contract
from spinaltap.time_packet import require_solver_step
from spinaltap.vertebra_delta import constraint_refusal, magnitude_refusal


SignalValidationHook = Callable[[SignalBundle], RefusalState | None]


def _accept_checked_bundle(bundle: SignalBundle) -> None:
    # The mandatory time, ownership, and numeric checks run before any hook.
    return None


class SignalConstraintSpine:
    def __init__(
        self,
        *,
        validation_hooks: Mapping[str, SignalValidationHook] | None = None,
    ) -> None:
        self._validation_hooks: dict[str, SignalValidationHook] = {
            "VG03": _accept_checked_bundle,
        }
        for name, hook in (validation_hooks or {}).items():
            self.register_validation_hook(name, hook)

    def register_validation_hook(self, name: str, hook: SignalValidationHook) -> None:
        if not isinstance(name, str) or not name.strip() or not callable(hook):
            raise ValueError("validation hook requires a nonblank name and callable")
        if name in self._validation_hooks:
            raise ValueError(f"validation hook already registered: {name}")
        self._validation_hooks[name] = hook

    def route(
        self,
        *,
        owner: str,
        channel: str,
        delta_packets: Iterable[DeltaPacket],
        constraint_envelope: Mapping[str, object],
        validation_hook: str,
    ) -> SignalBundle:
        missing = _missing_fields(owner, channel, validation_hook)
        if missing:
            return _refusal_bundle(
                owner=owner,
                channel=channel,
                constraint_envelope=constraint_envelope,
                reason=f"missing signal metadata: {', '.join(missing)}",
            )

        try:
            signals = tuple(delta_packets)
        except TypeError:
            return _refusal_bundle(
                owner=owner,
                channel=channel,
                constraint_envelope=constraint_envelope,
                reason="delta_packets must be an iterable of delta records",
                risk=refuse(
                    ContractRef.DC03,
                    GateRef.VG03,
                    RefusalCode.INVALID_PAYLOAD,
                    "delta_packets must be an iterable of delta records",
                ),
            )
        try:
            bundle = parse_contract(
                ContractRef.DC03,
                {
                    "owner": owner,
                    "channel": channel,
                    "ordered_signal_bundle": signals,
                    "constraint_envelope": constraint_envelope,
                    "validation_hook": validation_hook,
                    "residual_risk": None,
                },
            )
        except ContractValidationError as error:
            return _refusal_bundle(
                owner=owner,
                channel=channel,
                constraint_envelope=constraint_envelope,
                reason=error.refusal.reason,
                risk=error.refusal,
            )
        assert isinstance(bundle, SignalBundle)

        # A custom hook cannot waive the mandatory module boundaries.
        envelope_risk = magnitude_refusal(
            bundle.constraint_envelope,
            {},
            contract=ContractRef.DC03,
        )
        if envelope_risk is not None:
            return _blocked(bundle, envelope_risk)
        for delta in bundle.ordered_signal_bundle:
            if delta.residual_risk is not None:
                return _blocked(bundle, delta.residual_risk)
            try:
                require_solver_step(delta.time_packet)
            except ContractValidationError as error:
                return _blocked(bundle, error.refusal)
            risk = constraint_refusal(delta)
            if risk is not None:
                return _blocked(bundle, risk)
            risk = magnitude_refusal(
                bundle.constraint_envelope,
                delta.bounded_delta,
                contract=ContractRef.DC03,
            )
            if risk is not None:
                return _blocked(
                    bundle,
                    refuse(
                        ContractRef.DC03,
                        GateRef.VG03,
                        risk.code,
                        f"constraint_envelope: {risk.reason}",
                    ),
                )

        hook = self._validation_hooks.get(validation_hook)
        if hook is None:
            return _hook_failed(bundle, f"unknown validation hook: {validation_hook}")
        try:
            risk = hook(bundle)
        except Exception as error:
            return _hook_failed(
                bundle,
                f"validation hook {validation_hook} raised {type(error).__name__}",
            )
        if risk is None:
            return bundle
        if not isinstance(risk, RefusalState):
            return _hook_failed(
                bundle, "validation hook must return None or RefusalState"
            )
        try:
            checked = parse_contract(ContractRef.DC03, _blocked(bundle, risk))
        except ContractValidationError:
            return _hook_failed(
                bundle, "validation hook returned malformed refusal metadata"
            )
        assert isinstance(checked, SignalBundle)
        return checked

    def publish_direct(
        self,
        *,
        owner: str,
        channel: str,
        global_mutation: Mapping[str, object],
    ) -> SignalBundle:
        return _refusal_bundle(
            owner=owner,
            channel=channel,
            constraint_envelope={"global_mutation": dict(global_mutation)},
            reason="direct global mutation refused before aggregation",
        )


def _missing_fields(owner: str, channel: str, validation_hook: str) -> tuple[str, ...]:
    missing: list[str] = []
    if not isinstance(owner, str) or not owner.strip():
        missing.append("owner")
    if not isinstance(channel, str) or not channel.strip():
        missing.append("channel")
    if not isinstance(validation_hook, str) or not validation_hook.strip():
        missing.append("validation hook")
    return tuple(missing)


def _refusal_bundle(
    *,
    owner: str,
    channel: str,
    constraint_envelope: Mapping[str, object],
    reason: str,
    risk: RefusalState | None = None,
) -> SignalBundle:
    return SignalBundle(
        owner=owner if isinstance(owner, str) else "",
        channel=channel if isinstance(channel, str) else "",
        ordered_signal_bundle=(),
        constraint_envelope=(
            dict(constraint_envelope)
            if isinstance(constraint_envelope, Mapping)
            else {}
        ),
        validation_hook="VG03",
        residual_risk=risk
        or refuse(
            ContractRef.DC03,
            GateRef.VG03,
            RefusalCode.DIRECT_GLOBAL_MUTATION,
            reason,
        ),
    )


def _blocked(bundle: SignalBundle, risk: RefusalState) -> SignalBundle:
    return replace(bundle, ordered_signal_bundle=(), residual_risk=risk)


def _hook_failed(bundle: SignalBundle, reason: str) -> SignalBundle:
    return _blocked(
        bundle,
        refuse(
            ContractRef.DC03,
            GateRef.VG03,
            RefusalCode.VALIDATION_FAILED,
            reason,
        ),
    )
