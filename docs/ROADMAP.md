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

**Status:** minimum PC+2 player-presentation checkpoint complete; player-interaction/playability design is now active, while final historical/player-facing reconstruction and physical validation remain pending.

First-pass views exist for CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, FLIGHT, and CAPCOM. Exact semantics are retained where sourced; project renderings remain labeled where exact routing/layout is unresolved; **hidden integrity does not leak**, and missing fields are not turned into invented telemetry failures.

For TELMU inverter monitoring, source-backed `GC0071V` / `GC0155F` evidence may be rendered as a project product. H-2 has two identified mission-specific configuration authorities: PHO-TR155 Revision C for the Display System and TDFCB Revision 4 for telemetry-format/Flight Control products. Their cross-check is documented. PHO-TR155 also used multiple supporting data-pack products; the surviving generic reference to H-2 data-pack Revision N does not establish which sub-pack contained TELMU loading. Exact Apollo 13 indicator/module placement, CRT request, selector workflow, sample/display cadence, precision, and latency remain unresolved.

## Phase 4 — Authoritative simulation model

**Status:** first-playable authoritative model, compact transport/client integration, staged final-load workflow, spacecraft-model boundary, ground-data-processing boundary, facilitator-driven live nominal/contingency integration, propulsion/translational/tracking/guidance/radar model proofs, deterministic simulated crew actor, coarse generic electrical-power model, and finite resource inventory/depletion model implemented; multi-human execution and historical scenario validation remain.

Implemented architecture includes station-specific projections, explicit injection/action/communication/decision/physical/evidence layers, `PC2Session`, continuous mission time, readiness/FLIGHT decisions, CAPCOM queue/transmission, audit logging, facilitator authority, browser rejoin, compact station-set ownership, staged final PC+2 solution/uplink state, and a mission-neutral malfunction-plan scheduler that expands exercise-level failures into inspectable causal insertions.

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

The deployed nominal and ΔP paths are validated. Final player-interface reconstruction and multi-human playtesting are still pending, but **player-interaction/playability design is now an active parallel workstream** under research note 314. This permits interface auditing, prototype structure, and playability instrumentation without freezing unsupported historical display behavior.

D-024 is now applied to the active research portfolio in `docs/RESEARCH_PORTFOLIO_STATUS.md`. Reusable simulator/causal-engine architecture research is **SUFFICIENT** for current implementation; exact LMS internals are dependency-triggered rather than a standing research queue. PC+2 historical numerical-model readiness is **BLOCKED** on the named artifacts in research 214, while the Apollo 11 powered-descent reference remains **OPEN** because it has explicit current model/runtime dependencies.\n\nThe Apollo 11 landing-radar/controller-call subquestion is now **SUFFICIENT** (research 502), and a reusable controller decision-gate contract plus partial Mission-G profile is implemented. The contract preserves MSK-1137/CONTROL cues, the historical landing poll, FLIGHT decision authority, and CAPCOM relay without producing an automatic GO/NO-GO. The next Apollo 11 dependency is source-controlled binding of existing LR/guidance outputs into those cue IDs; exact Mission-G LR parameter routing remains **BLOCKED** and must not be invented.

1. Preserve the facilitator/test interface as the primary validation surface. The Causal Model Lab now also exposes the historical measurement-profile boundary: source-backed Apollo 13 LM-7 inverter measurements can execute at the vehicle layer while the unresolved H-2 ground-product gate remains explicitly blocked. The deployed Causal Model Lab now exposes DPS, trajectory/tracking, resource→power→observation, guidance comparison/consensus, landing-radar qualification/update gating, and guidance-computer alarm/restart proofs; new reusable causal domains should add their site-facing proof in the same workstream.
2. Continue integrating the deterministic simulated-crew actor. The nominal FLIGHT→CAPCOM `continue_pc2_burn_sequence` handoff is now a supported crew-receipt/acknowledgement path, and CAPCOM presentation keeps **approved/pending → transmitted/awaiting receipt → crew received** distinct. CAPCOM transmission still does not perform a crew action or spacecraft response. The PC+2 ΔP shutdown, inverter-transfer contingency, and premature-stop restart branch retain separate receipt/action/physical-response stages. Next integrate additional crew progression only where the scenario supplies a bounded rule; do not invent response latency.
3. Treat the reusable Apollo-simulator architecture question as **SUFFICIENT for current implementation** under D-024. Research 215–217 already constrain the layer boundaries needed now: dynamics/physical state, subsystem state, measurement/observation state, ground/interface products, and separate exercise control/failure insertion. Do **not** continue broad LMS/AMS searching merely to make this bibliography more complete.
4. Keep exact LMS retrieval scoped by the dependency. Generic handbook extraction remains **DEFERRED**, but a specifically reconstructed historical LMS malfunction/SimSup case or affirmative LMS-injectability claim is **BLOCKED** on Volume II Section 2 **Malfunction Data** and/or Section 6 **Scripting Data Sheets** in the Virginia Tech Avitabile collection. Treat Section 2/6 retrieval/digitization as critical-path work when that capability is selected; it does not block current PC+2/playability or the generic causal-engine architecture. Section 7 **Simulator Output Tables**, NASA RG 255 E.155B1 acceptance material, and the large public Volume I/User's Manual scans remain dependency-triggered unless a separate bounded question makes them material.
5. Treat PC+2 historical numerical-model readiness as **BLOCKED**, not as an endlessly active search. Research 214 found no valid same-input sourced interval for D-022 among mass, propulsion, trim, trajectory, tracking, or acceptance-tolerance gates. Do not schedule sensitivity work until a named source condition changes: Apollo 13 DPS Supplement 2, LM-7 performance/calibration or PC+2 high-speed propulsion data, H-2 mass-property/depletion records, the final PC+2 GDA/P30 artifact, or source-backed historical product/tolerance data. When one supplies a genuine range, reopen the bounded gate and run D-022 against controller-visible products.
6. Continue consequence testing beyond the first PC+2 matrix. The inverter contingency now also has isolated correct, omitted, wrong-order, and warning-clears causal probes through authoritative session + simulated crew + fresh-observation rule logic. The Causal Model Lab now runs isolated correct, late, omitted, and wrong-actor FLIGHT-GO cases through authoritative session logic: timely GO preserves the chain; late GO does not replay the missed P40 milestone; omitted GO misses dependent burn milestones while GET advances; wrong-actor GO is rejected without pausing GET. “Late” here is D-016 event-order semantics, not a historical delay tolerance. Extend the same pattern to additional supported subsystem actions only where their causal consequences are defined.
7. Generic electrical-power/equipment availability and finite resource inventory/depletion models are implemented, and a synthetic resource→power→tracking-observation chain now proves cross-model consequence propagation without scenario outcome branches. Next add only source-backed historical couplings where selected scenarios require them.
8. Cross-check simulator-era abstractions against Apollo 13 LM-7/CSM configuration sources before importing constants or mission-specific behavior.
9. Continue the player-interaction/playability workstream from research note 314. Playability instrumentation now records page/join/rejoin/workspace/action/station-switch events with client elapsed time in a stream separate from the authoritative mission audit, and the facilitator can copy that log for analysis. Use it during the neutral FLIGHT/CAPCOM part-task checkout under continuous GET, then prototype CONTROL/GUIDO phone product scanning using stable single-product layouts and general controller actions rather than branch-specific solution controls. Add packet/reference findability observations to the same checkout record. Keep final historical station reconstruction and seven-seat/five-player PASS claims deferred until the causal engine/simulated-crew loop and relevant product boundaries are sufficiently mature.
10. Continue the Apollo 11 powered-descent/program-alarm interval as the second architecture pressure test. The guidance alarm/restart domain, landing-radar update-eligibility gate, generic pairwise guidance cross-check machinery, generic multi-source consensus/quorum machinery, and non-executable scenario/model-profile metadata are implemented. Research note 204 defines source-backed Apollo 11 guidance-monitoring source pairs and velocity-residual limits; note 210 adds the PGNCS/AGS/MSFN two-out-of-three topology; note 218 recovers Mission G MSFN/PFP source-production timing while leaving inter-source freshness unresolved. The landing-radar estimator is now executable/composed from LM-5 position geometry and measurement-time attitude inputs through PIPA/gravity propagation, lunar-surface correction, beam projection, residual qualification, and historical weighting/update. The Causal Model Lab also replays the two Mission Report DATA NOT GOOD/GOOD intervals deterministically and applies the separate four-second onboard DATA GOOD requalification rule; these are event anchors, not a stochastic dropout model. Historical stochastic LR generation remains BLOCKED. The next implementation/research pressure point is the controller-product boundary: preserve the mission-specific MSK-1137 field family and mixed `D/L`/RTCC provenance without aliasing hidden state, and recover Apollo-11-effective per-field routing/external-name or computation identifiers where available. Keep onboard estimator timing, ground processing, D/TV buffering, CRT refresh, operator requests, and station-visible cadence distinct. Then complete powered-descent trajectory/propulsion, controller-product interfaces, and sourced decision rules before an Apollo 11 runtime is allowed.
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