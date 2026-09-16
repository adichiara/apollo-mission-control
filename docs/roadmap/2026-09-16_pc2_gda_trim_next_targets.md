# Roadmap — PC+2 GDA trim next targets

Date: 2026-09-16

Research Notes 180–181 close modeling ambiguities but not the ground-computation provenance gap. Apollo 13 primary material establishes that DPS gimbal trim can change automatically during powered flight to compensate for changing center of gravity. Mission-specific postflight evidence further establishes nominal primary-guidance/AUTO performance during the 61:29 firing with no reported vehicle attitude excursions. Neither finding supplies exact actuator position history.

## Priority 1 — ground-computation lineage

Recover a mission-specific artifact that bridges:

`T+55 LM-burn mass-properties deck -> generation/load/run identity -> RTCC/RTACF trim output -> 5.86 / 6.75`

Best targets: weight/c.g. sheet, RTCC/RTACF request/output, job/run record, controller working paper, or support-room product.

## Priority 2 — disagreement details

Recover CONTROL's competing numerical trim and the actual comparison/acceptance basis used when CONTROL challenged Flight Dynamics' solution. Do not apply the T+25 `0.01°` no-update comparison or the later `~0.3°` spacecraft-checkout statement to this decision without direct evidence.

## Priority 3 — actuator-state branch

Recover and inspect the Apollo 13 GN&C performance-analysis supplement (`NTRS 19730017939`, `MSC-02680-SUPPL-1`) and other mission telemetry/controller records for actual pitch/yaw GDA positions during and immediately after the 61:29 free-return burn.

Current primary evidence permits a stable vehicle-attitude model for this maneuver: primary guidance/AUTO performance was nominal and no vehicle attitude excursions were reported. Do not convert that into static-gimbal evidence.

## Priority 4 — executed propulsion profile

Use the postflight Apollo 13 Mission Report as the execution baseline: 34.3-second firing, minimum throttle reported as 12% for the first 5 seconds, then approximately 37%. Preserve the nominal preburn `10% / 40%` pad values separately as planned/commanded procedure rather than telemetry.

## Modeling rule meanwhile

Use `5.86 / 6.75` only as a sourced commanded/preburn trim reference. Model the 61:29 vehicle attitude response as nominal/stable if needed, but keep detailed powered-flight gimbal history unresolved or explicitly synthetic until separately validated.