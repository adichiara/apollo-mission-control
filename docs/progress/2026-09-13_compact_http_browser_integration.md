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
- Added research note 093 and reconciled the low-player-count source catalog, roadmaps, station status, README, resource index, and D-018.
- Repaired a regression-test assumption that conflated successful CONTROL authorization with the separate requirement that shutdown evidence actually exist.

## Authenticity boundary

`LM SYSTEMS` and `FLIGHT DYNAMICS` remain modern simulator grouping labels. They are not added to the authoritative Apollo station list and are not represented as historical combined positions.

All readiness, actions, authorization checks, presentations, and audit provenance remain attached to TELMU, CONTROL, GUIDO, FIDO/RETRO, FLIGHT, CAPCOM, or INCO as applicable.

## Validation state

GitHub Actions run 59 on commit `ae569dff997c17b0f67546ea452f1706d34b693d` completed successfully after the compact CONTROL test correction. The current functional compact HTTP/browser implementation is therefore recorded as passing automated CI, including the repository's unit/integration and workflow validation path.

This is not a physical play-validation claim. Seven-seat and five-player compact real-device/human play remain unexecuted.

## Next

1. Perform the documented seven-seat live-device/human validation.
2. Perform a five-player compact live run with explicit observation of substation switching, readiness attribution, action provenance, and information isolation.
3. Reopen historical research only if those runs expose a concrete missing procedure, authority, information, or terminology dependency.
