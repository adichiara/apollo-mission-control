# PC+2 Onboard Thrust-Monitor Source Addendum

Status: **active supplement to `PC2_IMPLEMENTATION_SOURCES.md`**

## Mission Operations Report — Apollo 13

- **Organization:** NASA Flight Control Division, Manned Spacecraft Center
- **Date:** 28 Apr 1970
- **Status:** PRIMARY / REVIEWED
- **Use:** establishes distinct PC+2 thrust criteria: approximately 85-psi ground chamber pressure and approximately 77-percent onboard thrust.
- **Caution:** does not identify the exact onboard percent-thrust instrument/signal.

## Apollo 13 technical/PAO air-ground transcript

- **Interval:** approximately 76:30–76:38 GET
- **Status:** PRIMARY / REVIEWED
- **Use:** CAPCOM calls the crew-side criterion a “thrust monitor readout, 77 percent or below”; crew readback repeats the thrust-monitor threshold.
- **Caution:** transcript wording alone does not identify P47, a physical gauge, or the signal path.

## LM guidance program documentation

- **Status:** PRIMARY TECHNICAL / REVIEWED-PARTIAL
- **Use:** distinguishes LM P40 (DPS powered flight) from P47 (Thrust Monitor).
- **Key constraint:** PC+2 was executed in P40; the existence of P47 does not justify mapping the 77-percent rule to P47 without direct procedure evidence.

## LM thrust-to-weight indicator technical material

- **Status:** PRIMARY TECHNICAL / REVIEWED-PARTIAL
- **Use:** establishes a crew thrust-related indicator as an accelerometer/thrust-to-weight display calibrated in lunar-gravity terms.
- **Key constraint:** reviewed material does not establish a percent-thrust scale or a 77-percent readout, so it is not used as the PC+2 crew criterion.

## Research record

- `resources/research/061_pc2_onboard_thrust_monitor_observation_path.md`

## Current gap

The exact onboard percent-thrust indication/source remains unresolved. `crew_thrust_monitor` therefore remains `NOT_EVALUABLE` until a mission-era crew/display or DPS-control source identifies it strongly enough to implement.
