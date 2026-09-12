# 087 — Player client / validation-admin separation

Date: 2026-09-12  
Status: **IMPLEMENTED — UI responsibility boundary clarified**

## Question

Now that the PC+2 prototype has continuous realtime pacing plus source injection, crew-response, vehicle-response, and audit endpoints, which controls belong in an ordinary controller phone client and which belong only in a validation/SimSup-facing interface?

## Decision

The ordinary player client must expose only station identity, station-visible products, and station-authorized controller actions.

Validation and session-administration controls are moved to a separate `/admin` console.

This is a **UI responsibility boundary**, not a security or authentication boundary. The current prototype still has no production authentication/authorization layer.

## Player client (`/`)

The player-facing root now contains:

- player/station join and idempotent rejoin;
- station-scoped presentation data;
- station readiness reporting;
- FLIGHT GO/NO-GO and CAPCOM queue operations when assigned FLIGHT;
- CONTROL ground-callout and shutdown-evidence assessment when assigned CONTROL;
- CAPCOM transmission of approved queue items when assigned CAPCOM;
- continuous GET/status display.

It deliberately omits:

- session create/reset;
- session start/pause/resume;
- manual GET jumps;
- SimSup/source injection;
- explicit crew-receipt/shutdown validation operations;
- direct physical vehicle-response controls;
- global audit-log inspection.

## Validation admin console (`/admin`)

The separate development/SimSup console includes:

- create/reset/start/pause/resume;
- manual GET advancement retained for test setup;
- explicit source-state injection;
- explicit crew receipt;
- explicit crew shutdown command;
- explicit crew shutdown report;
- explicit physical DPS engine-off response;
- CONTROL shutdown-evidence inspection;
- audit-log inspection.

These controls exist to exercise source-bounded integration layers independently. Their presence in the admin harness does not make them player-facing game actions.

## Architectural reason

The simulation already separates:

`authoritative state → controller-visible products → player decisions/actions`

from:

`scenario injection / validation / physical-response administration`.

The browser architecture should preserve that same separation. Putting manual time, source injection, physical vehicle response, and audit controls on every controller phone would leak implementation/SimSup authority into the player experience even if the underlying API remained correctly layered.

## Security boundary

None is claimed yet.

The `/admin` route is merely a separate interface. Its API operations are still reachable to any client that knows the endpoints. Production authentication, facilitator identity, and server-side authorization remain future work.

## Validation

`tests/test_web_client_role_separation.py` checks that:

- `/` omits validation/admin controls;
- `/admin` exposes them;
- the admin page explicitly states that the split is not an authentication boundary.

## Next boundary

The next useful integration step is facilitator/session authorization rather than more UI archaeology:

1. define minimum facilitator/admin authority separately from controller station identity;
2. protect validation/admin operations server-side without affecting station-scoped player information;
3. keep SimSup/scenario-authoring functions separable from ordinary session administration where practical;
4. then run the complete multi-client smoke path in a runnable deployment.
