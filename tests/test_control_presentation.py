from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.control_presentation import (  # noqa: E402
    PROJECT_RENDERING_NOTICE,
    build_pc2_control_presentation,
)
from apollo_mission_control.controller_products import ProjectionSet  # noqa: E402
from apollo_mission_control.pc2_nominal import Product, Validity  # noqa: E402
from apollo_mission_control.product_integrity import ProductIntegrity  # noqa: E402


class ControlPresentationTests(unittest.TestCase):
    def _projection(self):
        return ProjectionSet(
            "CONTROL",
            {
                "dps.engine_running": Product(True, validity=Validity.VALID, source_layer="physical/control", provenance="test"),
                "dps.throttle_command_phase": Product("maximum", validity=Validity.VALID, source_layer="command", provenance="test"),
                "dps.chamber_pressure_psi": Product(92.0, units="psi", validity=Validity.VALID, source_layer="measurement/telemetry", provenance="GQ6510P"),
                "dps.fuel_oxidizer_delta_p_psi": Product(12.0, units="psi", validity=Validity.VALID, source_layer="ground-derived/propulsion-monitoring", provenance="test"),
                "dps.engine_gimbal_warning": Product(False, validity=Validity.VALID, source_layer="onboard/telemetry", provenance="test"),
                "ces.dc_failure": Product(False, validity=Validity.VALID, source_layer="onboard/telemetry", provenance="test"),
                "rcs.ullage_active": Product(False, validity=Validity.VALID, source_layer="physical/control", provenance="test"),
                "rcs.ullage_jets_count": Product(0, validity=Validity.VALID, source_layer="physical/control", provenance="test"),
            },
            deferred_fields=("dps.inlet_pressure_psi",),
        )

    def test_screen_is_explicitly_project_rendering(self):
        presentation = build_pc2_control_presentation(self._projection())
        self.assertEqual(presentation.notice, PROJECT_RENDERING_NOTICE)
        self.assertIn("not an exact historical CRT transcription", presentation.notice)

    def test_psi_chamber_pressure_is_not_mislabeled_as_historical_tcp(self):
        presentation = build_pc2_control_presentation(self._projection())
        fields = {field.key: field for section in presentation.sections for field in section.fields}
        chamber = fields["dps.chamber_pressure_psi"]
        self.assertEqual(chamber.label, "CHAMBER P")
        self.assertEqual(chamber.units, "psi")
        self.assertNotEqual(chamber.label, "TCP")
        self.assertIn("MSK 1137 TCP", chamber.historical_analogue)
        self.assertIn("percent", chamber.historical_analogue)

    def test_deferred_project_gap_is_not_shown_as_unavailable_telemetry(self):
        presentation = build_pc2_control_presentation(self._projection())
        keys = {field.key for section in presentation.sections for field in section.fields}
        self.assertNotIn("dps.inlet_pressure_psi", keys)

    def test_hidden_integrity_metadata_is_not_rendered(self):
        projection = self._projection()
        projection.annotate_integrity(
            "dps.chamber_pressure_psi",
            integrity=ProductIntegrity.INCORRECT,
            integrity_reason="synthetic hidden fault",
        )
        presentation = build_pc2_control_presentation(projection)
        fields = {field.key: field for section in presentation.sections for field in section.fields}
        self.assertEqual(fields["dps.chamber_pressure_psi"].value, 92.0)
        self.assertFalse(hasattr(fields["dps.chamber_pressure_psi"], "integrity"))

    def test_rejects_non_control_projection(self):
        with self.assertRaises(ValueError):
            build_pc2_control_presentation(ProjectionSet("GUIDO"))


if __name__ == "__main__":
    unittest.main()
