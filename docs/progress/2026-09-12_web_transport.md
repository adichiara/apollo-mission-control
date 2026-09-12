# Progress — first playable web transport

Date: 2026-09-12

## Completed transport foundation

- Selected **FastAPI + Uvicorn** as the first playable transport shell while keeping the simulation/session domain framework-neutral.
- Added `src/apollo_mission_control/web_app.py` and a phone-first dependency-free client at `web/index.html`.
- Added `requirements.txt`, `.python-version`, `render.yaml`, and API tests.
- Recorded transport decision **D-014**.
- Exposed JSON operations for session creation/status, station join, lifecycle, station-scoped snapshots, readiness, FLIGHT decision, CAPCOM queue/transmission, scenario validation operations, and prototype audit access.
- Added idempotent same-player/same-station rejoin while preserving station-assignment protection.
- Browser client persists prototype player/station identity and attempts automatic rejoin after reload.

## Continuous mission clock — implemented

The former provisional decision-gate pause policy has been superseded.

Accepted decision **D-016** establishes:

- GET runs continuously while the session is `RUNNING`;
- controller decisions and missing authorization do not stop mission time;
- only explicit game/session pause stops GET;
- nominal timeline entries are event opportunities with prerequisites rather than unconditional scene transitions;
- a nominal event whose prerequisites are absent at its GET is recorded as missed and is not replayed retroactively.

Implementation changes:

- `src/apollo_mission_control/event_eligibility.py` — reusable declarative state-requirement evaluator;
- `src/apollo_mission_control/pc2_event_rules.py` — PC+2 nominal event prerequisites;
- `src/apollo_mission_control/pc2_session.py` — continuous GET plus `scenario_event_missed` audit behavior;
- `src/apollo_mission_control/realtime_clock.py` — 1× monotonic wall-clock pacing adapter;
- `src/apollo_mission_control/web_app.py` — synchronizes the authoritative session to wall-clock time on API interactions;
- `tests/test_event_eligibility.py`;
- `tests/test_realtime_clock.py`;
- updated session/API clock tests.

Research/decision record:

- `resources/research/081_pc2_mission_clock_and_decision_gate_semantics.md` retains the primary-source findings and marks the pause policy superseded;
- `resources/research/084_continuous_mission_clock_architecture.md` documents the current engine architecture.

## First nonnominal web/session path — now reaches physical response

The source-bounded synthetic ΔP path now runs through the HTTP/session validation interface as:

1. explicit source-state injection;
2. normal CONTROL projection/presentation;
3. common shutdown-rule evaluation;
4. explicit CONTROL callout decision;
5. CAPCOM queue;
6. explicit CAPCOM transmission;
7. explicit crew receipt;
8. explicit crew DPS shutdown command;
9. explicit physical DPS engine-off response.

New transport operations:

- `POST /api/session/crew/receipt/{item_id}`;
- `POST /api/session/crew/shutdown/{item_id}`;
- `POST /api/session/admin/vehicle/dps-engine-off`.

The transport calls the existing `crew_response.py` domain operations and does not collapse any layer. The physical response uses synchronized current authoritative GET; no fixed delay is inferred. The receipt endpoint's default `received` value is semantic test metadata, not claimed Apollo wording.

Primary-source boundary was rechecked against the Apollo 13 mission-operations record and NASA air-ground transcript. Those sources support a ground-call shutdown relationship but do not provide a hypothetical exceedance response latency, exact response wording, unique crewmember assignment, or engine-off delay.

See `resources/research/085_pc2_http_crew_response_integration.md` and `resources/source-catalog/PC2_CREW_RESPONSE_SOURCES.md`.

## Deployment boundary

The current server still holds one authoritative session in process memory. One worker is required; restart/redeploy/spin-down loses a live game; durable persistence and multiple concurrent sessions remain deferred.

Realtime pacing is currently fixed at **1×**. Time acceleration remains undecided and is not exposed as a player control.

## Test status

`tests/test_web_crew_response.py` is committed and validates the HTTP ordering/guardrails. The full repository suite is still **not recorded as passing** because this automation environment has not provided a runnable checked-out repository execution path.

## Current stopping point

The next integration boundary is **fresh controller-observable shutdown evidence**:

1. expose an explicit crew shutdown report as an independent evidence channel;
2. use a fresh post-command `GQ6510P` chamber-pressure observation through the existing controller product path;
3. expose/assess the existing `shutdown_confirmation.py` evidence aggregation without creating an `engine_off_confirmed` truth flag or pressure threshold;
4. smoke-test multi-client realtime behavior when a runnable environment is available;
5. review the phone UI now that GET advances automatically rather than through manual advancement;
6. keep manual `/advance` only as a development/validation control, not normal gameplay.
