# Roadmap

This roadmap separates historical reconstruction from software simplification. Dated research/progress records preserve implementation history; this file records the current canonical state.

## Phase 0 — Foundation and provenance

**Status:** substantially complete.

Repository baseline, research-first authenticity policy, source catalog/research-note structure, simulation architecture, decision log, and source-mirroring infrastructure are established. Standardized implementation citation format remains demand-driven.

## Phase 1 — Reconstruct Apollo Mission Control

**Status:** research-sufficient to proceed; not historically exhaustive.

Core Apollo 13 front-room positions are at B or better, with EECOM at A. Exact console/display reconstruction remains incomplete for several stations but is not a prerequisite where missing detail does not affect the selected scenario. Research note 100 makes the Staff Support Room boundary explicit: the seven-seat/five-player implementation is a front-room playable slice, not a complete staffing reconstruction.

## Phase 2 — First playable mission/scenario

**Status:** implemented to first-playable integration level; physical human/device execution remains.

Selected slice: **Apollo 13 PC+2 preparation/execution**, beginning near **77:55 GET** and continuing through immediate post-burn verification/power-down.

The primary research chain now runs through notes **048–103**. Notes 098–099 establish and implement the staged final state-vector/target-load/uplink workflow; note 100 defines the backroom/SSR scope boundary; note 101 resolves immediate post-burn closure; note 102 resolves the spacecraft-physics scope as a decision-relevant causal model; note **103** resolves MSFN/CCATS/RTCC scope as functional ground-data services rather than full ground-computer emulation.

Current detailed integration roadmap: `docs/roadmap/2026-09-12_first_playable_integration.md`.

### Player-count boundary

Full configuration: seven station players — FLIGHT, CAPCOM, CONTROL, TELMU, GUIDO, FIDO/RETRO, INCO.

Minimum supported compact PC+2 configuration: five players — FLIGHT; CAPCOM; LM SYSTEMS = TELMU + CONTROL; FLIGHT DYNAMICS = GUIDO + FIDO/RETRO; INCO.

This is a project adaptation, not a historical staffing claim. Original station products, actions, readiness, authorization, and audit identities remain distinct.

## Phase 3 — Display and console reconstruction

**Status:** minimum PC+2 player-presentation checkpoint complete.

First-pass views exist for CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, FLIGHT, and CAPCOM. Exact semantics are retained where sourced; project renderings remain labeled where exact routing/layout is unresolved.

## Phase 4 — Authoritative simulation model

**Status:** first-playable authoritative model, compact transport/client integration, staged final-load workflow, spacecraft-model boundary, and ground-data-processing boundary established; physical multi-device execution remains.

Implemented architecture includes station-specific projections, explicit injection/action/communication/decision/physical/evidence layers, `PC2Session`, continuous mission time, readiness/FLIGHT decisions, CAPCOM queue/transmission, audit logging, facilitator authority, browser rejoin, compact station-set ownership, and staged final PC+2 solution/uplink state.

Decision **D-016** remains canonical: GET advances whenever RUNNING; controller decisions do not stop GET; only explicit session pause stops time; ineligible nominal events are missed rather than replayed later.

Decision **D-019** bounds spacecraft physics to sourced decision dependencies. Required causal domains are DPS/maneuver state, guidance/attitude/control state, coarse electrical/equipment availability, communications/uplink/ranging availability, and instrumentation observation integrity. Full-spacecraft emulation is not a first-playable requirement.

Research note **103** applies the same admission rule to MCC ground systems: MSFN/CCATS/RTCC are represented through decision-relevant availability, quality, routing, and generated-product states. IBM/UNIVAC internals, exact support-console keying, internal message formats, full network routing/geometry, and unsupported delays/failure rates are not first-playable requirements.

The synthetic ΔP branch remains explicitly non-historical and source-bounded:

`source observation → CONTROL product/rule → CONTROL decision → CAPCOM queue/transmission → crew receipt → crew shutdown command → physical DPS response → crew report / fresh GQ6510P observation → CONTROL evidence assessment`

## Phase 5 — Mission Control data path

**Status:** first-slice architecture and ground-processing scope established.

The project preserves:

`spacecraft/source state → instrumentation/telemetry → communications/ground processing → controller products → controller interpretation → player presentation → controller decisions/communications`

Research note 102 reinforces that this chain is the physical-model admission test. Research note 103 now defines the ground-processing portion explicitly:

`MSFN source/path → CCATS reception/routing/processing → RTCC processing/product generation → station-visible product/status`

Only states that materially affect a sourced player decision or selected failure path enter the executable model. Tracking/ranging quality remains distinct from generated trajectory products, and ground systems must not leak hidden spacecraft truth.

The final PC+2 load path remains:

`FIDO/RTCC final solution → GUIDO load readiness/consistency → INCO uplink configuration → CAPCOM/crew P00 + DATA/ACCEPT + UPDATA LINK configuration → state-vector + target-load transmission → completion / computer returned to crew`

Exact Cartesian vector values, RTCC/CCATS command internals, exact controller key sequence, and exact transmission duration remain unfrozen. SSR-derived analysis is not silently invented inside this path.

## Phase 6 — Procedures and flight rules

**Status:** PC+2 core rule set operational; immediate post-burn boundary source-defined.

Implemented/evaluable: ISS warning + program alarm path, chamber-pressure observation, >25 psi ΔP ground callout, attitude criteria, inverter path, restart eligibility/sequence, crew STOP/off path, shutdown/restart evidence architecture, final state-vector/target-load staging, and final FLIGHT GO/NO-GO.

Research note **101** adds the first-playable post-burn sequence:

`burn cutoff/result → post-burn assessment → release from burn configuration → partial LM power-down → PTC preparation`

Primary Apollo 13 records place nominal PC+2 ignition at 79:27:38.30 GET, record PGNS residuals R1 +00010 / R2 +00003 / R3 +00000, place initial LM power-down at about 79+34 while retaining PTC-required functions, and place the detailed PTC procedure at about 79+52. The project does not infer exact console keying, an unsupported formal post-burn poll, exact switch-by-switch timing, or full PTC dynamics.

Still intentionally unresolved where evidence is insufficient: exact onboard 77-percent thrust indication, singular 150-psi inlet-pressure selection/aggregation, exact startup transient boundary, exact alternate-inverter detail, and exact final-load ground-system internals.

## Phase 7 — Simulation scenarios / SimSup

**Status:** repository-side first-playable preparation complete; physical validation remains.

Live-play protocol, structured evidence/debrief capture, scenario-blind player preparation/reference packet, facilitator separation, compact-mode integration, staged final-load workflow, backroom scope rule, source-bounded post-burn closure, decision-relevant spacecraft-model scope, and functional ground-data-processing scope are documented.

Modern HTTP/browser/localStorage/token/report/preparation/reference-packet mechanics are project infrastructure, not Apollo reconstruction.

## Immediate next work

The primary remaining validation boundary is **physical human/device execution**.

1. Prepare participants with `docs/testing/PC2_PLAYER_PREPARATION.md` and `PC2_PLAYER_REFERENCE_PACKET.md`; preserve scenario blindness.
2. Execute `PC2_LIVE_PLAYTEST_PROTOCOL.md` with separate real-phone/browser clients and one facilitator console: nominal PC+2 first, synthetic ΔP second.
3. In the nominal run, continue past engine cutoff through the note-101 post-burn assessment/power-down/PTC-preparation transition; do not treat cutoff as scenario completion.
4. Record incidents with `PC2_LIVE_PLAYTEST_REPORT_TEMPLATE.md`, retaining preparation/GET/station/device/build/audit provenance.
5. Validate packet findability and clarity separately from historical correctness.
6. Exercise the approved five-player compact configuration with simultaneous clients, especially TELMU↔CONTROL and GUIDO↔FIDO-RETRO switching.
7. Verify station-qualified readiness/action attribution and information isolation in facilitator audit output.
8. Repair reproducible network/mobile/presentation/instruction defects and add regression coverage.
9. Reopen historical, spacecraft-model, or ground-processing research only when validation exposes a concrete missing procedure, authority, information, terminology, display, support-room product, player-count dependency, causal spacecraft mechanism, or ground-data-path dependency.

## Explicitly deferred

- exact console pixel/character reconstruction;
- singular 150-psi inlet-pressure aggregation without direct evidence;
- exact onboard 77-percent thrust indication without direct evidence;
- detailed DPS transient timing beyond selected branch needs;
- full six-degree-of-freedom spacecraft/orbital propagation;
- pulse-level RCS jet dynamics;
- full LM ECS and dormant CSM subsystem physics for this slice;
- detailed battery chemistry, wiring, breaker, and RF propagation/modulation physics;
- complete LM instrumentation-channel emulation;
- full RTCC trajectory propagator and internal RTCC/CCATS computation;
- IBM 360/75 or UNIVAC 494 emulation, exact support-console keying, internal ground-system message formats, full MSFN routing/geometry, or unsupported processing delays/failure rates;
- exact PC+2 RTCC Cartesian vector contents/internal RTCC-CCATS load-keying/final-load transmission duration;
- exact post-burn controller console keying and switch-by-switch LM power-down timing;
- full PTC dynamics before a concrete scenario need;
- playable/detailed Staff Support Room reconstruction until a concrete dependency requires it;
- sub-five-player PC+2 mode unless reopened by live-play/scenario evidence;
- multi-session/durable production persistence;
- historically exact SimSup console UI;
- named facilitator accounts/fine-grained admin permissions;
- cryptographic player authentication;
- numeric PC+2 allowable-delay/retargeting model without direct evidence;
- time acceleration.

## Validation status

Automated coverage includes continuous-clock/event rules, crew response, shutdown evidence, player/admin separation, facilitator authority, multi-client integration, multi-station ownership, compact HTTP/browser contracts, and staged PC+2 final-load transitions/station products.

Research notes 095–103 and associated testing/scope documentation improve physical-run evidence quality and scenario closure but do not constitute physical validation. Physical seven-seat and five-player compact human/device PASS claims remain unmade.