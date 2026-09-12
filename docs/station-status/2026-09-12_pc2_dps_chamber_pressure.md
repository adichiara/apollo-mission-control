# Station Research Status Addendum — PC+2 DPS chamber pressure

Date: 2026-09-12  
Affected station: **CONTROL**  
Maturity: **B — unchanged**

## New evidence

Research note `055_pc2_dps_chamber_pressure_observation_path.md` closes a useful portion of the PC+2 propulsion-monitoring path.

Primary mission-era LM-7-family diagrams identify:

- `GQ6510P` — **PRESS, THRUST CHAMBER**.

The Apollo 13 Flight Control Division Mission Operations Report independently establishes approximately **85 psi ground chamber pressure** as a PC+2 shutdown criterion, distinct from the crew/onboard approximately 77-percent-thrust criterion.

A contemporary Apollo 10 DPS flight-evaluation report also documents `GQ6510P` as engine thrust-chamber pressure and demonstrates that chamber pressure was a real flight-analysis measurement. Its LM-4 sampling details are continuity evidence only and are not treated as Apollo 13 display cadence.

## Implementation consequence

CONTROL can now receive an explicitly modeled `dps.chamber_pressure_psi` product with source/provenance metadata, and the PC+2 ground chamber-pressure rule can be evaluated when such a value is supplied.

The nominal PC+2 fixture still supplies no invented pressure value. A missing project value remains a deferred implementation field rather than simulated unavailable telemetry.

## Why maturity remains B

This work establishes the **measurement identity and operational rule path**, but does not yet establish:

- exact Apollo 13 GQ6510P PCM word/channel assignment;
- exact ground engineering conversion;
- certified GQ6510P → MSK 1137 `TCP` routing;
- Apollo 13 controller-display update cadence;
- exact nominal PC+2 chamber-pressure trace;
- the separate onboard 77-percent-thrust indication path.

CONTROL therefore remains at maturity **B**: strong mission-specific workflow and increasingly strong telemetry provenance, but incomplete exact controller-display reconstruction.

## Source record

See:

- `resources/research/055_pc2_dps_chamber_pressure_observation_path.md`
- `resources/research/034_apollo13_msk1137_non_lgc_telemetry.md`
- `resources/source-catalog/PC2_IMPLEMENTATION_SOURCES.md`
