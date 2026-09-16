# Station research status — MCC-3 nomenclature and GDA continuity

Date: 2026-09-16  
Latest research note: `resources/research/191_lm7_volume3_amendment79_current_official_set.md`

## CONTROL

**Improved; exact selected input set unresolved.** Flight Dynamics says CONTROL challenged the ~59 GET PC+2 DPS trim using `premission mass properties`; CONTROL later agreed with Flight Dynamics' better data. Voice establishes the commanded pair `5.86° / 6.75°` and a separate preburn checkout disposition.

Note 191 now identifies a concrete late-preflight official source state: **SNA-8-D-027(III) Rev. 2, LM-7 Amendment 79, 30 March 1970**. Its LM-7 consumables summary is explicitly coupled to sequential mass-properties Table 3-3.2. This is evidence of what official LM-7 mass-property material was available before launch, not evidence that CONTROL selected it.

CONTROL's exact selected premission table/revision, alternative trim, exact inputs, comparison delta/acceptance rule, and direct T+55 run lineage remain unrecovered.

## FLIGHT / CAPCOM

**Stable.** `5.86 / 6.75` is the ~59/61:29 ground-issued commanded reference; later `5.85 / 6.74` is a PC+2 ground reference with `okay as it is from the last burn` disposition.

## Flight Dynamics / RTCC / RTACF

**Improved; mission-specific consumption edge unresolved.** T-6, T+25, and T+55 source states remain distinct. Contemporary RTACF material establishes the generic processor chain. Note 191 adds the official preflight LM-7 Amendment 79 sequential-mass-properties/consumables source state but does not connect it to CONTROL or to the real-time T+55 run.

Still unresolved: Table 3-3.2 current values, T+55 weight/c.g./deck contents, downstream Apollo 13 run/request/output, CONTROL's selected premission source and competing numerical values, comparison criterion, job identity, and direct T+55-to-`5.86 / 6.75` lineage.

## Simulator constraint

Track `official_available_preflight`, `controller_selected_source`, and `realtime_updated` independently. Record `SNA-8-D-027(III) Rev 2 / Amendment 79 / 1970-03-30 / LM-7` as available official preflight data with controller selection unknown.