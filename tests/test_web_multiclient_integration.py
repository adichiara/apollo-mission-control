from pathlib import Path
import os
import sys
import time
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fastapi.testclient import TestClient  # noqa: E402
from apollo_mission_control.web_app import app  # noqa: E402


class WebMultiClientIntegrationTests(unittest.TestCase):
    """Exercise several independent HTTP clients against one authoritative session.

    These are in-process transport tests, not a substitute for a deployed phone/
    browser smoke test. They protect shared-state, station-isolation, rejoin,
    facilitator-authority, pause/resume, and the synthetic Delta-P branch contract.
    """

    def setUp(self):
        self.token = "multiclient-facilitator-secret"
        self.headers = {"X-Apollo-Facilitator": self.token}
        self.env = patch.dict(
            os.environ,
            {"APOLLO_FACILITATOR_TOKEN": self.token},
            clear=False,
        )
        self.env.start()
        self.addCleanup(self.env.stop)

        self.facilitator = TestClient(app)
        self.flight = TestClient(app)
        self.control = TestClient(app)
        self.capcom = TestClient(app)
        self.guido = TestClient(app)

        created = self.facilitator.post("/api/session/create", headers=self.headers)
        self.assertEqual(created.status_code, 200)

        for client, player_id, station in (
            (self.flight, "flight", "FLIGHT"),
            (self.control, "control", "CONTROL"),
            (self.capcom, "capcom", "CAPCOM"),
            (self.guido, "guido", "GUIDO"),
        ):
            joined = client.post(
                "/api/session/join",
                json={"player_id": player_id, "station": station},
            )
            self.assertEqual(joined.status_code, 200)
            self.assertEqual(joined.json()["station"], station)

        started = self.facilitator.post("/api/session/start", headers=self.headers)
        self.assertEqual(started.status_code, 200)

    def _facilitator_post(self, path: str, body: dict | None = None):
        return self.facilitator.post(path, json=body, headers=self.headers)

    def _advance(self, get_s: float):
        response = self._facilitator_post(
            "/api/session/advance",
            {"target_get_s": get_s},
        )
        self.assertEqual(response.status_code, 200)
        return response

    def _reach_nonnominal_window(self):
        self._advance(79 * 3600 + 17 * 60)
        decision = self.flight.post(
            "/api/session/flight/flight/decision",
            json={"go": True, "basis": "multi-client synthetic integration test"},
        )
        self.assertEqual(decision.status_code, 200)
        self._advance(79 * 3600 + 29 * 60)

    def test_shared_session_rejoin_station_isolation_and_facilitator_pause(self):
        flight_snapshot = self.flight.get("/api/session/player/flight")
        control_snapshot = self.control.get("/api/session/player/control")
        capcom_snapshot = self.capcom.get("/api/session/player/capcom")
        guido_snapshot = self.guido.get("/api/session/player/guido")

        for response in (
            flight_snapshot,
            control_snapshot,
            capcom_snapshot,
            guido_snapshot,
        ):
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()["session_status"], "running")

        self.assertEqual(flight_snapshot.json()["station"], "FLIGHT")
        self.assertEqual(control_snapshot.json()["station"], "CONTROL")
        self.assertEqual(capcom_snapshot.json()["station"], "CAPCOM")
        self.assertEqual(guido_snapshot.json()["station"], "GUIDO")

        # Station-specific operational collections stay scoped to the stations
        # that actually use them.
        self.assertIn("readiness_reports", flight_snapshot.json()["presentation"])
        self.assertNotIn("readiness_reports", control_snapshot.json()["presentation"])
        self.assertIn("queue_items", capcom_snapshot.json()["presentation"])
        self.assertNotIn("queue_items", guido_snapshot.json()["presentation"])

        # A fresh browser/client can idempotently rejoin the same identity/station.
        reloaded_control = TestClient(app)
        rejoin = reloaded_control.post(
            "/api/session/join",
            json={"player_id": "control", "station": "CONTROL"},
        )
        self.assertEqual(rejoin.status_code, 200)
        self.assertEqual(rejoin.json()["station"], "CONTROL")

        switch = reloaded_control.post(
            "/api/session/join",
            json={"player_id": "control", "station": "GUIDO"},
        )
        self.assertEqual(switch.status_code, 400)

        occupied = TestClient(app).post(
            "/api/session/join",
            json={"player_id": "another-control", "station": "CONTROL"},
        )
        self.assertEqual(occupied.status_code, 400)

        # Station clients cannot invoke facilitator operations when authority is
        # configured, even though they remain free to use station actions.
        denied_pause = self.control.post("/api/session/pause")
        self.assertEqual(denied_pause.status_code, 401)
        self.assertEqual(self.control.get("/api/session/audit").status_code, 401)

        paused = self.facilitator.post("/api/session/pause", headers=self.headers)
        self.assertEqual(paused.status_code, 200)
        self.assertEqual(paused.json()["status"], "paused")
        paused_get = paused.json()["get_s"]

        time.sleep(0.02)
        status = self.control.get("/api/session/status")
        self.assertEqual(status.status_code, 200)
        self.assertEqual(status.json()["status"], "paused")
        self.assertEqual(status.json()["get_s"], paused_get)

        resumed = self.facilitator.post("/api/session/resume", headers=self.headers)
        self.assertEqual(resumed.status_code, 200)
        self.assertEqual(resumed.json()["status"], "running")

    def test_complete_delta_p_branch_crosses_clients_without_hidden_shortcuts(self):
        self._reach_nonnominal_window()

        injection = self._facilitator_post(
            "/api/session/admin/injection",
            {
                "injection_id": "multiclient-delta-p-26",
                "target": "dps_fuel_oxidizer_delta_p_psi",
                "value": 26.0,
                "evidence_class": "source_bounded_test",
                "provenance": (
                    "synthetic multi-client boundary test; "
                    "26 psi is not an Apollo 13 measurement"
                ),
            },
        )
        self.assertEqual(injection.status_code, 200)

        callout = self.control.post(
            "/api/session/control/control/delta-p-callout",
            json={"basis": "synthetic >25 psi ground-callout exercise"},
        )
        self.assertEqual(callout.status_code, 200)
        item_id = callout.json()["item_id"]
        self.assertFalse(callout.json()["transmitted"])

        # CAPCOM observes the queued item through its own player snapshot; the
        # CONTROL snapshot does not receive the CAPCOM queue representation.
        capcom_view = self.capcom.get("/api/session/player/capcom").json()
        queued = [
            item
            for item in capcom_view["presentation"]["queue_items"]
            if item["item_id"] == item_id
        ]
        self.assertEqual(len(queued), 1)
        self.assertFalse(queued[0]["transmitted"])
        self.assertNotIn(
            "queue_items",
            self.control.get("/api/session/player/control").json()["presentation"],
        )

        transmitted = self.capcom.post(
            f"/api/session/capcom/capcom/transmit/{item_id}"
        )
        self.assertEqual(transmitted.status_code, 200)
        self.assertTrue(transmitted.json()["transmitted"])

        # Crew and vehicle responses remain facilitator-side validation actions;
        # CAPCOM transmission itself does not perform them.
        self.assertEqual(
            self.control.post(
                f"/api/session/crew/receipt/{item_id}",
                json={},
            ).status_code,
            401,
        )

        receipt = self._facilitator_post(
            f"/api/session/crew/receipt/{item_id}",
            {},
        )
        self.assertEqual(receipt.status_code, 200)

        shutdown = self._facilitator_post(
            f"/api/session/crew/shutdown/{item_id}",
            {},
        )
        self.assertEqual(shutdown.status_code, 200)

        engine_off = self._facilitator_post(
            "/api/session/admin/vehicle/dps-engine-off",
            {"cause": "crew_stop_pushbutton"},
        )
        self.assertEqual(engine_off.status_code, 200)

        report = self._facilitator_post(
            "/api/session/crew/shutdown-report",
            {},
        )
        self.assertEqual(report.status_code, 200)

        fresh_pressure = self._facilitator_post(
            "/api/session/admin/injection",
            {
                "injection_id": "multiclient-post-command-pressure",
                "target": "dps_chamber_pressure_psi",
                "value": 100.0,
                "evidence_class": "source_bounded_test",
                "provenance": (
                    "synthetic fresh observation; deliberately high value proves "
                    "that no engine-off pressure threshold is implied"
                ),
            },
        )
        self.assertEqual(fresh_pressure.status_code, 200)

        evidence = self.control.get(
            "/api/session/control/control/shutdown-evidence"
        )
        self.assertEqual(evidence.status_code, 200)
        self.assertEqual(evidence.json()["state"], "corroborated")
        self.assertEqual(evidence.json()["chamber_pressure_psi"], 100.0)
        self.assertNotIn("engine_off_confirmed", evidence.json())

        audit = self.facilitator.get("/api/session/audit", headers=self.headers)
        self.assertEqual(audit.status_code, 200)
        kinds = [event["kind"] for event in audit.json()]
        ordered = [
            "state_injection_applied",
            "controller_shutdown_callout_decision",
            "capcom_item_transmitted",
            "crew_capcom_item_received",
            "crew_dps_shutdown_commanded",
            "dps_engine_off_physical_response",
            "crew_dps_shutdown_reported",
        ]
        positions = [kinds.index(kind) for kind in ordered]
        self.assertEqual(positions, sorted(positions))


if __name__ == "__main__":
    unittest.main()
