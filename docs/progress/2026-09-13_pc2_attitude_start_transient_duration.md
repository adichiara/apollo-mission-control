# Progress — PC+2 attitude start-transient duration boundary

Date: 2026-09-13

## Work completed

Targeted the remaining timing gap left by research note 109: whether the PC+2 attitude-error “start transient” exception can be assigned a numeric duration or end condition.

Primary-source review found no Apollo 13 operational document in the reviewed set that supplies such a duration. The Apollo 13 CAPCOM transmission/readback and Mission Operations Report preserve the rule wording but do not time-bound the transient.

Cross-mission NASA DPS final-flight-evaluation records materially narrow the term. Apollo 14 defines the engine start transient from FS-1 toward the minimum steady-state throttle setting: about 0.55 s to first chamber-pressure rise, 2.14 s to 90% of minimum steady-state thrust, and a 4.0 s specification limit for a minimum-throttle start. The report explicitly compares ignition delay with Apollo 13. Apollo 15/16 records use the same short-duration engineering concept.

## Result

Research note 110 records a bounded conclusion:

- “start transient” is technically a short engine-start phenomenon, not the complete +26 s commanded startup profile;
- Apollo 14/15/16 timing values are cross-mission engineering evidence, not an Apollo 13 PC+2 operational rule;
- no 2.14 s, 4.0 s, +5 s, +21 s, or +26 s exception window is encoded;
- any attitude-error case whose disposition depends on the exception remains `NOT_EVALUABLE` until an Apollo 13-specific operational source or explicitly synthetic scenario boundary defines it.

This does not change nominal PC+2 behavior or create a physical-play PASS claim.

## Files

- `resources/research/110_pc2_attitude_start_transient_duration_boundary.md`
- `resources/source-catalog/PC2_ATTITUDE_SOURCES.md`
- `docs/station-status/2026-09-13_pc2_attitude_start_transient_duration.md`
- `docs/roadmap/2026-09-13_pc2_attitude_start_transient_duration.md`

## Next boundary

Physical seven-seat nominal validation remains the principal first-playable blocker, followed by the synthetic ΔP exercise and five-player compact validation. Further archival work should remain bounded to gaps with concrete scenario impact.
