# Station research status — Apollo 11 landing-radar estimator chain

Date: 2026-09-19

## GUIDO / guidance-monitoring consequence

Historical readiness improves upstream of any controller product. Apollo 11's landing-radar velocity path is source-controlled from antenna-frame geometry through the measurement-time navigation-base-to-stable-member transformation, measurement-time guidance-velocity propagation, residual qualification, and downstream weighted velocity correction.

The LUMINARY 099 path time-tags the five-sample velocity measurement by saving `TIME2,TIME1`, IMU CDU angles, and PIPA values in `RDGIMS`. `VELUPDAT` later restores those values, advances the prior guidance velocity to `LRVTIME` with the PIPA-derived increment and previous gravity contribution, subtracts lunar-rotation velocity, transforms/projects onto the measurement-time beam, tests the residual, and passes accepted data to the weighting/update logic.

The measurement-time propagation leg is now executable as a mission-neutral explicit-input stage. This improves causal-model completeness but does **not** change GUIDO station maturity or authorize a new exact station display. No source inspected here establishes which onboard intermediate values were presented to Mission Control, their ground update cadence, or their formatting.

## CONTROL / FLIGHT consequence

None. No new CONTROL or FLIGHT display, callout, threshold, or timing rule is established. The recovered estimator chain is an onboard guidance/measurement computation dependency, not evidence of a Mission Control presentation.

## Player-facing boundary

Do not expose internal beam vectors, CDU/PIPA snapshots, `LRVTIME`, gravity terms, lunar-rotation correction, or estimator internals as controller-visible telemetry unless a separate source establishes such a product. They may support the causal/historical landing-radar model only.

## Evidence status

- **DOCUMENTED:** Apollo-11-effective static landing-radar antenna-position transform.
- **DOCUMENTED:** measurement-time IMU-CDU/PIPA capture and navigation-base-to-stable-member beam transform used by `VELUPDAT`.
- **DOCUMENTED:** measurement-time velocity propagation logic and explicit-input executable propagation stage.
- **DOCUMENTED:** downstream residual qualification and Apollo-11-effective velocity weighting/correction logic.
- **PARTIALLY DOCUMENTED:** executable end-to-end composition of those controlled stages.
- **UNRESOLVED / BLOCKED:** Apollo-11-effective numerical landing-radar measurement-error/noise model.
- **UNRESOLVED:** controller-visible radar/guidance product cadence, synchronization, and formatting.

No station maturity grade changes.
