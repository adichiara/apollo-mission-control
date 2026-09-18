# LMS handbook retrieval source catalog

Status: active companion catalog to `LMS_DEPLOYED_COMPUTE_TOPOLOGY.md`. Updated through research 323.

## `LMA-790-2-LMS` — NASA bibliographic control

Primary NASA/MSC corporate-author control identifies adjacent Grumman handbook records under contract `NAS9-1100`:

| MSC accession | Issue date | Report | Identified content |
| --- | --- | --- | --- |
| `67-14186` | 1 Apr. 1967 in original index; 15 May 1967 in supplement | `LMA-790-2-LMS` | *Lunar Module Mission Simulator Instructors Handbook. Volume I — Simulator Description* |
| `67-14187` | 1 Apr. 1967 in original index; 15 May 1967 in supplement | `LMA-790-2-LMS` | *Lunar Module Mission Simulator Instructors Handbook. Vol. II — Simulator Operation Sections 1 and 4* |
| `67-14188` | **1 Apr. 1967** | `LMA-790-2-LMS` | *Lunar Module Mission Simulator Instructors Handbook. Volume II — Simulator Operation Sections 5 and 6* |
| `67-16127` | **1 Jul. 1967** | `LMA-790-2-LMS` | *LM Mission Simulator Instructors Handbook, Vol. II — Simulator Operation, Section 7 — Simulator Output Tables* |

NASA/MSC indexing contains conflicting **issue-date** records for `67-14186` and `67-14187`: the original Corporate Author Index gives **1 April 1967**, while its supplement gives **15 May 1967**. Research 317 verified from the index's own `TYPICAL CITATION` schema that this field means **Issue date: day, month, year**. Neither record by itself establishes that a revision or technical-content change occurred.

Research 322 separately confirms that `67-16127` is a distinct Section 7 accession with its own **1 July 1967 issue date**. Research 323 controls `67-14188` separately: the recovered primary index assigns Volume II Sections 5 and 6 their own accession and **1 April 1967** issue date. Do not infer a 15 May date for `67-14188` from the adjacent accessions; absence of a recovered conflicting supplement entry is not proof that no later issue/revision existed.

NASA/KSC `GP-642`, an independently compiled primary NASA bibliography, identifies entry 346 as Grumman `LMA 790-2-LMS`, Volume I — **Simulator Description** and Volume II Sections 1 and 4, dated **1 April 1967**. NTRS: https://ntrs.nasa.gov/api/citations/19700025401/downloads/19700025401.pdf

## Public Volume I candidate

Virtual AGC/ibiblio exposes a 150 MB file named `lms_instructors_handbook_vol1.pdf`:

https://www.ibiblio.org/apollo/Documents/lms_instructors_handbook_vol1.pdf

Research 319 confirms strong filename/title/volume compatibility with NASA `GP-642` entry 346, but **does not promote the scan to page-verified identity**. The current retrieval path cannot inspect the 150 MB object's internal title/document-control pages. Treat the file as a high-confidence retrieval candidate until its internal report number, title, issue/revision markings, and dates are read.

## Volume II Sections 2 and 3 — archival-title crosswalk

A contemporaneous NASA/MSC engineering memorandum (`MSC-IN-CF-P-69-5` / `NASA-TM-X-64471`) cites `LMA790-2-LMS`, Volume II, Sections II and III, dated 1 April 1967. The Virginia Tech James J. Avitabile Papers finding aid identifies Section 2 as **Malfunction Data** (3 folders) and Section 3 as **Lunar-landing Mission Procedures** (4 folders). Their MSC accession identifier(s) and technical contents remain unrecovered.

## Evidence use

This catalog controls retrieval identity only. Bibliographic records and filename compatibility do not establish DDP-224 count/allocation, program ownership, common-memory organization, visual interfaces, site effectivity, or Apollo 13 configuration. Sections 5/6 (`67-14188`) and Section 7 (`67-16127`) are distinct document-control units; neither accession's date establishes the other's effectivity.

## Retrieval order

1. `67-14186` / public Volume I candidate — inspect title/revision/effectivity pages first.
2. `67-16127` — Section 7, **Simulator Output Tables**; inspect its own document-control pages before technical use.
3. Section 2 — **Malfunction Data** — request the three Avitabile folders.
4. Section 3 — **Lunar-landing Mission Procedures** — request the four Avitabile folders.
5. `67-14187` — Volume II Sections 1 and 4.
6. `67-14188` — Volume II Sections 5 and 6; use **1 Apr. 1967** as the recovered primary issue-date key and inspect control/change pages before technical use.

For `67-14186`/`67-14187`, include both 1 Apr. and 15 May 1967 in archive searches; for `67-14188`, use 1 Apr. 1967; for `67-16127`, use 1 Jul. 1967.

Cross-references: research 310, 311, 317, 319, 322, **323**, 220, 313, and 315.
