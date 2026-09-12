"""Thin FastAPI transport for the Apollo Mission Control PC+2 prototype.

The simulation/domain layer remains framework-neutral. This module owns only
HTTP request/response adaptation, an in-memory single-session registry, and
static prototype delivery.
"""

from __future__ import annotations

from pathlib import Path
from threading import RLock
from typing import Any, Callable

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from .pc2_nominal import load_fixture
from .pc2_session import PC2Session
from .scenario_injection import EvidenceClass, StateInjection


ROOT = Path(__file__).resolve().parents[2]
FIXTURE_PATH = ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json"
WEB_ROOT = ROOT / "web"

app = FastAPI(
    title="Apollo Mission Control",
    description="First playable Apollo 13 PC+2 Mission Control session API",
    version="0.1.0",
)

_lock = RLock()
_session: PC2Session | None = None


class JoinRequest(BaseModel):
    player_id: str = Field(min_length=1, max_length=64)
    station: str = Field(min_length=1, max_length=32)


class AdvanceRequest(BaseModel):
    target_get_s: float


class ReadinessRequest(BaseModel):
    ready: bool
    note: str = Field(default="", max_length=500)


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


def _require_session() -> PC2Session:
    if _session is None:
        raise HTTPException(status_code=409, detail="No PC+2 session has been created")
    return _session


def _domain_call(call: Callable[[], Any]) -> Any:
    try:
        return call()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


def _status_payload(session: PC2Session) -> dict[str, Any]:
    return {
        "status": session.status.value,
        "get_s": session.state.get_s,
        "phase": session.state.phase,
        "pending_gate": session.pending_gate,
        "pause_reason": session.pause_reason,
        "assigned_stations": sorted(session.station_assignments.values()),
        "available_stations": list(session.available_stations),
    }


def _join_or_rejoin(session: PC2Session, player_id: str, station: str) -> None:
    """Join a station or idempotently rejoin the player's existing assignment.

    This is deliberately lightweight prototype identity, not authentication.
    A repeated browser join with the same player ID and same station is allowed;
    the same ID cannot switch stations, and another ID cannot take an occupied
    station through this path.
    """
    normalized = station.upper()
    existing = session.station_assignments.get(player_id)
    if existing is not None:
        if existing != normalized:
            raise ValueError(
                f"Player {player_id} is already assigned to {existing}; cannot rejoin as {normalized}"
            )
        session._audit("player_rejoined", "SESSION", player_id=player_id, station=normalized)
        return
    session.assign_station(player_id, normalized)


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/session/create")
def create_session() -> dict[str, Any]:
    global _session
    with _lock:
        fixture = load_fixture(FIXTURE_PATH)
        _session = PC2Session.create(fixture)
        return _status_payload(_session)


@app.get("/api/session/status")
def session_status() -> dict[str, Any]:
    with _lock:
        return _status_payload(_require_session())


@app.post("/api/session/join")
def join_session(request: JoinRequest) -> dict[str, Any]:
    with _lock:
        session = _require_session()
        _domain_call(lambda: _join_or_rejoin(session, request.player_id, request.station))
        return session.player_snapshot(request.player_id).to_dict()


@app.post("/api/session/start")
def start_session() -> dict[str, Any]:
    with _lock:
        session = _require_session()
        _domain_call(session.start)
        return _status_payload(session)


@app.post("/api/session/pause")
def pause_session() -> dict[str, Any]:
    with _lock:
        session = _require_session()
        _domain_call(session.pause)
        return _status_payload(session)


@app.post("/api/session/resume")
def resume_session() -> dict[str, Any]:
    with _lock:
        session = _require_session()
        _domain_call(session.resume)
        return _status_payload(session)


@app.post("/api/session/advance")
def advance_session(request: AdvanceRequest) -> dict[str, Any]:
    with _lock:
        session = _require_session()
        reached = _domain_call(lambda: session.advance_to(request.target_get_s))
        payload = _status_payload(session)
        payload["reached_get_s"] = reached
        return payload


@app.post("/api/session/admin/injection")
def apply_injection(request: StateInjectionRequest) -> dict[str, Any]:
    """Prototype scenario-authoring/validation endpoint, not a player control."""
    with _lock:
        session = _require_session()
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
        session = _require_session()
        return _domain_call(lambda: session.player_snapshot(player_id).to_dict())


@app.post("/api/session/player/{player_id}/readiness")
def submit_readiness(player_id: str, request: ReadinessRequest) -> dict[str, Any]:
    with _lock:
        session = _require_session()
        report = _domain_call(
            lambda: session.submit_readiness(player_id, ready=request.ready, note=request.note)
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
        session = _require_session()
        _domain_call(lambda: session.record_flight_go(player_id, go=request.go, basis=request.basis))
        return session.player_snapshot(player_id).to_dict()


@app.post("/api/session/flight/{player_id}/capcom")
def queue_capcom(player_id: str, request: CapcomQueueRequest) -> dict[str, Any]:
    with _lock:
        session = _require_session()
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
def control_delta_p_callout(
    player_id: str, request: ControlDeltaPCalloutRequest
) -> dict[str, Any]:
    with _lock:
        session = _require_session()
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


@app.post("/api/session/capcom/{player_id}/transmit/{item_id}")
def transmit_capcom(player_id: str, item_id: int) -> dict[str, Any]:
    with _lock:
        session = _require_session()
        item = _domain_call(lambda: session.transmit_capcom_item(player_id, item_id))
        return {
            "item_id": item.item_id,
            "requested_by": item.requested_by,
            "action": item.action,
            "transmitted": item.transmitted,
            "transmitted_get_s": item.transmitted_get_s,
        }


@app.get("/api/session/audit")
def audit_log() -> list[dict[str, Any]]:
    """Prototype validation endpoint; not intended as a normal player view."""
    with _lock:
        session = _require_session()
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
