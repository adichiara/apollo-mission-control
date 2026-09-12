from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.session_orchestration import PC2Session  # noqa: E402


class SessionOrchestrationTests(unittest.TestCase):
    def test_get_is_monotonic_and_audited(self):
        session = PC2Session(get_s=77 * 3600 + 55 * 60)
        session.synchronize_get(session.get_s + 10)
        self.assertEqual(session.audit_log()[-1].kind, "get_sync")
        with self.assertRaises(ValueError):
            session.synchronize_get(session.get_s - 1)

    def test_station_assignment_rejects_conflicting_player(self):
        session = PC2Session(get_s=0)
        session.assign_station(player_id="p1", station="CONTROL")
        with self.assertRaises(ValueError):
            session.assign_station(player_id="p2", station="CONTROL")

    def test_readiness_reports_do_not_automatically_create_flight_go(self):
        session = PC2Session(get_s=0)
        session.report_readiness(station="CONTROL", status="GO")
        session.report_readiness(station="GUIDO", status="GO")
        session.report_readiness(station="TELMU", status="GO")
        self.assertIsNone(session.flight_decision)

    def test_flight_decision_is_explicit_and_audited(self):
        session = PC2Session(get_s=0)
        session.report_readiness(station="CONTROL", status="GO")
        decision = session.record_flight_decision(go_for_burn=True)
        self.assertTrue(decision.go_for_burn)
        self.assertEqual(session.audit_log()[-1].actor, "FLIGHT")
        self.assertEqual(session.audit_log()[-1].kind, "flight_decision")

    def test_callout_requires_distinct_capcom_transmission(self):
        session = PC2Session(get_s=0)
        queued = session.queue_crew_callout(
            callout_id="go-for-burn",
            origin_station="FLIGHT",
            action="go_for_burn",
        )
        self.assertIn(queued.callout_id, session.pending_callouts)
        self.assertEqual(session.transmitted_callouts, [])

        transmitted = session.capcom_transmit("go-for-burn", get_s=5)
        self.assertEqual(transmitted.origin_station, "FLIGHT")
        self.assertEqual(transmitted.transmitted_get_s, 5)
        self.assertNotIn("go-for-burn", session.pending_callouts)
        self.assertEqual(session.audit_log()[-1].kind, "capcom_to_crew")

    def test_latest_readiness_report_replaces_station_current_state_but_audit_retains_history(self):
        session = PC2Session(get_s=0)
        session.report_readiness(station="CONTROL", status="HOLD", note="checking data")
        session.report_readiness(station="CONTROL", status="GO", get_s=2)
        self.assertEqual(session.readiness_reports["CONTROL"].status, "GO")
        reports = [event for event in session.audit_log() if event.kind == "readiness_report"]
        self.assertEqual(len(reports), 2)


if __name__ == "__main__":
    unittest.main()
