"""Apollo 13 PC+2 premature DPS shutdown/restart decision logic.

The historical rule allowed a restart only when an early engine shutdown was
not caused by one of the listed shutdown criteria. This module evaluates that
branch without commanding or assuming a successful restart.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .shutdown_rules import RuleEvaluation, RuleState


class RestartDisposition(str, Enum):
    NOT_APPLICABLE = "not_applicable"
    RESTART_ELIGIBLE = "restart_eligible"
    DO_NOT_RESTART_RULE_SHUTDOWN = "do_not_restart_rule_shutdown"


@dataclass(frozen=True)
class RestartEvaluation:
    disposition: RestartDisposition
    basis: str
    triggered_rule_ids: tuple[str, ...] = ()
    noun97_flashing: bool | None = None


def evaluate_premature_shutdown_restart(
    evaluations: dict[str, RuleEvaluation],
    *,
    early_engine_stop_observed: bool,
    noun97_flashing: bool | None = None,
) -> RestartEvaluation:
    """Classify the documented restart branch.

    Noun 97 is retained as a crew-facing procedural cue from the contemporaneous
    read-up. It is not used to override a triggered shutdown criterion.
    """
    if not early_engine_stop_observed:
        return RestartEvaluation(
            RestartDisposition.NOT_APPLICABLE,
            "no premature engine shutdown observed",
            noun97_flashing=noun97_flashing,
        )

    triggered = tuple(
        rule_id
        for rule_id, item in evaluations.items()
        if item.state == RuleState.TRIGGERED
    )
    if triggered:
        return RestartEvaluation(
            RestartDisposition.DO_NOT_RESTART_RULE_SHUTDOWN,
            "Apollo 13 PC+2 restart was not authorized when early shutdown was due to a listed shutdown criterion",
            triggered_rule_ids=triggered,
            noun97_flashing=noun97_flashing,
        )

    return RestartEvaluation(
        RestartDisposition.RESTART_ELIGIBLE,
        "premature shutdown observed with no modeled listed shutdown criterion triggered",
        noun97_flashing=noun97_flashing,
    )
