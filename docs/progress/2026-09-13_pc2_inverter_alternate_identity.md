# Progress — PC+2 alternate inverter identity

Date: 2026-09-13

## Completed

- Continued from research note 112's corrected mission-specific PC+2 inverter-2 selection.
- Rechecked the Apollo 13 air-ground rule at approximately 76:30–76:38 GET: the crew is to judge the inverter caution after `switching inverters` / `trying switching inverters`.
- Rechecked the primary LM Operations Handbook AC architecture: the LM has two identical redundant inverters.
- Combined those primary-source facts conservatively: with PC+2 explicitly starting on inverter 2, the only other redundant inverter identity is inverter 1.
- Added `resources/research/113_pc2_inverter_alternate_identity.md`.
- Updated the inverter source catalog and TELMU/CONTROL/CAPCOM station-status addendum.

## Canonical result

For first playable:

`PC+2 selected inverter 2 → inverter caution/light → switch to other redundant inverter (inverter 1) → observe caution again → if it remains, shutdown criterion satisfied`

This closes the **alternate identity** question. It does not claim recovery of the exact historical cockpit switch/circuit-breaker sequence for a hypothetical failure that did not occur.

## Still unresolved

- exact inverter-transfer switch/circuit-breaker chronology;
- any reset/dwell requirement before judging persistence;
- exact crew-member action allocation;
- exact TELMU/CONTROL telemetry/display routing and independent knowledge of switch position;
- exact controller call sequence for the hypothetical contingency.

These gaps remain non-blocking unless physical validation or later implementation makes them decision-relevant.
