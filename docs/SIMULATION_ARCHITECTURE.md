# High-Level Simulation Architecture

Status: **current project architecture**, not a claim that Apollo software was structured this way.

The component boundaries below are chosen so that documented Apollo information flow can be represented without exposing the underlying simulation state directly to players.

## Historical basis for the decomposition

Apollo Mission Control documentation describes MCC operations in terms of the Mission Operations Control Room (MOCR), Staff Support Rooms (SSR), Communications, Command and Telemetry System (CCATS), Real-Time Computer Complex (RTCC), Voice Communications System, Display/Control System, and the Manned Space Flight Network.

Apollo simulation/training documentation also establishes that mission simulation was **closed-loop**, used active controls/displays, included malfunction insertion, and represented trajectories, telemetry, uplink/voice communications, and major spacecraft-system operations. Apollo engineering simulation used real-time mathematical/system models and hardware/software interfaces for closed-loop verification.

These sources support a causal/stateful simulator architecture, but they do not establish that the original Apollo simulator software used the same module boundaries defined here. See `resources/research/127_causal_simulation_engine_and_crew_model.md` and `resources/source-catalog/APOLLO_SIMULATION_ENGINE_SOURCES.md`.

## Core architecture rule: scenario is not the simulator

The project distinguishes **scenario authoring** from **simulation behavior**.

A scenario defines:

- initial conditions;
- mission objectives and nominal plan/context;
- external/environmental conditions;
- malfunction/failure injections;
- source-bounded scheduled events that are genuinely independent of player action;
- exercise-control conditions.

The simulation engine owns evolving spacecraft/mission state and computes consequences of elapsed time, configuration, failures, controller commands, and simulated-crew actions.

The intended closed loop is:

```text
scenario inputs + elapsed time + controller/crew actions
                         |
                         v
             authoritative mission state
                         |
                         v
       instrumentation / telemetry / ground processing
                         |
                         v
              controller-visible information
                         |
                         v
           controller interpretation / action
                         |
                         +---------------------> back into state
```

A scenario event may change state or inject a failure. It should not directly decree a downstream outcome when that outcome should emerge from modeled state.

## Scenario portability and validation-anchor rule

Apollo 13 PC+2 is the current **reference scenario** for building and validating the first complete causal chain. It is not the product boundary.

The architecture is intended to support a scenario library spanning different Apollo mission phases and problem classes. Therefore:

- reusable subsystem models should be mission/scenario-configurable rather than PC+2-specific where the historical system varies;
- mission-specific constants, procedures, station configurations, timelines, and failure injections should live in profiles/scenario data when practical;
- a mechanism first implemented because PC+2 needs it should expose a general causal contract that other sourced scenarios can reuse;
- mechanisms not exercised by PC+2 may be added later when another selected scenario requires them;
- historical fidelity is still evaluated per mission/scenario rather than by assuming the Apollo 13 configuration applies everywhere.

PC+2 is thus a **calibration and architecture proof case**: if arbitrary correct or incorrect actions produce plausible sourced consequences there, the same engine structure should be capable of supporting later lunar-descent, ascent, rendezvous, entry, launch-abort, communications/network, and other documented simulator cases after their required models are added.

This implements Decision D-021 and complements the Apollo 13-era default technical baseline in D-012.

## Causal-fidelity rule

The target is **not** an exhaustive first-principles emulation of every Apollo component. It is a modular causal simulator with enough fidelity to support the decisions/actions available in a scenario.

For every supported action or failure:

- important physical/logical consequences must be represented;
- downstream observations must be derived through the appropriate sensing/processing path;
- wrong, omitted, late, and correct actions must be able to produce different resulting state where the real system would differ;
- unsupported internal details may remain abstracted until a scenario dependency requires them.

This extends Decision D-019 rather than replacing it.

## Proposed software layers

### 1. Session / mission authority

Owns:

- selected mission/scenario;
- simulation lifecycle;
- mission elapsed time;
- pause/reset controls for simulation administration;
- connected stations;
- authoritative ordering of commands/events.

This is a software requirement of the multiplayer simulation.

**Current implementation:** a framework-neutral scenario catalog discovers fixture metadata and exposes scenario IDs independently of the PC+2 domain model. Session creation selects a scenario by ID and dispatches through a runtime-adapter registry. Only `pc2_v1` is currently executable; discovery of a fixture does not imply runtime support.

The transport and realtime clock now depend on a small shared `SessionRuntime` lifecycle/station contract rather than directly on `PC2Session`. Adapter capabilities explicitly identify scenario-specific operations. For example, the current adapter advertises `pc2_delta_p` and `pc2_dps_shutdown`; those endpoints are rejected for a future runtime that does not advertise them.

This deliberately does **not** force PC+2-specific state, products, rules, or controller procedures into the generic runtime interface.

### 2. Scenario definition / SimSup inputs

Defines the exercise rather than the physics.

Owns:

- initial mission/spacecraft state overrides;
- scheduled source-bounded external events;
- malfunction/failure insertion;
- ground/network/environment injections;
- scenario objectives and termination/evaluation conditions;
- validation/test hooks.

A scenario does not own controller-visible truth directly. Its injections enter the causal model at an appropriate layer.

The cross-scenario fixture metadata contract currently includes scenario identity/title, mission, provenance/status class, runtime-adapter identity, mission-profile identity, mission-time bounds, and vehicle configuration. PC+2-specific state remains below that boundary. Research note 141 now supplies the second reference case used to judge what additional state should become common.

### 3. Authoritative causal mission state

Stateful model of spacecraft, trajectory, crew-controlled configuration, and relevant ground conditions.

The model is expected to combine discrete state machines with continuous/algebraic models as needed. Example causal domains include:

- propulsion/engine/valve/configuration state;
- guidance, reference, attitude/control state;
- electrical sources, buses, loads, breakers/contactors, inverter state;
- communications/antenna/transmitter/receiver path state;
- consumables and configuration-dependent depletion;
- instrumentation/sensor/source validity;
- decision-relevant trajectory/maneuver results.

Subsystem detail is admitted when a supported player action, failure, rule, or observation depends on it.

Principle:

> Players do not read authoritative state directly.

### 4. Simulated flight crew

The spacecraft crew is part of the authoritative simulation, not a human player role. See Decision D-020.

Initial crew behavior may be deterministic and canned where that is sufficient:

`CAPCOM transmission → crew receipt/acknowledgement → supported crew action → spacecraft consequence → crew report/other observations`

These are separate stages. CAPCOM transmission does not automatically mutate spacecraft state, and a crew report is not a direct alias of hidden physical truth.

Later crew behavior may become more sophisticated only when scenarios require it. The first implementation target is deterministic support for known CAPCOM/crew action types and source-/scenario-bounded response timing/wording.

### 5. Instrumentation and telemetry

A generic tracking-observation proof now exercises this boundary for trajectory data:

`authoritative trajectory state → geometric tracking truth → delayed/biased/available observation`

The proof supports deterministic range/range-rate, latency/age, bias, availability, validity, and provenance without embedding Apollo/MSFN constants. It is not yet a model of MSFN radar/Doppler hardware, station visibility, propagation delay, CCATS, or RTCC processing. Those remain historical layers to be added when sourced scenario requirements demand them.



Transforms authoritative state into the measurements that would actually be available.

This layer is necessary to represent distinctions such as:

- actual physical condition versus measured value;
- sensor/instrumentation failure;
- unavailable data;
- stale data;
- different update rates;
- onboard indication versus telemetered value.

Exact behavior requires source support.

### 6. Ground communications and processing

Represents the documented path from received spacecraft/network data to controller-usable values and products.

Historical subjects to reconstruct include:

- MSFN data delivery;
- CCATS;
- RTCC;
- ground-computed parameters;
- data validation/quality;
- display generation;
- command/update paths.

Do not collapse this into direct access to simulation variables where the historical distinction affects controller work.

### Ground-processing fallibility

Apollo 13 supplies direct evidence that ground-derived controller information can be wrong even when the spacecraft condition is satisfactory.

After MCC-5, the LM crew established passive thermal control using AGS. Mission Control's last high-bit-rate attitude indication disagreed with the desired attitude; the Apollo 13 Mission Operations Report states that the **RTCC was incorrectly processing AGS body angles**. Controllers discarded that improper readout and relied on the independent FDAI reference, which showed PTC had been correctly established.

Therefore the ground-processing layer must be capable of representing:

- valid spacecraft state with incorrect ground transformation;
- correct received telemetry with a bad derived product;
- stale or misconfigured computational products;
- independent cues that allow controllers to reject a bad display value.

The architecture must never define controller-visible values as direct aliases of authoritative physical-state variables.

Conceptually:

```text
physical state
    ↓
sensor / onboard computation
    ↓
raw telemetry
    ↓
ground decoding / transformation   ← can be wrong
    ↓
controller product / CRT
```

See `resources/research/037_apollo13_ags_telemetry_ground_processing.md`.

### 7. Controller information services

Defines exactly what each controller position can request/observe.

For each position this eventually needs:

- display list;
- parameters/products;
- update characteristics;
- display selection workflow;
- voice/communication relationships;
- applicable reference documents.

### 8. Controller action/command layer

Controller actions are explicit authoritative inputs into the simulation, but only through historically/project-valid authority paths.

Examples:

- FLIGHT decisions/authorization;
- CONTROL/TELMU/GUIDO/FIDO/INCO judgments and requests;
- CAPCOM communication items;
- command/uplink operations where historically appropriate.

This layer does not directly set the intended outcome. It changes commands/configuration/communication state; the causal engine produces consequences.

### 9. Historical display renderer

Eventually renders documented display formats.

Requirements will come from MCC display-format research. Avoid generic "retro terminal" styling where an actual format can be reconstructed.

**Current development boundary:** player-facing station UI implementation is intentionally deferred while the causal engine, simulated crew, and validation harness are developed. The current admin/contingency screens are test surfaces, not candidate final station interfaces.

### 10. Station client

Future phone/web interface for one assigned controller station.

The client should primarily:

- show the station's historically justified displays/controls;
- allow documented display selection/input;
- connect to the central server;
- expose only the information appropriate to that station.

Modern session controls (join/reconnect/settings) should be visually and functionally separated from the simulated console.

### 11. Simulation Control / validation harness

Administrative/test layer for running and inspecting simulations during development.

Responsibilities may include:

- lifecycle/reset;
- manual validation time control;
- scenario/failure injection;
- direct inspection of hidden authoritative state for test purposes;
- test-only forcing of crew/vehicle responses while a corresponding simulated mechanism is not yet implemented;
- full audit-log access.

The test harness must be clearly distinguished from eventual player-facing station clients. As causal subsystems and crew behavior become implemented, test-only manual response buttons should be retired or retained only as explicit overrides.

### 12. Communications

Represents documented voice loops and air/ground paths where needed.

For the current architecture, CAPCOM↔crew exchange is a modeled communication path even if the response text is initially canned. In-person Mission Control players may still speak naturally; historical loop behavior remains a separate research/design question.

### 13. Reference/document package

Versioned set of the mission-specific material required for a session:

- flight rules;
- procedures;
- controller references;
- tables;
- timelines;
- project-created indexes.

This package should trace back to the source catalog.

### 14. Event/audit record

Records simulation events needed for reproducibility and post-simulation analysis:

- scenario injections;
- controller commands/input;
- crew receipt/action/report events;
- physical/logical state transitions that are useful for validation;
- instrumentation/ground-product changes where relevant;
- session joins/disconnects;
- communications events if represented in software.

This is not an in-play scoring system.

## Consequence propagation example

The current PC+2 shutdown chain should evolve from validation buttons into the following causal flow:

```text
synthetic/source failure or observation
        ↓
CONTROL-visible product
        ↓
CONTROL decision / callout
        ↓
CAPCOM transmission
        ↓
simulated crew receipt / STOP action
        ↓
DPS valve / engine state changes
        ↓
thrust + pressure + maneuver-result consequences
        ↓
instrumentation / telemetry / crew report
        ↓
CONTROL / GUIDO / FIDO-visible downstream evidence
        ↓
controller recovery decisions
```

If the shutdown occurs early, a future causal maneuver model should derive burn shortfall/trajectory consequences from the actual thrust history rather than select a pre-authored "premature shutdown" ending. The fidelity of that maneuver model remains a research/build question.

## Conceptual data flow

```text
SCENARIO / SIMSUP INPUTS
        |
        v
AUTHORITATIVE CAUSAL MISSION STATE <---------------------------+
        |                                                      |
        +--> SIMULATED CREW ACTIONS                            |
        |                                                      |
        v                                                      |
INSTRUMENTATION / TELEMETRY                                    |
        |                                                      |
        v                                                      |
COMMUNICATIONS / GROUND PROCESSING                             |
        |                                                      |
        +-------------------------+                            |
        |                         |                            |
        v                         v                            |
CONTROLLER INFORMATION       COMMAND / UPDATE PATHS            |
        |                         |                            |
        v                         |                            |
DISPLAY / TEST PRESENTATION      |                            |
        |                         |                            |
        v                         |                            |
CONTROLLER INTERPRETATION / COMMUNICATION / DECISION ----------+
```

Where Apollo documentation shows a materially different path, this architecture must change to match it.

## Development strategy

The simulation should grow by **causal vertical slices**, not by attempting an all-spacecraft emulator first.

For each slice:

1. identify a supported controller action/failure/problem;
2. document the real causal dependencies;
3. define authoritative state variables and transitions;
4. define sensor/telemetry/ground observation paths;
5. implement simulated crew actions if required;
6. expose the behavior through the test harness;
7. test correct, omitted, late, and wrong actions;
8. add deeper subsystem fidelity only if the supported behavior requires it.

The current PC+2 DPS/electrical/instrumentation chain is the preferred first causal-engine proving ground because substantial source work already exists.

## Deployment constraint already known

The project is intended to run from a central server hosted on Render with players connecting from phones.

FastAPI/Uvicorn is the current prototype transport. Durable storage, realtime push mechanism, and long-term production persistence remain open until simulation requirements make them necessary.

## Mission-era configuration profiles

The reusable simulation should distinguish the **common Apollo platform** from a **mission-specific historical profile**.

Current design direction:

- use the Apollo 13-era MCC configuration as the default technical baseline/superset for shared implementation;
- apply mission-specific configuration data for Apollo 11, Apollo 12, Apollo 13, and later scenarios;
- allow a mission profile to change nomenclature, controller availability, display sets, procedures, rules, telemetry/configuration, console capabilities, spacecraft/ground-system details, crew-response mappings, and causal-model parameters where sources establish differences.

Example:

```text
COMMON APOLLO PLATFORM
        |
        +-- APOLLO 11 PROFILE
        |      TELCOM terminology
        |      Apollo 11 display/configuration evidence
        |      Apollo 11 flight rules / spacecraft state
        |
        +-- APOLLO 13 PROFILE
               TELMU terminology
               AS-508 MCC/MSFN configuration
               Apollo 13 displays/rules/spacecraft state
```

This avoids maintaining entirely separate simulators while also avoiding the false assumption that a later Apollo console configuration is automatically historically correct for an earlier mission.
