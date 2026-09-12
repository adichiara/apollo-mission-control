from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fastapi.testclient import TestClient  # noqa: E402
from apollo_mission_control.web_app import app  # noqa: E402


class WebDeltaPIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.client.post("/api/session/create")
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
        self.client.post("/api/session/advance", json={"target_get_s": 285420.0})
        self.client.post(
            "/api/session/flight/flight/decision",
            json={"go": True, "basis": "test nominal readiness"},
        )
        self.client.post("/api/session/advance", json={"target_get_s": 286140.0})

    def test_source_bounded_delta_p_path_reaches_capcom_without_forcing_vehicle_response(self):
        injection = self.client.post(
            "/api/session/admin/injection",
            json={
                "injection_id": "test-delta-p-26",
                "target": "dps_fuel_oxidizer_delta_p_psi",
                "value": 26.0,
                "evidence_class": "source_bounded_test",
                "provenance": "synthetic boundary test; 26 psi is not an Apollo 13 measurement",
            },
        )
        self.assertEqual(injection.status_code, 200)

        callout = self.client.post(
            "/api/session/control/control/delta-p-callout",
            json={"basis": "fuel/oxidizer differential pressure >25 psi; ground callout only"},
        )
        self.assertEqual(callout.status_code, 200)
        body = callout.json()
        self.assertEqual(body["requested_by"], "CONTROL")
        self.assertFalse(body["transmitted"])

        capcom = self.client.get("/api/session/player/capcom").json()
        queue = capcom["presentation"]["queue_items"]
        self.assertEqual(len(queue), 1)
        self.assertEqual(queue[0]["requested_by"], "CONTROL")

        transmitted = self.client.post(
            f"/api/session/capcom/capcom/transmit/{body['item_id']}"
        )
        self.assertEqual(transmitted.status_code, 200)
        self.assertTrue(transmitted.json()["transmitted"])

        audit = self.client.get("/api/session/audit").json()
        kinds = [event["kind"] for event in audit]
        self.assertIn("state_injection_applied", kinds)
        self.assertIn("controller_shutdown_callout_decision", kinds)
        self.assertIn("capcom_item_transmitted", kinds)


if __name__ == "__main__":
    unittest.main()
