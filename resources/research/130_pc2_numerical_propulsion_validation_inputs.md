# PC+2 numerical propulsion validation inputs

Date: 2026-09-14  
Status: **source-bounded first-model input inventory; implementation not yet frozen**

## Purpose

Before implementing the first causal propulsion/dynamics slice, collect the source-backed values that can serve as model inputs or regression targets and separate them from values that remain uncertain.

The historical Apollo 13 PC+2 burn is useful because it provides a real long-duration docked DPS maneuver with known timing, throttle staging, vehicle weights, guidance velocity components, and postburn evidence.

## Apollo 13 PC+2 execution facts

Current project/source research establishes:

- ignition GET: 79:27:38.30;
- actual cutoff GET: 79:32:02.12;
- actual elapsed burn time: approximately 263.82 s;
- low-thrust start for approximately 5 s;
- then approximately 40 percent thrust;
- maximum-thrust segment for most of the remaining burn;
- executed PGNS velocity components: +742.21, -425.88, +91.04 ft/s;
- magnitude of those executed PGNS components: approximately 860.55 ft/s;
- planned PAD resultant Delta-V: 861.5 ft/s;
- existing scenario-fixture weights: CSM 62,480 lb and LM 33,452 lb;
- combined fixture weight: 95,932 lb.

Apollo 13 flight-operations reporting also describes the burn as approximately:

- 12.6 percent thrust for 5 s;
- 40 percent thrust for 21 s;
- 235 s at maximum thrust.

Those rounded segment durations total 261 s, which is shorter than the documented 263.82 s actual burn duration. The first model must **not** silently force those prose durations to be an exact piecewise-complete thrust history. Startup/ramp/transient timing, rounding, or source-description simplification must be resolved or explicitly modeled as uncertainty.

## DPS engineering values

NASA TN D-7143, *Apollo Experience Report — Descent Propulsion System*, gives basic descent-engine design requirements including:

- 10:1 throttling ratio;
- maximum rated thrust: 10,500 lbf;
- gimbal capability: plus/minus 6 degrees in Y and Z;
- pressure-fed engine;
- nitrogen tetroxide oxidizer;
- 50 percent UDMH / 50 percent hydrazine fuel;
- design specific impulse at end of duty cycle: 305 lbf-s/lbm.

Apollo 13-specific Review Board material describes the operational DPS as:

- throttleable from about 1,050 lbf to 6,300 lbf;
- throttle settings above that region automatically producing full thrust;
- nominal full thrust: 9,870 lbf;
- gimbal trim available through PGNS or AGS;
- manual thrust control able to override commanded thrust upward.

The 10,500-lbf engineering design rating and 9,870-lbf Apollo 13 nominal full-thrust value must therefore remain distinct. We should not choose one merely because it makes a regression result fit better.

## First-model state and inputs

A minimal propulsion/translational proof can use:

State:
- time;
- vehicle mass;
- inertial or explicitly defined working-frame velocity;
- position if trajectory propagation is included in the same step.

Inputs:
- engine command state;
- throttle command / effective thrust;
- thrust direction;
- vehicle attitude or externally supplied thrust vector;
- propulsion configuration needed to determine whether commanded thrust is physically available.

Parameters:
- mission/profile-specific full-thrust value;
- throttle mapping;
- specific impulse or mass-flow relationship;
- initial mass;
- gravity model if position/trajectory propagation is enabled.

Outputs:
- actual thrust;
- propellant mass flow;
- integrated impulse;
- mass remaining;
- vector Delta-V;
- updated velocity/position;
- engine state.

## Regression strategy

The model should have two levels of validation.

### Propulsion-only regression

With gravity/trajectory temporarily excluded, integrate a sourced thrust history against a sourced starting mass and verify:

- monotonic mass depletion;
- scalar impulse;
- vector Delta-V behavior;
- early/late cutoff ordering;
- throttle-error ordering;
- numerical convergence as timestep is reduced.

This does **not** need to reproduce the historical PC+2 Delta-V exactly until the thrust history and mass reference are sufficiently constrained.

### Historical maneuver regression

Once the source boundary is tighter, use the Apollo 13 burn as an end-to-end numerical check.

The model result should be compared to:

- executed PGNS velocity-component magnitude (~860.55 ft/s);
- planned resultant 861.5 ft/s;
- known burn timing;
- postburn residual/trajectory evidence.

A mismatch should trigger source/model diagnosis, not manual tuning of an arbitrary correction factor.

## Important current discrepancy

A naive piecewise calculation using:

- 95,932 lb starting combined weight;
- 9,870 lbf full thrust;
- 305 s specific impulse;
- 5 s at 12.6 percent;
- 21 s at 40 percent;
- 235 s at full thrust;

does not exactly reproduce the documented executed Delta-V.

That is expected at this stage and is useful. It demonstrates why the first model must preserve source provenance and expose assumptions rather than calibrate itself to one historical number.

Likely factors to research before freezing the validation case include:

- exact throttle/transient time history rather than rounded prose segments;
- exact mass epoch represented by the PAD weights;
- actual mission engine performance versus nominal full-thrust rating;
- guidance-frame/component definitions;
- whether reported velocity components include effects not represented by the naive isolated-thrust calculation;
- pressurization/blowdown details near cutoff;
- any gimbal/attitude effects relevant to vector magnitude/components.

## Next source targets

1. Extract Grumman LED 500-5 equations of motion and subsystem interfaces.
2. Extract the LMS 50 ms integration-step memo.
3. Recover the exact LMS/FMES LGC math-model material where possible.
4. Extract the Apollo 13/LM-7 DPS thrust/throttle and propellant-performance pages needed for PC+2.
5. Trace the 62,480-lb CSM and 33,452-lb LM PAD weights to their exact primary-source page/epoch.
6. Recover enough state-vector/trajectory information to move from maneuver Delta-V validation to postburn trajectory propagation.

## Source boundary

No new simulator constants are frozen by this note. It is an input/validation inventory.

Primary source families currently used:

- Apollo 13 Flight Operations / Mission Operations reporting;
- Apollo 13 Review Board material;
- NASA TN D-7143, *Apollo Experience Report — Descent Propulsion System*;
- existing PC+2 source chain and scenario fixture.

See also research notes 127–129 and docs/CAUSAL_SIMULATION_ENGINE.md.
