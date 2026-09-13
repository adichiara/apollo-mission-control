# Station status — Compact HTTP/browser integration

Date: 2026-09-13

## Status

**IMPLEMENTED; live compact usability validation pending.**

The compact client now presents multiple original station views to one modern player without merging the underlying station identities.

### LM SYSTEMS player

- TELMU remains TELMU.
- CONTROL remains CONTROL.
- The player switches explicitly between TELMU and CONTROL views.
- Readiness is attributed to the active original station.
- CONTROL-only actions/authorization appear and execute only as CONTROL.

### FLIGHT DYNAMICS player

- GUIDO remains GUIDO.
- FIDO/RETRO remains FIDO/RETRO.
- The player switches explicitly between the two views.
- Readiness remains station-qualified.

### FLIGHT, CAPCOM, INCO

Remain single-station roles in the approved compact configuration.

## Historical constraint

NASA Mission Control staffing material separately enumerates the relevant positions. The compact grouping is therefore documented as a simulator adaptation rather than historical staffing reconstruction.

## Evidence / documentation

- `resources/research/091_low_player_count_station_aggregation_boundary.md`
- `resources/research/092_multi_station_player_ownership.md`
- `resources/research/093_compact_http_browser_integration.md`
- `resources/source-catalog/PC2_LOW_PLAYER_COUNT_SOURCES.md`

## Remaining station-level validation

Physical play must determine whether substation switching is legible under time pressure and whether the player can maintain separate mental models for the bundled stations without hidden cross-station leakage. Any resulting usability issue must not be converted into an invented Apollo procedure.
