# MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/167_free_return_gda_test_acceptance_bound.md`

## Completed

- Reconciled the apparent `MCC-3` contradiction in the Flight Control Division report.
- Established that LM CONTROL calls the 61:29 contingency free-return DPS burn `MCC-3 - DPS 1`, although trajectory/mission-summary material calls that maneuver MCC-4 and records the originally planned MCC-3 as omitted.
- Added primary voice evidence immediately before the 61:29 burn: CAPCOM states that the GDA settings are "go as they are."
- Tightened the retained-state chain: the PC+2 reference state was the GDA state after the 61:29 burn's 40% powered-flight compliance.
- Recovered a numerical checkout observation from the primary controller loop: during the pre-61:29 gimbal/throttle test, CONTROL called the trim GO and reported it was "within about 0.3" and "plenty close."
- Classified that `~0.3°` result strictly as a pre-burn checkout acceptance observation, not as the missing PC+2 RTCC trim-update tolerance.
- Preserved the numerical boundary: post-compliance angles and the upstream PC+2 comparison/job remain unrecovered.

## Next

Search controller/RTCC working artifacts for the numerical comparison between the post-61:29 complied GDA state and the PC+2 candidate trim, including T+55 mass-property provenance. Keep hardware-checkout tolerances separate from mass-properties trim-comparison criteria.