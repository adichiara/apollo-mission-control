# Progress — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## Completed

Audited the next unresolved LM-5 descent inputs against primary Apollo documentation, preserving the distinction among design values, planned/commanded behavior, as-flown telemetry, reconstructed trajectory, and model inputs.

### PDI mass search narrowed to the correct primary table class

The Apollo 11 final Flight Plan documents an **unmanned LM weight of 33,278.3 lb** in its SPS budget assumptions and separately records **436.7 lb CSM→LM lunar-orbit weight transfer**. These are useful configuration-accounting anchors, but neither is promoted to PDI mass.

The targeted search identified **SNA-8-D-027(III) Rev. 2 / NASA-TM-X-68968, CSM/LM Spacecraft Operational Data Book, Volume III — Mass Properties** as the primary mission-specific mass-properties source family. The base revision is dated 20 August 1969 and covers G/H/J mission data.

### Public-scan amendment provenance audited

A recovery pass checked the surviving digitized Rev. 2 binder rather than assuming that its title-page date applies to every page. Indexed primary-document text shows the section 3 introduction at **Amendment 86 (9/10/70)** and a table 3.1-8 page at **Amendment 110 (7/19/71)** describing **LM-10**. The public binder therefore contains later replacement pages and is not a clean Mission-G-era snapshot.

### Primary postflight event masses recovered

The Apollo 11 Mission Report Appendix A.6/table A-I provides mission-specific postflight mass properties based on expendable loading/usage analysis and measured spacecraft/stage weights. For the LM it documents **33,683.5 lb at separation**, **33,669.6 lb at DOI ignition**, **33,401.6 lb at DOI cutoff**, and **16,153.2 lb at lunar landing**. The table does not contain a PDI row.

NASA SP-4029 and NASA 20080013635 were audited and rejected for PDI closure because their event/value assignments do not establish the missing Mission-G PDI state.

### Mission-specific preflight DPS thrust envelope recovered

The contemporary NASA **Apollo 11 Press Kit** gives a mission-facing DPS specification: **9,870 lbf maximum rated thrust**, throttleable between **1,050 and 6,300 lbf**, and ±6° gimbal capability. NASA TN D-7143 later records a **10,500-lbf maximum-rated design requirement**.

### Fixed-throttle-point source provenance corrected

The searchable later **LMA790-3-LM** Subsystems Data text gives 92.5-percent FTP and 9,870-lbf nominal fixed-full-throttle semantics, but surviving catalog provenance identifies that material as LM-7-and-subsequent or later. It remains design-family evidence, not LM-5 calibration.

The Apollo 11 Mission Report independently documents LM-5 advancing to FTP about 26 seconds after PDI.

### LM-5-specific operations handbook recovered

The next targeted search recovered a public scan of **LMA790-3-LM 5 and Subsequent, Volume II — Operational Procedures** in the Virtual AGC/ibiblio primary-document collection. Its title page explicitly identifies **LM 5 and Subsequent** and states that the issue supersedes the **15 February 1969** edition. This materially improves provenance: an LM-5-specific AOH is not merely known from later references or collector records; a mission-applicable operational volume is publicly inspectable.

The result is deliberately bounded. Volume II is the operational-procedures volume, not the subsystem-description/calibration volume. Targeted checks did not recover an LM-5-specific FTP percentage-to-force calibration, a 9,870-lbf FTP calibration statement, or delivered thrust/Isp performance from this volume. Therefore the later Volume-I 92.5-percent/9,870-lbf language is **not** back-projected onto Eagle.

The propulsion search is now narrower: recover **LM-5 Volume-I Subsystems Data** at a mission-applicable revision/change state, an LM-5 engine acceptance/performance record, or Apollo 11 Mission Report Supplement 7.

### Apollo 11 DPS Supplement 7 recovery audit tightened

Later NASA mission-report supplement tables identify Apollo 11 Supplement 7, *Descent Propulsion System Final Flight Evaluation*, as published in **September 1970**. Its contents remain **BLOCKED ON NAMED SOURCE RECOVERY**; no report number, author, accession number, or performance values are inferred from neighboring supplements.

## Boundary preserved

No launch/unmanned mass plus transfer arithmetic was promoted to PDI mass. No later-LM mass was transferred to LM-5. No amendment-overwritten table was treated as Mission-G evidence solely from its section number. No later-LM subsystem handbook was treated as LM-5 calibration evidence. Recovery of LM-5 Volume II was not misrepresented as recovery of LM-5 Volume I or of an engine calibration. No design or preflight thrust specification was promoted to delivered flight thrust, no design Isp was promoted to flight-effective Isp, and no reconstructed state was relabeled raw telemetry.

## Repository updates

- `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/station-status/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `resources/APOLLO11_DESCENT_DYNAMICS_INPUT_SOURCE_CATALOG_ADDENDUM.md`

## Next

Continue PDI-mass recovery only from a source explicitly labeling Mission G/LM-5 at PDI or pre-PDI with trustworthy event provenance. For propulsion, the generic LM-5 AOH target is narrowed: **LM-5 Volume II is recovered but does not close calibration**. Prioritize LM-5 **Volume-I Subsystems Data**, acceptance/performance records, or Apollo 11 DPS Supplement 7.

## Evidence status

**PARTIALLY DOCUMENTED.** Mission-specific postflight LM masses, Apollo 11 9,870-lbf preflight specification, LM-5 FTP use, and LM-5 Volume-II operational-handbook provenance are documented. Exact Mission-G PDI mass, LM-5 FTP force calibration, delivered thrust, and flight-effective Isp remain unresolved. Apollo 11 DPS Supplement 7 and TRW BET Volume II remain **BLOCKED ON NAMED SOURCE RECOVERY**.