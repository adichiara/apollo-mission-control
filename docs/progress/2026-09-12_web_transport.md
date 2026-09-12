# Progress — first playable web transport

Date: 2026-09-12

## Completed transport foundation

- Selected **FastAPI + Uvicorn** while keeping simulation/session logic framework-neutral.
- Added phone-first player client, facilitator/SimSup console, Render scaffolding, health endpoint, and API tests.
- Added idempotent same-player/same-station rejoin and browser identity persistence.
- Added 1× monotonic realtime GET pacing while `RUNNING`; manual `/advance` remains validation-only.

## Continuous mission clock

Decision **D-016** establishes that controller decisions do not stop mission time. Nominal events use prerequisites, missed events are recorded rather than replayed, and explicit game/session pause is the ordinary clock stop.

## First nonnominal web/session path

The source-bounded synthetic ΔP path reaches controller evidence end to end:

`source injection → CONTROL projection/rule → CONTROL decision → CAPCOM queue/transmission → crew receipt → crew shutdown command → physical DPS response → crew report / fresh GQ6510P observation → CONTROL evidence aggregation`

No stage silently implies the next, stale pressure cannot count as post-command evidence, no pressure magnitude is an engine-off threshold, and evidence assessment does not inspect hidden `engine_running` truth.

See research notes 085–086.

## Player/facilitator boundary

UI separation is complete:

- `/` is the normal station client;
- `/admin` is the facilitator/SimSup validation interface.

Server-side authority is also now implemented. When `APOLLO_FACILITATOR_TOKEN` is configured, exercise-wide operations require `X-Apollo-Facilitator`.

Protected operations include session create/reset/lifecycle, manual validation time, source injection, validation crew/vehicle response, and global audit access. Controller station actions remain independent from facilitator credentials.

Render generates the deployment secret through `render.yaml`; no secret value is stored in source. Render fails closed if the secret is unexpectedly missing.

This is a modern software protection mechanism. Primary NASA sources support the organizational separation of Simulation Supervisor/simulation control from flight controllers, not an Apollo-era authentication method.

See research note 088 and decision D-017.

## Deployment boundary

The server still holds one authoritative session in process memory. One worker is required; restart/redeploy/spin-down loses the live game. Durable persistence and multiple concurrent sessions remain deferred.

Realtime pacing is fixed at **1×**. Time acceleration remains undecided.

## Test status

HTTP/domain tests are committed, including crew response, shutdown evidence, player/admin UI separation, and facilitator authority. The complete suite is **not recorded as passing** because this automation environment does not provide a checked-out runnable repository execution path.

## Current stopping point

Runnable multi-client integration validation:

1. execute the full suite in a runnable environment;
2. exercise several station clients plus one facilitator console against one server;
3. validate realtime polling/actions, facilitator pause/resume, reload/rejoin, station isolation, and authority isolation;
4. run the complete synthetic ΔP branch through the live browser/API path;
5. repair usability/integration problems exposed by realtime play;
6. reopen historical research only if integrated play exposes a concrete information or decision gap.
