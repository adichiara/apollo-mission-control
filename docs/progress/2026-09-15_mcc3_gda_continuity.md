# MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/171_rtacf_mass_properties_trim_artifact_class.md`

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
- **New in note 171:** contemporary Apollo 11 Flight Dynamics documentation identifies the relevant computational artifact class: RTACF mass-properties computations included **weight-c.g. tables used by RTACF and RTCC trajectory processors to compute pitch/yaw trim angles**. This is adjacent-mission architecture evidence only; it does not establish the Apollo 13 job path.

## Next

Search Apollo 13 archival/controller material specifically for weight/c.g. or mass-properties tables, RTACF/RTCC trajectory-processor trim output, and associated job/request sheets behind the ~59 GET disagreement. Highest-value fields remain CONTROL's alternative numerical trim, input mass-properties identity, comparison/acceptance basis, calculation/job identity, and direct T+55 provenance.