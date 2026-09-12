# Progress — first playable web transport

Date: 2026-09-12

## Completed

- Selected **FastAPI + Uvicorn** as the first playable transport shell while keeping the simulation/session domain framework-neutral.
- Added `src/apollo_mission_control/web_app.py`.
- Added a phone-first dependency-free client at `web/index.html`.
- Added `requirements.txt`, `.python-version`, and `render.yaml`.
- Added `tests/test_web_app.py`.
- Added `resources/research/080_web_transport_selection.md`.
- Added `resources/source-catalog/WEB_TRANSPORT_SOURCES.md`.
- Recorded transport decision **D-014** in `docs/DECISIONS.md`.
- Exposed JSON operations for session creation/status, station join, session lifecycle, GET advancement, station-scoped snapshots, readiness, FLIGHT decision, CAPCOM queue/transmission, and prototype audit access.
- Preserved domain errors/rules inside `PC2Session`; the HTTP layer remains an adapter rather than a second simulation engine.
- Added idempotent **same-player / same-station rejoin** at the transport boundary.
- Preserved assignment protection: a rejoining player cannot switch stations and another player cannot take an occupied station.
- Added API tests for the rejoin behavior.

## Mission-clock boundary resolved

Primary-source review was completed before changing timing behavior.

The Apollo 13 Flight Control Division *Mission Operations Report* establishes the source-backed PC+2 sequence and explicitly states that PC+2 ignition time was **not time critical**, while still recording the actual GO/TIG/power-down chronology in GET. The source does not say GET stopped while controllers deliberated and does not give a numeric allowable delay.

Implementation policy for the deterministic first slice is therefore explicit:

- blocking controller gates pause the **simulation**, not historical Apollo GET;
- the final FLIGHT gate now sets session status `PAUSED` with `pause_reason=decision_gate:flight_go`;
- manual resume cannot bypass a pending gate;
- FLIGHT GO clears the gate and automatically resumes;
- NO-GO remains paused;
- later source-timed events are not silently applied retroactively;
- the API/player snapshot exposes the pause reason.

Added:

- `resources/research/081_pc2_mission_clock_and_decision_gate_semantics.md`;
- updated `PC2_SESSION_INTEGRATION_SOURCES.md`;
- updated `pc2_session.py`, `web_app.py`, and their tests.

No delay tolerance or retargeting rule was invented from the phrase “not time critical.”

## Phone-client checkpoint

The prototype client can:

- create/reset a session;
- join one of the seven first-slice stations;
- display station-scoped presentation data;
- poll session/player state;
- report readiness;
- perform FLIGHT GO/NO-GO when assigned FLIGHT;
- queue crew-facing items from FLIGHT;
- transmit approved items as CAPCOM;
- manually advance GET for integration testing.

Manual GET advancement remains temporary development infrastructure. A realtime driver can now be designed against explicit pause semantics rather than an ambiguous frozen clock.

## Deployment boundary

The current server holds **one authoritative session in process memory**.

Consequences:

- one process/worker only;
- restart/redeploy/spin-down loses a live game;
- no durable persistence yet;
- no multiple concurrent sessions yet.

This is accepted for the first workflow/playability milestone only.

## Test status

The new timing/domain/API tests are committed. A full-suite execution is still not recorded as passing because the available execution runtime has not provided a usable checked-out repository environment for running the suite.

## Current stopping point

The mission-clock / decision-gate ambiguity is resolved for the first deterministic slice.

The highest-value next work is now:

1. browser-side persistence of player ID/station and automatic same-player/same-station rejoin after reload;
2. runnable HTTP/mobile smoke validation;
3. then route one already-modeled nonnominal branch through the web/session layer;
4. introduce a realtime driver only after the smoke path is stable, using the explicit pause policy rather than inventing delayed-event semantics.
