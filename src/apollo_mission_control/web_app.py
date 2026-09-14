"""Thin FastAPI transport for the Apollo Mission Control PC+2 prototype.

The simulation/domain layer remains framework-neutral. This module owns only
HTTP request/response adaptation, an in-memory single-session registry, realtime
wall-clock pacing, facilitator authorization, and static prototype delivery.
"""

from __future__ import annotations

import hmac
import os
from pathlib import Path
from threading import RLock
from typing import Any, Callable

from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from .causal_dps_model import (
    BurnSegment,
    DPSModelConfig,
    ManeuverState,
    simulate_dps_maneuver,
)
from .crew_response import (
    apply_session_engine_off_response,
    command_dps_shutdown_from_callout,
    record_crew_receipt,
)
from .pc2_session import PC2Session
from .realtime_clock import RealtimeSessionClock
from .scenario_catalog import (
    DEFAULT_SCENARIO_ID,
    ScenarioRecord,
    discover_scenarios,
    get_scenario_record,
    load_scenario_fixture,
)
from .scenario_injection import EvidenceClass, StateInjection
from .session_shutdown_evidence import (
    assess_session_shutdown_evidence,
    record_crew_shutdown_report,
)

ROOT = Path(__file__).resolve().parents[2]
WEB_ROOT = ROOT / "web"
SUPPORTED_RUNTIME_ADAPTERS = frozenset({"pc2_v1"})
FACILITATOR_TOKEN_ENV = "APOLLO_FACILITATOR_TOKEN"

app = FastAPI(
    title="Apollo Mission Control",
    description="Reusable Apollo Mission Control simulation API",
    version="0.1.0",
)

_lock = RLock()
_session: PC2Session | None = None
_clock: RealtimeSessionClock | None = None
_active_scenario: ScenarioRecord | None = None


class JoinRequest(BaseModel):
    player_id: str = Field(min_length=1, max_length=64)
    station: str = Field(min_length=1, max_length=32)


class JoinSetRequest(BaseModel):
    player_id: str = Field(min_length=1, max_length=64)
    stations: list[str] = Field(min_length=1, max_length=7)


class AdvanceRequest(BaseModel):
    target_get_s: float


class ReadinessRequest(BaseModel):
    ready: bool
    note: str = Field(default="", max_length=500)
    station: str | None = Field(default=None, min_length=1, max_length=32)


class FlightDecisionRequest(BaseModel):
    go: bool
    basis: str = Field(min_length=1, max_length=1000)


class CapcomQueueRequest(BaseModel):
    action: str = Field(min_length=1, max_length=128)
    parameters: dict[str, Any] = Field(default_factory=dict)
    basis: str = Field(min_length=1, max_length=1000)


class StateInjectionRequest(BaseModel):
    injection_id: str = Field(min_length=1, max_length=128)
    target: str = Field(min_length=1, max_length=128)
    value: Any
    evidence_class: EvidenceClass
    provenance: str = Field(min_length=1, max_length=2000)


class ControlDeltaPCalloutRequest(BaseModel):
    basis: str = Field(min_length=1, max_length=1000)


class CrewReceiptRequest(BaseModel):
    crew_id: str = Field(default="CREW", min_length=1, max_length=64)
    response: str = Field(default="received", min_length=1, max_length=500)


class CrewShutdownRequest(BaseModel):
    crew_id: str = Field(default="CREW", min_length=1, max_length=64)
    provenance: str = Field(
        default=(
            "Apollo 13 PC+2 ground-call shutdown rule; "
            "exact cockpit choreography unresolved"
        ),
        min_length=1,
        max_length=2000,
    )


class CrewShutdownReportRequest(BaseModel):
    crew_id: str = Field(default="CREW", min_length=1, max_length=64)


class EngineOffResponseRequest(BaseModel):
    cause: str = Field(default="crew_stop_pushbutton", min_length=1, max_length=128)


class BurnSegmentRequest(BaseModel):
    duration_s: float = Field(ge=0.0, le=7200.0)
    thrust_n: float = Field(ge=0.0, le=1_000_000.0)
    direction: list[float] = Field(min_length=3, max_length=3)
    end_thrust_n: float | None = Field(default=None, ge=0.0, le=1_000_000.0)
    specific_impulse_s: float | None = Field(default=None, gt=0.0, le=10_000.0)
    regime: str = Field(default="regulated", min_length=1, max_length=64)


class DPSModelProofRequest(BaseModel):
    initial_time_s: float = 0.0
    initial_mass_kg: float = Field(gt=0.0, le=1_000_000.0)
    dry_mass_kg: float = Field(ge=0.0, le=1_000_000.0)
    initial_velocity_m_s: list[float] = Field(
        default_factory=lambda: [0.0, 0.0, 0.0],
        min_length=3,
        max_length=3,
    )
    specific_impulse_s: float = Field(gt=0.0, le=10_000.0)
    max_step_s: float = Field(default=0.25, gt=0.0, le=60.0)
    applicability: str = Field(
        default="generic model proof; not mission validated",
        min_length=1,
        max_length=500,
    )
    provenance: list[str] = Field(default_factory=list, max_length=20)
    segments: list[BurnSegmentRequest] = Field(min_length=1, max_length=50)


def _require_session() -> PC2Session:
    if _session is None:
        raise HTTPException(status_code=409, detail="No PC+2 session has been created")
    return _session


def _require_clock() -> RealtimeSessionClock:
    if _clock is None:
        raise HTTPException(status_code=409, detail="No PC+2 session clock has been created")
    return _clock


def _sync_session() -> PC2Session:
    session = _require_session()
    _require_clock().sync()
    return session


def _domain_call(call: Callable[[], Any]) -> Any:
    try:
        return call()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


def _facilitator_guard(
    x_apollo_facilitator: str | None = Header(default=None),
) -> None:
    """Protect facilitator/SimSup operations without conflating them with stations."""
    expected = os.getenv(FACILITATOR_TOKEN_ENV)
    if not expected:
        if os.getenv("RENDER", "").lower() == "true":
            raise HTTPException(
                status_code=503,
                detail="Facilitator authorization is not configured",
            )
        return
    if not x_apollo_facilitator or not hmac.compare_digest(
        x_apollo_facilitator, expected
    ):
        raise HTTPException(status_code=401, detail="Facilitator authorization required")


def _status_payload(session: PC2Session) -> dict[str, Any]:
    return {
        "status": session.status.value,
        "get_s": session.state.get_s,
        "phase": session.state.phase,
        "pending_gate": session.pending_gate,
        "pause_reason": session.pause_reason,
        "assigned_stations": sorted(session.assigned_stations),
        "available_stations": list(session.available_stations),
        "scenario_id": (
            _active_scenario.scenario_id if _active_scenario is not None else None
        ),
        "mission": (
            _active_scenario.mission if _active_scenario is not None else None
        ),
        "scenario_title": (
            _active_scenario.title if _active_scenario is not None else None
        ),
    }


def _create_runtime(record: ScenarioRecord) -> PC2Session:
    """Instantiate the currently supported runtime adapter for one scenario."""

    if record.runtime_adapter != "pc2_v1":
        raise ValueError(
            f"scenario {record.scenario_id} uses unsupported runtime adapter "
            f"{record.runtime_adapter!r}"
        )
    return PC2Session.create(load_scenario_fixture(record))


def _join_or_rejoin_set(
    session: PC2Session,
    player_id: str,
    stations: list[str] | tuple[str, ...],
) -> None:
    """Join/rejoin an exact set of original station identities."""
    normalized = tuple(station.upper() for station in stations)
    existing = session.player_station_sets.get(player_id)
    if existing is None and player_id in session.station_assignments:
        existing = (session.station_assignments[player_id],)
    if existing is not None:
        if existing != normalized:
            raise ValueError(
                f"Player {player_id} is already assigned to {list(existing)}; "
                f"cannot rejoin as {list(normalized)}"
            )
        session._audit(
            "player_rejoined",
            "SESSION",
            player_id=player_id,
            stations=list(normalized),
        )
        return
    session.assign_stations(player_id, normalized)


def _snapshot_payload(session: PC2Session, player_id: str) -> dict[str, Any]:
    stations = session.stations_for(player_id)
    if len(stations) == 1:
        return session.player_snapshot(player_id).to_dict()
    return session.bundled_player_snapshot(player_id).to_dict()


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/scenarios")
def list_scenarios() -> list[dict[str, object]]:
    records = _domain_call(discover_scenarios)
    return [
        {
            **record.to_public_dict(),
            "default": record.scenario_id == DEFAULT_SCENARIO_ID,
            "executable": record.runtime_adapter in SUPPORTED_RUNTIME_ADAPTERS,
        }
        for record in records
    ]


@app.post("/api/session/create", dependencies=[Depends(_facilitator_guard)])
def create_session(
    scenario_id: str = DEFAULT_SCENARIO_ID,
) -> dict[str, Any]:
    global _session, _clock, _active_scenario
    with _lock:
        record = _domain_call(lambda: get_scenario_record(scenario_id))
        session = _domain_call(lambda: _create_runtime(record))
        _session = session
        _clock = RealtimeSessionClock(session)
        _active_scenario = record
        return _status_payload(session)


@app.get("/api/session/status")
def session_status() -> dict[str, Any]:
    with _lock:
        return _status_payload(_sync_session())


@app.post("/api/session/join")
def join_session(request: JoinRequest) -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        _domain_call(
            lambda: _join_or_rejoin_set(session, request.player_id, (request.station,))
        )
        return _snapshot_payload(session, request.player_id)


@app.post("/api/session/join-set")
def join_session_set(request: JoinSetRequest) -> dict[str, Any]:
    """Join/rejoin multiple original stations without creating a synthetic station."""
    with _lock:
        session = _sync_session()
        _domain_call(
            lambda: _join_or_rejoin_set(session, request.player_id, request.stations)
        )
        return _snapshot_payload(session, request.player_id)


@app.post("/api/session/start", dependencies=[Depends(_facilitator_guard)])
def start_session() -> dict[str, Any]:
    with _lock:
        session = _require_session()
        _domain_call(session.start)
        _require_clock().reanchor()
        return _status_payload(session)


@app.post("/api/session/pause", dependencies=[Depends(_facilitator_guard)])
def pause_session() -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        _domain_call(session.pause)
        _require_clock().reanchor()
        return _status_payload(session)


@app.post("/api/session/resume", dependencies=[Depends(_facilitator_guard)])
def resume_session() -> dict[str, Any]:
    with _lock:
        session = _require_session()
        _domain_call(session.resume)
        _require_clock().reanchor()
        return _status_payload(session)


@app.post("/api/session/advance", dependencies=[Depends(_facilitator_guard)])
def advance_session(request: AdvanceRequest) -> dict[str, Any]:
    """Manual validation control retained alongside realtime pacing."""
    with _lock:
        session = _sync_session()
        reached = _domain_call(lambda: session.advance_to(request.target_get_s))
        _require_clock().reanchor()
        payload = _status_payload(session)
        payload["reached_get_s"] = reached
        return payload


@app.post(
    "/api/session/admin/injection",
    dependencies=[Depends(_facilitator_guard)],
)
def apply_injection(request: StateInjectionRequest) -> dict[str, Any]:
    """Prototype scenario-authoring/validation endpoint, not a player control."""
    with _lock:
        session = _sync_session()
        injection = StateInjection(
            injection_id=request.injection_id,
            get_s=float(session.state.get_s),
            target=request.target,
            value=request.value,
            evidence_class=request.evidence_class,
            provenance=request.provenance,
        )
        _domain_call(lambda: session.apply_session_injection(injection))
        return _status_payload(session)


@app.get("/api/session/player/{player_id}")
def player_snapshot(player_id: str) -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        return _domain_call(lambda: _snapshot_payload(session, player_id))


@app.post("/api/session/player/{player_id}/readiness")
def submit_readiness(player_id: str, request: ReadinessRequest) -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        report = _domain_call(
            lambda: session.submit_readiness(
                player_id,
                ready=request.ready,
                note=request.note,
                station=request.station,
            )
        )
        return {
            "get_s": report.get_s,
            "station": report.station,
            "ready": report.ready,
            "note": report.note,
        }


@app.post("/api/session/flight/{player_id}/decision")
def flight_decision(player_id: str, request: FlightDecisionRequest) -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        _domain_call(lambda: session.record_flight_go(player_id, go=request.go, basis=request.basis))
        return _snapshot_payload(session, player_id)


@app.post("/api/session/flight/{player_id}/capcom")
def queue_capcom(player_id: str, request: CapcomQueueRequest) -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        item = _domain_call(
            lambda: session.queue_capcom_instruction(
                player_id,
                action=request.action,
                parameters=request.parameters,
                basis=request.basis,
            )
        )
        return {
            "item_id": item.item_id,
            "get_s": item.get_s,
            "requested_by": item.requested_by,
            "action": item.action,
            "parameters": item.parameters,
            "basis": item.basis,
            "transmitted": item.transmitted,
        }


@app.post("/api/session/control/{player_id}/delta-p-callout")
def control_delta_p_callout(player_id: str, request: ControlDeltaPCalloutRequest) -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        item = _domain_call(
            lambda: session.record_control_delta_p_callout(player_id, basis=request.basis)
        )
        return {
            "item_id": item.item_id,
            "get_s": item.get_s,
            "requested_by": item.requested_by,
            "action": item.action,
            "parameters": item.parameters,
            "basis": item.basis,
            "transmitted": item.transmitted,
        }


@app.get("/api/session/control/{player_id}/shutdown-evidence")
def control_shutdown_evidence(player_id: str) -> dict[str, Any]:
    """Return controller-observable evidence availability, never hidden truth."""
    with _lock:
        session = _sync_session()
        if not _domain_call(lambda: session.owns_station(player_id, "CONTROL")):
            raise HTTPException(status_code=400, detail="Only a CONTROL owner can request shutdown evidence")
        return _domain_call(lambda: assess_session_shutdown_evidence(session))


@app.post("/api/session/capcom/{player_id}/transmit/{item_id}")
def transmit_capcom(player_id: str, item_id: int) -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        item = _domain_call(lambda: session.transmit_capcom_item(player_id, item_id))
        return {
            "item_id": item.item_id,
            "requested_by": item.requested_by,
            "action": item.action,
            "transmitted": item.transmitted,
            "transmitted_get_s": item.transmitted_get_s,
        }


@app.post(
    "/api/session/crew/receipt/{item_id}",
    dependencies=[Depends(_facilitator_guard)],
)
def crew_receipt(item_id: int, request: CrewReceiptRequest) -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        return _domain_call(
            lambda: record_crew_receipt(
                session,
                item_id,
                crew_id=request.crew_id,
                response=request.response,
            )
        )


@app.post(
    "/api/session/crew/shutdown/{item_id}",
    dependencies=[Depends(_facilitator_guard)],
)
def crew_shutdown(item_id: int, request: CrewShutdownRequest) -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        action = _domain_call(
            lambda: command_dps_shutdown_from_callout(
                session,
                item_id,
                crew_id=request.crew_id,
                provenance=request.provenance,
            )
        )
        return {
            "action_id": action.action_id,
            "get_s": action.get_s,
            "actor": action.actor,
            "action": action.action,
            "parameters": action.parameters,
            "provenance": action.provenance,
        }


@app.post(
    "/api/session/crew/shutdown-report",
    dependencies=[Depends(_facilitator_guard)],
)
def crew_shutdown_report(request: CrewShutdownReportRequest) -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        return _domain_call(lambda: record_crew_shutdown_report(session, crew_id=request.crew_id))


@app.post(
    "/api/session/admin/vehicle/dps-engine-off",
    dependencies=[Depends(_facilitator_guard)],
)
def dps_engine_off_response(request: EngineOffResponseRequest) -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        return _domain_call(
            lambda: apply_session_engine_off_response(
                session,
                get_s=float(session.state.get_s),
                cause=request.cause,
            )
        )


@app.post(
    "/api/admin/model-proof/dps-burn",
    dependencies=[Depends(_facilitator_guard)],
)
def dps_burn_model_proof(request: DPSModelProofRequest) -> dict[str, object]:
    """Run the mission-neutral Level-1 burn model from explicit caller inputs."""

    result = _domain_call(
        lambda: simulate_dps_maneuver(
            ManeuverState(
                time_s=request.initial_time_s,
                mass_kg=request.initial_mass_kg,
                velocity_m_s=tuple(request.initial_velocity_m_s),
            ),
            [
                BurnSegment(
                    duration_s=segment.duration_s,
                    thrust_n=segment.thrust_n,
                    direction=tuple(segment.direction),
                    end_thrust_n=segment.end_thrust_n,
                    specific_impulse_s=segment.specific_impulse_s,
                    regime=segment.regime,
                )
                for segment in request.segments
            ],
            DPSModelConfig(
                specific_impulse_s=request.specific_impulse_s,
                dry_mass_kg=request.dry_mass_kg,
                max_step_s=request.max_step_s,
                applicability=request.applicability,
                provenance=tuple(request.provenance),
            ),
        )
    )
    return result.to_dict()


@app.get("/api/session/audit", dependencies=[Depends(_facilitator_guard)])
def audit_log() -> list[dict[str, Any]]:
    with _lock:
        session = _sync_session()
        return [
            {
                "sequence": event.sequence,
                "get_s": event.get_s,
                "kind": event.kind,
                "actor": event.actor,
                "details": event.details,
            }
            for event in session.audit_log
        ]


@app.get("/", include_in_schema=False)
def index() -> FileResponse:
    return FileResponse(WEB_ROOT / "index.html")


@app.get("/admin", include_in_schema=False)
def admin_console() -> FileResponse:
    """Facilitator/SimSup validation console; API operations require authority."""
    return FileResponse(WEB_ROOT / "admin.html")
