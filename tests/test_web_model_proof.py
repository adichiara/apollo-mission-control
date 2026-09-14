from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fastapi.testclient import TestClient  # noqa: E402
from apollo_mission_control.web_app import app  # noqa: E402


class WebModelProofTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.payload = {
            "initial_time_s": 0.0,
            "initial_mass_kg": 10_000.0,
            "dry_mass_kg": 5_000.0,
            "initial_velocity_m_s": [0.0, 0.0, 0.0],
            "specific_impulse_s": 300.0,
            "max_step_s": 0.25,
            "applicability": "API contract test; not historical evidence",
            "provenance": ["synthetic unit-test inputs"],
            "segments": [
                {
                    "duration_s": 10.0,
                    "thrust_n": 10_000.0,
                    "direction": [1.0, 0.0, 0.0],
                }
            ],
        }

    def test_facilitator_endpoint_returns_assumption_visible_result(self):
        response = self.client.post("/api/admin/model-proof/dps-burn", json=self.payload)
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(
            body["model_status"],
            "level_1_model_proof_not_historically_validated",
        )
        self.assertEqual(body["applicability"], self.payload["applicability"])
        self.assertEqual(body["provenance"], self.payload["provenance"])
        self.assertEqual(body["elapsed_s"], 10.0)
        self.assertGreater(body["delta_v_m_s"][0], 0.0)
        self.assertEqual(body["delta_v_m_s"][1:], [0.0, 0.0])
        self.assertLess(body["final_state"]["mass_kg"], self.payload["initial_mass_kg"])
        self.assertIn("no gravity or external forces", body["assumptions"])

    def test_endpoint_rejects_unphysical_direction(self):
        self.payload["segments"][0]["direction"] = [0.0, 0.0, 0.0]
        response = self.client.post("/api/admin/model-proof/dps-burn", json=self.payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("direction must be non-zero", response.json()["detail"])

    def test_endpoint_rejects_invalid_vector_shape(self):
        self.payload["initial_velocity_m_s"] = [0.0, 0.0]
        response = self.client.post("/api/admin/model-proof/dps-burn", json=self.payload)
        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()
