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

    def test_malfunction_plan_endpoint_expands_one_failure_into_explicit_insertions_only(self):
        payload = {
            "malfunction_id": "synthetic-dual-layer",
            "description": "synthetic vehicle plus telemetry fault",
            "mode": "manual",
            "current_time_s": 10.0,
            "trigger_mode": "manual",
            "insertions": [
                {
                    "insertion_id": "vehicle-source",
                    "layer": "vehicle_system",
                    "target": "electrical.source_available",
                    "value": False,
                    "provenance": "synthetic browser/API test",
                },
                {
                    "insertion_id": "telemetry-channel",
                    "layer": "telemetry",
                    "target": "telemetry.channel_valid",
                    "value": False,
                    "provenance": "synthetic browser/API test",
                },
            ],
            "provenance": "synthetic malfunction-plan API proof",
        }
        response = self.client.post(
            "/api/admin/model-proof/malfunction-plan",
            json=payload,
        )
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(
            body["model_status"],
            "malfunction_plan_scheduler_proof_not_historically_validated",
        )
        activation = body["activation"]
        self.assertFalse(activation["applies_downstream_effects"])
        self.assertEqual(
            [item["layer"] for item in activation["insertions"]],
            ["vehicle_system", "telemetry"],
        )
        self.assertNotIn("outcome", activation)
        self.assertNotIn("diagnosis", activation)

    def test_time_dependent_malfunction_plan_endpoint_rejects_early_activation(self):
        payload = {
            "malfunction_id": "synthetic-timed",
            "description": "synthetic timed failure",
            "mode": "time_dependent",
            "activation_time_s": 20.0,
            "current_time_s": 19.0,
            "insertions": [
                {
                    "insertion_id": "source",
                    "layer": "vehicle_system",
                    "target": "source.state",
                    "value": "failed",
                    "provenance": "synthetic browser/API test",
                }
            ],
            "provenance": "synthetic timed plan proof",
        }
        response = self.client.post(
            "/api/admin/model-proof/malfunction-plan",
            json=payload,
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("not due until", response.json()["detail"])

    def test_resource_inventory_endpoint_exposes_depletion_and_shortfall(self):
        payload = {
            "initial_time_s": 0.0,
            "initial_quantities": {"energy": 5.0},
            "resources": [
                {
                    "resource_id": "energy",
                    "unit": "unit",
                    "minimum_quantity": 0.0,
                    "maximum_quantity": 5.0,
                }
            ],
            "segments": [
                {
                    "duration_s": 6.0,
                    "rates_per_s": {"energy": 1.0},
                    "label": "synthetic_load",
                }
            ],
            "applicability": "API resource test",
            "provenance": ["synthetic"],
        }
        response = self.client.post(
            "/api/admin/model-proof/resource-inventory",
            json=payload,
        )
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(
            body["model_status"],
            "resource_inventory_model_proof_not_historically_validated",
        )
        self.assertEqual(body["final_state"]["quantities"]["energy"], 0.0)
        self.assertEqual(body["unsatisfied_consumption"]["energy"], 1.0)
        self.assertEqual(body["boundary_events"][0]["time_s"], 5.0)

    def test_electrical_bus_endpoint_exposes_equipment_availability(self):
        payload = {
            "bus_id": "BUS",
            "sources": [{"source_id": "S", "max_power_w": 100.0}],
            "loads": [{"load_id": "receiver", "power_w": 20.0, "priority": 0}],
            "source_available": {"S": False},
            "load_commanded_on": {"receiver": True},
            "bus_enabled": True,
            "applicability": "API electrical test",
        }
        response = self.client.post(
            "/api/admin/model-proof/electrical-bus",
            json=payload,
        )
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(
            body["model_status"],
            "electrical_bus_model_proof_not_historically_validated",
        )
        self.assertFalse(body["loads"][0]["supplied"])
        self.assertEqual(body["loads"][0]["reason"], "no_available_source")

    def _resource_power_observation_payload(self, duration_s):
        return {
            "resource_inventory": {
                "initial_time_s": 0.0,
                "initial_quantities": {"energy": 5.0},
                "resources": [
                    {
                        "resource_id": "energy",
                        "unit": "unit",
                        "minimum_quantity": 0.0,
                        "maximum_quantity": 5.0,
                    }
                ],
                "segments": [
                    {
                        "duration_s": duration_s,
                        "rates_per_s": {"energy": 1.0},
                        "label": "synthetic_load",
                    }
                ],
                "applicability": "API causal-chain test",
            },
            "source_rules": [
                {
                    "source_id": "BATTERY",
                    "resource_id": "energy",
                    "minimum_operating_quantity": 0.0,
                    "available_at_threshold": False,
                    "provenance": "synthetic coupling",
                }
            ],
            "source_hardware_available": {"BATTERY": True},
            "electrical_bus": {
                "bus_id": "DATA_BUS",
                "sources": [{"source_id": "BATTERY", "max_power_w": 100.0}],
                "loads": [
                    {
                        "load_id": "TRACKING_RECEIVER",
                        "power_w": 20.0,
                        "priority": 0,
                    }
                ],
                "load_commanded_on": {"TRACKING_RECEIVER": True},
                "bus_enabled": True,
                "applicability": "API causal-chain electrical test",
            },
            "observation_load_id": "TRACKING_RECEIVER",
            "vehicle_time_s": duration_s,
            "vehicle_position_m": [1000.0, 0.0, 0.0],
            "vehicle_velocity_m_s": [1.0, 0.0, 0.0],
            "vehicle_mass_kg": 1000.0,
            "station_position_m": [0.0, 0.0, 0.0],
            "observation": {
                "upstream_valid": True,
                "source": "synthetic powered tracking product",
            },
        }

    def test_resource_power_observation_endpoint_propagates_causal_outage(self):
        before = self.client.post(
            "/api/admin/model-proof/resource-power-observation",
            json=self._resource_power_observation_payload(4.0),
        )
        after = self.client.post(
            "/api/admin/model-proof/resource-power-observation",
            json=self._resource_power_observation_payload(6.0),
        )

        self.assertEqual(before.status_code, 200)
        self.assertEqual(after.status_code, 200)

        before_body = before.json()
        after_body = after.json()

        self.assertEqual(
            before_body["model_status"],
            "resource_power_observation_chain_not_historically_validated",
        )
        self.assertTrue(before_body["source_coupling"][0]["available"])
        self.assertTrue(before_body["electrical_bus"]["loads"][0]["supplied"])
        self.assertTrue(before_body["tracking_observation"]["available"])
        self.assertIsNotNone(before_body["tracking_observation"]["range_m"])

        self.assertFalse(after_body["source_coupling"][0]["available"])
        self.assertFalse(after_body["electrical_bus"]["loads"][0]["supplied"])
        self.assertFalse(after_body["tracking_observation"]["available"])
        self.assertIsNone(after_body["tracking_observation"]["range_m"])

    def test_resource_power_chain_rejects_direct_source_availability_override(self):
        payload = self._resource_power_observation_payload(4.0)
        payload["electrical_bus"]["source_available"] = {"BATTERY": True}
        response = self.client.post(
            "/api/admin/model-proof/resource-power-observation",
            json=payload,
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("must be empty", response.json()["detail"])

    def test_guidance_alarm_endpoint_preserves_restart_without_mission_decision(self):
        payload = {
            "state_time_s": 10.0,
            "active_program": "P_SYNTH",
            "alarm_code": "A1",
            "alarm_meaning": "synthetic restart alarm",
            "software_restart": True,
            "restart_protected_programs": ["P_SYNTH"],
            "event_time_s": 11.0,
            "source": "synthetic_program_detected",
            "applicability": "API guidance alarm test",
            "provenance": ["synthetic"],
        }
        response = self.client.post(
            "/api/admin/model-proof/guidance-alarm",
            json=payload,
        )
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(
            body["model_status"],
            "guidance_alarm_model_proof_not_historically_validated",
        )
        self.assertTrue(body["restart_occurred"])
        self.assertTrue(body["restart_protected_recovery"])
        self.assertEqual(
            body["state"]["recovery_status"],
            "restart_protected_program_resumed",
        )
        self.assertNotIn("abort", body)
        self.assertNotIn("continue", body)

    def test_guidance_alarm_endpoint_exposes_unprotected_restart_as_unspecified(self):
        payload = {
            "active_program": "P_OTHER",
            "alarm_code": "A1",
            "alarm_meaning": "synthetic restart alarm",
            "software_restart": True,
            "restart_protected_programs": ["P_SYNTH"],
            "event_time_s": 1.0,
        }
        response = self.client.post(
            "/api/admin/model-proof/guidance-alarm",
            json=payload,
        )
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertFalse(body["restart_protected_recovery"])
        self.assertEqual(
            body["state"]["recovery_status"],
            "restart_occurred_program_recovery_unspecified",
        )

    def test_guidance_crosscheck_endpoint_preserves_pairwise_boundary(self):
        payload = {
            "first": {
                "source": "PRIMARY",
                "time_s": 10.0,
                "valid": True,
                "values": {"radial_velocity": 100.0},
                "provenance": ["synthetic"],
            },
            "second": {
                "source": "BACKUP",
                "time_s": 10.5,
                "valid": True,
                "values": {"radial_velocity": 101.0},
                "provenance": ["synthetic"],
            },
            "tolerances": {"radial_velocity": 2.0},
            "max_time_separation_s": 1.0,
            "applicability": "API guidance cross-check test",
            "provenance": ["synthetic"],
        }
        response = self.client.post(
            "/api/admin/model-proof/guidance-crosscheck",
            json=payload,
        )
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(
            body["model_status"],
            "guidance_crosscheck_model_not_historically_validated",
        )
        self.assertTrue(body["comparable"])
        self.assertTrue(body["agreement"])
        self.assertNotIn("truth_source", body)
        self.assertNotIn("abort", body)

    def test_guidance_consensus_endpoint_exposes_two_of_three_without_failure_label(self):
        payload = {
            "observations": [
                {
                    "source": "PRIMARY",
                    "time_s": 10.0,
                    "valid": True,
                    "values": {"radial_velocity": 100.0},
                },
                {
                    "source": "BACKUP",
                    "time_s": 10.0,
                    "valid": True,
                    "values": {"radial_velocity": 101.0},
                },
                {
                    "source": "GROUND",
                    "time_s": 10.0,
                    "valid": True,
                    "values": {"radial_velocity": 120.0},
                },
            ],
            "tolerances": {"radial_velocity": 2.0},
            "max_time_separation_s": 1.0,
            "minimum_agreeing_sources": 2,
            "applicability": "API guidance consensus test",
            "provenance": ["synthetic"],
        }
        response = self.client.post(
            "/api/admin/model-proof/guidance-consensus",
            json=payload,
        )
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(
            body["model_status"],
            "guidance_multisource_consensus_not_historically_validated",
        )
        field = body["fields"][0]
        self.assertEqual(field["status"], "consensus")
        self.assertEqual(field["consensus_sources"], ["PRIMARY", "BACKUP"])
        self.assertEqual(field["outside_consensus_sources"], ["GROUND"])
        self.assertNotIn("failed_sources", body)
        self.assertNotIn("truth_source", body)

    def _landing_radar_chain_payload(self):
        return {
            "time_s": 10.0,
            "guidance_time_s": 10.0,
            "data_good": True,
            "data_good_since_s": 5.0,
            "range_scale_last_changed_s": 8.0,
            "source": "synthetic radar",
            "channels": {
                "altitude": {
                    "measured_value": 1040.0,
                    "reference_value": 1000.0,
                    "unit": "m",
                    "valid": True,
                },
                "velocity_axis": {
                    "measured_value": 105.0,
                    "reference_value": 100.0,
                    "unit": "m/s",
                    "valid": True,
                },
            },
            "min_data_good_duration_s": 4.0,
            "min_range_scale_stable_s": 1.0,
            "scale_stability_channels": ["altitude"],
            "residual_rules": {
                "altitude": {
                    "fixed_tolerance": 200.0,
                    "proportional_tolerance": 0.125,
                },
                "velocity_axis": {
                    "fixed_tolerance": 7.5,
                    "proportional_tolerance": 0.125,
                },
            },
            "updates_enabled": True,
            "estimated_velocity_m_s": [500.0, 0.0, 0.0],
            "velocity_update_speed_threshold_m_s": 600.0,
            "altitude_channel": "altitude",
            "velocity_channel": "velocity_axis",
            "applicability": "API landing-radar chain test",
            "provenance": ["synthetic"],
        }

    def test_landing_radar_chain_exposes_quality_before_update_eligibility(self):
        response = self.client.post(
            "/api/admin/model-proof/landing-radar-quality-update",
            json=self._landing_radar_chain_payload(),
        )
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(
            body["model_status"],
            "landing_radar_quality_update_chain_not_historically_validated",
        )
        self.assertTrue(body["quality"]["data_good_qualified"])
        by_channel = {
            item["channel"]: item for item in body["quality"]["channels"]
        }
        self.assertTrue(by_channel["altitude"]["accepted"])
        self.assertTrue(by_channel["velocity_axis"]["accepted"])
        self.assertEqual(body["qualified_measurement"]["altitude_m"], 1040.0)
        self.assertEqual(
            body["qualified_measurement"]["velocity_m_s"],
            [105.0, 0.0, 0.0],
        )
        self.assertTrue(body["update_assessment"]["altitude_eligible"])
        self.assertTrue(body["update_assessment"]["velocity_eligible"])

    def test_landing_radar_chain_rejects_implicit_unit_conversion(self):
        payload = self._landing_radar_chain_payload()
        payload["channels"]["altitude"]["unit"] = "ft"
        response = self.client.post(
            "/api/admin/model-proof/landing-radar-quality-update",
            json=payload,
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "no implicit conversion",
            response.json()["detail"],
        )

    def test_pc2_action_consequence_matrix_endpoint(self):
        response = self.client.post(
            "/api/admin/model-proof/pc2-action-consequences",
            json={},
        )
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(
            body["model_status"],
            "pc2_action_consequence_reference_probe",
        )
        cases = {item["action_class"]: item for item in body["cases"]}
        self.assertTrue(cases["correct"]["engine_running"])
        self.assertFalse(cases["late"]["engine_running"])
        self.assertIn(
            "p40_active_final_preburn",
            cases["late"]["missed_events"],
        )
        self.assertIn(
            "dps_ignition",
            cases["omitted"]["missed_events"],
        )
        self.assertFalse(cases["wrong"]["action_accepted"])
        self.assertIn("no historical grace interval", body["late_semantics"])

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
