from pathlib import Path
import json
import math
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.landing_radar_geometry import (  # noqa: E402
    LandingRadarAntennaOrientation,
    compute_landing_radar_antenna_geometry,
)


class LandingRadarAntennaGeometryTests(unittest.TestCase):
    def test_zero_angles_produce_identity_axes(self):
        result = compute_landing_radar_antenna_geometry(
            LandingRadarAntennaOrientation(
                lralpha_revolutions=0.0,
                lrbeta_revolutions=0.0,
            )
        )
        self.assertEqual(result.x_axis_navigation_base, (1.0, 0.0, 0.0))
        self.assertEqual(result.y_axis_navigation_base, (0.0, 1.0, 0.0))
        self.assertEqual(result.z_axis_navigation_base, (0.0, 0.0, 1.0))

    def test_beta_then_alpha_matrix_matches_closed_form(self):
        alpha = 0.1
        beta = -0.07
        result = compute_landing_radar_antenna_geometry(
            LandingRadarAntennaOrientation(
                lralpha_revolutions=alpha / (2.0 * math.pi),
                lrbeta_revolutions=beta / (2.0 * math.pi),
            )
        )

        ca, sa = math.cos(alpha), math.sin(alpha)
        cb, sb = math.cos(beta), math.sin(beta)
        expected = (
            (cb, 0.0, sb),
            (sa * sb, ca, -sa * cb),
            (-ca * sb, sa, ca * cb),
        )
        for actual_row, expected_row in zip(
            result.antenna_to_navigation_base,
            expected,
        ):
            for actual, wanted in zip(actual_row, expected_row):
                self.assertAlmostEqual(actual, wanted, places=14)

    def test_axes_are_orthonormal_and_right_handed(self):
        result = compute_landing_radar_antenna_geometry(
            LandingRadarAntennaOrientation(
                lralpha_revolutions=0.0163371759,
                lrbeta_revolutions=0.0665287037,
            )
        )
        x = result.x_axis_navigation_base
        y = result.y_axis_navigation_base
        z = result.z_axis_navigation_base

        def dot(a, b):
            return sum(left * right for left, right in zip(a, b))

        def norm(v):
            return math.sqrt(dot(v, v))

        cross_xy = (
            x[1] * y[2] - x[2] * y[1],
            x[2] * y[0] - x[0] * y[2],
            x[0] * y[1] - x[1] * y[0],
        )
        for axis in (x, y, z):
            self.assertAlmostEqual(norm(axis), 1.0, places=14)
        self.assertAlmostEqual(dot(x, y), 0.0, places=14)
        self.assertAlmostEqual(dot(x, z), 0.0, places=14)
        self.assertAlmostEqual(dot(y, z), 0.0, places=14)
        for actual, wanted in zip(cross_xy, z):
            self.assertAlmostEqual(actual, wanted, places=14)

    def test_lm5_profile_preserves_source_padloads(self):
        profile = json.loads(
            (
                ROOT
                / "data"
                / "landing_radar_profiles"
                / "apollo11_lm5_landing_radar_partial.json"
            ).read_text(encoding="utf-8")
        )
        orientations = profile["antenna_orientation"]["positions"]

        self.assertEqual(
            orientations["position_1_stow"]["lralpha_rev"],
            0.0163371759,
        )
        self.assertEqual(
            orientations["position_1_stow"]["lrbeta_rev"],
            0.0665287037,
        )
        self.assertEqual(
            orientations["position_2_hover"]["lralpha_rev"],
            0.0161680555,
        )
        self.assertEqual(
            orientations["position_2_hover"]["lrbeta_rev"],
            0.0001361111,
        )

    def test_lm5_stow_axes_have_expected_numeric_result(self):
        result = compute_landing_radar_antenna_geometry(
            LandingRadarAntennaOrientation(
                lralpha_revolutions=0.0163371759,
                lrbeta_revolutions=0.0665287037,
                position="position_1_stow",
            )
        )
        expected_x = (
            0.913897692761,
            0.041596869878,
            -0.403807760677,
        )
        for actual, wanted in zip(result.x_axis_navigation_base, expected_x):
            self.assertAlmostEqual(actual, wanted, places=11)

    def test_unknown_axis_is_rejected(self):
        result = compute_landing_radar_antenna_geometry(
            LandingRadarAntennaOrientation(
                lralpha_revolutions=0.0,
                lrbeta_revolutions=0.0,
            )
        )
        with self.assertRaisesRegex(ValueError, "unknown landing-radar antenna axis"):
            result.axis("q")


if __name__ == "__main__":
    unittest.main()
