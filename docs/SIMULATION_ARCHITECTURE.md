# High-Level Simulation Architecture

Status: **initial project architecture**, not a claim that Apollo software was structured this way.

The component boundaries below are chosen so that documented Apollo information flow can be represented without exposing the underlying simulation state directly to players.

## Historical basis for the decomposition

Apollo Mission Control documentation describes MCC operations in terms of the Mission Operations Control Room (MOCR), Staff Support Rooms (SSR), Communications, Command and Telemetry System (CCATS), Real-Time Computer Complex (RTCC), Voice Communications System, Display/Control System, and the Manned Space Flight Network.

Those historical systems must be researched in detail before their behavior is reproduced. The software modules below are therefore placeholders for responsibilities, not assumptions about their internal implementation.

## Proposed software layers

### 1. Session / mission authority

Owns:

- selected mission/scenario
- simulation lifecycle
- mission elapsed time
- pause/reset controls for simulation administration
- connected stations
- authoritative ordering of commands/events

This is a software requirement of the multiplayer simulation.

### 2. Physical mission state

Authoritative model of the spacecraft/trajectory/crew/ground conditions required by the selected scenario.

Possible subsystem boundaries are not finalized until the first mission baseline is selected and documented.

Principle:

> Players do not read this state directly.

### 3. Instrumentation and telemetry

Transforms physical state into the measurements that would actually be available.

This layer is necessary to represent distinctions such as:

- actual physical condition versus measured value
- sensor/instrumentation failure
- unavailable data
- stale data
- different update rates

Exact behavior requires source support.

### 4. Ground communications and processing

Represents the documented path from received spacecraft/network data to controller-usable values and products.

Historical subjects to reconstruct include:

- MSFN data delivery
- CCATS
- RTCC
- ground-computed parameters
- data validation/quality
- display generation
- command/update paths

Do not collapse this into direct access to simulation variables where the historical distinction affects controller work.

### 5. Controller information services

Defines exactly what each controller position can request/observe.

For each position this eventually needs:

- display list
- parameters/products
- update characteristics
- display selection workflow
- voice/communication relationships
- applicable reference documents

### 6. Historical display renderer

Renders documented display formats.

Requirements will come from the MCC display-format research. Avoid generic "retro terminal" styling where an actual format can be reconstructed.

### 7. Station client

Phone/web interface for one assigned controller station.

The client should primarily:

- show the station's historically justified displays/controls
- allow documented display selection/input
- connect to the central server
- expose only the information appropriate to that station

Modern session controls (join/reconnect/settings) should be visually and functionally separated from the simulated console.

### 8. Simulation Control / scenario injection

Administrative layer for running nominal and nonnominal simulations.

Responsibilities may include:

- initial conditions
- scheduled/conditional events
- malfunction/failure injection
- ground/network failures
- crew/environment inputs
- operator controls

The historical Simulation Supervisor process must be researched before finalizing terminology and workflow.

### 9. Communications

Potentially represents documented voice loops and air/ground paths.

Initial in-person play may rely partly on natural room communication, but historical loop behavior should be researched before deciding which communication functions belong in software.

### 10. Reference/document package

Versioned set of the mission-specific material required for a session:

- flight rules
- procedures
- controller references
- tables
- timelines
- project-created indexes

This package should trace back to the source catalog.

### 11. Event/audit record

Records simulation events needed for reproducibility and post-simulation analysis:

- scenario events
- player commands/input
- system changes
- session joins/disconnects
- communications events if represented in software

This is not an in-play scoring system.

## Conceptual data flow

```text
PHYSICAL MISSION STATE
        |
        v
INSTRUMENTATION / TELEMETRY
        |
        v
COMMUNICATIONS / GROUND PROCESSING
        |
        +-------------------------+
        |                         |
        v                         v
CONTROLLER INFORMATION       COMMAND / UPDATE PATHS
        |                         |
        v                         |
HISTORICAL DISPLAY               |
        |                         |
        v                         |
STATION CLIENT ------------------+
        |
        v
PLAYER INTERPRETATION / COMMUNICATION / DECISION
```

The exact paths and responsibilities in this diagram are research targets. Where Apollo documentation shows a materially different path, this architecture must change to match it.

## Deployment constraint already known

The project is intended to run from a central server hosted on Render with players connecting from phones.

Specific web framework, database, WebSocket implementation, frontend framework, and persistence strategy remain open until simulation requirements are better defined.


## Mission-era configuration profiles

The reusable simulation should distinguish the **common Apollo platform** from a **mission-specific historical profile**.

Current design direction:

- use the Apollo 13-era MCC configuration as the default technical baseline/superset for shared implementation;
- apply mission-specific configuration data for Apollo 11, Apollo 12, Apollo 13, and later scenarios;
- allow a mission profile to change nomenclature, controller availability, display sets, procedures, rules, telemetry/configuration, console capabilities, and spacecraft/ground-system details where sources establish differences.

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
