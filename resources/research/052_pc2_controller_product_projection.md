# Apollo 13 PC+2 — controller-product projection boundary

Date: 2026-09-12  
Status: **REVIEWED — sufficient to implement the first controller-product projection layer without claiming unsupported CRT formatting or telemetry cadence**

## Question

What should the first executable model expose to controller stations, and how should implementation gaps be represented without confusing them with historical telemetry failures?

## Primary-source basis

### AS-508 MCC/MSFN Mission Configuration/System Description — March 1970

The Apollo 13-era MCC/MSFN configuration describes command, communications, telemetry, tracking, and MCC interfaces as distinct operational paths. It supports the project architecture in which spacecraft/onboard state is received and processed before becoming a controller-facing product rather than being read directly from authoritative simulation state.

Source: NASA TM X-64290, NTRS 19700024253.

### Apollo 13 Mission Operations Report — 28 April 1970

The controller appendices and PC+2 chronology establish that different disciplines owned different observations and judgments during the maneuver. CONTROL monitored propulsion/control quantities and shutdown criteria; GUIDO monitored guidance/computer state and residuals; FIDO/RETRO owned trajectory/return products; TELMU monitored LM systems/power; INCO owned communications/data-path concerns; FLIGHT integrated controller recommendations; CAPCOM handled the crew communication path.

The report also preserves a useful counterexample to direct-state aliasing: elsewhere in the mission the RTCC incorrectly processed AGS body angles even though the spacecraft attitude was acceptable. Ground-derived product validity therefore cannot be assumed from spacecraft-state validity.

### Apollo Experience Report — Real-Time Display System

NASA TN D-8316 documents the Apollo real-time display system as an organized collection of display subsystems rather than a direct window into spacecraft state. This is a retrospective NASA engineering source, not mission-specific evidence for PC+2 field cadence or exact layouts, but it supports the architectural separation between data acquisition/processing and controller presentation.

Source: NASA TN D-8316 / JSC-S-461, NTRS 19760024152.

## Implementation consequence

The first executable projection layer should produce **station-specific products** carrying:

- value;
- units where applicable;
- source/sample/receive/process/display timestamps where known or modeled;
- validity (`valid`, `stale`, `invalid`, `unavailable`);
- source layer;
- provenance identifier.

The nominal prototype may initially use equal sample/receive/display times for modeled real-time values. That is a zero-delay software simplification, not a claim about exact Apollo CRT refresh timing.

## Critical distinction: historical availability vs implementation completeness

Some products are historically required for PC+2 but the current project deliberately lacks a defensible nominal numeric value, especially:

- DPS chamber pressure;
- DPS inlet pressure;
- fuel/oxidizer differential pressure;
- exact attitude-error components;
- exact body-rate components;
- actual LM burn-configuration current.

These must **not** be projected to players as `unavailable` merely because the project has not yet modeled their nominal values. Doing that would simulate a telemetry/data-path failure that did not occur historically.

Instead the projection layer should keep a separate `deferred_fields` / implementation-gap list. A field enters the actual controller product set only when its value path is modeled. Historical telemetry validity and project implementation status remain different concepts.

## First-pass station projection

### CONTROL

Project now:

- DPS engine running state;
- commanded throttle phase;
- ullage state / jet count;
- engine-gimbal warning state;
- CES DC failure state.

Deferred numeric fields remain explicitly listed rather than faked.

### GUIDO

Project now:

- LGC operating state;
- program/P40 state;
- LGC/program warnings;
- alignment acceptance;
- target/load status;
- planned PGNS Vg;
- post-burn residual product once it becomes available.

### FIDO / RETRO

Project now:

- final PC+2 target/PAD product;
- return-plan product;
- target/trajectory solution status at the level already documented in the fixture.

Exact Cartesian RTCC trajectory state remains deferred until propagation requires it.

### TELMU

Project now:

- LM power mode/configuration;
- documented expected burn-configuration current range as a reference product;
- inverter-warning state;
- power-down transition state.

Actual measured current remains deferred rather than replaced by the expected range.

### INCO

Project now:

- air-ground quality;
- voice/telemetry availability;
- ranging state;
- uplink configuration state.

### FLIGHT

Project only mission phase and FLIGHT-owned decision state. Do not expose a synthesized all-systems health dashboard.

### CAPCOM

Project the air-ground communication state, final maneuver-PAD information needed for read-up, and timestamped crew reports. Do not expose hidden subsystem state.

## Stop condition

This is enough to implement and test the product-projection architecture. Do not delay the vertical slice to reconstruct exact historical screen layouts or exact PC+2 CRT refresh rates unless a later player decision requires them.

## Next implementation step

After projection tests are deterministic, implement the documented PC+2 shutdown rules against controller-observable/modelled quantities without introducing a generic authoritative `burn_abort` state.
