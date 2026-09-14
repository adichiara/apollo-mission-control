# Roadmap addendum — first playable PC+2 integration

Date: 2026-09-12  
Status: **CURRENT — facilitator-driven deployed nominal and ΔP integration validated; multi-human/device execution remains**

## Completed checkpoints

- [x] minimum player presentations for CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, FLIGHT, CAPCOM;
- [x] one authoritative mission state and synchronized GET;
- [x] readiness reports, FLIGHT decision requirement, CAPCOM queue/transmission, and audit trail;
- [x] FastAPI/Uvicorn phone-accessible transport and rejoin-safe browser identity persistence;
- [x] continuous mission clock, declarative nominal-event eligibility, and 1× monotonic pacing;
- [x] end-to-end source-bounded ΔP branch through fresh CONTROL evidence;
- [x] ordinary player client separated from facilitator/validation client;
- [x] facilitator authority protected independently from controller station identity;
- [x] in-process multi-client contract test and real-network smoke runner;
- [x] structured real-device/human-play protocol;
- [x] five-player compact role research and multi-original-station ownership;
- [x] compact HTTP/browser join/rejoin, bundled station views, original-station attribution, and substation navigation;
- [x] four-player boundary reviewed with no sub-five-player PC+2 mode approved;
- [x] structured live-play evidence/debrief package;
- [x] reproducible scenario-blind player-preparation package and first-run reference packet;
- [x] primary-source review and staged implementation of the final PC+2 state-vector/target-load/uplink workflow;
- [x] primary-source review of Apollo 13 Staff Support Room/backroom functions and explicit first-playable support-room scope boundary;
- [x] primary-source review of immediate post-burn verification/power-down and explicit first-playable post-burn closure sequence;
- [x] primary-source review of LM subsystem dependencies and explicit decision-relevant spacecraft-physics boundary;
- [x] primary-source review of MSFN/CCATS/RTCC support functions and explicit decision-relevant ground-data-processing boundary;
- [x] facilitator-driven deployed nominal PC+2 validation through post-burn/PTC preparation;
- [x] facilitator-driven deployed synthetic ΔP validation through corroborated CONTROL evidence without hidden engine truth.

See decisions D-016–D-019, research notes 084–103, and `docs/progress/2026-09-14_live_nominal_and_delta_p_validation.md`.

## Continuous-time engine boundary

At the approximately 79:17 GET final poll, `flight_go` becomes pending while the session remains RUNNING. GET continues. Downstream nominal events execute only if prerequisites are present at their scheduled times; otherwise they are recorded as missed and are not replayed after a late decision.

Manual `/advance` remains validation infrastructure only. Normal runtime pacing is 1× monotonic wall-clock time.

## Final PC+2 load boundary

Research notes 098–099 carry the final state-vector/target-load work into the executable model:

`FIDO/RTCC final solution → GUIDO load readiness/consistency → INCO uplink configuration → CAPCOM/crew configuration → state-vector + target-load transmission → load complete / computer returned to crew`

Exact Cartesian vector contents, RTCC/CCATS command internals, controller keying, and transmission duration remain deliberately unfrozen.

## Immediate post-burn boundary

Research note **101** resolves open question 35 for the first playable.

Primary Apollo 13 records establish:

- ignition at 79:27:38.30 GET and a nominal burn;
- nominal PGNS residuals R1 +00010, R2 +00003, R3 +00000;
- initial LM power-down beginning at approximately 79+34;
- retention of functions required for communications/guidance/PTC rather than an instantaneous total shutdown;
- a detailed PTC-establishment procedure read to the crew at approximately 79+52;
- later tracking as additional trajectory confirmation after the immediate post-burn transition.

First-playable sequence:

`cutoff/result → post-burn assessment → release from burn configuration → partial power-down → PTC preparation`

Do not add unsupported exact console keying, a formal controller-by-controller post-burn poll, switch-by-switch timing, or a full PTC dynamics model before a concrete scenario need exists.

## Spacecraft physical-model boundary

Research note **102** and Decision **D-019** resolve open question 12 for the current PC+2 slice.

The first playable uses **decision-relevant causal fidelity**. A physical mechanism is admitted when it is needed to generate sourced player information, enforce a sourced rule/procedure, or support a selected failure path.

Required domains:

- DPS/maneuver state;
- guidance/attitude/control state;
- coarse electrical/equipment availability;
- communications/uplink/ranging availability;
- instrumentation observation validity/freshness.

The first playable does not require full LM ECS/CSM physics, six-degree-of-freedom propagation, pulse-level RCS, detailed battery/wiring/RF physics, complete LM instrumentation, or full internal RTCC/CCATS emulation. Those remain deferred until a sourced controller decision or selected failure mechanism depends on them.

The admission chain is:

`historical/player decision dependency → physical cause → sensed/processed observation → station product/action`

An unresolved historical link stays unresolved; it is not replaced with a convenient invented mechanism.

## Ground data-processing boundary

Research note **103** resolves open question 13 for the current PC+2 slice.

Apollo 13 primary sources place CCATS between MCC and MSFN for telemetry/command/tracking data flow and place RTCC behind telemetry processing, trajectory/ephemeris calculations, command-load generation, display generation, tracking-data selection, and trajectory computation support.

For the first playable, represent these as functional services only when they affect a player decision:

`MSFN source/path → CCATS reception/routing/processing → RTCC processing/product generation → station-visible product/status`

Relevant modeled concepts may include tracking/ranging availability and quality, trajectory-solution readiness, telemetry-path availability, and staged command/load transfer. Do not emulate IBM 360/75 or UNIVAC 494 execution, exact support-console keying, internal message formats, full MSFN routing/geometry, or invented processing delays/failure rates without a concrete sourced scenario dependency.

## First nonnominal branch

The synthetic PC+2 fuel/oxidizer ΔP path remains:

`source injection → CONTROL product/rule → explicit CONTROL decision → CAPCOM queue/transmission → explicit crew receipt → crew shutdown command → physical DPS response → crew report / fresh GQ6510P observation → CONTROL evidence assessment`

The 26 psi exercise is explicitly synthetic. Internal CONTROL→CAPCOM routing is not claimed as historically exact; stale pre-command pressure cannot count; no pressure magnitude is treated as an engine-off threshold; CONTROL evidence does not read hidden `engine_running` truth.

This full chain has now passed deployed facilitator-driven browser validation. The successful final evidence state was `corroborated`, based on a post-command crew report plus a fresh synthetic chamber-pressure observation, with no authoritative engine-off verdict exposed to CONTROL.

## Facilitator boundary

The normal `/` client contains station-authorized controller operations only. `/admin` contains exercise-control functions. Configured deployments require the facilitator credential for exercise-wide operations. This is modern project infrastructure, not Apollo-era authentication reconstruction.

## Live-device / human-play boundary

The facilitator-driven deployed integration boundary is closed for the nominal PC+2 and synthetic ΔP paths. The remaining live boundary is **multi-human station play**.

Research notes 090 and 095–103 plus the testing protocol/preparation/reference/report files define that validation. Players receive source-bounded station responsibilities/rules/procedures while remaining blind to nonnominal branch timing/content, hidden state, another station's private evidence, and intended diagnosis.

Nominal PC+2 comes first and must continue through the immediate post-burn transition; synthetic ΔP follows to test human recognition, communication, and response rather than first-time software integration.

## Compact five-player boundary

The approved compact project configuration remains:

- FLIGHT;
- CAPCOM;
- LM SYSTEMS = TELMU + CONTROL;
- FLIGHT DYNAMICS = GUIDO + FIDO/RETRO;
- INCO.

Original station identities remain authoritative. Compact labels are presentation-only. Five players remain the minimum supported PC+2 configuration at the current fidelity target.

## Backroom / Staff Support Room boundary

Research note 100 resolves open question 19 for the current first playable. Apollo 13 SSR/backroom support is historically acknowledged, but no separate SSR player or fictional automated expert advice is added before a concrete support-generated decision dependency exists.

## Active priorities

### A. Preserve and improve the validation harness

1. repair confirmed test-console/runtime defects and add regression coverage;
2. keep the facilitator/test screen as the primary development surface;
3. do not begin player-facing station UI reconstruction yet.

### B. Replace scripted consequences with a causal simulation core

1. model the crew as a simulation-controlled actor responding to CAPCOM through structured/canned acknowledgements and supported cockpit actions;
2. separate scenario initial conditions/failure injections from authoritative subsystem evolution;
3. make supported actions alter subsystem state rather than select a pre-authored outcome branch;
4. derive instrumentation, telemetry, ground products, and crew reports from resulting state while preserving information boundaries.

### C. Research and implement the first numerical subsystem chain

1. prioritize Apollo LMS/AMS mathematical-model, malfunction, instructor, output-dictionary, and validation/correlation documentation;
2. extract state variables, equations, subsystem interfaces, integration/update assumptions, and failure-insertion boundaries;
3. cross-check simulator abstractions against Apollo 13 LM-7/CSM vehicle documentation before adopting mission-specific constants;
4. implement propulsion + attitude/thrust direction + trajectory as the first numerical proof chain;
5. validate correct, late, omitted, and incorrect burn commands through the existing test screen;
6. follow with electrical power and consumables, then connect those states to instrumentation/telemetry/controller products.

### D. Defer human/player-interface validation

The seven-seat/five-player play protocols, packets, and compact-role work remain valid, but execution is deliberately deferred until the causal engine and simulated-crew loop are mature enough that player actions can produce realistic emergent consequences.

## Explicitly deferred

- exact console pixel/character reconstruction;
- singular 150-psi inlet-pressure aggregation;
- exact onboard 77-percent thrust indication;
- detailed DPS transient timing beyond selected branch needs;
- full six-degree-of-freedom spacecraft/orbital propagation;
- pulse-level RCS jet dynamics;
- full LM ECS and dormant CSM subsystem physics for this slice;
- detailed battery chemistry, wiring, breaker, RF propagation/modulation physics;
- complete LM instrumentation-channel emulation;
- full RTCC trajectory propagator/internal RTCC-CCATS computation;
- IBM 360/75 or UNIVAC 494 emulation, exact support-console keying, internal ground-system message formats, full MSFN routing/geometry, and unsupported processing delays/failure rates;
- exact PC+2 RTCC Cartesian vector contents, RTCC/CCATS load-keying, and exact final-load transmission duration;
- exact post-burn console keying, formal poll structure, switch-by-switch power-down timing, and full PTC dynamics;
- playable/detailed Staff Support Room reconstruction until a concrete scenario dependency requires it;
- sub-five-player PC+2 mode unless explicitly reopened;
- multi-session/durable production persistence;
- historically exact SimSup console UI;
- named/fine-grained facilitator accounts;
- cryptographic player authentication;
- numeric PC+2 allowable-delay/retargeting model without direct evidence;
- time acceleration.

## Current success criterion

The repository has now demonstrated a rejoin-safe, phone-accessible, continuously running authoritative mission in deployed facilitator-driven validation: the nominal PC+2 sequence reaches the source-bounded post-burn/PTC transition, and the synthetic ΔP branch reaches corroborated controller evidence while preserving the separation between observation, communication, crew action, physical response, and controller-visible evidence.

The next unclosed PASS boundary is causal-engine behavior under the validation harness: arbitrary supported actions must propagate through subsystem state into realistic downstream mission and controller-visible consequences. Physical seven-seat and five-player compact multi-human PASS claims remain deliberately deferred.