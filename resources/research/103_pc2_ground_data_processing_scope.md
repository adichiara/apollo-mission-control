# Research Note 103 — PC+2 MSFN / CCATS / RTCC scope

**Date:** 2026-09-13  
**Status:** REVIEWED — first-playable scope boundary resolved

## Question

How much of MSFN, CCATS, and RTCC behavior materially affects Apollo 13 PC+2 controller decisions and therefore belongs in the first playable?

This note resolves open question 13 for the current PC+2 slice. It does **not** attempt to reconstruct the internal IBM/UNIVAC software, support-console keying, or full worldwide network.

## Primary sources reviewed

1. **Report of Apollo 13 Review Board, Appendix A — Baseline Data: Apollo 13 Flight Systems and Operations**, NASA-TM-X-66473, June 1970.  
   NTRS: https://ntrs.nasa.gov/citations/19700078804  
   Relevant material: Mission Support Areas, CCATS, RTCC, pp. A-133–A-137 (PDF pages approximately 164–168).
2. **Apollo MCC/MSFN Mission Configuration — Command, Communication, Telemetry, Tracking**, NASA-TM-X-64290, March 1970.  
   NTRS: https://ntrs.nasa.gov/citations/19700024253  
   Relevant material: MCC/MSFN architecture and RTCC general description.
3. **Apollo 13 Mission Report**, MSC-02680 / NASA-TM-X-66449, September 1970.  
   NTRS: https://ntrs.nasa.gov/citations/19710003598  
   Used as mission-specific context alongside the already documented PC+2 final-load/ranging evidence in notes 098–099.

## Findings

### 1. CCATS was the MCC ↔ MSFN data interface

The Apollo 13 Review Board describes CCATS as the interface between the Mission Control Center and MSFN sites. It handled reception, transmission, routing, processing, display, and control of telemetry, command, tracking, and administrative data.

For first-playable purposes, this establishes a **data-path function**, not a need to simulate a UNIVAC 494 or its operator consoles internally.

### 2. Command support extended from RTCC load generation through spacecraft acceptance

The CCATS Command Support Console operators were responsible for the command-data flow from generation and transfer of command loads from RTCC through verification of spacecraft acceptance after uplink execution.

This supports the staged final-load architecture already adopted in notes 098–099. It also shows that a successful load was not merely a single front-room boolean: a ground processing/transfer path existed between solution generation and spacecraft acceptance.

### 3. RTCC generated controller-relevant products

The Review Board states that RTCC provided MCC data-processing support including:

- telemetry processing, storage, and limit sensing;
- trajectory and ephemeris calculations;
- command-load generation;
- display generation;
- other mission logic processing/calculations.

The March 1970 MCC/MSFN configuration likewise describes RTCC as supplying controller display data and generating/transferring load data toward CCATS.

Therefore RTCC belongs in the simulator **where its products or availability affect a player decision**. Full internal computation does not.

### 4. Tracking-data selection and trajectory processing were explicit support functions

The Apollo 13 Review Board identifies an RTCC Tracking Data Selection Controller who monitored tracking data, selected the best usable source, evaluated trajectory determinations, and informed the Flight Dynamics Officer of data quality/status. It separately identifies Flight Dynamics Processing personnel who controlled and monitored trajectory-computation requests from MOCR flight-dynamics personnel.

This supports retaining a distinct concept of:

`tracking/ranging availability + quality → ground trajectory solution/product → FIDO/RETRO or GUIDO use`

It does **not** support giving FIDO omniscient raw network data or pretending every tracking station is directly player-controlled.

### 5. Command generation/transfer was coordinated with MOCR command responsibility

The RTCC Network and Command Processing function coordinated with MOCR personnel who held command responsibility and directed generation, review, and transfer of requested command loads.

That supports the existing separation between front-room operational authority and ground-computer/support processing. It does not justify creating new player authority for RTCC/CCATS support operators in the current slice.

## First-playable boundary

For PC+2, simulate **functional ground-data products and dependencies**, not ground-computer hardware/software internals.

Required ground-system state is limited to decision-relevant concepts such as:

- tracking/ranging data **available / unavailable** and, when needed, **usable / questionable**;
- trajectory/final-solution product **not ready / ready**;
- telemetry processing/data path **available / impaired** where a selected branch depends on it;
- command/load generation-transfer path **not ready / configured / transmitting / complete**;
- spacecraft acceptance/crew-side completion represented only when supported by the relevant workflow evidence.

These states may cause station products to be absent, stale, qualified, or unavailable. They must not leak hidden physical truth.

## What is not required now

Do not implement merely for completeness:

- IBM 360/75 execution or redundancy mechanics;
- UNIVAC 494 emulation;
- exact CCATS/RTCC operator console layouts or keystrokes;
- packet/message formats internal to MCC computers;
- full MSFN site scheduling/routing logic;
- complete worldwide tracking geometry;
- exact trajectory propagator internals;
- a playable CCATS, RTCC, or MSFN operator role;
- unsupported synthetic delays or failure rates.

A specific mechanism should enter the executable model only when a sourced controller decision or selected nonnominal branch requires it.

## Station consequences

- **FIDO/RETRO:** receives trajectory products and data-quality status, not unrestricted raw network truth.
- **GUIDO:** consumes guidance/load products downstream of ground solution processing; exact RTCC internals remain hidden.
- **INCO:** depends on communications/uplink/ranging availability but does not become the operator of CCATS internals.
- **CAPCOM:** owns crew-facing communication steps, not command-load computation.
- **FLIGHT:** coordinates readiness/decision consequences without an omniscient ground-system health display unless specifically sourced.

## Resolution

Open question 13 is **resolved for the current PC+2 first playable**:

> Represent MSFN/CCATS/RTCC as source-backed functional services that produce, qualify, route, or withhold controller-relevant data/products. Do not emulate internal ground-computer machinery unless a concrete scenario decision or failure mechanism requires it.

This is consistent with Decision D-019: causal fidelity is admitted by player-decision dependency rather than by subsystem completeness.
