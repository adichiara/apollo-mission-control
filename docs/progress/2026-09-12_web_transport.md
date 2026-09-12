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

Manual GET advancement is temporary development infrastructure, not a final mission-time design.

## Deployment boundary

The current server holds **one authoritative session in process memory**.

Consequences:

- one process/worker only;
- restart/redeploy/spin-down loses a live game;
- no durable persistence yet;
- no multiple concurrent sessions yet.

This is accepted for the first workflow/playability milestone only.

## Test status

Transport/domain tests are committed. A full-suite execution is still not recorded as passing because the available runtime has repeatedly failed DNS resolution for `github.com` before a fresh clone/test run can begin.

## Current stopping point

The highest-value unresolved integration issue is now **mission-clock semantics at decision gates**.

The current playable session freezes authoritative GET when the historical final GO/NO-GO poll opens and resumes only after FLIGHT records GO. That is convenient for a prototype but is not historical behavior: mission GET itself continued.

Before implementing a real-time server driver, explicitly define the relationship among:

- historical/session GET;
- scenario-event eligibility;
- pending controller decisions;
- explicit simulation pause;
- any future time acceleration.

Do not silently turn every decision gate into a historical clock stop, and do not apply later timed events retroactively without defined semantics.

## Next work

1. Define and implement the mission-clock / event-gate model.
2. Add browser-side local persistence or another lightweight mechanism so the client can automatically reattempt its same-player/same-station rejoin after reload.
3. Smoke-test the HTTP/mobile path when a runnable environment becomes available.
4. Then exercise one already-modeled nonnominal branch through the web/session layer.
