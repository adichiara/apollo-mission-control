# Roadmap addendum — first playable PC+2 integration

Date: 2026-09-12  
Status: **CURRENT — continuous-time nonnominal chain now reaches fresh controller evidence; runnable integration validation is next**

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
- [x] HTTP validation path exposes crew receipt, crew shutdown command, and physical DPS engine-off response;
- [x] explicit crew shutdown report exposed as controller-observable evidence;
- [x] fresh post-command `GQ6510P` evidence integrated through the normal CONTROL product path;
- [x] shutdown evidence aggregation exposed to CONTROL without an automatic engine-off verdict.

The current deployment architecture remains single-process/in-memory. Restart or redeploy loses the live session; multiple workers/sessions remain deferred.

See D-016 and research notes 084–086.

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

Prerequisites are declared through the reusable event-eligibility layer rather than embedded as PC+2-specific session branches.

The web layer uses a monotonic realtime driver fixed at 1× and synchronizes the authoritative session on API interaction. Manual `/advance` remains only as development/validation infrastructure.

## First nonnominal session/API path — implemented through controller evidence

Primary Apollo 13 sources establish the PC+2 **fuel/oxidizer ΔP >25 psi** criterion as a **ground callout**, but do not establish the exact internal CONTROL→FLIGHT→CAPCOM routing, exact hypothetical response wording, response latency, or a binary ground engine-off threshold.

Implemented without filling those gaps:

- [x] explicit source-state injection through the existing whitelisted scenario-injection model;
- [x] CONTROL receives the ground-derived ΔP through the normal product/presentation path;
- [x] the existing common shutdown-rule evaluator determines whether the criterion is triggered;
- [x] CONTROL must explicitly issue the shutdown callout decision;
- [x] the callout enters the CAPCOM queue as `requested_by=CONTROL`;
- [x] CAPCOM must explicitly transmit the item;
- [x] CAPCOM transmission does not imply crew receipt;
- [x] explicit crew receipt is required before the crew shutdown command;
- [x] crew shutdown command remains separate from physical engine response;
- [x] explicit vehicle DPS engine-off response occurs at current authoritative GET;
- [x] explicit crew shutdown report is a separate evidence channel;
- [x] fresh post-command `GQ6510P` chamber-pressure observation is a separate evidence channel;
- [x] pre-command pressure cannot count as shutdown-response evidence;
- [x] CONTROL receives evidence availability only: `none`, `crew_reported`, `ground_pressure_observed`, or `corroborated`;
- [x] no pressure magnitude is treated as a binary engine-off threshold;
- [x] evidence assessment does not inspect hidden authoritative `engine_running` state.

See research notes 082, 083, 085, and 086.

## Active priority — runnable integration validation and player-surface cleanup

1. execute the full domain/session/API suite in a runnable checked-out environment;
2. exercise several phone/browser clients against one authoritative server;
3. run the complete synthetic ΔP branch through source observation → controller decision → CAPCOM → crew → vehicle → fresh controller evidence;
4. verify realtime GET behavior under concurrent client polling/actions and explicit pause/resume;
5. review the phone UI for continuous realtime operation;
6. separate validation/admin controls from normal player-facing controls before broader playtesting;
7. reopen historical research only if integrated play exposes a concrete missing decision dependency.

## Integration validation still required

- verify reload/rejoin does not change mission state;
- verify station information isolation;
- verify GET continues through pending controller decisions;
- verify explicit pause is the only normal clock stop;
- verify late decisions create missed-event consequences rather than retroactive event execution;
- verify the nominal timeline reaches power-down when prerequisites are satisfied on time;
- verify the full ΔP nonnominal branch and evidence freshness boundaries;
- verify CONTROL evidence never leaks authoritative physical truth.

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

A rejoin-safe phone-accessible prototype running a **continuous authoritative mission clock** in which player actions affect event eligibility and mission evolution, and a source-bounded nonnominal condition can move through **source observation → correct station information → controller decision → CAPCOM transmission → explicit crew receipt/action → physical response → fresh controller evidence**, with no hidden automatic decisions, hidden physical-truth leaks, or invented historical routing.
