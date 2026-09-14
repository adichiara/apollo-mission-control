from pathlib import Path
import json
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.model_profiles import (  # noqa: E402
    assess_model_readiness,
    discover_model_profiles,
    get_model_profile,
    load_model_profile_record,
)


class ModelProfileTests(unittest.TestCase):
    def test_repository_profile_keeps_unresolved_domains_explicit(self):
        profile = get_model_profile("apollo13_h2_dynamics_partial")

        self.assertEqual(profile.mission_profile_id, "apollo13_h2")
        self.assertEqual(
            profile.validation_state,
            "not_historically_validated",
        )
        self.assertEqual(profile.domains["mass_properties"].status, "partial")
        self.assertEqual(profile.domains["propulsion"].status, "partial")
        self.assertEqual(
            profile.domains["translational_dynamics"].status,
            "unresolved",
        )
        self.assertEqual(
            profile.domains["tracking_observation"].status,
            "unresolved",
        )
        self.assertGreater(profile.source_count, 0)

    def test_readiness_is_scenario_specific_and_explicit(self):
        profile = get_model_profile("apollo13_h2_dynamics_partial")
        readiness = assess_model_readiness(
            profile,
            (
                "mass_properties",
                "propulsion",
                "translational_dynamics",
                "tracking_observation",
            ),
        )

        self.assertFalse(readiness.historical_validation_ready)
        self.assertEqual(readiness.missing_domains, ())
        self.assertEqual(
            readiness.unvalidated_domains,
            (
                "mass_properties",
                "propulsion",
                "translational_dynamics",
                "tracking_observation",
            ),
        )
        self.assertEqual(readiness.domain_statuses["propulsion"], "partial")
        self.assertEqual(
            readiness.domain_statuses["translational_dynamics"],
            "unresolved",
        )

    def test_readiness_reports_missing_required_domain(self):
        profile = get_model_profile("apollo13_h2_dynamics_partial")
        readiness = assess_model_readiness(
            profile,
            ("propulsion", "not_in_profile"),
        )

        self.assertFalse(readiness.historical_validation_ready)
        self.assertEqual(readiness.missing_domains, ("not_in_profile",))
        self.assertEqual(readiness.domain_statuses["not_in_profile"], "missing")

    def test_unknown_profile_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown model_profile_id"):
            get_model_profile("does-not-exist")

    def test_duplicate_profile_ids_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            base = {
                "model_profile_id": "duplicate",
                "mission_profile_id": "test_mission",
                "status": "test",
                "validation_state": "not_historically_validated",
                "domains": {
                    "test": {
                        "status": "unresolved",
                        "note": "synthetic test",
                    }
                },
                "sources": [],
            }
            for name in ("a.json", "b.json"):
                (root / name).write_text(json.dumps(base), encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "duplicate model_profile_id"):
                discover_model_profiles(root)

    def test_invalid_domain_status_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text(
                json.dumps(
                    {
                        "model_profile_id": "bad",
                        "mission_profile_id": "test_mission",
                        "status": "test",
                        "validation_state": "test",
                        "domains": {
                            "propulsion": {
                                "status": "guessed",
                                "note": "not allowed",
                            }
                        },
                        "sources": [],
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "invalid status"):
                load_model_profile_record(path)


if __name__ == "__main__":
    unittest.main()
