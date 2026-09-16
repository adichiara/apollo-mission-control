# Station research status — CONTROL / 61:29 GDA

Date: 2026-09-16

## Newly documented

Primary postflight evidence now provides mission-specific GDA actuator positions for the 61:29 free-return DPS burn. *Apollo 13 Mission Report* Table 6.4-I reports, in inches:

| Phase | Pitch | Roll |
|---|---:|---:|
| Initial | -0.02 | -0.34 |
| Maximum excursion | +0.31 | -0.27 |
| Steady-state | +0.04 | -0.51 |
| Cutoff | +0.10 | -0.31 |

This strengthens CONTROL's documented `GDA position/trim` information family with actual maneuver-specific postflight values.

## Fidelity boundary

The source reports actuator displacement in inches, while the crew-facing preburn trim was communicated in degrees. No conversion between those representations is asserted without calibration/geometry evidence. The four postflight values are summary points, not a continuous trace.

## Still unresolved

- exact Apollo 13 CONTROL CRT field calibration/precision for GDA position;
- exact live values seen by CONTROL during the burn versus the later postflight reconstruction;
- actuator-inch to trim-angle conversion/geometry;
- T+55 mass-properties computational lineage to the `5.86 / 6.75` preburn trim;
- CONTROL's competing numerical trim and comparison criterion.
