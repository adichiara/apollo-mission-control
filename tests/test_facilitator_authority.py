from pathlib import Path
import os
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fastapi.testclient import TestClient  # noqa: E402
from apollo_mission_control.web_app import app  # noqa: E402


class FacilitatorAuthorityTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.token = "test-facilitator-secret"
        self.headers = {"X-Apollo-Facilitator": self.token}

    def test_configured_token_protects_facilitator_operations_but_not_station_actions(self):
        with patch.dict(os.environ, {"APOLLO_FACILITATOR_TOKEN": self.token}, clear=False):
            denied = self.client.post("/api/session/create")
            self.assertEqual(denied.status_code, 401)

            created = self.client.post("/api/session/create", headers=self.headers)
            self.assertEqual(created.status_code, 200)

            # Station identity remains independent from facilitator authority.
            joined = self.client.post(
                "/api/session/join",
                json={"player_id": "control", "station": "CONTROL"},
            )
            self.assertEqual(joined.status_code, 200)

            denied_model = self.client.post(
                "/api/admin/model-proof/dps-burn",
                json={
                    "initial_mass_kg": 100.0,
                    "dry_mass_kg": 50.0,
                    "specific_impulse_s": 300.0,
                    "segments": [
                        {
                            "duration_s": 1.0,
                            "thrust_n": 10.0,
                            "direction": [1.0, 0.0, 0.0],
                        }
                    ],
                },
            )
            self.assertEqual(denied_model.status_code, 401)

            denied_start = self.client.post("/api/session/start")
            self.assertEqual(denied_start.status_code, 401)
            started = self.client.post("/api/session/start", headers=self.headers)
            self.assertEqual(started.status_code, 200)

            readiness = self.client.post(
                "/api/session/player/control/readiness",
                json={"ready": True, "note": "controller action"},
            )
            self.assertEqual(readiness.status_code, 200)

            self.assertEqual(self.client.get("/api/session/audit").status_code, 401)
            self.assertEqual(
                self.client.get("/api/session/audit", headers=self.headers).status_code,
                200,
            )

    def test_wrong_token_is_rejected(self):
        with patch.dict(os.environ, {"APOLLO_FACILITATOR_TOKEN": self.token}, clear=False):
            response = self.client.post(
                "/api/session/create",
                headers={"X-Apollo-Facilitator": "wrong"},
            )
            self.assertEqual(response.status_code, 401)

    def test_render_fails_closed_if_facilitator_secret_is_missing(self):
        old_token = os.environ.pop("APOLLO_FACILITATOR_TOKEN", None)
        try:
            with patch.dict(os.environ, {"RENDER": "true"}, clear=False):
                response = self.client.post("/api/session/create")
                self.assertEqual(response.status_code, 503)
        finally:
            if old_token is not None:
                os.environ["APOLLO_FACILITATOR_TOKEN"] = old_token


if __name__ == "__main__":
    unittest.main()
