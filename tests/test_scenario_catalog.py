from pathlib import Path
import json
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.scenario_catalog import (  # noqa: E402
    DEFAULT_SCENARIO_ID,
    discover_scenarios,
    get_scenario_record,
    load_scenario_fixture,
    load_scenario_record,
)


class ScenarioCatalogTests(unittest.TestCase):
    def test_repository_fixture_exposes_generic_metadata(self):
        record = get_scenario_record(DEFAULT_SCENARIO_ID)
        self.assertEqual(record.mission, "Apollo 13")
        self.assertEqual(record.runtime_adapter, "pc2_v1")
        self.assertEqual(record.mission_profile_id, "apollo13_h2")
        self.assertEqual(record.model_profile_id, "apollo13_h2_dynamics_partial")
        self.assertEqual(record.scenario_class, "historical_flight_reconstruction")
        self.assertGreater(record.source_count, 0)

        fixture = load_scenario_fixture(record)
        self.assertEqual(fixture["scenario_id"], record.scenario_id)
        self.assertEqual(fixture["title"], record.title)

    def test_unknown_scenario_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown scenario_id"):
            get_scenario_record("does-not-exist")

    def test_duplicate_ids_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            base = {
                "scenario_id": "duplicate",
                "title": "Synthetic duplicate",
                "mission": "Test",
                "status": "test",
                "scenario_class": "test",
                "runtime_adapter": "test_adapter",
                "mission_profile_id": "test_profile",
                "model_profile_id": "test_model_profile",
                "start_get_s": 0,
                "start_get_hms": "00:00:00",
                "end_target_get_hms": "00:01:00",
                "vehicle_configuration": "test",
                "sources": [],
            }
            for name in ("a.json", "b.json"):
                (root / name).write_text(json.dumps(base), encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "duplicate scenario_id"):
                discover_scenarios(root)

    def test_metadata_validation_rejects_missing_runtime_adapter(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text(
                json.dumps(
                    {
                        "scenario_id": "bad",
                        "title": "Bad",
                        "mission": "Test",
                        "status": "test",
                        "scenario_class": "test",
                        "mission_profile_id": "test_profile",
                        "model_profile_id": "test_model_profile",
                        "start_get_s": 0,
                        "start_get_hms": "00:00:00",
                        "end_target_get_hms": "00:01:00",
                        "vehicle_configuration": "test",
                        "sources": [],
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "runtime_adapter"):
                load_scenario_record(path)


if __name__ == "__main__":
    unittest.main()
