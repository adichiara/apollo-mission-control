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

### PC+2 behavior

At the historical final-poll point, `flight_go` becomes pending but the session remains RUNNING.

If GO arrives before the required nominal P40 milestone, the nominal sequence may continue. If GO is late, missed milestones are not replayed. P40, ullage, ignition, throttle, cutoff, residual, and power-down nominal events now depend on declared authoritative-state prerequisites.

This changes the engine from a sequence of gated scenes into a continuously evolving mission in which player timing can itself create consequences.

## First nonnominal web/session path

The source-bounded synthetic ΔP path remains implemented through:

1. explicit source-state injection;
2. normal CONTROL projection/presentation;
3. common shutdown-rule evaluation;
4. explicit CONTROL callout decision;
5. CAPCOM queue;
6. explicit CAPCOM transmission.

Crew receipt/command/physical-response continuation is already modeled at the domain layer and remains the next HTTP exposure target.

## Deployment boundary

The current server still holds one authoritative session in process memory. One worker is required; restart/redeploy/spin-down loses a live game; durable persistence and multiple concurrent sessions remain deferred.

Realtime pacing is currently fixed at **1×**. Time acceleration remains undecided and is not exposed as a player control.

## Test status

The new domain/API tests are committed. A fresh execution attempt on 2026-09-12 again failed before checkout because the runtime could not resolve `github.com`; therefore the full suite is **not recorded as passing**.

## Current stopping point

The engine now has the intended continuous-time foundation.

Next integration work:

1. expose explicit crew receipt, crew DPS shutdown command, and supplied-time physical DPS response through the HTTP validation interface;
2. reconnect physical shutdown to fresh controller evidence without inventing a pressure threshold or response latency;
3. smoke-test multi-client realtime behavior when a runnable environment is available;
4. review the phone UI now that GET advances automatically rather than through manual advancement;
5. keep manual `/advance` only as a development/validation control, not normal gameplay.
