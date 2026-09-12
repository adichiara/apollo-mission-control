from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.controller_products import ProjectionSet  # noqa: E402
from apollo_mission_control.inco_presentation import (  # noqa: E402
    PROJECT_RENDERING_NOTICE,
    build_pc2_inco_presentation,
)
from apollo_mission_control.pc2_nominal import Product, Validity  # noqa: E402
from apollo_mission_control.product_integrity import ProductIntegrity  # noqa: E402


class IncoPresentationTests(unittest.TestCase):
    def _projection(self):
        return ProjectionSet(
            "INCO",
            {
                "comm.air_ground_quality": Product("weak", validity=Validity.VALID, source_layer="communications", provenance="test"),
                "comm.voice_available": Product(True, validity=Validity.VALID, source_layer="communications", provenance="test"),
                "comm.telemetry_available": Product(True, validity=Validity.VALID, source_layer="communications", provenance="test"),
                "comm.ranging_enabled": Product(False, validity=Validity.VALID, source_layer="communications/navigation", provenance="test"),
                "comm.uplink_state": Product("configuration_dependent", validity=Validity.VALID, source_layer="communications/command", provenance="test"),
            },
        )

    def test_screen_is_explicitly_project_rendering(self):
        presentation = build_pc2_inco_presentation(self._projection())
        self.assertEqual(presentation.notice, PROJECT_RENDERING_NOTICE)
        self.assertIn("not an exact historical CRT transcription", presentation.notice)

    def test_minimum_comm_products_are_present(self):
        presentation = build_pc2_inco_presentation(self._projection())
        keys = {field.key for section in presentation.sections for field in section.fields}
        self.assertEqual(
            keys,
            {
                "comm.air_ground_quality",
                "comm.voice_available",
                "comm.telemetry_available",
                "comm.ranging_enabled",
                "comm.uplink_state",
            },
        )

    def test_ranging_product_preserves_controller_state(self):
        presentation = build_pc2_inco_presentation(self._projection())
        fields = {field.key: field for section in presentation.sections for field in section.fields}
        self.assertFalse(fields["comm.ranging_enabled"].value)
        self.assertIn("78:21:54", fields["comm.ranging_enabled"].historical_analogue)

    def test_hidden_integrity_metadata_is_not_rendered(self):
        projection = self._projection()
        projection.annotate_integrity(
            "comm.air_ground_quality",
            integrity=ProductIntegrity.INCORRECT,
            integrity_reason="synthetic hidden fault",
        )
        presentation = build_pc2_inco_presentation(projection)
        fields = {field.key: field for section in presentation.sections for field in section.fields}
        self.assertEqual(fields["comm.air_ground_quality"].value, "weak")
        self.assertFalse(hasattr(fields["comm.air_ground_quality"], "integrity"))

    def test_rejects_non_inco_projection(self):
        with self.assertRaises(ValueError):
            build_pc2_inco_presentation(ProjectionSet("CONTROL"))


if __name__ == "__main__":
    unittest.main()
