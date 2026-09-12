# Station research-status addendum — PC+2 DPS shutdown confirmation

Date: 2026-09-12

## CONTROL

**Maturity remains B.**

Improved:

- `GQ6510P` chamber pressure is now explicitly treated as a possible fresh post-command ground evidence channel for DPS response;
- pre-command pressure observations cannot be reused as shutdown evidence;
- no unsupported engine-off pressure threshold is imposed.

Still unresolved:

- exact Apollo 13 CONTROL CRT field/routing for GQ6510P;
- exact shutdown-confirmation latency;
- exact LM-7 shutdown pressure trace;
- whether a dedicated engine-off discrete was displayed to CONTROL.

## CAPCOM

**Maturity remains B.**

Improved:

- the crew's actual PC+2 “Shutdown” report is represented as a distinct communication event;
- a crew report does not mutate physical engine state or ground telemetry.

## FLIGHT

**Maturity remains B.**

Improved:

- shutdown evidence can now arrive through multiple channels rather than as one omniscient state flag;
- later FLIGHT/controller interpretation can use crew report and ground measurement independently.

## Research stop condition

The minimum information architecture is adequate. Exact display reconstruction and pressure thresholds are not prerequisites for the vertical slice unless a later decision specifically requires them.
