# Research Note 022 — Cross-Mission LM CRT Continuity Evidence

**Date:** 2026-09-11  
**Status:** CROSS-MISSION EVIDENCE

## Objective

Use documented displays before and after Apollo 13 to understand likely continuity while avoiding unsupported claims about Apollo 13 itself.

## Earlier Apollo ASPO 45 displays

The Apollo 11 AC Electronics Guidance & Navigation Summary explicitly lists:

- MSK 683 — CM
- MSK 966 — CM
- MSK 1123 — LM
- MSK 1137 — LM

### MSK 1123

The earlier display is a combined LM guidance/control/propulsion real-time page.

Its field descriptions include:

- LGC/AGS timing
- downlist/site identity
- TGO
- DAP/body rates
- AGS rate/ASA rates
- attitude commands
- gimbal/CDU/IMU/AGS attitude
- PGNS/AGS error
- moment/offset terms
- guidance-system velocities and delta velocities

### MSK 1137

The earlier display is strongly powered-descent/control oriented.

Fields include:

- timing
- site/downlink ID
- throttle select
- descent throttle command
- manual/auto/total throttle
- actuator position
- LGC commanded thrust
- thrust chamber pressure
- guidance/DAP attitude errors
- AGS error
- desired body rates
- engine-induced angular acceleration
- gimbal direction
- attitude-hold/auto state
- accumulated control torque

## Later Apollo mappings

Later NASA measurement tables explicitly map numerous LM telemetry parameters to primary MSK 1123 and 1137.

This confirms those displays remained real operational destinations for LM guidance/control/propulsion telemetry later in Apollo.

Examples mapped to 1123 include APS/DPS pressures, valve states, propellant quantities, thrust chamber pressure, and guidance/control quantities.

Examples mapped to 1137 include landing/rendezvous-radar status and radar-related data.

## Apollo 13 evidence

The Apollo 13 AC Electronics Guidance & Navigation Summary survives and contains an ASPO 45 CRT section.

Until those pages are extracted:

- 683/966/1123/1137 are **continuity candidates**, not Apollo 13 facts;
- field continuity is plausible but unconfirmed;
- Apollo 13-specific changes remain possible.

## Why this is useful now

The earlier/later evidence helps define what to search for and prevents us from designing an arbitrary LM display while we wait for the Apollo 13 scan extraction.

It does **not** authorize implementation as Apollo 13.

## Sources

- AC Electronics Apollo 11 Guidance & Navigation Summary:
  https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- Apollo 13 Guidance & Navigation Summary index:
  https://apollojournals.org/afj/ap13fj/a13-documents.html
- Apollo 17 Mission Evaluation Plan:
  https://ntrs.nasa.gov/citations/19730018126
- LM-10 Instrumentation Packet:
  https://www.ibiblio.org/apollo/Documents/LM-10_Instrumentation_Packet.pdf
