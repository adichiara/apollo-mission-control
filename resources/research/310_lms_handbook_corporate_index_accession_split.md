# Research 310 — LMS handbook corporate-index accession split

Date: 2026-09-18

## Question

Can the unresolved `LMA-790-2-LMS` retrieval target be narrowed using NASA/MSC primary bibliographic control without inferring handbook contents?

## Result

Yes. The NASA/MSC *Corporate Author Index* gives two adjacent, explicit Grumman records under `NAS9-1100`, both dated **15 May 1967**:

- MSC accession **67-14186** — `LMA-790-2-LMS`, *Lunar Module Mission Simulator Instructors Handbook. Volume I — Simulator Description*.
- MSC accession **67-14187** — `LMA-790-2-LMS`, *Lunar Module Mission Simulator Instructors Handbook. Vol. II — Simulator Operation Sections 1 and 4*.

This materially improves retrieval control: Volume I simulator-description work should target `67-14186`; the Sections 1/4 operating material should target `67-14187`. The shared report number does not mean the accessions are interchangeable.

## Evidence class

The NASA/MSC corporate-author index is primary bibliographic control. It establishes report/accession/date/contract/title identity, not the technical contents of the unrecovered handbook volumes.

Source: NASA/MSC *Corporate Author Index* (Grumman Aircraft Engineering Corp. entries), NASA-hosted archival copy mirrored by the Apollo archive: https://www.ibiblio.org/apollo/NARASWoverflow/CorporateIndex.pdf

## Important boundary

Do not use the index entry to infer:

- DDP-224 processor count or workload allocation;
- common-memory organization;
- program loading or machine ownership;
- visual-system hardware/configuration;
- KSC versus MSC effectivity of a particular handbook copy;
- Apollo 13 configuration.

Those claims require the handbook pages or other applicable primary records.

## Date-control consequence

The corporate-author index supports **15 May 1967** for both `67-14186` and `67-14187`. Existing project documentation also records an `01-04-67` date from another MSC index and an Apr. 1, 1967 KSC bibliography entry. Preserve that bibliographic date discrepancy rather than silently normalizing it; the dates may reflect edition, issue, receipt, or cataloging differences that have not yet been demonstrated.

## Project consequence

The next handbook retrieval sequence is now explicit:

1. `67-14186` for Volume I simulator description.
2. `67-14187` for Volume II simulator-operation Sections 1 and 4.
3. `67-16127` / other separately cataloged sections only when their identities are independently verified.

No executable constants, station maturity grades, machine counts, or workload assignments change.
