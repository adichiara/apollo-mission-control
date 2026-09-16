# Research note 170 — 59-hour PC+2 trim provenance

Date: 2026-09-15

## Question

Can the `5.86° / 6.75°` pair passed at about 59 GET be classified more precisely than an unexplained/interim crew value, and does the primary record identify whose mass-properties solution it represented?

## Primary-source synthesis

Yes. Two primary records can be joined without inventing a missing calculation.

The Apollo 13 air-to-ground record at about 59:03 GET identifies the values passed to the crew as DPS trim/GDA angles for PC+2. The crew reads back:

- pitch `5.86°`;
- roll `6.75°`.

The Flight Dynamics section of the NASA/MSC Flight Control Division *Mission Operations Report — Apollo 13* (MSC-02680, 28 April 1970) independently describes the PC+2 abort pad passed at approximately 59:00 GET. It states that the **DPS trim passed to the crew on that pad** was challenged by LM CONTROL, that CONTROL later agreed with Flight Dynamics' data, and that CONTROL had used **premission mass properties**, which the report says were not the best data available.

Because the time, maneuver, pad, and passed DPS-trim event coincide, the `5.86 / 6.75` pair can now be classified as the **Flight Dynamics PC+2 abort-pad trim solution passed at ~59 GET**, rather than merely an unexplained interim pair.

Primary sources:

- NASA Apollo 13 air-to-ground/mission voice record, approximately GET 59:03–59:05: CAPCOM identifies the values as DPS trim; crew reads back pitch `5.86`, roll `6.75`.
- NASA/MSC Flight Control Division, *Mission Operations Report — Apollo 13*, MSC-02680, 28 April 1970, Flight Dynamics chronology: ~59:00 PC+2 abort pad, LM CONTROL challenge, later agreement, and CONTROL's premission-mass-properties basis.

## What this resolves

The provenance chain at ~59 GET is now stronger:

`Flight Dynamics PC+2 abort-pad solution -> DPS trim passed to crew = 5.86 / 6.75 -> LM CONTROL challenges using premission mass properties -> CONTROL later agrees with Flight Dynamics data`.

This establishes that the disagreement was not simply a verbal uncertainty about what the numbers meant. It was a mass-properties-dependent controller disagreement over the PC+2 DPS trim solution.

It also identifies the known losing basis: **LM CONTROL's challenged calculation used premission mass properties**.

## T+55 relationship

The same Flight Dynamics chronology separately states that RTCC LM-burn mass-property decks had been updated to **T+55 decks** before the accident sequence. That makes the T+55 family the documented improved RTCC LM-burn mass-property context available to Flight Dynamics.

However, the report does **not** explicitly say that the specific calculation producing `5.86 / 6.75` was run from a named T+55 deck, nor does it provide a job/run identifier or printed mass-property inputs. Therefore the direct calculation-level link remains unresolved.

Do not rewrite the evidence as:

`T+55 deck -> 5.86 / 6.75`

until a working artifact or explicit primary statement supplies that link.

## Relationship to the later 5.85 / 6.74 readback

The post-61:29 revised PC+2 pad says the GDA should remain "okay as is" and associates that retained reference with `5.85 / 6.74` (crew readback qualified by "hopefully").

The new provenance for `5.86 / 6.75` does not establish that the later `5.85 / 6.74` pair is a recomputation, a rounded update, a telemetry observation, or evidence of a `0.01°` acceptance threshold. Those remain unsupported interpretations.

## Remaining unresolved comparison

This pass recovers a historically identified **candidate/passed solution at ~59 GET**, but not the complete comparison artifact. Still missing:

- LM CONTROL's alternative numerical trim from its premission mass-properties calculation;
- the numerical delta between CONTROL's challenged result and Flight Dynamics' `5.86 / 6.75` solution;
- the criterion used when CONTROL accepted Flight Dynamics' data;
- RTCC/RTACF job/run identity and calculation time;
- direct proof that the `5.86 / 6.75` run used the T+55 deck family;
- whether/how the later `5.85 / 6.74` retained-reference readback was generated from the post-61:29 state.

## Simulator implication

`5.86 / 6.75` may now be represented as a source-backed **Flight Dynamics PC+2 abort-pad trim solution passed at ~59 GET**, with a documented competing LM CONTROL calculation based on inferior premission mass properties. The competing numerical values and acceptance rule must remain unknown. Do not treat the pair as measured actuator state or as the final post-61:29 PC+2 state.

## Next archival target

Prioritize the LM CONTROL/Flight Dynamics working artifact for the ~59 GET disagreement: recover CONTROL's alternative values, the comparison/acceptance basis, and the RTCC job/deck provenance. That artifact is now more useful than searching generically for a final Noun 48 pair.