# Station research status — Apollo 11 landing-radar beam transform

Date: 2026-09-19
Research: 405

## GUIDO / guidance-monitoring consequence

Historical readiness improves upstream of any controller product: Apollo 11's static landing-radar antenna-position beam transform is now controlled by the LUMINARY 099 listing, Memo #95 orientation convention, LM-5 prelaunch pad-load angles, and final-program constants.

This does **not** change GUIDO station maturity or authorize a new exact station display. The remaining dynamic IMU-CDU/reference-frame transformation, estimator/filter behavior, and ground/controller product cadence are not closed by this step.

## CONTROL / FLIGHT consequence

None. No new CONTROL or FLIGHT display, callout, threshold, or timing rule is established. The recovered geometry is an onboard guidance/measurement computation dependency, not evidence of a Mission Control presentation.

## Player-facing boundary

Do not expose the recovered internal beam vectors or angle values as controller-visible telemetry unless a separate source establishes such a product. The values may support the causal/historical landing-radar model only.

## Evidence status

- **DOCUMENTED:** Apollo-11-effective static landing-radar antenna-position transform.
- **PARTIALLY DOCUMENTED:** dynamic velocity-measurement attitude/reference-frame transform.
- **UNRESOLVED:** controller-visible radar/guidance product cadence, synchronization, and formatting.

No station maturity grade changes.
