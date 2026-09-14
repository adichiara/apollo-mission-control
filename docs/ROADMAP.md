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

The primary research chain now runs through notes **048–115**. Notes 098–099 establish and implement the staged final state-vector/target-load/uplink workflow; note 100 defines the backroom/SSR scope boundary; note 101 resolves immediate post-burn closure while preserving an unresolved timing-source tension; note 102 bounds spacecraft physics to decision-relevant causal fidelity; note 103 bounds MSFN/CCATS/RTCC to functional ground-data services; note 104 defines layered observation failures without random generic telemetry faults; note 105 keeps crew action explicit and scenario-authored; note 106 narrows the 150-psi ground inlet-pressure lineage toward fuel inlet / `GQ3611P` without claiming an Apollo 13-specific mapping; notes 107–108 identify the onboard ENG THRUST percent indication and bound first-playable applicability to the commanded full-throttle transition; notes 109–110 allocate the attitude start-transient exception to attitude error and preserve the lack of an Apollo 13-specific numeric duration; note 111 records the generic LM inverter convention; note 112 corrects the first-playable inverter selection from mission-specific Apollo 13 procedure evidence; note 113 closes the alternate-inverter identity; note 114 directly resolves the inverter-2-to-inverter-1 cockpit transfer sequence from the Apollo 13 LM Malfunction Procedures; and note **115 closes the first-playable post-transfer timing ambiguity by requiring a fresh valid caution re-observation rather than an invented crew persistence timer**.

Current detailed integration roadmap: `docs/roadmap/2026-09-12_first_playable_integration.md`. Dated archival refinements are recorded under `docs/roadmap/`, including `2026-09-13_pc2_inverter_transfer_procedure.md` and `2026-09-13_pc2_inverter_reobservation_timing.md`.

### Player-count boundary

Full configuration: seven station players — FLIGHT, CAPCOM, CONTROL, TELMU, GUIDO, FIDO/RETRO, and INCO.

Minimum supported compact PC+2 configuration: five players — FLIGHT; CAPCOM; LM SYSTEMS = TELMU + CONTROL; FLIGHT DYNAMICS = GUIDO + FIDO/RETRO; INCO.

The spacecraft crew is not an additional first-playable player. Decision D-021 keeps crew receipt/action explicit in the scenario model while retaining CAPCOM as the player-facing communication boundary.

## Phase 3 — Display and console reconstruction

**Status:** minimum PC+2 player-presentation checkpoint complete.

First-pass views exist for CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, FLIGHT, and CAPCOM. Exact semantics are retained where sourced; project renderings remain labeled where exact routing/layout is unresolved; hidden integrity does not leak, and missing fields are not turned into invented telemetry failures.

## Phase 4 — Authoritative simulation model

**Status:** first-playable authoritative model, compact transport/client integration, staged final-load workflow, spacecraft-model boundary, ground-data-processing boundary, observation-failure boundary, and crew-action boundary established; physical multi-device execution remains.

Implemented architecture includes station-specific projections, explicit injection/action/communication/decision/physical/evidence layers, `PC2Session`, continuous mission time, readiness/FLIGHT decisions, CAPCOM queue/transmission, audit logging, facilitator authority, browser rejoin, compact station-set ownership, and staged final PC+2 solution/uplink state.

Decision D-016 remains canonical: GET advances whenever RUNNING; controller decisions do not stop GET; only explicit session pause stops time; ineligible nominal events are missed rather than replayed later.

Decision D-019 bounds spacecraft physics to sourced decision dependencies: DPS/maneuver state, guidance/attitude/control state, coarse electrical/equipment availability, communications/uplink/ranging availability, and instrumentation observation integrity. Full-spacecraft emulation is not a first-playable requirement.

Research note 103 applies the same admission rule to MCC ground systems. Decision D-020 and note 104 keep source/sensor, conditioning/PCM, communications/telemetry transport, ground processing, and station product separate. Decision D-021 and note 105 keep CAPCOM transmission, crew receipt/action, physical response, telemetry, and crew report separate.

The synthetic ΔP branch remains explicitly non-historical and source-bounded:

`source observation → CONTROL product/rule → CONTROL decision → CAPCOM queue/transmission → crew receipt → crew shutdown command → physical DPS response → crew report / fresh GQ6510P evidence → CONTROL evidence assessment`

No unsupported internal routing, automatic crew compliance, response timing, telemetry synthesis, binary chamber-pressure threshold, hidden engine-off truth, or invented sensor failure is added.

## Phase 5 — Mission Control data path

**Status:** first-slice architecture, ground-processing scope, observation-integrity scope, and crew-interaction boundary established.

The project preserves:

`spacecraft/source state → instrumentation/telemetry → communications/ground processing → controller products → controller interpretation → player presentation → controller decisions/communications`

Station projections enforce information boundaries; validity, age, hidden integrity, crew reports, telemetry, physical state, and controller conclusions remain distinct.

The final PC+2 load path remains:

`FIDO/RTCC final solution → GUIDO load readiness/consistency → INCO uplink configuration → CAPCOM/crew P00 + DATA/ACCEPT + UPDATA LINK configuration → state-vector + target-load transmission → completion / computer returned to crew`

Exact Cartesian vector values, RTCC/CCATS command internals, exact controller key sequence, and exact transmission duration remain unfrozen. SSR-derived analysis is not silently invented inside this path.

## Phase 6 — Procedures and flight rules

**Status:** PC+2 core rule set operational; immediate post-burn boundary source-defined.

Implemented/evaluable: ISS warning + program alarm path, chamber-pressure observation, >25 psi ΔP ground callout, attitude criteria, inverter warning/action path, restart eligibility/sequence, crew STOP/off path, shutdown/restart evidence architecture, final state-vector/target-load staging, and final FLIGHT GO/NO-GO.

### Immediate post-burn

Research note 101 defines:

`burn cutoff/result → post-burn assessment → release from burn configuration → partial LM power-down → PTC preparation`

Primary Apollo 13 records place nominal PC+2 ignition at 79:27:38.30 GET, record small PGNS residuals, place an initial LM power-down transition at about 79:33–79:34 while retaining PTC-required functions, and place the detailed PTC procedure at about 79:52. A separate change-of-shift briefing describes power-down timing of roughly cutoff +15 minutes; that tension remains documented rather than silently reconciled.

### 150-psi ground inlet criterion

Research note 106 identifies fuel inlet / `GQ3611P` as the leading lineage-supported interpretation from Apollo 10/11 rule lineage and LM-7 documentation. No reviewed Apollo 13-specific source explicitly makes the mapping, so the rule remains `NOT_EVALUABLE`; no minimum/average/either-side or synthetic combined pressure product is authorized.

### 77-percent onboard thrust criterion

Notes 107–108 identify the panel-1 CMD THRUST / ENG THRUST instrument family, with ENG THRUST the actual-thrust percent scale. The Apollo 13 crew debrief fixes the commanded PC+2 profile as 5 seconds at low/idle thrust, 21 seconds at 40 percent, then full throttle. For first playable, the 77-percent criterion becomes applicable on entry into the commanded maximum/full-throttle segment at burn +26 seconds. This remains a source-bounded lineage inference, not a verbatim recovered qualifier, and does not authorize deriving the crew gauge directly from hidden engine state.

### Attitude start transient

Note 109 gives operational precedence to the contemporaneous CAPCOM transmission and Haise readback, which attach the startup exception to ±10-degree attitude error, not the separate ±10-degree/sec rate criterion. Note 110 establishes only that DPS engineering usage treated “start transient” as a short engine-start phenomenon; no Apollo 13-specific numeric duration/end condition is recovered. No 2.14-second, 4-second, +5-second, +21-second, or +26-second historical exception timer is encoded.

### Inverter criterion — corrected configuration, transfer, and re-observation timing

Research notes 112–115 supersede note 111's earlier first-playable identity synthesis. Apollo 13's mission-specific PC+2 read-up explicitly directed `CB(16) INVERTER 2, CLOSE` and scratched the stock `Select Inverter 1` step, fixing the burn configuration on inverter 2. The Apollo 13 *LM Malfunction Procedures* then directly supplies the alternate-selection action for inverter 2 operating and immediately evaluates whether the INVERTER caution is off; it does not prescribe a crew stopwatch interval. NASA LM instrumentation documentation separately describes LM-5-and-subsequent inverter-selection transient-inhibit behavior, placing normal switching-transient suppression in spacecraft indication logic rather than in an additional crew dwell rule.

Canonical first-playable interpretation:

`PC+2 selected inverter 2 → inverter warning/light → close CB(11) EPS: INV 1 → select INVERTER 1 → open CB(16) EPS: INV 2 → indication transient/invalid state as required by caution logic → fresh valid INVERTER warning re-observation → warning remains → shutdown criterion satisfied`

Do not invent a 1-second, 2-second, 5-second, or other post-transfer persistence timer. The exact inverter-selection inhibit duration, exact ground display latency, crew-member assignment, controller voice wording, independent ground knowledge of selector position, automatic engine cutoff, and exact TELMU/CONTROL display field remain unresolved.

Still intentionally unresolved where evidence is insufficient: Apollo 13-specific confirmation of the 150-psi fuel-inlet mapping; exact operational duration/end condition of the attitude-error start transient; exact inverter-selection inhibit duration and exact ground display/routing latency/details; exact final-load ground-system internals; and display/routing details whose absence does not currently block first playable.

## Phase 7 — Simulation scenarios / SimSup

**Status:** repository-side first-playable preparation complete; physical validation remains.

Live-play protocol, structured evidence/debrief capture, scenario-blind player preparation/reference packet, facilitator separation, compact-mode integration, staged final-load workflow, backroom scope rule, source-bounded post-burn closure, decision-relevant spacecraft-model scope, functional ground-data-processing scope, layered observation-failure scope, and explicit scenario-authored crew-action scope are documented.

Modern HTTP/browser/localStorage/token/report/preparation/reference-packet/facilitator mechanics are project infrastructure, not Apollo reconstruction.

## Immediate next work

The primary remaining validation boundary is **physical human/device execution**.

1. Prepare participants with `docs/testing/PC2_PLAYER_PREPARATION.md` and `PC2_PLAYER_REFERENCE_PACKET.md`; preserve scenario blindness.
2. Execute `PC2_LIVE_PLAYTEST_PROTOCOL.md` with separate real-phone/browser clients and one facilitator console: nominal PC+2 first, synthetic ΔP second.
3. Continue the nominal run past cutoff through the note-101 post-burn assessment/power-down/PTC-preparation transition; do not improvise extra faults or unsupported crew delays/errors.
4. Record incidents with `PC2_LIVE_PLAYTEST_REPORT_TEMPLATE.md`, retaining preparation/GET/station/device/build/audit provenance.
5. Validate packet findability and clarity separately from historical correctness.
6. Exercise the approved five-player compact configuration with simultaneous clients, especially TELMU↔CONTROL and GUIDO↔FIDO-RETRO switching.
7. Verify station-qualified readiness/action attribution, CAPCOM→crew sequencing, and information isolation in facilitator audit output.
8. Repair reproducible network/mobile/presentation/instruction defects and add regression coverage.
9. Reopen historical or model research only when validation exposes a concrete missing decision dependency.

Research notes 106–115 are bounded archival refinements and corrections; they do not displace the physical-play priority.

## Explicitly deferred

- exact console pixel/character reconstruction;
- Apollo 13-specific proof of the 150-psi ground fuel-inlet mapping;
- a verbatim Apollo 13 qualifier for the 77-percent ENG THRUST applicability gate;
- exact operational duration/end of the attitude-error startup-transient exception;
- exact inverter-selection transient-inhibit duration and ground display latency;
- exact TELMU/CONTROL inverter-warning routing/display field and independent switch-position visibility;
- detailed DPS transient timing beyond selected branch needs;
- full six-degree-of-freedom spacecraft/orbital propagation;
- pulse-level RCS jet dynamics;
- full LM ECS and dormant CSM subsystem physics for this slice;
- detailed battery chemistry, wiring, breaker, and RF propagation/modulation physics;
- complete LM instrumentation-channel emulation;
- random/generic sensor or telemetry faults or unsupported failure distributions;
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

Research notes 095–115 and associated testing/scope documentation improve physical-run evidence quality and bounded historical interpretation but do not constitute physical validation. Physical seven-seat and five-player compact human/device PASS claims remain unmade.
