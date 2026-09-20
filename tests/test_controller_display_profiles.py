from pathlib import Path
import json
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.controller_display_profiles import (  # noqa: E402
    CONTROLLER_DISPLAY_PROFILE_ROOT,
    discover_controller_display_profiles,
    get_controller_display_profile,
    load_controller_display_profile,
)


PROFILE_ID = "apollo11_msk1137_landing_radar_partial"


class ControllerDisplayProfileTests(unittest.TestCase):
    def test_apollo11_profile_preserves_mixed_source_nonbinding_boundary(self):
        profile = get_controller_display_profile(PROFILE_ID)

        self.assertEqual(profile.mission_profile_id, "apollo11_g")
        self.assertEqual(profile.display_id, "MSK-1137")
        self.assertTrue(profile.mixed_source_format_documented)
        self.assertFalse(profile.historical_value_binding_executable)
        self.assertFalse(profile.historical_display_timing_executable)
        self.assertGreater(len(profile.downstream_gates), 0)

        with self.assertRaisesRegex(ValueError, "historical field binding is unresolved"):
            profile.require_historical_value_binding()
        with self.assertRaisesRegex(ValueError, "historical display timing is unresolved"):
            profile.require_historical_display_timing()

    def test_profile_contains_only_semantically_controlled_partial_field_family(self):
        profile = get_controller_display_profile(PROFILE_ID)
        ids = {item.field_id for item in profile.fields}
        self.assertEqual(
            ids,
            {
                "lr_range_validity",
                "lr_velocity_validity",
                "lr_velocity_x_body",
                "lr_velocity_y_body",
                "lr_velocity_z_body",
                "lr_slant_range",
                "pgns_altitude",
                "actual_delta_v",
            },
        )

        self.assertEqual(profile.field("lr_velocity_x_body").label, "VXB")
        self.assertEqual(
            profile.field("lr_velocity_x_body").reference_frame,
            "LM body axes",
        )
        self.assertEqual(profile.field("pgns_altitude").unit_or_states, "ft")
        self.assertEqual(profile.field("actual_delta_v").data_origin, "ground_computed")

        for item in profile.fields:
            self.assertEqual(item.routing_status, "unresolved")
            self.assertFalse(item.historically_bindable)
            self.assertIsNone(item.source_identifier)
            self.assertGreater(len(item.provenance), 0)

    def test_public_payload_keeps_routing_and_timing_gates_explicit(self):
        payload = get_controller_display_profile(PROFILE_ID).to_public_dict()

        self.assertFalse(payload["historical_value_binding_executable"])
        self.assertFalse(payload["historical_display_timing_executable"])
        self.assertTrue(payload["mixed_source_format_documented"])
        self.assertTrue(
            all(not field["historically_bindable"] for field in payload["fields"])
        )

    def test_loader_rejects_source_identifier_on_unresolved_field(self):
        source = json.loads(
            (
                CONTROLLER_DISPLAY_PROFILE_ROOT
                / "apollo11_msk1137_landing_radar_partial.json"
            ).read_text(encoding="utf-8")
        )
        source["profile_id"] = "invalid_unresolved_identifier"
        source["fields"][0]["source_identifier"] = "invented_source"

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "profile.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "must not carry a source_identifier"):
                load_controller_display_profile(path)

    def test_loader_rejects_binding_executable_profile_with_unresolved_fields(self):
        source = json.loads(
            (
                CONTROLLER_DISPLAY_PROFILE_ROOT
                / "apollo11_msk1137_landing_radar_partial.json"
            ).read_text(encoding="utf-8")
        )
        source["profile_id"] = "invalid_binding_ready"
        source["historical_value_binding_executable"] = True

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "profile.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "cannot contain unresolved field routing"):
                load_controller_display_profile(path)

    def test_catalog_discovers_profile_once(self):
        records = discover_controller_display_profiles()
        matches = [record for record in records if record.profile_id == PROFILE_ID]
        self.assertEqual(len(matches), 1)


if __name__ == "__main__":
    unittest.main()
