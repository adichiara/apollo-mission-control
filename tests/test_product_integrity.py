from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.pc2_nominal import Product, Validity  # noqa: E402
from apollo_mission_control.product_integrity import (  # noqa: E402
    ProductIntegrity,
    annotate_product,
    corrupt_ground_product,
    mark_controller_detection,
)


class ProductIntegrityTests(unittest.TestCase):
    def test_wrong_ground_product_can_remain_present_and_declared_valid(self):
        source = Product(
            value={"roll": 0.0, "pitch": 0.0, "yaw": 0.0},
            units="deg",
            validity=Validity.VALID,
            source_layer="ground-derived/RTCC",
            provenance="synthetic architecture test based on Apollo 13 post-MCC-5 AGS body-angle processing error",
        )

        bad = corrupt_ground_product(
            source,
            replacement_value={"roll": 12.0, "pitch": -8.0, "yaw": 17.0},
            integrity_reason="synthetic wrong-value fixture representing a ground-processing error class; values are not historical Apollo 13 angles",
        )

        self.assertEqual(bad.product.validity, Validity.VALID)
        self.assertEqual(bad.integrity, ProductIntegrity.INCORRECT)
        self.assertFalse(bad.controller_detected_problem)
        self.assertNotEqual(bad.product.value, source.value)

    def test_independent_reference_can_remain_correct(self):
        fdai_reference = Product(
            value={"ptc_established": True},
            validity=Validity.VALID,
            source_layer="independent/onboard-reference",
            provenance="architecture analogue of Apollo 13 FDAI cross-check",
        )
        annotated = annotate_product(fdai_reference)

        self.assertEqual(annotated.integrity, ProductIntegrity.CORRECT)
        self.assertEqual(annotated.product.validity, Validity.VALID)

    def test_controller_detection_is_not_automatic(self):
        product = Product(
            value="wrong-but-present",
            validity=Validity.VALID,
            source_layer="ground-derived",
        )
        bad = corrupt_ground_product(
            product,
            replacement_value="still-wrong",
            integrity_reason="synthetic ground transformation fault",
        )
        self.assertFalse(bad.controller_detected_problem)

        detected = mark_controller_detection(bad)
        self.assertTrue(detected.controller_detected_problem)
        self.assertEqual(detected.integrity, ProductIntegrity.INCORRECT)
        self.assertEqual(detected.product.validity, Validity.VALID)


if __name__ == "__main__":
    unittest.main()
