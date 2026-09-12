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
    CALL_OUT_SHUTDOWN_CRITERION = "call_out_shutdown_criterion"


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


def call_out_shutdown_criterion(
    *,
    get_s: float,
    station: str,
    product_name: str,
    basis: str,
) -> ControllerDecisionEvent:
    """Record a controller decision to issue a ground-only shutdown callout.

    This event does not itself communicate with the crew or change spacecraft
    state. Those remain separate communication and operational-action layers.
    """
    return ControllerDecisionEvent(
        get_s=float(get_s),
        station=station,
        decision=ControllerDecisionType.CALL_OUT_SHUTDOWN_CRITERION,
        product_name=product_name,
        basis=basis,
    )
