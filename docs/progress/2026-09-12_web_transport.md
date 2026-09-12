# Progress — first playable web transport

Date: 2026-09-12

## Completed transport foundation

- Selected **FastAPI + Uvicorn** as the first playable transport shell while keeping the simulation/session domain framework-neutral.
- Added `src/apollo_mission_control/web_app.py` and a phone-first dependency-free client at `web/index.html`.
- Added `requirements.txt`, `.python-version`, `render.yaml`, and API tests.
- Recorded transport decision **D-014**.
- Exposed JSON operations for session creation/status, station join, lifecycle, station-scoped snapshots, readiness, FLIGHT decision, CAPCOM queue/transmission, scenario validation operations, crew/vehicle response operations, controller evidence assessment, and prototype audit access.
- Added idempotent same-player/same-station rejoin while preserving station-assignment protection.
- Browser client persists prototype player/station identity and attempts automatic rejoin after reload.

## Continuous mission clock — implemented

Accepted decision **D-016** establishes:

- GET runs continuously while the session is `RUNNING`;
- controller decisions and missing authorization do not stop mission time;
- only explicit game/session pause stops GET;
- nominal timeline entries are event opportunities with prerequisites rather than unconditional scene transitions;
- a nominal event whose prerequisites are absent at its GET is recorded as missed and is not replayed retroactively.

Implementation includes reusable event eligibility, PC+2 event rules, continuous session behavior, and a 1× monotonic realtime clock adapter. Manual `/advance` remains only for validation/development.

## First nonnominal web/session path — complete through controller evidence

The source-bounded synthetic ΔP path now runs through the HTTP/session validation interface as:

1. explicit source-state injection;
2. normal CONTROL projection/presentation;
3. common shutdown-rule evaluation;
4. explicit CONTROL callout decision;
5. CAPCOM queue;
6. explicit CAPCOM transmission;
7. explicit crew receipt;
8. explicit crew DPS shutdown command;
9. explicit physical DPS engine-off response;
10. explicit crew shutdown report, if supplied;
11. fresh post-command CONTROL chamber-pressure observation, if supplied;
12. CONTROL evidence aggregation.

Transport operations added during this integration:

- `POST /api/session/crew/receipt/{item_id}`;
- `POST /api/session/crew/shutdown/{item_id}`;
- `POST /api/session/admin/vehicle/dps-engine-off`;
- `POST /api/session/crew/shutdown-report`;
- `GET /api/session/control/{player_id}/shutdown-evidence`.

The evidence endpoint is restricted to the assigned CONTROL player and returns evidence availability only: `none`, `crew_reported`, `ground_pressure_observed`, or `corroborated`.

Freshness is explicit: a pre-command chamber-pressure observation cannot count as shutdown-response evidence. A fresh pressure observation is not interpreted by magnitude; a synthetic 100 psi test intentionally demonstrates that the software records observation availability without claiming engine-off confirmation.

The evidence integration never consults authoritative `engine_running` state.

See research notes 085 and 086.

## Deployment boundary

The current server still holds one authoritative session in process memory. One worker is required; restart/redeploy/spin-down loses a live game; durable persistence and multiple concurrent sessions remain deferred.

Realtime pacing is currently fixed at **1×**. Time acceleration remains undecided and is not exposed as a player control.

## Test status

New HTTP tests are committed:

- `tests/test_web_crew_response.py`;
- `tests/test_web_shutdown_evidence.py`.

The full repository suite is still **not recorded as passing** because this automation environment does not provide a checked-out runnable repository execution path.

## Current stopping point

The first source-bounded nonnominal branch is now integrated end to end through fresh controller evidence.

Next work is operational validation and player-surface cleanup:

1. execute the complete domain/session/API suite in a runnable environment;
2. exercise several phone/browser clients against one server;
3. validate realtime polling/actions, pause/resume, rejoin, and station isolation;
4. run the complete synthetic ΔP branch through the live browser/API path;
5. review the phone UI now that GET advances automatically;
6. separate validation/admin controls from normal player-facing controls before broader playtesting;
7. reopen historical research only if integrated play exposes a concrete information or decision gap.
