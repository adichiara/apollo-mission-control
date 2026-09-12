# Roadmap addendum — first playable PC+2 integration

Date: 2026-09-12  
Status: **CURRENT — browser rejoin, first nonnominal web/session path, and explicit crew-response domain chain implemented; HTTP crew-response exposure is next**

## Completed presentation/session/web checkpoints

- [x] minimum player presentations for CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, FLIGHT, CAPCOM;
- [x] one authoritative mission state and synchronized GET;
- [x] deterministic scenario advancement, lifecycle, and audit log;
- [x] unique station assignment and station-scoped snapshots;
- [x] readiness reports surfaced to FLIGHT;
- [x] explicit FLIGHT GO/NO-GO decision gate;
- [x] explicit FLIGHT/CAPCOM queue and transmission path;
- [x] scripted nominal seven-station playthrough;
- [x] FastAPI/Uvicorn JSON transport and phone client;
- [x] Render configuration and health endpoint;
- [x] idempotent same-player/same-station server rejoin;
- [x] browser `localStorage` persistence of prototype player/station identity and automatic rejoin after reload;
- [x] explicit simulation-pause semantics for blocking decision gates (research note 081).

The current deployment architecture remains single-process/in-memory. Restart or redeploy loses the live session; multiple workers/sessions remain deferred.

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

## Active priority — expose crew response and reconnect evidence

1. expose explicit crew receipt and crew DPS shutdown command through the HTTP validation interface;
2. expose an explicit scenario/vehicle physical-response operation without inventing timing;
3. reuse the existing shutdown-confirmation architecture after physical engine-off;
4. require fresh controller evidence rather than treating physical state as automatically player-visible;
5. do not invent exact response delay, cockpit choreography, pressure tailoff, or a binary chamber-pressure confirmation threshold.

## Integration validation still required

When a runnable repository environment is available:

- execute the complete domain/session/API suite;
- exercise several phone/browser clients against one server;
- verify reload/rejoin does not change mission state;
- verify station information isolation;
- verify decision-gate pause/resume behavior;
- verify the nominal timeline reaches power-down;
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

A rejoin-safe phone-accessible prototype in which a source-bounded nonnominal condition can move through **source observation → correct station information → controller decision → CAPCOM transmission → explicit crew receipt/action → physical response → fresh controller evidence**, with no hidden automatic decisions or invented historical routing.
