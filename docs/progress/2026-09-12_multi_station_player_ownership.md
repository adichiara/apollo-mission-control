# Progress — multi-station player ownership

Date: 2026-09-12

## Completed

Implemented the framework-neutral domain boundary required by D-018 / research note 091.

### Session ownership

- Added `PC2Session.assign_stations()` so one player may own one or more **original** station identities.
- Added `stations_for()` and `owns_station()` for explicit multi-station authorization.
- Preserved one-owner-per-original-station uniqueness.
- Retained the existing single-station `assign_station()` / `station_for()` path for seven-seat compatibility.

### Presentation and readiness

- Added `BundledPlayerSessionSnapshot` and `bundled_player_snapshot()`.
- Bundled snapshots contain separate station presentations keyed by original station name; no synthetic domain presentation is created.
- Multi-station readiness now requires an explicit component station, preventing one bundled GO/NO-GO response from silently standing in for two disciplines.

### Action authority / provenance

- FLIGHT, CAPCOM, and CONTROL action checks now test ownership of the original station rather than assuming one station per player.
- Audit actors remain the original controller identity (`FLIGHT`, `CAPCOM`, `CONTROL`, etc.).
- Compact role labels do not enter the authoritative station list.

### Compact configuration

Added `compact_roles.py` with the source-constrained five-player project mapping:

- FLIGHT
- CAPCOM
- LM SYSTEMS = TELMU + CONTROL
- FLIGHT DYNAMICS = GUIDO + FIDO/RETRO
- INCO

These are project player-role labels, not historical Apollo positions.

### Regression coverage

Added `tests/test_pc2_compact_station_sets.py` covering:

- complete/non-overlapping five-player station coverage;
- multi-station ownership;
- station uniqueness;
- separate bundled presentations;
- station-qualified readiness;
- original-station action authorization.

## Research reconciliation

Added research note `092_multi_station_player_ownership.md` after rechecking primary NASA Apollo 13 organizational sources. The evidence continues to support station separation and functional-group affinity, but does not establish the proposed five-player bundle as historical staffing.

Updated `PC2_LOW_PLAYER_COUNT_SOURCES.md` to distinguish completed domain ownership from still-pending HTTP/browser wiring.

## Current boundary

The framework-neutral domain model is ready for compact mode. The next implementation boundary is transport/client support:

1. allow HTTP join/rejoin to bind a player to an approved station set;
2. return bundled snapshots over the API;
3. persist compact role/station-set identity in the browser;
4. present substation panels/actions without hiding their original call signs;
5. add API/browser contract tests before any five-player live playtest.

The separate seven-seat physical playtest remains the primary live-validation baseline.

## Validation note

The new tests are committed but are not recorded as locally executed in this run because the container runtime still cannot resolve `github.com` for a checkout. Existing CI should be used to establish PASS/FAIL for the new head.
