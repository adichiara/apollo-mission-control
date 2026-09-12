"""Internal integrity metadata for controller-facing products.

Apollo 13 demonstrated that a ground-derived product could be wrong even when
spacecraft/source information was satisfactory. Integrity is therefore kept
separate from controller-facing availability/validity semantics.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from typing import Any

from .pc2_nominal import Product


class ProductIntegrity(str, Enum):
    CORRECT = "correct"
    INCORRECT = "incorrect"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class IntegrityAnnotatedProduct:
    product: Product
    integrity: ProductIntegrity = ProductIntegrity.CORRECT
    integrity_reason: str = ""
    controller_detected_problem: bool = False


def annotate_product(
    product: Product,
    *,
    integrity: ProductIntegrity = ProductIntegrity.CORRECT,
    integrity_reason: str = "",
    controller_detected_problem: bool = False,
) -> IntegrityAnnotatedProduct:
    """Attach internal truth metadata without changing the displayed product."""
    return IntegrityAnnotatedProduct(
        product=product,
        integrity=integrity,
        integrity_reason=integrity_reason,
        controller_detected_problem=controller_detected_problem,
    )


def corrupt_ground_product(
    product: Product,
    *,
    replacement_value: Any,
    integrity_reason: str,
) -> IntegrityAnnotatedProduct:
    """Return a wrong-but-present ground product.

    This deliberately preserves the product's existing validity field. The
    Apollo 13 post-MCC-5 AGS body-angle case does not establish that the bad
    RTCC readout carried an automatic controller-visible invalid flag.
    """
    corrupted = replace(product, value=replacement_value)
    return IntegrityAnnotatedProduct(
        product=corrupted,
        integrity=ProductIntegrity.INCORRECT,
        integrity_reason=integrity_reason,
        controller_detected_problem=False,
    )


def mark_controller_detection(
    annotated: IntegrityAnnotatedProduct,
) -> IntegrityAnnotatedProduct:
    """Record that a controller has rejected/questioned the product.

    This is audit/decision state, not an automatic change to the historical
    display value or its declared validity.
    """
    return replace(annotated, controller_detected_problem=True)
