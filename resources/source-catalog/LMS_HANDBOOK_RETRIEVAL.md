# LMS handbook retrieval source catalog

Status: active companion catalog to `LMS_DEPLOYED_COMPUTE_TOPOLOGY.md`. Updated through research 319.

## `LMA-790-2-LMS` — NASA bibliographic control

Primary NASA/MSC corporate-author control identifies adjacent Grumman handbook records under contract `NAS9-1100`:

| MSC accession | Report | Identified content |
| --- | --- | --- |
| `67-14186` | `LMA-790-2-LMS` | *Lunar Module Mission Simulator Instructors Handbook. Volume I — Simulator Description* |
| `67-14187` | `LMA-790-2-LMS` | *Lunar Module Mission Simulator Instructors Handbook. Vol. II — Simulator Operation Sections 1 and 4* |

NASA/MSC indexing contains conflicting **issue-date** records: the original Corporate Author Index gives **1 April 1967** for the adjacent handbook accessions, while its supplement gives **15 May 1967** for `67-14186` and `67-14187`. Research 317 verified from the index's own `TYPICAL CITATION` schema that this field means **Issue date: day, month, year**. Neither record by itself establishes that a revision or technical-content change occurred.

NASA/KSC `GP-642`, an independently compiled primary NASA bibliography, identifies entry 346 as Grumman `LMA 790-2-LMS`, Volume I — **Simulator Description** and Volume II Sections 1 and 4, dated **1 April 1967**. NTRS: https://ntrs.nasa.gov/api/citations/19700025401/downloads/19700025401.pdf

## Public Volume I candidate

Virtual AGC/ibiblio exposes a 150 MB file named `lms_instructors_handbook_vol1.pdf`:

https://www.ibiblio.org/apollo/Documents/lms_instructors_handbook_vol1.pdf

Research 319 confirms strong filename/title/volume compatibility with NASA `GP-642` entry 346, but **does not promote the scan to page-verified identity**. The current retrieval path cannot inspect the 150 MB object's internal title/document-control pages, and no separately indexed NTRS record for `67-14186` / `LMA-790-2-LMS` was recovered in that pass. Treat the file as a high-confidence retrieval candidate until its internal report number, title, issue/revision markings, and dates are read.

## Volume II Sections 2 and 3 — archival-title crosswalk

A contemporaneous NASA/MSC engineering memorandum (`MSC-IN-CF-P-69-5` / `NASA-TM-X-64471`) cites `LMA790-2-LMS`, Volume II, Sections II and III, dated 1 April 1967.

The Virginia Tech James J. Avitabile Papers finding aid separately identifies the surviving section titles/extent:

- Section 2 — **Malfunction Data** — 3 folders;
- Section 3 — **Lunar-landing Mission Procedures** — 4 folders.

Their MSC accession identifier(s) and technical contents remain unrecovered. See research notes 220, 313, and 315.

## Evidence use

This catalog controls retrieval identity only. Bibliographic records and filename compatibility do not establish DDP-224 count/allocation, program ownership, common-memory organization, visual interfaces, site effectivity, or Apollo 13 configuration.

The 1 April versus 15 May 1967 discrepancy is specifically a conflict between NASA/MSC **issue-date records**. Preserve both dates until document-control pages or records-management evidence explains the conflict; do not relabel either date as publication, receipt, accession, revision, or reissue without evidence.

## Retrieval order

1. `67-14186` / public Volume I candidate — inspect title/revision/effectivity pages first and close the identity gate.
2. Volume II Section 2 — **Malfunction Data** — request the three Avitabile folders; high value for malfunction-insertion architecture.
3. `67-16127` — Volume II Section 7, Simulator Output Tables.
4. Volume II Section 3 — **Lunar-landing Mission Procedures** — request the four Avitabile folders.
5. `67-14187` — Volume II Sections 1 and 4.
6. `67-14188` — Volume II Sections 5 and 6 if operating/instructor material is still needed.

For archive requests include `LMA-790-2-LMS`, `NAS9-1100`, both accessions, and both 1 Apr. and 15 May 1967 dates to avoid false negatives caused by issue-date mismatch.

Cross-references:

- `resources/research/310_lms_handbook_corporate_index_accession_split.md`
- `resources/research/311_lms_handbook_gp642_bibliographic_crosscheck.md`
- `resources/research/317_lms_index_issue_date_semantics.md`
- `resources/research/319_lms_volume1_direct_retrieval_gate.md`
- `resources/research/220_lms_volume2_section7_archive_recovery.md`
- `resources/research/313_lms_handbook_sections_2_3_primary_reference.md`
- `resources/research/315_lms_sections_2_3_archival_title_reconciliation.md`
