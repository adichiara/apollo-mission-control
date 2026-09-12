# Roadmap addendum — first playable PC+2 integration

Date: 2026-09-12  
Status: **CURRENT — continuous mission clock adopted; dependency-driven integration is now the active priority**

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
- [x] **continuous mission clock** adopted: controller decisions do not stop GET;
- [x] explicit game/session pause retained as the only ordinary clock-stop mechanism;
- [x] nominal downstream events can be missed when prerequisites are absent and are not replayed retroactively.

The current deployment architecture remains single-process/in-memory. Restart or redeploy loses the live session; multiple workers/sessions remain deferred.

See D-016 and `resources/research/084_continuous_mission_clock_architecture.md`.

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

This turns timing itself into part of the simulation outcome rather than an artificial player timer or score.

## First nonnominal session/API path — implemented through CAPCOM transmission

Primary Apollo 13 sources establish the PC+2 **fuel/oxidizer ΔP >25 psi** criterion as a **ground callout**, but do not establish the exact internal CONTROL→FLIGHT→CAPCOM routing or exact call wording.

Implemented without filling those gaps:

- [x] explicit source-state injection through the existing whitelisted scenario-injection model;
- [x] CONTROL receives the ground-derived ΔP through the normal product/presentation path;
- [x] the existing common shutdown-rule evaluator determines whether the criterion is triggered;
- [x] CONTROL must explicitly issue the shutdown callout decision;
- [x] the callout enters the CAPCOM queue as `requested_by=CONTROL`;
- [x] queue metadata explicitly states that internal Apollo routing is unresolved;
- [x] CAPCOM must explicitly transmit the item;
- [x] transmission does **not** automatically create crew compliance or physical engine shutdown;
- [x] session/API tests cover the synthetic 26-psi threshold case and exact 25-psi non-trigger boundary.

See `resources/research/082_pc2_delta_p_session_integration_boundary.md`.

## Crew-response domain boundary — implemented

Primary-source review confirms the ground-call → crew-shutdown relationship but does not supply a response latency or unique hypothetical cockpit sequence for an actual ΔP exceedance.

Implemented as distinct layers:

- [x] CAPCOM transmission does not imply receipt;
- [x] crew receipt/acknowledgment is an explicit audit event;
- [x] crew DPS shutdown command requires prior receipt;
- [x] crew command reuses the existing operational-action model;
- [x] crew command does not directly set physical engine-off state;
- [x] physical DPS engine-off response reuses the existing vehicle-response helper;
- [x] physical-response GET is supplied by the caller rather than inferred from an invented delay;
- [x] no chamber-pressure tailoff or automatic shutdown-confirmation telemetry is synthesized;
- [x] integration tests cover communication → receipt → command → physical-response ordering.

See `resources/research/083_pc2_crew_response_after_ground_shutdown_call.md`.

## Active priority — make dependencies declarative, then continue HTTP integration

1. move nominal event prerequisites out of PC+2-specific session `if` statements into a reusable scenario-event eligibility model;
2. preserve the rule that missing prerequisites cause a nominal event to be missed, not delayed or replayed automatically;
3. expose explicit crew receipt and crew DPS shutdown command through the HTTP validation interface;
4. expose an explicit scenario/vehicle physical-response operation without inventing timing;
5. reconnect physical shutdown to the existing fresh controller-evidence path;
6. after runnable smoke validation, replace manual GET advancement with realtime pacing driven by wall clock while session status is `RUNNING`.

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
- verify communication → crew receipt → crew command → physical response ordering;
- then validate fresh shutdown evidence through the normal controller path.

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
- numeric PC+2 allowable-delay/retargeting model without direct evidence.

## Current success criterion

A rejoin-safe phone-accessible prototype running a **continuous authoritative mission clock** in which player actions affect event eligibility and mission evolution, and a source-bounded nonnominal condition can move through **source observation → correct station information → controller decision → CAPCOM transmission → explicit crew receipt/action → physical response → fresh controller evidence**, with no hidden automatic decisions or invented historical routing.
