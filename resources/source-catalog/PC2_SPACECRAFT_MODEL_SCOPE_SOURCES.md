# PC+2 spacecraft physical-model scope sources

Date reviewed: 2026-09-13

Purpose: constrain how much spacecraft physics the Apollo 13 PC+2 first playable needs. These sources support a decision-relevant causal model; they do not justify silently simplifying a historically required mechanism.

## Primary sources

### Apollo Experience Report — Lunar Module Instrumentation Subsystem

- NASA TN D-6845, David E. O'Brien III and Jared R. Woodfill IV, Manned Spacecraft Center, June 1972.
- Stable copy reviewed: https://www.ibiblio.org/apollo/Documents/19720018206.pdf
- NASA/NTRS document ID: 19720018206.
- Status: **REVIEWED for model-scope question**.
- Relevant evidence: LM instrumentation processed approximately 250 measurements for display, caution/warning, and telemetry; the subsystem monitored LM systems and prepared data for MSFN transmission.
- Scope consequence: preserve physical-state → sensor/conditioning → telemetry/product → controller-interpretation separation, while modeling only channels needed by this scenario.

### Apollo Experience Report — Descent Propulsion System

- NASA TN D-7143, William R. Hammock Jr., Eldon C. Currie, and Arlie E. Fisher, 1973.
- NTRS record: https://ntrs.nasa.gov/citations/19730011150
- Status: **REVIEWED-PARTIAL for model-scope question**.
- Relevant evidence: DPS comprises pressurization, propellant storage/feed, engine, and guidance/control interfaces and is a pressure-fed throttleable system.
- Scope consequence: model the causal state required by PC+2 execution, the ΔP branch, shutdown/restart, chamber-pressure evidence, and maneuver outcome; do not infer a requirement for full thermofluid engine simulation.

### Apollo Experience Report — Guidance and Control Systems: Lunar Module Stabilization and Control System

- NASA TN D-8086, D. Harold Shelton, Johnson Space Center, November 1975.
- Stable reviewed copy: https://www.ibiblio.org/apollo/Documents/Apollo%20Experience%20Report%20Guidance%20and%20Control%20Systems%20Lunar%20Module%20Stabilization%20and%20Control%20System.pdf
- Status: **REVIEWED-PARTIAL for model-scope question**.
- Relevant evidence: the stabilization/control subsystem provides LM attitude and translation control and interfaces with guidance, DPS, and RCS.
- Scope consequence: model authoritative attitude/guidance/control state required by sourced criteria, maneuver execution/residuals, and PTC preparation; full six-degree-of-freedom or jet-pulse simulation is not yet required.

### Apollo Experience Report — Lunar Module Electrical Power Subsystem

- NASA TN D-6977, Arturo B. Campos, Manned Spacecraft Center, September 1972.
- NTRS record: https://ntrs.nasa.gov/citations/19720025198
- Status: **REVIEWED-PARTIAL for model-scope question**.
- Relevant evidence: LM electrical power is an integrated spacecraft subsystem whose configuration and flight performance determine equipment availability.
- Scope consequence: model coarse source/bus/inverter/load configuration sufficient to distinguish maneuver power-up from post-burn partial power-down and govern selected equipment availability; do not add breaker-, wire-, or battery-chemistry detail without a scenario dependency.

### Apollo Experience Report — Lunar Module Communications System

- NASA TN D-6974, R. H. Dietz, D. E. Rhoades, and L. J. Davidson, Manned Spacecraft Center, September 1972.
- NTRS record: https://ntrs.nasa.gov/citations/19720023255
- Status: **REVIEWED-PARTIAL for model-scope question**.
- Relevant evidence: LM communications supported voice, telemetry, ranging information, and links among LM, MSFN, CSM, and crew.
- Scope consequence: model communications/uplink/ranging availability where it affects INCO, CAPCOM, telemetry, or final-load operations; RF propagation and detailed modulation remain outside the current slice.

### Apollo 13 Mission Operations Report / PC+2 chronology

- Existing project catalog/source trail: see `PC2_FINAL_LOAD_UPLINK_SOURCES.md`, `PC2_POSTBURN_SOURCES.md`, and research notes 098–101.
- Status: **REVIEWED-DETAILED for the selected PC+2 interval**.
- Relevant evidence: ties DPS, guidance, communications/uplink, telemetry, maneuver result, and the post-burn power-down/PTC transition to actual Apollo 13 operational decisions.
- Scope consequence: these mission-specific dependencies determine which generic LM subsystem mechanisms are required in the first playable.

## Boundary

These sources do **not** establish that omitted spacecraft systems were historically unimportant. They establish only that the selected first-playable controller decisions can be supported without complete emulation of every LM/CSM subsystem.

Research note 102 is the interpretation record. A later scenario must reopen this scope if its sourced controller decisions depend on additional physics.