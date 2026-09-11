# Research Note 004 — Support Rooms and Ground Processing

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Question

How much of the controller's apparent capability actually depended on personnel and systems outside the MOCR?

## Primary source

**Report of Apollo 13 Review Board — Appendix A, Part A4**

https://ntrs.nasa.gov/api/citations/19700078804/downloads/19700078804.pdf

Relevant printed pages A-131 through A-137.

## Findings

### Staff Support Rooms were integral

The source states that each MOCR group had an SSR supporting the activities required by the MOCR positions.

This means an authentic front-room role is not merely "one engineer looking at one screen." It is the visible leader/interface of a larger discipline capability.

### Flight Dynamics SSR

Provided detailed analysis of:

- launch parameters
- reentry parameters
- maneuver requirements
- orbital trajectories
- trajectory and guidance questions

It also interfaced with MPAD and external program/contractor representatives.

### Flight Director's SSR

Supported:

- Flight Director
- AFD
- Data Management Officer
- FAO

It also supported detailed communications-system monitoring and maintained Ground Timeline and Flight Plan TV-channel displays.

### Vehicle Systems SSR

Monitored detailed status/trends and worked on:

- failure avoidance
- failure correction/circumvention
- malfunction detection
- malfunction isolation

This is especially important for simulation design: the front-room systems controller's historically available reasoning support did not come solely from what one person could derive in real time.

### Life Systems SSR

Provided detailed physiological/environmental monitoring related to crew and environment.

### SPAN

The Spacecraft Planning and Analysis Room linked:

- MOCR
- data-analysis teams
- vehicle manufacturers
- KSC launch operations

and initiated analysis of spacecraft anomalies.

## CCATS

CCATS interfaced MCC with MSFN sites and handled the data path for:

- telemetry
- command
- tracking
- administrative information

The documented command path included Real-Time Command, Load Control, and CCATS command positions.

Telemetry and tracking had dedicated controller positions before the information reached MOCR consumers.

## RTCC

The RTCC performed:

- telemetry processing
- storage
- limit sensing
- trajectory/ephemeris calculations
- command-load generation
- display generation

A Tracking Data Selection Controller explicitly evaluated tracking-data quality and informed FIDO about data quality/status.

The Telemetry Processing Controller could access telemetry entering/leaving RTCC and kept MOCR/SSR users informed of telemetry-processing status.

## Simulation implication

The authoritative simulation should preserve at least the *logical* separation:

```text
physical state
  -> measured/instrumented state
  -> received network data
  -> ground processing/computation
  -> controller product/display
```

How much of CCATS/RTCC is modeled in detail remains open. But direct player access to physical truth would erase documented failure and uncertainty boundaries.

## Open issue: backroom abstraction

For practical player counts, many SSR roles will probably not be human-controlled initially.

No abstraction has been selected yet.

Potential approaches must be evaluated later against the actual work:

- automated support output
- embedded staff recommendations
- player-accessible secondary products
- dedicated support-role players
- selective omission where a mission phase genuinely does not need the function

No choice should be made until the first scenario's support-room workload is documented.
