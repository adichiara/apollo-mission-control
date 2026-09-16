# Station research status — MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/172_apollo13_postflight_mass_properties_validation_bound.md`

## CONTROL

**Improved.** The Flight Dynamics primary account establishes that LM CONTROL challenged the DPS trim passed on the ~59 GET PC+2 abort pad because CONTROL had used **premission mass properties**; CONTROL later agreed with Flight Dynamics' data. The air-to-ground record identifies the passed pair as pitch `5.86°`, roll `6.75°`.

CONTROL's alternative numerical solution, exact mass-properties inputs, comparison delta, and acceptance rule remain unrecovered.

The pre-61:29 checkout `~0.3°` observation remains hardware-checkout evidence only. CONTROL's later PC+2 ignition narrative yields approximate pre-ignition roll `~-0.8°` by arithmetic, not an independently printed trim value.

## FLIGHT / CAPCOM

**Improved.** Primary voice at ~59 GET identifies `5.86 / 6.75` as the PC+2 DPS trim/GDA pair passed to the crew. After the 61:29 maneuver, a revised PC+2 pad says GDA should be "okay as is," with `5.85 / 6.74` read back and qualified by "hopefully." These are distinct operational records and must not be treated as proof of a `0.01°` update criterion.

## GUIDANCE

**Boundary retained.** The immediate post-61:29 `0.2` trim exchange remains unclassified as a GDA quantity absent explicit primary evidence.

## Flight Dynamics / RTCC / RTACF

**Artifact class narrowed.** The ~59 GET `5.86 / 6.75` pair is source-classified as the Flight Dynamics PC+2 abort-pad trim solution that CONTROL challenged and later accepted. The disagreement was explicitly mass-properties-dependent; CONTROL's challenged basis was premission mass properties.

Contemporary Apollo 11 Flight Dynamics documentation adds architecture-level evidence that RTACF mass-properties computations produced **weight-c.g. tables used by RTACF and RTCC trajectory processors to compute pitch/yaw trim angles**. Because this is adjacent-mission evidence, it narrows the Apollo 13 archival search but does not establish which facility/program produced `5.86 / 6.75`.

**New validation boundary.** Apollo 13 Mission Report Table A-I supplies postflight mass/c.g./inertia values for significant mission events, including the second midcourse correction. These are authoritative mission-specific reconstructed values, but the report explicitly describes the table as based on postflight analysis of expendable loading and usage. They are therefore a validation reference, not evidence for the real-time T+55 deck or trim job.

Still unresolved: the Apollo 13 real-time weight/c.g./mass-properties input artifact, CONTROL's competing numerical values, acceptance criterion, RTCC/RTACF job/request identity, and direct proof that the Flight Dynamics calculation used the documented T+55 LM-burn deck family.

## Simulator constraint

Represent real-time mass-properties input, computed trim output, and postflight reconstructed mass properties as separate provenance layers. The model may represent `5.86 / 6.75` as the source-backed Flight Dynamics PC+2 abort-pad trim solution and may use Table A-I as a postflight validation target, but must not backfill the missing real-time controller deck with Table A-I values. Do not encode the Apollo 11 RTACF architecture as an Apollo 13 mission-specific implementation without direct evidence.