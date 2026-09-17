# Validation Evidence Model

Status: **architecture contract; historical criteria remain source/profile data**

## Purpose

The causal engine needs more than a binary `validated / not validated` label. Apollo source material now demonstrates multiple verification and validation layers with different evidentiary meanings.

This document defines how the project should record those layers without claiming that the original Apollo organizations used this exact modern schema.

Primary historical basis:

- NASA TN D-7990 / JSC S-424, *Apollo Experience Report — Guidance and Control Systems: Lunar Module Abort Guidance System*;
- flight-derived LMS/mission-simulator comparisons cataloged in `resources/source-catalog/LMS_FLIGHT_VALIDATION_SOURCES.md`;
- formal LMS acceptance/correlation source leads cataloged in `resources/source-catalog/LMS_ACCEPTANCE_PROCEDURES.md`.

## Validation layers

### 1. Equation / model verification

Question: does the mathematical model behave as intended over its declared input domain?

Apollo AGS analogue: closed-loop scientific/engineering simulation of the equations under nominal and 3σ vehicle/sensor/trajectory dispersions.

Project examples:

- numerical conservation/monotonicity checks;
- source-equation unit tests;
- convergence tests across smaller integration steps;
- parameter-range/sensitivity tests where D-022 permits a sourced range.

### 2. Implementation equivalence

Question: does the executable implementation reproduce the governing equations/reference implementation?

Apollo AGS analogue: bit-by-bit interpretive computer simulation verifying coded program implementation against the equations.

Project examples:

- independent reference calculation;
- exact synthetic fixtures with analytically known solutions;
- cross-implementation comparisons where independently specified.

### 3. Closed-loop causal integration

Question: do subsystem, vehicle, observation, and control interactions produce the intended causal behavior?

Apollo AGS analogue: closed-loop ICS flight simulator combining AEA program and vehicle flight characteristics; mission-specific 6-DOF simulations with AGS and LM flight-control hardware.

Project examples:

- thrust → dynamics → tracking;
- resource → source availability → power → observation;
- CAPCOM → crew action → physical response → fresh observation.

### 4. Ensemble / uncertainty performance

Question: how does the model perform under a defined distribution or dispersion set?

Apollo AGS analogue: 600-cycle Monte Carlo analysis against mission requirements.

Project rule: sample count and distributions are test-case choices unless explicitly source-defined. `600` is not a generic project default.

### 5. Independent / hardware-reference verification

Question: does the model agree with an independent facility, implementation, or real hardware at the same observable boundary?

Apollo AGS analogue: MSC hybrid-computer verification with actual ASA and DEDA hardware.

Project examples may include independent numerical implementations or preserved hardware-derived data. Modern third-party simulators remain comparison aids, not historical authority.

### 6. Operational checkout / bounded observable criteria

Question: does a mission/configuration-specific operational scenario keep declared outputs inside source-defined bounds or bounded curves?

Apollo AGS analogue: simulated-flight procedures for initialization, CSM acquisition, radar filtering, aborts, rendezvous maneuvers, and external delta-V; criteria derived from interpretive simulations and expressed as value bounds or bounded curves for AEA/display parameters.

Project rule: historical bounds belong to a specific test/profile/configuration. The existence of a criterion does not authorize inventing its missing numerical values.

### 7. Flight-derived validation

Question: how did simulator/model expectation compare with actual mission behavior?

Result classes:

- `representative_favorable` — source reports materially similar/representative behavior;
- `mismatch_negative` — source reports material divergence;
- `training_transfer` — simulator practice transferred usefully to flight without a direct model-equivalence claim;
- `not_comparable` — effectivity/input/observable mismatch prevents a defensible comparison.

Apollo examples currently include:

- Apollo 14 favorable steering/torque-to-inertia comparison;
- Apollo 9 negative AGS between-update degradation comparison;
- Apollo 15/17 landing visual/technique transfer.

Do not combine these into a single simulator-fidelity score.

## Required validation-case metadata

A future machine-readable validation case should be able to preserve at least:

- `case_id`;
- `evidence_layer`;
- model/program/document identity;
- version/revision/effectivity;
- mission/vehicle/site where applicable;
- initial/reference state;
- input/stimulus;
- uncertainty/dispersion assumptions;
- observable(s) and units;
- reference source / reference implementation;
- criterion representation;
- comparison/result;
- provenance;
- applicability limits;
- known discrepancies and causal explanation if sourced.

## Criterion representations

The architecture must not assume every criterion is a scalar tolerance.

Supported conceptual forms should include:

- exact/categorical expectation;
- one-sided bound;
- two-sided interval;
- residual tolerance;
- time series / trajectory;
- bounded curve / envelope;
- statistical/ensemble requirement;
- qualitative flight-comparison classification.

A source-defined `3σ` **input dispersion** is not automatically an output acceptance band. Preserve the role each numerical quantity plays.

## D-022 gate

Sensitivity testing may bridge an unresolved historical constant only when:

1. the source defines a valid range/uncertainty for the applicable quantity;
2. the comparison is performed at the actual player-visible/decision-relevant output boundary;
3. all other influential assumptions are controlled/documented;
4. the result demonstrates insensitivity across that sourced range.

Qualitative phrases such as `nearly identical`, `high fidelity`, or `much more rapidly` do not satisfy this gate.

## Discrepancy handling

A failed comparison is information, not a reason to retune silently.

Record:

`observed mismatch → applicable input/configuration → observable residual → source-supported cause if known → disposition`

Possible dispositions:

- model defect;
- source/effectivity mismatch;
- numerical artifact;
- reference uncertainty;
- unresolved.

Apollo TN D-7990's simulated-flight roundoff example is the preferred historical pattern: a discrepancy was isolated to a numerical mechanism, its operational significance was evaluated, and test interpretation was adjusted rather than hiding the discrepancy.

## Admission rule

A model becomes historically validated only for the **specific behavior, configuration, observable, and evidence layer actually supported**.

Passing a synthetic API/model proof demonstrates software architecture and numerical behavior; it is not historical validation.

Passing one historical comparison does not validate unrelated domains.
