# PC+2 controller-record roadmap — GDA state continuity

Date: 2026-09-15  
Latest research note: `resources/research/171_rtacf_mass_properties_trim_artifact_class.md`

## Roadmap refinement

The historical chain now separates three numerical/state layers that must not be collapsed:

1. **~59 GET Flight Dynamics PC+2 abort-pad trim solution:** `5.86° / 6.75°`. Primary voice identifies the pair as DPS trim/GDA angles for PC+2; the Flight Dynamics postflight chronology says the DPS trim passed on that ~59 GET pad was challenged by LM CONTROL, which had used premission mass properties, and that CONTROL later agreed with Flight Dynamics' data.
2. **Post-61:29 intended/retained PC+2 reference:** `5.85 / 6.74`, read back with "GDA should be okay as is" and qualified by "hopefully." This is not measured actuator telemetry.
3. **Immediately pre-PC+2 execution-state roll:** approximately `-0.8°`, derived from CONTROL's approximate report that roll moved to about `-2°` by `-1.2°` at ignition. This remains derived/approximate.

RTCC LM-burn mass-property decks were separately documented as updated to T+55 decks. That establishes the available Flight Dynamics mass-property context, but not a direct calculation-level `T+55 -> 5.86 / 6.75` link.

Research note 171 adds adjacent-mission architecture evidence from the contemporary Apollo 11 Flight Dynamics record: RTACF mass-properties computations produced **weight-c.g. tables used by RTACF and RTCC trajectory processors to compute pitch/yaw trim angles**. This does not prove the Apollo 13 job path, but it narrows the archival artifact class to seek.

## Highest-priority unresolved artifact

Search Apollo 13 archival/controller material specifically for the mass-properties/trim artifact chain behind the ~59 GET disagreement:

1. weight/c.g. table or equivalent mass-properties computation output;
2. RTACF/RTCC trajectory-processor trim output or associated request/job sheet;
3. LM CONTROL's alternative numerical trim from its premission-mass-properties calculation;
4. comparison delta and acceptance/decision criterion;
5. calculation time and job/run/request identity;
6. explicit deck/input provenance for the Flight Dynamics `5.86 / 6.75` solution, ideally direct T+55 linkage;
7. if available, the later calculation/state record explaining the `5.85 / 6.74` post-61:29 retained-reference readback.

Do not infer that Apollo 13 used the exact Apollo 11 RTACF program, request procedure, or output format. Do not infer a PC+2 `0.01°` criterion from the numerical difference between `5.86 / 6.75` and `5.85 / 6.74`, and do not import the separate T+25 SPS no-update criterion.