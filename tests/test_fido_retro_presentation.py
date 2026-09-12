from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.controller_products import ProjectionSet  # noqa: E402
from apollo_mission_control.fido_retro_presentation import (  # noqa: E402
    PROJECT_RENDERING_NOTICE,
    build_pc2_fido_retro_presentation,
)
from apollo_mission_control.pc2_nominal import Product, Validity  # noqa: E402
from apollo_mission_control.product_integrity import ProductIntegrity  # noqa: E402


class FidoRetroPresentationTests(unittest.TestCase):
    def _projection(self):
        return ProjectionSet(
            "FIDO_RETRO",
            {
                "ground.pc2.tig_get_s": Product(286058.30, units="s GET", validity=Validity.VALID, source_layer="ground-derived", provenance="test"),
                "ground.pc2.pad_dv_lvlh": Product({"x": 833.0, "y": -50.9, "z": -213.9, "resultant": 861.5}, units="ft/s", validity=Validity.VALID, source_layer="ground-derived", provenance="test"),
                "ground.pc2.expected_perigee_nmi": Product(20.5, units="nmi", validity=Validity.VALID, source_layer="ground-derived", provenance="test"),
                "ground.return.plan": Product({"landing_lat_deg": -21.65, "landing_lon_deg": -165.0, "range_to_go_005g_nmi": 1163.5, "velocity_005g_fps": 36292.0, "get_005g_hms": "142:39:22"}, validity=Validity.VALID, source_layer="ground-derived", provenance="test"),
                "ground.rtcc.solution_valid": Product(True, validity=Validity.VALID, source_layer="ground-derived", provenance="test"),
            },
            deferred_fields=("ground.rtcc.cartesian_state_vector", "ground.postburn.propagated_trajectory"),
        )

    def test_screen_is_explicitly_project_rendering(self):
        presentation = build_pc2_fido_retro_presentation(self._projection())
        self.assertEqual(presentation.notice, PROJECT_RENDERING_NOTICE)
        self.assertIn("not an exact historical CRT transcription", presentation.notice)

    def test_final_target_and_monitor_pad_products_are_present(self):
        presentation = build_pc2_fido_retro_presentation(self._projection())
        fields = {field.key: field for section in presentation.sections for field in section.fields}
        self.assertEqual(fields["ground.pc2.expected_perigee_nmi"].value, 20.5)
        self.assertEqual(fields["ground.return.plan"].value["landing_lat_deg"], -21.65)
        self.assertEqual(fields["ground.return.plan"].value["get_005g_hms"], "142:39:22")

    def test_deferred_trajectory_products_are_not_shown_as_failed_data(self):
        presentation = build_pc2_fido_retro_presentation(self._projection())
        keys = {field.key for section in presentation.sections for field in section.fields}
        self.assertNotIn("ground.rtcc.cartesian_state_vector", keys)
        self.assertNotIn("ground.postburn.propagated_trajectory", keys)

    def test_hidden_integrity_metadata_is_not_rendered(self):
        projection = self._projection()
        projection.annotate_integrity(
            "ground.rtcc.solution_valid",
            integrity=ProductIntegrity.INCORRECT,
            integrity_reason="synthetic hidden processing fault",
        )
        presentation = build_pc2_fido_retro_presentation(projection)
        fields = {field.key: field for section in presentation.sections for field in section.fields}
        self.assertFalse(hasattr(fields["ground.rtcc.solution_valid"], "integrity"))

    def test_rejects_non_fido_retro_projection(self):
        with self.assertRaises(ValueError):
            build_pc2_fido_retro_presentation(ProjectionSet("FIDO"))


if __name__ == "__main__":
    unittest.main()
