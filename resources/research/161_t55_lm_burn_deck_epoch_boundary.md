# Research note 161 — Apollo 13 T+55 LM-burn deck epoch boundary

Date: 2026-09-15

## Question

Can the documented `T+55` LM-burn mass-property decks be tied more tightly to the PC+2 trim decision without inventing a calculation run or job number?

## Primary evidence

### Flight Control Division Mission Operations Report — Apollo 13

The Flight Dynamics/RETRO chronology for MCC-2 through PC+2 explicitly states:

- `RTCC (LM burn) mass property decks were updated to T+55 decks.`

The same mission-specific report later records that the ~59-hour PC+2 abort-pad DPS trim was challenged by LM CONTROL, that CONTROL had used **premission mass properties**, and that CONTROL later agreed with Flight Dynamics because the premission set was not the best data available.

Source: NASA Manned Spacecraft Center, MSC-02680, *Flight Control Division Mission Operations Report — Apollo 13*, 28 April 1970, Flight Dynamics/RETRO appendix.

Accessible scan: https://faculty.tamuc.edu/cdavis/resources/apollo_press/Apollo%2013%20Mission%20Operations%20Report.pdf

## Finding

This strengthens the provenance chain but does **not** close it:

`T+55 LM-burn deck family exists in RTCC -> premission CONTROL data are explicitly inferior during the PC+2 trim dispute -> CONTROL later accepts Flight Dynamics data`.

The report does not identify a numbered job for the PC+2 calculation, does not print the T+55 deck contents, and does not explicitly say that a particular `5.86° / 6.75°` trim pair was the direct output of a named T+55 run.

The wording also reinforces an important modeling distinction: **`T+55` is a deck/reference-state label, not a recovered calculation timestamp or job identity**. A deck may be selected by epoch while the calculation using it occurs later.

## Historical boundary

Do not convert the evidence into any of the following unsupported claims:

- `T+55` means the calculation was executed exactly at GET 55:00;
- a specific numbered mass-properties job generated the PC+2 or free-return trim;
- the T+55 decks contained the final P30 Noun 47 values `62480 / 33452 lb`;
- the retained PC+2 gimbal state was numerically equal to the earlier `5.86° / 6.75°` pair;
- the T+25 `0.01°` comparison criterion applied to PC+2.

## Simulation implication

Represent RTCC mass-property provenance with separate fields for at least:

`deck_family`, `reference_epoch`, `calculation_time`, `job_number`, `input_mass_cg_state`, `candidate_trim`, `comparison_reference`, `comparison_delta`, `decision`.

For Apollo 13 PC+2, `deck_family/reference_epoch = LM-burn T+55` is historically supported at the family level. The specific calculation time, job number, candidate trim, and comparison delta remain unknown.

## Next archival target

Search H-2/Flight Dynamics working records for a PC+2 calculation artifact that explicitly joins the already-supported T+55 deck family to a candidate trim and comparison/no-update decision. If that artifact cannot be recovered, retain the provenance gap rather than filling it from the later P30 weights or postflight mass reconstruction.