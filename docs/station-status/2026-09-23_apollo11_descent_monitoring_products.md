# Station-status addendum — Apollo 11 descent monitoring products

Date: 2026-09-23
Parent: `docs/STATION_RESEARCH_STATUS.md`

The Apollo 13 station maturity table remains unchanged. This addendum applies only to the D-024 Apollo 11 powered-descent architecture reference.

## Source-backed boundary

NASA/MSC 70-FM-20 preserves Apollo 11 descent monitoring comparisons explicitly labeled `AGS−PGNCS` and `MSFN−PGNCS`, with in-plane/crossrange monitoring context and descent-event markers.

The mission-specific AC Electronics Apollo 11 manual defines `MSK-1137` ground-display fields directly relevant to powered descent/program alarms: `TIG`, `TGO`, significant-event timing, descent-only time-to-end-of-phase, LGC/ISS warning status, PGNCS/program caution status, first/second/most-recent alarm code, restart count, computer program, and DSKY verb/noun/flasher/rows.

NASA's Apollo 11 air-to-ground transcript independently establishes the crew-interface call path for the first 1202: Eagle reports the alarm/code and asks Houston for a reading; `CC`/CAPCOM returns the ground GO disposition.

## Station consequence

GUIDO/FLIGHT-facing architecture may treat independent guidance/tracking disagreement and alarm/restart/program context as historically grounded Apollo 11 controller-product families. Crew-facing alarm disposition should be CAPCOM-mediated; an internal controller should not speak directly to Eagle merely because that station has access to an alarm product.

No station maturity is promoted. The sources do not establish exact live request procedure, DRK mapping, routing, cadence, or which internal controller/support-room position generated the alarm recommendation. MSK-1137 semantics must not be converted into unsupported ownership or timing claims.

## Recovery target

PHO-TN401 is located in the **Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, Box 078-65/66**. Direct inspection remains required for usable Mission-G routing/configuration evidence. Internal voice-loop ownership may require an additional controller-loop source if PHO-TN401 does not cover it.

## Next station research target

Recover PHO-TN401 or equivalent Apollo-11-effective configuration/loop evidence and map the demonstrated comparison/MSK-1137 products to exact station requests, routing, DRK mapping, cadence, and internal alarm-assessment ownership.

## Evidence status

- **DOCUMENTED / SUFFICIENT:** Apollo-11-specific MSK-1137 alarm/program/descent field semantics.
- **DOCUMENTED / SUFFICIENT:** crew-interface alarm disposition is CAPCOM-mediated.
- **DOCUMENTED:** mission-specific independent-source descent comparison products.
- **UNRESOLVED:** exact live station request/routing/DRK mapping/cadence and internal assessment ownership.
- **BLOCKED ON DOCUMENT RECOVERY:** direct PHO-TN401 inspection.
- **UNCHANGED:** Apollo 13 station maturity.