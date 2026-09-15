from pathlib import Path
import json
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.measurement_profiles import (  # noqa: E402
    MEASUREMENT_PROFILE_ROOT,
    discover_measurement_profiles,
    get_measurement_profile,
    load_measurement_profile,
)


PROFILE_ID = "apollo13_lm7_inverter_electrical_partial"


class HistoricalMeasurementProfileTests(unittest.TestCase):
    def test_apollo13_inverter_profile_preserves_vehicle_vs_ground_boundary(self):
        profile = get_measurement_profile(PROFILE_ID)

        self.assertEqual(profile.mission_profile_id, "apollo13_h2")
        self.assertEqual(profile.vehicle_effectivity_id, "apollo13_lm7")
        self.assertTrue(profile.measurement_mapping_executable)
        self.assertFalse(profile.historical_ground_product_executable)
        self.assertGreater(len(profile.downstream_gates), 0)

        payload = profile.to_public_dict()
        self.assertEqual(
            payload["measurement_stage"],
            "vehicle_measurement_output_pre_ground_loading",
        )
        self.assertFalse(payload["historical_ground_product_executable"])

    def test_profile_contains_only_source_bounded_inverter_measurements(self):
        profile = get_measurement_profile(PROFILE_ID)

        self.assertEqual(
            {item.measurement_id for item in profile.measurements},
            {"GC0071V", "GC0155F"},
        )
        voltage = profile.measurement("GC0071V")
        frequency = profile.measurement("GC0155F")

        self.assertEqual(voltage.source_key, "inverter_bus_voltage_v_ac")
        self.assertEqual(voltage.unit, "V ac")
        self.assertEqual(frequency.source_key, "inverter_bus_frequency_hz")
        self.assertEqual(frequency.unit, "Hz")

        for item in profile.measurements:
            self.assertGreater(len(item.provenance), 0)
            self.assertIn(
                "project source_key is an implementation name",
                item.evidence_note,
            )

    def test_vehicle_measurement_mapping_evaluates_without_claiming_ground_product(self):
        profile = get_measurement_profile(PROFILE_ID)

        result = profile.evaluate_source_state(
            {
                "inverter_bus_voltage_v_ac": 115.0,
                "inverter_bus_frequency_hz": 400.0,
            }
        )

        self.assertEqual(result.measurement("GC0071V").value, 115.0)
        self.assertEqual(result.measurement("GC0155F").value, 400.0)
        self.assertTrue(result.measurement("GC0071V").applicable)
        self.assertTrue(result.measurement("GC0155F").applicable)
        self.assertIn("vehicle measurement boundary only", result.applicability)

        with self.assertRaisesRegex(ValueError, "historical ground product is unresolved"):
            profile.require_historical_ground_product()

    def test_catalog_discovers_unique_profile(self):
        profiles = discover_measurement_profiles()
        matches = [record for record in profiles if record.profile_id == PROFILE_ID]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].profile_path.parent, MEASUREMENT_PROFILE_ROOT)

    def test_loader_rejects_ground_ready_profile_with_unresolved_gates(self):
        source = json.loads(
            (
                MEASUREMENT_PROFILE_ROOT
                / "apollo13_lm7_inverter_electrical_partial.json"
            ).read_text(encoding="utf-8")
        )
        source["profile_id"] = "invalid_ground_ready"
        source["historical_ground_product_executable"] = True

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "profile.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "must not retain downstream_gates"):
                load_measurement_profile(path)

    def test_loader_rejects_duplicate_measurement_identity(self):
        source = json.loads(
            (
                MEASUREMENT_PROFILE_ROOT
                / "apollo13_lm7_inverter_electrical_partial.json"
            ).read_text(encoding="utf-8")
        )
        source["profile_id"] = "duplicate_measurement"
        source["measurements"].append(dict(source["measurements"][0]))

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "profile.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate historical measurement_id"):
                load_measurement_profile(path)


if __name__ == "__main__":
    unittest.main()
