from pathlib import Path
import json
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.controller_product_provenance import (  # noqa: E402
    ControllerFieldOrigin,
    HistoricalRoutingState,
    discover_controller_product_profiles,
    get_controller_product_profile,
    load_controller_product_profile,
)


class ControllerProductProvenanceTests(unittest.TestCase):
    def test_apollo11_profile_preserves_semantics_without_inventing_routes(self):
        profile = get_controller_product_profile("apollo11_msk1137_partial")
        self.assertEqual(profile.display_id, "MSK-1137")
        self.assertEqual(profile.mission_profile_id, "apollo11_g")
        self.assertFalse(profile.historical_rendering_executable)

        act_dv = profile.field("ACT_DELTA_V")
        self.assertEqual(act_dv.origin, ControllerFieldOrigin.GROUND_DERIVED)
        self.assertEqual(act_dv.routing_state, HistoricalRoutingState.PARTIAL)
        self.assertEqual(act_dv.unit, "ft/s")
        self.assertIsNone(act_dv.source_key)

        lr_velocity = profile.field("LR_BODY_VELOCITY_XYZ")
        self.assertEqual(lr_velocity.origin, ControllerFieldOrigin.UNRESOLVED)
        self.assertEqual(lr_velocity.routing_state, HistoricalRoutingState.UNRESOLVED)

    def test_partial_and_unresolved_historical_fields_are_withheld(self):
        profile = get_controller_product_profile("apollo11_msk1137_partial")
        values = profile.evaluate(
            {
                "ACT_DELTA_V": 9.9,
                "LR_BODY_VELOCITY_XYZ": [1, 2, 3],
            }
        )
        by_id = {item.definition.field_id: item for item in values}
        self.assertFalse(by_id["ACT_DELTA_V"].available)
        self.assertIsNone(by_id["ACT_DELTA_V"].value)
        self.assertEqual(
            by_id["ACT_DELTA_V"].reasons,
            ("historical_route_partial",),
        )
        self.assertFalse(by_id["LR_BODY_VELOCITY_XYZ"].available)
        self.assertEqual(
            by_id["LR_BODY_VELOCITY_XYZ"].reasons,
            ("historical_route_unresolved",),
        )

    def test_historical_profile_refuses_rendering_gate(self):
        profile = get_controller_product_profile("apollo11_msk1137_partial")
        with self.assertRaisesRegex(ValueError, "not historically executable"):
            profile.require_historical_rendering()

    def test_resolved_synthetic_profile_can_project_values(self):
        payload = {
            "profile_id": "synthetic",
            "mission_profile_id": "synthetic",
            "display_id": "SYNTH",
            "status": "test",
            "historical_rendering_executable": True,
            "fields": [
                {
                    "field_id": "F1",
                    "label": "F1",
                    "description": "synthetic resolved field",
                    "origin": "spacecraft_downlink",
                    "routing_state": "resolved",
                    "unit": "unit",
                    "source_key": "vehicle.signal",
                    "provenance": ["synthetic"],
                    "evidence_note": "synthetic",
                }
            ],
            "unresolved": [],
            "sources": ["synthetic"],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "profile.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            profile = load_controller_product_profile(path)

        values = profile.evaluate({"vehicle.signal": 12.5})
        self.assertTrue(values[0].available)
        self.assertEqual(values[0].value, 12.5)
        profile.require_historical_rendering()

    def test_unresolved_route_cannot_smuggle_source_binding(self):
        payload = {
            "profile_id": "bad",
            "mission_profile_id": "bad",
            "display_id": "BAD",
            "status": "test",
            "historical_rendering_executable": False,
            "fields": [
                {
                    "field_id": "F1",
                    "label": "F1",
                    "description": "bad unresolved field",
                    "origin": "unresolved",
                    "routing_state": "unresolved",
                    "source_key": "tempting.same_name",
                    "provenance": ["synthetic"],
                    "evidence_note": "synthetic",
                }
            ],
            "unresolved": ["route"],
            "sources": ["synthetic"],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "must not bind"):
                load_controller_product_profile(path)

    def test_claimed_historical_execution_requires_all_routes_resolved(self):
        payload = {
            "profile_id": "bad",
            "mission_profile_id": "bad",
            "display_id": "BAD",
            "status": "test",
            "historical_rendering_executable": True,
            "fields": [
                {
                    "field_id": "F1",
                    "label": "F1",
                    "description": "partial field",
                    "origin": "ground_derived",
                    "routing_state": "partial",
                    "provenance": ["synthetic"],
                    "evidence_note": "synthetic",
                }
            ],
            "unresolved": [],
            "sources": ["synthetic"],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "claims historical execution"):
                load_controller_product_profile(path)

    def test_profile_discovery_has_unique_ids(self):
        profiles = discover_controller_product_profiles()
        ids = [profile.profile_id for profile in profiles]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertIn("apollo11_msk1137_partial", ids)


if __name__ == "__main__":
    unittest.main()
