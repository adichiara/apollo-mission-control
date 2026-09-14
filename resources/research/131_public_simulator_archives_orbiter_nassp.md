# Public simulator archive and modern implementation references

Date: 2026-09-14  
Status: **source-access correction and secondary implementation-reference audit**

## Purpose

Two useful source categories need to be separated clearly:

1. surviving **primary/contemporary simulator documentation**, which can establish historical model structure and behavior;
2. modern open-source simulators, which can help us understand implementation patterns and provide comparison/regression references but are **not historical evidence**.

This note also corrects the preferred access route for the Apollo Mission Simulator manuals: use the public Virtual AGC / ibiblio scans rather than account-gated document mirrors.

## Preferred public archive: Virtual AGC / ibiblio

The public Virtual AGC document archive at:

- https://www.ibiblio.org/apollo/
- https://www.ibiblio.org/apollo/Documents/

contains direct downloadable scans of the Apollo/Lunar Module simulator material.

For the Apollo Mission Simulator Instructor Handbook, Volume II, a direct public scan is available at:

- https://ibiblio.org/apollo/Documents/19730060784_1973060784.pdf
- alternate archive filename: https://www.ibiblio.org/apollo/Documents/ams_instructor_handbook_vol2.pdf

The scan identifies itself as:

- North American Aviation, Inc.
- SM-6T-2-02 / SID 65-974-2
- *Preliminary Apollo Mission Simulator Instructor Handbook*
- Volume II: *Operation and Utilization*
- 1 July 1965
- Contract NAS9-150

The technical-report abstract states that Section 2 describes simulator computer programs including vehicle programs, vehicle-system programs, simulator-effects programs, and simulator-control programs.

The document itself is particularly valuable because it explicitly describes:

- translational and rotational equations of motion;
- conversions between inertial reference frames;
- continuous recomputation from spacecraft thrusting-system inputs;
- feedback of EOM outputs into other simulation programs;
- weight-and-balance calculations feeding total mass, moments/products of inertia, and center-of-gravity data to the EOM;
- propulsion-system, electrical-power-system, logic, display, and bus-equation vehicle-system programs;
- manual, preprogrammed, and time-dependent malfunction insertion;
- complete simulator-output tables in Volume III with program and/or mathematical-model designators.

This is stronger direct evidence than a third-party transcription or account-gated mirror and should be the preferred citation/access path.

## Architecture evidence from the AMS handbook

The AMS Volume II material substantially reinforces the current project architecture.

The original simulator separated at least:

- equations of motion;
- aerodynamic forces/moments;
- weight and balance;
- vehicle systems;
- simulator effects;
- control/executive functions;
- telemetry/interface programs;
- malfunction-insertion logic.

It also used feedback between dynamic outputs and subsystem calculations. For example, the handbook describes EOM outputs such as altitude and vehicle velocity being routed back into input programs, while weight-and-balance outputs feed mass/inertia/CG back to EOM.

That is very close to the modular closed-loop model we are designing:

```text
subsystem state / thrust / mass properties
            ↓
 equations of motion
            ↓
position / velocity / attitude
            ↓
subsystem + display / telemetry feedback
```

The key historical lesson is not a particular software class structure. It is that the simulator treated vehicle dynamics, subsystem state, display-driving values, and malfunctions as interacting model components rather than authored narrative branches.

## Orbiter Space Flight Simulator

Repository:

- https://github.com/orbitersim/orbiter

Project description:

- open-source spaceflight simulator based on Newtonian mechanics;
- MIT licensed;
- provides generic vessel dynamics, gravity-field handling, thrusters, propellant resources, mass properties, and rigid-body/orbital simulation services.

### Relevance to this project

Orbiter is a useful **modern implementation reference** for the external flight-dynamics layer.

Its public vessel API supports concepts such as:

- thruster position and direction;
- maximum thrust;
- propellant-resource association;
- specific impulse;
- propellant mass;
- vessel rigid-body state.

This is especially relevant because it demonstrates a clean separation between generic spaceflight dynamics and spacecraft-specific add-on systems.

### Boundary

Orbiter is **not** evidence for how Apollo hardware or the 1960s Apollo Mission Simulator behaved.

Its MIT license makes its implementation legally easier to study or reuse than GPL code, but any direct code reuse would still need explicit attribution/license handling and an architectural reason to do so. The current Python/server architecture does not make Orbiter itself a drop-in dependency.

For now, use Orbiter as:

- an implementation-pattern reference;
- an independent numerical-results comparison where practical;
- a source of ideas for generic vessel/thruster/propellant abstractions.

Do not use Orbiter as a historical source for Apollo constants or subsystem behavior.

## Project Apollo — NASSP

Project:

- https://nassp.space/index.php/Main_Page
- https://github.com/orbiternassp/NASSP

NASSP is an Apollo-specific add-on for Orbiter. Its project documentation describes:

- near-full CSM and LM control panels;
- increasingly detailed internal systems;
- electrical distribution and fuel-cell simulation;
- support for Virtual AGC;
- a study-simulator goal emphasizing systems-level accuracy and use of original NASA software/documentation/procedures where possible.

### Why NASSP is unusually relevant

NASSP demonstrates almost exactly the **hybrid architecture** now being considered for this project:

```text
Orbiter generic flight dynamics
        +
NASSP Apollo-specific subsystem simulation
        +
Virtual AGC flight software
        +
Apollo cockpit indications/controls
```

That is useful evidence that a practical Apollo simulation can separate general rigid-body/orbital mechanics from detailed Apollo subsystem state.

### Concrete code areas reviewed

The current NASSP repository includes an LM DPS model with explicit state for:

- propellant quantity;
- ambient/supercritical helium;
- helium regulator manifold pressure;
- fuel/oxidizer ullage pressure;
- fuel/oxidizer engine-inlet pressure;
- propellant-level indications;
- helium/isolation/compatibility/vent valves;
- engine command/arm/prevalve state;
- thrust command;
- chamber pressure;
- DPS gimbal actuators.

It also contains a causal LM electrical topology with batteries, electrical-control assemblies, main buses, bus ties/cross ties, circuit breakers, source/load relationships, voltage/current/frequency, and power draw.

This is directly useful as a **model-coverage checklist** and architectural comparison.

### Important caution: NASSP contains approximations

NASSP source itself marks some values/behaviors as simplified or TBD. For example, parts of the current LM DPS source use placeholder tank temperatures and simplified pressure relationships.

Therefore NASSP must never be treated as a substitute for primary Apollo documentation merely because it is detailed.

The correct use is:

1. identify a subsystem/model feature in NASSP;
2. trace its stated or likely source back to Apollo documentation;
3. use the primary source to decide what belongs in our model;
4. optionally compare our numerical behavior against NASSP as an independent modern implementation.

### Licensing boundary

NASSP source files identify themselves as GNU GPL version 2 or later.

No NASSP source code should be copied into this repository unless the project deliberately adopts a compatible licensing strategy.

Until such a decision exists:

- inspect NASSP for architecture and model coverage;
- use it to discover primary sources and cross-check outcomes;
- do not port/copy GPL implementation code.

This licensing boundary does not prevent us from independently implementing equations and behavior taken from the underlying public-domain/government/contractor historical sources.

## Combined research strategy

The source hierarchy for the causal engine should now be:

1. **Apollo mission-/vehicle-specific primary sources** for actual hardware/configuration;
2. **original LMS/AMS simulator documentation** for training-simulator abstraction, equations, model partitioning, integration, and malfunction behavior;
3. **Orbiter** as a modern generic flight-dynamics implementation reference;
4. **NASSP** as a modern Apollo systems-simulation comparison/discovery reference;
5. our own numerical validation and historical regression cases.

The modern projects should accelerate implementation research, but they do not change the project's evidence policy.

## Immediate consequences

1. Prefer ibiblio/Virtual AGC direct PDFs in the repository source catalog; avoid account-gated mirrors where a public primary scan exists.
2. Extract the AMS Volume II EOM, weight/balance, vehicle-system, malfunction, and output-model sections alongside the LMS material.
3. Use NASSP to build a subsystem coverage map for propulsion, electrical power, consumables, guidance/control, instrumentation, and ECS.
4. Use Orbiter to compare the shape of generic rigid-body/thruster/propellant abstractions before freezing our own Python interfaces.
5. Do not copy NASSP GPL code.
6. Keep implementation source-backed and independently coded.

## Evidence classification

- Public AMS Volume II scan and its contents: **DOCUMENTED**.
- Orbiter architecture/license and generic capabilities: **DOCUMENTED as modern implementation facts**, not Apollo historical evidence.
- NASSP architecture and represented subsystem coverage: **DOCUMENTED as modern implementation facts**, not Apollo historical evidence.
- Historical correctness of any particular NASSP equation/constant: **UNRESOLVED until traced to a primary source**.
