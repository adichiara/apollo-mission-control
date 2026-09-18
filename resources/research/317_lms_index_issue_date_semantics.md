# Research note 317 — LMS index issue-date semantics

Date: 2026-09-18  
Status: **PRIMARY NASA/MSC INDEX SCHEMA RESOLVES THE DATE FIELD AS ISSUE DATE; THE APRIL/MAY CONFLICT REMAINS.**

## Question

Research 316 localized conflicting dates for `LMA-790-2-LMS` accessions `67-14186` and `67-14187` within NASA/MSC bibliographic control. Are those dates merely generic catalog dates, or does the index itself define what the field means?

## Result

The original NASA/MSC *Apollo Engineering and Technology Index, Volume I — Corporate Author Index* explicitly defines the citation fields in its `TYPICAL CITATION` key. Field 2 is labeled **“Issue date: day, month, year.”**

Accordingly, the dates attached to the Grumman `LMA-790-2-LMS` entries are not semantically undefined catalog dates in this index system. They are represented by NASA/MSC as **issue dates**:

- original Corporate Author Index: `67-14186`, `67-14187`, and `67-14188` — **01-04-67**;
- Corporate Author Index Supplement: `67-14186` and `67-14187` — **15-05-67**;
- original Corporate Author Index: `67-16127`, Section 7 — **01-07-67**.

This corrects the narrower wording in research 316 that declined to assign even an issue-date meaning to the April/May fields. The source itself supplies that meaning.

## What this does — and does not — resolve

### Resolved

- Within the NASA/MSC AETI citation schema, the disputed field is explicitly an **issue date**.
- The April/May discrepancy is therefore a conflict between two NASA/MSC **issue-date records**, not an ambiguity between possible issue/receipt/accession/catalog dates.

### Still unresolved

The index does **not** explain why the same accession records later carry a different issue date. Do not infer that:

- 15 May is a revision or reissue date;
- 1 April is a draft date;
- either date is a receipt or accession-processing date;
- the handbook technical content changed between those dates;
- the May record supersedes the April technical configuration;
- either record establishes Apollo 13 effectivity.

Those questions still require title/revision pages, document-control records, or surviving handbook copies.

## Retrieval consequence

Retain both dates as retrieval keys, but label them accurately as **conflicting NASA/MSC issue-date metadata**. When a physical/digitized candidate is recovered, compare its title page, revision page, and document-control markings directly against both records.

## Simulator consequence

None. No processor allocation, station maturity, malfunction behavior, model constant, runtime profile, or Apollo 13 configuration changes.

## Primary source

NASA/MSC, *Apollo Engineering and Technology Index, Volume I — Corporate Author Index*. The front-matter `TYPICAL CITATION` key labels field 2 `Issue date: day, month, year`; the Grumman entries list `LMA-790-2-LMS` accessions `67-14186`, `67-14187`, `67-14188`, and `67-16127` with the dates above.

Related: research 316, which localized the discrepancy but left the date-field semantics unnecessarily open.
