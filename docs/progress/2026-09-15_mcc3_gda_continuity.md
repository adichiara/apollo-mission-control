# MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/169_post_mcc3_pc2_gda_as_is_readback.md`

## Completed

- Reconciled the apparent `MCC-3` contradiction in the Flight Control Division report.
- Established that LM CONTROL calls the 61:29 contingency free-return DPS burn `MCC-3 - DPS 1`, although trajectory/mission-summary material calls that maneuver MCC-4 and records the originally planned MCC-3 as omitted.
- Added primary voice evidence immediately before the 61:29 burn: CAPCOM states that the GDA settings are "go as they are."
- Tightened the retained-state chain: the PC+2 reference state was expected to remain acceptable after the 61:29 burn's 40% powered-flight compliance.
- Recovered a numerical checkout observation from the primary controller loop: during the pre-61:29 gimbal/throttle test, CONTROL called the trim GO and reported it was "within about 0.3" and "plenty close."
- Classified that `~0.3°` result strictly as a pre-burn checkout acceptance observation, not as the missing PC+2 RTCC trim-update tolerance.
- Re-examined CONTROL's PC+2 ignition account and derived an approximate immediately pre-ignition roll-GDA position of `~-0.8°` from its reported move to about `-2°` by `-1.2°`.
- Recovered a post-61:29 PC+2 pad readback in the NASA mission commentary: the crew says the GDA should be "okay as is," "hopefully" pitch `5.85` and second axis `6.74` (transcribed as "Yaw").
- Classified `5.85 / 6.74` as an intended/retained reference readback, not measured post-compliance actuator telemetry; kept it distinct from the `~-0.8°` execution-state roll derivation.
- Preserved the remaining numerical boundary: the upstream PC+2 candidate/reference comparison, criterion, job identity, and T+55 calculation linkage remain unrecovered.

## Next

Search controller/RTCC working artifacts for the numerical comparison behind the no-update decision: PC+2 candidate trim, reference used by controllers, comparison delta/criterion, calculation time/job identity, and direct T+55 mass-property provenance. Keep pad/reference values, hardware-checkout tolerances, measured actuator state, and mass-properties comparison criteria as separate provenance layers.