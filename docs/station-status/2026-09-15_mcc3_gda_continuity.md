# Station research status — MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/173_realtime_mass_properties_update_precedent.md`

## CONTROL

**Improved.** The Flight Dynamics primary account establishes that LM CONTROL challenged the DPS trim passed on the ~59 GET PC+2 abort pad because CONTROL had used **premission mass properties**; CONTROL later agreed with Flight Dynamics' data. The air-to-ground record identifies the passed pair as pitch `5.86°`, roll `6.75°`.

CONTROL's alternative numerical solution, exact mass-properties inputs, comparison delta, and acceptance rule remain unrecovered.

The pre-61:29 checkout `~0.3°` observation remains hardware-checkout evidence only. CONTROL's later PC+2 ignition narrative yields approximate pre-ignition roll `~-0.8°` by arithmetic, not an independently printed trim value.

## FLIGHT / CAPCOM

**Improved.** Primary voice at ~59 GET identifies `5.86 / 6.75` as the PC+2 DPS trim/GDA pair passed to the crew. After the 61:29 maneuver, a revised PC+2 pad says GDA should be "okay as is," with `5.85 / 6.74` read back and qualified by "hopefully." These are distinct operational records and must not be treated as proof of a `0.01°` PC+2 update criterion.

## GUIDANCE

**Boundary retained.** The immediate post-61:29 `0.2` trim exchange remains unclassified as a GDA quantity absent explicit primary evidence.

## Flight Dynamics / RTCC / RTACF

**Improved.** The Flight Control Division Mission Operations Report explicitly states that it uses only data available in real time. Its statement that RTCC LM-burn mass-property decks were updated to T+55 decks is therefore direct evidence that this newer deck family was operationally available, not a later reconstruction.

The same Apollo 13 chronology documents an earlier T+25 RTCC mass-properties run in which no update was required because pitch/yaw trims were within `0.01°` of T+6. This establishes a mission-specific real-time workflow of time-tagged mass-properties computation -> trim comparison -> update/no-update decision. The `0.01°` value is scoped only to that T+25/T+6 decision.

The ~59 GET `5.86 / 6.75` pair remains source-classified as the Flight Dynamics PC+2 abort-pad trim solution that CONTROL challenged and later accepted. The disagreement was explicitly mass-properties-dependent; CONTROL's challenged basis was premission mass properties. The coexistence of the real-time T+55 deck update materially strengthens the search hypothesis that newer operational mass properties underlay Flight Dynamics' preferred solution, but no reviewed source explicitly links the pair to a particular T+55 deck/job.

Contemporary Apollo 11 Flight Dynamics documentation adds architecture-level evidence that RTACF mass-properties computations produced **weight-c.g. tables used by RTACF and RTCC trajectory processors to compute pitch/yaw trim angles**. This narrows the artifact class but does not establish the Apollo 13 facility/program path.

Apollo 13 Mission Report Table A-I remains a separate postflight validation layer, not evidence for the real-time T+55 deck or trim job.

Still unresolved: the Apollo 13 real-time weight/c.g./mass-properties input artifact, CONTROL's competing numerical values, PC+2-specific acceptance criterion, RTCC/RTACF job/request identity, and direct proof that the Flight Dynamics `5.86 / 6.75` calculation used the documented T+55 LM-burn deck family.

## Simulator constraint

A generic controller workflow may now model a time-tagged mass-properties run producing trim values that are compared with an earlier solution before an update/no-update decision; Apollo 13 directly documents that pattern at T+25. Do not encode `0.01°` as a universal threshold or as the PC+2 criterion. Represent real-time mass-properties input, computed trim output, and postflight reconstructed mass properties as separate provenance layers.