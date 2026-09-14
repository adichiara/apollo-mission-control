from pathlib import Path
import json
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.guidance_monitoring_profiles import (  # noqa: E402
    discover_guidance_monitoring_profiles,
    get_guidance_monitoring_profile,
    load_guidance_monitoring_profile,
)


class GuidanceMonitoringProfileTests(unittest.TestCase):
    def test_apollo11_profile_preserves_sourced_fields_and_limits(self):
        profile = get_guidance_monitoring_profile(
            "apollo11_g_powered_descent_monitoring_partial"
        )
        self.assertEqual(profile.mission_profile_id, "apollo11_g")

        isolation = profile.comparison("ags_pgns_inplane_problem_detection")
        self.assertEqual(
            isolation.tolerances,
            {
                "radial_velocity_fps": 10.0,
                "downrange_velocity_fps": 10.0,
            },
        )

        failure = profile.comparison("pfp_pgns_pgns_failure_limits")
        self.assertEqual(failure.tolerances["radial_velocity_fps"], 35.0)
        self.assertEqual(failure.tolerances["downrange_velocity_fps"], 30.0)

        crossrange = profile.comparison("ags_pgns_crossrange_problem_detection")
        self.assertEqual(crossrange.tolerances["crossrange_velocity_fps"], 20.0)

    def test_unresolved_freshness_blocks_historical_execution(self):
        profile = get_guidance_monitoring_profile(
            "apollo11_g_powered_descent_monitoring_partial"
        )
        for comparison in profile.comparisons:
            self.assertFalse(comparison.historically_executable)
            with self.assertRaisesRegex(ValueError, "freshness is unresolved"):
                comparison.to_crosscheck_config()

    def test_resolved_synthetic_profile_can_build_generic_crosscheck_config(self):
        payload = {
            "profile_id": "synthetic",
            "mission_profile_id": "synthetic",
            "status": "test",
            "applicability": "synthetic test",
            "comparisons": [
                {
                    "comparison_id": "pair",
                    "first_source": "A",
                    "second_source": "B",
                    "purpose": "test",
                    "tolerances": {"velocity": 2.0},
                    "max_time_separation_s": 1.5,
                    "provenance": ["synthetic"],
                    "evidence_note": "synthetic",
                }
            ],
            "unresolved": [],
            "sources": ["synthetic"],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "profile.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            profile = load_guidance_monitoring_profile(path)

        config = profile.comparison("pair").to_crosscheck_config()
        self.assertEqual(config.tolerances["velocity"], 2.0)
        self.assertEqual(config.max_time_separation_s, 1.5)

    def test_duplicate_comparison_ids_are_rejected(self):
        payload = {
            "profile_id": "bad",
            "mission_profile_id": "synthetic",
            "status": "test",
            "applicability": "test",
            "comparisons": [
                {
                    "comparison_id": "same",
                    "first_source": "A",
                    "second_source": "B",
                    "purpose": "test",
                    "tolerances": {"x": 1},
                    "max_time_separation_s": 1,
                    "provenance": [],
                    "evidence_note": "test",
                },
                {
                    "comparison_id": "same",
                    "first_source": "C",
                    "second_source": "D",
                    "purpose": "test",
                    "tolerances": {"x": 1},
                    "max_time_separation_s": 1,
                    "provenance": [],
                    "evidence_note": "test",
                },
            ],
            "unresolved": [],
            "sources": [],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate"):
                load_guidance_monitoring_profile(path)

    def test_profile_discovery_is_unique(self):
        records = discover_guidance_monitoring_profiles()
        ids = [record.profile_id for record in records]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertIn("apollo11_g_powered_descent_monitoring_partial", ids)


if __name__ == "__main__":
    unittest.main()
