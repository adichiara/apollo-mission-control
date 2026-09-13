# Roadmap

This roadmap deliberately separates historical reconstruction from software simplification. Detailed dated progress records and research notes preserve the implementation history; this file records the current canonical project state.

## Phase 0 — Foundation and provenance

**Status:** substantially complete.

Completed:

- project/repository baseline;
- research-first authenticity policy;
- source catalog and research-note structure;
- simulation architecture and decision log.

Still open:

- decide whether/how primary-source files themselves should be mirrored in-repo;
- standardize source citation format for implementation/code comments.

## Phase 1 — Reconstruct Apollo Mission Control

**Status:** research-sufficient to proceed; not historically exhaustive.

Core Apollo 13 front-room positions are at B or better, with EECOM at A. Exact console/display reconstruction remains incomplete for several stations but is no longer a prerequisite where missing detail does not affect the selected scenario.

Further historical work is demand-driven by integrated play or a concrete scenario dependency.

## Phase 2 — First playable mission/scenario

**Status:** selected and implemented to first-playable integration level; live human/device execution remains.

Selected slice: **Apollo 13 PC+2 preparation/execution**, starting at approximately **77:55 GET** and continuing through immediate post-burn verification/power-down.

The primary research chain now runs through notes **048–090**, including controller actions/rules, initialization, nominal timing, product projections, shutdown/restart behavior, station presentations, authoritative session integration, continuous mission time, the ΔP nonnominal path, crew/vehicle response, fresh controller evidence, player/admin UI separation, facilitator authority, integrated multi-client validation, and the live-device/human-play validation boundary.

Current first-playable integration roadmap: `docs/roadmap/2026-09-12_first_playable_integration.md`.

Low-player-count station aggregation remains unresolved.

## Phase 3 — Display and console reconstruction

**Status:** minimum PC+2 player-presentation checkpoint complete.

Implemented first-pass player views: CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, FLIGHT, and CAPCOM.

Presentation remains conservative: exact semantics are retained where sourced; project renderings are labeled where exact CRT routing/layout is unresolved; hidden integrity does not leak to players; missing fields are not presented as telemetry failures; `GQ6510P` psi is not mislabeled as MSK 1137 `TCP` percent; TELMU's 38–40 A burn figure remains a reference value; and GUIDO residuals are not substituted for a FIDO propagated trajectory solution.

Further display archaeology is demand-driven.

## Phase 4 — Authoritative simulation model

**Status:** first playable authoritative model implemented; automated in-process and real-network validation passing; live multi-device execution remains.

Completed architecture includes framework-neutral state/event logic, station-specific products, rule evaluation, distinct injection/action/communication/decision/physical-response/evidence layers, restart/shutdown branches, `PC2Session`, station-scoped snapshots, readiness/FLIGHT decisions, CAPCOM queue/transmission, browser rejoin, audit logging, realtime wall-clock pacing, and a multi-client HTTP contract harness.

### Continuous mission-time architecture

Accepted decision **D-016** supersedes the earlier provisional decision-pause model.

- GET advances while `RUNNING`;
- controller decisions do not stop GET;
- explicit game/session pause is the normal clock stop;
- nominal events use declarative prerequisites;
- ineligible nominal events are recorded as missed and are not replayed retroactively.

Reusable implementation: `event_eligibility.py`, `pc2_event_rules.py`, and `realtime_clock.py`.

### First integrated nonnominal branch

The synthetic source-bounded PC+2 fuel/oxidizer ΔP branch now reaches controller evidence end to end:

`source observation → CONTROL product/rule → CONTROL decision → CAPCOM queue/transmission → crew receipt → crew shutdown command → physical DPS response → crew report / fresh GQ6510P observation → CONTROL evidence assessment`

The 26 psi exercise is explicitly non-historical. No unsupported internal routing, automatic crew compliance, response timing, telemetry synthesis, binary chamber-pressure threshold, or hidden engine-off truth is added.

### Multi-client validation

`tests/test_web_multiclient_integration.py` checks several independent station clients plus facilitator authority against one authoritative in-process session.

`scripts/pc2_multiclient_smoke.py` exercises the same boundaries over real TCP/HTTP: simultaneous station polling, rejoin, pause/resume, authority isolation, the complete synthetic ΔP branch, controller evidence, and audit ordering.

GitHub Actions launches a dedicated ephemeral Uvicorn server with facilitator authorization enabled and runs both the complete unit/integration suite and the real-network smoke successfully. This is not a claim that deployed/mobile validation has already passed.

### Live-device / human-play protocol

Research note 090 and `docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md` define the remaining physical validation as a structured integrated mission rehearsal. Apollo/NASA sources support combined crew/controller mission-environment simulation and decisionmaking/procedure readiness, but do not establish mobile UI, browser reload, HTTP latency, or token-authentication criteria. Those remain explicitly modern project concerns.

## Phase 5 — Mission Control data path

**Status:** first-slice architecture established.

The project preserves:

`spacecraft/source state → instrumentation/telemetry → communications/ground processing → controller products → controller interpretation → player presentation → controller decisions/communications`

Station projections enforce information boundaries; source injections alter observations rather than announce diagnoses; validity, age, and hidden integrity remain distinct; crew reports, telemetry, physical state, and controller conclusions remain separate.

## Phase 6 — Procedures and flight rules

**Status:** PC+2 core rule set operational for the first slice.

Implemented/evaluable: ISS-warning + program-alarm path, chamber-pressure rule with explicit observation, >25 psi ΔP ground callout, attitude criteria, inverter path, restart eligibility/sequence, crew STOP/off path, shutdown/restart evidence architecture, and final FLIGHT GO/NO-GO as a player decision.

Intentionally unresolved where appropriate: exact onboard 77-percent thrust indication, singular 150-psi inlet-pressure selection/aggregation, exact startup-transient boundary, and exact alternate-inverter details.

## Phase 7 — Simulation scenarios / SimSup

**Status:** source-bounded scenario architecture, facilitator authority, automated integrated validation, and live-play protocol implemented.

Completed:

- scenario evidence classes and explicit source-state injection;
- separation of injections, actions, communications, decisions, physical responses, and evidence;
- inverter, premature-shutdown/restart, and ΔP branches;
- continuous-time event processing;
- HTTP validation path through crew response and controller evidence;
- ordinary player client separated from facilitator/validation client;
- primary-source review of Simulation Supervisor / simulation-control role separation;
- server-side facilitator credential protecting exercise-wide operations in configured deployments;
- Render-generated deployment secret with no credential committed to source;
- primary-source review supporting integrated controller simulation validation;
- in-process multi-client contract coverage;
- real-network multi-client smoke execution in CI;
- primary-source review supporting integrated live crew/controller rehearsal;
- structured nominal + synthetic ΔP real-device/human-play protocol.

The facilitator credential is a modern software safety boundary, **not** a claim about Apollo-era authentication. Integrated HTTP/browser validation mechanics are likewise modern infrastructure. See research notes 088–090.

## Immediate next work

The automated runnable-validation and protocol-definition boundaries are closed. The primary need is **physical multi-device/human execution**.

1. Execute `docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md` with separate real phone/browser clients for at least FLIGHT, CONTROL, CAPCOM, and GUIDO plus one facilitator console.
2. Run the nominal PC+2 sequence first, including identity/rejoin/isolation checks, continuous GET, readiness, FLIGHT decision, and FLIGHT→CAPCOM handoff without hidden facilitator coaching.
3. Repair blocking phone/network/station-presentation defects and add regression coverage where reproducible.
4. Run the existing synthetic ΔP branch only after nominal coordination is coherent.
5. Reopen historical research only when play exposes a concrete missing information, procedure, authority, or terminology dependency.

## Explicitly deferred

- exact console pixel/character reconstruction;
- singular 150-psi inlet-pressure aggregation unless a direct source becomes useful;
- exact onboard 77-percent thrust indication unless a direct source becomes useful;
- detailed DPS transient timing;
- full RTCC trajectory propagator;
- backroom/staff-support simulation;
- low-player-count station aggregation;
- multi-session/durable production persistence;
- historically exact SimSup console UI;
- named facilitator accounts or fine-grained admin permissions;
- cryptographic player authentication;
- numeric PC+2 allowable-delay/retargeting model without direct evidence;
- time-acceleration controls.

## Validation status

Domain/API tests include continuous-clock, declarative-event, crew-response, shutdown-evidence, client-role-separation, facilitator-authority, and multi-client integration coverage. The validation pass also repaired a stale admin-role UI test and invalid `/admin` evidence-class option values.

As of 2026-09-12, GitHub Actions successfully executes the complete unit/integration suite, the real-network multi-client smoke against an ephemeral authorized Uvicorn server, and the documentation audit. A source-bounded physical playtest protocol is now documented. Remaining validation is actual multi-device/mobile and human-play execution; no PASS claim for that boundary is recorded yet.
