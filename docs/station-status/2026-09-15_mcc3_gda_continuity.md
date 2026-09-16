# Station research status — MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/188_post_flyby_pc2_gda_instruction_semantics.md`

## CONTROL

**Improved.** The Flight Dynamics primary account establishes that LM CONTROL challenged the DPS trim passed on the ~59 GET PC+2 abort pad because CONTROL had used **premission mass properties**; CONTROL later agreed with Flight Dynamics' data. The air-to-ground record identifies the passed pair as pitch `5.86°`, roll `6.75°`.

Primary mission voice also establishes that the same `5.86 / 6.75` pair was commanded for the 61:29 free-return DPS burn. The Flight Director loop gives a precise operational role for CONTROL immediately before that burn: CONTROL directs the gimbal-trim checkout, says `Trim looks okay`, and when FLIGHT asks how close the values are reports `within about 0.3` and `plenty close`, then reports readiness. This is classified as a **spacecraft preburn checkout acceptance**, not the missing Flight Dynamics/CONTROL ground-calculation comparison rule.

CONTROL later says the 40%-thrust compliance during the burn was expected to leave the GDA state optimum for PC+2.

CONTROL's alternative numerical solution, exact mass-properties inputs, ground-computation comparison delta/acceptance rule, and direct T+55 run lineage remain unrecovered.

## FLIGHT / CAPCOM

**Improved.** Primary voice at ~59 GET identifies `5.86 / 6.75` as a provisional PC+2 DPS trim/GDA pair and says the angles "will be updated." At 60:53–60:56 GET, CAPCOM passes the same pair on the actual 61:29 free-return DPS pad and accepts Haise's readback. FLIGHT then explicitly queries CONTROL about preburn trim closeness; CONTROL's `~0.3` answer is accepted for proceeding.

Research note 188 corrects the later event using the clearer NASA transcript rendering: CAPCOM issues a new PC+2 P30 pad and says the GDA `ought to be okay as it is from the last burn`, specifying **pitch `5.85`, roll `6.74`**. This is a ground-issued desired/reference pair plus no-action disposition, not a crew `hopefully` estimate and not telemetry.

## GUIDANCE

**Boundary retained.** The immediate post-61:29 `0.2` trim exchange remains unclassified as a GDA quantity absent explicit primary evidence.

## Flight Dynamics / RTCC / RTACF

**Improved but unresolved.** The Flight Control Division Mission Operations Report distinguishes T-6 mass properties generated/loaded in RTCC, T+25 RTCC mass properties run with pitch/yaw trim evaluation, and later RTCC LM-burn mass-property decks updated to T+55 decks. T+55 remains a reference-set/deck state, not proof of a generation/load/run event or direct `5.86 / 6.75` lineage.

The T+25 `0.01°` no-update result, the 61:11 `~0.3°` spacecraft checkout, and the later `0.01°` per-axis difference between the two ground references are explicitly separate contexts. None is generalized into the missing PC+2 ground-computation comparison criterion.

Still unresolved: T+55 weight/c.g./deck contents, generation/load event, downstream run/request/output, CONTROL's competing numerical values, PC+2 ground-computation acceptance criterion, RTCC/RTACF job identity, and direct T+55-to-`5.86 / 6.75` data lineage.

## Simulator constraint

Represent `reference_epoch`, `processing_domain`, `generated`, `loaded`, `deck_updated/reference_set_selected`, and `run_consumed` separately. Also separate `computed_trim`, `ground_issued_reference`, `commanded_trim`, `preburn_checkout_observed_delta`, `checkout_acceptance`, `powered_flight_compliance`, `postburn_actuator_state`, and `no_action_disposition`. The `~0.3°` evidence may populate the checkout layer for this maneuver only; the later `5.85 / 6.74` may populate a ground-issued reference plus `okay as it is` disposition. Neither populates a generic trim-calculation tolerance.