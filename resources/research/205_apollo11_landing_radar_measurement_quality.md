# 205 — Apollo 11 landing-radar measurement qualification boundary

## Purpose

Extend the Apollo 11 second-reference architecture from a simple radar-update eligibility gate to the upstream measurement-qualification stage, without implementing radar hardware or inventing LM-5 measurement noise.

## Primary-source findings

Apollo 11 guidance documentation distinguishes hardware/data-quality persistence, reasonableness testing, crew update approval, and guidance-state conditions.

For landing-radar state-vector updating, the Apollo 11 guidance material specifies:

- Landing Radar Data Good must have been present for **at least 4 seconds** before either range or velocity data are used for updating.
- For range updating, the landing-radar range scale must not have changed within the **last 1 second**.
- Range updating requires estimated LM altitude below **50,000 ft**.
- Velocity updating requires estimated LM speed below **2,000 ft/s**.
- Astronaut approval for radar updating is required.
- Range reasonableness uses an affine residual limit with a **200-ft fixed term plus 0.125 times the estimated altitude**.
- Velocity reasonableness uses a **7.5-ft/s fixed term plus a 0.125 proportional term** applied to the guidance-defined radar-axis velocity reference quantity.

The Apollo 11 Mission Report event table separately records when landing-radar data became good and when updates were enabled.

Sources:

- AC Electronics Apollo 11 guidance/navigation manual, *Lunar Descent State Vector Update Routine*.
- MIT Instrumentation Laboratory R-700 Volume II, landing-radar reasonableness-test discussion.
- NASA *Apollo 11 Mission Report*, November 1969.

## Architecture consequence

The chain is now explicitly:

`raw radar channels + Data Good history -> measurement qualification -> update enable/trajectory gates -> estimator -> guidance state`

The existing `landing_radar_model.py` remains the downstream update-eligibility gate.

The new `landing_radar_quality.py` supplies a reusable upstream mechanism for:

- Data Good persistence;
- channel validity;
- range-scale stability;
- affine residual reasonableness tests.

It contains no Apollo constants.

## Apollo 11 profile

`data/landing_radar_profiles/apollo11_lm5_landing_radar_partial.json` records the historical Apollo 11 values in source units.

The generic quality model can directly represent the Data Good persistence, range-scale stability, and affine residual form.

The profile does **not** yet claim a complete executable LM-5 radar model because the velocity reasonableness equation depends on an upstream radar-axis reference quantity whose exact coordinate computation is not yet implemented in the simulator.

## Deliberate exclusions

This pass does not implement:

- radar beam geometry or lunar terrain intersection;
- false-lock/sidelobe physics;
- measurement noise or bias generation;
- the Apollo estimator/filter weighting equations;
- exact guidance-cycle cadence;
- automatic state-vector correction;
- controller display generation.

## Model-readiness consequence

The Apollo 11 `landing_radar` domain remains **partial**, but the missing behavior is narrowed from a broad "measurement model" gap to specific upstream geometry/reference and downstream estimator/cadence work.
