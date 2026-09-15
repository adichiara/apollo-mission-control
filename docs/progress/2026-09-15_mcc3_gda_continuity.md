# MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/168_pc2_preignition_roll_gda_bound.md`

## Completed

- Reconciled the apparent `MCC-3` contradiction in the Flight Control Division report.
- Established that LM CONTROL calls the 61:29 contingency free-return DPS burn `MCC-3 - DPS 1`, although trajectory/mission-summary material calls that maneuver MCC-4 and records the originally planned MCC-3 as omitted.
- Added primary voice evidence immediately before the 61:29 burn: CAPCOM states that the GDA settings are "go as they are."
- Tightened the retained-state chain: the PC+2 reference state was the GDA state after the 61:29 burn's 40% powered-flight compliance.
- Recovered a numerical checkout observation from the primary controller loop: during the pre-61:29 gimbal/throttle test, CONTROL called the trim GO and reported it was "within about 0.3" and "plenty close."
- Classified that `~0.3°` result strictly as a pre-burn checkout acceptance observation, not as the missing PC+2 RTCC trim-update tolerance.
- Re-examined CONTROL's PC+2 ignition account and derived an approximate immediately pre-ignition roll-GDA position of `~-0.8°` from its reported move to about `-2°` by `-1.2°`.
- Classified `~-0.8°` as derived/approximate rather than as a separately documented controller value, and preserved the distinction between immediate pre-PC+2 state and exact 61:29 cutoff state.
- Preserved the remaining numerical boundary: retained pitch angle and the upstream PC+2 comparison/job remain unrecovered.

## Next

Search controller/RTCC working artifacts for the numerical comparison between the retained GDA state and the PC+2 candidate trim, including retained pitch, candidate values, comparison criterion, job identity, and T+55 mass-property provenance. Keep hardware-checkout tolerances and derived ignition-state arithmetic separate from mass-properties trim-comparison criteria.