# Roadmap addendum — first playable PC+2 integration

Date: 2026-09-12  
Status: **CURRENT — browser rejoin and first nonnominal web/session path implemented; crew-response integration is next**

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

## Active priority — crew-response boundary

Research and integrate the next stage without collapsing layers:

1. crew receipt/response to a transmitted shutdown callout must be an explicit communication/operational event;
2. crew DPS shutdown command must use the existing operational-action model;
3. crew command must remain separate from physical engine response;
4. physical DPS shutdown must remain separate from crew report and fresh controller evidence;
5. do not invent exact response delay, exact cockpit sequence, or a binary chamber-pressure confirmation threshold.

The existing research/implementation for command, physical response, and shutdown confirmation should be reused rather than replaced by a special-case scenario script.

## Integration validation still required

When a runnable repository environment is available:

- execute the complete domain/session/API suite;
- exercise several phone/browser clients against one server;
- verify reload/rejoin does not change mission state;
- verify station information isolation;
- verify decision-gate pause/resume behavior;
- verify the nominal timeline reaches power-down;
- verify the ΔP nonnominal path through CONTROL and CAPCOM;
- then validate the crew-command/physical-response continuation.

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

A rejoin-safe phone-accessible prototype in which a source-bounded nonnominal condition can move through **source observation → correct station information → controller decision → CAPCOM transmission → explicit crew action → physical response/evidence**, with no hidden automatic decisions or invented historical routing.
