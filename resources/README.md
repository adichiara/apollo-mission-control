# Research Resources

This directory is the provenance layer for the simulation.

## Structure

- `PRIMARY_SOURCE_CATALOG.md` — master index of identified source documents.
- `source-catalog/` — small implementation/scenario-specific catalog supplements that are part of the active source index and should be folded into the master catalog during comprehensive catalog maintenance.
- `research/` — project research notes derived from sources.
- `audits/` — dated verification reports and file-by-file evidence ledgers.
- `primary-sources/` — reserved for local copies of primary documents when the project decides that mirroring is appropriate and legally/permanently practical.

Current supplements:

- `source-catalog/PC2_IMPLEMENTATION_SOURCES.md` — sources used directly by the Apollo 13 PC+2 executable product-projection, shutdown-rule, and scenario-injection layers.
- `source-catalog/PC2_INLET_PRESSURE_SOURCES.md` — focused source record for the unresolved singular inlet-pressure selection/aggregation question.
- `source-catalog/PC2_INVERTER_WARNING_SOURCES.md` — focused source record for the inverter-caution, crew-switch, and post-switch mission-rule path.
- `source-catalog/PC2_THRUST_MONITOR_SOURCES.md` — focused source record for the unresolved onboard 77-percent thrust-monitor indication and rejected unsupported mappings.
- `source-catalog/PC2_ATTITUDE_SOURCES.md` — focused source record for PC+2 attitude-error/rate criteria, the startup-transient source conflict, and CONTROL observation provenance.
- `source-catalog/PC2_FRESHNESS_SOURCES.md` — focused source record for observation age, data validity, and the unresolved absence of a PC+2-specific stale-data threshold.
- `source-catalog/APOLLO13_GROUND_PRODUCT_INTEGRITY_SOURCES.md` — mission-specific sources for the post-MCC-5 RTCC/AGS body-angle processing error and the distinction between product availability/validity and hidden data integrity.

## Research rule

A source being listed here does **not** mean every statement in it has been validated or implemented. Research notes should identify specific sections/pages used.

When a source conflicts with another source, record the conflict rather than silently selecting one.

## Source status

Use these labels where helpful:

- **IDENTIFIED** — source found but not yet reviewed in sufficient detail.
- **REVIEWED-PARTIAL** — relevant portions reviewed.
- **REVIEWED** — reviewed for the research question being documented.
- **IMPLEMENTATION-SOURCE** — currently used to justify a simulation implementation.

## Local source files

The repository currently catalogs authoritative documents by stable NASA/NTRS URL. Whether full PDFs should also be mirrored under `primary-sources/` is intentionally undecided; see `docs/OPEN_QUESTIONS.md`.

If files are mirrored later, retain source metadata and original filenames where practical.
