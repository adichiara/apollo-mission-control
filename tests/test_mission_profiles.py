from pathlib import Path
import json
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.mission_profiles import (  # noqa: E402
    discover_mission_profiles,
    get_mission_profile,
    load_mission_profile_record,
)


class MissionProfileTests(unittest.TestCase):
    def test_repository_profiles_preserve_known_mission_differences(self):
        profiles = {
            record.mission_profile_id: record
            for record in discover_mission_profiles()
        }
        self.assertIn("apollo11_g", profiles)
        self.assertIn("apollo13_h2", profiles)

        ap11 = profiles["apollo11_g"]
        ap13 = profiles["apollo13_h2"]

        self.assertEqual(ap11.mission, "Apollo 11")
        self.assertEqual(ap11.launch_vehicle, "AS-506")
        self.assertEqual(ap11.spacecraft["lm"], "LM-5")
        self.assertEqual(ap11.controller_nomenclature["lm_systems"], "TELCOM")

        self.assertEqual(ap13.mission, "Apollo 13")
        self.assertEqual(ap13.launch_vehicle, "AS-508")
        self.assertEqual(ap13.spacecraft["lm"], "LM-7")
        self.assertEqual(
            ap13.controller_nomenclature["lm_electrical_environmental_emu"],
            "TELMU",
        )

    def test_unknown_profile_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown mission_profile_id"):
            get_mission_profile("does-not-exist")

    def test_duplicate_profile_ids_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            base = {
                "mission_profile_id": "duplicate",
                "mission": "Test",
                "mission_designation": "T",
                "status": "test",
                "launch_vehicle": "TEST",
                "spacecraft": {},
                "controller_nomenclature": {},
                "ground_configuration_reference": "test",
                "sources": [],
            }
            for name in ("a.json", "b.json"):
                (root / name).write_text(json.dumps(base), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate mission_profile_id"):
                discover_mission_profiles(root)

    def test_invalid_nomenclature_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text(
                json.dumps(
                    {
                        "mission_profile_id": "bad",
                        "mission": "Test",
                        "mission_designation": "T",
                        "status": "test",
                        "launch_vehicle": "TEST",
                        "spacecraft": {},
                        "controller_nomenclature": {"lm_systems": ""},
                        "ground_configuration_reference": "test",
                        "sources": [],
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "controller_nomenclature"):
                load_mission_profile_record(path)


if __name__ == "__main__":
    unittest.main()
