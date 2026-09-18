# Research note 313 — LMS handbook Sections 2 and 3 primary-reference recovery

Date: 2026-09-18  
Status: **PRIMARY NASA MISSION-ENGINEERING REFERENCE ESTABLISHES AN ADDITIONAL 1967 LMS HANDBOOK SECTION PAIR; ACCESSION/SCAN NOT YET RECOVERED.**

## Question

Does the current `LMA-790-2-LMS` retrieval map omit any handbook material that could matter to simulator operation, interface activity, or machine/program allocation?

## Primary-source result

NASA/MSC technical memorandum `MSC-IN-CF-P-69-5` / `NASA-TM-X-64471`, *Mission F, LM Descent/Phasing Summary Document*, by C. O. Lewis and R. T. Neal (1969; NTRS `19700026546`), includes in its references:

> Lunar Module Mission Simulator Instructors Handbook, Volume II, Secs. II and III, LMA790-2-LMS, April 1, 1967.

NTRS record and scan:

- https://ntrs.nasa.gov/citations/19700026546
- https://ntrs.nasa.gov/api/citations/19700026546/downloads/19700026546.pdf

This is contemporaneous NASA mission-engineering use of the exact Grumman report family and date already established for the 1967 handbook.

## What this changes

The repository's archival map already tracks:

- `67-14186` — Volume I, Simulator Description;
- `67-14187` — Volume II, Sections 1 and 4;
- `67-14188` — Volume II, Sections 5 and 6;
- `67-16127` — Volume II, Section 7, Simulator Output Tables.

The 1969 NASA memorandum proves that **Volume II Sections 2 and 3 also existed and were used as a technical reference**. The current accession crosswalk is therefore incomplete as a map of the handbook's Volume II contents, even though it remains correct for the accession records already recovered.

## What is not established

The reference does not provide:

- an MSC accession number for Sections 2 and 3;
- section titles;
- page content;
- machine/program allocation;
- DDP-224 workload ownership;
- site-specific configuration;
- Apollo 13 effectivity.

Do not infer any of those from section numbering or from the fact that a Mission F engineering memorandum cited the handbook.

## Retrieval consequence

Sections 2 and 3 become an explicit retrieval target. Search bibliographic controls and archival holdings for `LMA-790-2-LMS` together with `SECTION 2`, `SECTION 3`, `SECTIONS II AND III`, and the April 1, 1967 date. If recovered, inspect their actual titles/scope before assigning them a role in the compute-topology investigation.

The existing priority remains to authenticate/page-extract Volume I because it is explicitly *Simulator Description*. Sections 2/3 should be pursued in parallel with `67-16127`, `67-14187`, and `67-14188` rather than guessed from the gaps in numbering.

## Architecture/product consequence

None yet. This closes a documentation-map omission, not a simulator-behavior gate. No runtime constants, station products, station maturity, or Apollo 13 profile assumptions change.

## Evidence state

**DOCUMENTED**

- NASA/MSC `MSC-IN-CF-P-69-5` cites `LMA790-2-LMS`, Volume II, Sections II and III, dated April 1, 1967.
- Volume II therefore contained Sections 2 and 3 in addition to the currently accession-mapped Sections 1, 4, 5, 6, and 7.

**NOT YET ESTABLISHED**

- Sections 2/3 titles and contents.
- Their MSC accession identifier(s).
- Whether they contain computer/machine/program-allocation evidence.
- Apollo 13 applicability.

## Sources

- NASA NTRS `19700026546`, Lewis & Neal, *Mission F, LM Descent/Phasing Summary Document*, `MSC-IN-CF-P-69-5` / `NASA-TM-X-64471`, 1969.
- Existing NASA/MSC corporate-author index crosswalk for the other `LMA-790-2-LMS` volumes/sections.
