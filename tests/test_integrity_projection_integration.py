from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.controller_decisions import (  # noqa: E402
    ControllerDecisionType,
    reject_product,
)
from apollo_mission_control.controller_products import ProjectionSet  # noqa: E402
from apollo_mission_control.pc2_nominal import Product, Validity  # noqa: E402
from apollo_mission_control.product_integrity import ProductIntegrity  # noqa: E402


class IntegrityProjectionIntegrationTests(unittest.TestCase):
    def test_hidden_integrity_annotation_does_not_change_visible_product(self):
        visible = Product(
            value={"roll": 12.0},
            units="deg",
            validity=Validity.VALID,
            source_layer="ground-derived/RTCC",
        )
        projection = ProjectionSet("GUIDO", {"ground.ags.body_angles": visible})

        annotated = projection.annotate_integrity(
            "ground.ags.body_angles",
            integrity=ProductIntegrity.INCORRECT,
            integrity_reason="synthetic RTCC processing fault",
        )

        self.assertEqual(projection.products["ground.ags.body_angles"].value, {"roll": 12.0})
        self.assertEqual(projection.products["ground.ags.body_angles"].validity, Validity.VALID)
        self.assertEqual(annotated.integrity, ProductIntegrity.INCORRECT)
        self.assertFalse(annotated.controller_detected_problem)

    def test_rejection_is_an_explicit_controller_event(self):
        event = reject_product(
            get_s=100.0,
            station="GUIDO",
            product_name="ground.ags.body_angles",
            basis="disagrees with independent FDAI reference",
            alternate_reference="crew.fdai.attitude",
        )

        self.assertEqual(event.decision, ControllerDecisionType.REJECT_PRODUCT)
        self.assertEqual(event.station, "GUIDO")
        self.assertEqual(event.alternate_reference, "crew.fdai.attitude")


if __name__ == "__main__":
    unittest.main()
