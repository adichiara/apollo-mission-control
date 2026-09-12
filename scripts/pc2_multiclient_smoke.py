#!/usr/bin/env python3
"""Network smoke test for the first playable Apollo 13 PC+2 session.

This script intentionally resets the target session. Run it only against a local
or dedicated validation deployment, not an active player session.

Examples:
    python scripts/pc2_multiclient_smoke.py http://127.0.0.1:8000
    APOLLO_FACILITATOR_TOKEN=... python scripts/pc2_multiclient_smoke.py https://example.onrender.com
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import os
import time
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import Request, urlopen


def request_json(
    base_url: str,
    method: str,
    path: str,
    *,
    body: dict | None = None,
    headers: dict[str, str] | None = None,
    expected: int = 200,
):
    data = None if body is None else json.dumps(body).encode("utf-8")
    merged = {"Content-Type": "application/json", **(headers or {})}
    request = Request(
        base_url.rstrip("/") + path,
        data=data,
        headers=merged,
        method=method,
    )
    try:
        with urlopen(request, timeout=15) as response:
            status = response.status
            raw = response.read().decode("utf-8")
    except HTTPError as exc:
        status = exc.code
        raw = exc.read().decode("utf-8")
    payload = json.loads(raw) if raw else None
    if status != expected:
        raise RuntimeError(
            f"{method} {path}: expected HTTP {expected}, got {status}: {payload}"
        )
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run destructive multi-client validation against a PC+2 server."
    )
    parser.add_argument("base_url", help="Server base URL, e.g. http://127.0.0.1:8000")
    parser.add_argument(
        "--facilitator-token",
        default=os.getenv("APOLLO_FACILITATOR_TOKEN", ""),
        help="Facilitator token; defaults to APOLLO_FACILITATOR_TOKEN",
    )
    args = parser.parse_args()

    token_headers = (
        {"X-Apollo-Facilitator": args.facilitator_token}
        if args.facilitator_token
        else {}
    )

    def get(path: str, *, headers=None, expected=200):
        return request_json(
            args.base_url,
            "GET",
            path,
            headers=headers,
            expected=expected,
        )

    def post(path: str, body: dict | None = None, *, headers=None, expected=200):
        return request_json(
            args.base_url,
            "POST",
            path,
            body=body,
            headers=headers,
            expected=expected,
        )

    # Destructive by design: establish one clean authoritative session.
    post("/api/session/create", headers=token_headers)
    stations = {
        "flight": "FLIGHT",
        "control": "CONTROL",
        "capcom": "CAPCOM",
        "guido": "GUIDO",
    }
    for player_id, station in stations.items():
        joined = post(
            "/api/session/join",
            {"player_id": player_id, "station": station},
        )
        if joined["station"] != station:
            raise RuntimeError(f"Station mismatch for {player_id}: {joined}")

    post("/api/session/start", headers=token_headers)

    # Exercise simultaneous polling from independent station identities.
    def poll_player(player_id: str):
        return get(f"/api/session/player/{quote(player_id)}")

    with ThreadPoolExecutor(max_workers=len(stations)) as executor:
        snapshots = list(executor.map(poll_player, stations))

    gets = [float(snapshot["get_s"]) for snapshot in snapshots]
    if max(gets) - min(gets) > 1.0:
        raise RuntimeError(f"Station GETs diverged unexpectedly: {gets}")
    if any(snapshot["session_status"] != "running" for snapshot in snapshots):
        raise RuntimeError("Not all station snapshots observe the running session")

    # Reload/rejoin contract.
    rejoin = post(
        "/api/session/join",
        {"player_id": "control", "station": "CONTROL"},
    )
    if rejoin["station"] != "CONTROL":
        raise RuntimeError("CONTROL rejoin did not preserve station identity")

    # Authority isolation is testable only when the target actually has a token.
    if args.facilitator_token:
        post("/api/session/pause", expected=401)

    # Explicit pause must stop GET while controller clients can still inspect state.
    paused = post("/api/session/pause", headers=token_headers)
    paused_get = float(paused["get_s"])
    time.sleep(0.5)
    paused_status = get("/api/session/status")
    if float(paused_status["get_s"]) != paused_get:
        raise RuntimeError(
            f"GET advanced while paused: {paused_get} -> {paused_status['get_s']}"
        )
    post("/api/session/resume", headers=token_headers)

    # Move deterministically into the existing source-bounded synthetic branch.
    post(
        "/api/session/advance",
        {"target_get_s": 79 * 3600 + 17 * 60},
        headers=token_headers,
    )
    post(
        "/api/session/flight/flight/decision",
        {"go": True, "basis": "network multi-client validation"},
    )
    post(
        "/api/session/advance",
        {"target_get_s": 79 * 3600 + 29 * 60},
        headers=token_headers,
    )
    post(
        "/api/session/admin/injection",
        {
            "injection_id": "network-delta-p-26",
            "target": "dps_fuel_oxidizer_delta_p_psi",
            "value": 26.0,
            "evidence_class": "source_bounded_test",
            "provenance": (
                "synthetic network smoke test; 26 psi is not an Apollo 13 measurement"
            ),
        },
        headers=token_headers,
    )
    callout = post(
        "/api/session/control/control/delta-p-callout",
        {"basis": "synthetic >25 psi ground-callout exercise"},
    )
    item_id = int(callout["item_id"])

    capcom_view = get("/api/session/player/capcom")
    if not any(
        item["item_id"] == item_id
        for item in capcom_view["presentation"].get("queue_items", [])
    ):
        raise RuntimeError("CAPCOM did not receive CONTROL's queued callout")

    post(f"/api/session/capcom/capcom/transmit/{item_id}")
    post(f"/api/session/crew/receipt/{item_id}", {}, headers=token_headers)
    post(f"/api/session/crew/shutdown/{item_id}", {}, headers=token_headers)
    post(
        "/api/session/admin/vehicle/dps-engine-off",
        {"cause": "crew_stop_pushbutton"},
        headers=token_headers,
    )
    post("/api/session/crew/shutdown-report", {}, headers=token_headers)
    post(
        "/api/session/admin/injection",
        {
            "injection_id": "network-post-command-pressure",
            "target": "dps_chamber_pressure_psi",
            "value": 100.0,
            "evidence_class": "source_bounded_test",
            "provenance": (
                "synthetic fresh observation; high value deliberately proves no "
                "engine-off pressure threshold is implied"
            ),
        },
        headers=token_headers,
    )

    evidence = get("/api/session/control/control/shutdown-evidence")
    if evidence.get("state") != "corroborated":
        raise RuntimeError(f"Expected corroborated CONTROL evidence: {evidence}")
    if "engine_off_confirmed" in evidence:
        raise RuntimeError("Controller evidence leaked an engine-off verdict")

    audit = get("/api/session/audit", headers=token_headers)
    kinds = [event["kind"] for event in audit]
    ordered = [
        "state_injection_applied",
        "controller_shutdown_callout_decision",
        "capcom_item_transmitted",
        "crew_capcom_item_received",
        "crew_dps_shutdown_commanded",
        "dps_engine_off_physical_response",
        "crew_dps_shutdown_reported",
    ]
    positions = [kinds.index(kind) for kind in ordered]
    if positions != sorted(positions):
        raise RuntimeError(f"Unexpected audit ordering: {positions}")

    print(
        json.dumps(
            {
                "result": "PASS",
                "stations": stations,
                "initial_get_spread_s": max(gets) - min(gets),
                "rejoin": "CONTROL preserved",
                "pause_get_s": paused_get,
                "delta_p_item_id": item_id,
                "shutdown_evidence": evidence,
                "audit_events": len(audit),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
