# Station-status addendum — PC+2/free-return trim lifecycle

Date: 2026-09-15  
Parent: `docs/STATION_RESEARCH_STATUS.md`

Historical station maturity grades are unchanged. Research note 157 improves the cross-console/product-lifecycle model.

## CONTROL

The `5.86° / 6.75°` GDA pair should no longer be described only as a challenged or discarded ~59-hour PC+2 value. After the documented mass-properties disagreement was reconciled, the same pair was transmitted for the actual 61:29 free-return DPS burn. CONTROL therefore participates in a workflow where trim can be challenged, reconciled, accepted for execution, and later recomputed for a different maneuver.

## FIDO / RETRO / Flight Dynamics

The Flight Dynamics evidence now connects more strongly to an executed maneuver: T+55 LM-burn decks were available, Flight Dynamics defended its trim against CONTROL's premission-mass-properties result, and the reconciled `5.86° / 6.75°` pair was subsequently used for the free-return burn. A direct numbered-job/T+55 derivation remains unrecovered.

## FLIGHT

For simulation, FLIGHT should receive trim readiness/finality as maneuver-specific status rather than treating one GDA pair as globally current for all planned burns. The same pair could be GO for the near-term free-return burn while still explicitly update-required for later PC+2.

## Remaining station-research target

Recover H-2 CONTROL/Flight Dynamics working material between the free-return burn and PC+2 that records the later PC+2 GDA setpoint, calculation run/job, or mass-properties state used to generate it.