"""Reusable prerequisite evaluation for source-timed scenario events.

A scenario event may have a nominal GET without being unconditionally executable.
This module evaluates declarative state requirements without deciding how a
session should react to failure. The session/engine may record the event as
missed, branch, or expose some other consequence.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable


@dataclass(frozen=True)
class StateRequirement:
    """One required authoritative-state value for an event to be eligible."""

    path: str
    expected: Any = True
    description: str = ""


@dataclass(frozen=True)
class EventEligibilityRule:
    """Declarative prerequisite set for one named scenario event."""

    event_name: str
    requirements: tuple[StateRequirement, ...]


def resolve_state_path(state: Any, path: str) -> Any:
    """Resolve a dotted attribute path from an authoritative state object."""
    value = state
    for part in path.split("."):
        value = getattr(value, part)
    return value


def evaluate_requirements(
    state: Any,
    requirements: Iterable[StateRequirement],
) -> tuple[bool, str | None]:
    """Return eligibility and a human-readable failure reason.

    All requirements must match exactly. The reason is intended for audit and
    scenario-authoring diagnostics, not as a player-facing diagnosis.
    """
    failures: list[str] = []
    for requirement in requirements:
        actual = resolve_state_path(state, requirement.path)
        if actual != requirement.expected:
            label = requirement.description or requirement.path
            failures.append(
                f"{label}: expected {requirement.expected!r}, observed {actual!r}"
            )
    if failures:
        return False, "; ".join(failures)
    return True, None


def evaluate_event_eligibility(
    state: Any,
    event_name: str,
    rules: dict[str, EventEligibilityRule],
) -> tuple[bool, str | None]:
    """Evaluate the declared prerequisite rule for ``event_name`` if present."""
    rule = rules.get(event_name)
    if rule is None:
        return True, None
    return evaluate_requirements(state, rule.requirements)
