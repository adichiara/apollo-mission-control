# Research note 152 — Apollo 13 PC+2 interim DPS-trim update boundary

Date: 2026-09-15

## Question

Can the ~59-hour PC+2 trim dispute be narrowed to a concrete controller-to-crew product, and does the surviving record distinguish an interim trim from the later final PC+2 solution?

## Primary source first

NASA Manned Spacecraft Center, Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970.

NASA/Apollo Journal scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf

The Flight Dynamics/RETRO chronology states that at approximately GET 59 hours a PC+2 block-data pad was uplinked for a DPS maneuver at 79:30 GET. The DPS trim passed on that abort pad was challenged by LM Control; Flight Dynamics reports that LM Control had used premission mass properties, which were not the best data available, and later agreed with Flight Dynamics' data. The same chronology had already recorded that RTCC LM-burn mass-property decks were updated to `T+55` decks.

This remains the controlling mission-specific primary evidence for provenance and reconciliation. It still does not explicitly name the Flight Dynamics mass-properties job or say that the accepted basis was the `T+55` deck.

## Mission-audio transcript corroboration

The Apollo 13 Flight Journal / Apollo 13 Real-time transcript preserves the air-ground exchange beginning at GET 59:01:39. CAPCOM reads a P30 pad for a PC+2 DPS abort and at 59:03:19 gives two gimbal trim angles, explicitly saying they **will be updated**. The values read are:

- pitch GDA: `5.86°`
- second GDA value: `6.75°` (Haise's accepted readback identifies this axis as roll)

The crew confirms these as DPS gimbal angles/GDAs in the readback. Research note 153 later corrects the axis label: the exchange is inconsistent, but Haise's accepted readback and LM CONTROL evidence support treating the second value as roll rather than normalizing it to yaw.

Transcript presentation: https://apollo13realtime.org/ (GET 059:01–059:05)

The transcript is an edited restoration/transcription of mission audio rather than the Flight Control Division's own written report, so it is used here to identify the controller-to-crew product and values, not to override the primary report's provenance statements.

## Finding

The ~59-hour event is now bounded more tightly:

`mass-properties basis -> Flight Dynamics trim calculation/product -> P30/block-data communication -> crew GDA values`

At GET ~59:03 the crew had a concrete PC+2 trim pair (`5.86°`, `6.75°`), but CAPCOM explicitly marked it as **subject to later update**. Therefore these values must not be treated as the final PC+2 trim merely because they are the first recovered numerical values associated with the documented mass-properties dispute.

This is operationally important: a maneuver product can be valid enough to communicate while still carrying an expected-update state. Product provenance and product finality are separate dimensions.

## Relationship to the later final pad

The Flight Dynamics report states separately that the **final PC+2 pad went to the crew at 78 hours**, based on the GYM 289 vector, for TIG `79:27:38.30`.

Research note 137 documents the later final P30 module weights (`62480 lb` CSM / `33452 lb` LM). Nothing recovered here proves that the 59-hour `5.86° / 6.75°` trim pair survived unchanged into that final pad.

## Boundary retained

Do not infer:

- that `5.86° / 6.75°` were the final PC+2 trim angles;
- that these values came specifically from the `T+55` deck;
- a mass-properties job number for the ~59-hour calculation;
- that the same calculation produced the later `62480 / 33452 lb` module weights;
- that the final GYM 289 targeting solution retained the same trim;
- exact RTCC/RTACF processor inputs, execution venue, table layout, or software version.

## Simulation implication

A maneuver/trim product should support explicit lifecycle state and provenance, for example:

- `draft/interim` versus `final`;
- `expected_update: true/false`;
- source mass-properties basis/version;
- optional job number when sourced;
- communicated-to-crew timestamp;
- superseded-by relationship.

For the recovered ~59-hour product, `expected_update = true` is historically supported. The final trim remains unresolved.

## Next archival target

Search the Apollo 13 Flight Director Log and H-2 Flight Dynamics/RETRO working records from GET 55–59 and 77–78 hours for the mass-properties job/run behind the interim `5.86° / 6.75°` pair and for any later replacement trim. Highest-value evidence would explicitly connect a numbered job or `T+55` basis to either trim pair and/or to the final `62480 / 33452 lb` P30 module weights.