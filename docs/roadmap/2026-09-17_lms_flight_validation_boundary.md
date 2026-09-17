# Roadmap addendum — LMS flight-derived validation boundary

Date: 2026-09-17

## Current state

Formal LMS numerical acceptance/correlation criteria remain unrecovered. RG 255 E.155B1 and the surviving `1L5-102-(H)` lineage remain the main archival targets.

Research note 234 adds a complementary primary-source validation layer from postflight mission reporting:

- Apollo 14 reports LMS steering equations and torque-to-inertia behavior as nearly identical to the flown LM and credits simulator visual-display fidelity in landing-site recognition;
- Apollo 17 independently records transfer of a trained outside/in-cockpit attention technique from LMS/LLTV practice into the actual landing and credits LMS training as part of preparation for the manual approach.

## Roadmap consequence

Future LMS model recovery should be evaluated on two distinct tracks:

### Track 1 — engineering acceptance/correlation

Recover and preserve source-defined:

`configuration → reference input → simulator output → reference output → tolerance/criterion → result`

This track is required before historical numerical tolerance claims or D-022 intervals are allowed.

### Track 2 — flight-derived operational cross-check

For domains explicitly linked to flight, preserve:

`simulator behavior/training technique → operator expectation/strategy → flown behavior/task → postflight comparison`

Use this to confirm model-domain relevance, broad behavioral fidelity, and operator-technique transfer. Do not manufacture numerical limits from qualitative language.

## Priority order

1. Continue E.155B1 / acceptance-procedure recovery.
2. Recover LMS steering / equations-of-motion / weight-and-balance interfaces at configuration/effectivity level.
3. Cross-check recovered model structure against Apollo 14's flight-derived steering/torque-to-inertia comparison.
4. Recover visual/display and operator-facing information-path material separately; cross-check against Apollo 14 visual-fidelity and Apollo 17 technique-transfer evidence.
5. Only after source-defined numerical ranges appear, apply D-022 sensitivity testing.
