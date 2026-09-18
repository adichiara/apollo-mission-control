# Research note 316 — LMS handbook date-control reconciliation

Date: 2026-09-18  
Status: **PRIMARY BIBLIOGRAPHIC DISCREPANCY NARROWED — 1 APRIL 1967 IS SUPPORTED BY THE ORIGINAL NASA/MSC CORPORATE INDEX; THE SUPPLEMENT RETAINS 15 MAY FOR TWO ENTRIES.**

## Question

The repository has preserved a date discrepancy for `LMA-790-2-LMS`: several NASA sources support 1 April 1967, while a NASA/MSC corporate-index record recovered later showed 15 May 1967. Can the discrepancy be localized more precisely without guessing which date represents issue, receipt, revision, or cataloging activity?

## Result

Yes.

The NASA/MSC **Corporate Author Index** itself lists three adjacent Grumman `LMA-790-2-LMS` records under `NAS9-1100`, all dated **01-04-67**:

- `67-14186` — Volume I, Simulator Description;
- `67-14187` — Volume II, Simulator Operation, Sections 1 and 4;
- `67-14188` — Volume II, Simulator Operation, Sections 5 and 6.

It separately lists:

- `67-16127` — Volume II, Section 7, Simulator Output Tables — **01-07-67**.

The separately published **Corporate Author Index Supplement** reproduces `67-14186` and `67-14187` but gives **15-05-67** for those two records. The currently recovered supplement excerpt does not establish a corresponding May date for `67-14188`.

This means the discrepancy is not simply “NASA bibliography versus corporate index.” It exists **within NASA/MSC bibliographic control**: the original corporate index supports 1 April, while the supplement gives 15 May for at least `67-14186` and `67-14187`.

## Evidence boundary

### Documented

- Original NASA/MSC Corporate Author Index: `67-14186`, `67-14187`, and `67-14188` are dated 1 April 1967.
- NASA/MSC Corporate Author Index Supplement: `67-14186` and `67-14187` are dated 15 May 1967.
- The 1969 NASA/MSC Mission F engineering memorandum independently cites Volume II Sections II and III as `LMA790-2-LMS`, dated 1 April 1967.
- NASA bibliography `GP-642` also supports the 1 April 1967 handbook date, as documented in research 311.

### Not documented

Do **not** infer that:

- 15 May is a revision date;
- 15 May is an accession/receipt date;
- 1 April is necessarily the physical issue date of every surviving section;
- Sections 2/3 share an MSC accession number with any neighboring section pair;
- the date discrepancy reflects a technical-content change;
- either date establishes Apollo 13 effectivity.

Only inspection of the handbook title/revision pages or associated accession/configuration records can establish what the two dates mean.

## Retrieval consequence

For archive/database searching, use **both dates** for `LMA-790-2-LMS`:

- `01-04-67` / `April 1, 1967`;
- `15-05-67` / `May 15, 1967`.

Do not reject a candidate solely because it carries one of these dates rather than the other.

The best direct closure remains recovery of the physical/digitized handbook title and revision pages, especially Volume I (`67-14186`) and the Avitabile Section 2/3 folders.

## Simulator consequence

None. This is bibliographic control only. No processor allocation, station maturity, malfunction behavior, model constant, or runtime profile changes.

## Sources

- NASA/MSC, *Corporate Author Index* (primary NASA/MSC bibliographic control), Grumman entries for `LMA-790-2-LMS`, including `67-14186`, `67-14187`, `67-14188`, and `67-16127`.
- NASA/MSC, *Corporate Author Index Supplement* (primary NASA/MSC bibliographic control), Grumman entries for `67-14186` and `67-14187`.
- Research 311 — NASA `GP-642` date corroboration.
- Research 313 — NASA/MSC `MSC-IN-CF-P-69-5` / `NASA-TM-X-64471` reference to Volume II Sections II/III.
