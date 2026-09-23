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

Accordingly, **page 2.3-25 is BLOCKED ON LEGIBLE PAGE-IMAGE / LEP RECOVERY**.

### Supplement 7 archival pass

A bounded recovery pass searched the current NASA/NTRS public catalog and Apollo mission-report indexes for **Apollo 11 Mission Report Supplement 7, _Descent Propulsion System Final Flight Evaluation_**. The catalog exposes neighboring DPS final-flight evaluations for Apollo 9, Apollo 10, Apollo 12, Apollo 15, and Apollo 16, but no public Apollo 11 Supplement 7 record was recovered. The Virtual AGC mission-document index likewise exposes Apollo 11 Supplement 5 but not Supplement 7.

This is **negative catalog evidence only**, not evidence that Supplement 7 did not exist. The previously recovered later NASA mission-report supplement tables remain the positive primary evidence for its title and September 1970 publication. The useful result is procedural: repeated broad public-catalog searching is no longer the next discriminating step. Recovery now requires a report identifier/accession trail from MSC/NASA bibliographic records, archival holdings, or a contemporaneous citation.

No performance value was imported from neighboring-mission DPS reports. Apollo 16's NTRS record confirms that this report family can contain FTP thrust/Isp and comparison with engine acceptance-test values, which strengthens Supplement 7's relevance but does not establish any LM-5 number.

## Boundary preserved

No later-LM force calibration was back-projected onto Eagle. No preflight/design thrust was promoted to delivered thrust. PDI mass remains unresolved.

## Repository updates

- `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/station-status/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `resources/APOLLO11_DESCENT_DYNAMICS_INPUT_SOURCE_CATALOG_ADDENDUM.md`

## Next

For Supplement 7, stop repeating generic NTRS title searches and pursue its **report number/accession/citation trail** through MSC/NASA bibliographic or archival records. In parallel, search LM-5 engine acceptance/performance records for an explicit FTP force mapping or delivered thrust/Isp. Retain page 2.3-25 as a named image-recovery target and continue PDI-mass recovery only from explicitly event-identified primary records.

## Evidence status

**PARTIALLY DOCUMENTED.** Exact handbook location and revision-control context are established, but page 2.3-25's own effective state and values remain blocked on legible primary-page recovery. Supplement 7 existence/publication is documented, while its public catalog record/content remains **BLOCKED ON REPORT-IDENTIFIER / ARCHIVAL RECOVERY**. Exact LM-5 FTP force calibration, delivered thrust/Isp, and PDI mass remain unresolved. TRW BET Volume II remains **BLOCKED ON NAMED SOURCE RECOVERY**.