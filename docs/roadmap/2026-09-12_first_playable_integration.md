# Roadmap addendum — first playable PC+2 integration

Date: 2026-09-12  
Status: **CURRENT — automated/network multi-client validation artifacts implemented; actual suite/deployment/phone execution is next**

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
- [x] destructive real-network multi-client smoke runner for dedicated validation deployments;
- [x] admin UI evidence-class values reconciled with the server enum;
- [x] stale pre-authorization UI contract assertion repaired.

The deployment remains single-process/in-memory. Restart/redeploy loses the live session; multiple workers/sessions and durable persistence remain deferred.

See decisions D-016–D-017 and research notes 084–089.

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

`tests/test_web_multiclient_integration.py` now protects the in-process contract for:

- shared authoritative state across independent clients;
- station-scoped operational information;
- same-player/same-station rejoin;
- occupied-station and station-switch rejection;
- facilitator authority isolation;
- explicit pause semantics;
- complete synthetic ΔP propagation and evidence ordering.

`scripts/pc2_multiclient_smoke.py` carries the same checks into a real HTTP environment and adds simultaneous station polling.

Neither artifact is recorded as executed/passing in this automation environment.

## Active priority — execute runnable validation

1. execute the complete domain/session/API test suite in a checked-out runtime;
2. run `scripts/pc2_multiclient_smoke.py` against a dedicated local/Render instance;
3. run one facilitator console plus several simultaneous real phone station clients;
4. verify realtime GET under concurrent polling/actions and real network latency;
5. verify facilitator pause/resume, player reload/rejoin, and station information isolation on actual browsers;
6. repair usability/integration problems exposed by live multi-client operation;
7. reopen historical research only if integrated play exposes a concrete missing procedure or information dependency.

## Integration validation still required

Covered by automated contract tests but still requiring actual execution in a runnable environment:

- reload/rejoin state preservation;
- station information isolation;
- explicit pause as the normal clock stop;
- end-to-end ΔP evidence boundaries;
- facilitator/player authority isolation.

Still requiring live/deployed validation:

- full-suite execution;
- real concurrent HTTP polling/actions;
- real phone/browser reload/rejoin;
- continuous GET behavior under network latency;
- phone readability and action ergonomics;
- nominal PC+2 completion in a full live playthrough;
- missed-event behavior during real late-controller decisions.

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

A rejoin-safe, phone-accessible, continuously running authoritative mission in which station players receive only their operational information/actions, a separately authorized facilitator controls exercise-wide simulation functions, and source-bounded nonnominal conditions propagate through explicit controller/crew/vehicle/evidence layers without hidden decisions, hidden physical-truth leaks, or invented historical behavior—validated both by automated contracts and an actual multi-device network run.
