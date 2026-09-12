from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fastapi.testclient import TestClient  # noqa: E402
from apollo_mission_control.web_app import app  # noqa: E402


class WebAppTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        response = self.client.post("/api/session/create")
        self.assertEqual(response.status_code, 200)

    def test_health_and_phone_shell(self):
        self.assertEqual(self.client.get("/api/health").json(), {"status": "ok"})
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertIn("APOLLO MISSION CONTROL", page.text)

    def test_join_start_advance_and_snapshot(self):
        join = self.client.post(
            "/api/session/join",
            json={"player_id": "inco", "station": "INCO"},
        )
        self.assertEqual(join.status_code, 200)
        self.assertEqual(join.json()["station"], "INCO")

        self.assertEqual(self.client.post("/api/session/start").status_code, 200)
        advance = self.client.post("/api/session/advance", json={"target_get_s": 280560.0})
        self.assertEqual(advance.status_code, 200)

        snapshot = self.client.get("/api/session/player/inco")
        self.assertEqual(snapshot.status_code, 200)
        body = snapshot.json()
        self.assertEqual(body["station"], "INCO")
        self.assertEqual(body["presentation"]["title"], "INCO — PC+2 COMMUNICATIONS SUPPORT")
        self.assertNotIn("audit_log", body)

    def test_same_player_can_rejoin_same_station_but_not_switch(self):
        first = self.client.post(
            "/api/session/join",
            json={"player_id": "inco", "station": "INCO"},
        )
        self.assertEqual(first.status_code, 200)

        rejoin = self.client.post(
            "/api/session/join",
            json={"player_id": "inco", "station": "INCO"},
        )
        self.assertEqual(rejoin.status_code, 200)
        self.assertEqual(rejoin.json()["station"], "INCO")

        switch = self.client.post(
            "/api/session/join",
            json={"player_id": "inco", "station": "GUIDO"},
        )
        self.assertEqual(switch.status_code, 400)

        audit = self.client.get("/api/session/audit").json()
        self.assertIn("player_rejoined", [event["kind"] for event in audit])

    def test_flight_gate_readiness_and_capcom_handoff_over_api(self):
        for player_id, station in (
            ("flight", "FLIGHT"),
            ("control", "CONTROL"),
            ("capcom", "CAPCOM"),
        ):
            response = self.client.post(
                "/api/session/join",
                json={"player_id": player_id, "station": station},
            )
            self.assertEqual(response.status_code, 200)

        self.client.post("/api/session/start")
        # 79:20 GET is after the historical final-poll event; playable session
        # must stop at the 79:17 decision gate.
        advance = self.client.post("/api/session/advance", json={"target_get_s": 285600.0})
        self.assertEqual(advance.status_code, 200)
        self.assertEqual(advance.json()["pending_gate"], "flight_go")

        readiness = self.client.post(
            "/api/session/player/control/readiness",
            json={"ready": True, "note": "CONTROL ready"},
        )
        self.assertEqual(readiness.status_code, 200)

        flight_snapshot = self.client.get("/api/session/player/flight").json()
        self.assertEqual(len(flight_snapshot["presentation"]["readiness_reports"]), 1)

        decision = self.client.post(
            "/api/session/flight/flight/decision",
            json={"go": True, "basis": "controller reports"},
        )
        self.assertEqual(decision.status_code, 200)
        self.assertIsNone(decision.json()["pending_gate"])

        queued = self.client.post(
            "/api/session/flight/flight/capcom",
            json={"action": "continue_pc2_burn_sequence", "parameters": {}, "basis": "FLIGHT GO"},
        )
        self.assertEqual(queued.status_code, 200)
        item_id = queued.json()["item_id"]

        capcom_snapshot = self.client.get("/api/session/player/capcom").json()
        self.assertEqual(len(capcom_snapshot["presentation"]["queue_items"]), 1)
        self.assertFalse(capcom_snapshot["presentation"]["queue_items"][0]["transmitted"])

        transmitted = self.client.post(f"/api/session/capcom/capcom/transmit/{item_id}")
        self.assertEqual(transmitted.status_code, 200)
        self.assertTrue(transmitted.json()["transmitted"])

    def test_station_assignment_conflict_returns_400(self):
        first = self.client.post(
            "/api/session/join",
            json={"player_id": "a", "station": "GUIDO"},
        )
        self.assertEqual(first.status_code, 200)
        second = self.client.post(
            "/api/session/join",
            json={"player_id": "b", "station": "GUIDO"},
        )
        self.assertEqual(second.status_code, 400)


if __name__ == "__main__":
    unittest.main()
