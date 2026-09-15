# Roadmap

This roadmap separates historical reconstruction from software simplification. Dated research/progress records preserve implementation history; this file records the current canonical state.

## Phase 0 — Foundation and provenance

**Status:** substantially complete.

Repository baseline, research-first authenticity policy, source catalog/research-note structure, simulation architecture, decision log, and source-mirroring infrastructure are established. Standardized implementation citation format remains demand-driven.

## Phase 1 — Reconstruct Apollo Mission Control

**Status:** research-sufficient to proceed; not historically exhaustive.

Core Apollo 13 front-room positions are at B or better, with EECOM at A. Exact console/display reconstruction remains incomplete for several stations but is not a prerequisite where missing detail does not affect the selected scenario. Research note 100 makes the Staff Support Room boundary explicit: the seven-seat/five-player implementation is a front-room playable slice, not a complete staffing reconstruction.

Mission H-2 display/telemetry provenance has now been tightened through research notes **123–126**. PHO-TR155 Revision C was issued before flight, the H-2 Display System was implemented in accordance with it during March 1970, and Philco explicitly reported that no equipment configuration changes were required. Separately, Mission H-2 **TDFCB Revision 4** was delivered on 28 January 1970 with mission-specific LM Flight Control, PCMGS, high-speed/wideband, index, and compare products; Philco records checking the H-2 Rev. 4 PCMGS against PHO-TR155. Earlier PHO-TR155 work also used multiple named H-2 data-pack products plus a preliminary IBM card deck/listing, so the later **data-pack Revision N** reference must not be treated as a TELMU-specific loading artifact without the package or an authoritative pack key. Exact Apollo 13 TELMU loading remains unrecovered, so project renderings must not be represented as exact H-2 physical-console or parameter-loading reconstructions.

## Phase 2 — First playable mission/scenario

**Status:** implemented and facilitator-driven live integration validated; multi-human/device play remains.

Selected slice: **Apollo 13 PC+2 preparation/execution**, beginning near **77:55 GET** and continuing through immediate post-burn verification/power-down.

The primary research chain now runs through notes **048–126**. Notes 098–103 establish the final-load, support-room, post-burn, spacecraft-model, and ground-data-processing boundaries. Notes 104–126 further constrain the PC+2 observation and shutdown-rule evidence paths, including inlet-pressure and thrust-monitor semantics, attitude-transient handling, inverter transfer/re-observation, ground inverter telemetry, TELMU station continuity, crew-local electrical monitoring, H-2 PHO-TR155 provenance/implementation, mission-specific H-2 TDFCB telemetry configuration, and the PHO-TR155 data-pack lineage boundary.

The deployed browser runtime has now completed a facilitator-driven nominal PC+2 pass through the immediate post-burn/PTC-preparation sequence and a separate synthetic ΔP contingency pass through CONTROL corroborated shutdown evidence. See `docs/progress/2026-09-14_live_nominal_and_delta_p_validation.md`.

Current detailed integration roadmap: `docs/roadmap/2026-09-12_first_playable_integration.md`.

### Player-count boundary

Full configuration: seven station players — FLIGHT, CAPCOM, CONTROL, TELMU, GUIDO, FIDO/RETRO, INCO.

Minimum supported compact PC+2 configuration: five players — FLIGHT; CAPCOM; LM SYSTEMS = TELMU + CONTROL; FLIGHT DYNAMICS = GUIDO + FIDO/RETRO; INCO.

This is a project adaptation, not a historical staffing claim. Decision **D-018** and research notes **091–094** require compact play to map one player to a set of original station identities rather than create synthetic historical stations. Original station products, actions, readiness, authorization, and audit identities remain distinct.

## Phase 3 — Display and console reconstruction

**Status:** minimum PC+2 player-presentation checkpoint complete; player-facing usability/presentation refinement remains.

First-pass views exist for CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, FLIGHT, and CAPCOM. Exact semantics are retained where sourced; project renderings remain labeled where exact routing/layout is unresolved; **hidden integrity does not leak**, and missing fields are not turned into invented telemetry failures.

For TELMU inverter monitoring, source-backed `GC0071V` / `GC0155F` evidence may be rendered as a project product. H-2 has two identified mission-specific configuration authorities: PHO-TR155 Revision C for the Display System and TDFCB Revision 4 for telemetry-format/Flight Control products. Their cross-check is documented. PHO-TR155 also used multiple supporting data-pack products; the surviving generic reference to H-2 data-pack Revision N does not establish which sub-pack contained TELMU loading. Exact Apollo 13 indicator/module placement, CRT request, selector workflow, sample/display cadence, precision, and latency remain unresolved.

## Phase 4 — Authoritative simulation model

**Status:** first-playable authoritative model, compact transport/client integration, staged final-load workflow, spacecraft-model boundary, ground-data-processing boundary, facilitator-driven live nominal/contingency integration, propulsion/translational/tracking/guidance/radar model proofs, deterministic simulated crew actor, coarse generic electrical-power model, and finite resource inventory/depletion model implemented; multi-human execution and historical scenario validation remain.

Implemented architecture includes station-specific projections, explicit injection/action/communication/decision/physical/evidence layers, `PC2Session`, continuous mission time, readiness/FLIGHT decisions, CAPCOM queue/transmission, audit logging, facilitator authority, browser rejoin, compact station-set ownership, and staged final PC+2 solution/uplink state.

Decision **D-016** remains canonical: GET advances whenever RUNNING; controller decisions do not stop GET; only explicit session pause stops time; ineligible nominal events are missed rather than replayed later.

Decision **D-019** bounds spacecraft physics to sourced decision dependencies. Decision **D-021** additionally requires reusable model boundaries rather than treating PC+2 as the simulator's scope. Required causal domains are DPS/maneuver state, guidance/attitude/control state, coarse electrical/equipment availability, communications/uplink/ranging availability, and instrumentation observation integrity. Full-spacecraft emulation is not a first-playable requirement. The current generic translational proof supports point-mass position/velocity propagation with optional caller-supplied central gravity, but does not yet claim an Apollo historical frame, orbit solution, or RTCC-equivalent propagator.

Research note **103** applies the same admission rule to MCC ground systems: MSFN/CCATS/RTCC are represented through decision-relevant availability, quality, routing, and generated-product states. IBM/UNIVAC internals, exact support-console keying, internal message formats, full network routing/geometry, and unsupported delays/failure rates are not first-playable requirements.

The synthetic ΔP branch remains explicitly non-historical and source-bounded:

`source observation → CONTROL product/rule → CONTROL decision → CAPCOM queue/transmission → crew receipt → crew shutdown command → physical DPS response → crew report / fresh GQ6510P observation → CONTROL evidence assessment`

The 26 psi exercise is explicitly non-historical. No unsupported internal routing, **automatic crew compliance**, response timing, telemetry synthesis, **binary chamber-pressure threshold**, or **hidden engine-off truth** is added. This chain has now passed live deployed facilitator-driven validation through `state = corroborated`.

Compact-role implementation preserves original station identities end to end:

`player → exact original station set → HTTP join/rejoin → bundled station-scoped snapshots → browser substation navigation → station-qualified readiness/actions/audit provenance`


A distinct model-profile catalog now separates historical mission metadata from numerical-model readiness. Scenarios now also declare `required_model_domains`, allowing numerical historical readiness to be evaluated per scenario rather than globally. Scenarios reference a `model_profile_id`; the initial Apollo 13 profile marks mass properties and propulsion as partial and translational/tracking historical configuration as unresolved. No unresolved constants are promoted merely to satisfy configuration.

## Phase 5 — Mission Control data path

**Status:** first-slice architecture and ground-processing scope established; core ΔP information path live-validated; generic trajectory-to-tracking observation boundary implemented.

A mission-neutral tracking proof now derives geometric range/range-rate from authoritative translational state, then separately applies caller-supplied delay, bias, availability, and validity. This is validation infrastructure for the truth/observation boundary, not an MSFN or RTCC reconstruction.

The project preserves:

`spacecraft/source state → instrumentation/telemetry → communications/ground processing → controller products → controller interpretation → player presentation → controller decisions/communications`

Station projections enforce information boundaries; source injections alter observations rather than announce diagnoses; **validity, age, hidden integrity, crew reports, telemetry, physical state, and controller conclusions remain distinct**.

Research note 102 reinforces that this chain is the physical-model admission test. Research note 103 now defines the ground-processing portion explicitly:

`MSFN source/path → CCATS reception/routing/processing → RTCC processing/product generation → station-visible product/status`

Only states that materially affect a sourced player decision or selected failure path enter the executable model. Tracking/ranging quality remains distinct from generated trajectory products, and ground systems must not leak hidden spacecraft truth.

Research notes **125–126** add a historical configuration-control boundary above this functional model. Mission H-2 TDFCB Revision 4 carried mission-specific telemetry-format/Flight Control products and its PCMGS material was checked against PHO-TR155. PHO-TR155 itself used a family of configuration data-pack products; because the contents/scope of Revision N are unrecovered, it cannot substitute for an exact TELMU loading source. Neither archival gap may be filled with guessed H-2 parameter loading or adjacent-mission sample rates.

The final PC+2 load path remains:

`FIDO/RTCC final solution → GUIDO load readiness/consistency → INCO uplink configuration → CAPCOM/crew P00 + DATA/ACCEPT + UPDATA LINK configuration → state-vector + target-load transmission → completion / computer returned to crew`

Exact Cartesian vector values, RTCC/CCATS command internals, exact controller key sequence, and exact transmission duration remain unfrozen. SSR-derived analysis is not silently invented inside this path.

## Phase 6 — Procedures and flight rules

**Status:** PC+2 core rule set operational; immediate post-burn boundary source-defined; inverter observation path substantially constrained; ΔP shutdown procedure live-validated.

Implemented/evaluable: ISS warning + program alarm path, chamber-pressure observation, >25 psi ΔP ground callout, attitude criteria, inverter path, restart eligibility/sequence, crew STOP/off path, shutdown/restart evidence architecture, final state-vector/target-load staging, and final FLIGHT GO/NO-GO.

Research notes **104–126** now constrain several previously loose rule/observation details. In particular, Apollo 13 retained inverter 2 for the burn, the alternate-inverter transfer procedure is source-backed, the post-transfer warning must be treated as a fresh observation rather than an invented timed dwell, `GC0071V` / `GC0155F` provide a ground electrical evidence path, and crew Power/Temp Monitor/caution observation remains a distinct local path. Direct ground telemetry of the caution state or inverter selector position has not been established. Mission-specific TDFCB provenance identifies the correct archival route for exact H-2 telemetry loading, while note 126 prevents the unrecovered PHO-TR155 Revision N data pack from being misrepresented as a known TELMU-specific source.

Research note **101** adds the first-playable post-burn sequence:

`burn cutoff/result → post-burn assessment → release from burn configuration → partial LM power-down → PTC preparation`

Primary Apollo 13 records place nominal PC+2 ignition at 79:27:38.30 GET, record PGNS residuals R1 +00010 / R2 +00003 / R3 +00000, place an initial LM power-down transition at about 79+33–79+34 while retaining PTC-required functions, and place the detailed PTC procedure at about 79+52. A separate change-of-shift briefing describes a power-down timing of roughly cutoff +15 minutes; research note 101 preserves that as an unresolved timing-source tension rather than silently reconciling it. The project does not infer exact console keying, an unsupported formal post-burn poll, exact switch-by-switch timing, or full PTC dynamics.

Still intentionally unresolved where evidence is insufficient: exact onboard 77-percent thrust indication semantics, singular 150-psi inlet-pressure selection/aggregation, exact startup transient duration, exact H-2 TELMU display/loading and live update cadence, and exact final-load ground-system internals.

## Phase 7 — Simulation scenarios / SimSup

**Status:** first reference scenario integrated; generic scenario catalog/selection, mission-profile catalog, shared runtime-adapter boundary, and a synthetic generic runtime adapter implemented; historically grounded additional scenario adapters remain.

Live-play protocol, structured evidence/debrief capture, scenario-blind player preparation/reference packet, facilitator separation, compact-mode integration, staged final-load workflow, backroom scope rule, source-bounded post-burn closure, decision-relevant spacecraft-model scope, and functional ground-data-processing scope are documented for the first reference scenario.

Per D-021, Apollo 13 PC+2 is a validation anchor rather than the simulator's terminal scope. A generic scenario catalog now discovers fixture metadata and session creation accepts an explicit scenario ID while preserving the existing PC+2 default. Scenarios explicitly reference a mission-era configuration profile; the first partial profiles are Apollo 13 H-2 and Apollo 11 Mission G. Runtime construction now goes through an adapter registry and a shared session contract; PC+2-only procedures are exposed as explicit adapter capabilities instead of generic methods. The catalog distinguishes **available metadata** from **executable runtime support**. `pc2_v1` remains the historical reference runtime; `generic_v1` now provides a PC+2-independent validation runtime for lifecycle, stations, readiness, FLIGHT/CAPCOM workflow, timed external events, projections, audit history, and controlled injections. It is not itself a historical Apollo scenario or a replacement for causal subsystem models. Mission-profile metadata is not yet allowed to rewrite station behavior automatically. Phase 7 still requires additional historically grounded scenario fixtures/runtime adapters without baking PC+2-specific assumptions into reusable engine layers.

Modern HTTP/browser/localStorage/token/report/preparation/reference-packet mechanics are project infrastructure, not Apollo reconstruction.

## Immediate next work

The deployed nominal and ΔP paths are validated, but the project is **not yet at player-interface or multi-human playtest stage**. The immediate historical-integration task is now a D-022 gate-closure test: select one unresolved PC+2 numerical input with a fully sourced plausible range, propagate both endpoints through the causal model, and compare the actual controller-visible products at their documented resolution. Only if the full range is player-invisible may that gate close without exact recovery.

1. Complete the remaining test-console cleanup and preserve the facilitator/test interface as the primary validation surface.
2. Continue integrating the now-implemented deterministic simulated-crew actor. The generic actor separates CAPCOM transmission, receipt/acknowledgement, supported crew action, and physical subsystem response without inventing response latency. The PC+2 shutdown path now uses this actor while retaining its existing operational-action and physical-response separation. Next migrate additional source-bounded crew actions/reports as their mappings are established.
3. Continue targeted research into Apollo LMS/AMS mathematical-model, subsystem-model, malfunction-insertion, instructor, output-dictionary, and validation/correlation documentation.
4. Extract the original simulator's useful abstraction boundaries: state variables, equations, subsystem coupling, integration/update assumptions, failure insertion points, and separation of physical truth from indications/telemetry.
5. Apply D-022 to the first suitable PC+2 numerical integration gate before freezing another historical input. Establish a fully sourced plausible range, run both endpoints through propulsion/trajectory and station-product generation, and record product-resolution deltas in a research note. A negative sensitivity result closes the gate as not decision-relevant; a positive result keeps it open and prioritizes further archival recovery.
6. Add consequence tests for correct, late, omitted, and wrong actions. Scenario files should define initial conditions, plans, and failures; they should not enumerate every possible outcome.
7. Generic electrical-power/equipment availability and finite resource inventory/depletion models are implemented, and a synthetic resource→power→tracking-observation chain now proves cross-model consequence propagation without scenario outcome branches. Next add only source-backed historical couplings where selected scenarios require them.
8. Cross-check simulator-era abstractions against Apollo 13 LM-7/CSM configuration sources before importing constants or mission-specific behavior.
9. Keep player-facing station UI reconstruction, multi-human seven-seat/five-player playtesting, and packet-usability work deferred until the causal engine and simulated-crew loop are sufficiently mature.
10. Continue the Apollo 11 powered-descent/program-alarm interval as the second architecture pressure test. The guidance alarm/restart domain, landing-radar update-eligibility gate, generic independent-guidance cross-check machinery, and non-executable scenario/model-profile metadata are implemented. Research note 204 now defines source-backed Apollo 11 guidance-monitoring source pairs and several velocity-residual limits in a dedicated historical profile, while deliberately blocking executable comparison because freshness/update cadence remains unresolved. Next recover the guidance-comparison timing boundary. The landing-radar path now includes a generic upstream measurement-qualification model plus Apollo 11 source-profile values for Data Good persistence, range-scale stability, update-state boundaries, and residual tests; remaining radar work is LM-5 measurement geometry/reference computation and the downstream estimator/filter. Then complete powered-descent trajectory/propulsion, controller-product interfaces, and sourced decision rules before an Apollo 11 runtime is allowed.
11. Continue mission-specific archival work only where it materially constrains the causal engine, supported actions/failures, or controller-visible consequences.

## Explicitly deferred

- exact console pixel/character reconstruction;
- singular 150-psi inlet-pressure aggregation without direct evidence;
- exact onboard 77-percent thrust indication semantics without direct evidence;
- detailed DPS transient timing beyond selected branch needs;
- exact H-2 TELMU module/indicator/CRT loading, request/key workflow, and display cadence without mission-specific evidence;
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

## Causal composition validation

A synthetic integration test and facilitator validation endpoint now verify a multi-model chain in which finite resource depletion changes electrical source availability, which changes equipment supply, which changes tracking-observation availability. The composed API rejects direct source-availability override. This is architecture validation only; no Apollo resource/power/tracking constants are asserted.

## Validation status

Automated coverage includes continuous-clock/event rules, crew response, shutdown evidence, player/admin separation, facilitator authority, multi-client integration, multi-station ownership, compact HTTP/browser contracts, and staged PC+2 final-load transitions/station products.

Facilitator-driven validation against the deployed browser application has now passed both the complete nominal PC+2 sequence through post-burn/PTC preparation and the synthetic ΔP branch through corroborated CONTROL evidence without hidden engine truth. See `docs/progress/2026-09-14_live_nominal_and_delta_p_validation.md`.

Physical seven-seat and five-player compact **multi-human** PASS claims remain unmade.