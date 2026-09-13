# Roadmap

This roadmap separates historical reconstruction from software simplification. Dated research/progress records preserve implementation history; this file records the current canonical state.

## Phase 0 — Foundation and provenance

**Status:** substantially complete.

Completed: repository baseline, research-first authenticity policy, source catalog/research-note structure, simulation architecture, and decision log.

Open: primary-source mirroring policy and standardized implementation citation format.

## Phase 1 — Reconstruct Apollo Mission Control

**Status:** research-sufficient to proceed; not historically exhaustive.

Core Apollo 13 front-room positions are at B or better, with EECOM at A. Exact console/display reconstruction remains incomplete for several stations but is not a prerequisite where missing detail does not affect the selected scenario. Further historical work is demand-driven.

## Phase 2 — First playable mission/scenario

**Status:** implemented to first-playable integration level; physical human/device execution remains.

Selected slice: **Apollo 13 PC+2 preparation/execution**, starting at approximately **77:55 GET** and continuing through immediate post-burn verification/power-down.

The primary research chain now runs through notes **048–093**, including controller rules/actions, nominal timing, products, station presentations, authoritative session integration, continuous mission time, the source-bounded ΔP branch, crew/vehicle response, fresh controller evidence, player/admin separation, facilitator authority, automated multi-client validation, live-device validation, compact-role research, multi-station ownership, and compact HTTP/browser integration.

Current detailed integration roadmap: `docs/roadmap/2026-09-12_first_playable_integration.md`.

### Player-count boundary

Full configuration: seven station players — FLIGHT, CAPCOM, CONTROL, TELMU, GUIDO, FIDO/RETRO, INCO.

Approved compact project configuration: five players — FLIGHT; CAPCOM; LM SYSTEMS = TELMU + CONTROL; FLIGHT DYNAMICS = GUIDO + FIDO/RETRO; INCO.

This is a usability adaptation constrained by Apollo organizational evidence, not a historical staffing claim. Original station products, actions, readiness, authorization, and audit identities remain distinct. Four-player-or-smaller aggregation remains unresolved.

## Phase 3 — Display and console reconstruction

**Status:** minimum PC+2 player-presentation checkpoint complete.

First-pass views exist for CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, FLIGHT, and CAPCOM. Presentation remains conservative: exact semantics are retained where sourced; project renderings are labeled where exact routing/layout is unresolved; hidden integrity does not leak; missing fields are not turned into invented telemetry failures.

## Phase 4 — Authoritative simulation model

**Status:** first-playable authoritative model and compact transport/client integration implemented and passing automated CI; physical multi-device execution remains.

Implemented architecture includes framework-neutral state/event logic, station-specific products, rules, explicit injection/action/communication/decision/physical/evidence layers, shutdown/restart branches, `PC2Session`, continuous realtime pacing, readiness/FLIGHT decisions, CAPCOM queue/transmission, audit logging, facilitator authority, single-station browser rejoin, and compact station-set ownership.

### Continuous mission time

Decision **D-016** remains canonical: GET advances while RUNNING; controller decisions do not stop GET; only explicit game/session pause stops advancement; nominal events use declarative prerequisites; ineligible nominal events are recorded as missed rather than replayed later.

### Nonnominal ΔP branch

The synthetic source-bounded path remains:

`source observation → CONTROL product/rule → CONTROL decision → CAPCOM queue/transmission → crew receipt → crew shutdown command → physical DPS response → crew report / fresh GQ6510P observation → CONTROL evidence assessment`

The 26 psi exercise is explicitly non-historical. No unsupported internal routing, automatic crew compliance, response timing, telemetry synthesis, binary chamber-pressure threshold, or hidden engine-off truth is added.

### Compact-role architecture

Decision **D-018** and research notes **091–093** require compact play to map one player to a set of original stations rather than create synthetic historical stations.

Implemented end to end:

`player → exact original station set → HTTP join/rejoin → bundled station-scoped snapshots → browser substation navigation → station-qualified readiness/actions/audit provenance`

`PC2Session.assign_stations()`, `stations_for()`, `owns_station()`, station-qualified readiness, and `bundled_player_snapshot()` provide the domain boundary. `/api/session/join-set` exposes it without breaking `/api/session/join`. The browser persists station sets and active substations, migrates legacy single-station identity, and keeps original call signs visible. `LM_SYSTEMS` and `FLIGHT_DYNAMICS` remain presentation-only project labels, not authoritative station identities.

## Phase 5 — Mission Control data path

**Status:** first-slice architecture established.

The project preserves:

`spacecraft/source state → instrumentation/telemetry → communications/ground processing → controller products → controller interpretation → player presentation → controller decisions/communications`

Station projections enforce information boundaries; source injections alter observations rather than announce diagnoses; validity, age, hidden integrity, crew reports, telemetry, physical state, and controller conclusions remain distinct.

## Phase 6 — Procedures and flight rules

**Status:** PC+2 core rule set operational.

Implemented/evaluable: ISS warning + program alarm path, chamber-pressure observation, >25 psi ΔP ground callout, attitude criteria, inverter path, restart eligibility/sequence, crew STOP/off path, shutdown/restart evidence architecture, and final FLIGHT GO/NO-GO.

Still intentionally unresolved where evidence is insufficient: exact onboard 77-percent thrust indication, singular 150-psi inlet-pressure selection/aggregation, exact startup transient boundary, and exact alternate-inverter detail.

## Phase 7 — Simulation scenarios / SimSup

**Status:** source-bounded scenario architecture, facilitator authority, automated integration validation, live-play protocol, and compact browser integration implemented.

Modern HTTP/browser/localStorage/token/compact-role mechanics are project infrastructure, not Apollo reconstruction.

## Immediate next work

Automated compact-path validation is now complete. The primary remaining validation boundary is **physical human/device execution**.

1. Execute `docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md` using separate real phone/browser clients and one facilitator console; nominal PC+2 first, synthetic ΔP second.
2. Exercise the approved five-player compact configuration with actual simultaneous clients, especially TELMU↔CONTROL and GUIDO↔FIDO/RETRO switching under time pressure.
3. Verify station-qualified readiness/action attribution and information isolation in facilitator audit output.
4. Repair reproducible network/mobile/presentation defects and add regression coverage.
5. Reopen historical research only when validation exposes a concrete missing procedure, authority, information, or terminology dependency.

## Explicitly deferred

- exact console pixel/character reconstruction;
- singular 150-psi inlet-pressure aggregation without direct evidence;
- exact onboard 77-percent thrust indication without direct evidence;
- detailed DPS transient timing;
- full RTCC trajectory propagator;
- backroom/staff-support simulation;
- four-player-or-smaller aggregation;
- multi-session/durable production persistence;
- historically exact SimSup console UI;
- named facilitator accounts/fine-grained admin permissions;
- cryptographic player authentication;
- numeric PC+2 allowable-delay/retargeting model without direct evidence;
- time acceleration.

## Validation status

Automated coverage includes continuous-clock/event rules, crew response, shutdown evidence, player/admin separation, facilitator authority, multi-client integration, multi-station ownership, compact HTTP station-set join/rejoin, station-qualified readiness, original-station conflict enforcement, compact CONTROL authorization, and browser compact-role/persistence/navigation contracts.

GitHub Actions run 59 on commit `ae569dff997c17b0f67546ea452f1706d34b693d` passed after correcting a compact CONTROL regression-test expectation that had conflated authorization with evidence availability. The compact HTTP/browser implementation is therefore recorded as passing automated CI. Physical seven-seat and five-player compact human/device validation remain unclaimed.
