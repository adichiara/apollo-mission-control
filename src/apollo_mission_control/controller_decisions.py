"""Controller decision/audit events.

These events record controller interpretation and action. They are intentionally
separate from product values and hidden simulator integrity metadata.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ControllerDecisionType(str, Enum):
    QUESTION_PRODUCT = "question_product"
    REJECT_PRODUCT = "reject_product"
    ACCEPT_ALTERNATE_REFERENCE = "accept_alternate_reference"


@dataclass(frozen=True)
class ControllerDecisionEvent:
    get_s: float
    station: str
    decision: ControllerDecisionType
    product_name: str
    basis: str
    alternate_reference: str | None = None


def reject_product(
    *,
    get_s: float,
    station: str,
    product_name: str,
    basis: str,
    alternate_reference: str | None = None,
) -> ControllerDecisionEvent:
    """Record explicit controller rejection; never infer this from hidden integrity."""
    return ControllerDecisionEvent(
        get_s=float(get_s),
        station=station,
        decision=ControllerDecisionType.REJECT_PRODUCT,
        product_name=product_name,
        basis=basis,
        alternate_reference=alternate_reference,
    )
