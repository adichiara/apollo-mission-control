# Progress — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## Completed

Audited unresolved LM-5 descent inputs against primary Apollo documentation while preserving design/planned/as-flown/reconstructed/model distinctions.

### PDI mass boundary

The Apollo 11 Mission Report Appendix A.6/table A-I documents **33,683.5 lb at separation**, **33,669.6 lb at DOI ignition**, **33,401.6 lb at DOI cutoff**, and **16,153.2 lb at landing**. It contains no PDI row. Exact PDI mass remains unresolved.

### Propulsion/control boundary

The Apollo 11 Press Kit gives **9,870 lbf maximum rated thrust**; the Mission Report documents LM-5 advancing to FTP about 26 seconds after PDI. LMA790-3-LM page 2.2-215, **Change Date 15 June 1969**, directly establishes the **92.5% THRUST** TTCA hard stop in the LM-5 handbook state. This does not establish an LM-5 engine-specific force calibration at that control point.

### DPS performance page target recovered

The September 1969 LM-6-and-subsequent Volume-I contents/illustration material identifies **§2.3.5**, beginning at **page 2.3-25**, and **Table 2.3-1, Descent Propulsion Section — Performance and Design Data**. The primary LEP rendering is too OCR-corrupted to assign page 2.3-25's issue date defensibly, so the page remains **BLOCKED ON LEGIBLE PAGE-IMAGE / LEP RECOVERY**.

### Supplement 7 archival pass

Apollo 11 Mission Report Supplement 7, _Descent Propulsion System Final Flight Evaluation_, is documented by later NASA supplement tables as published in **September 1970**, but its public catalog record/content remains unrecovered. Apollo 10 primary evidence establishes that its corresponding MSC Supplement 7 wraps earlier TRW project report **11176-H314-R0-00**, dated 8 August 1969 under NAS9-8166. This supports searching for the underlying LM-5 contractor report without interpolating an Apollo 11 H-series number.

### Apollo 11 FTP archival lead

A primary-archive locator pass found a highly discriminating LM-5 lead in the **official Purdue University Libraries finding aid for the Neil A. Armstrong papers, MSA 5**. In Apollo Program working files / Mission Planning / A-11 Planning, the inventory lists an item titled **“Effect of fixed throttle point thrust on the time from loss of radial guidance control to DPS throttle-down,” dated 5 June 1969**.

The title is directly responsive to the unresolved FTP-force question and is contemporaneous with Apollo 11 planning. However, only the finding aid has been recovered, not the underlying document. Therefore no numerical FTP force is recorded or inferred.

### Companion throttle-down dispersion records located

A follow-on pass through Purdue's official Archives and Special Collections catalog found two additional Apollo 11 Mission Planning records dated **8 July 1969**:

- **“Effects of DPS engine dispersions and LM weight on throttle-down time”** — MSA 5, Series 1, Sub-Series 5, Sub-Group 4, File 2, Item 20; Box 54, Folder 5, Item 14.
- **“Effects of known dispersions at PDI on throttle-down time”** — MSA 5, Series 1, Sub-Series 5, Sub-Group 4, File 2, Item 21; Box 54, Folder 5, Item 15.

This is meaningful narrowing rather than numerical closure. The records' titles show that the Apollo 11 planning team explicitly analyzed throttle-down timing sensitivity to DPS engine dispersion, LM weight, and PDI dispersions immediately before flight. Their underlying contents were not exposed by the catalog, so no engine value, LM weight, PDI mass, or dispersion was inferred. These two items are now paired recovery targets with the 5 June FTP-thrust study.

## Boundary preserved

No later-LM force calibration was back-projected onto Eagle. No preflight/design thrust was promoted to delivered thrust. No pattern-derived Apollo 11 report number was promoted to sourced metadata. Purdue archive metadata is treated strictly as locator/provenance evidence until the underlying items are recovered. PDI mass remains unresolved.

## Repository updates

- `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/station-status/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `resources/APOLLO11_DESCENT_DYNAMICS_INPUT_SOURCE_CATALOG_ADDENDUM.md`

## Next

Recover the **5 June 1969 MSA 5 fixed-throttle-point-thrust item** and the two **8 July 1969 throttle-down dispersion items (File 2, Items 20–21)** from Purdue Archives. Inspect them for explicit LM-5 FTP force/calibration, engine-dispersion assumptions, LM weight/PDI state, and throttle-down sensitivity. Continue the underlying Apollo 11 / LM-5 DPS Final Flight Evaluation contractor-report search in parallel, followed by LM-5 engine acceptance/performance records. Retain page 2.3-25 and BET Volume II as named blocked targets.

## Evidence status

**PARTIALLY DOCUMENTED.** Purdue's official archival metadata now establishes three contemporaneous Apollo 11 planning documents directly relevant to FTP/throttle-down calibration and sensitivity, but their numerical/content evidence is **BLOCKED ON ARCHIVAL ITEM RECOVERY**. Supplement 7 identifiers/content remain blocked on bibliographic/archival recovery. Page 2.3-25 remains blocked on legible primary-page recovery. Exact LM-5 FTP force calibration, delivered thrust/Isp, and PDI mass remain unresolved. TRW BET Volume II remains **BLOCKED ON NAMED SOURCE RECOVERY**.