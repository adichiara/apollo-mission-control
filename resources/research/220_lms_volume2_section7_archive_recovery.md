# Research note 220 — LMS Volume II Section 7 archival recovery

Date: 2026-09-16  
Status: **PRIMARY DOCUMENT IDENTITY/ARCHIVAL HOLDING RECOVERED; Section 7 contents not yet digitized/reviewed.**

## Question

Can the LMS `Simulator Output Tables` target left by research note 219 be narrowed from a corporate-index citation to a concrete surviving archival holding without inventing its contents?

## Evidence

### 1. NASA bibliographic record establishes the handbook family

NASA's 1970 technical-report bibliography includes item 346:

> `LUNAR MODULE MISSION SIMULATOR INSTRUCTORS HANDBOOK, VOL. 1 - SIMULATOR DESCRIPTION, VOL 2 - SECTION 1 - SIMULATOR OPERATION, SECTION 4 - INSTRUCTOR ACTIVITY FOR INTERFACE OPERATION.`

It identifies Grumman Aircraft Engineering Corporation and dates the handbook family to 1 April 1967 (`GAEC LMA 790-2-LMS Vols. I and II`).

Primary scan:
https://www.ibiblio.org/apollo/Documents/19700025401.pdf

This confirms the document family independently of the corporate index, but the bibliography item itself names only Volume II Sections 1 and 4. It therefore does **not** establish Section 7 contents.

### 2. Surviving James J. Avitabile papers contain the missing Section 7 holding

The University of Houston-Clear Lake Archives catalog for the James J. Avitabile Papers lists the LMS handbook at folder level. Under Volume II it identifies:

- `Simulator Operation`, 1 Apr 1967;
- changed `Simulator Operation`, 15 May 1967;
- Section 2 — `Malfunction Data` (3 folders);
- Section 3 — `Lunar-landing Mission Procedures` (4 folders);
- Section 4 — `Instructor Activity for Interface Operation`;
- Section 5 — `Instructor Material` (6 folders);
- Section 6 — `Scripting Data Sheets` (2 folders);
- **Section 7 — `Simulator Output Tables`, 1 Jul 1967 (3 folders).**

Archive catalog:
https://arvasarchive.org/catalog/viblbv_repositories_2_resources_2187

The catalog is a finding aid, not the primary technical content. It establishes that a surviving three-folder Section 7 holding exists and gives its date/title; it does not authorize reconstruction of any output field, model designator, routing, cadence, precision, or acceptance criterion.

### 3. Relationship to the corporate index

The existing source catalog records the NASA/NARA corporate-index accession `*67-16127` for LMA-790-2-LMS Volume II, Section 7. The Avitabile finding aid independently identifies a surviving Section 7 under the same handbook family and gives a 1 July 1967 date and three-folder extent.

This is useful corroboration of identity and survival, but no claim is made that the Avitabile folders are physically the same accession copy represented by `*67-16127`.

## What is now established

- `Simulator Output Tables` is not merely a title in a corporate index; a surviving archival Section 7 holding is cataloged.
- The holding is dated **1 July 1967** and spans **three folders** in the Avitabile Papers.
- Volume II was a multi-section operational/instructor handbook that separately included malfunction data, mission procedures, instructor material, scripting data, and output tables.
- This makes Section 7 a concrete retrieval target for source-variable/output/model-designator extraction.

## What remains unresolved

Until the three folders are opened, do **not** claim:

- which LMS outputs are listed;
- which subsystem/model owns a given output;
- output units, resolution, cadence, precision, or routing;
- which outputs were visible to instructors versus Mission Control;
- whether Section 7 supplies acceptance/correlation observables or tolerances;
- Apollo 13/LM-7 effectivity of any listed field;
- that the Avitabile copy and MSC accession `*67-16127` are identical physical copies/revisions.

## Project consequence

Research note 219's `Simulator Output Tables` target is now actionable at folder level. The next archival request should ask specifically for **LMA-790-2-LMS Volume II, Section 7, Simulator Output Tables, 1 July 1967, three folders** in the James J. Avitabile Papers.

If recovered, extraction should build a table of:

`output identifier → source/model designator → engineering representation → simulator destination/use → effectivity/revision evidence`

and only then compare those observables with acceptance/correlation documents from RG 255 E.155B1.

## Sources

- NASA technical-report bibliography, item 346, primary scan: https://www.ibiblio.org/apollo/Documents/19700025401.pdf
- University of Houston-Clear Lake Archives, James J. Avitabile Papers finding aid: https://arvasarchive.org/catalog/viblbv_repositories_2_resources_2187
- Existing corporate-index evidence and acceptance boundary: `resources/source-catalog/APOLLO_SIMULATION_ENGINE_SOURCES.md`; `resources/research/219_lms_validation_acceptance_source_boundary.md`.
