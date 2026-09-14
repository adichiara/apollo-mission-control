# 135 — Public Apollo Mission Simulator Instructor Handbook extraction

Status: **reviewed primary-source scan; early AMS applicability only**

## Source identity

- North American Aviation, Space and Information Systems Division.
- *Preliminary Apollo Mission Simulator Instructor Handbook, Volume II: Operation & Utilization*.
- Document `SM6T-2-02` / `SID 65-974-2`.
- 1 July 1965.
- Contract NAS 9-150.
- Public scan: https://ibiblio.org/apollo/Documents/19730060784_1973060784.pdf
- Public archive index: https://ibiblio.org/apollo/Documents/

The scan is publicly readable without the account gate encountered at Scribd.

## Scope correction

This specific scan is an **Apollo Mission Simulator (AMS)** handbook, not the *Lunar Module Mission Simulator (LMS) Instructor's Handbook*. The same archive separately indexes `lms_instructors_handbook_vol1.pdf`:

https://www.ibiblio.org/apollo/Documents/lms_instructors_handbook_vol1.pdf

The two simulator lineages must remain distinct in project notes.

## Document warning and applicability

The handbook labels itself preliminary and says its contents were not to be considered verified until the simulator hardware had passed acceptance demonstration. It also says the handbook was not design-requirements data.

Therefore:

- it is strong primary evidence for the intended initial AMS operating/model architecture;
- it is not proof that every described behavior survived acceptance unchanged;
- it is not automatically evidence for the later Block II or Apollo 13 configuration;
- it must not supply Apollo 13 constants without mission/configuration cross-checking.

## Extracted model architecture

### Program partition

The handbook divides computer programs into operational and diagnostic programs. It identifies five operational program types (scan pages 116–117):

1. vehicle dynamics;
2. vehicle systems;
3. simulation effects;
4. simulator control;
5. Mission Simulation Control Center interface.

Vehicle-dynamics programs calculate equations of motion, aerodynamics, and time-varying weight and balance. The resulting geographic/celestial position and attitude drive visual systems and simulated spacecraft instruments.

### Closed causal feedback

The equations-of-motion outputs feed programs that provide subsequent equations-of-motion inputs, continually updating the solution from continued thrust (scan pages 118–120).

The documented chain includes:

- thrust and firing commands;
- mass and weight/balance state;
- translational and rotational equations;
- integrated velocity and position;
- acceleration and radius vector;
- spacecraft guidance/control inputs;
- instrument and visual-system drive values.

This is direct primary evidence for an iterative causal simulator rather than a table of scripted outcomes.

### Truth, onboard, visual, and ground interfaces

The stabilization/control and guidance/navigation simulations receive rates, acceleration, position/radius, and direction-cosine data from the dynamics solution. Visual systems receive position, direction cosines, and rotational rates (scan page 118).

In integrated operation, selected local equations-of-motion velocity, position, or acceleration outputs could be replaced by Mission Simulation Control Center data. Uplink originated through the control-center interface (scan pages 144–147).

This supports explicit interface seams between:

- authoritative/local dynamics;
- simulated onboard systems;
- display/visual products;
- external mission-control simulation;
- uplink and communications paths.

It does not establish that our software must reproduce the original computer/network topology.

### Malfunction insertion

The Malfunction Insertion Unit allowed manual, preprogrammed, and time-dependent entries. A master program distributed malfunction commands to the simulator computers, validated entries, and recorded them (scan pages 43 and 141–142).

The telemetry simulation used modeled spacecraft-system data, while the MIU could also insert malfunctions directly into telemetry (scan page 147). This is strong evidence that a displayed/telemetered fault could be distinct from a physical subsystem fault.

### Training and output documentation

The handbook says Volume III contained:

- complete simulated-malfunction entries;
- crew and instructor manifestations;
- expected responses;
- links to system flow diagrams;
- simulation-output tables grouped by program, with program/math-model designators, addresses, functional descriptions, and scaling (scan page 226).

It also emphasizes that the prepared syllabus covered only a fraction of possible situations. This supports reusable causal models and instructor-authored exercises rather than exhaustive scenario branches.

## Project implications

The source strengthens these project boundaries:

- keep physical truth separate from indications, telemetry, and controller products;
- model failures at the physical, instrumentation, communications, or telemetry layer explicitly;
- keep dynamics, subsystem, simulation-effect, control, and external-interface concerns separable;
- let instructor/scenario inputs alter conditions or observations rather than directly selecting narrative outcomes;
- preserve enough provenance to distinguish historical simulator behavior from modern implementation choices.

## What this note does not authorize

This extraction does **not** freeze:

- an Apollo 13 vehicle model;
- numerical equations, constants, reference frames, or timestep;
- the AMS computer/network layout as a project architecture requirement;
- every listed malfunction as implemented or accepted;
- LMS-specific behavior.

The next useful AMS extraction is Volume III's malfunction and output tables. The next LMS extraction remains the separately archived Volume I handbook and mathematical-model reports.
