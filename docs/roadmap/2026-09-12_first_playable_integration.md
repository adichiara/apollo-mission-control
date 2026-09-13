# Roadmap addendum — first playable PC+2 integration

Date: 2026-09-12  
Status: **CURRENT — repository-side preparation and source-bounded scope work complete; physical human/device execution remains**

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
- [x] primary-source review of LM subsystem dependencies and explicit decision-relevant spacecraft-physics boundary.

See decisions D-016–D-019 and research notes 084–102.

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

## First nonnominal branch

The synthetic PC+2 fuel/oxidizer ΔP path remains:

`source injection → CONTROL product/rule → explicit CONTROL decision → CAPCOM queue/transmission → explicit crew receipt → crew shutdown command → physical DPS response → crew report / fresh GQ6510P observation → CONTROL evidence assessment`

The 26 psi exercise is explicitly synthetic. Internal CONTROL→CAPCOM routing is not claimed as historically exact; stale pre-command pressure cannot count; no pressure magnitude is treated as an engine-off threshold; CONTROL evidence does not read hidden `engine_running` truth.

## Facilitator boundary

The normal `/` client contains station-authorized controller operations only. `/admin` contains exercise-control functions. Configured deployments require the facilitator credential for exercise-wide operations. This is modern project infrastructure, not Apollo-era authentication reconstruction.

## Live-device / human-play boundary

Research notes 090 and 095–102 plus the testing protocol/preparation/reference/report files define the remaining physical validation. Players receive source-bounded station responsibilities/rules/procedures while remaining blind to nonnominal branch timing/content, hidden state, another station's private evidence, and intended diagnosis.

Nominal PC+2 comes first and must continue through the immediate post-burn transition; synthetic ΔP follows only after nominal coordination is coherent.

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

### A. Execute live multi-device validation

1. brief every player from `PC2_PLAYER_PREPARATION.md`, provide `PC2_PLAYER_REFERENCE_PACKET.md`, record preparation completion, and preserve scenario blindness;
2. run one facilitator console plus separate real-phone/browser clients against one dedicated server;
3. execute identity/rejoin/authority/isolation checks;
4. complete nominal PC+2 through note-101 post-burn verification/power-down/PTC preparation without hidden facilitator coaching;
5. assess FLIGHT/CAPCOM handoff, station readability, packet findability, staged final-load handoffs, and whether the post-burn transition needs more station-specific interaction;
6. execute the synthetic ΔP run after nominal coordination is coherent;
7. record incidents with preparation/station/build/GET/audit provenance;
8. reopen physical-model scope only if play exposes a sourced decision whose causal mechanism is absent.

### B. Execute five-player compact human validation

1. use FLIGHT, CAPCOM, LM SYSTEMS, FLIGHT DYNAMICS, and INCO simultaneously;
2. practice substation switching before timed play without scenario-specific disclosure;
3. provide separate original-station reference sheets;
4. observe TELMU↔CONTROL and GUIDO↔FIDO/RETRO switching under time pressure;
5. verify readiness/action attribution and audit provenance stay tied to original stations;
6. classify usability/instruction defects separately from historical/research defects.

### C. Reopen research only from evidence

Reopen historical or physical-model work only for concrete information/procedure/authority/support/causal dependencies exposed by validation. Player difficulty alone is not sufficient.

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

A rejoin-safe, phone-accessible, continuously running authoritative mission in which prepared station players receive only source-bounded operational information/actions, a separately authorized facilitator controls exercise-wide functions, the nominal load process remains staged, successful PC+2 continues through a source-bounded post-burn verification/power-down transition, spacecraft physics remains causal but scenario-bounded, compact play preserves original-station identities, and omitted historical support-room functions are not replaced with invented analysis. Physical seven-seat and five-player human/device execution remain the next unclosed PASS boundaries.