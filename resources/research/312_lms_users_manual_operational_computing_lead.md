# Research note 312 — LMS User's Manual operational-computing source lead

Date: 2026-09-18  
Status: **DIRECT PUBLIC SCAN LOCATED; SEARCH-INDEX TEXT REVIEWED; PAGE-LEVEL EXTRACTION INCOMPLETE BECAUSE THE PUBLIC PDF EXCEEDS THE CURRENT VIEWER LIMIT.**

## Question

Can the newly surfaced *LMS User's Manual* help close the remaining deployed-compute and program-operation gaps without importing late-program configuration into Apollo 13?

## Source recovered

Virtual AGC's public document index contains:

- `LMS_Users_Manual.pdf` — 89 MB;
- `LMS_Console_Directory.pdf` — 11 MB, adjacent in the same January 2025 addition set.

Public scan:

https://www.ibiblio.org/apollo/Documents/LMS_Users_Manual.pdf

Discovery/index:

https://www.ibiblio.org/apollo/Documents/

Virtual AGC's 23 January 2025 change log describes this source as **a user's manual for the Lunar Module Simulator**, separately from the LMS Console Directory.

https://www.ibiblio.org/apollo/changes.html

The searchable scan index exposed a cover/header identifying **LMS USER'S MANUAL, VOLUME 1**, **UPDATE #34**, dated **22 October 1971**. It also exposed a `TABLE 3-1 PERIPHERAL DEVICE CODES` with DDP-oriented peripheral categories including magnetic tape, character, typewriter, and card devices.

Because the 89 MB PDF cannot currently be fetched/rendered by the available page viewer, those indexed snippets are retained as retrieval evidence rather than treated as a page-by-page extraction.

## What this adds

This is a different source class from the 1967 instructor handbook and the 1971 Console Directory:

- the instructor handbook describes simulator equipment/subsystem simulation;
- the Console Directory describes exposed measurements/output-channel metadata;
- the User's Manual appears to describe user/operator interaction with the LMS computing environment.

That makes it a high-value candidate for questions that remain open after the current topology work:

- program loading and initialization;
- operator-visible computer/peripheral controls;
- DDP-oriented I/O conventions;
- possibly software/program operational ownership or machine use.

The indexed peripheral-code table is enough to justify pursuing the manual as a computing-operations source. It is **not** enough to assign workloads to specific LMS processors.

## Historical boundary

The manual is dated October 1971. It therefore cannot, by itself, establish Apollo 13 H-2 configuration in April 1970.

Do **not** use it alone to assert:

- Apollo 13 processor count or machine assignment;
- original two-DDP workload ownership;
- common-memory mapping;
- exact program names or revisions in the H-2 LMS;
- Apollo 13 load procedures;
- Apollo 13 telemetry/output routing;
- model integration cadence or numerical tolerances.

Any Apollo 13 adoption needs an earlier or configuration-controlled cross-check.

## Relationship to the current Volume I retrieval gate

This source does not replace `LMA-790-2-LMS` Volume I / MSC accession `67-14186`.

The public 1967 Volume I candidate remains the more important source for subsystem-simulation architecture and machine-description context. The 1971 User's Manual is complementary: it may expose how the mature simulator computing environment was operated.

The identity gate in research note 240 remains open until the public 1967 scan's own title/revision pages can be inspected or equivalent provenance metadata ties it directly to `LMA-790-2-LMS` / `67-14186`.

## Architecture consequence

**No new historical runtime behavior is frozen from this source yet.**

The project already has the right separation:

`authoritative model state -> measurement/output definition -> exposed value/validity -> ground/controller product`

and already has a reusable measurement/output model plus a site-facing Causal Model Lab proof.

The User's Manual should now be used to investigate the **simulator-computing/operator layer**, not to collapse that layer into spacecraft physics or telemetry definitions.

## Next extraction targets

1. Obtain a locally/page-renderable copy and capture the title, update/revision, table of contents, and introductory scope.
2. Search the manual for `DDP-224`, `computer`, `common memory`, `program`, `load`, `magnetic tape`, `card`, `initialize`, `restart`, and machine identifiers.
3. Separate generic DDP peripheral operation from LMS-specific program/machine assignment.
4. Cross-check any machine/program claims against:
   - `67-14186` Volume I;
   - `67-16127` Volume II Section 7 output tables;
   - NASA TN D-7112;
   - Apollo 13-period configuration/change records.
5. Keep 1971 operational practices profile-dated unless an earlier source establishes continuity.

## Evidence state

**DOCUMENTED**

- A public 89 MB `LMS_Users_Manual.pdf` exists in the Virtual AGC Apollo document collection.
- Virtual AGC identifies it as a user's manual for the Lunar Module Simulator.
- Search-index text identifies Volume 1 / Update #34 / 22 October 1971 and exposes a DDP-oriented peripheral-device-code table.

**PARTIALLY DOCUMENTED**

- The manual's detailed program-loading and computer-operation content.

**NOT YET ESTABLISHED**

- Exact machine/program ownership.
- Apollo 13 applicability.
- A direct relationship between this 1971 manual and the `67-14186` archival accession beyond their common LMS subject.

## Sources

- Virtual AGC document index, `LMS_Users_Manual.pdf`.
- Virtual AGC change log, 23 January 2025 addition note.
- Public searchable index text for the LMS User's Manual scan.
