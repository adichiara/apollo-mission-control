# Progress — Apollo 11 landing-radar velocity estimator/update

Date: 2026-09-19

## Completed

Closed the source logic for both the Apollo-11-effective landing-radar measurement-time velocity estimate and its downstream weighting/correction stage.

The flown LUMINARY 099 `RDGIMS` / `VELUPDAT` path constrains the propagation leg: during the five-sample LR velocity read, `RDGIMS` saves `LRVTIME`, IMU CDUs, and the PIPA snapshot; `VELUPDAT` then forms the measurement-time estimate as the prior guidance velocity plus the saved PIPA-derived increment plus the previous gravity contribution over `LRVTIME - PIPTIME`, and subtracts the lunar-rotation velocity correction before beam projection and residual testing.

The same flown path plus the LM-5 Mission G prelaunch erasable load constrain `LRVMAX`, `LRVF`, the `LRWV*`/`LRWVF*`/`LRWVFF` weights, piecewise weighting behavior, P65/P66/P67 override, update inhibition, and correction along the selected measurement-time beam. Research note 500 records the controlled chain.

## Implementation

The repository now contains:

- `landing_radar_propagation.py` — mission-neutral measurement-time propagation with explicit prior velocity, PIPA delta-V, previous gravity, elapsed time, and lunar-surface-velocity inputs;
- `landing_radar_reference.py` — source-bounded surface-relative beam projection;
- `landing_radar_velocity_update.py` — generic weighting/correction model with historical constants supplied by profile;
- `landing_radar_profiles.py` — historical profile loader and Apollo 11 LM-5 weighting metadata;
- unit/profile/API/browser-contract coverage for the previously implemented stages, plus direct unit coverage for propagation.

The propagation module deliberately accepts the PIPA increment and previous gravity as inputs. It does not synthesize a gravity field, PIPA behavior, radar noise, or measurements.

## Next implementation boundary

Compose the propagation result with the already source-controlled LM-5 measurement-time antenna/CDU beam transform, residual qualification, and historical weighting/correction into one model-proof path. Preserve each intermediate quantity and provenance so the Causal Model Lab can show the causal chain without presenting onboard internals as Mission Control telemetry.

Landing-radar measurement generation/error behavior remains **BLOCKED** on a flight-effective numerical error model. Controller-visible product cadence/formatting remains a separate unresolved evidence problem.
