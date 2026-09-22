# Progress — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## Completed

Audited unresolved LM-5 descent inputs against primary Apollo documentation while preserving design/planned/as-flown/reconstructed/model distinctions.

### PDI mass boundary

The Apollo 11 Mission Report Appendix A.6/table A-I documents **33,683.5 lb at separation**, **33,669.6 lb at DOI ignition**, **33,401.6 lb at DOI cutoff**, and **16,153.2 lb at landing**. It contains no PDI row. Exact PDI mass remains unresolved.

### Propulsion/control boundary

The Apollo 11 Press Kit gives **9,870 lbf maximum rated thrust**; the Mission Report documents LM-5 advancing to FTP about 26 seconds after PDI. LMA790-3-LM page 2.2-215, **Change Date 15 June 1969**, directly establishes the **92.5% THRUST** TTCA hard stop in the LM-5 handbook state. This does not establish an LM-5 engine-specific force calibration at that control point.

### DPS performance page target recovered

The September 1969 LM-6-and-subsequent Volume-I contents/illustration material identifies the exact missing performance section as **§2.3.5, Descent Propulsion Section Performance and Design Data**, beginning at **page 2.3-25**, and identifies **Table 2.3-1, Descent Propulsion Section — Performance and Design Data** at that location.

A follow-on recovery pass reached the September 1969 scan's **List of Effective Pages**. That primary-document LEP confirms that the main-propulsion pages are individually revision-controlled across Original / 15 March / 15 June / 15 September 1969 states. However, the available indexed rendering is sufficiently OCR-corrupted around the 2.3 page ranges that the issue assigned specifically to **2.3-25** cannot be read defensibly. Searches for the table's likely performance terms likewise do not expose the table body in that rendering.

This is an evidence boundary, not permission to infer the missing footer. The later LM-10 handbook shows page 2.3-25 at a later effective state and is retained only as a locator/cross-check. No thrust, Isp, or LM-5 applicability is asserted from it.

Accordingly, **page 2.3-25 is now BLOCKED ON LEGIBLE PAGE-IMAGE / LEP RECOVERY**. A usable image of the September 1969 page itself, or a clean LEP transcription from the same primary issue, is required before the table can be configuration-qualified.

### Supplement 7

Apollo 11 Mission Report Supplement 7, *Descent Propulsion System Final Flight Evaluation*, remains **BLOCKED ON NAMED SOURCE RECOVERY**; no performance values are inferred from neighboring mission supplements.

## Boundary preserved

No later-LM force calibration was back-projected onto Eagle. No preflight/design thrust was promoted to delivered thrust. PDI mass remains unresolved.

## Repository updates

- `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/station-status/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `resources/APOLLO11_DESCENT_DYNAMICS_INPUT_SOURCE_CATALOG_ADDENDUM.md`

## Next

With page 2.3-25 blocked on a legible primary page image, shift the active propulsion search to **Apollo 11 DPS Supplement 7** and LM-5 engine acceptance/performance records while retaining 2.3-25 as a named recovery target. Continue Mission-G PDI-mass recovery only from explicitly event-identified primary records.

## Evidence status

**PARTIALLY DOCUMENTED.** Exact handbook location and revision-control context are established, but page 2.3-25's own effective state and values remain blocked on legible primary-page recovery. Exact LM-5 FTP force calibration, delivered thrust/Isp, and PDI mass remain unresolved. Apollo 11 DPS Supplement 7 and TRW BET Volume II remain **BLOCKED ON NAMED SOURCE RECOVERY**.