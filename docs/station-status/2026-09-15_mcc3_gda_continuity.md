# Station research status — MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/175_gda_pair_reuse_free_return_burn.md`

## CONTROL

**Improved.** The Flight Dynamics primary account establishes that LM CONTROL challenged the DPS trim passed on the ~59 GET PC+2 abort pad because CONTROL had used **premission mass properties**; CONTROL later agreed with Flight Dynamics' data. The air-to-ground record identifies the passed pair as pitch `5.86°`, roll `6.75°`.

Primary NASA voice now also establishes that the same `5.86 / 6.75` pair was passed and accepted as the commanded GDA pair for the 61:29 free-return DPS burn. This matters because CONTROL later says the 40%-thrust compliance during that burn was expected to leave the GDA state optimum for PC+2.

CONTROL's alternative numerical solution, exact mass-properties inputs, comparison delta, acceptance rule, and exact post-compliance two-axis state remain unrecovered.

The pre-61:29 checkout `~0.3°` observation remains hardware-checkout evidence only. CONTROL's later PC+2 ignition narrative yields approximate pre-ignition roll `~-0.8°` by arithmetic, not an independently printed trim value.

## FLIGHT / CAPCOM

**Improved.** Primary voice at ~59 GET identifies `5.86 / 6.75` as a provisional PC+2 DPS trim/GDA pair and says the angles "will be updated." At 60:53–60:56 GET, CAPCOM passes the same pair on the actual 61:29 free-return DPS pad and accepts Haise's readback. After that maneuver, a revised PC+2 pad says GDA should be "okay as is," with `5.85 / 6.74` read back and qualified by "hopefully."

These records now establish commanded-value continuity across the intervening burn, but not numerical identity between the commanded pair and the post-powered-flight actuator state.

## GUIDANCE

**Boundary retained.** The immediate post-61:29 `0.2` trim exchange remains unclassified as a GDA quantity absent explicit primary evidence.

## Flight Dynamics / RTCC / RTACF

**Improved.** The Flight Control Division Mission Operations Report explicitly states that it uses only data available in real time. Its statement that RTCC LM-burn mass-property decks were updated to T+55 decks is therefore direct evidence that this newer deck family was operationally available, not a later reconstruction.

The same chronology uses `T+6`, `T+25`, and `T+55` for time-tagged mass-properties sets/decks. `T+55` is classified as a mass-properties reference-epoch label, not a calculation timestamp or RTCC job identifier. The T+25 case establishes a mission-specific real-time workflow of time-tagged mass-properties computation -> trim comparison -> update/no-update decision; its `0.01°` result is scoped only to that earlier decision.

The ~59 GET `5.86 / 6.75` pair remains source-classified as the Flight Dynamics PC+2 abort-pad trim solution that CONTROL challenged and later accepted, and note 175 now additionally proves that this exact pair became the commanded GDA pair for the 61:29 free-return DPS maneuver. That closes a downstream numerical continuity gap but does not close the upstream mass-properties provenance gap.

Contemporary Apollo 11 Flight Dynamics documentation adds architecture-level evidence that RTACF mass-properties computations produced weight-c.g. tables used by RTACF and RTCC trajectory processors to compute pitch/yaw trim angles. Apollo 13 Mission Report Table A-I remains a separate postflight validation layer.

Still unresolved: the Apollo 13 real-time weight/c.g./mass-properties input artifact, T+55 deck contents and generation/load time, CONTROL's competing numerical values, PC+2-specific acceptance criterion, RTCC/RTACF job/request identity, direct proof that `5.86 / 6.75` used the T+55 reference-epoch deck, and exact two-axis post-61:29 complied GDA state.

## Simulator constraint

Represent ground-computed trim, commanded/loaded burn trim, post-powered-flight complied actuator state, and later pad/reference values as separate fields. For the 61:29 maneuver, `5.86 / 6.75` is directly supported as the commanded pair; do not automatically copy it into the post-compliance state. Likewise, do not encode `0.01°` as a universal threshold or as the PC+2 criterion.