from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.landing_radar_profiles import (  # noqa: E402
    get_landing_radar_profile,
)


class LandingRadarProfileTests(unittest.TestCase):
    def test_apollo11_profile_builds_historical_velocity_weight_config(self):
        profile = get_landing_radar_profile("apollo11_lm5_landing_radar_partial")
        self.assertEqual(profile.mission_profile_id, "apollo11_g")
        self.assertIsNotNone(profile.velocity_weighting)

        config = profile.velocity_update_config().validated()
        self.assertAlmostEqual(config.maximum_speed_m_s, 609.6)
        self.assertAlmostEqual(config.low_speed_threshold_m_s, 60.96)
        self.assertEqual(config.linear_component_weights, {"z": 0.3, "y": 0.3, "x": 0.3})
        self.assertEqual(config.low_speed_component_weights, {"z": 0.2, "y": 0.2, "x": 0.2})
        self.assertEqual(config.override_programs, ("P65", "P66", "P67"))
        self.assertEqual(config.override_weight, 0.1)

    def test_profile_public_metadata_preserves_source_units_and_unresolved_boundary(self):
        profile = get_landing_radar_profile("apollo11_lm5_landing_radar_partial")
        public = profile.to_public_dict()
        weighting = public["velocity_update_weighting"]
        self.assertEqual(weighting["maximum_speed_fps"], 2000.0)
        self.assertEqual(weighting["low_speed_threshold_fps"], 200.0)
        self.assertIn("P66", weighting["override_programs"])
        self.assertTrue(
            any("PIPA/gravity propagation" in item for item in public["unresolved"])
        )


if __name__ == "__main__":
    unittest.main()
