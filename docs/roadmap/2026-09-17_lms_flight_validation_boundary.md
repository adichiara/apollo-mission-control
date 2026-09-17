# Roadmap addendum — LMS flight-derived validation boundary

Date: 2026-09-17

## Current state

Formal LMS numerical acceptance/correlation criteria remain unrecovered. RG 255 E.155B1 and the surviving `1L5-102-(H)` lineage remain the main archival targets.

Research note 234 adds a complementary primary-source validation layer from the Apollo 14 Mission Report:

- LMS steering equations and torque-to-inertia behavior were reported as nearly identical to the flown LM;
- simulator visual-display fidelity was credited in landing-site recognition and landing training.

## Roadmap consequence

Future LMS model recovery should be evaluated on two distinct tracks:

### Track 1 — engineering acceptance/correlation

Recover and preserve source-defined:

`configuration → reference input → simulator output → reference output → tolerance/criterion → result`

This track is required before historical numerical tolerance claims or D-022 intervals are allowed.

### Track 2 — flight-derived operational cross-check

For domains explicitly compared with flight, preserve:

`simulator behavior → operator expectation/training → flown behavior → postflight comparison`

Use this to confirm model-domain relevance and broad behavioral fidelity. Do not manufacture numerical limits from qualitative language.

## Priority order

1. Continue E.155B1 / acceptance-procedure recovery.
2. Recover LMS steering / equations-of-motion / weight-and-balance interfaces at configuration/effectivity level.
3. Cross-check recovered model structure against Apollo 14's flight-derived steering/torque-to-inertia comparison.
4. Recover visual-system acceptance/configuration material separately; cross-check against Apollo 14's postflight visual-fidelity statement.
5. Only after source-defined numerical ranges appear, apply D-022 sensitivity testing.
