# LM mission simulator mathematical-model source discovery

Date: 2026-09-14  
Status: **high-value source discovery / extraction target**

## Why this matters

The project has now chosen a causal numerical simulation direction: player/CAPCOM/crew actions should alter authoritative spacecraft state, and downstream trajectory, power, consumables, instrumentation, telemetry, and controller products should emerge from that state rather than from an exhaustive pre-authored branch tree.

A key research question is whether surviving Apollo simulator documentation exposes the mathematical abstractions, state variables, subsystem couplings, and malfunction boundaries NASA/contractors themselves considered sufficient for realistic training.

The answer is now clearly **yes, at least in part**.

## Direct LM mission-simulator mathematical source recovered

Virtual AGC's document library contains:

**Proposal for LEM Mission Simulator, Volume II, Technical Addendum: Glossary of Symbols**  
Link Group - Systems Division, General Precision, Inc.  
Public scan: https://www.ibiblio.org/apollo/Documents/proposal_for_lem_mission_simulator_vol2.pdf

The Virtual AGC catalog explicitly notes that, despite the title, this document contains numerous flowcharts showing the mathematical equations underlying the Lunar Module Mission Simulator.

This is qualitatively different from a training-procedure or user-interface manual. It is direct evidence about the mathematical model design of the LMS and is therefore a priority extraction source for the project's own causal engine.

### Source status

- public digital copy: **located**
- provenance: contractor proposal/technical addendum for the LEM/Lunar Module Mission Simulator
- usefulness: **very high**
- exact mission-era applicability: requires section-by-section review; it is a simulator-design source, not automatically Apollo-13-specific vehicle configuration
- next action: extract equation/flowchart families, modeled state variables, subsystem coupling, and assumptions without copying unsupported adjacent-configuration details into the Apollo 13 profile

## LM Mission Simulator Instructor's Handbook

Virtual AGC also identifies:

**Lunar Module Mission Simulator Instructor's Handbook, Volume I - Simulator Description**

The catalog describes this manual as containing details on switches/displays and on how the simulator's subsystems are simulated.

NASA documentation independently references the companion **Lunar Module Mission Simulator Instructors Handbook, Volume II, Sections II and III, LMA790-2-LMS, 1 April 1967** in Apollo LM descent/phasing work (NTRS document 19700026546).

This gives a strong document lineage:

- simulator-description material explaining subsystem representation;
- instructor/operations material explaining how the simulation is run;
- technical-addendum material exposing mathematical equations/flowcharts.

That combination is exactly the source family needed to reconstruct abstraction boundaries rather than invent them.

## Apollo Mission Simulator evidence is similarly useful

The surviving Apollo Mission Simulator instructor material is also unusually valuable.

The AMS Instructor Handbook describes the AMS as simulating spacecraft system performance and flight dynamics through computer-controlled system parameters, dynamics, and visual perspective. Its instructor station includes a Malfunction Insertion Unit.

The companion operations/utilization material describes:

- manual malfunction insertion;
- preprogrammed malfunction insertion;
- time-dependent malfunction insertion;
- computer-initiated malfunction handling;
- malfunction status;
- system-specific malfunction codes;
- a complete malfunction section in Volume III;
- simulation-output tables associated with program/math-model designators.

The output-table description is particularly important because it indicates that simulator parameters were organized by **program and/or mathematical-model designator**, giving a possible route to reconstruct the original simulator's model partitioning and observable variables.

## Strong architecture implication

The source base now supports a more precise project target than simply "use physics where useful."

The reusable simulation engine should be structured so that each domain can be traced to a model boundary:

```text
scenario/failure inputs
        |
        v
physical / logical subsystem models
        |
        +--> dynamics / trajectory
        +--> propulsion
        +--> electrical
        +--> consumables
        +--> guidance / control
        +--> communications
        |
        v
instrumentation / onboard indication
        |
        v
telemetry / ground processing
        |
        v
controller products
```

Each modeled subsystem should eventually document:

- authoritative state variables;
- algebraic/continuous/discrete equations;
- integration/update rate;
- inputs from other subsystems;
- outputs to other subsystems;
- switch/crew/controller command effects;
- failure injection points;
- sensor/telemetry derivation;
- fidelity/source provenance;
- known omissions.

That is substantially closer to the architecture used by real training simulators than an authored event tree.

## Burn-error example

The project's desired behavior for arbitrary player error can be expressed directly in the model.

A CAPCOM burn instruction should define command variables such as:

- ignition GET;
- burn duration or cutoff condition;
- engine/throttle selection;
- target attitude / thrust direction;
- any guidance-mode/configuration commands.

The simulated crew performs those actions. The propulsion model generates thrust and mass flow. The attitude model resolves thrust direction. The dynamics propagator integrates acceleration into velocity/position. The resulting trajectory drives later tracking/RTCC/controller products.

Therefore a wrong burn time, duration, throttle, or attitude does **not** require a pre-authored branch. It is simply a different input trajectory through the same equations.

## Research priorities from here

1. Extract the LM simulator technical addendum systematically by subsystem/equation family.
2. Locate and review the LM Mission Simulator Instructor's Handbook Volume I scan and relevant Volume II sections.
3. Search the AMS manuals for Volume III malfunction tables and simulation-output tables, especially program/math-model designators.
4. Search for LMS/AMS mathematical-model specifications, computer-program descriptions, acceptance/correlation tests, and simulator-output dictionaries.
5. Compare the simulator abstractions against Apollo 13 LM-7 spacecraft handbooks and subsystem documentation before adopting values/configurations.
6. Use the first implementation slice to validate architecture, not to maximize fidelity: propulsion + attitude + trajectory is the strongest initial numerical chain, with electrical/consumables next.

## Evidence boundary

The newly located simulator documents support the existence of mathematical and subsystem simulation structure. They do **not** yet justify reproducing any specific equation, constant, failure mapping, sample rate, or Apollo-13 configuration until the relevant pages are extracted and cross-checked.

The simulator documentation should guide abstraction and model topology. Mission/vehicle-specific spacecraft documentation remains authoritative for Apollo 13 configuration where the two differ.
