# Roadmap addendum — negative flight-derived validation and AGS verification architecture

Date: 2026-09-17

## Current state

Flight-derived validation now includes both favorable and unfavorable simulator comparisons.

Apollo 9 provides the first explicit negative boundary in this workstream: AGS range/range-rate information degraded much more rapidly in flight than in the simulator after radar updates, while pulse-mode control response in the same rendezvous context was reported as very similar to the mission simulator. The flight report also supplies an approximately ±3 ft/s AGS solution-variation magnitude, but the matching simulator-side value remains unrecovered.

NASA TN D-7990 now supplies the complementary Apollo-era verification architecture. It confirms layered equation, implementation, closed-loop, Monte Carlo, hardware-reference, and operational simulated-flight testing. Radar-filter simulated flight was an explicit test area, with criteria derived as value bounds or bounded curves for AEA/display parameters.

## Architecture consequence

Validation must be scoped to an observable behavior chain, not to a simulator as a monolith.

For navigation/filter/state-propagation models, preserve at least:

`measurement/update → state correction → propagation interval → displayed/derived error growth`

A model may match the update event and still be historically wrong during the propagation interval.

The project validation contract is now documented in `docs/VALIDATION_EVIDENCE_MODEL.md`. It preserves separate evidence layers rather than reducing all checks to a single pass/fail flag.

## Priority retrieval

1. Apollo 9 Mission Report Supplement 3, *LM Abort Guidance System Postflight Analysis Report* — recover quantitative explanation of rendezvous state-error growth and identify the flight-side comparison observables.
2. Recover the TN D-7990 radar-filter simulated-flight procedure's actual value bounds/bounded curves, not merely the statement that such criteria existed.
3. Crosswalk Apollo 9 software/AGS configuration to the applicable preflight radar-filter test case and simulator/test facility.
4. Identify whether LMS/AGS integration or acceptance records preserve the same radar-update/propagation test case.
5. Recover simulator configuration/effectivity before mapping the Apollo 9 mismatch onto Apollo 13 H-2.
6. If same-input simulator and flight/reference trajectories are recovered, evaluate whether D-022 becomes applicable at the relevant player-product resolution.
7. Continue formal LMS acceptance/correlation retrieval from RG 255 E.155B1 independently of the AGS software-verification workstream.

## Evidence rule

Future validation reports should explicitly classify each comparison as:

- representative/favorable;
- mismatch/negative;
- training-transfer only;
- unresolved/not comparable.

Engineering evidence should additionally state whether it is:

- equation/model verification;
- implementation equivalence;
- closed-loop causal integration;
- ensemble/statistical performance;
- independent/hardware reference;
- operational bounded-observable checkout.

Do not average these into a single overall simulator-fidelity score.

## Cadence rule

The 20-ms AEA computing-cycle evidence in TN D-7990 remains AGS-specific. It does not supersede or merge with the LMS 50-ms AACS integration-step study and is not a global simulation cadence.
