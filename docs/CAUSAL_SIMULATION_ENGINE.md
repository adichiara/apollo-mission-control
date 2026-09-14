# Causal Simulation Engine

Status: **current architecture direction; implementation staged through the validation harness**

This document defines the project-level numerical/state architecture needed to let controller actions produce realistic consequences without pre-authoring every outcome branch.

It is not a claim that the Apollo spacecraft or original LMS software used these exact software abstractions. Historical simulator documentation is used to constrain model boundaries and fidelity; modern implementation details remain project choices.

## Goal

The simulator should support this general loop:

scenario initial conditions / external failures
+ controller instructions / simulated crew actions
+ elapsed time
→ authoritative causal state
→ subsystem models
→ instrumentation / onboard indications
→ telemetry / communications / ground processing
→ controller products and crew reports
→ player decisions / CAPCOM instructions
→ back into the causal state loop

A scenario supplies the starting problem. It does not enumerate all possible player outcomes.

## Historical simulator basis

Current research has identified direct evidence for this type of architecture:

- Grumman LED 500-5, *LMS Math Model — Equations of Motion, Subsystem Interfaces and Visual Display Drive Equations*, 22 April 1965;
- Grumman LED 500-16, *LEM Guidance Computer (LGC) Math Model for the Full Mission Engineering Simulator (FMES) and LEM Mission Simulator (LMS)*, 8 June 1966;
- Link Group's *Proposal for LEM Mission Simulator, Volume II, Technical Addendum*, whose surviving scan contains LMS mathematical-equation flowcharts;
- a Grumman memo studying the effect of 50-millisecond LMS integration steps on simulated Abort Attitude Control System response;
- LMS/AMS instructor material documenting subsystem simulation and malfunction insertion;
- the publicly available North American Aviation AMS Instructor Handbook Volume II, which explicitly separates equations of motion, weight/balance, vehicle-system, simulator-effects, and simulator-control programs and describes feedback among them.

The AMS handbook is especially useful because it describes translational/rotational EOM driven by simulated thrusting-system inputs, weight/balance outputs feeding mass/inertia/CG back to EOM, vehicle-system programs for propulsion/electrical/logic/displays/bus equations, and explicit malfunction insertion. This is direct historical evidence for a modular closed-loop simulator architecture.

These sources establish that equations of motion, subsystem interfaces, model partitions, numerical integration behavior, display-driving outputs, and malfunction injection were explicit simulator concerns. They do not yet establish every equation, constant, or Apollo-13-specific configuration we should implement.

Primary simulator scans should be cited from the public Virtual AGC / ibiblio archive when available rather than account-gated mirrors. Orbiter and Project Apollo — NASSP are useful modern implementation references, but they are not historical evidence and do not replace primary Apollo sources.

See research notes 127–131 and resources/source-catalog/APOLLO_SIMULATION_ENGINE_SOURCES.md.

## Core architecture rule

If the simulator supports an action, the action must change commanded/configuration state or an external condition. It should not directly select a narrative result.

Bad pattern:

wrong burn duration → assign bad-trajectory outcome

Required pattern:

burn instruction → crew action → propulsion state → thrust/mass flow → attitude/thrust direction → numerical dynamics → new position/velocity/mass → tracking/trajectory products → controller observation

The same model therefore handles a nominal burn, early cutoff, late cutoff, wrong throttle setting, incorrect attitude, or combinations of those conditions.

## Model types

The engine is intentionally hybrid. Not every subsystem requires the same mathematics.

### Continuous numerical models

Use where state changes continuously and timing matters.

Likely examples:

- translational dynamics;
- rotational/attitude dynamics where required;
- thrust and propellant depletion;
- battery charge depletion;
- consumable depletion;
- tank/pressure evolution where supported by source and gameplay need.

### Algebraic models

Use where output is a direct function of current state/configuration.

Examples may include:

- bus/load power balance;
- some sensor conversions;
- static pressure/temperature relationships;
- derived controller quantities.

### Discrete state machines

Use for configuration and logic.

Examples:

- switch/breaker/valve position;
- engine command state;
- guidance/program mode;
- communications path selection;
- relay/contactor logic where circuit-level modeling is unnecessary;
- crew procedural state.

### Event models

Use for genuinely external/discrete occurrences.

Examples:

- a scenario malfunction injection;
- ground-station loss;
- external tank rupture;
- scheduled mission-plan communication;
- exercise-control intervention.

An event may modify state. It should not bypass causal state to impose downstream consequences that should be calculated.

## Time and integration

Mission GET remains continuous when the session is RUNNING.

The causal engine adds an internal model clock beneath the existing session clock.

Each numerical model must declare:

- state variables;
- input variables;
- derivative/update rule;
- integration method;
- numerical step policy;
- outputs;
- source provenance;
- validity/fidelity limits.

### Timestep rule

Do not assume one historical timestep globally.

The surviving Grumman 50 ms memo establishes that timestep sensitivity mattered for at least one LMS attitude-control response. It does not prove that every LMS model ran at 50 ms.

Project implementation may use a modern fixed or adaptive integrator. The important requirements are:

1. deterministic results for identical inputs/configuration;
2. convergence checks showing materially similar outcomes when the step is refined;
3. an explicit model-level integration contract;
4. no coupling of physical integration cadence to browser polling cadence;
5. no assumption that historical numerical limitations are fidelity requirements.

## Authoritative state vs observations

The engine must continue the separation already established in the project.

authoritative physical/logical state != onboard indication != raw telemetry != ground-processed value != controller interpretation != crew report

A physical state change may produce several observations with different delays, failures, validity states, or biases.

Conversely, an observation failure must not silently modify physical truth.

## Scenario contract

A scenario should define only what is external to the reusable model or necessary to initialize it.

Typical scenario content:

- epoch / GET start;
- spacecraft configuration/profile;
- initial dynamic state;
- initial subsystem configuration;
- initial consumable quantities;
- mission objectives and nominal plan;
- externally injected malfunction/environment/network events;
- scenario-specific crew/ground communications where intentionally fixed.

Scenario files should not contain tables enumerating every possible player-error outcome.

## Simulated crew contract

The flight crew is simulation-controlled.

CAPCOM messages are structured simulation inputs. For supported message types:

1. crew receives the transmission;
2. crew may acknowledge/report using bounded canned text/state;
3. crew performs the associated cockpit action at the applicable time;
4. that action changes command/configuration state;
5. the physical subsystem decides what actually happens;
6. later crew reports remain an observation channel rather than hidden truth.

The crew model is not an AI decision-maker at this stage. It is deterministic exercise infrastructure representing the non-player spacecraft crew.

## First numerical vertical slice

The first implementation should prove that arbitrary burn inputs create computed consequences.

### Model chain

burn command / crew action
→ DPS propulsion model
→ thrust magnitude + mass flow + engine state
→ attitude / thrust-direction model
→ translational dynamics
→ position + velocity + vehicle mass
→ derived maneuver / trajectory result
→ controller-observable tracking/trajectory product

### Current Level-1 implementation checkpoint

The first numerical proof is now implemented on the development branch as a deliberately narrow, framework-neutral model:

- `src/apollo_mission_control/propulsion_dynamics.py` owns thrust, specific impulse, propellant mass depletion, command state, thrust direction, and vector Delta-V;
- crew/engine commands are separated from elapsed-time physical evolution;
- arbitrary piecewise-constant duration/throttle/direction inputs all use the same model;
- the model uses SI internally and does not embed Apollo-specific constants;
- `POST /api/validation/propulsion` exposes the model only as a facilitator validation endpoint and does not mutate the live PC+2 session;
- `/dynamics-test` provides a dedicated test screen with editable inputs and quick early-cutoff, late-cutoff, wrong-throttle, and attitude-offset perturbations.

This Level-1 model is **not yet an orbital trajectory simulator**. It currently computes thrust-produced vector Delta-V and propellant/mass consequences. It omits gravity, Earth/Moon propagation, position integration, rotational dynamics, actual attitude response, detailed DPS feed/pressurization behavior, and controller tracking/RTCC products.

That limitation is intentional: it gives the project a small causal kernel that can be tested before adding coupled dynamics.

### Source-bounded PC+2 validation case

Existing Apollo 13 evidence provides a useful regression case:

- PC+2 TIG: 79:27:38.30 GET;
- actual burn duration: approximately 263.82 s;
- staged throttle profile beginning at low thrust, then 40 percent, then maximum thrust;
- executed PGNS velocity components are documented;
- resultant maneuver magnitude and postburn residual evidence are documented;
- Apollo 13 documentation gives source-backed LM/CSM weights used in the existing scenario fixture;
- DPS engineering documentation provides thrust/throttle/propellant design information.

The historical case is a validation oracle, not the simulation algorithm.

The engine should calculate the result from state and commands, then compare with the historical result.

## First acceptance tests

The validation harness should support at least these cases without adding separate outcome branches.

### Nominal

Use the source-backed PC+2 command profile.

Expected: computed burn result falls within an explicitly documented model tolerance of the source-backed historical target once required model inputs are frozen.

### Early cutoff

Cut the engine before nominal cutoff.

Expected:

- less accumulated impulse/Delta-V;
- more remaining propellant;
- changed postburn trajectory product.

### Late cutoff

Continue beyond nominal cutoff.

Expected:

- greater accumulated impulse/Delta-V;
- less remaining propellant;
- changed postburn trajectory product.

### Wrong throttle

Hold an incorrect supported throttle setting.

Expected consequence emerges from thrust and mass-flow integration.

### Wrong attitude

Apply the same thrust history at an offset attitude.

Expected:

- similar scalar impulse if thrust history is unchanged;
- different vector Delta-V;
- different trajectory product.

### Combined error

Allow wrong attitude plus wrong duration/throttle.

Expected: no special scenario branch is required.

## Fidelity ladder

The model should grow by replacing abstractions, not by rewriting the architecture.

### Level 1 — impulse / translational proof

- thrust magnitude;
- mass depletion;
- prescribed attitude/thrust direction;
- translational integration;
- derived Delta-V / trajectory state.

### Level 2 — propulsion state

- engine command vs actual state;
- throttle limits/zones;
- restart/shutdown eligibility;
- propellant/pressurization dependencies needed by supported failures.

### Level 3 — attitude/control coupling

- commanded vs actual attitude;
- rotational response where needed;
- gimbal/RCS authority and failure effects.

### Level 4 — electrical / consumables

- sources, buses, loads, switching;
- battery energy/current;
- consumable rates tied to active equipment.

### Level 5 — observation chain

- onboard sensors/indications;
- telemetry channels;
- communications/ground processing;
- controller products.

The order may change if newly recovered simulator documentation shows a more useful model boundary.

## Source and validation requirements

Every implemented numerical model must carry:

- source list;
- mission/profile applicability;
- modeled variables and units;
- assumptions;
- unsupported/deferred mechanisms;
- regression cases;
- numerical convergence test where integration is used.

A simulator-era equation may be adopted only after checking whether it describes the relevant LMS/FMES configuration and whether its constants/configuration are applicable to Apollo 13/LM-7.

## Near-term implementation sequence

The Level-1 propulsion/Delta-V kernel now exists. The next steps should increase causal fidelity in controlled increments rather than expanding every subsystem at once.

1. Validate the Level-1 model through CI and the deployed `/dynamics-test` screen, including early/late cutoff, throttle, attitude-vector, and timestep-refinement cases.
2. Continue extracting the public LMS/AMS mathematical-model material, especially equations of motion, model interfaces, integration cadence, mass properties, and malfunction boundaries.
3. Add position plus gravity/orbital propagation so different burns produce different Earth-Moon trajectory states rather than only different Delta-V vectors.
4. Add actual attitude/orientation evolution and thrust-vector coupling, replacing the current externally prescribed direction vector.
5. Connect the simulated crew/CAPCOM path to these command inputs so a wrong instruction changes the same authoritative dynamics model.
6. Add electrical-power and consumables causal models, using primary Apollo sources for behavior and NASSP only as a secondary implementation/coverage cross-check.
7. Derive instrumentation/telemetry/ground products from the resulting state rather than injecting outcomes directly.

The historical PC+2 event model remains a useful chronology and regression scaffold during this transition, but it is no longer the intended mechanism for determining physical consequences.
