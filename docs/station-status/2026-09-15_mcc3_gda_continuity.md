# Station research status — MCC-3 nomenclature and GDA continuity

Date: 2026-09-16  
Latest research note: `resources/research/193_lm7_sequential_mass_properties_table_recovery.md`

## CONTROL

**Improved; exact selected input set unresolved.** Flight Dynamics says CONTROL challenged the ~59 GET PC+2 DPS trim using `premission mass properties`; CONTROL later agreed with Flight Dynamics' better data. Voice establishes the commanded pair `5.86° / 6.75°` and a separate preburn checkout disposition.

Note 193 now identifies the concrete official LM-7 sequential model available preflight: **SNA-8-D-027(III) Rev. 2, Amendment 79, Table 3.3-3**, dated 30 March 1970. A recovered `LM PRE P.D.I.` row is 33,980.1 lb with X/Y/Z c.g. approximately 188.1/-0.0/-0.8 in. This materially narrows the candidate premission source family but does not establish CONTROL selected it.

The source itself contains a numbering inconsistency: Table 3.3-8 calls its companion `LM sequential mass properties Table 3-3.2`, while recovered LM-7 sequential pages are Table 3.3-3 and Table 3.3-2 is CSM 109. Preserve that discrepancy; do not infer its cause.

CONTROL's exact selected premission table/revision/state, alternative trim, exact inputs, comparison delta/acceptance rule, and direct T+55 run lineage remain unrecovered.

## FLIGHT / CAPCOM

**Stable.** `5.86 / 6.75` is the ~59/61:29 ground-issued commanded reference; later `5.85 / 6.74` is a PC+2 ground reference with `okay as it is from the last burn` disposition.

## Flight Dynamics / RTCC / RTACF

**Improved; mission-specific consumption edge unresolved.** T-6, T+25, and T+55 source states remain distinct. Contemporary RTACF material establishes the generic processor chain. Amendment 79/Table 3.3-3 now supplies direct official preflight LM-7 weight/c.g. rows, but no recovered artifact yet connects one of those rows—or the T+55 real-time deck—to the specific run that yielded `5.86 / 6.75`.

Still unresolved: T+55 weight/c.g./deck contents, downstream Apollo 13 run/request/output, CONTROL's selected premission source and competing numerical values, comparison criterion, job identity, and direct T+55-to-`5.86 / 6.75` lineage.

## Simulator constraint

Track `analysis_specific`, `official_available_preflight_lm7_sequential`, `mission_summary`, `controller_selected_source`, and `realtime_updated` independently. Preserve Table 3.3-3 rows only as official preflight sequential-model states unless a controller source proves selection. Do not infer relationships among the 17 March 33,872.3-lbm analysis value, Amendment 79 sequential rows, Review Board 33,941-lb separation summary, CONTROL's unknown state, or T+55.