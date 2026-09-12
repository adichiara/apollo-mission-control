# Progress — PC+2 observation age/freshness

Date: 2026-09-12

## Completed

- Researched whether the PC+2 shutdown rules or contemporaneous crew-facing read-up define a generic analog-observation freshness, persistence, or repeat-confirmation requirement.
- Found no explicit time-based freshness threshold in the reviewed mission-specific primary sources.
- Added research note `064_pc2_observation_age_and_freshness.md` and source catalog `PC2_FRESHNESS_SOURCES.md`.
- Preserved a key distinction between observation/sample time and later projection/display/evaluation time.
- Corrected the implementation contract so a carried-forward injected analog value does not acquire a new source/sample timestamp merely because it is projected later.
- Added observation-age reporting to rule-audit evidence without assigning a fabricated `STALE` threshold.
- Kept source-specific confirmation semantics separate: the inverter warning still requires a distinct post-switch observation because that ordering is supported by the mission rule wording.
- Updated CONTROL/TELMU/GUIDO/CAPCOM/FLIGHT station-status documentation; maturity remains B.

## Historical boundary

The absence of a discovered stale-data timeout is not evidence that Apollo controllers accepted arbitrarily old measurements. It means the current source package does not support encoding a numeric timeout. Age is therefore retained and exposed, while historical acceptability remains procedure-specific and unresolved.

## Next stopping point

Use the new timestamp/age model to research and implement the first **data-validity degradation path** that can be source-backed without inventing a failure: e.g. loss/freeze/questionable telemetry or a documented ground-processing validity problem affecting a PC+2-relevant product. Prefer a mission-specific Apollo 13 example; otherwise keep the behavior generic and clearly architectural.
