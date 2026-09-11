# Apollo 13 RETRO Station Specification

Status: **research specification — partial**

Purpose: reconstruct the Apollo 13 Retrofire Officer from mission-specific operational evidence.

RETRO is not simply an "abort button" position. Apollo 13 shows RETRO continuously maintaining return/reentry options while integrating trajectory, recovery, weather, spacecraft capability, clocks, targeting, and entry geometry.

---

## 1. Position

**Call sign / position:** RETRO / RFO  
**Apollo 13 Mission Operations Report:** Retrofire Officer

### Documented responsibility

Apollo Mission Control documentation assigns RETRO responsibility for:

- maintaining an updated abort/return/reentry plan throughout the mission;
- retrofire / return timing;
- landing and recovery geometry;
- entry planning;
- return-to-Earth contingency planning.

Apollo 13 turned this normal responsibility into one of the mission's central tasks.

---

# 2. Return planning existed before the accident

Before the CSM accident, RETRO already maintained:

- launch abort return plans;
- P37/RTE block data;
- weather-adjusted landing targets;
- LOI abort chart updates;
- return-to-Earth status products.

The report notes that abort/RTE block-data status was passed to FLIGHT before the accident.

### Simulation significance

RETRO has meaningful workload even in a nominal mission.

The role is not activated only after an emergency.

---

# 3. Mission abort became trajectory redesign

After the oxygen-tank failure, RETRO evaluated multiple return strategies.

The report preserves options including:

- direct return;
- free-return transfer / lunar flyby;
- PC+2 return-speed-up options;
- different landing oceans/areas;
- different return times;
- different ΔV requirements.

The selected approach:

1. execute an early maneuver to regain free return;
2. defer the major return-time/recovery-area choice until consumables were better known;
3. execute PC+2 to shorten the return and target the Pacific recovery area.

### Key point

RETRO's decision problem is inherently multi-variable:

- ΔV capability
- available propulsion system
- consumables/lifetime
- landing time
- landing area
- recovery assets
- weather
- entry geometry
- backup-entry feasibility

The simulator should not reduce this to a single "safe/unsafe return" flag.

---

# 4. Recovery/weather is operational data

RETRO repeatedly altered or evaluated return/entry plans because of recovery weather.

Examples include:

- Mode II weather;
- P37 block-data landing points;
- mid-Pacific target-area weather;
- weather near planned entry target;
- whether lift during entry could avoid bad weather.

### Station implication

A mature RETRO implementation needs access to recovery/weather products relevant to landing-area selection.

The weather source itself belongs to recovery/meteorology, not RETRO, but RETRO must use it.

---

# 5. Free-return maneuver selection

After the accident, RETRO computed return options for several TIGs.

The chosen free-return flyby maneuver was approximately:

- TIG: 61:29:42.84 GET
- ΔV: about 38 fps
- landing time: about 151:45 GET
- Indian Ocean landing geometry

The report also records coordination issues over:

- LM mass properties;
- DPS trim assumptions;
- ullage assumptions;
- clocks/timing.

The RETRO console clock was used to resolve a Mission Control timing confusion with the LGC.

### Simulation significance

Return planning depends on accurate:

- vehicle mass/configuration;
- propulsion assumptions;
- timebase;
- targeting state.

These are not abstract scenario variables.

---

# 6. PC+2 as a return-plan optimization

PC+2 did not merely "save the crew."

The maneuver was used to optimize:

- return time;
- recovery area;
- propellant margin;
- future midcourse capability.

Apollo 13 could remain on a free-return trajectory without PC+2, but PC+2 improved the practical recovery plan.

This is exactly the kind of outcome hierarchy the project intends to preserve:

> safe return may already be possible, while further decisions improve mission recovery quality and margin.

---

# 7. Entry planning

Near Earth, RETRO generated and updated:

- preliminary entry PAD;
- CMC clock update;
- state-vector update coordination;
- entry flight-path angle;
- final entry PAD;
- backup/roll-entry logic;
- landing point.

The report states that after new tracking showed the entry flight-path angle had changed, RETRO verified the trajectory, produced the final entry PAD, and coordinated the state-vector uplink.

The final reported entry flight-path angle was approximately -6.28 degrees.

---

# 8. Spacecraft separation / geometry

RETRO also handled return-related separation geometry.

During Apollo 13:

- the CSM could not use a normal SM jettison concept because of system limitations;
- RETRO modified contingency separation procedures;
- LM/CM separation direction and geometry were evaluated;
- an off-nominal yaw orientation before LM jettison was accepted after checking that separation distance remained adequate.

### Simulation significance

RETRO's responsibility includes whether a trajectory/entry plan remains safe under actual spacecraft attitude and separation geometry.

---

# 9. Clocks / timing

Apollo 13 RETRO work includes several explicit clock/time tasks:

- CMC clock drift monitoring;
- LGC/GET synchronization concerns;
- return-maneuver TIGs;
- entry timing;
- CMC clock update near entry.

The report even records a clock update later found to be off by 0.06 seconds because it was derived during low-bit-rate telemetry.

### Station implication

Mission time, onboard computer time, and RTCC/ground time cannot simply be assumed identical.

Timebase errors can affect guidance/entry products.

---

# 10. Information families justified by Apollo 13 evidence

## Return/abort products

- current return mode / option
- maneuver TIG
- maneuver ΔV
- required propulsion system
- predicted landing time
- predicted landing area
- free-return / non-free-return status

## Entry products

- entry flight-path angle
- target latitude/longitude
- entry PAD
- state-vector update status
- backup-entry geometry
- lift/roll implications

## Constraints

- vehicle mass/configuration
- propulsion capability
- consumables/lifetime
- weather
- recovery forces
- clock/timebase
- separation geometry

## Coordination data

- accepted FIDO trajectory vector
- GUIDO/CMC state-vector update status
- GNC/CONTROL propulsion/control capability
- recovery-area/weather updates

---

# 11. RETRO versus FIDO

## FIDO

Maintains/validates the ground trajectory solution.

## RETRO

Uses the accepted trajectory to maintain the practical return/reentry plan.

Apollo 13 demonstrates constant exchange between these roles, but they solve different problems.

---

# 12. Implementation status

## DOCUMENTED

- abort/RTE block-data maintenance
- weather/recovery integration
- free-return and PC+2 option analysis
- return-time / landing-area / ΔV tradeoffs
- entry PAD generation
- entry flight-path angle monitoring
- clock/timebase work
- separation/recovery geometry

## PARTIAL

- exact RTCC processors/products used for each return option
- exact return-plan display suite

## UNRESOLVED

- exact Apollo 13 RETRO console layout
- exact display IDs / MSK assignments
- exact entry/abort display pages
- exact clock panel / timing controls
- DRK/MSK assignments
- exact voice-loop configuration

---

# 13. Research targets

1. Locate RETRO display-format / RTCC return-to-Earth processor documentation.
2. Identify P37/RTE block-data displays and entry displays.
3. Locate RETRO console handbook.
4. Map entry/landing/recovery data products.
5. Reconstruct how recovery weather was delivered to RETRO.
6. Map FIDO-vector handoff into RETRO entry processing.

## Primary source

- *Mission Operations Report — Apollo 13*, Appendix B: Retrofire Officer.
  https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
