# Station-status addendum — Apollo 11 descent monitoring products

Date: 2026-09-23
Parent: `docs/STATION_RESEARCH_STATUS.md`

The Apollo 13 station maturity table remains unchanged. This addendum applies only to the D-024 Apollo 11 powered-descent architecture reference.

## Source-backed boundary

NASA/MSC 70-FM-20 preserves Apollo 11 descent monitoring comparisons explicitly labeled `AGS−PGNCS` and `MSFN−PGNCS`, with in-plane/crossrange monitoring context and descent-event markers.

The mission-specific AC Electronics Apollo 11 manual additionally defines `MSK-1137` ground-display fields directly relevant to the powered-descent/program-alarm interval: `TIG`, `TGO`, last/next significant-event time, descent-only time-to-end-of-phase, LGC/ISS warning status, PGNCS/program caution status, first/second/most-recent alarm code, restart count, computer program, and DSKY verb/noun/flasher/rows.

## Station consequence

GUIDO/FLIGHT-facing architecture may treat independent guidance/tracking disagreement and alarm/restart/program context as historically grounded Apollo 11 controller-product families. A modern synthetic alarm panel is not required for this reference.

No station maturity is promoted. The sources do not establish exact live request procedure, DRK mapping, routing, cadence, or definitive station ownership of every field. MSK-1137 semantics must not be converted into unsupported ownership or timing claims.

## Recovery target

PHO-TN401 is located in the **Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, Box 078-65/66**. Direct inspection remains required for any usable Mission-G routing/configuration evidence.

## Next station research target

Recover PHO-TN401 or equivalent Apollo-11-effective configuration evidence and map the demonstrated comparison/MSK-1137 products to exact station requests, routing, DRK mapping, cadence, and call ownership.

## Evidence status

- **DOCUMENTED / SUFFICIENT:** Apollo-11-specific MSK-1137 alarm/program/descent field semantics for current product architecture.
- **DOCUMENTED:** mission-specific independent-source descent comparison products.
- **UNRESOLVED:** exact live station request/routing/DRK mapping/cadence and call ownership.
- **BLOCKED ON DOCUMENT RECOVERY:** direct PHO-TN401 inspection.
- **UNCHANGED:** Apollo 13 station maturity.