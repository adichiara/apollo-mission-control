from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fastapi.testclient import TestClient  # noqa: E402
from apollo_mission_control.web_app import app  # noqa: E402


class WebRestartFlowTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.assertEqual(self.client.post("/api/session/create").status_code, 200)
        for player_id, station in (
            ("flight", "FLIGHT"),
            ("control", "CONTROL"),
            ("capcom", "CAPCOM"),
        ):
            self.assertEqual(
                self.client.post(
                    "/api/session/join",
                    json={"player_id": player_id, "station": station},
                ).status_code,
                200,
            )
        self.assertEqual(self.client.post("/api/session/start").status_code, 200)
        self.assertEqual(
            self.client.post(
                "/api/session/advance",
                json={"target_get_s": 79 * 3600 + 17 * 60},
            ).status_code,
            200,
        )
        self.assertEqual(
            self.client.post(
                "/api/session/flight/flight/decision",
                json={"go": True, "basis": "restart integration test"},
            ).status_code,
            200,
        )
        self.assertEqual(
            self.client.post(
                "/api/session/advance",
                json={"target_get_s": 79 * 3600 + 29 * 60},
            ).status_code,
            200,
        )

    def test_prebriefed_restart_requires_eligibility_and_explicit_vehicle_response(self):
        stop = self.client.post(
            "/api/session/admin/vehicle/dps-premature-stop",
            json={
                "shutdown_cause_known_non_rule": True,
                "noun97_flashing": True,
                "cause": "synthetic non-rule early stop",
            },
        )
        self.assertEqual(stop.status_code, 200)
        self.assertEqual(
            stop.json()["restart_evaluation"]["disposition"],
            "restart_eligible",
        )

        audit_before = self.client.get("/api/session/audit").json()
        self.assertFalse(
            any(event["kind"] == "capcom_item_queued" for event in audit_before)
        )

        procedure = self.client.post(
            "/api/session/crew/restart-procedure",
            json={},
        )
        self.assertEqual(procedure.status_code, 200)
        actions = [
            event["details"]["action"]
            for event in procedure.json()["events"]
        ]
        self.assertEqual(
            actions,
            [
                "proceed_noun_97",
                "restart_manual_ullage",
                "press_engine_start",
                "descent_engine_command_override_on",
            ],
        )

        audit_after_procedure = self.client.get("/api/session/audit").json()
        self.assertFalse(
            any(
                event["kind"] == "dps_restart_physical_response"
                for event in audit_after_procedure
            )
        )

        restarted = self.client.post(
            "/api/session/admin/vehicle/dps-restart",
            json={},
        )
        self.assertEqual(restarted.status_code, 200)
        self.assertTrue(restarted.json()["engine_on_command_received"])
        self.assertFalse(restarted.json()["thrust_level_known"])

        audit = self.client.get("/api/session/audit").json()
        kinds = [event["kind"] for event in audit]
        self.assertLess(
            kinds.index("dps_premature_engine_stop"),
            kinds.index("crew_restart_procedure_step"),
        )
        self.assertLess(
            max(i for i, kind in enumerate(kinds) if kind == "crew_restart_procedure_step"),
            kinds.index("dps_restart_physical_response"),
        )
        self.assertFalse(any(kind == "capcom_item_transmitted" for kind in kinds))

    def test_unknown_stop_cause_does_not_allow_restart_procedure(self):
        stop = self.client.post(
            "/api/session/admin/vehicle/dps-premature-stop",
            json={
                "shutdown_cause_known_non_rule": False,
                "noun97_flashing": True,
            },
        )
        self.assertEqual(stop.status_code, 200)
        self.assertEqual(
            stop.json()["restart_evaluation"]["disposition"],
            "insufficient_context",
        )

        procedure = self.client.post(
            "/api/session/crew/restart-procedure",
            json={},
        )
        self.assertEqual(procedure.status_code, 400)
        self.assertIn("restart_eligible", procedure.json()["detail"])

    def test_listed_shutdown_rule_blocks_restart_even_if_non_rule_flag_is_true(self):
        injection = self.client.post(
            "/api/session/admin/injection",
            json={
                "injection_id": "restart-test-delta-p",
                "target": "dps_fuel_oxidizer_delta_p_psi",
                "value": 26.0,
                "evidence_class": "source_bounded_test",
                "provenance": "synthetic rule-blocking observation",
            },
        )
        self.assertEqual(injection.status_code, 200)

        stop = self.client.post(
            "/api/session/admin/vehicle/dps-premature-stop",
            json={
                "shutdown_cause_known_non_rule": True,
                "noun97_flashing": True,
            },
        )
        self.assertEqual(stop.status_code, 200)
        body = stop.json()["restart_evaluation"]
        self.assertEqual(body["disposition"], "do_not_restart_rule_shutdown")
        self.assertIn("fuel_oxidizer_delta_p", body["triggered_rule_ids"])

        self.assertEqual(
            self.client.post(
                "/api/session/crew/restart-procedure",
                json={},
            ).status_code,
            400,
        )


if __name__ == "__main__":
    unittest.main()
