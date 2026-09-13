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
    def test_scripted_nominal_playthrough_reaches_ptc_preparation_complete(self):
        fixture = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")
        session = run_scripted_nominal_playthrough(fixture)

        self.assertEqual(session.status, SessionStatus.COMPLETE)
        self.assertTrue(session.state.flight_go)
        self.assertTrue(session.state.cutoff_complete)
        self.assertTrue(session.state.residual_review_complete)
        self.assertTrue(session.state.powerdown_started)
        self.assertTrue(session.state.ptc_preparation_started)
        self.assertEqual(session.state.phase, "pc2_ptc_preparation")
        self.assertIsNone(session.pending_gate)
        self.assertEqual(set(session.station_assignments.values()), set(DEFAULT_PLAYERS.values()))

        latest = session.latest_readiness_by_station()
        for station in ("CONTROL", "GUIDO", "TELMU", "FIDO_RETRO", "INCO"):
            self.assertTrue(latest[station].ready)

        kinds = [event.kind for event in session.audit_log]
        self.assertIn("decision_gate_opened", kinds)
        gate_events = [event for event in session.audit_log if event.kind == "decision_gate_opened"]
        self.assertEqual(gate_events[0].details["gate"], "flight_go")
        self.assertFalse(gate_events[0].details["simulation_paused"])
        self.assertIn("flight_go_decision", kinds)
        self.assertIn("capcom_item_queued", kinds)
        self.assertIn("capcom_item_transmitted", kinds)
        self.assertIn("session_completed", kinds)

        applied = [
            event.details.get("event")
            for event in session.audit_log
            if event.kind == "scenario_event_applied"
        ]
        self.assertIn("lm_powerdown_transition", applied)
        self.assertIn("ptc_preparation_begins", applied)

    def test_every_logical_player_can_receive_a_final_snapshot(self):
        fixture = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")
        session = run_scripted_nominal_playthrough(fixture)

        for player_id, station in DEFAULT_PLAYERS.items():
            snapshot = session.player_snapshot(player_id).to_dict()
            self.assertEqual(snapshot["station"], station)
            self.assertEqual(snapshot["session_status"], "complete")
            self.assertEqual(snapshot["mission_phase"], "pc2_ptc_preparation")
            self.assertIn("presentation", snapshot)


if __name__ == "__main__":
    unittest.main()
