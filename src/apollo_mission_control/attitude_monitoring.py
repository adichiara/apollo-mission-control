"""Source-bounded Apollo 13 PC+2 attitude-error/rate rule helpers.

The operational thresholds follow the contemporaneous CAPCOM read-up and crew
readback. The postflight Mission Operations Report places the startup exception
on the other clause; that documentation discrepancy is preserved in research
note 062 rather than hidden here.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Mapping


class AttitudeRuleState(str, Enum):
    CLEAR = "clear"
    TRIGGERED = "triggered"
    NOT_EVALUABLE = "not_evaluable"
    NOT_APPLICABLE = "not_applicable"


@dataclass(frozen=True)
class AttitudeRuleResult:
    rule_id: str
    state: AttitudeRuleState
    threshold: float
    max_abs_value: float | None
    vector: Mapping[str, float] | None
    basis: str


def _max_abs(vector: Mapping[str, float] | None) -> float | None:
    if vector is None or not vector:
        return None
    return max(abs(float(value)) for value in vector.values())


def evaluate_attitude_error(
    vector_deg: Mapping[str, float] | None,
    *,
    threshold_deg: float = 10.0,
    startup_transient_exception_active: bool | None = False,
) -> AttitudeRuleResult:
    """Evaluate the crew-facing PC+2 attitude-error criterion.

    The exception is source-backed, but its exact time boundary is not. Callers
    must supply the transient context explicitly; this function never derives it
    from elapsed seconds or throttle phase.
    """
    maximum = _max_abs(vector_deg)
    if maximum is None:
        state = AttitudeRuleState.NOT_EVALUABLE
    elif maximum <= threshold_deg:
        state = AttitudeRuleState.CLEAR
    elif startup_transient_exception_active is True:
        state = AttitudeRuleState.NOT_APPLICABLE
    elif startup_transient_exception_active is None:
        state = AttitudeRuleState.NOT_EVALUABLE
    else:
        state = AttitudeRuleState.TRIGGERED

    return AttitudeRuleResult(
        "attitude_error",
        state,
        threshold_deg,
        maximum,
        vector_deg,
        "absolute attitude error > 10 deg; contemporaneous crew rule excepts startup transient",
    )


def evaluate_attitude_rate(
    vector_deg_s: Mapping[str, float] | None,
    *,
    threshold_deg_s: float = 10.0,
) -> AttitudeRuleResult:
    """Evaluate the contemporaneous crew-facing PC+2 attitude-rate criterion."""
    maximum = _max_abs(vector_deg_s)
    if maximum is None:
        state = AttitudeRuleState.NOT_EVALUABLE
    else:
        state = AttitudeRuleState.TRIGGERED if maximum > threshold_deg_s else AttitudeRuleState.CLEAR

    return AttitudeRuleResult(
        "attitude_rate",
        state,
        threshold_deg_s,
        maximum,
        vector_deg_s,
        "absolute attitude rate > 10 deg/s; no startup exception in CAPCOM read-up or crew readback",
    )
