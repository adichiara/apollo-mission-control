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
        self.assertEqual(response.json()["scenario_id"], "apollo13_pc2_nominal")
        self.assertEqual(response.json()["mission_profile_id"], "apollo13_h2")
        self.assertEqual(
            response.json()["model_profile_id"],
            "apollo13_h2_dynamics_partial",
        )
        self.assertEqual(
            response.json()["model_validation_state"],
            "not_historically_validated",
        )
        self.assertEqual(response.json()["runtime_adapter"], "pc2_v1")
        self.assertIn("mission_control_core", response.json()["runtime_capabilities"])
        self.assertIn("pc2_delta_p", response.json()["runtime_capabilities"])

    def test_health_and_phone_shell(self):
        self.assertEqual(self.client.get("/api/health").json(), {"status": "ok"})
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertIn("APOLLO MISSION CONTROL", page.text)


    def test_scenario_catalog_and_explicit_selection(self):
        response = self.client.get("/api/scenarios")
        self.assertEqual(response.status_code, 200)
        scenarios = response.json()
        self.assertTrue(scenarios)

        pc2 = next(
            item for item in scenarios
            if item["scenario_id"] == "apollo13_pc2_nominal"
        )
        self.assertEqual(pc2["mission"], "Apollo 13")
        self.assertEqual(pc2["runtime_adapter"], "pc2_v1")
        self.assertEqual(pc2["mission_profile_id"], "apollo13_h2")
        self.assertEqual(
            pc2["model_profile_id"],
            "apollo13_h2_dynamics_partial",
        )
        self.assertEqual(pc2["scenario_class"], "historical_flight_reconstruction")
        self.assertTrue(pc2["default"])
        self.assertTrue(pc2["executable"])

        created = self.client.post(
            "/api/session/create?scenario_id=apollo13_pc2_nominal"
        )
        self.assertEqual(created.status_code, 200)
        self.assertEqual(created.json()["scenario_title"], pc2["title"])
        self.assertEqual(created.json()["mission_profile_id"], "apollo13_h2")
        self.assertEqual(
            created.json()["model_profile_id"],
            "apollo13_h2_dynamics_partial",
        )

        rejected = self.client.post(
            "/api/session/create?scenario_id=does-not-exist"
        )
        self.assertEqual(rejected.status_code, 400)
        self.assertIn("unknown scenario_id", rejected.json()["detail"])

        status = self.client.get("/api/session/status")
        self.assertEqual(status.status_code, 200)
        self.assertEqual(status.json()["scenario_id"], "apollo13_pc2_nominal")
        self.assertEqual(status.json()["mission_profile_id"], "apollo13_h2")
        self.assertEqual(
            status.json()["model_profile_id"],
            "apollo13_h2_dynamics_partial",
        )
        self.assertEqual(
            status.json()["model_validation_state"],
            "not_historically_validated",
        )


    def test_mission_profile_catalog_preserves_documented_nomenclature(self):
        response = self.client.get("/api/mission-profiles")
        self.assertEqual(response.status_code, 200)
        profiles = {
            item["mission_profile_id"]: item
            for item in response.json()
        }
        self.assertIn("apollo11_g", profiles)
        self.assertIn("apollo13_h2", profiles)
        self.assertEqual(
            profiles["apollo11_g"]["controller_nomenclature"]["lm_systems"],
            "TELCOM",
        )
        self.assertEqual(
            profiles["apollo13_h2"]["controller_nomenclature"][
                "lm_electrical_environmental_emu"
            ],
            "TELMU",
        )

    def test_model_profile_catalog_exposes_domain_readiness(self):
        response = self.client.get("/api/model-profiles")
        self.assertEqual(response.status_code, 200)
        profiles = {
            item["model_profile_id"]: item
            for item in response.json()
        }
        self.assertIn("apollo13_h2_dynamics_partial", profiles)
        profile = profiles["apollo13_h2_dynamics_partial"]
        self.assertEqual(profile["mission_profile_id"], "apollo13_h2")
        self.assertEqual(
            profile["validation_state"],
            "not_historically_validated",
        )
        self.assertEqual(
            profile["domains"]["propulsion"]["status"],
            "partial",
        )
        self.assertEqual(
            profile["domains"]["translational_dynamics"]["status"],
            "unresolved",
        )


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

    def test_flight_gate_does_not_pause_get_and_go_can_clear_it(self):
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
        advance = self.client.post("/api/session/advance", json={"target_get_s": 285600.0})
        self.assertEqual(advance.status_code, 200)
        self.assertEqual(advance.json()["pending_gate"], "flight_go")
        self.assertEqual(advance.json()["status"], "running")
        self.assertIsNone(advance.json()["pause_reason"])
        self.assertEqual(advance.json()["reached_get_s"], 285600.0)

        readiness = self.client.post(
            "/api/session/player/control/readiness",
            json={"ready": True, "note": "CONTROL ready"},
        )
        self.assertEqual(readiness.status_code, 200)

        flight_snapshot = self.client.get("/api/session/player/flight").json()
        self.assertEqual(len(flight_snapshot["presentation"]["readiness_reports"]), 1)
        self.assertIsNone(flight_snapshot["pause_reason"])

        decision = self.client.post(
            "/api/session/flight/flight/decision",
            json={"go": True, "basis": "controller reports"},
        )
        self.assertEqual(decision.status_code, 200)
        self.assertIsNone(decision.json()["pending_gate"])
        self.assertEqual(decision.json()["session_status"], "running")

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

    def test_late_unresolved_go_misses_nominal_p40_without_freezing_clock(self):
        self.client.post(
            "/api/session/join",
            json={"player_id": "flight", "station": "FLIGHT"},
        )
        self.client.post("/api/session/start")

        advance = self.client.post(
            "/api/session/advance",
            json={"target_get_s": 79 * 3600 + 24 * 60},
        )
        self.assertEqual(advance.status_code, 200)
        self.assertEqual(advance.json()["status"], "running")
        self.assertEqual(advance.json()["pending_gate"], "flight_go")

        audit = self.client.get("/api/session/audit").json()
        missed = [e for e in audit if e["kind"] == "scenario_event_missed"]
        self.assertTrue(any(e["details"].get("event") == "p40_active_final_preburn" for e in missed))

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
