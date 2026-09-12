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

**Status:** selected and implemented to first-playable integration level.

Selected slice: **Apollo 13 PC+2 preparation/execution**, starting at approximately **77:55 GET** and continuing through immediate post-burn verification/power-down.

The primary research chain now runs through notes **048–086**, including:

- controller actions/rules and initialization;
- nominal event timeline and throttle/ullage profile;
- controller-product projections;
- shutdown/restart rules and evidence;
- station presentation boundaries;
- authoritative session integration;
- web transport;
- continuous mission-clock semantics;
- ΔP nonnominal session path;
- crew response;
- HTTP crew-response integration;
- fresh shutdown-evidence integration.

Current first-playable integration roadmap: `docs/roadmap/2026-09-12_first_playable_integration.md`.

Low-player-count station aggregation remains unresolved.

## Phase 3 — Display and console reconstruction

**Status:** minimum PC+2 player-presentation checkpoint complete.

Implemented first-pass player views:

- CONTROL;
- GUIDO;
- TELMU;
- FIDO/RETRO;
- INCO;
- FLIGHT;
- CAPCOM.

Presentation rules remain conservative:

- exact historical semantics are retained where sourced;
- project renderings are labeled where exact CRT routing/layout is unresolved;
- hidden product-integrity metadata is never exposed automatically;
- missing implementation fields are not presented as telemetry failures;
- `GQ6510P` psi is not falsely labeled as Apollo 13 MSK 1137 `TCP` percent;
- TELMU's documented 38–40 A burn-configuration figure remains a reference value, not fabricated live telemetry;
- GUIDO residuals are not substituted for a missing FIDO propagated trajectory solution.

Further display archaeology is demand-driven.

## Phase 4 — Authoritative simulation model

**Status:** first playable authoritative model implemented; integration validation remains.

Completed architecture:

- framework-neutral PC+2 state/event model;
- source/sample/receive/process/display metadata;
- station-specific controller products;
- shutdown-rule evaluation without a generic `burn_abort` abstraction;
- scenario injection, operational action, communication, controller-decision, physical-response, and evidence layers kept distinct;
- premature-shutdown/restart branch;
- crew-command versus physical DPS response separation;
- fresh controller evidence after shutdown/restart;
- single-process authoritative `PC2Session`;
- station assignment and station-scoped snapshots;
- readiness reports and explicit FLIGHT decision state;
- CAPCOM queue/transmission path;
- browser rejoin persistence;
- audit log.

### Continuous mission-time architecture

Accepted decision **D-016** supersedes the earlier provisional decision-pause model.

The engine is a continuously evolving mission:

- GET advances while the session is `RUNNING`;
- controller decisions do not stop GET;
- only explicit game/session pause stops simulated time;
- nominal events have declarative prerequisites;
- an event whose prerequisites are missing at its nominal GET is recorded as missed;
- missed nominal events are not replayed retroactively.

Reusable implementation:

- `event_eligibility.py`;
- `pc2_event_rules.py`;
- `realtime_clock.py`.

The web layer now uses **1× monotonic wall-clock pacing**. Manual `/advance` remains validation/development infrastructure only.

See research notes 081 and 084.

### First integrated nonnominal branch

The synthetic source-bounded PC+2 fuel/oxidizer ΔP branch now reaches controller evidence end to end:

`source observation → CONTROL product/rule → CONTROL decision → CAPCOM queue/transmission → crew receipt → crew shutdown command → physical DPS response → crew report / fresh GQ6510P observation → CONTROL evidence assessment`

Guardrails:

- the synthetic 26 psi exercise is non-historical;
- exact CONTROL→FLIGHT→CAPCOM routing is not claimed;
- CAPCOM transmission does not imply crew receipt/compliance;
- crew command does not imply physical response;
- physical response does not synthesize telemetry;
- pre-command chamber-pressure observations cannot count as response evidence;
- no pressure magnitude is interpreted as a binary engine-off threshold;
- CONTROL evidence assessment never inspects authoritative `engine_running` state;
- no `engine_off_confirmed` truth flag is invented.

See research notes 082, 083, 085, and 086.

## Phase 5 — Mission Control data path

**Status:** first-slice architecture established.

The project preserves:

`spacecraft/source state → instrumentation/telemetry → communications/ground processing → controller products → controller interpretation → player presentation → controller decisions/communications`

Current guarantees:

- station projections enforce information boundaries;
- source injections alter observations rather than announcing diagnoses;
- validity, age, and hidden integrity remain separate concepts;
- controller suspicion/rejection is explicit;
- crew reports, telemetry evidence, physical state, and controller conclusions remain distinct;
- HTTP transport remains a thin adapter over domain logic.

## Phase 6 — Procedures and flight rules

**Status:** PC+2 core rule set operational for the first slice.

Implemented/evaluable:

- ISS-warning + program-alarm shutdown path;
- ground chamber-pressure rule when an explicit observation exists;
- fuel/oxidizer ΔP >25 psi ground-callout rule;
- attitude-error/rate criteria;
- inverter-warning-after-switch path;
- premature-shutdown restart eligibility and sequence;
- crew STOP/off command path;
- shutdown/restart evidence architecture;
- final FLIGHT GO/NO-GO decision as a player/controller decision requirement.

Intentionally unresolved / `NOT_EVALUABLE` where appropriate:

- exact onboard 77-percent thrust indication;
- singular 150-psi ground inlet-pressure selection/aggregation;
- exact startup-transient time boundary;
- exact alternate-inverter switch identity/details.

## Phase 7 — Simulation scenarios / SimSup

**Status:** source-bounded scenario architecture implemented for first-slice validation.

Completed:

- scenario evidence classes;
- source-condition → dependent-effects architecture;
- explicit timed/source-state injections;
- separation of injections, operational actions, communications, controller decisions, physical responses, and evidence;
- inverter contingency branch;
- premature DPS shutdown/restart branch;
- ground-call ΔP shutdown branch;
- continuous-time nominal event processing;
- HTTP validation path through crew response and controller evidence.

A historical SimSup operator UI remains deferred.

## Immediate next work

The primary need is now **runnable integrated validation**, not additional low-value subsystem reconstruction.

1. Execute the complete domain/session/API test suite in a runnable checked-out environment.
2. Exercise several phone/browser clients against one authoritative server.
3. Run the complete synthetic ΔP branch through the live browser/API path.
4. Verify realtime GET under concurrent polling/actions, explicit pause/resume, reload/rejoin, and station information isolation.
5. Review the phone UI for continuous realtime operation.
6. Separate validation/admin controls from normal player-facing controls before broader playtesting.
7. Reopen historical research only when integrated play exposes a concrete missing information, procedure, or decision dependency.

## Explicitly deferred

- exact console pixel/character reconstruction;
- singular 150-psi inlet-pressure aggregation unless a direct source becomes useful;
- exact onboard 77-percent thrust indication unless a direct source becomes useful;
- detailed DPS transient timing;
- full RTCC trajectory propagator;
- backroom/staff-support simulation;
- low-player-count station aggregation;
- multi-session/durable production persistence;
- historical SimSup UI;
- numeric PC+2 allowable-delay/retargeting model without direct evidence;
- time-acceleration controls.

## Validation status

New domain/API tests are committed, including continuous-clock, declarative-event, crew-response, and shutdown-evidence tests. A fresh local execution attempt on 2026-09-12 failed before checkout because the execution environment could not resolve `github.com`; therefore the repository test suite is **not recorded as passing**.
