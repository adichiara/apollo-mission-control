from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.capcom_presentation import build_pc2_capcom_presentation  # noqa: E402
from apollo_mission_control.controller_products import ProjectionSet  # noqa: E402
from apollo_mission_control.flight_presentation import build_pc2_flight_presentation  # noqa: E402
from apollo_mission_control.pc2_nominal import Product, Validity  # noqa: E402


class FlightCapcomPresentationTests(unittest.TestCase):
    def test_flight_omits_deferred_readiness_reports(self):
        projection = ProjectionSet(
            "FLIGHT",
            {
                "mission.phase": Product("pc2_final_readiness", validity=Validity.VALID, source_layer="mission/session", provenance="test"),
                "flight.go_for_burn": Product(False, validity=Validity.VALID, source_layer="controller-decision", provenance="test"),
            },
            deferred_fields=("controller.readiness_reports",),
        )
        presentation = build_pc2_flight_presentation(projection)
        keys = {field.key for field in presentation.fields}
        self.assertEqual(keys, {"mission.phase", "flight.go_for_burn"})
        self.assertNotIn("controller.readiness_reports", keys)

    def test_flight_go_is_presented_as_decision_state(self):
        projection = ProjectionSet(
            "FLIGHT",
            {
                "mission.phase": Product("pc2_go_for_burn", validity=Validity.VALID, source_layer="mission/session", provenance="test"),
                "flight.go_for_burn": Product(True, validity=Validity.VALID, source_layer="controller-decision", provenance="test"),
            },
        )
        presentation = build_pc2_flight_presentation(projection)
        fields = {field.key: field for field in presentation.fields}
        self.assertTrue(fields["flight.go_for_burn"].value)
        self.assertEqual(fields["flight.go_for_burn"].source_layer, "controller-decision")

    def test_capcom_contains_only_air_ground_pad_and_reports(self):
        projection = ProjectionSet(
            "CAPCOM",
            {
                "comm.air_ground_quality": Product("clear", validity=Validity.VALID, source_layer="communications", provenance="test"),
                "ground.pc2.final_pad": Product({"tig_get_s": 1.0}, validity=Validity.VALID, source_layer="ground-derived/procedure", provenance="test"),
                "crew.report_stream": Product([], validity=Validity.VALID, source_layer="crew-report", provenance="test"),
            },
        )
        presentation = build_pc2_capcom_presentation(projection)
        keys = {field.key for field in presentation.fields}
        self.assertEqual(keys, {"comm.air_ground_quality", "ground.pc2.final_pad", "crew.report_stream"})

    def test_capcom_can_show_explicit_crew_inverter_caution_report(self):
        projection = ProjectionSet(
            "CAPCOM",
            {
                "comm.air_ground_quality": Product("clear", validity=Validity.VALID, source_layer="communications", provenance="test"),
                "ground.pc2.final_pad": Product({"tig_get_s": 1.0}, validity=Validity.VALID, source_layer="ground-derived/procedure", provenance="test"),
                "crew.report_stream": Product([], validity=Validity.VALID, source_layer="crew-report", provenance="test"),
                "crew.inverter_warning_report": Product(True, validity=Validity.VALID, source_layer="crew-report", provenance="test"),
            },
        )
        presentation = build_pc2_capcom_presentation(projection)
        fields = {field.key: field for field in presentation.fields}
        self.assertTrue(fields["crew.inverter_warning_report"].value)
        self.assertEqual(fields["crew.inverter_warning_report"].source_layer, "crew-report")
        self.assertIn("not direct ground telemetry", fields["crew.inverter_warning_report"].historical_analogue)

    def test_presentations_reject_wrong_station(self):
        with self.assertRaises(ValueError):
            build_pc2_flight_presentation(ProjectionSet("CAPCOM"))
        with self.assertRaises(ValueError):
            build_pc2_capcom_presentation(ProjectionSet("FLIGHT"))


if __name__ == "__main__":
    unittest.main()
