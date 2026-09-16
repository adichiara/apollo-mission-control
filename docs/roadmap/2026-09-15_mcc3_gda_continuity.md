# PC+2 controller-record roadmap — GDA state continuity

Date: 2026-09-15  
Latest research note: `resources/research/176_t55_lm_burn_deck_scope.md`

## Roadmap refinement

The historical chain separates four numerical/state layers that must not be collapsed:

1. **~59 GET provisional Flight Dynamics PC+2 abort-pad trim:** `5.86° / 6.75°`. Primary voice identifies the pair as DPS trim/GDA angles for PC+2 and says the angles "will be updated" while instructing the crew to use them for the moment. The Flight Dynamics chronology says the passed trim was challenged by LM CONTROL, which had used premission mass properties, and that CONTROL later agreed with Flight Dynamics' data.
2. **61:29 free-return DPS commanded trim:** primary NASA air-to-ground voice at 60:53–60:56 GET passes and confirms the same `5.86° / 6.75°` pair as the LM GDA angles for the intervening free-return burn. This directly carries the numerical pair into the maneuver whose 40% powered-flight compliance CONTROL later identified as setting the GDA state relevant to PC+2.
3. **Post-61:29 intended/retained PC+2 reference:** `5.85 / 6.74`, read back with "GDA should be okay as is" and qualified by "hopefully." This is not measured actuator telemetry and must not be substituted for the exact post-compliance state.
4. **Immediately pre-PC+2 execution-state roll:** approximately `-0.8°`, derived from CONTROL's approximate report that roll moved to about `-2°` by `-1.2°` at ignition. This remains derived/approximate.

The strengthened continuity chain is:

`~59 provisional PC+2 5.86 / 6.75 -> same pair commanded for 61:29 free-return DPS burn -> 40% powered-flight compliance -> exact resulting GDA state unrecovered -> CONTROL expects resulting state optimum for PC+2 -> later 5.85 / 6.74 "okay as is" reference -> no new PC+2 Noun 48 trim load`.

RTCC mass-property provenance is now narrowed one step further. The primary Apollo 13 Flight Dynamics chronology explicitly calls the T+55 products **"RTCC (LM burn) mass property decks."** The same chronology's earlier T+25 case explicitly connects an RTCC mass-properties run to pitch/yaw trim comparison. Thus T+55 is source-backed as a reference-epoch deck in the correct LM-burn processing domain, not merely a generic mass-properties update. Direct consumption by the `5.86 / 6.75` solution remains unproven.

Research note 171 adds adjacent-mission architecture evidence that RTACF mass-properties computations produced weight-c.g. tables used by RTACF and RTCC trajectory processors to compute pitch/yaw trim angles. Research note 172 adds Apollo 13 postflight mass-properties values as a validation layer only; they are not the missing real-time deck.

## Highest-priority unresolved artifact

Search Apollo 13 archival/controller material specifically for the real-time mass-properties/trim data-lineage chain behind the ~59 GET disagreement:

1. T+55 weight/c.g. table or equivalent real-time mass-properties computation output;
2. RTACF/RTCC LM-burn trajectory-processor trim output or associated request/job sheet;
3. LM CONTROL's alternative numerical trim from its premission-mass-properties calculation;
4. comparison delta and PC+2-specific acceptance/decision criterion;
5. calculation time and job/run/request identity;
6. explicit linkage from the **T+55 reference-epoch RTCC LM-burn deck** to the Flight Dynamics `5.86 / 6.75` solution;
7. deck generation/load timestamp if recoverable, kept distinct from its T+55 reference epoch;
8. telemetry or controller working-sheet evidence for the exact post-61:29 complied two-axis GDA state;
9. the calculation/state record, if any, explaining the later `5.85 / 6.74` reference readback.

Do not infer that the exact post-compliance state was `5.86 / 6.75`, that `5.85 / 6.74` was measured telemetry, that their `0.01°` per-axis difference was a PC+2 criterion, or that T+55 directly generated either numerical pair.