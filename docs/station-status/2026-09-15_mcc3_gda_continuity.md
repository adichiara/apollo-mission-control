# Station research status — MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/170_pc2_59h_trim_provenance.md`

## CONTROL

**Improved.** The Flight Dynamics primary account now establishes that LM CONTROL challenged the DPS trim passed on the ~59 GET PC+2 abort pad because CONTROL had used **premission mass properties**; CONTROL later agreed with Flight Dynamics' data. The air-to-ground record identifies the passed pair as pitch `5.86°`, roll `6.75°`.

CONTROL's alternative numerical solution, comparison delta, and acceptance rule remain unrecovered.

The pre-61:29 checkout `~0.3°` observation remains hardware-checkout evidence only. CONTROL's later PC+2 ignition narrative still yields approximate pre-ignition roll `~-0.8°` by arithmetic, not an independently printed trim value.

## FLIGHT / CAPCOM

**Improved.** Primary voice at ~59 GET identifies `5.86 / 6.75` as the PC+2 DPS trim/GDA pair passed to the crew. After the 61:29 maneuver, a revised PC+2 pad says GDA should be "okay as is," with `5.85 / 6.74` read back and qualified by "hopefully." These are distinct operational records and must not be treated as proof of a `0.01°` update criterion.

## GUIDANCE

**Boundary retained.** The immediate post-61:29 `0.2` trim exchange remains unclassified as a GDA quantity absent explicit primary evidence.

## Flight Dynamics / RTCC

**Materially improved.** The ~59 GET `5.86 / 6.75` pair can now be classified as the Flight Dynamics PC+2 abort-pad trim solution that CONTROL challenged and later accepted. The disagreement was explicitly mass-properties-dependent; CONTROL's challenged basis was premission mass properties.

Still unresolved: CONTROL's competing numerical values, the acceptance criterion, RTCC/RTACF job identity, and direct proof that the Flight Dynamics calculation used the documented T+55 LM-burn deck family. The report's separate statement that LM-burn decks were updated to T+55 is contextual provenance, not yet a calculation-level link.

## Simulator constraint

The model may represent `5.86 / 6.75` as a source-backed Flight Dynamics PC+2 abort-pad trim solution at ~59 GET and may represent a competing CONTROL solution whose basis was premission mass properties, but the competing values and acceptance rule must remain unknown. Keep this distinct from the later `5.85 / 6.74` retained-reference readback and the approximate `~-0.8°` execution-state roll.