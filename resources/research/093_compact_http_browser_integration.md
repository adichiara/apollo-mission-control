# 093 — Compact HTTP/browser integration boundary

Date: 2026-09-13  
Status: **IMPLEMENTED — transport/client support added; physical five-player validation still pending**

## Question

How should the already-approved five-player compact PC+2 configuration cross the HTTP/browser boundary without erasing the historically distinct Apollo station identities underneath it?

## Primary-source constraint

NASA Mission Control staffing material lists FIDO, RETRO, GUIDO, LM/TELMU, LM/CONTROL, INCO, FLIGHT DIRECTOR, and CAPCOM as distinct positions. The Apollo 13 mission/organization sources already cataloged in `PC2_LOW_PLAYER_COUNT_SOURCES.md` likewise distinguish their responsibilities even when stations belong to the same larger functional group.

Primary reference added/confirmed for this implementation pass:

- NASA Mission Operations Control Room flight-controller assignments, hosted by NASA History/ALSJ: `flight_controller_assigns.pdf`.
- It independently enumerates FIDO, RETRO, GUIDO, LM/TELMU, LM/CONTROL, INCO, CAPCOM, and FLIGHT leadership as separate positions.

This supports one implementation rule only: a compact UI may bundle access for a modern player, but must continue to expose and attribute the original station identities separately.

The source does **not** establish:

- a historical five-person Apollo 13 Mission Control configuration;
- a historical `LM SYSTEMS` or `FLIGHT DYNAMICS` combined console operator;
- any browser, HTTP, localStorage, tab-navigation, or rejoin behavior.

Those are explicitly modern simulator mechanics.

## Implementation

### HTTP

Added `/api/session/join-set` for exact station-set ownership while retaining `/api/session/join` for the existing single-station contract.

Rejoin is idempotent only when the same player submits the same ordered station set. A compact player cannot silently mutate its assigned set, and an original station cannot be owned by two players.

`GET /api/session/player/{player_id}` now returns:

- the legacy single-station snapshot for one-station players;
- a bundled snapshot with a `stations` list and separate `presentations` keyed by original call sign for multi-station players.

Readiness requests now accept an explicit original `station`. Multi-station players must qualify readiness by station.

CONTROL shutdown-evidence authorization now checks ownership of CONTROL rather than requiring a single-station player.

### Browser

The player client now offers the approved compact selections:

- `LM SYSTEMS — TELMU + CONTROL`;
- `FLIGHT DYNAMICS — GUIDO + FIDO / RETRO`.

These labels are identified in the UI as simulator conveniences.

Compact identity persistence stores the original station set and active substation. Existing v1 single-station localStorage identities are migrated on read.

A compact player navigates between original-station tabs. The active original call sign remains visible on the display and action surface. Readiness is submitted against that active station, and station-specific controls appear only while the corresponding original station is active.

No merged synthetic presentation was created.

## Tests added

`tests/test_web_compact_roles.py` covers:

- station-set join and bundled snapshots;
- exact-set rejoin;
- station-qualified readiness;
- cross-bundle station conflicts;
- CONTROL authority under compact ownership.

`tests/test_web_client_contract.py` now checks compact role definitions, v2 persistence, join-set transport, substation switching, and active-station readiness attribution.

## Remaining validation

Repository-level implementation is complete, but the compact configuration is not yet recorded as human-play validated.

Next compact-specific validation:

1. run CI against this head;
2. exercise five simultaneous browser/phone players using the approved compact configuration;
3. verify that switching between TELMU/CONTROL and GUIDO/FIDO-RETRO is legible under time pressure;
4. verify that readiness/actions remain correctly attributed in the facilitator audit;
5. log usability defects separately from historical/research defects.

The broader seven-seat live-device protocol remains the canonical physical validation requirement for the full station model.
