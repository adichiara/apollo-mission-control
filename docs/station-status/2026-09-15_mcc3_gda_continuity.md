# Station research status — MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/177_mass_properties_operation_verb_boundary.md`

## CONTROL

**Improved.** The Flight Dynamics primary account establishes that LM CONTROL challenged the DPS trim passed on the ~59 GET PC+2 abort pad because CONTROL had used **premission mass properties**; CONTROL later agreed with Flight Dynamics' data. The air-to-ground record identifies the passed pair as pitch `5.86°`, roll `6.75°`.

Primary NASA voice also establishes that the same `5.86 / 6.75` pair was passed and accepted as the commanded GDA pair for the 61:29 free-return DPS burn. CONTROL later says the 40%-thrust compliance during that burn was expected to leave the GDA state optimum for PC+2.

CONTROL's alternative numerical solution, exact mass-properties inputs, comparison delta, acceptance rule, and exact post-compliance two-axis state remain unrecovered.

## FLIGHT / CAPCOM

**Improved.** Primary voice at ~59 GET identifies `5.86 / 6.75` as a provisional PC+2 DPS trim/GDA pair and says the angles "will be updated." At 60:53–60:56 GET, CAPCOM passes the same pair on the actual 61:29 free-return DPS pad and accepts Haise's readback. After that maneuver, a revised PC+2 pad says GDA should be "okay as is," with `5.85 / 6.74` read back and qualified by "hopefully."

These records establish commanded-value continuity across the intervening burn, but not numerical identity between the commanded pair and the post-powered-flight actuator state.

## GUIDANCE

**Boundary retained.** The immediate post-61:29 `0.2` trim exchange remains unclassified as a GDA quantity absent explicit primary evidence.

## Flight Dynamics / RTCC / RTACF

**Improved.** The Flight Control Division Mission Operations Report explicitly distinguishes several mass-properties operations in its Apollo 13 chronology: T-6 mass properties were **generated** and **loaded in the RTCC**; T+25 RTCC mass properties were **run** and their pitch/yaw trims evaluated; later **RTCC (LM burn) mass property decks were updated to T+55 decks**.

This verb-level distinction matters. The T+55 statement supports a deck update/reference-set state in the RTCC LM-burn domain, but does not itself prove generation, a separate RTCC load event, or a downstream trim run. The T+25 `0.01°` result remains scoped only to that earlier no-update decision.

`T+55` remains a mass-properties reference-epoch label, not a calculation timestamp or RTCC job identifier. Direct proof that the ~59 GET `5.86 / 6.75` solution consumed the T+55 deck is still absent.

Contemporary Apollo 11 Flight Dynamics documentation remains architecture-level corroboration that RTACF mass-properties computations produced weight-c.g. tables used by RTACF and RTCC trajectory processors to compute pitch/yaw trim angles. Apollo 13 Mission Report Table A-I remains a separate postflight validation layer.

Still unresolved: T+55 weight/c.g./deck contents, generation/load event, downstream run/request/output, CONTROL's competing numerical values, PC+2-specific acceptance criterion, RTCC/RTACF job identity, direct T+55-to-`5.86 / 6.75` data lineage, and exact two-axis post-61:29 complied GDA state.

## Simulator constraint

Represent `reference_epoch`, `processing_domain`, `generated`, `loaded`, `deck_updated/reference_set_selected`, and `run_consumed` as separate provenance fields/events. For T+55, only the reference epoch, RTCC LM-burn domain, and deck-update/reference-set state are currently source-backed. Likewise keep ground-computed trim, commanded/loaded burn trim, post-powered-flight complied actuator state, and later pad/reference values separate.