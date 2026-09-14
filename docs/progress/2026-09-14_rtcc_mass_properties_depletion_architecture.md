# Progress — RTCC mass-properties depletion-table architecture

Date: 2026-09-14

## Completed

- Continued from research note 143 and the unresolved Apollo 13/H-2 `T+55` mass-properties epoch/deck question.
- Located and inspected NASA MSC Internal Note 71-FM-214, *Skylab RTCC Mass Properties System Requirements* (June 14, 1971; MSC-04378 / NASA-TM-X-67442).
- Verified the note's explicit statement that the Skylab system was intended as a carryover of the then-current Apollo RTCC Mass Properties System.
- Documented the architecture's module summation, total weight/CG computation, temporary/permanent propellant depletion tables, and downstream engine-trim use.
- Added research note 144.
- Updated the PC+2 numerical-validation roadmap, FIDO/FLIGHT station-status addendum, and RTCC mass-properties source catalog.

## Consequence

The project can now represent Apollo-era RTCC mass properties as a structured operational state rather than a single scalar weight: module contributions and propellant-depletion state feed total weight/CG products that can in turn support trim/trajectory calculations.

This improves the simulation architecture but does not supply Apollo 13/H-2 values. The source does not establish that `T+55` was itself a depletion table, define the exact `T+N` epoch convention, or map the H-2 deck into the final PC+2 P30 weights.

## Next

Continue searching for mission-specific H-2 RTCC/Flight Dynamics requirements, mass-properties deck/listing definitions, processor descriptions, and maneuver-support worksheets that connect the generic Apollo RTCC architecture to the `T+55` LM-burn deck. Search explicitly for `temporary` / `permanent propellant depletion table` terminology alongside `H-2`, `Apollo 13`, `T+55`, `LM burn`, and `mass properties`.

Keep recovery of Apollo 13 Mission Report Supplement 2, *Descent Propulsion System Final Flight Evaluation*, as the parallel propulsion target.