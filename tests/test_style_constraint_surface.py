import unittest

from spinaltap.contract_kernel import RefusalCode, RefusalState, StyleLimits
from spinaltap.style_surface import StyleConstraintSurface


class StyleConstraintSurfaceTests(unittest.TestCase):
    def test_style_profile_becomes_measurable_limits(self):
        surface = StyleConstraintSurface()

        result = surface.translate(
            {
                "geometry_limit": "low_poly_budget:1200",
                "lighting_limit": "single_key_plus_ambient",
                "texture_limit": "nearest_64px",
                "color_limit": "indexed_32",
                "fog_limit": "linear_depth_band",
                "alpha_limit": "binary_cutout",
                "depth_limit": "fixed_near_far",
                "camera_limit": "locked_pitch",
                "animation_cadence": "12fps_step",
                "artifact_limits": "dither_allowed_no_smear",
            }
        )

        limits = result.limits
        assert isinstance(limits, StyleLimits)
        self.assertEqual(limits.geometry_limit, "low_poly_budget:1200")
        self.assertEqual(limits.texture_limit, "nearest_64px")
        self.assertEqual(limits.artifact_limits, "dither_allowed_no_smear")
        self.assertIsNone(result.refusal)

    def test_vague_style_profile_is_refused(self):
        surface = StyleConstraintSurface()

        result = surface.translate({"mood": "retro and crunchy"})

        self.assertIsNone(result.limits)
        refusal = result.refusal
        assert isinstance(refusal, RefusalState)
        self.assertEqual(refusal.code, RefusalCode.VAGUE_STYLE)
        self.assertIn("geometry_limit", refusal.reason)


if __name__ == "__main__":
    unittest.main()
