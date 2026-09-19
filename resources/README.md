# Research Resources

This directory is the provenance layer for the simulation.

## Structure

- `PRIMARY_SOURCE_CATALOG.md` — master navigation catalog for identified source documents and every scoped source-catalog supplement.
- `RESEARCH_INDEX.md` — master navigation index for every research note.
- `source-catalog/` — scoped implementation/scenario source ledgers. They remain detailed local catalogs and are indexed from the master catalog rather than duplicated wholesale into it.
- `research/` — project research notes derived from sources.
- `audits/` — dated verification reports, evidence ledgers, withdrawn-claim controls, and the legacy research-metadata baseline.
- `primary-sources/` — local primary-source copies when mirroring is appropriate and legally/permanently practical.

Run `python3 scripts/update_research_indexes.py` after adding, renaming, or deleting a research note or source-catalog supplement. `scripts/audit_documentation.py` fails when either master index no longer covers the tree.

Use `python3 scripts/query_research.py` to retrieve across the current corpus without pretending the legacy prose has already been normalized. Useful filters include `--text`, `--evidence DOCUMENTED|PARTIALLY DOCUMENTED|UNRESOLVED|UNLABELED`, and `--source-heading canonical|legacy|mixed|none`; add `--json` for machine-readable output. `UNLABELED` is metadata state, not an evidence conclusion.

## Research-note conventions

The repository accumulated several headings for the same retrieval function. New research notes use one vocabulary:

- `## Sources` — source references, document identities, URLs, pages/sections, and provenance.
- `## Evidence status` — explicit claim-scoped evidence labels.
- `## Findings` — source-derived findings when a separate findings section is useful.
- `## Unresolved` — remaining gaps when a separate unresolved section is useful.

Do not create new variants such as `Primary source`, `Primary sources`, `Primary evidence`, `Primary-source findings`, or singular `Source`. Existing notes may retain legacy headings until they are substantively revisited.

The formal evidence labels are exactly those in `docs/PROJECT_PRINCIPLES.md`:

- **DOCUMENTED** — directly supported by source material.
- **PARTIALLY DOCUMENTED** — some required details are supported; others remain unresolved.
- **UNRESOLVED** — documentation has not yet been found or is insufficient.

A note may legitimately contain more than one label because different claims can have different evidentiary states. Put the label in `## Evidence status` with enough text to identify the claim scope; do not reduce a mixed note to a single overall rating.

The pre-standard corpus is listed in `audits/research_metadata_legacy.json`. That file is a formatting exemption only. It does not assign an evidence status. Do not bulk-backfill evidence labels from prose, filenames, another agent's summary, or the existence of a citation. Reopen the underlying source before adding or upgrading a formal label.

## Source-catalog status labels

Source-review status is separate from historical claim status. Use these labels where helpful:

- **IDENTIFIED** — source found but not yet reviewed in sufficient detail.
- **REVIEWED-PARTIAL** — relevant portions reviewed.
- **REVIEWED** — reviewed for the research question being documented.
- **IMPLEMENTATION-SOURCE** — currently used to justify a simulation implementation.

A source being listed or reviewed does **not** make every claim derived from it `DOCUMENTED`.

## Research rule

Research notes should identify the specific document and, where practical, page/section used. When sources conflict, record the conflict rather than silently selecting one. Unresolved details remain explicit until a source or project decision closes them.

## Local source files

The repository currently catalogs authoritative documents by stable NASA/NTRS or archival URLs. Whether full PDFs should also be mirrored under `primary-sources/` remains intentionally undecided; see `docs/OPEN_QUESTIONS.md`.

If files are mirrored later, retain source metadata and original filenames where practical.
