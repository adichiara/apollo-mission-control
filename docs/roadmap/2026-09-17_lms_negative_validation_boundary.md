# Roadmap addendum — negative flight-derived validation

Date: 2026-09-17

## Current state

Flight-derived validation now includes both favorable and unfavorable simulator comparisons.

Apollo 9 provides the first explicit negative boundary in this workstream: AGS range/range-rate information degraded much more rapidly in flight than in the simulator after radar updates, while pulse-mode control response in the same rendezvous context was reported as very similar to the mission simulator.

## Architecture consequence

Validation must be scoped to an observable behavior chain, not to a simulator as a monolith.

For navigation/filter/state-propagation models, preserve at least:

`measurement/update → state correction → propagation interval → displayed/derived error growth`

A model may match the update event and still be historically wrong during the propagation interval.

## Priority retrieval

1. Apollo 9 Mission Report Supplement 3, *LM Abort Guidance System Postflight Analysis Report* — recover any quantitative explanation of rendezvous state-error growth.
2. Apollo Experience Report — LM Abort Guidance System — extract radar-filter verification methodology, error models, bounds/bounded curves, and simulated-flight criteria.
3. Identify whether LMS/AGS integration records preserve the corresponding radar-update/propagation test case.
4. Recover simulator configuration/effectivity before mapping the Apollo 9 mismatch onto Apollo 13 H-2.
5. If same-input simulator and flight/reference trajectories are recovered, then evaluate whether D-022 becomes applicable at the relevant player-product resolution.

## Evidence rule

Future validation reports should explicitly classify each comparison as:

- representative/favorable;
- mismatch/negative;
- training-transfer only;
- unresolved/not comparable.

Do not average these into a single overall simulator-fidelity score.
