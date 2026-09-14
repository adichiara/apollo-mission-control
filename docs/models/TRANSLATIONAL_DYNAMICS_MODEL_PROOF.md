# Generic Translational Dynamics Model Proof

Status: **implemented validation model; not historically validated**

## Purpose

This model adds the next reusable causal layer beneath Apollo scenarios:

`supplied propulsion history + mass + inertial thrust direction + optional central gravity -> position + velocity + mass`

It is deliberately mission-neutral. It does not contain Earth, Moon, Apollo 13, PC+2, or any other mission constants.

Implementation:

`src/apollo_mission_control/causal_translational_model.py`

## Why this is separate from PC+2

PC+2 is the current validation anchor, not the simulator's scope boundary (Decision D-021).

A reusable Mission Control simulator needs trajectory consequences for many scenario families: translunar/lunar-orbit maneuvering, descent/ascent, rendezvous, aborts, TEI/LOI-type operations, and entry-support calculations. The first translational layer therefore accepts all mission geometry and gravity parameters from the caller rather than embedding PC+2 assumptions.

## State

The authoritative numerical state contains:

- time, seconds;
- position vector, meters;
- velocity vector, meters/second;
- vehicle mass, kilograms.

No coordinate frame is implied by the code. Scenario/profile documentation must define the frame before historical use.

## Inputs

The model reuses the generic `BurnSegment` propulsion-profile representation:

- duration;
- start thrust;
- optional end thrust for a linear supplied profile;
- inertial thrust direction;
- optional segment-specific effective Isp;
- regime metadata.

The translational configuration adds:

- dry-mass floor;
- optional central gravitational parameter `mu`;
- optional gravity-center position;
- numerical maximum step;
- applicability and provenance.

A zero gravitational parameter gives inertial straight-line/thrust-only propagation.

## Numerical method

The model uses a second-order midpoint integration for position and velocity.

Within each substep:

1. evaluate supplied thrust history;
2. integrate propellant depletion from effective Isp;
3. evaluate gravity and thrust acceleration;
4. estimate midpoint position/velocity;
5. evaluate midpoint acceleration;
6. advance position and velocity.

For a linear thrust segment with constant effective Isp, midpoint thrust integration preserves the exact segment impulse and propellant integral.

This is a modern implementation choice. It is not a claim about LMS, RTCC, AGC, or other Apollo numerical methods.

## Gravity model

Optional gravity is intentionally limited to a single inverse-square central field:

`a = -mu * r / |r|^3`

This is sufficient to test causal coupling between propulsion and trajectory while keeping assumptions explicit.

Not yet modeled:

- third-body gravity;
- rotating frames;
- oblateness;
- atmosphere/aerodynamics;
- finite-body surface contact;
- attitude/gimbal dynamics;
- navigation/filtering error;
- tracking/measurement generation.

Those belong in later layers when selected scenarios require them.

## Validation coverage

Automated tests cover:

- exact zero-gravity straight-line coast;
- thrust-driven position/velocity/mass change;
- linear-thrust impulse and mass invariance across step sizes;
- central-gravity curvature;
- numerical convergence over a synthetic circular orbit;
- gravity-parameter and central singularity rejection.

All tests use synthetic numbers and are not historical validation.

## Historical-use gate

A scenario may use this model historically only after defining from appropriate sources:

- coordinate/reference frame;
- epoch;
- initial position/velocity state;
- applicable central-body parameter and frame origin;
- thrust direction mapping;
- propulsion history/mass-flow treatment;
- required perturbations or proof that they are negligible for the scenario interval;
- comparison target and acceptance tolerance.

The model provides the reusable causal machinery; mission/scenario profiles provide the historically grounded inputs.
