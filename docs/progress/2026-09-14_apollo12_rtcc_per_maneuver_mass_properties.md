# Progress — RTCC per-maneuver mass-properties workflow

Date: 2026-09-14
Research note: `resources/research/150_apollo12_rtcc_mass_properties_per_maneuver_boundary.md`

## Completed

- Continued from research note 149's unresolved RTCC/RTACF operational lineage.
- Reviewed the primary Apollo 12 Flight Control Division postflight RETRO report.
- Established that Apollo 12 mass properties were computed by **RTCC controllers in an offline computer in lieu of RTACF**.
- Established that **mass properties were run prior to each maneuver** and that computed SPS trims agreed within 0.1 degree with onboard postburn values for CSM-alone and docked configurations.
- Preserved the mission boundary: this is strong immediately-preceding-mission architecture evidence, not proof that H-2 used an identical program or cadence.
- Added research note 150 and reconciled the PC+2 numerical roadmap, station-status documentation, and RTCC mass-properties source catalog.

## Result

The simulator can now distinguish a persistent mass-properties state/deck from a **controller-initiated calculation run** that produces maneuver-support products. This is a better operational abstraction for the documented Apollo 13 stale-versus-current PC+2 trim disagreement than treating trim as a fixed field.

## Next

Find H-2 RTCC controller procedures, run sheets/listings, Flight Dynamics worksheets, or processor documentation explicitly tying a pre-PC+2 calculation run to `T+55`, the accepted DPS trim, or the `62,480 / 33,452 lb` P30 module weights.