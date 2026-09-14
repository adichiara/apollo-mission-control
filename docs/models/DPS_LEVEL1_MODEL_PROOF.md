# DPS Level-1 Causal Model Proof

Status: **implemented validation model; not historically validated**

## Purpose

This model proves that a single deterministic calculation can produce different maneuver consequences from different duration, thrust, and direction inputs. It is framework-neutral and does not replace the existing PC+2 scenario state.

The implementation is in `src/apollo_mission_control/causal_dps_model.py`.

## Inputs and units

All values use SI units.

- initial time, seconds;
- initial vehicle mass, kilograms;
- initial three-component velocity, meters/second;
- dry-mass floor, kilograms;
- specific impulse, seconds;
- one or more constant-command burn segments:
  - duration, seconds;
  - thrust, newtons;
  - three-component thrust direction;
- maximum numerical step, seconds;
- caller-supplied applicability and provenance.

The implementation contains no Apollo 13 mass, thrust, throttle, attitude, or trajectory constants.

## Equations and numerical method

For each constant-command segment:

[
dot m = rac{T}{I_{sp}g_0}
]

[
m_{n+1} = m_n - dot m,Delta t
]

[
Delta ec v_n =
rac{T}{(m_n + m_{n+1})/2},hat u,Delta t
]

where (T) is thrust, (I_{sp}) is specific impulse, (g_0) is the standard SI acceleration (9.80665,m/s^2), and (hat u) is the normalized caller-supplied thrust direction.

Segment boundaries are preserved exactly. The integrator subdivides each segment so no step exceeds the configured maximum step and evaluates acceleration at midpoint mass.

This is a modern project implementation choice. It is not a claim about an original LMS integrator.

## Computed result

Each run returns:

- final mass and velocity;
- elapsed time;
- integrated impulse;
- propellant used;
- vector and scalar-magnitude Delta-V;
- numerical step count;
- applicability;
- input provenance;
- explicit model assumptions;
- status `level_1_model_proof_not_historically_validated`.

## Current assumptions

- constant thrust and direction within a segment;
- constant specific impulse for the run;
- no gravity or other external forces;
- no position propagation;
- no attitude, gimbal, or rotational dynamics;
- instantaneous transition between segments;
- no engine start/cutoff transient;
- no pressurization, valve, erosion, or failure dependencies;
- no instrumentation, telemetry, or ground-product derivation.

## Validation coverage

Automated tests cover:

- mass depletion and impulse;
- convergence toward the constant-specific-impulse rocket equation as the step is reduced;
- deterministic repeatability;
- correct/early/late cutoff ordering;
- wrong-throttle ordering;
- direction-vector effects;
- combined duration/thrust/direction errors without a special outcome branch;
- zero-thrust coast;
- invalid vectors and dry-mass-floor violations;
- facilitator API and browser-panel contract.

## Validation interface

The facilitator endpoint is:

`POST /api/admin/model-proof/dps-burn`

The admin console's **MODEL** panel sends explicit inputs to that endpoint and displays the complete result and assumptions. It is validation infrastructure, not a player station or scenario outcome control.

## Historical-validation gate

Before the model can claim Apollo 13 PC+2 validity, the project still must freeze from primary sources:

- mass value and exact epoch;
- thrust/time history, including transients and throttle mapping;
- applicable specific impulse or mass-flow relationship;
- working frame and thrust-direction mapping;
- gravity/trajectory treatment;
- comparison target and acceptance tolerance.

A mismatch with historical data must cause source/model investigation, not an arbitrary correction factor.
