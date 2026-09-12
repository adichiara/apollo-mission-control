# Roadmap addendum — first playable PC+2 integration

Date: 2026-09-12  
Status: **CURRENT — continuous-time nonnominal chain, player/admin separation, and facilitator authority implemented; runnable multi-client validation is next**

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
- [x] facilitator authority kept separate from all controller station identities.

The deployment remains single-process/in-memory. Restart/redeploy loses the live session; multiple workers/sessions and durable persistence remain deferred.

See decisions D-016–D-017 and research notes 084–088.

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

## Active priority — runnable multi-client integration validation

1. execute the complete domain/session/API test suite in a checked-out runtime;
2. run one facilitator console plus several simultaneous phone station clients;
3. verify realtime GET under concurrent polling/actions;
4. verify facilitator pause/resume, player reload/rejoin, and station information isolation;
5. run the complete synthetic ΔP branch through the live interfaces;
6. verify players cannot invoke protected facilitator operations when deployment authorization is configured;
7. repair usability/integration problems exposed by live multi-client operation;
8. reopen historical research only if integrated play exposes a concrete missing procedure or information dependency.

## Integration validation still required

- full-suite execution;
- reload/rejoin state preservation;
- station information isolation;
- continuous GET through pending controller decisions;
- explicit pause as the normal clock stop;
- missed-event behavior after late decisions;
- nominal PC+2 completion when prerequisites are satisfied on time;
- end-to-end ΔP evidence freshness boundaries;
- facilitator/player authority isolation in a deployed-style configuration.

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

A rejoin-safe, phone-accessible, continuously running authoritative mission in which station players receive only their operational information/actions, a separately authorized facilitator controls exercise-wide simulation functions, and source-bounded nonnominal conditions propagate through explicit controller/crew/vehicle/evidence layers without hidden decisions, hidden physical-truth leaks, or invented historical behavior.
