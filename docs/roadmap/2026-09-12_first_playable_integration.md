# Roadmap addendum — first playable PC+2 integration

Date: 2026-09-12  
Status: **CURRENT — continuous-time HTTP chain now reaches physical DPS response; fresh controller evidence is next**

## Completed presentation/session/web checkpoints

- [x] minimum player presentations for CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, FLIGHT, CAPCOM;
- [x] one authoritative mission state and synchronized GET;
- [x] deterministic scenario advancement, lifecycle, and audit log;
- [x] unique station assignment and station-scoped snapshots;
- [x] readiness reports surfaced to FLIGHT;
- [x] explicit FLIGHT GO/NO-GO decision requirement;
- [x] explicit FLIGHT/CAPCOM queue and transmission path;
- [x] scripted nominal seven-station playthrough;
- [x] FastAPI/Uvicorn JSON transport and phone client;
- [x] Render configuration and health endpoint;
- [x] idempotent same-player/same-station server rejoin;
- [x] browser `localStorage` persistence of prototype player/station identity and automatic rejoin after reload;
- [x] continuous mission clock adopted: controller decisions do not stop GET;
- [x] explicit game/session pause retained as the only ordinary clock-stop mechanism;
- [x] nominal downstream events can be missed when prerequisites are absent and are not replayed retroactively;
- [x] reusable declarative event-eligibility layer replaces PC+2 session-specific prerequisite branching;
- [x] 1× monotonic wall-clock pacing integrated with the web session;
- [x] HTTP validation path now exposes crew receipt, crew shutdown command, and physical DPS engine-off response.

The current deployment architecture remains single-process/in-memory. Restart or redeploy loses the live session; multiple workers/sessions remain deferred.

See D-016, `resources/research/084_continuous_mission_clock_architecture.md`, and `resources/research/085_pc2_http_crew_response_integration.md`.

## Continuous-time engine boundary — implemented

The session no longer treats the final FLIGHT poll as a scene boundary that freezes simulation time.

At the approximately 79:17 GET poll:

- `flight_go` becomes a pending decision requirement;
- session status remains `RUNNING`;
- GET continues;
- FLIGHT may record GO or NO-GO at the actual current GET;
- downstream nominal events execute only if their operational prerequisites are present when their scheduled time arrives;
- ineligible nominal events are recorded as `scenario_event_missed` with a reason;
- missed nominal events are not replayed automatically after a late GO.

Prerequisites are now declared through the reusable event-eligibility layer rather than embedded as PC+2-specific session branches.

The web layer uses a monotonic realtime driver fixed at 1× and synchronizes the authoritative session on API interaction. Manual `/advance` remains only as development/validation infrastructure.

## First nonnominal session/API path — implemented through physical response

Primary Apollo 13 sources establish the PC+2 **fuel/oxidizer ΔP >25 psi** criterion as a **ground callout**, but do not establish the exact internal CONTROL→FLIGHT→CAPCOM routing, exact hypothetical response wording, or response latency.

Implemented without filling those gaps:

- [x] explicit source-state injection through the existing whitelisted scenario-injection model;
- [x] CONTROL receives the ground-derived ΔP through the normal product/presentation path;
- [x] the existing common shutdown-rule evaluator determines whether the criterion is triggered;
- [x] CONTROL must explicitly issue the shutdown callout decision;
- [x] the callout enters the CAPCOM queue as `requested_by=CONTROL`;
- [x] queue metadata explicitly states that internal Apollo routing is unresolved;
- [x] CAPCOM must explicitly transmit the item;
- [x] CAPCOM transmission does not imply crew receipt;
- [x] explicit crew receipt is required before the crew shutdown command;
- [x] crew shutdown command remains separate from physical engine response;
- [x] explicit vehicle DPS engine-off response occurs at current authoritative GET;
- [x] no response delay, chamber-pressure tailoff, or automatic shutdown-confirmation telemetry is synthesized;
- [x] domain and HTTP tests cover communication → receipt → command → physical-response ordering.

See research notes 082, 083, and 085.

## Active priority — fresh controller-observable shutdown evidence

1. expose an explicit crew shutdown report as one evidence channel;
2. feed a fresh post-command `GQ6510P` chamber-pressure observation through the existing controller product path;
3. reuse `shutdown_confirmation.py` to report evidence availability (`NONE`, `CREW_REPORTED`, `GROUND_PRESSURE_OBSERVED`, `CORROBORATED`);
4. do **not** create an automatic `engine_off_confirmed` verdict or pressure threshold;
5. ensure pre-command chamber-pressure observations cannot count as shutdown evidence;
6. then exercise the full ΔP branch end-to-end through controller-visible evidence.

## Integration validation still required

When a runnable repository environment is available:

- execute the complete domain/session/API suite;
- exercise several phone/browser clients against one server;
- verify reload/rejoin does not change mission state;
- verify station information isolation;
- verify GET continues through pending controller decisions;
- verify explicit pause is the only normal clock stop;
- verify late decisions create missed-event consequences rather than retroactive event execution;
- verify the nominal timeline reaches power-down when prerequisites are satisfied on time;
- verify the ΔP nonnominal path through CONTROL and CAPCOM;
- verify transmission → crew receipt → crew command → physical response ordering;
- validate fresh shutdown evidence through the normal controller path.

## Explicitly deferred

- exact console pixel/character reconstruction;
- singular 150-psi inlet-pressure aggregation;
- exact onboard 77-percent thrust indication;
- detailed DPS transient timing;
- full RTCC trajectory propagator;
- backroom/staff-support simulation;
- low-player-count station aggregation;
- multi-session/durable production persistence;
- historical SimSup UI;
- numeric PC+2 allowable-delay/retargeting model without direct evidence;
- time-acceleration controls.

## Current success criterion

A rejoin-safe phone-accessible prototype running a **continuous authoritative mission clock** in which player actions affect event eligibility and mission evolution, and a source-bounded nonnominal condition can move through **source observation → correct station information → controller decision → CAPCOM transmission → explicit crew receipt/action → physical response → fresh controller evidence**, with no hidden automatic decisions or invented historical routing.
