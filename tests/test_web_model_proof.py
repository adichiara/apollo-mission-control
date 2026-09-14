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


    def test_endpoint_accepts_linear_thrust_and_segment_isp_override(self):
        self.payload["segments"] = [
            {
                "duration_s": 5.0,
                "thrust_n": 0.0,
                "end_thrust_n": 5_000.0,
                "specific_impulse_s": 280.0,
                "regime": "startup",
                "direction": [1.0, 0.0, 0.0],
            },
            {
                "duration_s": 5.0,
                "thrust_n": 5_000.0,
                "end_thrust_n": 2_000.0,
                "regime": "blowdown",
                "direction": [1.0, 0.0, 0.0],
            },
        ]
        response = self.client.post("/api/admin/model-proof/dps-burn", json=self.payload)
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body["elapsed_s"], 10.0)
        self.assertGreater(body["impulse_n_s"], 0.0)
        self.assertLess(body["final_state"]["mass_kg"], self.payload["initial_mass_kg"])
        self.assertIn(
            "specific impulse is constant for the run unless a segment override is supplied",
            body["assumptions"],
        )


    def test_trajectory_tracking_endpoint_returns_observation_chain(self):
        payload = {
            "initial_time_s": 0.0,
            "initial_position_m": [1000.0, 0.0, 0.0],
            "initial_velocity_m_s": [0.0, 10.0, 0.0],
            "initial_mass_kg": 1000.0,
            "dry_mass_kg": 500.0,
            "specific_impulse_s": 300.0,
            "gravitational_parameter_m3_s2": 0.0,
            "max_step_s": 0.25,
            "applicability": "API chain test; not historical evidence",
            "provenance": ["synthetic API test"],
            "segments": [
                {
                    "duration_s": 10.0,
                    "thrust_n": 0.0,
                    "direction": [0.0, 0.0, 0.0],
                    "regime": "coast",
                }
            ],
            "station_position_m": [0.0, 0.0, 0.0],
            "station_velocity_m_s": [0.0, 0.0, 0.0],
            "observation": {
                "receive_delay_s": 2.0,
                "range_bias_m": 5.0,
                "range_rate_bias_m_s": 0.25,
                "available": True,
                "valid": True,
                "source": "synthetic tracking product",
                "provenance": ["synthetic observation config"],
            },
        }

        response = self.client.post(
            "/api/admin/model-proof/trajectory-tracking",
            json=payload,
        )
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(
            body["model_status"],
            "trajectory_tracking_chain_not_historically_validated",
        )
        trajectory = body["trajectory"]
        observation = body["tracking_observation"]

        self.assertEqual(
            trajectory["model_status"],
            "translational_model_proof_not_historically_validated",
        )
        self.assertEqual(trajectory["final_state"]["position_m"], [1000.0, 100.0, 0.0])
        self.assertEqual(observation["source_time_s"], 10.0)
        self.assertEqual(observation["received_time_s"], 12.0)
        self.assertEqual(observation["age_s"], 2.0)
        self.assertTrue(observation["available"])
        self.assertTrue(observation["valid"])
        self.assertGreater(observation["range_m"], 1000.0)

    def test_trajectory_tracking_endpoint_can_withhold_unavailable_product(self):
        payload = {
            "initial_position_m": [1000.0, 0.0, 0.0],
            "initial_velocity_m_s": [0.0, 0.0, 0.0],
            "initial_mass_kg": 1000.0,
            "dry_mass_kg": 500.0,
            "specific_impulse_s": 300.0,
            "segments": [
                {
                    "duration_s": 1.0,
                    "thrust_n": 0.0,
                    "direction": [0.0, 0.0, 0.0],
                }
            ],
            "station_position_m": [0.0, 0.0, 0.0],
            "observation": {
                "available": False,
                "valid": False,
                "source": "synthetic outage",
            },
        }

        response = self.client.post(
            "/api/admin/model-proof/trajectory-tracking",
            json=payload,
        )
        self.assertEqual(response.status_code, 200)
        observation = response.json()["tracking_observation"]
        self.assertIsNone(observation["range_m"])
        self.assertIsNone(observation["range_rate_m_s"])
        self.assertFalse(observation["available"])
        self.assertFalse(observation["valid"])

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
