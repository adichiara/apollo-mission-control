from math import tau
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.landing_radar_profiles import get_landing_radar_profile  # noqa: E402


class LandingRadarProfileTests(unittest.TestCase):
    def test_apollo11_profile_builds_historical_velocity_weight_config(self):
        profile = get_landing_radar_profile("apollo11_lm5_landing_radar_partial")
        self.assertEqual(profile.mission_profile_id, "apollo11_g")
        config = profile.velocity_update_config().validated()
        self.assertAlmostEqual(config.maximum_speed_m_s, 609.6)
        self.assertAlmostEqual(config.low_speed_threshold_m_s, 60.96)
        self.assertEqual(config.linear_component_weights, {"z": 0.3, "y": 0.3, "x": 0.3})
        self.assertEqual(config.low_speed_component_weights, {"z": 0.2, "y": 0.2, "x": 0.2})
        self.assertEqual(config.override_programs, ("P65", "P66", "P67"))
        self.assertEqual(config.override_weight, 0.1)

    def test_apollo11_profile_adapts_source_geometry_without_manual_transcription(self):
        profile = get_landing_radar_profile("apollo11_lm5_landing_radar_partial")
        p1 = profile.beam_geometry(1, cdu_y_rad=0.1, cdu_z_rad=0.2, cdu_x_rad=0.3)
        p2 = profile.beam_geometry(2, cdu_y_rad=0.1, cdu_z_rad=0.2, cdu_x_rad=0.3)
        self.assertAlmostEqual(p1.alpha_rad, 0.0163371759 * tau)
        self.assertAlmostEqual(p1.beta_rad, 0.0665287037 * tau)
        self.assertAlmostEqual(p2.alpha_rad, 0.0161680555 * tau)
        self.assertAlmostEqual(p2.beta_rad, 0.0001361111 * tau)
        self.assertEqual((p1.cdu_y_rad, p1.cdu_z_rad, p1.cdu_x_rad), (0.1, 0.2, 0.3))
        with self.assertRaises(ValueError):
            profile.beam_geometry(3, cdu_y_rad=0, cdu_z_rad=0, cdu_x_rad=0)

    def test_apollo11_profile_exposes_historical_data_good_transitions(self):
        profile = get_landing_radar_profile("apollo11_lm5_landing_radar_partial")
        self.assertEqual(profile.data_good_min_duration_s, 4.0)
        self.assertEqual(
            [(item.time_s, item.data_good) for item in profile.historical_data_good_transitions],
            [
                (369851.0, False),
                (369861.0, True),
                (369899.0, False),
                (369903.0, True),
            ],
        )
        self.assertTrue(
            all(item.source_resolution_s == 1.0 for item in profile.historical_data_good_transitions)
        )

    def test_profile_public_metadata_preserves_current_boundary(self):
        profile = get_landing_radar_profile("apollo11_lm5_landing_radar_partial")
        public = profile.to_public_dict()
        weighting = public["velocity_update_weighting"]
        self.assertEqual(weighting["maximum_speed_fps"], 2000.0)
        self.assertIn("P66", weighting["override_programs"])
        geometry = public["landing_radar_geometry"]
        self.assertEqual(geometry["positions"]["1"]["name"], "stow")
        self.assertEqual(geometry["positions"]["2"]["name"], "hover")
        self.assertFalse(any("PIPA/gravity propagation" in item for item in public["unresolved"]))
        self.assertTrue(any("stochastic" in item for item in public["unresolved"]))


if __name__ == "__main__":
    unittest.main()
