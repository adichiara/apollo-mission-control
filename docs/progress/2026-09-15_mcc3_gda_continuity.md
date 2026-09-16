# MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/174_tplus_mass_properties_deck_semantics.md`

## Completed

- Reconciled the apparent `MCC-3` contradiction in the Flight Control Division report.
- Established that LM CONTROL calls the 61:29 contingency free-return DPS burn `MCC-3 - DPS 1`, although trajectory/mission-summary material calls that maneuver MCC-4 and records the originally planned MCC-3 as omitted.
- Added primary voice evidence immediately before the 61:29 burn: CAPCOM states that the GDA settings are "go as they are."
- Recovered the pre-61:29 checkout observation `within about 0.3` / `plenty close`, classified only as hardware checkout evidence.
- Derived approximate immediately pre-PC+2 roll-GDA position `~-0.8°` from CONTROL's reported ignition motion; retained it as approximate execution-state evidence only.
- Recovered the post-61:29 PC+2 retained-reference readback `5.85 / 6.74`, qualified by the crew's "hopefully" and not treated as actuator telemetry.
- Note 170 joined the ~59 GET air-to-ground readback to the Flight Dynamics postflight chronology. The `5.86 / 6.75` pair is classified as the Flight Dynamics PC+2 abort-pad DPS trim solution passed to the crew at ~59 GET.
- The same primary Flight Dynamics account says LM CONTROL challenged that passed trim using **premission mass properties**, then later agreed with Flight Dynamics' data.
- Note 171 identified the adjacent-mission computational artifact class: weight-c.g. tables used by RTACF/RTCC trajectory processors to compute pitch/yaw trim.
- Note 172 added the Apollo 13 Mission Report postflight validation layer for the second midcourse correction: ignition 95,959.9 lb with c.g. 378.8 / 4.9 / 0.7 in; cutoff 95,647.1 lb with c.g. 379.4 / 5.0 / 0.7 in. These remain postflight values, not the real-time deck.
- Note 173 established the T+55 RTCC LM-burn mass-property deck update as real-time operational evidence and recovered the T+25/T+6 `0.01°` no-update precedent.
- **New in note 174:** the Apollo 13 Flight Dynamics chronology itself shows that `T+6`, `T+25`, and `T+55` are time-tagged mass-properties set/deck labels or reference epochs. `T+55` must not be treated as a calculation timestamp or job identifier.
- The chronology lists the T+55 deck update before the 53:26/54:25 LM-ingress entries, reinforcing that the label is not evidence that generation/loading occurred exactly at 55:00 GET.
- Kept the `0.01°` boundary strict: it is evidence for the T+25/T+6 decision only, not a universal threshold and not evidence for the later PC+2 criterion.

## Next

Search Apollo 13 archival/controller material specifically for the real-time weight/c.g. or mass-properties table, RTACF/RTCC trajectory-processor trim output, and associated job/request sheet behind the ~59 GET disagreement. Highest-value fields remain CONTROL's alternative numerical trim, explicit T+55-reference-deck-to-job linkage for `5.86 / 6.75`, PC+2-specific comparison/acceptance basis, and calculation/job identity. Keep deck reference epoch, deck generation/load time, and downstream job identity as separate provenance fields.