# Research Note 003 — MOCR Positions and Responsibilities

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Question

What controller positions and responsibility boundaries are directly documented for the Apollo lunar-mission MOCR?

## Primary source

**Report of Apollo 13 Review Board — Appendix A, Part A4: Mission Control Center Activities**

https://ntrs.nasa.gov/api/citations/19700078804/downloads/19700078804.pdf

Relevant printed pages A-128 through A-130 (PDF pages 159–162 in the current scan).

## Findings

The source explicitly divides the MOCR into three operating groups.

### Mission Command and Control

- Mission Director
- Flight Operations Director
- Flight Director
- Assistant Flight Director
- Flight Activities Officer
- DOD Representative / Assistant
- Network Controller / Assistant
- Public Affairs Officer
- Surgeon
- CAPCOM
- Experiments Officer

The Flight Director is described as responsible for MOCR decisions/actions concerning vehicle systems, vehicle dynamics, and MCC/MSFN operations.

CAPCOM is explicitly responsible for voice communications with the flight crew and also functions as a crew-procedures adviser with FAO.

### Systems Operations

- CSM EECOM
- CSM GNC
- LM/TELCOM
- LM/CONTROL
- three Booster Systems Engineers
- INCO
- O&P / PROCEDURES

Responsibility boundaries are strongly spacecraft/subsystem based:

- EECOM ↔ CSM environmental/electrical/sequential
- GNC ↔ CSM guidance/navigation/control/propulsion
- TELCOM ↔ LM environmental/electrical/sequential
- CONTROL ↔ LM guidance/navigation/control/propulsion

INCO and O&P shared a console/responsibility area in the documented configuration.

### Flight Dynamics

- FIDO
- RETRO
- GUIDO
- YAW

The source distinguishes:

- FIDO: trajectory / mission feasibility / reentry trajectory
- RETRO: maintained reentry plan
- GUIDO: onboard guidance-monitoring and computer-update responsibilities
- YAW: second guidance officer without command functions

## Simulation implications

These are evidence constraints, not yet role-combination recommendations.

A future low-player-count design must preserve the fact that:

- spacecraft systems and trajectory/navigation were separate disciplines
- CSM and LM systems responsibilities were separate
- FIDO and GUIDO were not the same job
- FLIGHT was decision authority, not an omnibus technical monitor
- communications/procedures had their own operational responsibilities

## Remaining research

- mission-phase workload by position
- exact Apollo 11 differences from Apollo 13-era descriptions
- controller display ownership
- parameter availability
- loop topology
- exact command authority/workflow
