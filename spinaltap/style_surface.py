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


_STYLE_LIMIT_FIELDS = StyleLimits.fields()


@dataclass(frozen=True)
class StyleSurfaceResult:
    limits: StyleLimits | None
    refusal: RefusalState | None


class StyleConstraintSurface:
    def translate(self, profile: Mapping[str, str]) -> StyleSurfaceResult:
        missing = tuple(field for field in _STYLE_LIMIT_FIELDS if not profile.get(field))
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

        return StyleSurfaceResult(
            limits=StyleLimits(
                geometry_limit=profile["geometry_limit"],
                lighting_limit=profile["lighting_limit"],
                texture_limit=profile["texture_limit"],
                color_limit=profile["color_limit"],
                fog_limit=profile["fog_limit"],
                alpha_limit=profile["alpha_limit"],
                depth_limit=profile["depth_limit"],
                camera_limit=profile["camera_limit"],
                animation_cadence=profile["animation_cadence"],
                artifact_limits=profile["artifact_limits"],
            ),
            refusal=None,
        )
