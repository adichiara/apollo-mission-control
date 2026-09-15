# PC+2 numerical-validation roadmap — pad-weight epoch

Date: 2026-09-15
Research notes: `resources/research/137_pc2_pad_weight_epoch_boundary.md` through `resources/research/161_t55_lm_burn_deck_epoch_boundary.md`

## Current resolved boundary

The final Apollo 13 PC+2 P30 LM maneuver PAD explicitly carried `62480 lb` CSM and `33452 lb` LM at GET 077:55:24 for TIG 079:27:38.30; their sum is `95932 lb`. The Flight Control Division report establishes an in-flight, mission-relative RTCC mass-properties lineage (`T-6`, `T+6`, `T+25`, `T+55`), with `T±N` distinct from generation/load time, and shows that stale premission mass properties caused a PC+2 trim challenge later reconciled with Flight Dynamics.

Apollo 11 operational documentation establishes the architecture `mass-properties weight/CG tables -> RTACF/RTCC trajectory processors -> trim outputs`. Apollo 12 evidence shows RTCC controllers running mass properties before maneuvers in an offline computer in lieu of RTACF. Apollo 13 itself proves separately referencable numbered mass-properties jobs through late-entry **job 27**, which must not be back-projected to PC+2.

Research note 152 identified the ~59-hour interim PC+2 angular GDA pair (`pitch 5.86°`, `roll 6.75°`) and CAPCOM's explicit statement that it would be updated. Research note 157 established that the same pair was actually used for the 61:29 free-return DPS burn, making it an operationally accepted near-term trim after the documented cross-console mass-properties reconciliation.

Research note 158 resolves the previously assumed missing-final-trim problem differently. During the PC+2 two-hour activation at GET 075:07–075:09, Mission Control explicitly inserted `VERB 34 ENTER` **after Noun 47**, terminating the DAP-loading sequence before Noun 48 gimbal-trim entry. Haise asked whether this meant the gimbals already looked all right; Duke answered affirmatively and said there was nothing else on the page. The later burn-rules exchange also records Haise's uncorrected readback that there were **no trim requirements on this burn**. The best-supported model is therefore **no new crew-entered PC+2 trim**, not an unrecovered final Noun 48 pair.

Research note 159 independently verifies that interpretation in Apollo 13's **Luminary 131 flight-software source**. In R03/Verb 48, the Noun 47 response dispatcher sends `V34E` to `ENDR03` and `ENDEXT`; only `V33E PROCEED` continues through mass/moment processing to `DAPDATA3`, which displays Noun 48, and a later proceed response can invoke `TRIMGIMB`. Thus the PC+2 V34 instruction selected a real computer termination branch before N48. This proves the crew/computer behavior but still does not reveal CONTROL's rationale for choosing the no-update branch.

Research note 160 adds the strongest mission-specific precedent yet recovered for that controller-side rationale. In the same Apollo 13 Flight Dynamics report, the **T+25 RTCC mass properties were run but an update was not needed because the resulting pitch/yaw trims were within 0.01° of T+6**. This directly establishes a `new mass-properties run -> compare candidate trims with prior reference -> update/no-update decision` workflow. The `0.01°` criterion is documented only for that T+25/T+6 CSM/SPS case and must not be applied to PC+2 without direct evidence.

Research note 161 tightens the T+55 provenance boundary. The same primary Flight Dynamics chronology explicitly states that **RTCC LM-burn mass-property decks were updated to T+55 decks**. Combined with the later statement that LM CONTROL's disputed PC+2 trim used inferior premission mass properties, this supports a stronger family-level chain: `T+55 LM-burn deck available -> premission CONTROL basis rejected -> Flight Dynamics basis accepted`. It still does not identify the PC+2 calculation time, job number, deck contents, candidate trim, comparison delta, or direct calculation-level link to `5.86° / 6.75°`. Treat `T+55` as a reference/deck epoch, not a calculation timestamp.

Research note 153 establishes PC+2 execution-state evidence. Research note 155 corrects note 154's overbroad unit reinterpretation: the April FCD LM CONTROL narrative reports the PC+2 ignition roll-GDA state in **degrees**, approximately `-2°`, a `-1.2°` change from pre-ignition, implying approximately `-0.8°` immediately before ignition. This is retained/observed execution-state evidence and must not be converted into a supposed final Noun 48 command.

Research note 156 independently showed that the final P30 LM maneuver PAD read up at GET 077:55:24 did **not** contain a GDA trim pair. Notes 158–159 now explain that omission consistently with the activation procedure and software: the crew was deliberately not taken through a new Noun 48 entry.

The September 1970 *Apollo 13 Mission Report* independently provides a postflight PC+2 GDA actuator-displacement trace explicitly in **inches**: initial pitch/roll approximately `+0.13 / -0.28 in`, roll maximum excursion `-0.44 in`, steady-state pitch/roll `-0.21 / -0.55 in`, and cutoff pitch/roll `+0.23 / -0.85 in`.

Primary NASA/Grumman LM hardware documentation resolves why both unit systems appear: GDA stroke is `+2 to -2 in` (±5%) and corresponding engine-gimbal position is `+6° to -6°` (±5%), with gimbal rate `0.2°/sec` (±10%). This supports a **generic nominal** 3°/in hardware scale, not an exact LM-7 flight calibration.

The September Mission Report gives PC+2/transearth-injection mass as `95,424.0 lb` at ignition and `87,456.0 lb` at cutoff, explicitly as postflight reconstructed mass properties. The `508.0 lb` difference from the final P30 module-weight sum therefore compares distinct historical product classes and must not be normalized away.

## Boundary retained

Keep distinct physical mass/CG, postflight reconstructed event mass, RTCC mass-properties deck/state, module/depletion state, reference epoch, generation/load time, calculation provenance, calculation run, optional job identity, processor inputs/outputs, candidate/recommended trim, trim comparison/reference, comparison criterion, update/no-update decision, P30 module weights, crew-entered Noun 48 trim, retained pre-existing gimbal state, observed engine-gimbal angular state, GDA linear actuator displacement, sampled/postflight actuator trace, ignition compliance response, and product lifecycle/finality.

Do not infer the cause of the 508-lb difference; assign job 27 to PC+2; equate `T+55` with a GET 55:00 calculation timestamp; claim a numbered job or direct mathematical `T+55` derivation for `5.86° / 6.75°`; assume the earlier free-return pair remained numerically set at PC+2; invent a final PC+2 Noun 48 pair; transfer the T+25 `0.01°` no-update criterion to PC+2; treat generic 3°/in as exact LM-7 calibration; or substitute postflight actuator displacement for a crew-entered trim command.

## Next unresolved numerical inputs

Priority order:

1. recover a controller-side artifact that explicitly joins the documented **T+55 LM-burn deck family** to the PC+2 equivalent of the T+25 comparison: calculation time/job identity, candidate trim, current/reference trim, comparison delta/tolerance, and disposition;
2. recover a direct record tying the accepted `5.86° / 6.75°` free-return trim to a specific T+55 calculation run/job;
3. recover the operational module/depletion accounting behind the final Noun 47 weights (`62480 / 33452 lb`) and the precise `T+N` reference-epoch convention;
4. recover LM-7-specific GDA/engine acceptance calibration if a higher-fidelity degrees↔inches transform is needed;
5. recover Apollo 13 Mission Report Supplement 2, *Descent Propulsion System Final Flight Evaluation*;
6. recover PC+2 high-speed propulsion data;
7. extract original LMS/FMES equations/integration assumptions;
8. recover sufficient state-vector/trajectory information for postburn propagation and regression.

## Integration rule

Do not force a numerical DPS model to reproduce `861.5 ft/s` by assuming either `95932 lb` or `95424.0 lb` is the exact RTCC targeting mass. Preserve provenance. For trim/GDA, model an explicit deck-selection/calculation/comparison/update decision and distinguish any computed recommendation from a crew-entered Noun 48 value and from retained/observed gimbal state. Apollo 13 now directly demonstrates that an RTCC mass-properties recalculation could leave the prior trim operationally unchanged after comparison; for PC+2, primary operational evidence plus Apollo 13 flight-software evidence supports **V34 termination at Noun 47, before Noun 48**. The T+55 LM-burn deck family is directly documented, but PC+2 `calculation_time`, `job_number`, candidate trim, comparison delta/tolerance, exact retained two-axis pre-ignition gimbal state, and direct calculation-level T+55 linkage remain unknown until sourced.