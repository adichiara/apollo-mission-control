from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fastapi.testclient import TestClient  # noqa: E402
from apollo_mission_control.web_app import app  # noqa: E402


class WebCrewResponseTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        response = self.client.post("/api/session/create")
        self.assertEqual(response.status_code, 200)
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
        self.assertEqual(self.client.post("/api/session/start").status_code, 200)

    def _transmitted_delta_p_callout(self) -> int:
        advance = self.client.post(
            "/api/session/advance",
            json={"target_get_s": 79 * 3600 + 17 * 60},
        )
        self.assertEqual(advance.status_code, 200)

        decision = self.client.post(
            "/api/session/flight/flight/decision",
            json={"go": True, "basis": "synthetic integration test"},
        )
        self.assertEqual(decision.status_code, 200)

        advance = self.client.post(
            "/api/session/advance",
            json={"target_get_s": 79 * 3600 + 29 * 60},
        )
        self.assertEqual(advance.status_code, 200)

        injection = self.client.post(
            "/api/session/admin/injection",
            json={
                "injection_id": "web-test-delta-p-26",
                "target": "dps_fuel_oxidizer_delta_p_psi",
                "value": 26.0,
                "evidence_class": "source_bounded_test",
                "provenance": "synthetic boundary test; not an Apollo 13 measurement",
            },
        )
        self.assertEqual(injection.status_code, 200)

        callout = self.client.post(
            "/api/session/control/control/delta-p-callout",
            json={"basis": "synthetic >25 psi rule exercise"},
        )
        self.assertEqual(callout.status_code, 200)
        item_id = callout.json()["item_id"]

        transmitted = self.client.post(f"/api/session/capcom/capcom/transmit/{item_id}")
        self.assertEqual(transmitted.status_code, 200)
        return item_id

    def test_http_chain_preserves_receipt_command_and_physical_response_boundaries(self):
        item_id = self._transmitted_delta_p_callout()

        too_early = self.client.post(
            f"/api/session/crew/shutdown/{item_id}",
            json={},
        )
        self.assertEqual(too_early.status_code, 400)

        receipt = self.client.post(
            f"/api/session/crew/receipt/{item_id}",
            json={},
        )
        self.assertEqual(receipt.status_code, 200)
        self.assertEqual(receipt.json()["kind"], "crew_capcom_item_received")

        command = self.client.post(
            f"/api/session/crew/shutdown/{item_id}",
            json={},
        )
        self.assertEqual(command.status_code, 200)
        self.assertEqual(command.json()["action"], "command_dps_shutdown")

        response = self.client.post(
            "/api/session/admin/vehicle/dps-engine-off",
            json={},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["engine_off_discrete_received"])

        audit = self.client.get("/api/session/audit")
        self.assertEqual(audit.status_code, 200)
        kinds = [event["kind"] for event in audit.json()]
        self.assertLess(kinds.index("capcom_item_transmitted"), kinds.index("crew_capcom_item_received"))
        self.assertLess(kinds.index("crew_capcom_item_received"), kinds.index("crew_dps_shutdown_commanded"))
        self.assertLess(kinds.index("crew_dps_shutdown_commanded"), kinds.index("dps_engine_off_physical_response"))

    def test_physical_response_requires_prior_crew_command(self):
        response = self.client.post(
            "/api/session/admin/vehicle/dps-engine-off",
            json={},
        )
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
