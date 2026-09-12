from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.pc2_nominal import hms_to_seconds, load_fixture  # noqa: E402
from apollo_mission_control.pc2_session import PC2Session, SessionStatus  # noqa: E402


class PC2SessionTests(unittest.TestCase):
    def _session(self):
        fixture = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")
        return PC2Session.create(fixture)

    def test_station_assignment_is_unique_and_view_is_station_scoped(self):
        session = self._session()
        session.assign_station("alice", "CONTROL")
        session.assign_station("bob", "FLIGHT")

        with self.assertRaises(ValueError):
            session.assign_station("charlie", "CONTROL")
        with self.assertRaises(ValueError):
            session.assign_station("alice", "INCO")

        view = session.get_station_view("alice")
        self.assertEqual(view.title, "CONTROL — PC+2 BURN MONITOR")

    def test_go_poll_is_a_player_decision_gate_not_an_automatic_nominal_go(self):
        session = self._session()
        session.assign_station("flight", "FLIGHT")
        session.assign_station("control", "CONTROL")
        session.start()

        reached = session.advance_to(hms_to_seconds("79:20:00"))

        self.assertEqual(reached, hms_to_seconds("79:17:00"))
        self.assertEqual(session.pending_gate, "flight_go")
        self.assertFalse(session.state.flight_go)
        self.assertEqual(session.state.phase, "pc2_final_readiness")

        session.submit_readiness("control", ready=True, note="propulsion/control ready")
        session.record_flight_go("flight", go=True, basis="controller reports")

        self.assertTrue(session.state.flight_go)
        self.assertIsNone(session.pending_gate)
        self.assertEqual(session.state.phase, "pc2_go_for_burn")

        session.advance_to(hms_to_seconds("79:23:00"))
        self.assertTrue(session.state.p40_active)
        self.assertEqual(session.state.phase, "pc2_p40_preignition")

    def test_non_flight_player_cannot_clear_go_gate(self):
        session = self._session()
        session.assign_station("flight", "FLIGHT")
        session.assign_station("guido", "GUIDO")
        session.start()
        session.advance_to(hms_to_seconds("79:17:00"))

        with self.assertRaises(ValueError):
            session.record_flight_go("guido", go=True, basis="not authorized")
        self.assertEqual(session.pending_gate, "flight_go")

    def test_no_go_keeps_session_at_readiness_gate(self):
        session = self._session()
        session.assign_station("flight", "FLIGHT")
        session.start()
        session.advance_to(hms_to_seconds("79:17:00"))

        session.record_flight_go("flight", go=False, basis="one discipline not ready")
        self.assertFalse(session.state.flight_go)
        self.assertEqual(session.pending_gate, "flight_go")

        reached = session.advance_to(hms_to_seconds("79:23:00"))
        self.assertEqual(reached, hms_to_seconds("79:17:00"))
        self.assertFalse(session.state.p40_active)

    def test_flight_to_capcom_handoff_is_explicit(self):
        session = self._session()
        session.assign_station("flight", "FLIGHT")
        session.assign_station("capcom", "CAPCOM")
        session.start()

        item = session.queue_capcom_instruction(
            "flight",
            action="continue_pc2_preparation",
            parameters={"status": "go"},
            basis="Flight Director decision",
        )
        self.assertFalse(item.transmitted)

        transmitted = session.transmit_capcom_item("capcom", item.item_id)
        self.assertTrue(transmitted.transmitted)
        self.assertIsNotNone(transmitted.transmitted_get_s)

        kinds = [event.kind for event in session.audit_log]
        self.assertIn("capcom_item_queued", kinds)
        self.assertIn("capcom_item_transmitted", kinds)

    def test_pause_resume_and_audit(self):
        session = self._session()
        session.start()
        session.pause()
        self.assertEqual(session.status, SessionStatus.PAUSED)
        with self.assertRaises(ValueError):
            session.advance_to(hms_to_seconds("77:56:00"))
        session.resume()
        session.advance_to(hms_to_seconds("77:56:00"))
        self.assertEqual(session.status, SessionStatus.RUNNING)
        self.assertGreater(len(session.audit_log), 0)


if __name__ == "__main__":
    unittest.main()
