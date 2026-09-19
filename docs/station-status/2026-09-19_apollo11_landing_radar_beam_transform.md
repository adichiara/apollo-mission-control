# Station research status — Apollo 11 landing-radar estimator chain

Date: 2026-09-19

## GUIDO / guidance-monitoring consequence

Apollo 11's onboard landing-radar velocity path is source-controlled from antenna-frame geometry through measurement-time propagation, residual qualification, and weighted velocity correction. The executable proof now composes propagation → selected-beam reference → qualification → correction, while requiring the selected measurement-time beam explicitly.

The LUMINARY 099 path time-tags the five-sample velocity measurement by saving time, IMU CDU angles, and PIPA values in `RDGIMS`. `VELUPDAT` later restores those values, advances the prior guidance velocity to `LRVTIME`, subtracts lunar-surface rotation, transforms/projects onto the measurement-time beam, tests the residual, and passes accepted data to weighting/update logic.

Primary-source reinspection confirms that historical beam synthesis is not yet executable in the repository: `SETPOS` supplies antenna-to-NB geometry and `*NBSM*` supplies the measurement-time NB-to-SM leg through AGC `AX*SR*T`, but that transform has not yet been independently ported/verified. The composed proof therefore exposes the beam as an explicit dependency rather than guessing a rotation convention.

This improves causal-model completeness but does **not** change GUIDO station maturity or authorize a new exact station display. No source inspected here establishes which onboard intermediate values were presented to Mission Control, their ground update cadence, or their formatting.

## CONTROL / FLIGHT consequence

None. No new CONTROL or FLIGHT display, callout, threshold, or timing rule is established. The estimator chain is an onboard guidance/measurement computation dependency, not evidence of a Mission Control presentation.

## Player-facing boundary

Do not expose internal beam vectors, CDU/PIPA snapshots, `LRVTIME`, gravity terms, lunar-rotation correction, or estimator internals as controller-visible telemetry unless a separate source establishes such a product.

## Evidence status

- **DOCUMENTED:** Apollo-11-effective static landing-radar antenna-position transform semantics and LM-5 load values.
- **DOCUMENTED:** measurement-time IMU-CDU/PIPA capture and NB-to-SM transform semantics used by `VELUPDAT`.
- **DOCUMENTED / IMPLEMENTED:** explicit-input measurement-time velocity propagation, residual qualification, weighting/correction, and composed estimator proof with supplied beam.
- **PARTIALLY IMPLEMENTED:** historical beam synthesis; the AGC transform is not yet independently ported/verified.
- **UNRESOLVED / BLOCKED:** Apollo-11-effective numerical landing-radar measurement-error/noise model.
- **UNRESOLVED:** controller-visible radar/guidance product cadence, synchronization, and formatting.

No station maturity grade changes.
