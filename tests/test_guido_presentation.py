from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.controller_products import ProjectionSet  # noqa: E402
from apollo_mission_control.guido_presentation import (  # noqa: E402
    PROJECT_RENDERING_NOTICE,
    build_pc2_guido_presentation,
)
from apollo_mission_control.pc2_nominal import Product, Validity  # noqa: E402
from apollo_mission_control.product_integrity import ProductIntegrity  # noqa: E402


class GuidoPresentationTests(unittest.TestCase):
    def _projection(self):
        return ProjectionSet(
            "GUIDO",
            {
                "pg_ns.lgc.operating": Product(True, validity=Validity.VALID, source_layer="onboard/telemetry", provenance="test"),
                "pg_ns.lgc.program": Product("P40", validity=Validity.VALID, source_layer="onboard/telemetry", provenance="test"),
                "pg_ns.lgc.program_alarm": Product(None, validity=Validity.VALID, source_layer="onboard/telemetry", provenance="test"),
                "pg_ns.iss.warning": Product(False, validity=Validity.VALID, source_layer="onboard/telemetry", provenance="test"),
                "pg_ns.lgc.warning": Product(False, validity=Validity.VALID, source_layer="onboard/telemetry", provenance="test"),
                "pg_ns.alignment.accepted": Product(True, validity=Validity.VALID, source_layer="onboard/ground_assessment", provenance="test"),
                "pg_ns.state_vector_load_status": Product("verified", validity=Validity.VALID, source_layer="onboard/uplink", provenance="test"),
                "pg_ns.target_load_status": Product("verified", validity=Validity.VALID, source_layer="onboard/uplink", provenance="test"),
                "pg_ns.vg_imu_planned": Product({"x": 0.0, "y": 0.0, "z": 0.0}, units="ft/s", validity=Validity.VALID, source_layer="onboard/target", provenance="test"),
                "pg_ns.postburn_residual": Product(None, units="ft/s", validity=Validity.UNAVAILABLE, source_layer="onboard/telemetry", provenance="test"),
            },
            deferred_fields=("pg_ns.vg_remaining", "pg_ns.dv_gained"),
        )

    def test_screen_is_explicitly_project_rendering(self):
        presentation = build_pc2_guido_presentation(self._projection())
        self.assertEqual(presentation.notice, PROJECT_RENDERING_NOTICE)
        self.assertIn("not an exact historical CRT transcription", presentation.notice)

    def test_program_and_alarm_use_bounded_historical_analogues(self):
        presentation = build_pc2_guido_presentation(self._projection())
        fields = {field.key: field for section in presentation.sections for field in section.fields}
        self.assertEqual(fields["pg_ns.lgc.program"].label, "PROGRAM")
        self.assertIn("program/verb/noun", fields["pg_ns.lgc.program"].historical_analogue)
        self.assertIn("alarm-code", fields["pg_ns.lgc.program_alarm"].historical_analogue)

    def test_project_assessment_is_not_claimed_as_crt_literal(self):
        presentation = build_pc2_guido_presentation(self._projection())
        fields = {field.key: field for section in presentation.sections for field in section.fields}
        alignment = fields["pg_ns.alignment.accepted"]
        self.assertEqual(alignment.label, "ALIGNMENT")
        self.assertIn("project assessment product", alignment.historical_analogue)

    def test_deferred_fields_are_not_rendered_as_failed_telemetry(self):
        presentation = build_pc2_guido_presentation(self._projection())
        keys = {field.key for section in presentation.sections for field in section.fields}
        self.assertNotIn("pg_ns.vg_remaining", keys)
        self.assertNotIn("pg_ns.dv_gained", keys)

    def test_unavailable_postburn_residual_preserves_actual_product_validity(self):
        presentation = build_pc2_guido_presentation(self._projection())
        fields = {field.key: field for section in presentation.sections for field in section.fields}
        residual = fields["pg_ns.postburn_residual"]
        self.assertEqual(residual.validity, Validity.UNAVAILABLE.value)
        self.assertIsNone(residual.value)

    def test_hidden_integrity_metadata_is_not_rendered(self):
        projection = self._projection()
        projection.annotate_integrity(
            "pg_ns.lgc.program",
            integrity=ProductIntegrity.INCORRECT,
            integrity_reason="synthetic hidden fault",
        )
        presentation = build_pc2_guido_presentation(projection)
        fields = {field.key: field for section in presentation.sections for field in section.fields}
        self.assertEqual(fields["pg_ns.lgc.program"].value, "P40")
        self.assertFalse(hasattr(fields["pg_ns.lgc.program"], "integrity"))

    def test_rejects_non_guido_projection(self):
        with self.assertRaises(ValueError):
            build_pc2_guido_presentation(ProjectionSet("CONTROL"))


if __name__ == "__main__":
    unittest.main()
