# Roadmap addendum — first playable PC+2 integration

Date: 2026-09-12  
Status: **CURRENT — compact HTTP/browser integration implemented; sub-five-player boundary researched; live-device execution remains**

## Completed checkpoints

- [x] minimum player presentations for CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, FLIGHT, CAPCOM;
- [x] one authoritative mission state and synchronized GET;
- [x] readiness reports, FLIGHT decision requirement, CAPCOM queue/transmission, and audit trail;
- [x] FastAPI/Uvicorn phone-accessible transport;
- [x] rejoin-safe browser identity persistence;
- [x] continuous mission clock and declarative nominal-event eligibility;
- [x] 1× monotonic wall-clock pacing;
- [x] end-to-end source-bounded ΔP branch through fresh CONTROL evidence;
- [x] ordinary player client separated from facilitator/validation client;
- [x] facilitator authority protected independently from controller station identity;
- [x] in-process multi-client contract test and real-network smoke runner;
- [x] complete pre-compact suite and real TCP/HTTP smoke passing in GitHub Actions;
- [x] structured real-device/human-play protocol;
- [x] primary-source review constraining five-player compact play;
- [x] one-player/multiple-original-stations domain ownership;
- [x] bundled snapshots with separate original-station presentations;
- [x] station-qualified readiness/action authorization and original-station audit provenance;
- [x] HTTP station-set join/rejoin with legacy single-station compatibility;
- [x] generic player snapshot polling for single- and multi-station players;
- [x] compact browser persistence, legacy identity migration, and original-call-sign substation navigation;
- [x] compact HTTP/browser regression coverage;
- [x] primary-source review of the four-player boundary, with no sub-five-player PC+2 mode approved at current fidelity.

The deployment remains single-process/in-memory. Restart/redeploy loses the live session; multiple workers/sessions and durable persistence remain deferred.

See decisions D-016–D-018 and research notes 084–094.

## Continuous-time engine boundary

At the approximately 79:17 GET final poll, `flight_go` becomes pending while the session remains RUNNING. GET continues. Downstream nominal events execute only if prerequisites are present at their scheduled times; otherwise they are recorded as missed and are not replayed after a late decision.

Manual `/advance` remains validation infrastructure only. Normal runtime pacing is 1× monotonic wall-clock time.

## First nonnominal branch

The synthetic PC+2 fuel/oxidizer ΔP path remains:

`source injection → CONTROL product/rule → explicit CONTROL decision → CAPCOM queue/transmission → explicit crew receipt → crew shutdown command → physical DPS response → crew report / fresh GQ6510P observation → CONTROL evidence assessment`

The 26 psi exercise is explicitly synthetic. Internal CONTROL→CAPCOM routing is not claimed as historically exact; each communication/action/physical/evidence layer remains explicit; stale pre-command pressure cannot count; no pressure magnitude is treated as an engine-off threshold; CONTROL evidence does not read hidden `engine_running` truth.

## Facilitator boundary

The normal `/` client contains station-authorized controller operations only. `/admin` contains exercise-control functions. Configured deployments require the facilitator credential for exercise-wide operations. This is a modern project safety boundary, not Apollo-era authentication reconstruction.

## Multi-client validation boundary

`tests/test_web_multiclient_integration.py` protects the in-process contract for shared state, station isolation, rejoin, occupied-station protection, facilitator isolation, pause semantics, and ΔP ordering.

`scripts/pc2_multiclient_smoke.py` exercises those boundaries over real TCP/HTTP and simultaneous polling. Pre-compact CI has passed both the suite and network smoke.

## Live-device / human-play boundary

Research note 090 and `docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md` define the remaining physical validation. Apollo/NASA sources support integrated crew/controller rehearsal and decision/procedure readiness, but not phone UI criteria, browser reload semantics, HTTP latency limits, or token authentication.

The nominal PC+2 run comes first. The synthetic ΔP branch follows only after nominal coordination is coherent.

## Compact five-player boundary

Research notes 091–094 define and constrain the compact project configuration without claiming a historical five-person Apollo team:

- FLIGHT;
- CAPCOM;
- LM SYSTEMS = TELMU + CONTROL;
- FLIGHT DYNAMICS = GUIDO + FIDO/RETRO;
- INCO.

Primary Apollo sources support the underlying functional relationships and distinct station identities; they do not establish the bundled operators historically.

Implemented end-to-end shape:

`player → exact set of original stations → HTTP join/rejoin → bundled station-scoped snapshots → browser substation navigation → station-qualified readiness/actions/audit provenance`

The browser explicitly labels compact roles as simulator conveniences, preserves original call signs in station tabs and action surfaces, persists station sets and the active substation, and migrates legacy single-station identity. No synthetic `LM_SYSTEMS` or `FLIGHT_DYNAMICS` authoritative station exists.

Research note 094 resolves the previously open general four-player question for this scenario/fidelity target: **five players are the minimum supported PC+2 configuration**. CAPCOM and INCO remain distinct because crew-facing voice authority and communications-system monitoring/troubleshooting are separately documented functions, and communications/data-path reasoning is active in the selected PC+2 window. Silent INCO omission/automation is therefore not accepted merely to reduce player count.

This is a simulator-design boundary, not a historical minimum-staffing claim.

## Active priorities

### A. Execute live multi-device validation

1. run one facilitator console plus separate real-phone/browser clients against one dedicated server;
2. execute identity/rejoin/authority/isolation checks from `PC2_LIVE_PLAYTEST_PROTOCOL.md`;
3. complete nominal PC+2 without hidden facilitator coaching;
4. assess FLIGHT/CAPCOM handoff and station readability;
5. execute the synthetic ΔP run after nominal coordination is coherent.

### B. Execute five-player compact human validation

1. use FLIGHT, CAPCOM, LM SYSTEMS, FLIGHT DYNAMICS, and INCO clients simultaneously;
2. observe TELMU↔CONTROL and GUIDO↔FIDO/RETRO switching under time pressure;
3. verify readiness/action attribution remains tied to the active original station;
4. inspect audit output for original-station provenance and isolation;
5. classify usability defects separately from historical/research defects.

### C. Reopen research only from evidence

Reopen historical work only for concrete information/procedure/authority dependencies exposed by validation. Reopen sub-five-player design only if live testing demonstrates a real need, a different scenario removes a station dependency, stronger primary evidence supports another pairing, or an explicitly lower-fidelity accessibility mode is deliberately chosen.

## Explicitly deferred

- exact console pixel/character reconstruction;
- singular 150-psi inlet-pressure aggregation;
- exact onboard 77-percent thrust indication;
- detailed DPS transient timing;
- full RTCC trajectory propagator;
- backroom/staff-support simulation;
- sub-five-player PC+2 mode unless the boundary is explicitly reopened;
- multi-session/durable production persistence;
- historically exact SimSup console UI;
- named/fine-grained facilitator accounts;
- cryptographic player authentication;
- numeric PC+2 allowable-delay/retargeting model without direct evidence;
- time acceleration.

## Current success criterion

A rejoin-safe, phone-accessible, continuously running authoritative mission in which station players receive only their operational information/actions, a separately authorized facilitator controls exercise-wide simulation functions, and source-bounded nonnominal conditions propagate through explicit controller/crew/vehicle/evidence layers without hidden decisions, hidden physical-truth leaks, or invented historical behavior. Compact mode must preserve the same boundaries while allowing one modern player to operate several separately identified original stations. Physical seven-seat and five-player human/device execution remain the next unclosed PASS boundaries.
