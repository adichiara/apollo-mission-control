# Roadmap — PC+2 GDA trim next targets

Date: 2026-09-16

Research Note 180 closes a modeling ambiguity but not the ground-computation provenance gap. Apollo 13 primary material establishes that DPS gimbal trim can change automatically during powered flight to compensate for changing center of gravity. Therefore the initial `5.86 / 6.75` commanded pair is not a defensible substitute for exact powered-flight/postburn GDA telemetry.

## Priority 1 — ground-computation lineage

Recover a mission-specific artifact that bridges:

`T+55 LM-burn mass-properties deck -> generation/load/run identity -> RTCC/RTACF trim output -> 5.86 / 6.75`

Best targets: weight/c.g. sheet, RTCC/RTACF request/output, job/run record, controller working paper, or support-room product.

## Priority 2 — disagreement details

Recover CONTROL's competing numerical trim and the actual comparison/acceptance basis used when CONTROL challenged Flight Dynamics' solution. Do not apply the T+25 `0.01°` no-update comparison or the later `~0.3°` spacecraft-checkout statement to this decision without direct evidence.

## Priority 3 — actuator-state branch

Search mission telemetry/controller records for actual pitch/yaw GDA positions during and immediately after the 61:29 free-return burn. Automatic trim means the commanded starting pair cannot simply be carried forward as physical state.

## Modeling rule meanwhile

Use `5.86 / 6.75` only as a sourced commanded/preburn trim reference. Any detailed powered-flight gimbal history must remain unresolved or explicitly synthetic until separately validated.