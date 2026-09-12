from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.pc2_nominal import load_fixture  # noqa: E402
from apollo_mission_control.pc2_playthrough import (  # noqa: E402
    DEFAULT_PLAYERS,
    run_scripted_nominal_playthrough,
)
from apollo_mission_control.pc2_session import SessionStatus  # noqa: E402


class PC2PlaythroughTests(unittest.TestCase):
    def test_scripted_nominal_playthrough_reaches_powerdown_complete(self):
        fixture = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")
        session = run_scripted_nominal_playthrough(fixture)

        self.assertEqual(session.status, SessionStatus.COMPLETE)
        self.assertTrue(session.state.flight_go)
        self.assertTrue(session.state.cutoff_complete)
        self.assertTrue(session.state.residual_review_complete)
        self.assertTrue(session.state.powerdown_started)
        self.assertEqual(session.state.phase, "pc2_postburn_powerdown")
        self.assertIsNone(session.pending_gate)
        self.assertEqual(set(session.station_assignments.values()), set(DEFAULT_PLAYERS.values()))

        latest = session.latest_readiness_by_station()
        for station in ("CONTROL", "GUIDO", "TELMU", "FIDO_RETRO", "INCO"):
            self.assertTrue(latest[station].ready)

        kinds = [event.kind for event in session.audit_log]
        self.assertIn("flight_go_no_go_poll_opened", kinds)
        self.assertIn("flight_go_decision", kinds)
        self.assertIn("capcom_item_queued", kinds)
        self.assertIn("capcom_item_transmitted", kinds)
        self.assertIn("session_completed", kinds)

    def test_every_logical_player_can_receive_a_final_snapshot(self):
        fixture = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")
        session = run_scripted_nominal_playthrough(fixture)

        for player_id, station in DEFAULT_PLAYERS.items():
            snapshot = session.player_snapshot(player_id).to_dict()
            self.assertEqual(snapshot["station"], station)
            self.assertEqual(snapshot["session_status"], "complete")
            self.assertIn("presentation", snapshot)


if __name__ == "__main__":
    unittest.main()
