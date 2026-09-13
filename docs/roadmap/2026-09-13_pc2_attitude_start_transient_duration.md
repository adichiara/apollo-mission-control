# Roadmap addendum — PC+2 attitude start-transient duration

Date: 2026-09-13

## Resolved research boundary

Research note 110 closes the current archival pass on the exact duration of the PC+2 attitude-error “start transient” exception without inventing a numeric gate.

Primary Apollo DPS engineering evidence establishes that “start transient” refers to a short engine-start phenomenon, not the complete 26-second commanded low-thrust buildup. However, no reviewed Apollo 13 operational source defines the flight-rule exception’s exact duration or end condition. Cross-mission Apollo 14/15/16 engine-performance timings therefore remain corroborating engineering context only.

## First-playable rule

- retain the note-109 rule allocation: ±10-degree attitude error carries the exception;
- do not implement a historical 2.14 s, 4.0 s, +5 s, +21 s, or +26 s exception timer;
- exception-dependent attitude-error cases remain `NOT_EVALUABLE` unless an Apollo 13-specific source or explicitly synthetic scenario event defines the boundary;
- nominal PC+2 does not require this unresolved timing to reproduce its sourced outcome.

## Priority

This refinement does not change the canonical first-playable priority order. The next blocking work remains:

1. seven-seat physical human/device nominal PC+2 validation through immediate post-burn transition;
2. synthetic ΔP branch physical validation;
3. five-player compact physical validation;
4. reopen archival/technical research only when a concrete validation incident or selected scenario requires it.

## Canonical references

- `resources/research/109_pc2_attitude_start_transient_scope.md`
- `resources/research/110_pc2_attitude_start_transient_duration_boundary.md`
- `resources/source-catalog/PC2_ATTITUDE_SOURCES.md`
- `docs/ROADMAP.md` (canonical roadmap; this addendum narrows its currently deferred start-transient item)
