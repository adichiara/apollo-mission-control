# Research note 215 — AMS program partition and malfunction-insertion boundaries

Date: 2026-09-15  
Status: **REVIEWED for reusable simulator-architecture constraints; AMS initial-delivered-configuration evidence, not Apollo-13 LMS configuration authority.**

## Question

What surviving Apollo Mission Simulator evidence constrains how this project should separate vehicle physics, system behavior, simulator effects, external Mission Control interfaces, and malfunction insertion?

## Primary source

North American Aviation, *Preliminary Apollo Mission Simulator Instructor Handbook, Volume II: Operation & Utilization*, SM6T-2-02 / SID 65-974-2, 1 July 1965.

The public scan is cataloged at:

- https://ibiblio.org/apollo/Documents/19730060784_1973060784.pdf

This is an **AMS** source for the initial delivered configuration. It is not an LMS document and is not evidence that Apollo 13 used identical program names, constants, update rates, or malfunction inventories.

## 1. Operational-program partition

The handbook divides operational software into five classes:

1. vehicle dynamics;
2. vehicle systems;
3. simulator effects;
4. simulator control;
5. Mission Simulation Control Center interface.

The program-data section separately identifies diagnostic programs.

This is stronger evidence than a generic statement that Apollo simulators were “closed loop.” It shows an explicit partition among:

- physical/dynamic evolution;
- subsystem behavior;
- rendered/environmental effects;
- exercise/simulator orchestration;
- external Mission Control/network interfaces.

### Project consequence

Retain separate reusable domains rather than one monolithic scenario state machine:

`vehicle dynamics → subsystem state → instrumentation/effects → ground/interface products`

with simulator/facilitator control outside that causal chain.

## 2. Vehicle dynamics were continuously driven by subsystem inputs

The AMS handbook states that vehicle-dynamics computation included equations of motion, aerodynamic coefficients, and weight/balance effects as a function of elapsed time. Resulting spacecraft position/attitude fed visual systems and simulated spacecraft instruments.

It also states that these characteristics were continually computed from simulated thrusting-system inputs and from operation of other spacecraft systems where those operations affected weight and balance.

### Project consequence

This supports the current rule that scenario files should not enumerate downstream motion outcomes. Thrust, mass properties, configuration, and other modeled source states should drive the dynamics model, whose outputs then feed indications/observations.

It also supports keeping mass-properties/resource changes as upstream model inputs rather than decorating a pre-authored trajectory.

## 3. Vehicle systems had normal and malfunctioned real-time behavior

The handbook describes real-time vehicle-system programs representing spacecraft systems in both normal and malfunctioned conditions.

That implies malfunction behavior belonged inside or at the input boundary of subsystem simulation rather than solely in a scripted narrative layer.

### Project consequence

A malfunction should be inserted at the narrowest supported causal point:

- source/physical component state when a physical failure is intended;
- command/control state when a control failure is intended;
- observation/telemetry layer when only the indication/data path is intended to fail.

Do not automatically translate a failure label into every downstream consequence.

## 4. Malfunction insertion was not a single mechanism

The Instructor-Operator Station Malfunction Insertion Unit supported:

- manual malfunction insertion;
- preprogrammed malfunction insertion;
- time-dependent malfunction insertion.

The handbook also states that one simulated malfunction could require more than one malfunction code.

### Project consequence

The project should preserve a distinction between:

- the **exercise-level failure intent** (“this training failure”); and
- one or more **model-level insertions** needed to realize it.

A scenario malfunction definition may therefore map to multiple explicit causal insertions, but those insertions should remain inspectable rather than hiding a pre-authored outcome bundle.

Time-triggered failure activation is historically supportable as an instructor/simulator mechanism, but activation time must remain scenario data rather than a generic subsystem property.

## 5. Telemetry faults were separable from spacecraft-system faults

The AMS telemetry console allowed instructors to select faults in analog, digital-word, and bilevel telemetry channels. Those faults could be prepared independently and then activated manually or by computer control.

This is direct evidence for a separate observation/data-path failure layer.

### Project consequence

Continue to distinguish:

`physical truth ≠ onboard indication ≠ telemetry channel ≠ processed ground product ≠ controller-visible interpretation`

A telemetry-channel failure must not silently mutate physical spacecraft state.

Likewise, a physical failure should not automatically imply that all telemetry or controller products become invalid unless the modeled instrumentation/data path says so.

## 6. Inserted indications did not necessarily force the downstream vehicle event

The handbook's abort-simulation discussion is especially important. Several malfunction insertions illuminated abort-related indications but did **not** automatically cause the simulated automatic abort that the actual spacecraft would have produced. The instructor could then separately initiate an automatic abort or allow subsequent events to develop.

This is a simulator-specific implementation detail, not a spacecraft-behavior rule. But it demonstrates that the training simulator explicitly separated:

- an inserted malfunction/indication;
- automatic-response logic;
- instructor augmentation;
- subsequent simulated consequences.

### Project consequence

This reinforces the project's refusal to encode:

`failure label → predetermined scenario outcome`

as a generic shortcut.

Where historical vehicle automation is source-backed, that automation belongs in the physical/control model. Where a historical simulator deliberately bypassed it for training control, that belongs in simulator/instructor configuration—not in the spacecraft truth model.

## 7. Current architecture decision

The reusable engine should maintain at least these separable layers:

1. **Dynamics / physical truth**
   - translational/rotational state;
   - mass properties;
   - force/torque sources.

2. **Vehicle subsystem state**
   - propulsion, electrical, guidance/control, communications, resources;
   - normal and malfunctioned behavior.

3. **Instrumentation / observation state**
   - onboard indications;
   - telemetry channels;
   - validity/bias/loss/fault state.

4. **Ground/interface state**
   - network/ground processing;
   - controller products;
   - uplink/voice/data interfaces.

5. **Simulator/exercise control**
   - lifecycle;
   - scenario failure intent;
   - manual/preprogrammed/time-dependent insertion;
   - validation/facilitator controls.

These boundaries align with the existing project direction and now have direct Apollo-simulator precedent.

## 8. What this source does not authorize

Do not use this handbook to claim:

- Apollo 13 LMS program names were identical;
- Apollo 13 LMS used the same malfunction codes/inventories;
- the AMS update rates or integration steps apply to the LMS;
- a specific AMS simulation shortcut reproduces real LM/CSM automatic behavior;
- the initial delivered configuration represents later Block II or mission-specific simulator fidelity.

Those questions require LMS-specific and mission-era evidence.

## Next research step

Prioritize surviving LMS sources that can refine the same boundaries:

1. LMS Instructor's Handbook Volume I — subsystem representation;
2. LMS mathematical-model proposal/technical addendum — equations and interfaces;
3. LMS numerical-integration/timestep studies;
4. simulator output dictionaries and malfunction tables;
5. validation/correlation or acceptance reports tying model outputs to spacecraft/reference data.

Cross-check every candidate equation or coupling against Apollo 13 LM-7/CSM sources before freezing historical constants.
