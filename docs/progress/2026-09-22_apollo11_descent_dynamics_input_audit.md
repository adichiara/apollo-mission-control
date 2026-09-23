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

The September 1969 scan's primary List of Effective Pages confirms individual revision control, but its indexed rendering is too OCR-corrupted around the 2.3 page ranges to read page 2.3-25's issue defensibly. Accordingly, **page 2.3-25 is BLOCKED ON LEGIBLE PAGE-IMAGE / LEP RECOVERY**.

### Supplement 7 archival pass

A bounded recovery pass searched the current NASA/NTRS public catalog and Apollo mission-report indexes for **Apollo 11 Mission Report Supplement 7, _Descent Propulsion System Final Flight Evaluation_**. No public Apollo 11 Supplement 7 catalog record was recovered. Later NASA mission-report supplement tables remain positive primary evidence for its **September 1970** publication.

The identifier-focused follow-up tested the report-number path rather than repeating the title search. NTRS metadata for Apollo 11 Supplement 5 shows that an Apollo 11 sibling can be cataloged under parent report **MSC-00171** plus separate supplement/TM identifiers. NTRS metadata for Apollo 12 DPS Supplement 5 explicitly carries **MSC-01855-SUPPL-5**, **TRW-11176-H585-R0-00-SUPPL-5**, **NASA-TM-X-68933**, accession **73N15812**, and contract **NAS9-8166**.

This establishes relevant identifier families but not Apollo 11 Supplement 7's identifiers. In particular, **`MSC-00171-SUPPL-7` is not accepted as historical metadata merely because it is a plausible later-mission pattern**. Targeted searches using that string and title/LM-5/TRW combinations did not recover authoritative Apollo 11 metadata.

The next discriminating retrieval is therefore an MSC/NASA September-1970 bibliographic index, TRW Systems Group propulsion-report index, or archival crosswalk that exposes the Apollo 11 report's actual MSC/TRW/NASA-TM/accession identifiers.

No performance value was imported from neighboring-mission DPS reports.

## Boundary preserved

No later-LM force calibration was back-projected onto Eagle. No preflight/design thrust was promoted to delivered thrust. No pattern-derived report number was promoted to sourced metadata. PDI mass remains unresolved.

## Repository updates

- `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/station-status/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `resources/APOLLO11_DESCENT_DYNAMICS_INPUT_SOURCE_CATALOG_ADDENDUM.md`

## Next

Pursue the Apollo 11 DPS Supplement 7 **identifier crosswalk** through MSC/NASA September-1970 bibliographic records or TRW Systems Group propulsion-report indexes. In parallel, search LM-5 engine acceptance/performance records for an explicit FTP force mapping or delivered thrust/Isp. Retain page 2.3-25 as a named image-recovery target and continue PDI-mass recovery only from explicitly event-identified primary records.

## Evidence status

**PARTIALLY DOCUMENTED.** Supplement 7 existence/title/date are documented; its actual report identifiers and content remain **BLOCKED ON BIBLIOGRAPHIC / ARCHIVAL RECOVERY**. Page 2.3-25 remains blocked on legible primary-page recovery. Exact LM-5 FTP force calibration, delivered thrust/Isp, and PDI mass remain unresolved. TRW BET Volume II remains **BLOCKED ON NAMED SOURCE RECOVERY**.