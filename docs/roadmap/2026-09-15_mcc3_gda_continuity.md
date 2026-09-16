# PC+2 controller-record roadmap — GDA state continuity

Date: 2026-09-15  
Latest research note: `resources/research/170_pc2_59h_trim_provenance.md`

## Roadmap refinement

The historical chain now separates three numerical/state layers that must not be collapsed:

1. **~59 GET Flight Dynamics PC+2 abort-pad trim solution:** `5.86° / 6.75°`. Primary voice identifies the pair as DPS trim/GDA angles for PC+2; the Flight Dynamics postflight chronology says the DPS trim passed on that ~59 GET pad was challenged by LM CONTROL, which had used premission mass properties, and that CONTROL later agreed with Flight Dynamics' data.
2. **Post-61:29 intended/retained PC+2 reference:** `5.85 / 6.74`, read back with "GDA should be okay as is" and qualified by "hopefully." This is not measured actuator telemetry.
3. **Immediately pre-PC+2 execution-state roll:** approximately `-0.8°`, derived from CONTROL's approximate report that roll moved to about `-2°` by `-1.2°` at ignition. This remains derived/approximate.

The ~59 GET pair is therefore no longer merely an unexplained interim value: it has source-backed Flight Dynamics provenance and a documented competing LM CONTROL calculation based on inferior premission mass properties.

RTCC LM-burn mass-property decks were separately documented as updated to T+55 decks. That establishes the available Flight Dynamics mass-property context, but not a direct calculation-level `T+55 -> 5.86 / 6.75` link.

## Highest-priority unresolved artifact

Find the controller/RTCC working artifact for the ~59 GET disagreement:

1. LM CONTROL's alternative numerical trim from its premission-mass-properties calculation;
2. comparison delta and acceptance/decision criterion;
3. calculation time and RTCC/RTACF job/run identity;
4. explicit deck/input provenance for the Flight Dynamics `5.86 / 6.75` solution, ideally direct T+55 linkage;
5. if available, the later calculation or state record explaining the `5.85 / 6.74` post-61:29 retained-reference readback;
6. telemetry/working-sheet evidence reconciling retained reference with actual GDA actuator position.

Do not infer a PC+2 `0.01°` criterion from the numerical difference between `5.86 / 6.75` and `5.85 / 6.74`, and do not import the separate T+25 SPS no-update criterion. Keep passed/candidate trim, competing calculation, retained reference, hardware checkout, powered-flight compliance, and actuator state as separate provenance layers.