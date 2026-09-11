# Research Note 015 — NASA Simulator Configuration and Fidelity Practice

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Primary source

**NASA Manned Spacecraft Center — Flight Crew Operations Branch — Simulator Operations**  
Prepared by Riley David McCafferty  
14 February 1968

Public scan:
https://www.ibiblio.org/apollo/Documents/msc_simulator_operations.pdf

## Why this matters

This source describes how NASA actually maintained Apollo mission simulators as spacecraft configurations evolved.

It provides a process model for this project's own fidelity policy.

## Simulator fidelity was configuration-controlled

The report describes spacecraft changes entering the simulator through formal change processes.

Simulator personnel monitored:

- spacecraft Master Change Requests / change-board actions;
- engineering change orders;
- hardware/software changes;
- trajectory and mission-profile revisions.

A simulator change was reviewed for:

- system effectivity;
- design impact;
- documentation;
- installation;
- checkout;
- schedule.

NASA operational personnel reviewed the resulting implementation.

## Authoritative technical sources

For simulator hardware design, the report states that the primary descriptive data included the **Apollo Operations Handbook** and related spacecraft documentation.

For software changes, NASA supplied specifications to the contractor, the contractor modified simulator **Math Models**, and the revised behavior was checked against an accepted source such as:

- the modification request;
- Apollo Operations Handbook;
- spacecraft schematic.

This is direct evidence that the real simulator was expected to trace its behavior to controlled spacecraft documentation.

## Simulator configuration was not assumed perfect

The report openly tracks outstanding modifications/discrepancies and distinguishes:

- changes required to reach the target spacecraft configuration;
- simulator discrepancies;
- items mandatory for crew training;
- items desirable for crew training;
- NASA/external problems.

This is useful conceptually:

> a historical simulator itself can have known fidelity limitations.

If this project later reproduces a documented NASA simulator case, we should distinguish a simulator artifact from actual spacecraft behavior when evidence identifies the difference.

## Integrated training progression

The report describes a progression from:

- systems instruction;
- increasingly mission-plan-related simulator work;
- Mission Rules and procedure work;
- rendezvous/reentry/emergency procedure practice;
- ground-interface checkout;
- integrated MCC-Houston simulations.

For the typical example shown, approximately 45 days before launch the plan included roughly:

- 20 hours launch simulations;
- 40 hours simulated network simulations;
- 20 hours reentry simulations.

These values are from a 1968 CMS example, not an Apollo 13 schedule.

## Instructor-only capability

The report separately identifies **Instructor Aids**: displays, readouts, and real-time printing available at the Instructor Operator's Station and not part of the spacecraft configuration.

This is an important architecture distinction for our eventual SimSup interface:

```text
PLAYER / CONTROLLER-VISIBLE STATE
!=
SIMULATOR INSTRUCTOR / SIMSUP STATE
```

A SimSup interface may legitimately expose information that no controller player receives.

## Ground integration

The report repeatedly describes ground-interface checkout with MCC-Houston as preparation for integrated training.

This reinforces the principle that the spacecraft simulator and Mission Control should be coupled through the operational data/interface path rather than by direct ad-hoc failure messages to individual players.

## Project implications

1. Maintain mission/spacecraft configuration explicitly.
2. Trace subsystem behavior to controlled source material.
3. Record known simulation approximations separately from vehicle behavior.
4. Keep instructor/SimSup aids isolated from controller-visible interfaces.
5. Treat scenario reset points/training loads as configuration state, not merely narrative checkpoints.
6. Preserve provenance for changes to the simulation model.

## Sources

- NASA MSC, *Flight Crew Operations Branch Simulator Operations*, 14 February 1968:
  https://www.ibiblio.org/apollo/Documents/msc_simulator_operations.pdf

- Virtual AGC document library/change log for related simulator manuals:
  https://www.ibiblio.org/apollo/changes.html
