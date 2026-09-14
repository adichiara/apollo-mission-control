"""Mission-neutral guidance-computer alarm/restart state model.

The model represents alarm storage, alarm-light state, software-restart events,
and restart-protected program recovery using caller-supplied rules.

It does not decide abort/continue, infer hidden guidance validity, emulate an
AGC instruction set, or contain Apollo mission constants.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from math import isfinite
from typing import Mapping


def _finite(value: float, name: str) -> float:
    number = float(value)
    if not isfinite(number):
        raise ValueError(f"{name} must be finite")
    return number


def _text(value: str, name: str) -> str:
    result = str(value).strip()
    if not result:
        raise ValueError(f"{name} must not be empty")
    return result


@dataclass(frozen=True)
class ProgramAlarmRule:
    code: str
    meaning: str
    software_restart: bool

    def validated(self) -> "ProgramAlarmRule":
        return ProgramAlarmRule(
            code=_text(self.code, "alarm code"),
            meaning=_text(self.meaning, "alarm meaning"),
            software_restart=bool(self.software_restart),
        )


@dataclass(frozen=True)
class GuidanceComputerConfig:
    alarm_rules: Mapping[str, ProgramAlarmRule]
    restart_protected_programs: tuple[str, ...] = ()
    applicability: str = "generic guidance-computer model proof; not mission validated"
    provenance: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = (
        "alarm/restart classification is caller supplied",
        "restart-protected program identity is caller supplied",
        "no hidden abort/continue recommendation is generated",
        "no CPU scheduling or instruction-level emulation is performed",
        "guidance validity must be supplied/observed through separate model paths",
    )

    def validated(self) -> "GuidanceComputerConfig":
        if not self.alarm_rules:
            raise ValueError("at least one alarm rule is required")

        rules: dict[str, ProgramAlarmRule] = {}
        for raw_code, raw_rule in self.alarm_rules.items():
            key = _text(raw_code, "alarm rule key")
            rule = raw_rule.validated()
            if key != rule.code:
                raise ValueError(
                    f"alarm rule key {key!r} does not match rule code {rule.code!r}"
                )
            rules[key] = rule

        protected: list[str] = []
        for raw_program in self.restart_protected_programs:
            program = _text(raw_program, "restart-protected program")
            if program not in protected:
                protected.append(program)

        applicability = _text(self.applicability, "applicability")
        return GuidanceComputerConfig(
            alarm_rules=rules,
            restart_protected_programs=tuple(protected),
            applicability=applicability,
            provenance=tuple(self.provenance),
            assumptions=tuple(self.assumptions),
        )


@dataclass(frozen=True)
class GuidanceComputerState:
    time_s: float
    active_program: str
    program_alarm_active: bool = False
    active_alarm_code: str | None = None
    restart_count: int = 0
    recovery_status: str = "normal"
    alarm_history: tuple[str, ...] = ()

    def validated(self) -> "GuidanceComputerState":
        time_s = _finite(self.time_s, "time_s")
        active_program = _text(self.active_program, "active_program")
        if self.restart_count < 0:
            raise ValueError("restart_count must be non-negative")
        if self.program_alarm_active and not self.active_alarm_code:
            raise ValueError(
                "active_alarm_code is required when program_alarm_active is true"
            )
        return GuidanceComputerState(
            time_s=time_s,
            active_program=active_program,
            program_alarm_active=bool(self.program_alarm_active),
            active_alarm_code=(
                None
                if self.active_alarm_code is None
                else _text(self.active_alarm_code, "active_alarm_code")
            ),
            restart_count=int(self.restart_count),
            recovery_status=_text(self.recovery_status, "recovery_status"),
            alarm_history=tuple(_text(code, "alarm history code") for code in self.alarm_history),
        )


@dataclass(frozen=True)
class ProgramAlarmEvent:
    time_s: float
    code: str
    source: str = "program_detected"

    def validated(self) -> "ProgramAlarmEvent":
        return ProgramAlarmEvent(
            time_s=_finite(self.time_s, "alarm event time_s"),
            code=_text(self.code, "alarm event code"),
            source=_text(self.source, "alarm event source"),
        )


@dataclass(frozen=True)
class ProgramAlarmResult:
    state: GuidanceComputerState
    rule: ProgramAlarmRule
    source: str
    restart_occurred: bool
    restart_protected_recovery: bool
    applicability: str
    provenance: tuple[str, ...]
    assumptions: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "model_status": "guidance_alarm_model_proof_not_historically_validated",
            "state": {
                "time_s": self.state.time_s,
                "active_program": self.state.active_program,
                "program_alarm_active": self.state.program_alarm_active,
                "active_alarm_code": self.state.active_alarm_code,
                "restart_count": self.state.restart_count,
                "recovery_status": self.state.recovery_status,
                "alarm_history": list(self.state.alarm_history),
            },
            "alarm": {
                "code": self.rule.code,
                "meaning": self.rule.meaning,
                "source": self.source,
                "software_restart": self.rule.software_restart,
            },
            "restart_occurred": self.restart_occurred,
            "restart_protected_recovery": self.restart_protected_recovery,
            "applicability": self.applicability,
            "provenance": list(self.provenance),
            "assumptions": list(self.assumptions),
        }


def apply_program_alarm(
    state: GuidanceComputerState,
    event: ProgramAlarmEvent,
    config: GuidanceComputerConfig,
) -> ProgramAlarmResult:
    """Apply one caller-classified program alarm without deciding mission action."""

    checked_state = state.validated()
    checked_event = event.validated()
    checked_config = config.validated()

    if checked_event.time_s < checked_state.time_s:
        raise ValueError("alarm event time cannot move backward")

    rule = checked_config.alarm_rules.get(checked_event.code)
    if rule is None:
        raise ValueError(f"unknown alarm code for configured model: {checked_event.code}")

    restart_occurred = rule.software_restart
    restart_protected = (
        restart_occurred
        and checked_state.active_program in checked_config.restart_protected_programs
    )

    if restart_protected:
        recovery_status = "restart_protected_program_resumed"
    elif restart_occurred:
        recovery_status = "restart_occurred_program_recovery_unspecified"
    else:
        recovery_status = "alarm_without_software_restart"

    next_state = GuidanceComputerState(
        time_s=checked_event.time_s,
        active_program=checked_state.active_program,
        program_alarm_active=True,
        active_alarm_code=rule.code,
        restart_count=checked_state.restart_count + (1 if restart_occurred else 0),
        recovery_status=recovery_status,
        alarm_history=checked_state.alarm_history + (rule.code,),
    )

    return ProgramAlarmResult(
        state=next_state,
        rule=rule,
        source=checked_event.source,
        restart_occurred=restart_occurred,
        restart_protected_recovery=restart_protected,
        applicability=checked_config.applicability,
        provenance=checked_config.provenance,
        assumptions=checked_config.assumptions,
    )


def clear_program_alarm(
    state: GuidanceComputerState,
    *,
    time_s: float | None = None,
) -> GuidanceComputerState:
    """Clear the active alarm indication while retaining restart/alarm history."""

    checked = state.validated()
    target_time = checked.time_s if time_s is None else _finite(time_s, "time_s")
    if target_time < checked.time_s:
        raise ValueError("clear time cannot move backward")
    return replace(
        checked,
        time_s=target_time,
        program_alarm_active=False,
        active_alarm_code=None,
    )
