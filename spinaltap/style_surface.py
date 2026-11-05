"""Style Constraint Surface specimen for measurable visual limits."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from spinaltap.contract_kernel import (
    ContractRef,
    GateRef,
    RefusalCode,
    RefusalState,
    StyleLimits,
    refuse,
)
from spinaltap.contract_validation import ContractValidationError, parse_contract


_STYLE_LIMIT_FIELDS = StyleLimits.fields()


@dataclass(frozen=True)
class StyleSurfaceResult:
    limits: StyleLimits | None
    refusal: RefusalState | None


class StyleConstraintSurface:
    def translate(self, profile: object) -> StyleSurfaceResult:
        missing = ()
        if isinstance(profile, Mapping):
            missing = tuple(
                field
                for field in _STYLE_LIMIT_FIELDS
                if field not in profile
                or (isinstance(profile[field], str) and not profile[field].strip())
            )
        if missing:
            return StyleSurfaceResult(
                limits=None,
                refusal=refuse(
                    ContractRef.DC05,
                    GateRef.VG05,
                    RefusalCode.VAGUE_STYLE,
                    f"style profile missing measurable limits: {', '.join(missing)}",
                ),
            )

        try:
            limits = parse_contract(ContractRef.DC05, profile)
        except ContractValidationError as error:
            return StyleSurfaceResult(limits=None, refusal=error.refusal)
        assert isinstance(limits, StyleLimits)
        return StyleSurfaceResult(limits=limits, refusal=None)
