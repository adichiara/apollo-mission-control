# Progress — Apollo 11 landing-radar velocity weighting/update

Date: 2026-09-19

## Completed

Closed and implemented the Apollo-11-effective landing-radar velocity weighting/correction stage after upstream residual qualification.

The flown LUMINARY 099 `VUPDAT` path and the LM-5 Mission G prelaunch erasable load together constrain:

- `LRVMAX = 2000 ft/s`;
- `LRVF = 200 ft/s`;
- `LRWVZ/Y/X = 0.3`;
- `LRWVFZ/Y/X = 0.2`;
- `LRWVFF = 0.1`;
- piecewise low-speed / linear / zero-weight behavior;
- P65/P66/P67 override to `LRWVFF`;
- update-inhibit bypass;
- vector correction along the selected measurement-time velocity beam.

Research note 500 records the source chain and claims the new `apollo11-landing-radar` 500-series research block.

## Implementation

Added:

- `landing_radar_velocity_update.py` — generic weighting/correction model with no Apollo constants;
- `landing_radar_profiles.py` — historical profile loader;
- Apollo 11 profile weighting metadata and source values;
- historical profile/model-proof endpoints;
- Causal Model Lab stage for historical weighting/correction;
- unit, profile, API, and browser-contract tests.

The Causal Model Lab keeps upstream quality inputs visibly separate from the historical downstream weighting profile; synthetic quality inputs are not promoted to historical evidence.

## Remaining estimator boundary

Still not integrated end-to-end:

1. PIPA increment + lunar-gravity propagation to the landing-radar measurement time;
2. executable application of the already source-controlled LM-5 antenna / measurement-time CDU transform;
3. measurement generation/error behavior;
4. controller-visible product cadence/formatting.

The next implementation step is the first two items as a composed measurement-time estimator path. Controller products remain a separate evidence problem.
