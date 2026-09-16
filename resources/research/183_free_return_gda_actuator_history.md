# Research Note 183 — Free-return GDA actuator history

**Date:** 2026-09-16  
**Status:** REVIEWED — exact 61:29 GDA actuator history recovered from primary postflight report

## Question

Can the project replace the unresolved/synthetic powered-flight GDA branch for the 61:29 Apollo 13 free-return DPS firing with mission-specific measured actuator positions?

## Primary source

NASA/MSC, *Apollo 13 Mission Report*, MSC-02680, September 1970, section 6.4, Table 6.4-I, NTRS citation `19710003598`.

NTRS: https://ntrs.nasa.gov/citations/19710003598

## Finding

Yes. Table 6.4-I, **Lunar Module Maneuver Summary**, gives Gimbal Drive Actuator position in **inches** for the second midcourse correction — the 61:29 free-return firing under `PGNCS/DPS` — at four phases:

| Phase | Pitch GDA, in. | Roll GDA, in. |
|---|---:|---:|
| Initial | -0.02 | -0.34 |
| Maximum excursion | +0.31 | -0.27 |
| Steady-state | +0.04 | -0.51 |
| Cutoff | +0.10 | -0.31 |

The same table identifies ignition `61:29:43.49`, cutoff `61:30:17.72`, and duration `34.23 s`, so the actuator column is unambiguously associated with the free-return maneuver.

This is the exact mission-specific postflight actuator history class that notes 154, 180, and 181 had left unresolved.

## Interpretation boundary

These are **GDA actuator positions in inches**, not the preburn GDA trim angles in degrees. They must not be numerically equated with the commanded `5.86° / 6.75°` pair without a sourced actuator calibration/geometry conversion.

The table labels the second actuator axis **Roll**. Preserve that mission-report terminology; do not silently rename it yaw merely because other DPS trim material describes pitch/yaw or pitch/roll angular conventions differently.

The four values are phase summaries, not a continuous telemetry trace. `Maximum excursion` also does not establish the time of the extremum. No interpolation shape should be invented.

## Consequence

The project may now model the historical 61:29 GDA state at the source's actual resolution using the four tabulated phase values above. A continuous time-series remains unsupported.

This closes the parallel archival target for exact free-return GDA actuator values. It does **not** close the main ground-computation lineage:

`T+55 LM-burn mass-properties deck -> generation/load/run identity -> RTCC/RTACF trim output -> 5.86 / 6.75`.

CONTROL's competing numerical trim and the ground-computation comparison/acceptance basis also remain unresolved.
