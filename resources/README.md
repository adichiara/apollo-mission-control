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
- `source-catalog/PC2_RESTART_SOURCES.md` — mission-specific sources for the premature DPS shutdown/restart branch and the distinction between rule-caused shutdown and restart-eligible unexplained shutdown.
- `source-catalog/PC2_DPS_RESTART_RESPONSE_SOURCES.md` — mission-specific and contemporary sources for separating an eligible restart procedure from the successful physical engine-on response.
- `source-catalog/PC2_DELTA_P_CALLOUT_SOURCES.md` — mission-specific sources for the ground-only fuel/oxidizer ΔP >25 psi shutdown callout and crew-response path.
- `source-catalog/PC2_DPS_SHUTDOWN_RESPONSE_SOURCES.md` — contemporary LM sources for crew STOP-pushbutton control, engine-off command routing, and DPS valve-response semantics.
- `source-catalog/PC2_DPS_SHUTDOWN_CONFIRMATION_SOURCES.md` — mission-specific and contemporary evidence for crew voice shutdown report plus fresh GQ6510P chamber-pressure observation as distinct response-evidence channels, without an invented engine-off threshold.
- `source-catalog/PC2_CONTROL_PRESENTATION_SOURCES.md` — mission-specific Apollo 13 MSK 1123/1137 and PC+2 operational sources constraining the first player-facing CONTROL rendering.
- `source-catalog/PC2_GUIDO_PRESENTATION_SOURCES.md` — mission-specific Apollo 13 MSK 1123/1137, LUMINARY 1C R-567, and PC+2 operational sources constraining the first player-facing GUIDO rendering.
- `source-catalog/PC2_TELMU_PRESENTATION_SOURCES.md` — mission-specific PC+2 chronology, TELMU post-mission, Review Board, and inverter-rule sources constraining the first player-facing TELMU rendering.
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
