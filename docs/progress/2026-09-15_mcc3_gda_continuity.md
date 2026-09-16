# MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/172_apollo13_postflight_mass_properties_validation_bound.md`

## Completed

- Reconciled the apparent `MCC-3` contradiction in the Flight Control Division report.
- Established that LM CONTROL calls the 61:29 contingency free-return DPS burn `MCC-3 - DPS 1`, although trajectory/mission-summary material calls that maneuver MCC-4 and records the originally planned MCC-3 as omitted.
- Added primary voice evidence immediately before the 61:29 burn: CAPCOM states that the GDA settings are "go as they are."
- Recovered the pre-61:29 checkout observation `within about 0.3` / `plenty close`, classified only as hardware checkout evidence.
- Derived approximate immediately pre-PC+2 roll-GDA position `~-0.8°` from CONTROL's reported ignition motion; retained it as approximate execution-state evidence only.
- Recovered the post-61:29 PC+2 retained-reference readback `5.85 / 6.74`, qualified by the crew's "hopefully" and not treated as actuator telemetry.
- Note 170 joined the ~59 GET air-to-ground readback to the Flight Dynamics postflight chronology. The `5.86 / 6.75` pair is classified as the Flight Dynamics PC+2 abort-pad DPS trim solution passed to the crew at ~59 GET.
- The same primary Flight Dynamics account says LM CONTROL challenged that passed trim using **premission mass properties**, then later agreed with Flight Dynamics' data.
- Preserved the T+55 boundary: RTCC LM-burn decks were documented as updated to T+55, but no reviewed source explicitly ties the specific `5.86 / 6.75` calculation/job to a named T+55 deck.
- Note 171 identified the adjacent-mission computational artifact class: weight-c.g. tables used by RTACF/RTCC trajectory processors to compute pitch/yaw trim.
- **New in note 172:** the Apollo 13 Mission Report Appendix A.5/Table A-I supplies mission-specific **postflight** mass properties for the second midcourse correction: ignition 95,959.9 lb with c.g. 378.8 / 4.9 / 0.7 in; cutoff 95,647.1 lb with c.g. 379.4 / 5.0 / 0.7 in. The report explicitly describes these values as postflight-analysis results, so they are retained as a validation layer and are not substituted for the missing real-time T+55/controller deck.

## Next

Search Apollo 13 archival/controller material specifically for the real-time weight/c.g. or mass-properties table, RTACF/RTCC trajectory-processor trim output, and associated job/request sheet behind the ~59 GET disagreement. Compare any recovered candidate against the postflight Table A-I values, but require independent provenance before treating it as the operational input. Highest-value fields remain CONTROL's alternative numerical trim, real-time input/deck identity, comparison/acceptance basis, calculation/job identity, and direct T+55 provenance.