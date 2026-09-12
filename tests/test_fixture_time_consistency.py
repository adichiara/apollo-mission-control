from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.pc2_nominal import hms_to_seconds, load_fixture  # noqa: E402


class FixtureTimeConsistencyTests(unittest.TestCase):
    def test_pc2_start_seconds_match_hms(self):
        fixture = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")
        self.assertEqual(
            float(fixture["start_get_s"]),
            hms_to_seconds(fixture["start_get_hms"]),
        )


if __name__ == "__main__":
    unittest.main()
