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
- [x] primary-source review of LM subsystem dependencies and explicit decision-relevant spacecraft-physics boundary;
- [x] primary-source review of MSFN/CCATS/RTCC support functions and explicit decision-relevant ground-data-processing boundary;
- [x] primary-source review of LM instrumentation failure experience and explicit layered observation-failure boundary with no random first-playable faults;
- [x] primary-source review of ground-to-crew procedure execution and explicit scenario-authored crew-action boundary with no separate first-playable crew player;
- [x] follow-up primary-source review of the 150-psi DPS inlet-pressure rule lineage, narrowing the leading candidate to fuel inlet / `GQ3611P` without asserting an Apollo 13-specific exact mapping;
- [x] follow-up primary-source review of the onboard 77-percent rule, identifying the panel-1 CMD THRUST / ENG THRUST instrument family and ENG THRUST actual-thrust scale;
- [x] follow-up primary-source review of the 77-percent startup applicability gate, using the Apollo 13 crew-debrief full-throttle transition at burn +26 seconds as the first-playable applicability boundary while explicitly labeling the final mapping as a lineage-based inference rather than a verbatim recovered Apollo 13 rule qualifier;
- [x] follow-up primary-source reconciliation of the attitude “start transient” wording conflict: the contemporaneous CAPCOM transmission and Haise readback attach the exception to ±10-degree attitude error, while the later postflight summary wording differs. Exact transient duration remains unresolved.

See decisions D-016–D-021 and research notes 084–109.

## Continuous-time engine boundary

At the approximately 79:17 GET final poll, `flight_go` becomes pending while the session remains RUNNING. GET continues. Downstream nominal events execute only if prerequisites are present at their scheduled times; otherwise they are recorded as missed and are not replayed after a late decision.

Manual `/advance` remains validation infrastructure only. Normal runtime pacing is 1× monotonic wall-clock time.

## Final PC+2 load boundary

Research notes 098–099 carry the final state-vector/target-load work into the executable model:

`FIDO/RTCC final solution → GUIDO load readiness/consistency → INCO uplink configuration → CAPCOM/crew configuration → state-vector + target-load transmission → load complete / computer returned to crew`

Exact Cartesian vector contents, RTCC/CCATS command internals, controller keying, and transmission duration remain deliberately unfrozen.

## Immediate post-burn boundary

Research note **101** resolves open question 35 for the first playable.

Primary Apollo 13 records establish ignition at 79:27:38.30 GET, nominal PGNS residuals, initial LM power-down beginning at approximately 79+34, retention of functions required for communications/guidance/PTC, a detailed PTC-establishment procedure at approximately 79+52, and later tracking as additional trajectory confirmation.

First-playable sequence:

`cutoff/result → post-burn assessment → release from burn configuration → partial power-down → PTC preparation`

Do not add unsupported exact console keying, a formal controller-by-controller post-burn poll, switch-by-switch timing, or a full PTC dynamics model before a concrete scenario need exists.

## Spacecraft physical-model boundary

Research note **102** and Decision **D-019** resolve open question 12 for the current PC+2 slice.

The first playable uses **decision-relevant causal fidelity**. A physical mechanism is admitted when needed to generate sourced player information, enforce a sourced rule/procedure, or support a selected failure path.

Required domains are DPS/maneuver state, guidance/attitude/control state, coarse electrical/equipment availability, communications/uplink/ranging availability, and instrumentation observation validity/freshness.

The first playable does not require full LM ECS/CSM physics, six-degree-of-freedom propagation, pulse-level RCS, detailed battery/wiring/RF physics, complete LM instrumentation, or full internal RTCC/CCATS emulation.

## Ground data-processing boundary

Research note **103** resolves open question 13 for the current PC+2 slice.

Represent MSFN/CCATS/RTCC as functional services only where they affect a player decision:

`MSFN source/path → CCATS reception/routing/processing → RTCC processing/product generation → station-visible product/status`

Relevant modeled concepts may include tracking/ranging availability and quality, trajectory-solution readiness, telemetry-path availability, and staged command/load transfer. Do not emulate IBM 360/75 or UNIVAC 494 execution, exact support-console keying, internal message formats, full MSFN routing/geometry, or invented processing delays/failure rates without a concrete sourced scenario dependency.

## Observation-failure boundary

Research note **104** and Decision **D-020** resolve open question 14 for the current PC+2 slice.

The simulator preserves:

`physical source → sensor/transducer → conditioning/PCM → communications/telemetry path → ground processing → station product`

Nominal PC+2 receives no added historical sensor fault; the synthetic ΔP exercise is not retroactively explained as a failed transducer; and unsupported probabilities, random failure rates, noise/bias magnitudes, durations, recovery timing, and correlations are not invented.

## Crew-action boundary

Research note **105** and Decision **D-021** resolve open question 15 for the current PC+2 slice.

The first playable uses:

`controller evidence → controller decision → CAPCOM message → crew receipt → crew action → physical spacecraft response → telemetry / crew report → controller evidence`

No separate human crew player is added. Nominal crew actions may be deterministic scenario-authored steps where crew discretion is not the mechanic being tested. Random misunderstanding/noncompliance, generic crew-error rates, and unsupported response-delay distributions are not invented.

## Inlet-pressure rule-lineage boundary

Research note **106** revisits the deliberately unresolved 150-psi ground inlet-pressure criterion without changing the executable model.

Apollo 13 CAPCOM explicitly related the PC+2 shutdown rules to **LOI Mode I abort with tight limits**. A surviving Apollo 10 DPS mission rule uses **fuel inlet pressure <150 psi above 65% throttle**. LM-7-family data identify `GQ3611P` as engine-interface fuel pressure and `GQ4111P` as the separate oxidizer value.

This makes fuel inlet / `GQ3611P` the leading historical candidate for the Apollo 13 150-psi ground criterion. It does **not** prove an Apollo 13-specific mapping because no exact CONTROL rule/display/routing page has been recovered.

Therefore keep the rule `NOT_EVALUABLE`; do not invent minimum/average/either-side aggregation or a synthetic combined inlet-pressure product.

## Onboard 77-percent thrust boundary

Research notes **107–108** resolve the first-playable instrument and applicability questions while preserving the provenance limit.

Primary mission evidence says the crew was to shut down for a **“thrust monitor readout, 77 percent or below”** and separately describes the criterion as onboard thrust. Primary LM technical documentation identifies a panel-1 dual-scale **CMD THRUST / ENG THRUST** indicator:

- CMD THRUST = commanded thrust;
- ENG THRUST = actual engine thrust;
- ENG is derived from a descent-engine combustion-chamber-pressure transducer;
- ENG is displayed as percent thrust and reads about 92.5 percent at fixed full throttle.

Apollo 13 LM malfunction procedures also use CMD THRUST / ENG THRUST indicator terminology. The instrument identity is therefore high-confidence, and the ENG scale is the source-backed actual-performance scale relevant to the rule.

The Apollo 13 Technical Crew Debriefing supplies the missing phase boundary: PC+2 used 5 seconds at idle/low thrust, 21 seconds at 40-percent throttle, then the remainder at full throttle; Lovell states that the configured transition to full throttle occurred at **burn +26 seconds**. The Mission Operations Report independently records the same staged throttle profile in rounded form.

For the current first playable:

- the 77-percent criterion is inactive during the intentionally commanded 12.6-percent/40-percent startup segments;
- it becomes applicable when the commanded profile enters maximum/full throttle;
- the nominal Apollo 13 gate is burn +26 seconds;
- the gate is explicitly a **source-bounded lineage inference**, not a recovered Apollo 13 sentence saying that the 77-percent rule activates exactly at that moment;
- the gate does not create an ENG THRUST observation: a scenario-authored crew-visible indication is still required for evaluation;
- do not alias the indication to ground `GQ6510P` or derive it directly from hidden engine state.

## Attitude start-transient boundary

Research note **109** resolves the prior conflict over which PC+2 attitude criterion carried the startup exception.

The contemporaneous 76:30 GET CAPCOM transmission and 76:37 GET Haise readback both specify:

- attitude error ±10 degrees, **except for the start transient**;
- attitude rate ±10 degrees/sec, with no stated exception.

The later Flight Control Division Mission Operations Report III-25 instead attaches “except start transients” to attitude rate. The project preserves that conflict but gives implementation precedence to the operational instruction actually transmitted to and acknowledged by the crew.

The exact duration of “start transient” is still unsupported. Do not equate it to the 5-second 12.6-percent segment, the 21-second 40-percent segment, the full +26-second low-thrust interval, or any inferred hidden engine-dynamics window without direct evidence.

## First nonnominal branch

The synthetic PC+2 fuel/oxidizer ΔP path remains:

`source injection → CONTROL product/rule → explicit CONTROL decision → CAPCOM queue/transmission → explicit crew receipt → crew shutdown command → physical DPS response → crew report / fresh GQ6510P observation → CONTROL evidence assessment`

The 26 psi exercise is explicitly synthetic. Internal CONTROL→CAPCOM routing is not claimed as historically exact; stale pre-command pressure cannot count; no pressure magnitude is treated as an engine-off threshold; CONTROL evidence does not read hidden `engine_running` truth.

## Facilitator boundary

The normal `/` client contains station-authorized controller operations only. `/admin` contains exercise-control functions. Configured deployments require the facilitator credential for exercise-wide operations. This is modern project infrastructure, not Apollo-era authentication reconstruction.

## Live-device / human-play boundary

Research notes 090 and 095–109 plus the testing protocol/preparation/reference/report files define the remaining physical validation. Players receive source-bounded station responsibilities/rules/procedures while remaining blind to nonnominal branch timing/content, hidden state, another station's private evidence, and intended diagnosis.

Nominal PC+2 comes first and must continue through the immediate post-burn transition; synthetic ΔP follows only after nominal coordination is coherent. Observation faults beyond the authored synthetic branch and unsourced crew delays/errors must not be improvised during play.

## Compact five-player boundary

The approved compact project configuration remains FLIGHT; CAPCOM; LM SYSTEMS = TELMU + CONTROL; FLIGHT DYNAMICS = GUIDO + FIDO/RETRO; and INCO.

Original station identities remain authoritative. Compact labels are presentation-only. Five players remain the minimum supported PC+2 configuration at the current fidelity target. The spacecraft crew remains an external scenario actor, not a sixth compact-role player.

## Backroom / Staff Support Room boundary

Research note 100 resolves open question 19 for the current first playable. Apollo 13 SSR/backroom support is historically acknowledged, but no separate SSR player or fictional automated expert advice is added before a concrete support-generated decision dependency exists.

## Active priorities

### A. Execute live multi-device validation

1. brief every player from `PC2_PLAYER_PREPARATION.md`, provide `PC2_PLAYER_REFERENCE_PACKET.md`, record preparation completion, and preserve scenario blindness;
2. run one facilitator console plus separate real-phone/browser clients against one dedicated server;
3. execute identity/rejoin/authority/isolation checks;
4. complete nominal PC+2 through note-101 post-burn verification/power-down/PTC preparation without hidden facilitator coaching, improvised telemetry faults, or invented crew delays/errors;
5. assess FLIGHT/CAPCOM handoff, station readability, packet findability, staged final-load handoffs, CAPCOM→crew sequencing, and whether the post-burn transition needs more station-specific interaction;
6. execute the synthetic ΔP run after nominal coordination is coherent;
7. record incidents with preparation/station/build/GET/audit provenance;
8. reopen spacecraft, observation-integrity, crew-action, or ground-data-processing scope only if play exposes a sourced decision whose causal/data-path/crew-execution mechanism is absent.

### B. Execute five-player compact human validation

1. use FLIGHT, CAPCOM, LM SYSTEMS, FLIGHT DYNAMICS, and INCO simultaneously;
2. practice substation switching before timed play without scenario-specific disclosure;
3. provide separate original-station reference sheets;
4. observe TELMU↔CONTROL and GUIDO↔FIDO-RETRO switching under time pressure;
5. verify readiness/action attribution and audit provenance stay tied to original stations;
6. classify usability/instruction defects separately from historical/research defects.

### C. Reopen research only from evidence

Reopen historical, physical-model, observation-integrity, crew-action, or ground-processing work only for concrete information/procedure/authority/support/causal/data-path/crew-discretion dependencies exposed by validation. Player difficulty alone is not sufficient.

Notes 106–109 are retained as bounded archival refinements discovered during repository continuation; they do not change the physical-validation priority or authorize unsupported mechanics.

## Explicitly deferred

- exact console pixel/character reconstruction;
- Apollo 13-specific proof that the 150-psi ground criterion maps directly to fuel-interface measurement `GQ3611P`;
- a verbatim Apollo 13 mission-rule qualifier for the 77-percent ENG THRUST applicability gate; the first playable uses the sourced full-throttle transition at burn +26 seconds as an explicitly labeled lineage-based approximation;
- exact duration/end definition of the attitude-error “start transient” exception; no 5-, 21-, or 26-second boundary is assumed;
- detailed DPS transient timing beyond selected branch needs;
- full six-degree-of-freedom spacecraft/orbital propagation;
- pulse-level RCS jet dynamics;
- full LM ECS and dormant CSM subsystem physics for this slice;
- detailed battery chemistry, wiring, breaker, RF propagation/modulation physics;
- complete LM instrumentation-channel emulation;
- random/generic instrumentation or telemetry failure generation, unsupported failure rates, noise distributions, fault durations, or recovery timing;
- random crew-error/noncompliance mechanics and unsupported response-delay distributions;
- a human crew player before a selected scenario requires decision-relevant astronaut discretion/workload/manual operation;
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

A rejoin-safe, phone-accessible, continuously running authoritative mission in which prepared station players receive only source-bounded operational information/actions, a separately authorized facilitator controls exercise-wide functions, the nominal load process remains staged, successful PC+2 continues through a source-bounded post-burn verification/power-down transition, spacecraft physics and ground processing remain causal but scenario-bounded, observation faults remain layered and scenario-authored rather than random, crew actions remain explicit downstream of CAPCOM rather than automatic or randomly error-prone, compact play preserves original-station identities, and omitted historical support-room functions are not replaced with invented analysis. Physical seven-seat and five-player human/device execution remain the next unclosed PASS boundaries.