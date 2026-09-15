# Station-status addendum — H-2 mass-properties job-number provenance

Date: 2026-09-15  
Parent: `docs/STATION_RESEARCH_STATUS.md`

Historical station maturity grades are unchanged. Research note 151 strengthens a Flight Dynamics/RTCC workflow boundary rather than reconstructing a console display.

## FIDO / RETRO

**Evidence strengthened.** The Apollo 13 Flight Control Division Mission Operations Report explicitly identifies late entry aerodynamics loaded into RTCC as being based on **mass properties job 27**. This proves that H-2 Flight Dynamics could refer to a mass-properties calculation by numbered job identity and preserve that provenance into a downstream operational product.

For simulation, FIDO/RETRO products may therefore carry a sourced mass-properties job identifier when one is historically known. PC+2's identifier remains unknown.

## FLIGHT

No maturity change. The finding improves provenance behind Flight Dynamics products but does not establish what job-number metadata, if any, was visible to FLIGHT.

## CONTROL

No maturity change. The finding does not identify the mass-properties job behind the ~59-hour DPS-trim disagreement. CONTROL's documented use of stale premission mass properties versus Flight Dynamics' better data remains the controlling PC+2 evidence.

## RTCC/support boundary

Represent mass-properties **job identity** separately from `T+N` deck/reference epoch, generation time, input provenance, and derived products. Do not assign job 27 to PC+2: the source explicitly places that job in the later entry-aerodynamics workflow around GET 122 hours.

## Remaining PC+2 gap

Recover an H-2 numbered mass-properties job/run record near GET 55–59 hours that explicitly links its basis to `T+55` and its outputs to the accepted DPS trim and/or final P30 module weights.