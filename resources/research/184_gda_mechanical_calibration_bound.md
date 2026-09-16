# Research Note 184 — GDA mechanical calibration boundary

**Date:** 2026-09-16  
**Status:** REVIEWED — generic LM GDA stroke/gimbal calibration recovered; Apollo 13 representation mapping remains unresolved

## Question

Can the four Apollo 13 Mission Report GDA actuator positions in inches be converted directly into the crew-facing `5.86 / 6.75` trim-angle representation?

## Primary source

NASA, *Apollo News Reference — Lunar Module*, main-propulsion/GN&C material, Gimbal Drive Actuator specifications and gimbal-ring description.

NASA-hosted excerpt: https://www.nasa.gov/wp-content/uploads/static/history/alsj/LM09_Main_Propulsion_ppMP1-22.pdf

The NASA reference states that each GDA can extend or retract **2 inches from mid-position** to tilt the descent engine a maximum of **6 degrees** along its axis. The associated LM News Reference specification gives stroke `+2 to -2 inches ±5%` and gimbal position `+6° to -6° ±5%`.

## Finding

At the generic LM mechanism level, the endpoint ratio is nominally:

`6 degrees / 2 inches = 3 degrees per inch`.

This establishes a useful mechanical scale and confirms that the Mission Report's inch-valued GDA column is physically an actuator-displacement representation of engine gimbal position.

It does **not** establish that the relation should be applied as an exact Apollo 13/LM-7 telemetry conversion. The published stroke and angular ranges carry tolerances, and the recovered source does not supply LM-7-specific calibration, sign convention, zero/reference definition, linkage nonlinearity/error, or the mapping between physical signed gimbal angle and the crew-facing `5.86 / 6.75` numbers.

## Important representation warning

A naive direct conversion of `5.86° / 6.75°` as signed physical deflections from mechanical center is not justified by this source. Those values must remain in their documented crew/ground trim representation until a primary source establishes its zero/reference and axis/sign convention.

Likewise, applying `3°/in` to Table 6.4-I can be used only as a **nominal generic mechanism-scale estimate**, not as recovered Apollo 13 flight telemetry in degrees.

For reference, the nominal endpoint-ratio estimates from the four postflight phase values would be:

| Phase | Pitch, in | nominal scale estimate, deg | Roll, in | nominal scale estimate, deg |
|---|---:|---:|---:|---:|
| Initial | -0.02 | -0.06 | -0.34 | -1.02 |
| Maximum excursion | +0.31 | +0.93 | -0.27 | -0.81 |
| Steady-state | +0.04 | +0.12 | -0.51 | -1.53 |
| Cutoff | +0.10 | +0.30 | -0.31 | -0.93 |

These derived values are **not historical reported values** and must not be stored or displayed as such.

## Consequence for simulation

The simulation may use the sourced inch values directly at Table 6.4-I resolution. If a generic mechanical visualization requires angular motion before LM-7 calibration is recovered, the nominal `3°/in` ratio may be used only when visibly identified as a generic mechanism approximation rather than Apollo 13 measured angle data.

## Remaining archival target

Recover a primary Apollo LM GDA trim representation definition and, preferably, LM-7 calibration/telemetry documentation that establishes:

1. the reference/zero behind crew-facing GDA trim numbers;
2. axis and sign conventions;
3. conversion from displayed/commanded trim to physical engine angle or actuator stroke;
4. whether mission-control GDA displays used raw displacement, converted angle, or another encoded quantity.

The principal ground-computation target remains separately unresolved:

`T+55 LM-burn mass-properties deck -> generation/load/run identity -> RTCC/RTACF trim output -> 5.86 / 6.75`.
