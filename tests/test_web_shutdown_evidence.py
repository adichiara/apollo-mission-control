from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fastapi.testclient import TestClient  # noqa: E402
from apollo_mission_control.web_app import app  # noqa: E402


class WebShutdownEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.client.post("/api/session/create")
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

    def _reach_shutdown_command(self) -> int:
        self.client.post(
            "/api/session/advance",
            json={"target_get_s": 79 * 3600 + 17 * 60},
        )
        self.client.post(
            "/api/session/flight/flight/decision",
            json={"go": True, "basis": "synthetic integration test"},
        )
        self.client.post(
            "/api/session/advance",
            json={"target_get_s": 79 * 3600 + 29 * 60},
        )

        # A pre-command chamber-pressure observation must not later count as
        # response evidence merely because it remains the current value.
        pressure = self.client.post(
            "/api/session/admin/injection",
            json={
                "injection_id": "pre-command-pressure",
                "target": "dps_chamber_pressure_psi",
                "value": 100.0,
                "evidence_class": "source_bounded_test",
                "provenance": "synthetic freshness test; not an Apollo 13 measurement",
            },
        )
        self.assertEqual(pressure.status_code, 200)

        delta_p = self.client.post(
            "/api/session/admin/injection",
            json={
                "injection_id": "delta-p-26",
                "target": "dps_fuel_oxidizer_delta_p_psi",
                "value": 26.0,
                "evidence_class": "source_bounded_test",
                "provenance": "synthetic boundary test; not an Apollo 13 measurement",
            },
        )
        self.assertEqual(delta_p.status_code, 200)

        callout = self.client.post(
            "/api/session/control/control/delta-p-callout",
            json={"basis": "synthetic >25 psi rule exercise"},
        )
        self.assertEqual(callout.status_code, 200)
        item_id = callout.json()["item_id"]
        self.assertEqual(
            self.client.post(f"/api/session/capcom/capcom/transmit/{item_id}").status_code,
            200,
        )
        self.assertEqual(
            self.client.post(f"/api/session/crew/receipt/{item_id}", json={}).status_code,
            200,
        )
        self.assertEqual(
            self.client.post(f"/api/session/crew/shutdown/{item_id}", json={}).status_code,
            200,
        )
        return item_id

    def test_precommand_pressure_does_not_count_but_crew_report_does(self):
        self._reach_shutdown_command()

        evidence = self.client.get("/api/session/control/control/shutdown-evidence")
        self.assertEqual(evidence.status_code, 200)
        self.assertEqual(evidence.json()["state"], "none")

        report = self.client.post("/api/session/crew/shutdown-report", json={})
        self.assertEqual(report.status_code, 200)

        evidence = self.client.get("/api/session/control/control/shutdown-evidence")
        self.assertEqual(evidence.status_code, 200)
        self.assertEqual(evidence.json()["state"], "crew_reported")
        self.assertIsNone(evidence.json()["chamber_pressure_psi"])

    def test_fresh_pressure_is_evidence_without_becoming_a_threshold_verdict(self):
        self._reach_shutdown_command()
        self.client.post("/api/session/crew/shutdown-report", json={})

        # Deliberately use a high value. The evidence model should report that a
        # fresh pressure observation exists, not interpret 100 psi as engine off.
        fresh = self.client.post(
            "/api/session/admin/injection",
            json={
                "injection_id": "post-command-pressure",
                "target": "dps_chamber_pressure_psi",
                "value": 100.0,
                "evidence_class": "source_bounded_test",
                "provenance": "synthetic freshness test; no engine-off threshold implied",
            },
        )
        self.assertEqual(fresh.status_code, 200)

        evidence = self.client.get("/api/session/control/control/shutdown-evidence")
        self.assertEqual(evidence.status_code, 200)
        body = evidence.json()
        self.assertEqual(body["state"], "corroborated")
        self.assertEqual(body["chamber_pressure_psi"], 100.0)
        self.assertNotIn("engine_off_confirmed", body)

    def test_non_control_player_cannot_request_control_evidence(self):
        self._reach_shutdown_command()
        response = self.client.get("/api/session/control/flight/shutdown-evidence")
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
