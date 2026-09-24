from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.apollo11_descent_products import (  # noqa: E402
    APOLLO11_DESCENT_FIELDS,
    ProductRouteStatus,
    project_apollo11_descent_products,
)


class Apollo11DescentProductTests(unittest.TestCase):
    def test_schema_contains_source_backed_descent_and_alarm_fields(self):
        keys = {field.key for field in APOLLO11_DESCENT_FIELDS}
        for required in (
            "lr.range_data_good",
            "lr.velocity_data_good",
            "lr.vxb_fps",
            "lr.vyb_fps",
            "lr.vzb_fps",
            "lr.slant_range_ft",
            "pgns.altitude_ft",
            "guidance.tgo_s",
            "guidance.time_to_phase_end_s",
            "program.alarm_first",
            "program.alarm_second",
            "program.alarm_latest",
            "program.restart_count",
            "program.number",
            "dsky.verb",
            "dsky.noun",
            "dsky.flasher",
            "control.lr_antenna_position",
        ):
            self.assertIn(required, keys)

    def test_projection_uses_only_explicit_values(self):
        result = project_apollo11_descent_products(
            {
                "lr.range_data_good": True,
                "lr.slant_range_ft": 32000.0,
                "program.alarm_latest": "1202",
            },
            provenance=("synthetic contract test",),
        )

        self.assertTrue(result.product("lr.range_data_good").available)
        self.assertEqual(result.product("lr.slant_range_ft").value, 32000.0)
        self.assertEqual(result.product("program.alarm_latest").value, "1202")

        # Known but absent fields remain unavailable rather than being derived.
        self.assertFalse(result.product("pgns.altitude_ft").available)
        self.assertIsNone(result.product("pgns.altitude_ft").to_dict()["value"])
        self.assertFalse(result.product("control.lr_antenna_position").available)

    def test_lr_family_preserves_documented_downlink_family_without_exact_route(self):
        result = project_apollo11_descent_products({"lr.vxb_fps": 10.0})
        product = result.product("lr.vxb_fps")
        self.assertEqual(
            product.route_status,
            ProductRouteStatus.DOWNLINK_FAMILY_ROUTE_UNRESOLVED,
        )
        self.assertIn("LGC landing-radar downlink family", product.source_candidates)
        self.assertIn("exact downlink-to-display conversion unresolved", product.evidence_note)

    def test_mixed_dl_rtcc_candidate_is_not_collapsed_to_one_source(self):
        result = project_apollo11_descent_products({"pgns.altitude_ft": 31500.0})
        product = result.product("pgns.altitude_ft")
        self.assertEqual(
            product.route_status,
            ProductRouteStatus.MIXED_DOWNLINK_RTCC_UNRESOLVED,
        )
        self.assertEqual(product.source_candidates, ("D/L", "RTCC/ground processing"))

    def test_control_lr_position_remains_controller_reported_and_separate(self):
        result = project_apollo11_descent_products(
            {
                "control.lr_antenna_position": 2,
                "lr.range_data_good": False,
                "lr.velocity_data_good": True,
            }
        )
        position = result.product("control.lr_antenna_position")
        self.assertEqual(position.route_status, ProductRouteStatus.CONTROLLER_REPORTED)
        self.assertEqual(position.value, 2)
        self.assertFalse(result.product("lr.range_data_good").value)
        self.assertTrue(result.product("lr.velocity_data_good").value)

    def test_field_provenance_is_explicit_and_field_scoped(self):
        result = project_apollo11_descent_products(
            {"program.alarm_latest": "1202"},
            field_provenance={
                "program.alarm_latest": (
                    "Apollo 11 MSK-1137 field semantics",
                    "caller-supplied controller-visible observation",
                )
            },
        )
        self.assertEqual(
            result.product("program.alarm_latest").provenance,
            (
                "Apollo 11 MSK-1137 field semantics",
                "caller-supplied controller-visible observation",
            ),
        )

    def test_unknown_field_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown Apollo 11 descent product key"):
            project_apollo11_descent_products({"hidden.agc.truth": 123})

    def test_unknown_provenance_key_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown Apollo 11 descent provenance key"):
            project_apollo11_descent_products(
                {},
                field_provenance={"hidden.agc.truth": ("bad",)},
            )


if __name__ == "__main__":
    unittest.main()
