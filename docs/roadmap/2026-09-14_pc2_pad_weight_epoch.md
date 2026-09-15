# PC+2 numerical-validation roadmap — pad-weight epoch

Date: 2026-09-15
Research notes: `resources/research/137_pc2_pad_weight_epoch_boundary.md` through `resources/research/158_pc2_no_new_gda_trim_load.md`

## Current resolved boundary

The final Apollo 13 PC+2 P30 LM maneuver PAD explicitly carried `62480 lb` CSM and `33452 lb` LM at GET 077:55:24 for TIG 079:27:38.30; their sum is `95932 lb`. The Flight Control Division report establishes an in-flight, mission-relative RTCC mass-properties lineage (`T-6`, `T+6`, `T+25`, `T+55`), with `T±N` distinct from generation/load time, and shows that stale premission mass properties caused a PC+2 trim challenge later reconciled with Flight Dynamics.

Apollo 11 operational documentation establishes the architecture `mass-properties weight/CG tables -> RTACF/RTCC trajectory processors -> trim outputs`. Apollo 12 evidence shows RTCC controllers running mass properties before maneuvers in an offline computer in lieu of RTACF. Apollo 13 itself proves separately referencable numbered mass-properties jobs through late-entry **job 27**, which must not be back-projected to PC+2.

Research note 152 identified the ~59-hour interim PC+2 angular GDA pair (`pitch 5.86°`, `roll 6.75°`) and CAPCOM's explicit statement that it would be updated. Research note 157 established that the same pair was actually used for the 61:29 free-return DPS burn, making it an operationally accepted near-term trim after the documented cross-console mass-properties reconciliation.

Research note 158 resolves the previously assumed missing-final-trim problem differently. During the PC+2 two-hour activation at GET 075:07–075:09, Mission Control explicitly inserted `VERB 34 ENTER` **after Noun 47**, terminating the DAP-loading sequence before Noun 48 gimbal-trim entry. Haise asked whether this meant the gimbals already looked all right; Duke answered affirmatively and said there was nothing else on the page. The later burn-rules exchange also records Haise's uncorrected readback that there were **no trim requirements on this burn**. The best-supported model is therefore **no new crew-entered PC+2 trim**, not an unrecovered final Noun 48 pair.

Research note 153 establishes PC+2 execution-state evidence. Research note 155 corrects note 154's overbroad unit reinterpretation: the April FCD LM CONTROL narrative reports the PC+2 ignition roll-GDA state in **degrees**, approximately `-2°`, a `-1.2°` change from pre-ignition, implying approximately `-0.8°` immediately before ignition. This is retained/observed execution-state evidence and must not be converted into a supposed final Noun 48 command.

Research note 156 independently showed that the final P30 LM maneuver PAD read up at GET 077:55:24 did **not** contain a GDA trim pair. Note 158 now explains that omission consistently with the activation procedure: the crew was deliberately not taken through a new Noun 48 entry.

The September 1970 *Apollo 13 Mission Report* independently provides a postflight PC+2 GDA actuator-displacement trace explicitly in **inches**: initial pitch/roll approximately `+0.13 / -0.28 in`, roll maximum excursion `-0.44 in`, steady-state pitch/roll `-0.21 / -0.55 in`, and cutoff pitch/roll `+0.23 / -0.85 in`.

Primary NASA/Grumman LM hardware documentation resolves why both unit systems appear: GDA stroke is `+2 to -2 in` (±5%) and corresponding engine-gimbal position is `+6° to -6°` (±5%), with gimbal rate `0.2°/sec` (±10%). This supports a **generic nominal** 3°/in hardware scale, not an exact LM-7 flight calibration.

The September Mission Report gives PC+2/transearth-injection mass as `95,424.0 lb` at ignition and `87,456.0 lb` at cutoff, explicitly as postflight reconstructed mass properties. The `508.0 lb` difference from the final P30 module-weight sum therefore compares distinct historical product classes and must not be normalized away.

## Boundary retained

Keep distinct physical mass/CG, postflight reconstructed event mass, RTCC mass-properties deck/state, module/depletion state, reference epoch, generation/load time, calculation provenance, calculation run, optional job identity, processor inputs/outputs, P30 module weights, computed/recommended trim, update/no-update decision, crew-entered Noun 48 trim, retained pre-existing gimbal state, observed engine-gimbal angular state, GDA linear actuator displacement, sampled/postflight actuator trace, ignition compliance response, and product lifecycle/finality.

Do not infer the cause of the 508-lb difference; assign job 27 to PC+2; claim a numbered job or direct mathematical `T+55` derivation for `5.86° / 6.75°`; assume the earlier free-return pair remained numerically set at PC+2; invent a final PC+2 Noun 48 pair; treat generic 3°/in as exact LM-7 calibration; or substitute postflight actuator displacement for a crew-entered trim command.

## Next unresolved numerical inputs

Priority order:

1. recover an H-2 CONTROL/Flight Dynamics working sheet, Flight Director Log entry, GDA setup/checklist record, or mass-properties job output documenting the **basis for the PC+2 no-trim-update decision** — ideally a calculated trim, comparison tolerance, retained gimbal state, and/or job identity;
2. recover a direct record tying the accepted `5.86° / 6.75°` free-return trim to a specific `T+55` calculation run/job;
3. recover the operational module/depletion accounting behind the final Noun 47 weights (`62480 / 33452 lb`) and the precise `T+N` reference-epoch convention;
4. recover LM-7-specific GDA/engine acceptance calibration if a higher-fidelity degrees↔inches transform is needed;
5. recover Apollo 13 Mission Report Supplement 2, *Descent Propulsion System Final Flight Evaluation*;
6. recover PC+2 high-speed propulsion data;
7. extract original LMS/FMES equations/integration assumptions;
8. recover sufficient state-vector/trajectory information for postburn propagation and regression.

## Integration rule

Do not force a numerical DPS model to reproduce `861.5 ft/s` by assuming either `95932 lb` or `95424.0 lb` is the exact RTCC targeting mass. Preserve provenance. For trim/GDA, model an explicit update/no-update decision and distinguish any computed recommendation from a crew-entered Noun 48 value and from retained/observed gimbal state. For PC+2, primary operational evidence now supports **no new Noun 48 entry**. PC+2 `job_number`, the calculation-level basis for the no-update decision, exact retained two-axis pre-ignition gimbal state, and explicit calculation-level `T+55` linkage remain unknown until directly sourced.