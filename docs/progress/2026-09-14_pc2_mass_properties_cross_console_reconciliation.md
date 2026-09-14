# Progress — PC+2 mass-properties cross-console reconciliation

Date: 2026-09-14

## Work completed

- Continued from research note 145 and the unresolved H-2 `T+N`/LM-burn deck semantics.
- Re-examined the primary Apollo 13 Flight Control Division Mission Operations Report around the pre-accident `T+55` update and early PC+2 planning.
- Confirmed that at about 59 hours GET a PC+2 block-data pad carried a DPS trim challenged by LM Control.
- Confirmed the Flight Dynamics/RETRO account says LM Control had used **premission mass properties**, which were not the best data available, and later agreed with the Flight Dynamics data.
- Added research note 146 to formalize the cross-console provenance/reconciliation boundary.
- Updated the PC+2 numerical-validation roadmap, FIDO/CONTROL/FLIGHT station-status addendum, and RTCC mass-properties source catalog.

## Consequence

The simulator can now safely represent mass-properties provenance as operationally meaningful state: a stale premission basis may propagate into a derived maneuver product and trigger a controller challenge/reconciliation.

The source does **not** explicitly state that the accepted Flight Dynamics trim used the `T+55` deck. That connection remains open and must not be promoted from chronology to fact.

## Next target

Recover mission-specific H-2 RTCC/Flight Dynamics material that explicitly identifies the mass-properties job/deck used for the accepted ~59-hour PC+2 DPS trim, ideally also defining the precise `T+N` reference-epoch convention and LM-burn deck fields.