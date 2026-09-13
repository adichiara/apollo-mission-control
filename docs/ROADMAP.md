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

The primary research chain now runs through notes **048–106**. Notes 098–099 establish and implement the staged final state-vector/target-load/uplink workflow; note 100 defines the backroom/SSR scope boundary; note 101 resolves immediate post-burn closure while preserving an unresolved timing-source tension; note 102 resolves the spacecraft-physics scope as a decision-relevant causal model; note 103 resolves MSFN/CCATS/RTCC scope as functional ground-data services rather than full ground-computer emulation; note 104 resolves the first-playable sensor/telemetry-failure scope as layered, explicitly authored observation faults rather than a generic random telemetry-failure mechanic; note 105 resolves first-playable crew representation as an explicit scenario-authored external actor rather than an additional player or automatic controller-side effect; note **106** narrows the unresolved 150-psi ground inlet-pressure lineage toward **fuel inlet pressure / `GQ3611P`** without claiming an Apollo 13-specific exact mapping or changing executable behavior.

Current detailed integration roadmap: `docs/roadmap/2026-09-12_first_playable_integration.md`.

### Player-count boundary

Full configuration: seven station players — FLIGHT, CAPCOM, CONTROL, TELMU, GUIDO, FIDO/RETRO, and INCO.

Minimum supported compact PC+2 configuration: five players — FLIGHT; CAPCOM; LM SYSTEMS = TELMU + CONTROL; FLIGHT DYNAMICS = GUIDO + FIDO/RETRO; INCO.

The spacecraft crew is not an additional first-playable player. Decision **D-021** keeps crew receipt/action explicit in the scenario model while retaining CAPCOM as the player-facing communication boundary.

This is a project adaptation, not a historical staffing claim. Decision **D-018** and research notes **091–094** require compact play to map one player to a set of original station identities rather than create synthetic historical stations. Original station products, actions, readiness, authorization, and audit identities remain distinct.

## Phase 3 — Display and console reconstruction

**Status:** minimum PC+2 player-presentation checkpoint complete.

First-pass views exist for CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, FLIGHT, and CAPCOM. Exact semantics are retained where sourced; project renderings remain labeled where exact routing/layout is unresolved; **hidden integrity does not leak**, and missing fields are not turned into invented telemetry failures.

## Phase 4 — Authoritative simulation model

**Status:** first-playable authoritative model, compact transport/client integration, staged final-load workflow, spacecraft-model boundary, ground-data-processing boundary, observation-failure boundary, and crew-action boundary established; physical multi-device execution remains.

Implemented architecture includes station-specific projections, explicit injection/action/communication/decision/physical/evidence layers, `PC2Session`, continuous mission time, readiness/FLIGHT decisions, CAPCOM queue/transmission, audit logging, facilitator authority, browser rejoin, compact station-set ownership, and staged final PC+2 solution/uplink state.

Decision **D-016** remains canonical: GET advances whenever RUNNING; controller decisions do not stop GET; only explicit session pause stops time; ineligible nominal events are missed rather than replayed later.

Decision **D-019** bounds spacecraft physics to sourced decision dependencies. Required causal domains are DPS/maneuver state, guidance/attitude/control state, coarse electrical/equipment availability, communications/uplink/ranging availability, and instrumentation observation integrity. Full-spacecraft emulation is not a first-playable requirement.

Research note **103** applies the same admission rule to MCC ground systems: MSFN/CCATS/RTCC are represented through decision-relevant availability, quality, routing, and generated-product states. IBM/UNIVAC internals, exact support-console keying, internal message formats, full network routing/geometry, and unsupported delays/failure rates are not first-playable requirements.

Decision **D-020** and research note **104** make observation integrity equally explicit: physical source, sensor/transducer, conditioning/PCM, communications/telemetry transport, ground processing, and station product remain separate layers. The nominal PC+2 run receives no invented historical sensor failure, and later observation faults are admitted only as sourced or explicitly synthetic scenario mechanisms—not random generic telemetry failures.

Decision **D-021** and research note **105** keep crew execution as a separate scenario layer. Controller conclusions do not directly cause crew/vehicle state changes; CAPCOM transmission, crew receipt/action, physical response, telemetry, and crew report remain distinct. Nominal crew actions may be deterministic scenario steps when crew discretion is not being tested, but unsupported crew delays/errors are not invented.

The synthetic ΔP branch remains explicitly non-historical and source-bounded:

`source observation → CONTROL product/rule → CONTROL decision → CAPCOM queue/transmission → crew receipt → crew shutdown command → physical DPS response → crew report / fresh GQ6510P observation → CONTROL evidence assessment`

The 26 psi exercise is explicitly non-historical. No unsupported internal routing, automatic crew compliance, response timing, telemetry synthesis, binary chamber-pressure threshold, or hidden engine-off truth is added. It is not retroactively explained as a failed pressure transducer.

Compact-role implementation preserves original station identities end to end:

`player → exact original station set → HTTP join/rejoin → bundled station-scoped snapshots → browser substation navigation → station-qualified readiness/actions/audit provenance`

## Phase 5 — Mission Control data path

**Status:** first-slice architecture, ground-processing scope, observation-integrity scope, and crew-interaction boundary established.

The project preserves:

`spacecraft/source state → instrumentation/telemetry → communications/ground processing → controller products → controller interpretation → player presentation → controller decisions/communications`

Station projections enforce information boundaries; source injections alter observations rather than announce diagnoses; **validity, age, hidden integrity, crew reports, telemetry, physical state, and controller conclusions remain distinct**.

Research note 102 reinforces that this chain is the physical-model admission test. Research note 103 defines the ground-processing portion explicitly:

`MSFN source/path → CCATS reception/routing/processing → RTCC processing/product generation → station-visible product/status`

Research note 104 further decomposes observation integrity:

`physical source → sensor/transducer → conditioning/PCM → communications/telemetry path → ground processing → station product`

Research note 105 defines the crew-control boundary:

`controller decision → CAPCOM transmission → crew receipt/action → physical response → telemetry / crew report → controller evidence`

Only states that materially affect a sourced player decision or selected failure path enter the executable model. A fresh but biased measurement is not the same condition as a missing/stale communications product, a bad ground-derived product is not automatically bad spacecraft telemetry, and a controller decision is not itself a crew action. Unsupported random fault rates, crew-error rates, response-delay distributions, or recovery times are not introduced.

The final PC+2 load path remains:

`FIDO/RTCC final solution → GUIDO load readiness/consistency → INCO uplink configuration → CAPCOM/crew P00 + DATA/ACCEPT + UPDATA LINK configuration → state-vector + target-load transmission → completion / computer returned to crew`

Exact Cartesian vector values, RTCC/CCATS command internals, exact controller key sequence, and exact transmission duration remain unfrozen. SSR-derived analysis is not silently invented inside this path.

## Phase 6 — Procedures and flight rules

**Status:** PC+2 core rule set operational; immediate post-burn boundary source-defined.

Implemented/evaluable: ISS warning + program alarm path, chamber-pressure observation, >25 psi ΔP ground callout, attitude criteria, inverter path, restart eligibility/sequence, crew STOP/off path, shutdown/restart evidence architecture, final state-vector/target-load staging, and final FLIGHT GO/NO-GO.

Research note **101** adds the first-playable post-burn sequence:

`burn cutoff/result → post-burn assessment → release from burn configuration → partial LM power-down → PTC preparation`

Primary Apollo 13 records place nominal PC+2 ignition at 79:27:38.30 GET, record PGNS residuals R1 +00010 / R2 +00003 / R3 +00000, place an initial LM power-down transition at about 79+33–79+34 while retaining PTC-required functions, and place the detailed PTC procedure at about 79+52. A separate change-of-shift briefing describes a power-down timing of roughly cutoff +15 minutes; research note 101 preserves that as an unresolved timing-source tension rather than silently reconciling it. The project does not infer exact console keying, an unsupported formal post-burn poll, exact switch-by-switch timing, or full PTC dynamics.

Research note **106** revisits the unresolved 150-psi ground inlet-pressure criterion. Apollo 13 explicitly described the PC+2 rules as similar to LOI Mode I abort with tight limits; a surviving Apollo 10 DPS mission rule names **fuel inlet pressure <150 psi for >65% throttle**. LM-7 documentation identifies `GQ3611P` as engine-interface fuel pressure. This makes fuel inlet / `GQ3611P` the leading historical candidate, but Apollo 13-specific rule/display/routing evidence explicitly tying PC+2 to that measurement has not been recovered. The rule therefore remains `NOT_EVALUABLE`; no minimum/average/either-side or synthetic combined inlet-pressure product is authorized.

Still intentionally unresolved where evidence is insufficient: Apollo 13-specific confirmation of the 150-psi fuel-inlet mapping, exact onboard 77-percent thrust indication, exact startup transient boundary, exact alternate-inverter detail, and exact final-load ground-system internals.

## Phase 7 — Simulation scenarios / SimSup

**Status:** repository-side first-playable preparation complete; physical validation remains.

Live-play protocol, structured evidence/debrief capture, scenario-blind player preparation/reference packet, facilitator separation, compact-mode integration, staged final-load workflow, backroom scope rule, source-bounded post-burn closure, decision-relevant spacecraft-model scope, functional ground-data-processing scope, layered observation-failure scope, and explicit scenario-authored crew-action scope are documented.

Modern HTTP/browser/localStorage/token/report/preparation/reference-packet/facilitator crew-step mechanics are project infrastructure, not Apollo reconstruction.

## Immediate next work

The primary remaining validation boundary is **physical human/device execution**.

1. Prepare participants with `docs/testing/PC2_PLAYER_PREPARATION.md` and `PC2_PLAYER_REFERENCE_PACKET.md`; preserve scenario blindness.
2. Execute `PC2_LIVE_PLAYTEST_PROTOCOL.md` with separate real-phone/browser clients and one facilitator console: nominal PC+2 first, synthetic ΔP second.
3. In the nominal run, continue past engine cutoff through the note-101 post-burn assessment/power-down/PTC-preparation transition; do not treat cutoff as scenario completion, improvise extra telemetry/sensor faults, or add unsourced crew delays/errors.
4. Record incidents with `PC2_LIVE_PLAYTEST_REPORT_TEMPLATE.md`, retaining preparation/GET/station/device/build/audit provenance.
5. Validate packet findability and clarity separately from historical correctness.
6. Exercise the approved five-player compact configuration with simultaneous clients, especially TELMU↔CONTROL and GUIDO↔FIDO-RETRO switching.
7. Verify station-qualified readiness/action attribution, CAPCOM→crew sequencing, and information isolation in facilitator audit output.
8. Repair reproducible network/mobile/presentation/instruction defects and add regression coverage.
9. Reopen historical, spacecraft-model, observation-integrity, crew-action, or ground-processing research only when validation exposes a concrete missing procedure, authority, information, terminology, display, support-room product, player-count dependency, causal spacecraft mechanism, observation failure, crew-discretion dependency, or ground-data-path dependency.

Research note 106 is a bounded archival refinement, not a change to that priority ordering.

## Explicitly deferred

- exact console pixel/character reconstruction;
- Apollo 13-specific proof that the singular 150-psi ground criterion maps directly to fuel interface pressure `GQ3611P`; fuel inlet is the leading lineage-supported candidate, while minimum/average/either-side aggregation remains unsupported;
- exact onboard 77-percent thrust indication without direct evidence;
- detailed DPS transient timing beyond selected branch needs;
- full six-degree-of-freedom spacecraft/orbital propagation;
- pulse-level RCS jet dynamics;
- full LM ECS and dormant CSM subsystem physics for this slice;
- detailed battery chemistry, wiring, breaker, and RF propagation/modulation physics;
- complete LM instrumentation-channel emulation;
- random/generic sensor or telemetry faults, unsupported failure probabilities, noise/bias distributions, durations, correlations, or recovery timing;
- random crew-error/noncompliance mechanics or unsupported response-delay distributions;
- a separate human spacecraft-crew role until a selected scenario requires decision-relevant astronaut discretion/workload/manual operation;
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

Research notes 095–106 and associated testing/scope documentation improve physical-run evidence quality and bounded historical interpretation but do not constitute physical validation. Physical seven-seat and five-player compact human/device PASS claims remain unmade.