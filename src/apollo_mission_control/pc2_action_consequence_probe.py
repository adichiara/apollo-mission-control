"""PC+2 reference-scenario action consequence probes.

These probes exercise the authoritative PC2Session timing/action semantics with
four deliberately different player-action cases. They are validation fixtures,
not historical claims about how late a real controller decision could be.

"Late" here means only: the player decision occurs after a scheduled nominal
scenario milestone has already been recorded as missed under D-016. No grace
period or historical allowable-delay threshold is inferred.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from .pc2_nominal import hms_to_seconds
from .pc2_session import PC2Session


@dataclass(frozen=True)
class ActionConsequenceCase:
    case_id: str
    action_class: str
    decision_get_s: float | None
    action_accepted: bool | None
    rejection_reason: str | None
    flight_go: bool
    p40_active: bool
    engine_running: bool
    cutoff_complete: bool
    pending_gate: str | None
    session_status: str
    missed_events: tuple[str, ...]
    note: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _session(fixture: dict[str, Any], *, include_guido: bool = False) -> PC2Session:
    session = PC2Session.create(fixture)
    session.assign_station("flight", "FLIGHT")
    if include_guido:
        session.assign_station("guido", "GUIDO")
    session.start()
    return session


def _missed_events(session: PC2Session) -> tuple[str, ...]:
    return tuple(
        event.details.get("event")
        for event in session.audit_log
        if event.kind == "scenario_event_missed"
        and isinstance(event.details.get("event"), str)
    )


def _snapshot(
    session: PC2Session,
    *,
    case_id: str,
    action_class: str,
    decision_get_s: float | None,
    action_accepted: bool | None,
    rejection_reason: str | None = None,
    note: str,
) -> ActionConsequenceCase:
    return ActionConsequenceCase(
        case_id=case_id,
        action_class=action_class,
        decision_get_s=decision_get_s,
        action_accepted=action_accepted,
        rejection_reason=rejection_reason,
        flight_go=bool(session.state.flight_go),
        p40_active=bool(session.state.p40_active),
        engine_running=bool(session.state.engine_running),
        cutoff_complete=bool(session.state.cutoff_complete),
        pending_gate=session.pending_gate,
        session_status=session.status.value,
        missed_events=_missed_events(session),
        note=note,
    )


def run_pc2_action_consequence_matrix(
    fixture: dict[str, Any],
) -> dict[str, Any]:
    """Run correct, late, omitted, and wrong-action PC+2 reference probes."""

    # Correct/timely: GO is recorded after the poll opens but before the P40
    # nominal milestone, allowing the normal prerequisite chain to continue.
    correct = _session(fixture)
    correct.advance_to(hms_to_seconds("79:20:00"))
    correct.record_flight_go("flight", go=True, basis="synthetic timely GO probe")
    correct.advance_to(hms_to_seconds("79:29:00"))
    correct_case = _snapshot(
        correct,
        case_id="correct_timely_go",
        action_class="correct",
        decision_get_s=hms_to_seconds("79:20:00"),
        action_accepted=True,
        note=(
            "Timely FLIGHT GO precedes the scheduled P40 milestone; "
            "the downstream nominal preparation/ignition chain remains eligible."
        ),
    )

    # Late: the P40 milestone has already arrived and been missed before GO.
    # D-016 forbids replaying it after the fact.
    late = _session(fixture)
    late.advance_to(hms_to_seconds("79:24:00"))
    late.record_flight_go("flight", go=True, basis="synthetic late GO probe")
    late.advance_to(hms_to_seconds("79:29:00"))
    late_case = _snapshot(
        late,
        case_id="late_go_after_p40_milestone",
        action_class="late",
        decision_get_s=hms_to_seconds("79:24:00"),
        action_accepted=True,
        note=(
            "GO is accepted, but the already-missed P40 milestone is not replayed. "
            "This is D-016 event-order semantics, not a historical allowable-delay claim."
        ),
    )

    # Omitted: no GO is ever recorded. GET continues and dependent nominal
    # milestones are missed in place.
    omitted = _session(fixture)
    omitted.advance_to(hms_to_seconds("79:33:00"))
    omitted_case = _snapshot(
        omitted,
        case_id="omitted_go",
        action_class="omitted",
        decision_get_s=None,
        action_accepted=None,
        note=(
            "No GO is recorded. Mission time continues; dependent nominal burn "
            "milestones are missed rather than auto-authorized or replayed."
        ),
    )

    # Wrong actor: GUIDO attempts to issue the FLIGHT-only decision. The action
    # is rejected, the gate stays pending, and continuing time can still cause
    # the nominal milestone to be missed.
    wrong = _session(fixture, include_guido=True)
    wrong.advance_to(hms_to_seconds("79:18:00"))
    rejection_reason: str | None = None
    try:
        wrong.record_flight_go("guido", go=True, basis="synthetic wrong-actor probe")
        accepted = True
    except ValueError as exc:
        accepted = False
        rejection_reason = str(exc)
    wrong.advance_to(hms_to_seconds("79:24:00"))
    wrong_case = _snapshot(
        wrong,
        case_id="wrong_actor_go",
        action_class="wrong",
        decision_get_s=hms_to_seconds("79:18:00"),
        action_accepted=accepted,
        rejection_reason=rejection_reason,
        note=(
            "A non-FLIGHT player cannot clear the FLIGHT GO gate. Rejection does "
            "not pause GET, so the P40 milestone can still be missed."
        ),
    )

    return {
        "model_status": "pc2_action_consequence_reference_probe",
        "scope": (
            "Reference-scenario validation of authoritative session/action timing; "
            "not a historical delay-tolerance model"
        ),
        "late_semantics": (
            "after a scheduled nominal milestone has already been missed; "
            "no historical grace interval is implied"
        ),
        "cases": [
            correct_case.to_dict(),
            late_case.to_dict(),
            omitted_case.to_dict(),
            wrong_case.to_dict(),
        ],
    }
