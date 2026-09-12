from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.pc2_nominal import (  # noqa: E402
    build_events,
    load_fixture,
    run_nominal,
    validate_nominal,
)


class PC2NominalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = load_fixture(
            ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json"
        )

    def test_event_order(self):
        events = build_events(self.fixture)
        times = [event.get_s for event in events]
        self.assertEqual(times, sorted(times))

    def test_historical_tig_and_cutoff(self):
        events = {event.name: event.get_s for event in build_events(self.fixture)}
        self.assertAlmostEqual(events["dps_ignition"], 286058.30)
        self.assertAlmostEqual(events["guided_cutoff"], 286322.12)

    def test_nominal_run_reaches_powerdown(self):
        state = run_nominal(self.fixture)
        self.assertTrue(state.cutoff_complete)
        self.assertTrue(state.residual_review_complete)
        self.assertTrue(state.powerdown_started)
        self.assertFalse(state.shutdown_rule_triggers)

    def test_nominal_validation_contract(self):
        state = run_nominal(self.fixture)
        self.assertEqual(validate_nominal(self.fixture, state), [])


if __name__ == "__main__":
    unittest.main()
