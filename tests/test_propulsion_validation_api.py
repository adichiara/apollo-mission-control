from pathlib import Path
import os
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fastapi.testclient import TestClient  # noqa: E402
from apollo_mission_control.live_app import app  # noqa: E402


class PropulsionValidationApiTests(unittest.TestCase):
    def setUp(self):
        self.token = "propulsion-validation-secret"
        self.headers = {"X-Apollo-Facilitator": self.token}
        self.env = patch.dict(
            os.environ,
            {"APOLLO_FACILITATOR_TOKEN": self.token},
            clear=False,
        )
        self.env.start()
        self.addCleanup(self.env.stop)
        self.client = TestClient(app)

    def _body(self):
        return {
            "initial_mass_lb": 95932.0,
            "full_thrust_lbf": 9870.0,
            "specific_impulse_s": 305.0,
            "step_s": 0.1,
            "segments": [
                {
                    "duration_s": 5.0,
                    "throttle_fraction": 0.126,
                    "direction": {"x": 1.0, "y": 0.0, "z": 0.0},
                },
                {
                    "duration_s": 21.0,
                    "throttle_fraction": 0.4,
                    "direction": {"x": 1.0, "y": 0.0, "z": 0.0},
                },
                {
                    "duration_s": 237.82,
                    "throttle_fraction": 1.0,
                    "direction": {"x": 1.0, "y": 0.0, "z": 0.0},
                },
            ],
        }

    def _run(self, body):
        response = self.client.post(
            "/api/validation/propulsion",
            json=body,
            headers=self.headers,
        )
        self.assertEqual(response.status_code, 200, response.text)
        return response.json()

    def test_validation_endpoint_requires_facilitator_authority(self):
        response = self.client.post(
            "/api/validation/propulsion",
            json=self._body(),
        )
        self.assertEqual(response.status_code, 401)

    def test_nominal_like_profile_returns_computed_physical_outputs(self):
        result = self._run(self._body())
        self.assertEqual(result["model"], "level_1_propulsion_delta_v")
        self.assertGreater(result["delta_v_magnitude_fps"], 0.0)
        self.assertGreater(result["propellant_used_lb"], 0.0)
        self.assertLess(result["final_mass_lb"], result["initial_mass_lb"])
        self.assertIn("no gravity/orbital propagation", result["scope"])

    def test_early_and_late_cutoff_change_outputs_without_new_branch(self):
        baseline = self._body()
        early = self._body()
        late = self._body()
        early["segments"][2]["duration_s"] -= 30.0
        late["segments"][2]["duration_s"] += 30.0

        base_result = self._run(baseline)
        early_result = self._run(early)
        late_result = self._run(late)

        self.assertLess(
            early_result["delta_v_magnitude_fps"],
            base_result["delta_v_magnitude_fps"],
        )
        self.assertGreater(
            late_result["delta_v_magnitude_fps"],
            base_result["delta_v_magnitude_fps"],
        )
        self.assertLess(
            early_result["propellant_used_lb"],
            base_result["propellant_used_lb"],
        )
        self.assertGreater(
            late_result["propellant_used_lb"],
            base_result["propellant_used_lb"],
        )

    def test_wrong_attitude_rotates_delta_v_vector(self):
        body = self._body()
        angle_rad = 10.0 * 3.141592653589793 / 180.0
        direction = {
            "x": 0.984807753012208,
            "y": 0.17364817766693033,
            "z": 0.0,
        }
        for segment in body["segments"]:
            segment["direction"] = direction

        straight = self._run(self._body())
        angled = self._run(body)

        self.assertAlmostEqual(
            straight["delta_v_magnitude_fps"],
            angled["delta_v_magnitude_fps"],
            places=6,
        )
        self.assertGreater(angled["delta_v_fps"]["y"], 0.0)
        self.assertLess(
            angled["delta_v_fps"]["x"],
            straight["delta_v_fps"]["x"],
        )
        self.assertGreater(angle_rad, 0.0)

    def test_dynamics_test_screen_is_deployed_validation_surface(self):
        response = self.client.get("/dynamics-test")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Causal Dynamics Test", response.text)
        self.assertIn("/api/validation/propulsion", response.text)
        self.assertIn("EARLY CUTOFF", response.text)
        self.assertIn("ATTITUDE OFFSET", response.text)


if __name__ == "__main__":
    unittest.main()
