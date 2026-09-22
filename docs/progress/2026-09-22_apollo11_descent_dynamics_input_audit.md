# Progress — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## Completed

Audited the next unresolved LM-5 descent inputs against primary Apollo documentation, preserving the distinction among design values, planned/commanded behavior, as-flown telemetry, reconstructed trajectory, and model inputs.

### PDI mass search narrowed to the correct primary table class

The Apollo 11 final Flight Plan documents an **unmanned LM weight of 33,278.3 lb** in its SPS budget assumptions and separately records **436.7 lb CSM→LM lunar-orbit weight transfer**. These are useful configuration-accounting anchors, but neither is promoted to PDI mass.

The targeted search identified **SNA-8-D-027(III) Rev. 2 / NASA-TM-X-68968, CSM/LM Spacecraft Operational Data Book, Volume III — Mass Properties** as the primary mission-specific mass-properties source family. The base revision is dated 20 August 1969 and covers G/H/J mission data.

### Public-scan amendment provenance audited

A recovery pass checked the surviving digitized Rev. 2 binder rather than assuming that its title-page date applies to every page. It does not. Indexed primary-document text shows the section 3 introduction at **Amendment 86 (9/10/70)** and a table 3.1-8 page at **Amendment 110 (7/19/71)** describing **LM-10**. The public binder therefore contains later replacement pages and is not a clean Mission-G-era snapshot.

### Primary postflight event masses recovered

The Apollo 11 Mission Report Appendix A.6/table A-I provides mission-specific postflight mass properties based on expendable loading/usage analysis and measured spacecraft/stage weights. For the LM it documents **33,683.5 lb at separation**, **33,669.6 lb at DOI ignition**, **33,401.6 lb at DOI cutoff**, and **16,153.2 lb at lunar landing**.

The table does not contain a PDI row, so PDI mass remains unresolved. These values are now the preferred primary event-mass checkpoints around the missing state.

A cross-check of NASA SP-4029, *Apollo by the Numbers*, found a provenance hazard: its cross-mission table places **33,669.6 lb** under PDI and **33,401.6 lb** under DOI ignition, whereas the primary Mission Report explicitly identifies those values as DOI ignition and DOI cutoff respectively. The secondary compilation is therefore not used to close PDI mass.

### PDI source-conflict propagation audit

NASA technical paper **20080013635**, *Lunar Surface Virtual Simulation* (2008), says its simulated Apollo 11 LM weight at PDI was **33,683.5 lb**, with 18,000 lb descent propellant. The number is exactly the primary Mission Report's **LM-separation** mass. Because the paper describes a simulation approximation and provides no Mission-G mass-ledger provenance for that PDI assignment, it is **not accepted as historical closure**.

### Mission-specific preflight DPS thrust envelope recovered

The contemporary NASA **Apollo 11 Press Kit** gives a mission-facing DPS specification: **9,870 lbf maximum rated thrust**, throttleable between **1,050 and 6,300 lbf**, and ±6° gimbal capability. NASA TN D-7143 later records a **10,500-lbf maximum-rated design requirement**.

### Fixed-throttle-point source provenance corrected

A follow-up provenance audit found that the searchable **LMA790-3-LM** Subsystems Data text previously used for the 92.5-percent fixed-throttle-point control description is not demonstrated to be LM-5 configuration evidence. NTRS identifies the surviving later handbook family as **LM-11 and subsequent** (NASA-CR-115269 / LMA790-3-LM-11), while the widely searchable Volume-I copy carries a **1 February 1970 basic date** and later change pages. Smithsonian independently catalogs the corresponding 1 February 1970 Volume I as **LM-7 and subsequent**.

The same later handbook family explicitly states that the engine develops **9,870 lbf nominal thrust at the fixed full-throttle position**, with a nominal throttle range of 1,050–6,800 lbf. This is strong primary evidence for the mature LM design semantics, but because its configuration postdates LM-5 it is **not promoted to an LM-5 calibration**.

The Apollo 11 Mission Report independently remains mission-specific evidence that LM-5 advanced from minimum thrust to the **fixed throttle point** about 26 seconds after PDI. The Apollo 11 Press Kit independently remains contemporary mission-specific evidence for a **9,870-lbf maximum-rated thrust** specification. What is still missing is a configuration-controlled LM-5 source explicitly tying its FTP calibration to that force value.

Implementation consequence: preserve **9,870 lbf as the Apollo 11 mission-facing preflight specification**, preserve FTP as the Apollo 11 as-flown control state, and treat the later handbook's 9,870-lbf nominal fixed-full-throttle statement as corroborating design-family evidence only. Do not label 9,870 lbf as LM-5 delivered thrust or an LM-5 recovered calibration.

### Apollo 11 DPS Supplement 7 recovery audit tightened

Later NASA mission-report supplement tables repeatedly identify Apollo 11 Supplement 7, *Descent Propulsion System Final Flight Evaluation*, as published in **September 1970**. A NASA retrospective technical-report catalog also contains the neighboring Apollo 11 ascent-propulsion final-flight evaluation, while the currently searchable NTRS Apollo holdings expose Apollo 11 Supplement 5 but not Supplement 7. This strengthens the classification **BLOCKED ON NAMED SOURCE RECOVERY**: the report's existence/publication is documented; its contents are not recovered. No report number, author, accession number, or performance values are inferred from neighboring supplements.

## Boundary preserved

No launch/unmanned mass plus transfer arithmetic was promoted to PDI mass. No Apollo 13 LM-7 or later LM-10 pre-PDI value was transferred to LM-5. No amendment-overwritten table was treated as Mission-G evidence solely from its section number. Later event-label drift was quarantined. No later-LM operations handbook was treated as LM-5 configuration evidence. No design or preflight thrust specification was promoted to delivered flight thrust, no design Isp was promoted to flight-effective Isp, and no reconstructed state was relabeled raw telemetry.

## Repository updates

- `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/station-status/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `resources/APOLLO11_DESCENT_DYNAMICS_INPUT_SOURCE_CATALOG_ADDENDUM.md`

## Next

Continue PDI-mass recovery only from a source explicitly labeling Mission G/LM-5 at PDI or pre-PDI with trustworthy event provenance. For propulsion, prioritize a **LM-5-specific AOH/vehicle manual revision, acceptance/performance record, or Apollo 11 DPS Supplement 7**. The later LMA790-3-LM handbook has clarified mature-design FTP semantics but does not close LM-5 calibration.

## Evidence status

**PARTIALLY DOCUMENTED.** Mission-specific postflight LM masses at separation, DOI ignition, DOI cutoff, and landing are primary-source documented. Exact Mission-G PDI mass remains unresolved. Apollo 11 sources establish a 9,870-lbf preflight specification and as-flown use of FTP; later primary operations documentation establishes 9,870-lbf nominal fixed-full-throttle semantics for later LMs, but exact LM-5 FTP calibration, delivered thrust, and flight-effective Isp remain unresolved. Apollo 11 DPS Supplement 7 and TRW BET Volume II remain **BLOCKED ON NAMED SOURCE RECOVERY**.