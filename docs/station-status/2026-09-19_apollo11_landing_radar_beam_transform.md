# Station research status — Apollo 11 landing-radar beam transform

Date: 2026-09-19

## GUIDO / guidance-monitoring consequence

Historical readiness improves upstream of any controller product: Apollo 11's landing-radar velocity-beam geometry is now controlled from antenna-frame geometry through the measurement-time navigation-base-to-stable-member transformation.

The LUMINARY 099 path time-tags the five-sample velocity measurement by saving `TIME2,TIME1` and the IMU CDU angles in `RDGIMS`; `VELUPDAT` later restores those saved angles, computes their trig values, and applies `*NBSM*` to the selected navigation-base beam. This closes the previously open dynamic attitude leg without assuming current-time attitude.

This does **not** change GUIDO station maturity or authorize a new exact station display. The downstream estimator/update behavior and ground/controller product cadence remain separate dependencies.

## CONTROL / FLIGHT consequence

None. No new CONTROL or FLIGHT display, callout, threshold, or timing rule is established. The recovered geometry is an onboard guidance/measurement computation dependency, not evidence of a Mission Control presentation.

## Player-facing boundary

Do not expose internal beam vectors, CDU snapshots, `LRVTIME`, or estimator internals as controller-visible telemetry unless a separate source establishes such a product. They may support the causal/historical landing-radar model only.

## Repository consistency

The earlier landing-radar note was assigned 405 inside the already allocated P66/PCR-700 block. That invalid cross-thread allocation was removed; no station claim depends on that note number.

## Evidence status

- **DOCUMENTED:** Apollo-11-effective static landing-radar antenna-position transform.
- **DOCUMENTED:** measurement-time IMU-CDU capture and navigation-base-to-stable-member beam transform used by `VELUPDAT`.
- **PARTIALLY DOCUMENTED:** downstream velocity reasonableness/update estimator.
- **UNRESOLVED:** controller-visible radar/guidance product cadence, synchronization, and formatting.

No station maturity grade changes.
