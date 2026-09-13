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
- [x] station-set HTTP join/rejoin, bundled snapshots, station-qualified readiness/actions, audit provenance, and browser substation navigation;
- [x] four-player boundary reviewed with no sub-five-player PC+2 mode approved at current fidelity;
- [x] structured live-play evidence/debrief package;
- [x] reproducible scenario-blind player-preparation package and first-run reference packet;
- [x] primary-source review and staged implementation of the final PC+2 state-vector/target-load/uplink workflow;
- [x] staged final-load regression coverage passing GitHub Actions run 118;
- [x] primary-source review of Apollo 13 Staff Support Room/backroom functions and explicit first-playable support-room scope boundary.

See decisions D-016–D-018 and research notes 084–100.

## Continuous-time engine boundary

At the approximately 79:17 GET final poll, `flight_go` becomes pending while the session remains RUNNING. GET continues. Downstream nominal events execute only if prerequisites are present at their scheduled times; otherwise they are recorded as missed and are not replayed after a late decision.

Manual `/advance` remains validation infrastructure only. Normal runtime pacing is 1× monotonic wall-clock time.

## Final PC+2 load boundary

Research notes 098–099 carry the final state-vector/target-load work into the executable model:

`FIDO/RTCC final solution → GUIDO load readiness/consistency → INCO uplink configuration → CAPCOM/crew configuration → state-vector + target-load transmission → load complete / computer returned to crew`

The model distinguishes `preliminary` → `final_ready` → `final_stable` ground-solution state and `preliminary_loaded` → `final_pending` → `transmitting` → `final_loaded` state-vector/target-load status. Ranging remains a separate final-preparation dependency.

Exact Cartesian vector contents, RTCC/CCATS command internals, controller keying, and transmission duration remain deliberately unfrozen.

## First nonnominal branch

The synthetic PC+2 fuel/oxidizer ΔP path remains:

`source injection → CONTROL product/rule → explicit CONTROL decision → CAPCOM queue/transmission → explicit crew receipt → crew shutdown command → physical DPS response → crew report / fresh GQ6510P observation → CONTROL evidence assessment`

The 26 psi exercise is explicitly synthetic. Internal CONTROL→CAPCOM routing is not claimed as historically exact; each communication/action/physical/evidence layer remains explicit; stale pre-command pressure cannot count; no pressure magnitude is treated as an engine-off threshold; CONTROL evidence does not read hidden `engine_running` truth.

## Facilitator boundary

The normal `/` client contains station-authorized controller operations only. `/admin` contains exercise-control functions. Configured deployments require the facilitator credential for exercise-wide operations. This is modern project infrastructure, not Apollo-era authentication reconstruction.

## Live-device / human-play boundary

Research notes 090 and 095–097 plus the testing protocol/preparation/reference/report files define the remaining physical validation. Players receive station responsibility, visible products/actions, relevant PC+2 rules/procedures, authority/coordination boundaries, and modern client-operation knowledge while remaining blind to nonnominal branch timing/content, hidden state, another station's private evidence, and intended diagnosis.

Each material incident should retain run/build, GET, player role, active original station, device/browser, visible evidence, action/communication, expected/observed result, audit/event reference where available, and participant preparation record. Debrief must separate observed facts from interpretation, reproducible defects, historical questions, usability-only changes, instructional gaps, and legitimate uncertainty.

Nominal PC+2 comes first; synthetic ΔP follows only after nominal coordination is coherent.

## Compact five-player boundary

Research notes 091–094 define the compact project configuration without claiming a historical five-person Apollo team:

- FLIGHT;
- CAPCOM;
- LM SYSTEMS = TELMU + CONTROL;
- FLIGHT DYNAMICS = GUIDO + FIDO/RETRO;
- INCO.

Original station identities remain authoritative. Compact labels are presentation-only. Five players remain the minimum supported PC+2 configuration at the current fidelity target.

## Backroom / Staff Support Room boundary

Research note 100 resolves open question 19 for the current first playable.

Apollo 13 primary sources show that the MOCR was supported by Staff Support Rooms. Flight Dynamics SSR supplied detailed trajectory/guidance analysis and outside technical interfaces; Vehicle Systems SSR supported detailed system monitoring/troubleshooting; the Apollo 13 Mission Operations Report specifically commended EECOM SSR support during the emergency.

Therefore:

- the seven-seat/five-player configurations are front-room playable slices, not complete historical staffing reconstructions;
- no separate SSR player is added before physical front-room validation;
- no fictional automated expert advice is introduced;
- no unsupported backroom analysis is silently transferred to a front-room station;
- a concrete support-generated product or handoff exposed by playtesting/later scenarios reopens research and implementation.

Exact PC+2 SSR rosters, loop topology, and support-product flow remain unfrozen unless needed.

## Active priorities

### A. Execute live multi-device validation

1. brief every player from `PC2_PLAYER_PREPARATION.md`, provide `PC2_PLAYER_REFERENCE_PACKET.md`, record preparation completion, and preserve scenario blindness;
2. run one facilitator console plus separate real-phone/browser clients against one dedicated server;
3. execute identity/rejoin/authority/isolation checks;
4. record incidents with preparation/station/build/GET/audit provenance;
5. complete nominal PC+2 without hidden facilitator coaching;
6. assess FLIGHT/CAPCOM handoff, station readability, packet findability/clarity, and staged final-load handoffs;
7. execute the synthetic ΔP run after nominal coordination is coherent.

### B. Execute five-player compact human validation

1. use FLIGHT, CAPCOM, LM SYSTEMS, FLIGHT DYNAMICS, and INCO simultaneously;
2. ensure compact players have practiced substation switching before timed play without seeing scenario-specific events;
3. provide separate original-station reference sheets;
4. observe TELMU↔CONTROL and GUIDO↔FIDO/RETRO switching under time pressure;
5. verify readiness/action attribution and audit provenance stay tied to original stations;
6. classify usability/instruction defects separately from historical/research defects.

### C. Reopen research only from evidence

Reopen historical work only for concrete information/procedure/authority/support dependencies exposed by validation. Player difficulty alone is not sufficient. Reopen sub-five-player design only if live testing demonstrates a real need, a different scenario removes a station dependency, stronger primary evidence supports another pairing, or an explicitly lower-fidelity accessibility mode is deliberately chosen.

## Explicitly deferred

- exact console pixel/character reconstruction;
- singular 150-psi inlet-pressure aggregation;
- exact onboard 77-percent thrust indication;
- detailed DPS transient timing;
- full RTCC trajectory propagator;
- exact PC+2 RTCC Cartesian vector contents, RTCC/CCATS load-keying, and exact final-load transmission duration;
- playable/detailed Staff Support Room reconstruction until a concrete scenario dependency requires it;
- sub-five-player PC+2 mode unless explicitly reopened;
- multi-session/durable production persistence;
- historically exact SimSup console UI;
- named/fine-grained facilitator accounts;
- cryptographic player authentication;
- numeric PC+2 allowable-delay/retargeting model without direct evidence;
- time acceleration.

## Current success criterion

A rejoin-safe, phone-accessible, continuously running authoritative mission in which prepared station players receive only source-bounded operational information/actions, a separately authorized facilitator controls exercise-wide functions, nonnominal conditions propagate through explicit controller/crew/vehicle/evidence layers, the nominal final-load process remains staged, compact play preserves original-station identities, and omitted historical support-room functions are not replaced with invented analysis. Physical seven-seat and five-player human/device execution remain the next unclosed PASS boundaries.