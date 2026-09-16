# PC+2 controller-record roadmap — GDA state continuity

Date: 2026-09-15  
Latest research note: `resources/research/178_ntrs_19710010485_metadata_payload_mismatch.md`

## Roadmap refinement

The historical chain separates four numerical/state layers that must not be collapsed:

1. **~59 GET provisional Flight Dynamics PC+2 abort-pad trim:** `5.86° / 6.75°`. Primary voice identifies the pair as DPS trim/GDA angles for PC+2 and says the angles "will be updated" while instructing the crew to use them for the moment. The Flight Dynamics chronology says the passed trim was challenged by LM CONTROL, which had used premission mass properties, and that CONTROL later agreed with Flight Dynamics' data.
2. **61:29 free-return DPS commanded trim:** primary NASA air-to-ground voice at 60:53–60:56 GET passes and confirms the same `5.86° / 6.75°` pair as the LM GDA angles for the intervening free-return burn.
3. **Post-61:29 intended/retained PC+2 reference:** `5.85 / 6.74`, read back with "GDA should be okay as is" and qualified by "hopefully." This is not measured actuator telemetry.
4. **Immediately pre-PC+2 execution-state roll:** approximately `-0.8°`, derived from CONTROL's approximate report that roll moved to about `-2°` by `-1.2°` at ignition.

The strengthened continuity chain is:

`~59 provisional PC+2 5.86 / 6.75 -> same pair commanded for 61:29 free-return DPS burn -> 40% powered-flight compliance -> exact resulting GDA state unrecovered -> CONTROL expects resulting state optimum for PC+2 -> later 5.85 / 6.74 "okay as is" reference -> no new PC+2 Noun 48 trim load`.

RTCC mass-property provenance is source-backed only in discrete operations. The Apollo 13 chronology distinguishes: T-6 mass properties **generated** and **loaded in the RTCC**; T+25 RTCC mass properties **run** with P/Y trim comparison; and later RTCC LM-burn mass-property decks **updated to T+55 decks**. Because the source uses these operations distinctly, the T+55 deck update is not treated as proof of generation, loading, or downstream trim-run execution. Direct consumption by the `5.86 / 6.75` solution remains unproven.

Research note 171 adds adjacent-mission architecture evidence that RTACF mass-properties computations produced weight-c.g. tables used by RTACF and RTCC trajectory processors to compute pitch/yaw trim angles. Research note 172 adds Apollo 13 postflight mass-properties values as a validation layer only.

Research note 178 adds an archive-provenance gate: NTRS citation `19710010485` currently has metadata for a different Apollo 13 investigation report while serving the Flight Control Division Mission Operations Report as its PDF payload. Future archival identifiers must be checked at both metadata and payload levels; `19710010485` is not treated as an unambiguous bibliographic identifier for the Mission Operations Report.

## Highest-priority unresolved artifact

Search Apollo 13 archival/controller material specifically for the real-time mass-properties/trim data-lineage chain behind the ~59 GET disagreement:

1. T+55 weight/c.g. table or equivalent real-time mass-properties computation output;
2. explicit T+55 **generation/load record** or **downstream run/request/output**;
3. RTACF/RTCC LM-burn trajectory-processor trim output or associated request/job sheet;
4. LM CONTROL's alternative numerical trim from its premission-mass-properties calculation;
5. comparison delta and PC+2-specific acceptance/decision criterion;
6. calculation time and job/run/request identity;
7. explicit linkage from the T+55 RTCC LM-burn deck to the Flight Dynamics `5.86 / 6.75` solution;
8. telemetry or controller working-sheet evidence for the exact post-61:29 complied two-axis GDA state;
9. the calculation/state record, if any, explaining the later `5.85 / 6.74` reference readback.

Do not infer that `deck updated` means `generated`, `loaded`, or `run`; that the exact post-compliance state was `5.86 / 6.75`; that `5.85 / 6.74` was measured telemetry; that the `0.01°` differences establish a PC+2 criterion; that T+55 directly generated either numerical pair; or that archive landing-page metadata necessarily describes the payload currently served under the same identifier.