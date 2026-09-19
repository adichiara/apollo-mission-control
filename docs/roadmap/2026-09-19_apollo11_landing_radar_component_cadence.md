# Roadmap addendum — Apollo 11 landing-radar timing and measurement boundary

Date: 2026-09-19

## Newly closed

The Apollo 11 AC Electronics guidance/navigation manual directly constrains the onboard landing-radar velocity-update schedule: the three LR velocity components are consumed one per 2-second Average-G/PIPA interval, in the illustrated repeating `Vz → Vx → Vy` sequence.

The next measurement-error search further constrains the model. NASA TN D-6849 records that an LM-5 preflight one-count velocity bias was corrected before flight and that a Gaussian assumption used for Doppler-spectrum-simulator test limits required correction because the test approximation produced heavier tails. The Apollo 11 flight data were reported within specification limits apart from low/near-zero-Doppler behavior, but the recovered source does not supply a numerical flight-effective stochastic distribution.

## Current boundary

Do not use onboard cadence as a proxy for Mission Control presentation. Keep distinct:

- LR sensor measurement/error generation — a historical stochastic generator is now **BLOCKED**, not free to assume Gaussian noise;
- LGC component-read/update schedule — source-controlled at one component per 2-second navigation interval;
- spacecraft downlink sampling/word-list behavior;
- ground processing/product generation;
- controller display refresh/formatting and operational response.

## Next

The immediate implementation target remains the end-to-end composition already bounded by the flown LUMINARY 099 listing and LM-5 load: measurement-time PIPA/gravity propagation → measurement-time beam transform → residual qualification → historical weighting/correction.

Synthetic perturbations may be injected for tests/scenarios only when labeled synthetic rather than historical. Reopen historical stochastic LR generation only if an LM-5 end-item specification, qualification/acceptance report, applicable performance specification, or sufficiently resolved Apollo 11 flight-data source supplies the missing error model.

After composition, pursue controller-facing timing only through direct Mission G telemetry/downlink/display evidence. Do not invent a two-second GUIDO or MCC refresh rate from the onboard estimator schedule.

## Evidence status

- **DOCUMENTED:** LGC descent-state-vector LR velocity-component cadence.
- **DOCUMENTED:** LM-5 preflight one-count velocity bias was corrected; the Doppler-simulator Gaussian test-limit assumption required correction for heavier tails.
- **PARTIALLY DOCUMENTED:** executable end-to-end landing-radar estimator composition.
- **UNRESOLVED:** ground/controller-visible cadence and formatting.
- **UNRESOLVED / BLOCKED:** Apollo-11-effective numerical stochastic radar measurement-error distribution.
