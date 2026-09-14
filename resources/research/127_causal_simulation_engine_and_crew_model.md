# Apollo causal simulation engine and simulated-crew boundary

Date: 2026-09-14  
Status: **architecture research / decision support**

## Question

The first PC+2 implementation used a historically anchored sequence of nominal events plus selected source-bounded contingency actions. That is sufficient to validate timing, information boundaries, controller authority, and one nonnominal chain, but it is not sufficient for a reusable game in which controller decisions can change spacecraft behavior and create new downstream problems.

Two architecture questions now matter:

1. should the spacecraft/mission be represented primarily as a pre-scripted branching scenario graph, or as a stateful causal simulator whose future state is computed from current state and actions?
2. should the flight crew be another human player role, or a simulated part of the exercise that exchanges bounded communications/actions with CAPCOM?

## Historical simulation evidence

### Apollo mission simulation was closed-loop, not merely event playback

NASA's Apollo systems/procedures experience report describes mission simulation as including spacecraft trajectories, telemetry, uplink and voice communications, and all major spacecraft systems operations. The Apollo mission simulator was coupled to a simulated Manned Space Flight Network and Mission Control was used as part of the procedure-verification/training environment. NASA explicitly characterizes the mission simulator as the highest-fidelity spacecraft simulator available for this purpose.

Source: NASA TN D-7436, *Apollo Experience Report: Systems and Flight Procedures Development*, NTRS `19730023040`.

An earlier Apollo training description states that mission-simulator controls and displays were active and driven closed-loop by peripheral computing equipment, while the instructor console included duplicate displays and malfunction-insertion units.

Source: NTRS `19660019476`.

### Apollo engineering simulators used mathematical/physical models

NASA's guidance-and-control engineering-simulation experience report describes real-time simulation using general-purpose analog and digital computing equipment, subsystem hardware, special interfaces, and large hybrid mission-evaluation simulators. These simulations were used for closed-loop hardware verification, hardware/software compatibility, software/procedure verification, and mission-specific evaluation.

Source: NASA TN D-7287, *Apollo Experience Report: Guidance and Control Systems—Engineering Simulation Program*, NTRS `19730016146`.

This does not prove that every crew-training simulator subsystem used the exact same model implementation. It does establish that Apollo simulation practice included causal mathematical/system modeling rather than relying only on fixed event scripts.

### Training explicitly had to handle unplanned nonnominal situations

NASA's flight-mission-rule experience report discusses training controllers and crews in determining the best response to nonnominal in-flight situations for which no complete action had been preplanned.

Source: NASA TN D-7822, *Apollo Experience Report: The Role of Flight Mission Rules in Mission Preparation and Conduct*, NTRS `19750002893`.

This is directly relevant to game architecture: a useful Mission Control simulation cannot require that every possible player mistake or recovery sequence be authored in advance as a unique branch.

## Architecture conclusion

The project should move toward a **hybrid causal simulation engine**, not an exhaustive branch tree and not a complete first-principles recreation of every LM/CSM subsystem.

The central distinction should be:

- **scenario** defines initial conditions, mission objectives, nominal plans, externally injected failures/malfunctions, scripted environmental/ground events, and any historical communications that are intentionally fixed;
- **simulation engine** owns evolving spacecraft/mission state and computes the consequences of actions, omissions, configuration changes, failures, and elapsed time;
- **observation model** derives onboard indications, telemetry, ground-processing products, and controller-visible information from that state;
- **controller actions** alter commanded/configuration state only through historically valid authority paths;
- **crew model** interprets CAPCOM instructions and performs modeled crew actions according to scenario/crew-response rules;
- **mission logic** evaluates operational consequences and objectives from resulting state rather than selecting a pre-authored outcome label.

In compact form:

`scenario inputs + elapsed time + player/crew actions → authoritative physical/logical state → instrumentation/telemetry/ground products → controller observations → new actions`

This is a closed loop.

## Why a full branch tree is the wrong scaling model

A branch-tree implementation scales poorly because each controller action can interact with:

- prior configuration;
- subsystem health;
- power availability;
- guidance/control state;
- consumables;
- communications/telemetry state;
- mission timing;
- other controller/crew actions;
- latent failures already present.

The number of combinations grows rapidly. More importantly, branch scripting tends to encode outcomes directly rather than reproduce the causal information chain the controllers actually reason from.

A causal model allows an action to have the same local meaning wherever it occurs. For example, opening or closing a breaker, changing an inverter, shutting down an engine, changing a guidance mode, or losing a communications path changes defined state variables and dependencies. Downstream indications and consequences follow from those state changes instead of requiring a bespoke authored branch for each combination.

## Why a complete spacecraft emulator is also the wrong first target

The project's existing decision-relevant causal-fidelity rule remains useful. A true simulator does **not** require immediate six-degree-of-freedom, circuit-level, fluid-dynamic, thermal, or software-cycle emulation of the entire spacecraft.

The required fidelity is **causal completeness for supported gameplay decisions**:

- if a player can take an action, the engine must represent the important consequences of that action;
- if a failure can occur, the engine must represent the important downstream effects and observations;
- if a controller decision depends on a measurement, the model must explain where that measurement comes from and how it can become stale, unavailable, misleading, or changed;
- unsupported internal detail may remain abstracted until a scenario/action depends on it.

This suggests a modular hybrid engine composed of discrete state machines plus continuous or algebraic models where needed.

Examples:

- electrical: buses, sources, loads, contactors/breakers, inverter selection, voltage/frequency availability, current draw;
- propulsion: engine commanded state, valve/configuration state, propellant/pressurization conditions, thrust level, shutdown/restart eligibility;
- guidance/control: computer/program mode, attitude/reference state, control authority, gimbal/RCS availability;
- communications: antenna/path/transmitter/receiver configuration, link availability/quality, telemetry/uplink/ranging consequences;
- consumables: time-dependent depletion rates that change with equipment/configuration;
- instrumentation: sensor source, signal conditioning, telemetry availability, freshness/validity, onboard indication path.

Not every domain needs the same mathematical sophistication.

## Simulator-documentation value

Historical simulator documentation could be extremely valuable because it may reveal exactly how Apollo-era training systems simplified these same causal problems. Particularly valuable targets are:

- simulator functional descriptions;
- mathematical-model descriptions;
- malfunction insertion inventories and definitions;
- instructor-station manuals;
- simulation-computer interface/control documents;
- subsystem model specifications;
- mission-simulator/MCC integration documents;
- validation/correlation reports showing what simulator behavior was considered adequate.

These could provide:

- model boundaries;
- state variables;
- simplified equations;
- discrete failure modes;
- cause/effect mappings;
- timing assumptions;
- which indications changed under each malfunction;
- which underlying 'true' values versus displayed/telemetry values were maintained separately.

However, simulator documentation alone is unlikely to be complete enough to build the whole project. The expected source stack is:

`original simulator documentation where available + spacecraft handbooks/specifications + subsystem engineering reports + malfunction procedures + telemetry/instrumentation documentation + flight rules/controller documentation`

The original simulator can guide **how to abstract**; the spacecraft documentation still establishes **what the system does**.

## Crew representation decision support

For this project, the crew should not be another human Mission Control player role. The player experience is Mission Control; adding a separate crew player creates a different game and introduces a player who has a radically different information/action environment.

A simulated crew is also consistent with the architecture above: the crew is part of the controlled environment with which CAPCOM interacts.

Initial implementation can be deliberately simple:

- CAPCOM transmits a structured instruction/message;
- the crew model recognizes supported message/action types;
- after a source-/scenario-bounded delay or at the appropriate procedural point, the model emits a canned acknowledgement/report and performs the associated cockpit action;
- the action changes authoritative spacecraft state through the same causal engine used for all other actions;
- crew reports remain a separate observation channel and do not automatically reveal hidden physical truth.

Example:

`CONTROL callout → CAPCOM transmission → crew acknowledgement → crew STOP action → DPS physical state changes → telemetry/crew report consequences`

The current validation harness already separates these stages. The next step is to move them from facilitator button presses into a deterministic/sourced simulated-crew response layer.

## What should remain scripted

A causal engine does not eliminate scenario scripting. Scripted elements remain appropriate for:

- external failures/malfunction injections;
- environmental/network conditions not generated by the modeled vehicle;
- historically fixed ground/crew communications when reproducing a known case;
- scenario setup and initial conditions;
- scheduled mission-plan events that are genuinely independent of player action;
- exercise-control cues.

The key change is that scripted events should change state or present information; they should not directly decree the final consequence when that consequence ought to emerge from the modeled state.

## Proposed next research/build sequence

1. Search specifically for Apollo CSM/LM mission-simulator functional descriptions, instructor/malfunction manuals, mathematical-model documents, and integration specifications.
2. Choose one narrow subsystem chain already represented in PC+2—preferably DPS/electrical—and replace the current event-driven consequence with a small causal model.
3. Implement the simulated crew as a deterministic message/action responder for the existing CAPCOM shutdown path.
4. Extend the validation test screen so actions can be issued and the resulting state/observations inspected without pretending to be a final station UI.
5. Add consequence tests that deliberately take correct, omitted, late, and wrong actions and verify that downstream state and evidence differ logically.
6. Expand subsystem fidelity only when a supported action/failure requires it.

## Current conclusion

The user's concern is well founded: authoring every possible outcome as a branch is not a sustainable architecture for the intended simulation. The historical Apollo program itself relied on closed-loop mission simulators, mathematical/system models, and malfunction insertion. The project should therefore treat the present scripted PC+2 timeline as a **validation scaffold**, not as the long-term simulation architecture.

The appropriate target is a modular, stateful, causal simulation engine with scenario-driven initial conditions/failures and a simulated crew interacting through CAPCOM.

See `resources/source-catalog/APOLLO_SIMULATION_ENGINE_SOURCES.md`.
