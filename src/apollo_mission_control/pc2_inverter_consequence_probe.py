"""PC+2 inverter-contingency consequence probes.

These probes exercise the already-sourced inverter contingency through the
authoritative session/crew/rule layers. They test causal ordering, not historical
reaction time. No numeric response or persistence tolerance is inferred.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from .controller_products import project_controller_products
from .crew_response import (
    perform_inverter_transfer_from_callout,
    record_crew_receipt,
    record_inverter_transfer_completion_report,
)
from .pc2_nominal import hms_to_seconds
from .pc2_session import PC2Session
from .scenario_injection import EvidenceClass, StateInjection
from .shutdown_rules import evaluate_pc2_shutdown_rules


@dataclass(frozen=True)
class InverterConsequenceCase:
    case_id: str
    action_class: str
    transfer_authorized: bool
    transmitted: bool
    receipt_recorded: bool
    transfer_performed: bool
    completion_reported: bool
    action_rejected: bool
    rejection_reason: str | None
    pre_observation_rule_state: str
    post_observation_value: bool
    final_rule_state: str
    engine_running: bool
    note: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _burn_session(fixture: dict[str, Any]) -> PC2Session:
    session = PC2Session.create(fixture)
    session.assign_station("flight", "FLIGHT")
    session.assign_station("capcom", "CAPCOM")
    session.start()
    session.advance_to(hms_to_seconds("79:20:00"))
    session.record_flight_go(
        "flight",
        go=True,
        basis="synthetic inverter-consequence probe",
    )
    session.advance_to(hms_to_seconds("79:29:00"))
    return session


def _inject_warning(
    session: PC2Session,
    *,
    value: bool,
    injection_id: str,
    provenance: str,
) -> None:
    session.apply_session_injection(
        StateInjection(
            injection_id=injection_id,
            get_s=float(session.state.get_s),
            target="lm_inverter_warning",
            value=value,
            evidence_class=EvidenceClass.SOURCE_BOUNDED_TEST,
            provenance=provenance,
        )
    )


def _rule_state(session: PC2Session) -> str:
    result = evaluate_pc2_shutdown_rules(
        project_controller_products(session.state, session.fixture),
        session.fixture,
    )
    return result["persistent_inverter_warning"].state.value


def _authorize_and_transmit(session: PC2Session):
    item = session.queue_inverter_transfer_instruction(
        "flight",
        basis="synthetic inverter-consequence probe",
    )
    session.transmit_capcom_item("capcom", item.item_id)
    return item


def _fresh_observation(session: PC2Session, value: bool, case_id: str) -> None:
    # The increment establishes event ordering only; it is not a sourced dwell.
    session.advance_to(float(session.state.get_s) + 0.1)
    _inject_warning(
        session,
        value=value,
        injection_id=f"{case_id}-post-transfer-observation",
        provenance=(
            "synthetic fresh post-transfer inverter observation; "
            "0.1 s establishes ordering only and is not a historical dwell"
        ),
    )


def run_pc2_inverter_consequence_matrix(
    fixture: dict[str, Any],
) -> dict[str, Any]:
    """Run bounded inverter action/observation consequence cases."""

    # Correct chain: warning -> authorization/transmission -> receipt -> sourced
    # crew transfer -> completion report -> fresh warning -> triggered rule.
    correct = _burn_session(fixture)
    _inject_warning(
        correct,
        value=True,
        injection_id="correct-initial-warning",
        provenance="synthetic initial inverter warning for consequence probe",
    )
    item = _authorize_and_transmit(correct)
    record_crew_receipt(correct, item.item_id)
    perform_inverter_transfer_from_callout(correct, item.item_id)
    record_inverter_transfer_completion_report(correct, item.item_id)
    correct_pre = _rule_state(correct)
    _fresh_observation(correct, True, "correct")
    correct_case = InverterConsequenceCase(
        case_id="correct_transfer_fresh_warning",
        action_class="correct",
        transfer_authorized=True,
        transmitted=True,
        receipt_recorded=True,
        transfer_performed=True,
        completion_reported=True,
        action_rejected=False,
        rejection_reason=None,
        pre_observation_rule_state=correct_pre,
        post_observation_value=True,
        final_rule_state=_rule_state(correct),
        engine_running=bool(correct.state.engine_running),
        note=(
            "The sourced crew transfer and completion report do not trigger the "
            "rule by themselves; a fresh post-transfer warning is required."
        ),
    )

    # Omitted transfer: a later warning alone cannot satisfy the criterion.
    omitted = _burn_session(fixture)
    _inject_warning(
        omitted,
        value=True,
        injection_id="omitted-initial-warning",
        provenance="synthetic initial inverter warning for omitted-action probe",
    )
    omitted_pre = _rule_state(omitted)
    _fresh_observation(omitted, True, "omitted")
    omitted_case = InverterConsequenceCase(
        case_id="omitted_transfer",
        action_class="omitted",
        transfer_authorized=False,
        transmitted=False,
        receipt_recorded=False,
        transfer_performed=False,
        completion_reported=False,
        action_rejected=False,
        rejection_reason=None,
        pre_observation_rule_state=omitted_pre,
        post_observation_value=True,
        final_rule_state=_rule_state(omitted),
        engine_running=bool(omitted.state.engine_running),
        note=(
            "Repeated warning observations without the required crew transfer "
            "leave the persistent-warning rule not evaluable."
        ),
    )

    # Wrong order: transmission does not permit crew action before explicit receipt.
    wrong = _burn_session(fixture)
    _inject_warning(
        wrong,
        value=True,
        injection_id="wrong-order-initial-warning",
        provenance="synthetic initial inverter warning for wrong-order probe",
    )
    wrong_item = _authorize_and_transmit(wrong)
    rejection_reason: str | None = None
    try:
        perform_inverter_transfer_from_callout(wrong, wrong_item.item_id)
        rejected = False
    except ValueError as exc:
        rejected = True
        rejection_reason = str(exc)
    wrong_pre = _rule_state(wrong)
    _fresh_observation(wrong, True, "wrong-order")
    wrong_case = InverterConsequenceCase(
        case_id="wrong_order_action_before_receipt",
        action_class="wrong_order",
        transfer_authorized=True,
        transmitted=True,
        receipt_recorded=False,
        transfer_performed=False,
        completion_reported=False,
        action_rejected=rejected,
        rejection_reason=rejection_reason,
        pre_observation_rule_state=wrong_pre,
        post_observation_value=True,
        final_rule_state=_rule_state(wrong),
        engine_running=bool(wrong.state.engine_running),
        note=(
            "CAPCOM transmission alone is insufficient; the deterministic crew "
            "actor rejects action before explicit receipt."
        ),
    )

    # Cleared condition: correct transfer followed by a fresh clear observation
    # produces CLEAR, not a triggered shutdown criterion.
    cleared = _burn_session(fixture)
    _inject_warning(
        cleared,
        value=True,
        injection_id="cleared-initial-warning",
        provenance="synthetic initial inverter warning for cleared-condition probe",
    )
    cleared_item = _authorize_and_transmit(cleared)
    record_crew_receipt(cleared, cleared_item.item_id)
    perform_inverter_transfer_from_callout(cleared, cleared_item.item_id)
    record_inverter_transfer_completion_report(cleared, cleared_item.item_id)
    cleared_pre = _rule_state(cleared)
    _fresh_observation(cleared, False, "cleared")
    cleared_case = InverterConsequenceCase(
        case_id="correct_transfer_warning_clears",
        action_class="cleared",
        transfer_authorized=True,
        transmitted=True,
        receipt_recorded=True,
        transfer_performed=True,
        completion_reported=True,
        action_rejected=False,
        rejection_reason=None,
        pre_observation_rule_state=cleared_pre,
        post_observation_value=False,
        final_rule_state=_rule_state(cleared),
        engine_running=bool(cleared.state.engine_running),
        note=(
            "A fresh clear observation after the sourced transfer clears the "
            "criterion; the transfer itself does not predetermine the outcome."
        ),
    )

    return {
        "model_status": "pc2_inverter_consequence_reference_probe",
        "scope": (
            "Reference-scenario validation of inverter action/observation causality; "
            "not a historical reaction-time or failure-occurrence model"
        ),
        "ordering_increment_s": 0.1,
        "ordering_increment_meaning": (
            "synthetic event-order separator only; no historical dwell or "
            "allowable response time is implied"
        ),
        "cases": [
            correct_case.to_dict(),
            omitted_case.to_dict(),
            wrong_case.to_dict(),
            cleared_case.to_dict(),
        ],
    }
