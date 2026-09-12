# Progress Log — 2026-09-12 — PC+2 inlet-pressure follow-on

Continuation of the PC+2 implementation progress logs.

## Research completed

After completing the generic timed scenario-injection layer, the next candidate rule path was selected by primary-source strength rather than convenience: DPS inlet pressure.

Research note `057_pc2_dps_inlet_pressure_observation_path.md` establishes:

- the PC+2 ground criterion was stated as **engine inlet pressure =/≤150 psi on the ground**;
- the crew/onboard threshold was 160 psi;
- Apollo 13's LM-7 family had two distinct engine-interface pressure measurements:
  - `GQ3611P` — fuel interface pressure;
  - `GQ4111P` — oxidizer interface pressure;
- LM-7 checkout documentation independently confirms both transducer identities.

## Deliberate stop condition

The reviewed primary sources do **not** yet establish how the singular ground “engine inlet pressure” rule was formed from the two interface measurements.

The project therefore did not implement any of these unsupported assumptions:

- either leg ≤150 psi;
- minimum(fuel, oxidizer) ≤150 psi;
- average pressure ≤150 psi;
- selected/derived single value without source evidence.

`ground_inlet_pressure` remains `NOT_EVALUABLE` in the rule engine.

## Repository maintenance

- Added `resources/research/057_pc2_dps_inlet_pressure_observation_path.md`.
- Added `resources/source-catalog/PC2_INLET_PRESSURE_SOURCES.md`.
- Added `docs/station-status/2026-09-12_pc2_inlet_pressure.md`.
- CONTROL remains maturity B.

## Current stopping point

The next highest-value evidence target is exact CONTROL display/limit logic or a procedure defining how `GQ3611P` and `GQ4111P` fed the singular 150-psi PC+2 ground criterion.

If that mapping cannot be found cheaply in primary material, the project should not infer it. The alternate next research branch is fuel/oxidizer differential pressure, where the same two source measurements may contribute but the exact ground delta-P calculation still needs documentation.
