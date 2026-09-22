# Progress — Apollo 11 P66 decision-gate integration

Date: 2026-09-21

## Completed

- Rechecked the implementation boundary against primary NASA sources rather than adding a new historical assumption.
- Added explicit automatic/manual descent control mode to the reusable Apollo 11 descent decision-gate contract.
- Added a derived rule-applicability output: trajectory/guidance constraints may themselves cause abort before crew takeover, but not after manual takeover under Apollo 11 Flight Mission Rule 5-11.
- Preserved the landing-radar/controller observation object unchanged across that transition.
- Added regression coverage proving observation continuity and authority change are separate.
- Updated the powered-descent source-catalog addendum and station-status/roadmap records.

## Files changed

- `src/apollo_mission_control/descent_decision_gate.py`
- `tests/test_descent_decision_gate.py`
- `resources/APOLLO11_POWERED_DESCENT_PHASE_SOURCE_CATALOG_ADDENDUM.md`
- `docs/roadmap/2026-09-21_apollo11_p66_decision_gate_integration.md`
- `docs/progress/2026-09-21_apollo11_p66_decision_gate_integration.md`
- `docs/station-status/2026-09-21_apollo11_p66_decision_gate_integration.md`

## Guardrail

This implementation does not convert P66 into an automatic event detector. The exact ground indication of crew takeover remains unresolved. Callers must supply the control mode from a separately sourced scenario/event layer. No trajectory departure automatically creates an abort or FLIGHT decision.

## Site-facing completion

The Causal Model Lab now accepts explicit automatic/manual control mode and includes
an **Automatic / manual authority comparison** action. The paired proof holds the
landing-radar observation, Guidance/CONTROL readiness, FLIGHT state, and CAPCOM relay
constant while changing only control mode.

The UI exposes the resulting
`trajectory_guidance_abort_constraints_applicable` change without creating an
automatic abort/continue decision.

## Next

Return to the next unresolved powered-descent controller-product dependency. Keep
exact Mission-G P66 annunciation and voice details deferred unless they become
player-decision critical.

## Evidence status

- **DOCUMENTED / PRIMARY:** rule 5-11 and continued ground monitoring.
- **IMPLEMENTED:** domain contract and regression test.
- **IMPLEMENTED:** site-facing automatic/manual paired proof.
- **UNRESOLVED BUT NOT REQUIRED:** exact Mission-G P66 ground indication/keying and unique station voice call.