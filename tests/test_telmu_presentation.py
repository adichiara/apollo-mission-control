from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.controller_products import ProjectionSet  # noqa: E402
from apollo_mission_control.pc2_nominal import Product, Validity  # noqa: E402
from apollo_mission_control.product_integrity import ProductIntegrity  # noqa: E402
from apollo_mission_control.telmu_presentation import (  # noqa: E402
    PROJECT_RENDERING_NOTICE,
    build_pc2_telmu_presentation,
)


class TelmuPresentationTests(unittest.TestCase):
    def _projection(self):
        return ProjectionSet(
            "TELMU",
            {
                "lm.power.mode": Product("burn_configuration", validity=Validity.VALID, source_layer="physical/configuration", provenance="test"),
                "lm.power.burn_configuration_expected_current_range_a": Product([38.0, 40.0], units="A", validity=Validity.VALID, source_layer="mission-report/reference", provenance="test"),
                "lm.inverter_warning": Product(False, validity=Validity.VALID, source_layer="onboard/telemetry", provenance="test"),
                "lm.inverter_switch_attempted": Product(False, validity=Validity.VALID, source_layer="crew/procedure-event", provenance="test"),
                "lm.inverter_switch_attempt_get_s": Product(None, units="s GET", validity=Validity.UNAVAILABLE, source_layer="crew/procedure-event", provenance="test"),
                "lm.powerdown.started": Product(False, validity=Validity.VALID, source_layer="physical/configuration", provenance="test"),
            },
            deferred_fields=("lm.power.current_a",),
        )

    def test_screen_is_explicitly_project_rendering(self):
        presentation = build_pc2_telmu_presentation(self._projection())
        self.assertEqual(presentation.notice, PROJECT_RENDERING_NOTICE)
        self.assertIn("not an exact historical CRT transcription", presentation.notice)

    def test_expected_current_range_is_clearly_reference_not_live_measurement(self):
        presentation = build_pc2_telmu_presentation(self._projection())
        fields = {field.key: field for section in presentation.sections for field in section.fields}
        current = fields["lm.power.burn_configuration_expected_current_range_a"]
        self.assertEqual(current.label, "BURN CONFIG CURRENT REF")
        self.assertEqual(current.units, "A")
        self.assertIn("reference range", current.historical_analogue)
        self.assertIn("not measured current", current.historical_analogue)

    def test_deferred_measured_current_is_not_rendered_as_failed_telemetry(self):
        presentation = build_pc2_telmu_presentation(self._projection())
        keys = {field.key for section in presentation.sections for field in section.fields}
        self.assertNotIn("lm.power.current_a", keys)

    def test_inverter_action_and_warning_remain_distinct(self):
        presentation = build_pc2_telmu_presentation(self._projection())
        fields = {field.key: field for section in presentation.sections for field in section.fields}
        self.assertIn("lm.inverter_warning", fields)
        self.assertIn("lm.inverter_switch_attempted", fields)
        self.assertNotEqual(fields["lm.inverter_warning"].label, fields["lm.inverter_switch_attempted"].label)

    def test_hidden_integrity_metadata_is_not_rendered(self):
        projection = self._projection()
        projection.annotate_integrity(
            "lm.inverter_warning",
            integrity=ProductIntegrity.INCORRECT,
            integrity_reason="synthetic hidden fault",
        )
        presentation = build_pc2_telmu_presentation(projection)
        fields = {field.key: field for section in presentation.sections for field in section.fields}
        self.assertFalse(hasattr(fields["lm.inverter_warning"], "integrity"))

    def test_rejects_non_telmu_projection(self):
        with self.assertRaises(ValueError):
            build_pc2_telmu_presentation(ProjectionSet("CONTROL"))


if __name__ == "__main__":
    unittest.main()
