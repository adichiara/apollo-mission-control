"""Minimal procedural communication events for the Apollo 13 PC+2 slice.

These events record approved crew-facing instructions and crew completion
reports. They do not alter spacecraft state or infer procedure outcomes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class ProcedureCommunication:
    event_id: str
    get_s: float
    sender: str
    recipient: str
    kind: str
    action: str
    parameters: dict[str, Any]
    provenance: str


@dataclass
class ProcedureExchangeLog:
    events: list[ProcedureCommunication] = field(default_factory=list)

    def record(self, event: ProcedureCommunication) -> None:
        if event.kind not in {"instruction", "completion_report", "readback", "callout"}:
            raise ValueError(f"Unsupported procedure communication kind: {event.kind}")
        self.events.append(event)
        self.events.sort(key=lambda item: item.get_s)

    def for_action(self, action: str) -> list[ProcedureCommunication]:
        return [event for event in self.events if event.action == action]


def record_inverter_switch_instruction(
    log: ProcedureExchangeLog,
    *,
    event_id: str,
    get_s: float,
    provenance: str,
) -> None:
    """Record a CAPCOM request to perform the PC+2 inverter-switch contingency.

    Exact alternate-inverter identity remains unresolved, so no inverter number
    is accepted here.
    """
    log.record(
        ProcedureCommunication(
            event_id=event_id,
            get_s=get_s,
            sender="CAPCOM",
            recipient="CREW",
            kind="instruction",
            action="switch_lm_inverter",
            parameters={},
            provenance=provenance,
        )
    )


def record_inverter_switch_completion(
    log: ProcedureExchangeLog,
    *,
    event_id: str,
    get_s: float,
    provenance: str,
) -> None:
    """Record crew report that the requested switch action was performed.

    This communication event does not assert whether the inverter warning
    cleared or remained on; that is an independent observation.
    """
    log.record(
        ProcedureCommunication(
            event_id=event_id,
            get_s=get_s,
            sender="CREW",
            recipient="CAPCOM",
            kind="completion_report",
            action="switch_lm_inverter",
            parameters={},
            provenance=provenance,
        )
    )


def record_pc2_restart_instruction(
    log: ProcedureExchangeLog,
    *,
    event_id: str,
    get_s: float,
    provenance: str,
) -> None:
    """Record the documented PC+2 premature-shutdown restart sequence.

    The contemporaneous read-up gives the sequence as PRO, manual ullage,
    Engine Start push, and Descent Engine Command Override on. Recording the
    instruction does not imply that a restart is authorized for a rule-caused
    shutdown or that the engine actually restarts.
    """
    log.record(
        ProcedureCommunication(
            event_id=event_id,
            get_s=get_s,
            sender="CAPCOM",
            recipient="CREW",
            kind="instruction",
            action="pc2_premature_shutdown_restart",
            parameters={
                "sequence": [
                    "proceed_noun_97",
                    "manual_ullage",
                    "engine_start_push",
                    "descent_engine_command_override_on",
                ]
            },
            provenance=provenance,
        )
    )


def record_delta_p_shutdown_callout(
    log: ProcedureExchangeLog,
    *,
    event_id: str,
    get_s: float,
    delta_p_psi: float,
    provenance: str,
) -> None:
    """Record the PC+2 ground-only fuel/oxidizer Delta-P shutdown callout.

    The mission rule states that Delta-P greater than 25 psi requires a ground
    call to the crew and that the crew should shut down. CAPCOM is modeled as
    the air-ground sender; the exact CONTROL/FLIGHT internal voice-loop sequence
    and exact spoken wording are deliberately not asserted.
    """
    log.record(
        ProcedureCommunication(
            event_id=event_id,
            get_s=get_s,
            sender="CAPCOM",
            recipient="CREW",
            kind="callout",
            action="shutdown_dps_for_fuel_oxidizer_delta_p",
            parameters={
                "delta_p_psi": float(delta_p_psi),
                "criterion_psi": 25.0,
                "origin_discipline": "CONTROL",
            },
            provenance=provenance,
        )
    )
