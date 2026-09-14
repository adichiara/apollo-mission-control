# Research note 146 — Apollo 13 PC+2 mass-properties cross-console reconciliation

Date: 2026-09-14

## Question

What does the Apollo 13 Flight Control Division Mission Operations Report establish about how updated mass-properties data were actually used and challenged during early PC+2 planning?

## Primary source

NASA Manned Spacecraft Center, Flight Control Division, *Mission Operations Report — Apollo 13*, April 28, 1970.

NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf

Relevant Flight Dynamics / RETRO narrative, Appendix B:

- before the accident, RTCC LM-burn mass-property decks were updated to `T+55` decks;
- at approximately 59 hours GET, a PC+2 block-data pad was uplinked for a DPS maneuver at 79:30 GET;
- the DPS trim passed with that PC+2 abort pad was challenged by LM Control;
- the Flight Dynamics/RETRO narrative says LM Control had used **premission mass properties**, then later agreed with the Flight Dynamics data because the premission set was **not the best data available**.

## Finding

This closes an important operational boundary. Apollo 13 mass properties were not merely archival or background inputs: controllers could compare maneuver-support products generated from different mass-property bases, detect a disagreement, and reconcile the result across stations. By roughly 59 hours GET, use of a premission mass-properties basis for the PC+2 DPS trim was explicitly treated as inferior to better in-flight data then available.

For the simulation architecture this supports a distinction between:

1. the current Flight Dynamics/RTCC mass-properties state;
2. an older or stale premission mass-properties state;
3. derived controller-facing products such as DPS trim and block-data pads; and
4. cross-console challenge/reconciliation when different stations are working from different state bases.

A historically plausible station model may therefore allow a stale mass-properties basis to create a disagreement in a derived product without implying that the underlying physical spacecraft state changed.

## Critical boundary

The report does **not** explicitly say that the particular Flight Dynamics data which won the ~59-hour trim dispute were the `T+55` decks. The chronology makes that possible — the report records the `T+55` LM-burn deck update shortly before the accident and later says the premission basis was not the best available — but the source does not make the direct identification.

Therefore:

- do not write `T+55 caused/corrected the LM Control trim discrepancy` as established fact;
- do not infer the numerical trim difference from the text;
- do not infer which console, processor, or worksheet physically carried the competing mass-property values;
- do not equate the better Flight Dynamics basis with exact physical ignition mass.

The safe statement is narrower: **updated in-flight mass-properties information existed, premission mass properties were later rejected as the best available basis for a PC+2 DPS trim product, and the resulting disagreement was reconciled operationally across Flight Dynamics and LM Control.**

## Simulation implication

Represent mass-properties provenance on maneuver-support calculations. At minimum, a derived trim/targeting product should retain a source-state identifier such as `premission` versus `current operational state`, so disagreement can be traced to state provenance rather than represented as arbitrary controller error.

Do not assign actual H-2 deck field names or values until recovered from mission-specific RTCC documentation.

## Next unresolved item

The highest-value remaining archival target is still an H-2 RTCC/Flight Dynamics definition of the precise `T+N` reference-epoch convention and LM-burn deck fields. A particularly valuable source would explicitly link the ~59-hour PC+2 trim calculation to the `T+55` deck or identify which mass-properties job/deck supplied the accepted trim.