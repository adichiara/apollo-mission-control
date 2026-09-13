# Progress — Compact HTTP/browser integration

Date: 2026-09-13

## Completed

- Rechecked the compact-role implementation boundary against NASA Mission Control staffing/organization sources before changing transport behavior.
- Added exact station-set HTTP join/rejoin via `/api/session/join-set` while preserving the single-station `/api/session/join` contract.
- Multi-station players now receive bundled snapshots with separate presentations keyed by original station call sign.
- Player snapshot polling works for both single- and multi-station ownership.
- Readiness can be explicitly station-qualified; bundled players cannot submit ambiguous readiness.
- CONTROL evidence authorization now recognizes a player who owns CONTROL inside a bundle.
- Browser client now exposes the approved five-player compact bundles, persists station sets and active substation, migrates legacy single-station identity, and provides original-call-sign substation navigation.
- Added compact HTTP regression tests and expanded browser contract tests.
- Added research note 093 and reconciled the low-player-count source catalog and canonical roadmap.

## Authenticity boundary

`LM SYSTEMS` and `FLIGHT DYNAMICS` remain modern simulator grouping labels. They are not added to the authoritative Apollo station list and are not represented as historical combined positions.

All readiness, actions, authorization checks, presentations, and audit provenance remain attached to TELMU, CONTROL, GUIDO, FIDO/RETRO, FLIGHT, CAPCOM, or INCO as applicable.

## Validation state

Implementation is committed. Do not record current-head CI as passing until the workflow completes successfully.

Physical five-player compact play has not been executed and is not claimed as validated.

## Next

1. Confirm current-head CI.
2. Perform the documented seven-seat live-device/human validation.
3. Perform a five-player compact live run with explicit observation of substation switching, readiness attribution, action provenance, and information isolation.
