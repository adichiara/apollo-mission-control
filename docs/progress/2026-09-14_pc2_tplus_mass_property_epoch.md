# Progress — Apollo 13 T+N mass-property epoch semantics

Date: 2026-09-14

## Completed

- Revisited the unresolved `T+55` LM-burn mass-property deck label using the mission-specific Apollo 13 Flight Control Division Mission Operations Report.
- Identified the same Flight Dynamics narrative's earlier `T-6`, `T+6`, and `T+25` mass-properties references.
- Verified that a `T+25` RTCC mass-properties run was explicitly compared against `T+6` pitch/yaw trims and that no update was needed because the trims differed by no more than 0.01 degree.
- Combined that sequence with the later statement that LM-burn mass-property decks were updated to `T+55` before PC+2 abort-maneuver work.
- Added research note 143 and updated the numerical-validation roadmap, FIDO/FLIGHT station-status addendum, and RTCC mass-properties source catalog.

## Consequence

The project no longer needs to treat `T+55` as an opaque deck identifier. Mission-specific evidence supports a **mission-relative, time-tagged mass-properties interpretation associated with approximately +55 hours**.

The exact convention remains unresolved: the source does not state whether `T+55` is precisely a 55:00:00 GET state, a nominal calculation epoch, a deck-generation timestamp, or a propagated state referenced to that time.

The final PC+2 P30 CSM/LM weights therefore remain targeting references with a documented in-flight, time-tagged mass-properties lineage; they are still not proven exact physical ignition masses.

## Next

Prioritize H-2 RTCC/Flight Dynamics requirements, mass-property deck definitions/listings, or maneuver-support worksheets that define the precise `T+N` epoch convention and the `T+55` LM-burn deck fields. Continue the Apollo 13 DPS Supplement 2 retrieval in parallel.