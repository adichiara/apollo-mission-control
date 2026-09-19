# Roadmap addendum — Apollo 11 landing-radar timing and measurement boundary

Date: 2026-09-19

## Newly closed

The Apollo 11 AC Electronics guidance/navigation manual directly constrains the onboard landing-radar velocity-update schedule: the three LR velocity components are consumed one per 2-second Average-G/PIPA interval, in the illustrated repeating `Vz → Vx → Vy` sequence.

NASA TN D-6849 constrains the error boundary: an LM-5 preflight one-count velocity bias was corrected before flight and a Gaussian assumption used for Doppler-spectrum-simulator test limits required correction because the test approximation produced heavier tails. Apollo 11 flight data were reported within specification limits apart from low/near-zero-Doppler behavior, but the recovered source does not supply a numerical flight-effective stochastic distribution.

The flown LUMINARY 099 `VELUPDAT` propagation equation is now represented by a mission-neutral executable stage: prior guidance velocity + caller-supplied PIPA delta-V + caller-supplied previous-gravity contribution to the LR epoch, followed by lunar-surface velocity subtraction. No independent gravity, PIPA, or noise model is inferred.

## Current boundary

Keep distinct:

- LR sensor measurement/error generation — historical stochastic generation is **BLOCKED**, not free to assume Gaussian noise;
- LGC component-read/update schedule — source-controlled at one component per 2-second navigation interval;
- onboard measurement-time propagation — source-controlled and now executable as an explicit-input stage;
- spacecraft downlink sampling/word-list behavior;
- ground processing/product generation;
- controller display refresh/formatting and operational response.

## Next

Compose the executable propagation stage with the source-controlled LM-5 measurement-time beam transform, residual qualification, and historical weighting/correction into one model-proof path. Preserve source boundaries at every stage.

Synthetic perturbations may be injected for tests/scenarios only when labeled synthetic rather than historical. Reopen historical stochastic LR generation only if an LM-5 end-item specification, qualification/acceptance report, applicable performance specification, or sufficiently resolved Apollo 11 flight-data source supplies the missing error model.

After composition, pursue controller-facing timing only through direct Mission G telemetry/downlink/display evidence. Do not invent a two-second GUIDO or MCC refresh rate from the onboard estimator schedule.

## Evidence status

- **DOCUMENTED:** LGC descent-state-vector LR velocity-component cadence.
- **DOCUMENTED:** measurement-time velocity propagation semantics and executable explicit-input propagation stage.
- **DOCUMENTED:** LM-5 preflight one-count velocity bias was corrected; the Doppler-simulator Gaussian test-limit assumption required correction for heavier tails.
- **PARTIALLY DOCUMENTED:** executable end-to-end landing-radar estimator composition.
- **UNRESOLVED:** ground/controller-visible cadence and formatting.
- **UNRESOLVED / BLOCKED:** Apollo-11-effective numerical stochastic radar measurement-error distribution.
