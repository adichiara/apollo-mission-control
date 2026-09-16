# PC+2 controller-record roadmap — GDA state continuity

Date: 2026-09-15  
Latest research note: `resources/research/174_tplus_mass_properties_deck_semantics.md`

## Roadmap refinement

The historical chain now separates three numerical/state layers that must not be collapsed:

1. **~59 GET Flight Dynamics PC+2 abort-pad trim solution:** `5.86° / 6.75°`. Primary voice identifies the pair as DPS trim/GDA angles for PC+2; the Flight Dynamics chronology says the passed trim was challenged by LM CONTROL, which had used premission mass properties, and that CONTROL later agreed with Flight Dynamics' data.
2. **Post-61:29 intended/retained PC+2 reference:** `5.85 / 6.74`, read back with "GDA should be okay as is" and qualified by "hopefully." This is not measured actuator telemetry.
3. **Immediately pre-PC+2 execution-state roll:** approximately `-0.8°`, derived from CONTROL's approximate report that roll moved to about `-2°` by `-1.2°` at ignition. This remains derived/approximate.

RTCC LM-burn mass-property decks were documented as updated to T+55 decks. Notes 173–174 refine the provenance: the Flight Control Division report uses real-time information and, within the same chronology, uses `T+6`, `T+25`, and `T+55` as time-tagged mass-properties set/deck labels. Treat `T+55` as a **reference epoch label**, not as a calculation timestamp or job number. The chronology places the T+55 update entry before LM ingress at 53:26/54:25 GET, so it does not support an assumption that the deck was generated/loaded exactly at 55:00 GET.

The same mission-specific chronology provides an earlier mass-properties update precedent: the T+25 RTCC mass-properties run required no update because pitch/yaw trims were within `0.01°` of T+6. This directly establishes a time-tagged mass-properties run -> trim comparison -> update/no-update workflow on Apollo 13. It does **not** establish `0.01°` as the later PC+2 criterion.

Research note 171 adds adjacent-mission architecture evidence from the contemporary Apollo 11 Flight Dynamics record: RTACF mass-properties computations produced **weight-c.g. tables used by RTACF and RTCC trajectory processors to compute pitch/yaw trim angles**. This does not prove the Apollo 13 job path, but it narrows the archival artifact class to seek.

Research note 172 adds a mission-specific **postflight validation layer** from Apollo 13 Mission Report Table A-I. For the second midcourse correction it reports ignition mass/c.g. `95,959.9 lb; 378.8 / 4.9 / 0.7 in` and cutoff `95,647.1 lb; 379.4 / 5.0 / 0.7 in`. Because the report states these are postflight-analysis values, they must not be treated as the real-time T+55/controller input deck.

## Highest-priority unresolved artifact

Search Apollo 13 archival/controller material specifically for the real-time mass-properties/trim artifact chain behind the ~59 GET disagreement:

1. weight/c.g. table or equivalent real-time mass-properties computation output;
2. RTACF/RTCC trajectory-processor trim output or associated request/job sheet;
3. LM CONTROL's alternative numerical trim from its premission-mass-properties calculation;
4. comparison delta and PC+2-specific acceptance/decision criterion;
5. calculation time and job/run/request identity;
6. explicit linkage from the **T+55 reference-epoch deck** to the Flight Dynamics `5.86 / 6.75` solution;
7. deck generation/load timestamp if recoverable, kept distinct from its T+55 reference epoch;
8. comparison of any recovered operational mass-properties artifact with postflight Table A-I, without conflating the two provenance layers;
9. if available, the later calculation/state record explaining the `5.85 / 6.74` post-61:29 retained-reference readback.

Use the Apollo 13 T+25 `0.01°` no-update result as a search discriminator and workflow precedent only. Do not infer that it was a universal threshold or the PC+2 rule. Do not infer that Apollo 13 used the exact Apollo 11 RTACF program, request procedure, or output format. Do not substitute Apollo 13 postflight Table A-I values for the missing real-time deck.