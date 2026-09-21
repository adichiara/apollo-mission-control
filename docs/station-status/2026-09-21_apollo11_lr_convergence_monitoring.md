# Station-status addendum — Apollo 11 LR convergence monitoring

Date: 2026-09-21
Parent: `docs/STATION_RESEARCH_STATUS.md`

Historical Apollo 13 station maturity grades remain unchanged. This addendum concerns the Apollo 11 reference descent.

## FLIGHT / flight-control team

NASA TM X-58040 establishes a real-time **ground flight-controller monitoring role** for descent altitude and altitude rate and states that, because of communications delay, ground controllers could only advise based on projected trends. This supports a player-facing ground-monitoring function at the team level.

It does not, by itself, assign each LR comparison or convergence declaration to FLIGHT, GUIDO, FIDO, or a support-room position.

## GUIDO

The prior mission-rule research establishes guidance/LR decision inputs relevant to the powered descent, but the new source does not identify a GUIDO-specific CRT or voice call. Therefore GUIDO's exact Apollo 11 LR-convergence presentation/call workflow remains **PARTIAL / UNRESOLVED**.

## Reference evidence available to implementation

Apollo 11 postflight anchors may be represented without inventing station routing:

- LR lock/data good near 37,000 ft;
- initial Δh about -2,200 ft;
- altitude-data incorporation near 31,600 ft after monitoring and no limit violation;
- Δh convergence to about 100 ft within 30 seconds;
- velocity updates beginning near 29,000 ft;
- continued altitude/altitude-rate monitoring toward P64.

These are observed Apollo 11 sequence facts, not generic thresholds.

## Remaining station question

Recover a primary source that identifies the station/speaker and call sequence around LR acceptance/convergence and the GO for landing. Until then, do not encode an invented `GUIDO converged → FLIGHT GO` protocol merely because it is operationally plausible.

## Evidence status

- **DOCUMENTED:** ground flight controllers monitored altitude and altitude rate and advised from projected trends.
- **DOCUMENTED:** Apollo 11 LR convergence sequence at postflight-analysis resolution.
- **UNRESOLVED:** exact front-room station ownership, CRT product, and call workflow.