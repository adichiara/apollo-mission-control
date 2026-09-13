# Roadmap addendum — first playable PC+2 integration

Date: 2026-09-12  
Status: **CURRENT — automated validation passing; live-device/human-play protocol defined and physical execution remains**

## Completed checkpoints

- [x] minimum player presentations for CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, FLIGHT, CAPCOM;
- [x] one authoritative mission state and synchronized GET;
- [x] readiness reports, FLIGHT decision requirement, CAPCOM queue/transmission, and audit trail;
- [x] FastAPI/Uvicorn phone-accessible transport;
- [x] rejoin-safe browser identity persistence;
- [x] continuous mission clock: controller decisions do not stop GET;
- [x] declarative nominal-event eligibility and missed-event consequences;
- [x] 1× monotonic wall-clock pacing;
- [x] end-to-end source-bounded ΔP branch through fresh CONTROL evidence;
- [x] ordinary player station client separated from validation/SimSup client;
- [x] primary-source review of Simulation Supervisor / simulation-control role separation;
- [x] server-side facilitator credential for exercise-wide operations;
- [x] Render deployment secret generated outside source control;
- [x] facilitator authority kept separate from all controller station identities;
- [x] primary-source review of integrated flight-controller simulation as the validation model;
- [x] in-process multi-client contract test across FLIGHT/CONTROL/CAPCOM/GUIDO + facilitator;
- [x] destructive real-network multi-client smoke runner;
- [x] complete unit/integration suite passing in GitHub Actions;
- [x] real TCP/HTTP smoke passing in GitHub Actions against an ephemeral authorized Uvicorn server;
- [x] admin UI evidence-class values reconciled with the server enum;
- [x] stale pre-authorization UI contract assertion repaired;
- [x] primary-source review of Apollo integrated crew/ground-controller simulation for the live-play boundary;
- [x] structured real-device/human-play protocol with nominal and synthetic ΔP runs, pass criteria, and defect classification.

The deployment remains single-process/in-memory. Restart/redeploy loses the live session; multiple workers/sessions and durable persistence remain deferred.

See decisions D-016–D-017 and research notes 084–090.

## Continuous-time engine boundary

At the approximately 79:17 GET final poll, `flight_go` becomes pending while the session remains `RUNNING`. GET continues. Downstream nominal events execute only if their prerequisites are present at their scheduled times; otherwise they are recorded as missed and are not replayed after a late decision.

Manual `/advance` is validation infrastructure only. Normal runtime pacing is 1× monotonic wall-clock time.

## First nonnominal branch

The synthetic PC+2 fuel/oxidizer ΔP branch now reaches controller evidence end to end:

`source injection → CONTROL product/rule → explicit CONTROL decision → CAPCOM queue/transmission → explicit crew receipt → crew shutdown command → physical DPS response → crew report / fresh GQ6510P observation → CONTROL evidence assessment`

The branch preserves all established guardrails: 26 psi is synthetic; internal CONTROL→CAPCOM routing is not claimed as historically exact; each communication/action/physical/evidence layer is explicit; stale pre-command pressure cannot count; no pressure magnitude becomes an engine-off threshold; and CONTROL evidence never reads hidden `engine_running` truth.

## Facilitator boundary

The normal `/` client contains station-authorized controller operations only. The `/admin` interface contains exercise-control functions.

When `APOLLO_FACILITATOR_TOKEN` is configured, exercise-wide API operations require the `X-Apollo-Facilitator` header. Render receives a generated secret through `render.yaml`; if a Render instance somehow lacks that configuration, protected operations fail closed.

Protected operations include lifecycle/reset, manual validation time, state injection, validation crew/vehicle response operations, and global audit access. Controller station operations remain independent of this credential.

This is a modern software safety boundary. Historical NASA sources support the organizational separation of SimSup/simulation control from flight controllers, but do not establish an Apollo authentication mechanism.

## Multi-client validation boundary

Research note 089 uses primary NASA simulation-training evidence to justify validating the controller environment as an integrated system while keeping facilitator/simulation-control functions distinct.

`tests/test_web_multiclient_integration.py` protects the in-process contract for shared authoritative state, station-scoped operational information, rejoin, occupied-station protection, facilitator authority isolation, explicit pause semantics, and complete synthetic ΔP propagation/evidence ordering.

`scripts/pc2_multiclient_smoke.py` carries those checks into a real HTTP environment and adds simultaneous station polling.

GitHub Actions now runs both the full unit/integration suite and that smoke runner against an ephemeral localhost Uvicorn server with facilitator authorization enabled. Both are recorded as passing.

## Live-device / human-play boundary

Research note 090 uses Apollo/NASA integrated-simulation sources to constrain the remaining physical validation. The sources support combined crew/controller rehearsal in a mission environment and decisionmaking/procedure readiness, but do not establish phone UI criteria, browser reload semantics, HTTP latency limits, or facilitator authentication.

`docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md` therefore treats the remaining run as a structured mission rehearsal while keeping modern usability/network observations explicitly separate from historical research findings.

The nominal PC+2 run comes first. The existing synthetic ΔP branch is a second run only after normal coordination is coherent.

## Active priority — execute live multi-device validation

1. run one facilitator console plus separate real-phone/browser clients for at least FLIGHT, CONTROL, CAPCOM, and GUIDO against one dedicated server;
2. execute the pre-run identity/rejoin/authority/isolation checks in `docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md`;
3. complete the nominal PC+2 sequence without hidden facilitator coaching and assess FLIGHT/CAPCOM handoff ergonomics;
4. repair blocking phone/network/presentation defects and add regression tests where reproducible;
5. execute the synthetic ΔP run after nominal coordination is coherent;
6. reopen historical research only for concrete information/procedure/authority dependencies exposed by play.

## Integration validation still required

Covered and executed automatically:

- complete unit/integration suite;
- in-process multi-client station isolation;
- real TCP/HTTP concurrent polling and actions;
- reload/rejoin contract;
- explicit pause behavior;
- ΔP evidence boundaries;
- facilitator/player authority isolation.

Protocol defined but still requiring physical execution:

- real phone/browser reload/rejoin;
- continuous GET behavior under external network latency;
- phone readability and action ergonomics;
- nominal PC+2 completion with human operators;
- missed-event behavior during real late-controller decisions;
- FLIGHT/CAPCOM handoff under actual play;
- synthetic ΔP human-play follow-up after nominal success.

## Explicitly deferred

- exact console pixel/character reconstruction;
- singular 150-psi inlet-pressure aggregation;
- exact onboard 77-percent thrust indication;
- detailed DPS transient timing;
- full RTCC trajectory propagator;
- backroom/staff-support simulation;
- low-player-count station aggregation;
- multi-session/durable production persistence;
- historically exact SimSup console UI;
- named/fine-grained facilitator accounts;
- cryptographic player authentication;
- numeric PC+2 allowable-delay/retargeting model without direct evidence;
- time acceleration.

## Current success criterion

A rejoin-safe, phone-accessible, continuously running authoritative mission in which station players receive only their operational information/actions, a separately authorized facilitator controls exercise-wide simulation functions, and source-bounded nonnominal conditions propagate through explicit controller/crew/vehicle/evidence layers without hidden decisions, hidden physical-truth leaks, or invented historical behavior—validated automatically in-process and over real HTTP, with the remaining real-device/human-play protocol then executed successfully on actual clients.