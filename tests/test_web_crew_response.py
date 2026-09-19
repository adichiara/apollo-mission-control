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

    def test_nominal_flight_capcom_handoff_exposes_receipt_as_separate_state(self):
        advance = self.client.post(
            "/api/session/advance",
            json={"target_get_s": 79 * 3600 + 17 * 60},
        )
        self.assertEqual(advance.status_code, 200)

        decision = self.client.post(
            "/api/session/flight/flight/decision",
            json={"go": True, "basis": "nominal interaction integration test"},
        )
        self.assertEqual(decision.status_code, 200)

        queued = self.client.post(
            "/api/session/flight/flight/capcom",
            json={
                "action": "continue_pc2_burn_sequence",
                "parameters": {},
                "basis": "FLIGHT approved nominal continuation",
            },
        )
        self.assertEqual(queued.status_code, 200)
        item_id = queued.json()["item_id"]

        pending = self.client.get("/api/session/player/capcom").json()["presentation"][
            "queue_items"
        ][0]
        self.assertFalse(pending["transmitted"])
        self.assertFalse(pending["received"])
        self.assertIsNone(pending["received_get_s"])
        self.assertIsNone(pending["acknowledgement"])

        transmitted = self.client.post(
            f"/api/session/capcom/capcom/transmit/{item_id}"
        )
        self.assertEqual(transmitted.status_code, 200)

        after_transmit = self.client.get(
            "/api/session/player/capcom"
        ).json()["presentation"]["queue_items"][0]
        self.assertTrue(after_transmit["transmitted"])
        self.assertFalse(after_transmit["received"])
        self.assertIsNotNone(after_transmit["transmitted_get_s"])

        audit_before_receipt = self.client.get("/api/session/audit").json()
        self.assertNotIn(
            "crew_capcom_item_received",
            [event["kind"] for event in audit_before_receipt],
        )

        receipt = self.client.post(
            f"/api/session/crew/receipt/{item_id}",
            json={},
        )
        self.assertEqual(receipt.status_code, 200)
        self.assertEqual(receipt.json()["kind"], "crew_capcom_item_received")

        received = self.client.get(
            "/api/session/player/capcom"
        ).json()["presentation"]["queue_items"][0]
        self.assertTrue(received["transmitted"])
        self.assertTrue(received["received"])
        self.assertIsNotNone(received["received_get_s"])
        self.assertEqual(received["acknowledgement"], "received")

        audit = self.client.get("/api/session/audit").json()
        kinds = [event["kind"] for event in audit]
        self.assertLess(
            kinds.index("capcom_item_transmitted"),
            kinds.index("crew_capcom_item_received"),
        )
        self.assertNotIn("crew_dps_shutdown_commanded", kinds)
        self.assertNotIn("crew_inverter_transfer_performed", kinds)

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

    def _transmitted_inverter_transfer(self) -> int:
        advance = self.client.post(
            "/api/session/advance",
            json={"target_get_s": 79 * 3600 + 17 * 60},
        )
        self.assertEqual(advance.status_code, 200)
        decision = self.client.post(
            "/api/session/flight/flight/decision",
            json={"go": True, "basis": "synthetic inverter integration test"},
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
                "injection_id": "web-test-inverter-warning",
                "target": "lm_inverter_warning",
                "value": True,
                "evidence_class": "source_bounded_test",
                "provenance": "synthetic warning for sourced inverter contingency path",
            },
        )
        self.assertEqual(injection.status_code, 200)
        queued = self.client.post(
            "/api/session/flight/flight/inverter-transfer",
            json={"basis": "warning observed; execute sourced alternate-inverter procedure"},
        )
        self.assertEqual(queued.status_code, 200)
        body = queued.json()
        self.assertEqual(body["action"], "switch_lm_inverter")
        self.assertEqual(body["parameters"]["from_inverter"], 2)
        self.assertEqual(body["parameters"]["to_inverter"], 1)
        self.assertEqual(
            body["parameters"]["control_sequence"],
            [
                "CB(11) EPS: INV 1 — close",
                "INVERTER — 1",
                "CB(16) EPS: INV 2 — open",
            ],
        )
        item_id = body["item_id"]
        transmitted = self.client.post(
            f"/api/session/capcom/capcom/transmit/{item_id}"
        )
        self.assertEqual(transmitted.status_code, 200)
        return item_id

    def test_inverter_transfer_uses_simulated_crew_and_keeps_reobservation_separate(self):
        item_id = self._transmitted_inverter_transfer()

        too_early = self.client.post(
            f"/api/session/crew/inverter-transfer/{item_id}",
            json={},
        )
        self.assertEqual(too_early.status_code, 400)

        receipt = self.client.post(
            f"/api/session/crew/receipt/{item_id}",
            json={},
        )
        self.assertEqual(receipt.status_code, 200)
        self.assertEqual(receipt.json()["kind"], "crew_capcom_item_received")

        action = self.client.post(
            f"/api/session/crew/inverter-transfer/{item_id}",
            json={},
        )
        self.assertEqual(action.status_code, 200)
        action_body = action.json()
        self.assertEqual(action_body["action"], "switch_lm_inverter")
        self.assertEqual(action_body["parameters"]["from_inverter"], 2)
        self.assertEqual(action_body["parameters"]["to_inverter"], 1)

        report = self.client.post(
            f"/api/session/crew/inverter-transfer-report/{item_id}",
            json={},
        )
        self.assertEqual(report.status_code, 200)
        self.assertEqual(
            report.json()["kind"],
            "crew_inverter_transfer_reported",
        )
        self.assertEqual(
            report.json()["details"]["observation_consequence"],
            "not_asserted",
        )

        before_fresh_observation = self.client.get(
            "/api/session/admin/inverter-rule"
        )
        self.assertEqual(before_fresh_observation.status_code, 200)
        self.assertEqual(
            before_fresh_observation.json()["state"],
            "not_evaluable",
        )

        # The crew report does not itself create a new caution observation.
        # Advance only to establish ordering; no source-based dwell is implied.
        status = self.client.get("/api/session/status").json()
        advance = self.client.post(
            "/api/session/advance",
            json={"target_get_s": status["get_s"] + 0.1},
        )
        self.assertEqual(advance.status_code, 200)
        post_observation = self.client.post(
            "/api/session/admin/injection",
            json={
                "injection_id": "web-test-inverter-warning-post-transfer",
                "target": "lm_inverter_warning",
                "value": True,
                "evidence_class": "source_bounded_test",
                "provenance": "synthetic fresh post-transfer caution observation",
            },
        )
        self.assertEqual(post_observation.status_code, 200)
        after_fresh_observation = self.client.get(
            "/api/session/admin/inverter-rule"
        )
        self.assertEqual(after_fresh_observation.status_code, 200)
        self.assertEqual(
            after_fresh_observation.json()["state"],
            "triggered",
        )

        audit = self.client.get("/api/session/audit")
        self.assertEqual(audit.status_code, 200)
        kinds = [event["kind"] for event in audit.json()]
        self.assertLess(
            kinds.index("capcom_item_transmitted"),
            kinds.index("crew_capcom_item_received"),
        )
        self.assertLess(
            kinds.index("crew_capcom_item_received"),
            kinds.index("crew_inverter_transfer_performed"),
        )
        self.assertLess(
            kinds.index("crew_inverter_transfer_performed"),
            kinds.index("crew_inverter_transfer_reported"),
        )
        self.assertNotIn("dps_engine_off_physical_response", kinds)

    def test_inverter_transfer_requires_current_warning(self):
        response = self.client.post(
            "/api/session/flight/flight/inverter-transfer",
            json={"basis": "should be rejected without warning"},
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("current inverter-warning", response.json()["detail"])

    def test_physical_response_requires_prior_crew_command(self):
        response = self.client.post(
            "/api/session/admin/vehicle/dps-engine-off",
            json={},
        )
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
