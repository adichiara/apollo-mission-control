# LMS handbook retrieval source catalog

Status: active companion catalog to `LMS_DEPLOYED_COMPUTE_TOPOLOGY.md`. Updated through research 328.

## `LMA-790-2-LMS` — NASA bibliographic control

Primary NASA/MSC corporate-author control identifies adjacent Grumman handbook records under contract `NAS9-1100`:

| MSC accession | Issue date | Report | Identified content |
| --- | --- | --- | --- |
| `67-14186` | 1 Apr. 1967 in original index; 15 May 1967 in supplement | `LMA-790-2-LMS` | *Lunar Module Mission Simulator Instructors Handbook. Volume I — Simulator Description* |
| `67-14187` | 1 Apr. 1967 in original index; 15 May 1967 in supplement | `LMA-790-2-LMS` | *Lunar Module Mission Simulator Instructors Handbook. Vol. II — Simulator Operation Sections 1 and 4* |
| `67-14188` | **1 Apr. 1967** | `LMA-790-2-LMS` | *Lunar Module Mission Simulator Instructors Handbook. Volume II — Simulator Operation Sections 5 and 6* |
| `67-16127` | **1 Jul. 1967** | `LMA-790-2-LMS` | *LM Mission Simulator Instructors Handbook, Vol. II — Simulator Operation, Section 7 — Simulator Output Tables* |

NASA/MSC indexing contains conflicting **issue-date** records for `67-14186` and `67-14187`: the original Corporate Author Index gives **1 April 1967**, while its supplement gives **15 May 1967**. Research 317 verified from the index's own `TYPICAL CITATION` schema that this field means **Issue date: day, month, year**.

Research 324 adds archival arrangement evidence from the Virginia Tech Avitabile finding aid: Volume II has a 1 April 1967 **Simulator Operation** holding and a 15 May 1967 **Simulator Operation (Changed)** holding. This permits the May holding to be described as changed, but does not establish the technical delta, revision identifier, or which body pages changed.

Research 322 separately confirms that `67-16127` is a distinct Section 7 accession with its own **1 July 1967 issue date**. Research 323 controls `67-14188` separately: the recovered primary index assigns Volume II Sections 5 and 6 their own accession and **1 April 1967** issue date. Do not infer a 15 May date for `67-14188`; absence of a recovered conflicting supplement entry is not proof that no later issue/revision existed.

NASA/KSC `GP-642`, an independently compiled primary NASA bibliography, identifies entry 346 as Grumman `LMA 790-2-LMS`, Volume I — **Simulator Description** and Volume II Sections 1 and 4, dated **1 April 1967**. NTRS: https://ntrs.nasa.gov/api/citations/19700025401/downloads/19700025401.pdf

## Public Volume I candidate

Virtual AGC/ibiblio exposes a 150 MB file named `lms_instructors_handbook_vol1.pdf`:

https://www.ibiblio.org/apollo/Documents/lms_instructors_handbook_vol1.pdf

Research 319 confirms strong filename/title/volume compatibility with NASA `GP-642` entry 346, but **does not promote the scan to page-verified identity**. Treat the file as a high-confidence retrieval candidate until its internal report number, title, issue/revision markings, and dates are read.

## Volume II archival section crosswalk

The Virginia Tech James J. Avitabile Papers finding aid supplies the following retrieval titles and extents:

- Section 1 — **Simulator Operation** — 2 folders in the April arrangement; another Section 1 follows the 15 May **Changed** heading.
- Section 2 — **Malfunction Data** — 3 folders.
- Section 3 — **Lunar-landing Mission Procedures** — 4 folders.
- Section 4 — **Instructor Activity for Interface Operation** — represented twice in the arrangement.
- Section 5 — **Instructor Material** — 6 folders.
- Section 6 — **Scripting Data Sheets** — 2 folders.
- Section 7 — **Simulator Output Tables** — 1 July 1967 — 3 folders.

A contemporaneous NASA/MSC engineering memorandum (`MSC-IN-CF-P-69-5` / `NASA-TM-X-64471`) independently cites `LMA790-2-LMS`, Volume II, Sections II and III, dated 1 April 1967. MSC accession identifier(s) for Sections 2/3 and their technical contents remain unrecovered. The finding-aid arrangement alone does not establish whether Sections 2/3 or either Section 4 holding belong to a particular issue without page-level verification.

Finding aid: https://arvasarchive.org/catalog/viblbv_repositories_2_resources_2187

## Apollo 13 mission-specific malfunction cross-check

Research 325 added **Apollo 13 LM Malfunction Procedures** as a separate operational-effectivity source family. Research 326 resolves the state of the public Lovell scan from its own indexed cover text:

- title: **Apollo 13 LM Malfunction Procedures**;
- part number: `SKB32100076-386`;
- cover status: **FINAL**;
- cover date: **16 March 1970**.

Virtual AGC records that the public scan was digitized from Jim Lovell's original copy and added to the collection on 6 March 2023. NASA's Apollo 13 final stowage list independently identifies `SKB32100076-386` as **LM MALFUNCTION PROCEDURES** within the LM Flight Data File, establishing mission carriage for that part number.

Primary/public records:

- Lovell-copy scan: https://www.ibiblio.org/apollo/Documents/Apollo%2013%20Malfunction%20Procedures.pdf
- Virtual AGC provenance: https://www.ibiblio.org/apollo/changes.html
- NASA Apollo 13 final stowage list: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/as13b-stowage-list-final-197007.pdf

A separately surviving 1 April 1970 **FINAL CHANGE A** quarters/training copy is a later document state. Its technical delta from the 16 March FINAL state remains unrecovered and must not be merged into the Lovell scan without page-level comparison.

Research 328 begins the requested page/tab inventory. Indexed OCR from the primary Lovell scan directly exposes **AGS, CES, DPS, and RCS** labels. A secondary artifact description of another 16 March copy of the same part number gives the fuller provisional inventory **G&C Displays, PGNS, AGS, CES, DPS, APS, RCS, EPS, COMM, ECS, ED, HTRS, Camera, EMU**. Only the labels directly exposed by the primary scan are presently promoted as direct scan observations; the fourteen-label list remains provisional until S/N 1001 tabs/pages can be inspected directly.

Use the controlled 16 March source to corroborate **player-visible Apollo 13 LM symptoms, caution/warning indications, crew troubleshooting branches, and phase restrictions**, preserving any page-specific dates/change markings encountered. Do not use it to infer LMS instructor controls, scripting syntax, internal failure representation, or whether a malfunction was injectable in the LMS.

The contemporaneous NASA H-2 mission-technique series (January-April 1970) remains an independent cross-check for mission phase and operational applicability.

## Apollo 13 simulation failure-planning evidence

Research 327 consolidates a primary Apollo 13-period operational constraint already represented in the station research:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, **28 April 1970**.
- NASA: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- NTRS: https://ntrs.nasa.gov/api/citations/19710010485/downloads/19710010485.pdf

Its simulation lessons state that simulation mistakes should be corrected promptly to avoid **negative training**; that malfunction procedures depend on the failure actually present, with different loss scopes potentially requiring different procedures; and that failures should therefore be planned carefully so the appropriate procedures can be exercised.

Evidence use: this supports historical scenario-authoring and validation rules at the operational level — especially **failure -> observable consequence -> applicable procedure/decision path**. It does not document LMS instructor controls, scripting syntax, internal failure representation, or prove that a specific LM malfunction was simulator-injectable.

## Evidence use

This catalog controls retrieval identity and evidence scope. Bibliographic records and archival arrangement do not establish DDP-224 count/allocation, program ownership, common-memory organization, visual interfaces, site effectivity, Apollo 13 LMS configuration, scripting syntax, malfunction definitions, or numerical constants. Sections 5/6 (`67-14188`) and Section 7 (`67-16127`) are distinct document-control units; neither accession's date establishes the other's effectivity. Apollo 13 crew malfunction procedures constrain operational behavior only and do not establish simulator implementation. Apollo 13 simulation lessons constrain exercise design, not LMS capability.

## Retrieval order

1. `67-14186` / public Volume I candidate — inspect title/revision/effectivity pages first.
2. Section 2 — **Malfunction Data** — request the three Avitabile folders.
3. Apollo 13 `SKB32100076-386` — continue page extraction of the controlled **16 Mar. 1970 FINAL** state; first verify the provisional tab inventory against S/N 1001, then inventory symptom/procedure headings and page-specific markings tab-by-tab.
4. Cross-check candidate scenario failures against Apollo 13-period operational procedures and research 327's failure-scope/negative-training constraints.
5. Compare the 16 Mar. FINAL and 1 Apr. FINAL CHANGE A states if page-level access to both becomes available; recover the actual delta before using Change A material.
6. `67-16127` — Section 7, **Simulator Output Tables**; inspect its own document-control pages before technical use.
7. Section 6 — **Scripting Data Sheets** — request the two Avitabile folders if historical instructor scripting/failure-insertion abstractions remain unresolved.
8. Section 3 — **Lunar-landing Mission Procedures** — request the four Avitabile folders.
9. `67-14187` / Sections 1 and 4 — compare April and May control/body pages; use the archival **Changed** label without inventing a revision number or delta.
10. `67-14188` / Section 5 **Instructor Material** and Section 6 **Scripting Data Sheets**; use **1 Apr. 1967** as the recovered NASA issue-date key and inspect control/change pages before technical use.

For `67-14186`/`67-14187`, include both 1 Apr. and 15 May 1967 in archive searches; for `67-14188`, use 1 Apr. 1967; for `67-16127`, use 1 Jul. 1967.

Cross-references: research 310, 311, 317, 319, 322, 323, 324, 325, 326, 327, **328**, 220, 313, and 315.
