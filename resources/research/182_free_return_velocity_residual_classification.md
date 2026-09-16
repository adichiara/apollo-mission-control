# Research Note 182 — 61:29 free-return velocity residual classification

Date: 2026-09-16

## Question

Can the small numerical values reported around the 61:29 free-return maneuver be used as evidence for GDA/gimbal residuals or a trim-acceptance criterion?

## Primary source

NASA/MSC, *Apollo 13 Mission Report*, MSC-02680, September 1970, NTRS `19710003598`, Table 6.4-I (Lunar Module Maneuver Summary).

Primary PDF: https://ntrs.nasa.gov/api/citations/19710003598/downloads/19710003598.pdf

## Finding

Table 6.4-I identifies the second midcourse correction as a PGNCS/DPS maneuver with ignition at `61:29:43.49`, cutoff at `61:30:17.72`, and duration `34.23 s`. For this maneuver it reports actual/desired velocity change before trim and then a separate row explicitly labeled **velocity residual after trim, ft/sec**:

- X: `+0.2 ft/s`
- Y: `0.0 ft/s`
- Z: `+0.3 ft/s`

These are translational velocity residuals, not angular GDA residuals and not gimbal-position errors.

## Provenance boundary

This closes a classification ambiguity in the PC+2 research thread. A `0.2` or `0.3` value associated with the completed 61:29 maneuver must not be promoted to a GDA angle, gimbal error, or trim acceptance tolerance unless a separate primary source explicitly identifies it that way.

The mission-report residuals also remain distinct from CONTROL's preburn statement that gimbal trim was `within about 0.3` and `plenty close`: the latter is a spacecraft checkout statement in angular/gimbal context, while Table 6.4-I's `+0.3` is explicitly a post-maneuver velocity residual in ft/s.

## Simulator implication

For a historical 61:29 maneuver outcome model, the mission report supports a post-trim velocity residual vector of approximately `[+0.2, 0.0, +0.3] ft/s`. It does **not** support deriving exact postburn GDA actuator positions from those values.

## Remaining unresolved items

- T+55 mass-properties generation/load/run lineage into the `5.86 / 6.75` trim solution;
- CONTROL's competing numerical trim and the ground-computation comparison criterion;
- exact pitch/yaw GDA actuator history during and after the 61:29 burn.
