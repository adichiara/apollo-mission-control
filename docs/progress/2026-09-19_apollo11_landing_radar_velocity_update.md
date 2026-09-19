# Progress — Apollo 11 landing-radar velocity estimator/update

Date: 2026-09-19

## Completed

Closed the source logic for both the Apollo-11-effective landing-radar measurement-time velocity estimate and its downstream weighting/correction stage.

The flown LUMINARY 099 `RDGIMS` / `VELUPDAT` path now constrains the previously open propagation leg: during the five-sample LR velocity read, `RDGIMS` saves `LRVTIME`, IMU CDUs, and the PIPA snapshot; `VELUPDAT` then forms the measurement-time estimate as the prior guidance velocity plus the saved PIPA-derived increment plus the previous gravity contribution over `LRVTIME - PIPTIME`, and subtracts the lunar-rotation velocity correction before beam projection and residual testing.

The same flown path plus the LM-5 Mission G prelaunch erasable load constrain:

- `LRVMAX = 2000 ft/s`;
- `LRVF = 200 ft/s`;
- `LRWVZ/Y/X = 0.3`;
- `LRWVFZ/Y/X = 0.2`;
- `LRWVFF = 0.1`;
- piecewise low-speed / linear / zero-weight behavior;
- P65/P66/P67 override to `LRWVFF`;
- update-inhibit bypass;
- vector correction along the selected measurement-time velocity beam.

Research note 500 records the controlled chain.

## Implementation already present in this PR

Added:

- `landing_radar_velocity_update.py` — generic weighting/correction model with no Apollo constants;
- `landing_radar_profiles.py` — historical profile loader;
- Apollo 11 profile weighting metadata and source values;
- historical profile/model-proof endpoints;
- Causal Model Lab stage for historical weighting/correction;
- unit, profile, API, and browser-contract tests.

The Causal Model Lab keeps upstream quality inputs visibly separate from the historical downstream weighting profile; synthetic quality inputs are not promoted to historical evidence.

## Next implementation boundary

The historical propagation equation is now source-controlled, but not yet composed in executable code. Next:

1. implement a mission-neutral measurement-time propagation stage with explicit inputs for prior guidance velocity, PIPA-derived increment, previous gravity contribution/time delta, and lunar-rotation correction;
2. compose it with the already controlled LM-5 antenna / measurement-time CDU beam transform;
3. feed that result into the existing residual qualification and weighting/correction stages.

Do not invent a standalone lunar gravity field, PIPA error/noise model, or measurement noise merely to complete the chain. Landing-radar measurement generation/error behavior and controller-visible product cadence/formatting remain separate unresolved evidence problems.
