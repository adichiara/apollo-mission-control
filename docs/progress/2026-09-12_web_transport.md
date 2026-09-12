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
- Exposed JSON operations for session creation/status, station join, session lifecycle, GET advancement, station-scoped snapshots, readiness, FLIGHT decision, CAPCOM queue/transmission, and prototype audit access.
- Preserved domain errors/rules inside `PC2Session`; the HTTP layer is an adapter rather than a second simulation engine.

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

## Next work

1. Make station join idempotent for the same player/station so a browser reload can rejoin without losing or stealing the assignment.
2. Persist player ID/station locally in the browser prototype and attempt rejoin on reload.
3. Resolve mission-clock semantics before adding a real-time driver: historical GET should not silently freeze merely because a controller decision is pending unless the game explicitly pauses.
4. Smoke-test the HTTP/mobile path when a runnable environment becomes available.
5. Then exercise one already-modeled nonnominal branch through the web/session layer.
