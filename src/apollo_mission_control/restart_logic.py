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
    INSUFFICIENT_CONTEXT = "insufficient_context"


@dataclass(frozen=True)
class RestartEvaluation:
    disposition: RestartDisposition
    basis: str
    triggered_rule_ids: tuple[str, ...] = ()
    unresolved_rule_ids: tuple[str, ...] = ()
    noun97_flashing: bool | None = None


def evaluate_premature_shutdown_restart(
    evaluations: dict[str, RuleEvaluation],
    *,
    early_engine_stop_observed: bool,
    shutdown_cause_known_non_rule: bool = False,
    noun97_flashing: bool | None = None,
) -> RestartEvaluation:
    """Classify the documented restart branch conservatively.

    The source says restart only when the early shutdown was for a reason other
    than the listed shutdown criteria. Therefore the absence of a currently
    triggered modeled rule is not sufficient when historical criteria remain
    NOT_EVALUABLE. A positive non-rule cause classification is required before
    returning RESTART_ELIGIBLE.

    Noun 97 is retained as a crew-facing procedural cue from the contemporaneous
    read-up. It never overrides a triggered shutdown criterion.
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

    unresolved = tuple(
        rule_id
        for rule_id, item in evaluations.items()
        if item.state == RuleState.NOT_EVALUABLE
    )
    if not shutdown_cause_known_non_rule:
        return RestartEvaluation(
            RestartDisposition.INSUFFICIENT_CONTEXT,
            "premature shutdown observed, but the cause has not been affirmatively established as outside the listed PC+2 shutdown criteria",
            unresolved_rule_ids=unresolved,
            noun97_flashing=noun97_flashing,
        )

    return RestartEvaluation(
        RestartDisposition.RESTART_ELIGIBLE,
        "premature shutdown cause affirmatively classified as outside the listed PC+2 shutdown criteria",
        unresolved_rule_ids=unresolved,
        noun97_flashing=noun97_flashing,
    )
