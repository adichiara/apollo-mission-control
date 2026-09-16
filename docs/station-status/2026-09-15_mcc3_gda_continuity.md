# Station research status — MCC-3 nomenclature and GDA continuity

Date: 2026-09-16  
Latest research note: `resources/research/192_lm7_preflight_weight_state_crosscheck.md`

## CONTROL

**Improved; exact selected input set unresolved.** Flight Dynamics says CONTROL challenged the ~59 GET PC+2 DPS trim using `premission mass properties`; CONTROL later agreed with Flight Dynamics' better data. Voice establishes the commanded pair `5.86° / 6.75°` and a separate preburn checkout disposition.

Note 191 identifies a concrete late-preflight official source state: **SNA-8-D-027(III) Rev. 2, LM-7 Amendment 79, 30 March 1970**. Note 192 now shows why source-state separation matters numerically: the Apollo 13 Review Board reports **33,941 lb at CSM/LM separation**, while the 17 March analysis-specific source used **33,872.3 lbm**. The 68.7-lb difference is evidence of differing documented mass states, not evidence of which state CONTROL used or why they differ.

CONTROL's exact selected premission table/revision, alternative trim, exact inputs, comparison delta/acceptance rule, and direct T+55 run lineage remain unrecovered.

## FLIGHT / CAPCOM

**Stable.** `5.86 / 6.75` is the ~59/61:29 ground-issued commanded reference; later `5.85 / 6.74` is a PC+2 ground reference with `okay as it is from the last burn` disposition.

## Flight Dynamics / RTCC / RTACF

**Improved; mission-specific consumption edge unresolved.** T-6, T+25, and T+55 source states remain distinct. Contemporary RTACF material establishes the generic processor chain. Notes 191–192 add the official preflight LM-7 Amendment 79 source state and an independent mission-summary separation-weight constraint, but neither connects a specific mass state to CONTROL or to the real-time T+55 run.

Still unresolved: Table 3-3.2 current values, T+55 weight/c.g./deck contents, downstream Apollo 13 run/request/output, CONTROL's selected premission source and competing numerical values, comparison criterion, job identity, and direct T+55-to-`5.86 / 6.75` lineage.

## Simulator constraint

Track `analysis_specific`, `official_available_preflight`, `mission_summary`, `controller_selected_source`, and `realtime_updated` independently. Preserve `33,872.3 lbm` only as the 17 March analysis state and `33,941 lb` only as the Review Board CSM/LM-separation mission-summary state. Do not infer the cause of their 68.7-lb difference.