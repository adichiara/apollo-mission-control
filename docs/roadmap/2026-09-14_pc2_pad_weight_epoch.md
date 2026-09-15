# PC+2 numerical-validation roadmap — pad-weight epoch

Date: 2026-09-15
Research notes: `resources/research/137_pc2_pad_weight_epoch_boundary.md` through `resources/research/155_pc2_gda_dual_units_and_calibration.md`

## Current resolved boundary

The final Apollo 13 PC+2 P30 LM maneuver PAD explicitly carried `62480 lb` CSM and `33452 lb` LM at GET 077:55:24 for TIG 079:27:38.30; their sum is `95932 lb`. The Flight Control Division report establishes an in-flight, mission-relative RTCC mass-properties lineage (`T-6`, `T+6`, `T+25`, `T+55`), with `T±N` distinct from generation/load time, and shows that stale premission mass properties caused a PC+2 trim challenge later reconciled with Flight Dynamics.

Apollo 11 operational documentation establishes the architecture `mass-properties weight/CG tables -> RTACF/RTCC trajectory processors -> trim outputs`. Apollo 12 evidence shows RTCC controllers running mass properties before maneuvers in an offline computer in lieu of RTACF. Apollo 13 itself proves separately referencable numbered mass-properties jobs through late-entry **job 27**, which must not be back-projected to PC+2.

Research note 152 identified the ~59-hour interim PC+2 angular GDA pair (`pitch 5.86°`, `roll 6.75°`) and CAPCOM's explicit statement that it would be updated. Research note 153 establishes supersession. Research note 155 corrects note 154's overbroad unit reinterpretation: the April FCD LM CONTROL narrative reports the PC+2 ignition roll-GDA state in **degrees**, approximately `-2°`, a `-1.2°` change from pre-ignition, implying approximately `-0.8°` immediately before ignition.

The September 1970 *Apollo 13 Mission Report* independently provides a postflight PC+2 GDA actuator-displacement trace explicitly in **inches**: initial pitch/roll approximately `+0.13 / -0.28 in`, roll maximum excursion `-0.44 in`, steady-state pitch/roll `-0.21 / -0.55 in`, and cutoff pitch/roll `+0.23 / -0.85 in`.

Primary NASA/Grumman LM hardware documentation resolves why both unit systems appear: GDA stroke is `+2 to -2 in` (±5%) and corresponding engine-gimbal position is `+6° to -6°` (±5%), with gimbal rate `0.2°/sec` (±10%). This supports a **generic nominal** 3°/in hardware scale, not an exact LM-7 flight calibration. As a consistency check only, the Mission Report initial roll `-0.28 in` maps nominally to `-0.84°`, close to LM CONTROL's approximate pre-ignition `-0.8°`; sample identity is not proven.

The September Mission Report gives PC+2/transearth-injection mass as `95,424.0 lb` at ignition and `87,456.0 lb` at cutoff, explicitly as postflight reconstructed mass properties. The `508.0 lb` difference from the final P30 module-weight sum therefore compares distinct historical product classes and must not be normalized away.

## Boundary retained

Keep distinct physical mass/CG, postflight reconstructed event mass, RTCC mass-properties deck/state, module/depletion state, reference epoch, generation/load time, calculation provenance, calculation run, optional job identity, processor inputs/outputs, P30 module weights, commanded angular trim, observed engine-gimbal angular state, GDA linear actuator displacement, sampled/postflight actuator trace, ignition compliance response, and product lifecycle/finality.

Do not infer the cause of the 508-lb difference; assign job 27 to PC+2; attribute the PC+2 job specifically to `T+55`; treat the ~59-hour angular pair as final; treat generic 3°/in as exact LM-7 calibration; or substitute postflight actuator displacement for the missing final commanded angular trim.

## Next unresolved numerical inputs

Priority order:

1. recover the final ~78-hour PC+2 P30/GDA pad, Flight Director Log page, or H-2 Flight Dynamics/CONTROL working sheet giving the complete superseding **angular** trim pair and its mass-properties provenance/job number;
2. recover LM-7-specific GDA/engine acceptance calibration if a higher-fidelity degrees↔inches transform is needed;
3. recover the operational module/depletion accounting behind `T+55` and the precise `T+N` reference-epoch convention;
4. recover Apollo 13 Mission Report Supplement 2, *Descent Propulsion System Final Flight Evaluation*;
5. recover PC+2 high-speed propulsion data;
6. extract original LMS/FMES equations/integration assumptions;
7. recover sufficient state-vector/trajectory information for postburn propagation and regression.

## Integration rule

Do not force a numerical DPS model to reproduce `861.5 ft/s` by assuming either `95932 lb` or `95424.0 lb` is the exact RTCC targeting mass. Preserve provenance. For trim/GDA, require explicit representation and units: commanded trim and LM CONTROL execution state are angular; the September Mission Report telemetry table is linear actuator displacement. The documented generic hardware scale is ±2 in ↔ ±6°, but exact LM-7 calibration remains unknown. PC+2 `job_number`, complete final commanded angular trim, and explicit `T+55` linkage remain unknown until directly sourced.