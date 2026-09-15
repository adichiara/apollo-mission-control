# Research Note 170 — Apollo Mission Simulator Technical Sources

**Date:** 2026-09-11  
**Status:** SOURCES IDENTIFIED

## Objective

Identify documentation that can constrain the underlying spacecraft-simulation model rather than reconstructing it solely from flight hardware handbooks.

## Lunar Module Mission Simulator

The Virtual AGC document collection reports a surviving:

**Lunar Module Mission Simulator Instructor's Handbook, Volume I — Simulator Description**

The collection description states that this manual contains detail on:

- simulator switches;
- displays;
- how LM subsystems were simulated.

A companion technical addendum is described as containing flowcharts and mathematical equations underlying the Lunar Module Mission Simulator.

This is potentially a high-value source for:

- subsystem model boundaries;
- simulator inputs/outputs;
- simulated failures;
- sensor/indicator behavior;
- simulator fidelity and simplifications;
- instructor controls.

## Apollo Mission Simulator

The same collection also preserves Apollo Mission Simulator Instructor Handbook material for Command Module spacecraft simulators.

Recent additions include:

- **Apollo Mission Simulator Instructor Handbook, Spacecraft 012, Volume I — Description and Utilization**
- **Volume II — Instructor Workbook**

Although Spacecraft 012 is a Block I vehicle and therefore not an Apollo 13 configuration source, the documents may reveal the simulator architecture and instructor/failure-injection methodology.

## Additional recent simulator documents

The Virtual AGC collection also identifies:

- a Lunar Module Simulator user's manual;
- a Lunar Module Simulator console directory described as listing available telemetry measurements;
- LM-7/8/9 elementary functional diagrams covering the Apollo 13 LM family;
- LM instrumentation study material.

## Research significance

These documents provide a separate evidence path from flight hardware documentation.

For this project we should distinguish:

```text
REAL SPACECRAFT DOCUMENTATION
        ↓
what the hardware physically did

MISSION CONTROL DOCUMENTATION
        ↓
what controllers could see/do

NASA/SINGER SIMULATOR DOCUMENTATION
        ↓
how NASA itself chose to simulate the hardware
and inject/observe failures
```

Where simulator documentation survives, it may answer implementation questions more directly than deriving a new simulation from first principles.

## Important caution

A simulator model is not automatically identical to the spacecraft.

Any simulator simplification must be documented as a simulator behavior, not mistaken for the actual vehicle physics.

## Sources

- Virtual AGC change log / document library:
  https://www.ibiblio.org/apollo/changes.html

- Virtual AGC document library:
  https://www.ibiblio.org/apollo/links.html

## Priority

High, particularly for the LM-7/Apollo 13 baseline and for future SimSup failure injection research.
