# MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/176_t55_lm_burn_deck_scope.md`

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
- Note 174 established that `T+6`, `T+25`, and `T+55` function as time-tagged mass-properties set/deck labels or reference epochs, not calculation timestamps or job identifiers.
- Note 175 established that the exact `5.86 / 6.75` pair previously passed on the provisional PC+2 pad was also passed and accepted as the commanded LM GDA pair for the 61:29 free-return DPS burn.
- **New in note 176:** the primary Flight Dynamics chronology explicitly scopes the T+55 update as **RTCC (LM burn) mass property decks**. Combined with the earlier mission-specific T+25 RTCC mass-properties run that explicitly produced/evaluated pitch/yaw trims, this narrows T+55 to the correct LM-burn computational domain without asserting direct lineage to `5.86 / 6.75`.
- Kept commanded trim, post-compliance actuator state, and later `5.85 / 6.74` PC+2 reference readback as separate provenance layers.

## Next

Search Apollo 13 archival/controller material specifically for the real-time T+55 weight/c.g. or mass-properties output, RTCC/RTACF LM-burn trim output, and associated job/request sheet behind the ~59 GET disagreement. Highest-value fields remain CONTROL's alternative numerical trim, explicit T+55-reference-deck-to-job linkage for `5.86 / 6.75`, PC+2-specific comparison/acceptance basis, and calculation/job identity. Also seek telemetry or a controller working sheet that records the exact two-axis GDA state after 61:29 powered-flight compliance.