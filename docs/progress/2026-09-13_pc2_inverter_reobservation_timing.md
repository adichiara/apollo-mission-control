# 2026-09-13 — PC+2 inverter re-observation timing boundary

## Completed

- Reviewed the Apollo 13 *LM Malfunction Procedures* INVERTER caution flowchart after note 114 recovered the inverter-2-to-inverter-1 transfer sequence.
- Confirmed that the flowchart proceeds from the transfer directly to the `INVERTER lt — off?` decision and does **not** specify a crew stopwatch interval or numeric persistence dwell.
- Cross-checked NASA TN D-6845, *Apollo Experience Report — Lunar Module Instrumentation Subsystem*, which documents LM-5-and-subsequent inverter-selection transient-inhibit behavior applicable to LM-7.
- Closed first-playable timing semantics as **fresh valid caution re-observation**, not a fabricated post-transfer timer.
- Preserved the remaining evidence limits: exact inhibit duration, exact telemetry/display latency, crew-member assignment, exact controller/CAPCOM wording, independent ground visibility of selector position, and the exact TELMU/CONTROL field remain unresolved.
- Added research note 115 and reconciled the inverter source catalog, open questions, canonical roadmap, and dated roadmap record.

## First-playable consequence

Canonical sequence:

`inverter-2 caution → sourced transfer to inverter 1 → selection transient handled by spacecraft caution/inhibit logic → fresh valid INVERTER caution observation → remains = shutdown criterion satisfied`

No arbitrary 1-second, 2-second, 5-second, or other persistence timer is authorized.

## Station consequence

TELMU and CONTROL remain maturity **B**. The new evidence improves the operational rule boundary but does not recover exact ground routing/display presentation or a numeric inhibit/display latency.

## Next work

Physical seven-seat nominal validation, synthetic ΔP validation, and five-player compact validation remain the principal unclosed first-playable PASS boundaries. Reopen inverter timing research only if physical play or a later scenario exposes a concrete dependency on exact inhibit/display latency.
