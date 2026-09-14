"""Shared lifecycle contract for scenario runtimes.

This module contains only behavior already required by more than one planned
scenario class: authoritative GET, lifecycle state, timed-event progression,
station ownership/snapshots, readiness/FLIGHT/CAPCOM exchange, audit history,
and explicit scenario-state injection.

Scenario-specific controller procedures remain outside this protocol.
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Protocol, Sequence, runtime_checkable


class SessionStatus(str, Enum):
    CREATED = "created"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETE = "complete"


@runtime_checkable
class RuntimeState(Protocol):
    get_s: float
    phase: str


@runtime_checkable
class RuntimeEvent(Protocol):
    get_s: float


@runtime_checkable
class SessionRuntime(Protocol):
    """Minimum shared contract used by transport and realtime pacing."""

    state: RuntimeState
    events: Sequence[RuntimeEvent]
    status: SessionStatus
    pending_gate: str | None
    pause_reason: str | None
    station_assignments: dict[str, str]
    player_station_sets: dict[str, tuple[str, ...]]
    audit_log: list[Any]

    @property
    def available_stations(self) -> tuple[str, ...]: ...

    @property
    def assigned_stations(self) -> tuple[str, ...]: ...

    def start(self) -> None: ...
    def pause(self) -> None: ...
    def resume(self) -> None: ...
    def advance_to(self, target_get_s: float) -> float: ...

    def assign_stations(self, player_id: str, stations: Sequence[str]) -> None: ...
    def stations_for(self, player_id: str) -> tuple[str, ...]: ...
    def player_snapshot(self, player_id: str) -> Any: ...
    def bundled_player_snapshot(self, player_id: str) -> Any: ...

    def submit_readiness(
        self,
        player_id: str,
        *,
        ready: bool,
        note: str = "",
        station: str | None = None,
    ) -> Any: ...

    def record_flight_go(self, player_id: str, *, go: bool, basis: str) -> None: ...

    def queue_capcom_instruction(
        self,
        player_id: str,
        *,
        action: str,
        parameters: dict[str, Any],
        basis: str,
    ) -> Any: ...

    def transmit_capcom_item(self, player_id: str, item_id: int) -> Any: ...
    def apply_session_injection(self, injection: Any) -> None: ...
