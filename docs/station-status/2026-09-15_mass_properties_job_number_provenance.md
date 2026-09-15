# Station-status addendum — H-2 mass-properties job-number provenance

Date: 2026-09-15  
Parent: `docs/STATION_RESEARCH_STATUS.md`

Historical station maturity grades are unchanged. Research notes 151–152 strengthen the Flight Dynamics/RTCC workflow boundary rather than reconstructing a console display.

## FIDO / RETRO

**Evidence strengthened.** The Apollo 13 Flight Control Division Mission Operations Report identifies late entry aerodynamics loaded into RTCC as based on **mass properties job 27**. This proves that H-2 Flight Dynamics could refer to a mass-properties calculation by numbered job identity and preserve that provenance into a downstream operational product.

Research note 152 further narrows the earlier PC+2 workflow: the restored mission-audio transcript records a ~59-hour P30/block-data communication containing DPS gimbal trim values `5.86°` pitch and `6.75°` yaw, explicitly flagged as values that **will be updated**. The Flight Dynamics report independently identifies the ~59-hour trim as the product challenged by LM Control after use of inferior premission mass properties.

For simulation, FIDO/RETRO products may therefore carry a sourced mass-properties job identifier when one is historically known and a separate lifecycle/finality state. PC+2's job identifier and final trim remain unknown.

## FLIGHT

No maturity change. The finding improves provenance behind Flight Dynamics products and establishes that an interim crew-facing trim could be communicated before finalization, but it does not establish what job-number metadata or calculation details were visible to FLIGHT.

## CONTROL

No maturity change. CONTROL's documented use of stale premission mass properties versus Flight Dynamics' better data remains the controlling PC+2 evidence. The recovered `5.86° / 6.75°` values identify the interim crew-facing trim product associated with this period, but CAPCOM explicitly marked them for later update; they must not be represented as the final PC+2 trim.

## CAPCOM / crew interface

**Workflow evidence strengthened; maturity unchanged.** At GET ~59:03 CAPCOM read the DPS gimbal trim values to the crew as part of the PC+2 P30/block-data sequence and explicitly announced that the angles would be updated. This is evidence for communicating a usable-but-not-final maneuver product and for preserving update state across the Flight Dynamics -> CAPCOM -> crew path.

## RTCC/support boundary

Represent mass-properties **job identity** separately from `T+N` deck/reference epoch, generation time, input provenance, derived products, and product lifecycle/finality. Do not assign job 27 to PC+2: the source places that job in the later entry-aerodynamics workflow around GET 122 hours. Do not assign the interim `5.86° / 6.75°` pair specifically to `T+55` until a direct H-2 record establishes that link.

## Remaining PC+2 gap

Recover Apollo 13 Flight Director Log pages and H-2 mass-properties/Flight Dynamics working records near GET 55–59 and 77–78 hours that identify the numbered job/run behind the interim trim and any later replacement trim, ideally linking the accepted basis to `T+55`, the final GYM 289/P30 product, and/or the `62480 / 33452 lb` module weights.