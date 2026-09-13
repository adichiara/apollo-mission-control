# Station research status addendum — multi-station player ownership

Date: 2026-09-12

## Status

The compact-mode domain implementation now preserves original Apollo station identity under shared human ownership.

### LM SYSTEMS project role

Human player ownership may include:

- TELMU
- CONTROL

The software continues to treat TELMU and CONTROL as separate stations for products, presentations, readiness, actions, and audit provenance.

### FLIGHT DYNAMICS project role

Human player ownership may include:

- GUIDO
- FIDO/RETRO

The software continues to treat GUIDO and FIDO/RETRO as separate stations for products, presentations, readiness, actions, and audit provenance.

### Independent roles retained

- FLIGHT
- CAPCOM
- INCO

No change has been made to their historical responsibility boundaries.

## Historical confidence

No station research grade changes are implied by this implementation. The compact player labels remain modern project abstractions constrained by primary Apollo 13 organizational evidence.

The primary-source basis remains:

- Apollo 13 Press Kit;
- Apollo 13 Review Board Appendix A / Mission Control organization material;
- Apollo 13 Mission Operations Report controller appendices.

## Remaining station-interface work

- HTTP/API station-set join/rejoin;
- bundled browser navigation while retaining original call signs;
- station-qualified action controls in compact mode;
- live compact-mode validation after the seven-seat baseline.

Four-player-or-smaller aggregation remains unresolved.

See:

- `resources/research/091_low_player_count_station_aggregation_boundary.md`
- `resources/research/092_multi_station_player_ownership.md`
- `resources/source-catalog/PC2_LOW_PLAYER_COUNT_SOURCES.md`
