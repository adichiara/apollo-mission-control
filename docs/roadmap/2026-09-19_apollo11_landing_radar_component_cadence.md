# Roadmap addendum — Apollo 11 landing-radar timing boundary

Date: 2026-09-19

## Newly closed

The Apollo 11 AC Electronics guidance/navigation manual directly constrains the onboard landing-radar velocity-update schedule: the three LR velocity components are consumed one per 2-second Average-G/PIPA interval, in the illustrated repeating `Vz → Vx → Vy` sequence.

## Current boundary

Do not use that onboard cadence as a proxy for Mission Control presentation. The following remain distinct:

- LR sensor measurement/noise generation;
- LGC component-read/update schedule — now source-controlled at one component per 2-second navigation interval;
- spacecraft downlink sampling/word-list behavior;
- ground processing/product generation;
- controller display refresh/formatting and operational response.

## Next

The immediate implementation target remains the end-to-end composition already bounded by the flown LUMINARY 099 listing and LM-5 load: measurement-time PIPA/gravity propagation → measurement-time beam transform → residual qualification → historical weighting/correction.

After that, pursue controller-facing timing only through direct Mission G telemetry/downlink/display evidence. Do not invent a two-second GUIDO or MCC refresh rate from the onboard estimator schedule.

Measurement/noise generation remains source-blocked and should stay outside the historical executable profile until directly constrained.

## Evidence status

- **DOCUMENTED:** LGC descent-state-vector LR velocity-component cadence.
- **PARTIALLY DOCUMENTED:** executable end-to-end landing-radar estimator composition.
- **UNRESOLVED:** ground/controller-visible cadence and formatting.
- **UNRESOLVED:** radar measurement/noise generation.
