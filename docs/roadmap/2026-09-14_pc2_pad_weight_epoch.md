# PC+2 numerical-validation roadmap — pad-weight epoch

Date: 2026-09-15
Research notes: `resources/research/137_pc2_pad_weight_epoch_boundary.md` through `resources/research/153_pc2_final_gda_supersession_boundary.md`

## Current resolved boundary

The final Apollo 13 PC+2 P30 LM maneuver PAD explicitly carried `62480 lb` CSM and `33452 lb` LM at GET 077:55:24 for TIG 079:27:38.30; their sum is `95932 lb`. The Flight Control Division report establishes an in-flight, mission-relative RTCC mass-properties lineage (`T-6`, `T+6`, `T+25`, `T+55`), with `T±N` distinct from generation/load time, and shows that stale premission mass properties caused a PC+2 trim challenge later reconciled with Flight Dynamics.

Apollo 11 operational documentation establishes the architecture `mass-properties weight/CG tables -> RTACF/RTCC trajectory processors -> pitch/yaw trim outputs`. Apollo 12 evidence shows RTCC controllers running mass properties before maneuvers in an offline computer in lieu of RTACF. Apollo 13 itself proves separately referencable numbered mass-properties jobs through late-entry **job 27**, which must not be back-projected to PC+2.

Research note 152 identified the ~59-hour interim PC+2 GDA pair (`5.86°`, `6.75°`) and CAPCOM's explicit statement that it would be updated. Research note 153 now proves supersession from the mission-specific LM CONTROL postflight report: immediately before actual PC+2 ignition, the **roll GDA** was approximately `-0.8°`, inferred from its reported motion at ignition to approximately `-2°`, a `-1.2°` delta. Thus the ~59-hour `6.75°` second-axis value did not survive unchanged to ignition. The complete final trim pair remains unrecovered.

Research note 153 also corrects the project's axis normalization. The ~59-hour air-ground exchange contains inconsistent pitch/yaw versus pitch/roll wording; Haise's accepted readback and the LM CONTROL report support recording the second DPS GDA conservatively as **roll**, not yaw. Earlier derivative references to `5.86° pitch / 6.75° yaw` should be read as `5.86° pitch / 6.75° roll` pending a direct pad artifact.

The September 1970 *Apollo 13 Mission Report* gives PC+2/transearth-injection mass as `95,424.0 lb` at ignition and `87,456.0 lb` at cutoff, explicitly as postflight reconstructed mass properties. The `508.0 lb` difference from the final P30 module-weight sum therefore compares distinct historical product classes and must not be normalized away.

## Boundary retained

Keep distinct physical mass/CG, postflight reconstructed event mass, RTCC mass-properties deck/state, module/depletion state, reference epoch, generation/load time, calculation provenance, calculation run, optional job identity, processor inputs/outputs, P30 module weights, commanded trim, observed actuator state, ignition compliance response, and product lifecycle/finality.

Do not infer the cause of the 508-lb difference; assign job 27 to PC+2; attribute the PC+2 job specifically to `T+55`; treat the ~59-hour GDA pair as final; or treat the inferred `-0.8°` pre-ignition roll GDA as a recovered pad-printed trim value.

## Next unresolved numerical inputs

Priority order:

1. recover the final ~78-hour PC+2 P30/GDA pad, Flight Director Log page, or H-2 Flight Dynamics/CONTROL working sheet giving the complete superseding trim pair and its mass-properties provenance/job number;
2. recover the operational module/depletion accounting behind `T+55` and the precise `T+N` reference-epoch convention;
3. recover Apollo 13 Mission Report Supplement 2, *Descent Propulsion System Final Flight Evaluation*;
4. recover LM-7 engine acceptance/calibration or PC+2 high-speed propulsion data;
5. extract original LMS/FMES equations/integration assumptions;
6. recover sufficient state-vector/trajectory information for postburn propagation and regression.

## Integration rule

Do not force a numerical DPS model to reproduce `861.5 ft/s` by assuming either `95932 lb` or `95424.0 lb` is the exact RTCC targeting mass. Preserve provenance. For trim, model the ~59-hour product as interim/superseded; preserve the approximately `-0.8°` pre-ignition roll actuator state separately from the approximately `-2°` ignition response. PC+2 `job_number`, complete final commanded trim, and explicit `T+55` linkage remain unknown until directly sourced.