# Research note 322 — LMS Volume II Section 7 separate issue control

Date: 2026-09-18

## Question

What does the primary NASA/MSC bibliographic record establish about `LMA-790-2-LMS`, Volume II, Section 7, and how should that affect retrieval/effectivity control?

## Primary-source-first finding

The NASA/MSC *Apollo Engineering and Technology Index*, Corporate Author Index, identifies a separate Grumman record under contract `NAS9-1100`:

- report: `LMA-790-2-LMS`;
- issue date: **1 July 1967**;
- MSC accession: **67-16127**;
- title/content: **LM Mission Simulator Instructors Handbook, Vol. 2 — Simulator Operation, Section 7 — Simulator Output Tables**.

Primary source: NASA/MSC *Apollo Engineering and Technology Index*, Corporate Author Index, Grumman Aircraft Engineering Corp. entries, public scan at `https://www.ibiblio.org/apollo/NARASWoverflow/CorporateIndex.pdf`.

The same index's citation key defines this date field as **Issue date: day, month, year**.

## Interpretation boundary

This establishes that Section 7 has its own accession and a **1 July 1967 issue date**, distinct from the April 1967 adjacent handbook records. It therefore should be retrieved and effectivity-controlled as a separately issued handbook section rather than silently treated as part of the April Volume II issue set.

It does **not** establish what individual output tables contain, which machine generated an output, how outputs were routed, whether later revisions existed, or whether the July 1967 tables remained unchanged through Apollo 13.

## Repository consequence

- Keep `67-16127` as the exact primary retrieval key for Section 7.
- Preserve **1 July 1967** as its source-backed issue date.
- Do not merge its effectivity with the 1 April / 15 May 1967 metadata conflict for `67-14186` and `67-14187`.
- Prioritize direct Section 7 recovery after the blocked Volume I identity attempt because it is the strongest unresolved source for simulator-output ownership/interface mapping.
- Align roadmap and source-catalog retrieval order so Section 7 precedes the Section 2/3 archival-folder requests.

No station maturity, processor allocation, output routing, causal-engine constant, or runtime behavior changes from this bibliographic result alone.
