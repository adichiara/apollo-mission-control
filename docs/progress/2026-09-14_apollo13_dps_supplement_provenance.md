# Progress — Apollo 13 DPS Supplement 2 provenance and RTCC mass-properties semantics

Date: 2026-09-14

## Completed

- Continued from research notes 138–141.
- Re-ran exact-title and report-key searches for Apollo 13 Mission Report Supplement 2, *Descent Propulsion System Final Flight Evaluation*; no direct public Apollo 13 Supplement 2 scan or authoritative catalog record was recovered.
- Retained the primary-supported TRW Systems Group / MSC / `NAS9-8166` provenance tuple from adjacent Apollo DPS final-flight evaluations without importing adjacent-mission numerical values.
- Investigated the parallel unresolved RTCC `T+55` mass-property-deck question using Apollo-era operational support documentation.
- Established that Apollo mass-properties products fed trajectory, trim, DAP/control, and propellant-support computations and were updated as propellant state and vehicle configuration changed.
- Combined that operational context with the Apollo 13 Flight Control Division statement that LM-burn mass-property decks were updated to `T+55` decks and that premission mass properties produced a disputed PC+2 DPS trim.
- Added research note 142 and updated the numerical-validation roadmap, station-status record, and source catalog.

## Consequence

The project can now model the PC+2 mass-property source as an **in-flight updated operational state product** rather than a fixed preflight constant. The documented P30 CSM/LM weights remain targeting references, not proven exact physical ignition masses.

No source reviewed in this pass defines the exact H-2 `T+55` label, deck record layout, field meanings, processor mapping, or derivation of the final P30 weight pair. Those remain explicit archival gaps.

No new historical LM-7 thrust, mass-flow, mixture-ratio, or specific-impulse constants are frozen by this pass.

## Next

Prioritize mission-specific Apollo 13/H-2 RTCC or Flight Dynamics mass-properties requirements, deck definitions/listings, or ACF/RTCC documentation that explicitly defines `T+55` and LM-burn deck fields. Continue the Apollo 13 DPS Supplement 2 retrieval in parallel using the established provenance tuple.