# Roadmap continuation — Apollo 11 P66 decision-gate integration

Date: 2026-09-21
Parent: `docs/roadmap/2026-09-21_apollo11_p66_manual_landing_monitoring.md`

## Bounded implementation question

Can the already-sourced P66/manual-takeover boundary be represented in the reusable descent decision gate without inventing a ground indication, voice call, or automatic abort decision?

## Primary-source constraint

Apollo 11 Flight Mission Rule 5-11 (16 July 1969) states that after crew takeover of powered descent, trajectory or guidance constraints are not cause for abort. NASA TM X-58038 independently shows that ground guidance monitoring/comparison continued into terminal descent/manual landing. The Apollo 11 Mission Report describes P66 as a crew-initiated manual landing mode while computer functions remained involved.

Therefore the correct reusable state transition is:

`observations available + automatic control + trajectory/guidance abort constraints applicable`

→ **crew takeover / P66** →

`observations still available + manual control + trajectory/guidance abort constraints not themselves abort causes`

This transition says nothing about independently sourced systems or propellant abort criteria.

## Implementation result

`src/apollo_mission_control/descent_decision_gate.py` now carries an explicit `DescentControlMode` (`automatic` / `manual`). The serialized contract exposes `trajectory_guidance_abort_constraints_applicable`.

The flag is derived only from the sourced control-mode boundary. It does not infer a FLIGHT decision, erase landing-radar/controller observations, or alter CONTROL/GUIDANCE readiness.

`tests/test_descent_decision_gate.py` now verifies that the same controller-visible LR observation survives the automatic→manual transition while trajectory/guidance abort-rule applicability changes.

## Deliberate non-claims

- no exact Mission-G CRT/PBI/DRK field for P66 entry;
- no invented GUIDANCE call announcing P66;
- no automatic abort/continue decision;
- no claim that systems/propellant criteria cease after takeover;
- no exact continuous flown trajectory generated from this state transition.

## Status

**SUFFICIENT / IMPLEMENTED at the domain-contract layer.**

The existing HTTP/model-lab endpoint still defaults to the pre-existing automatic-mode contract because its request schema has not yet been extended to select manual mode. That site-facing extension is the next implementation step; it should expose the same two-mode proof without adding new historical claims.

## Next

1. Extend the site-facing descent-decision-gate proof to accept/display `control_mode`.
2. Add automatic-vs-manual paired cases demonstrating unchanged observations and changed rule applicability.
3. Then return to the next unresolved powered-descent controller-product dependency rather than expanding P66 detail that is not player-decision critical.

## Evidence status

- **DOCUMENTED / MISSION RULE:** post-takeover trajectory/guidance constraints are not abort causes.
- **DOCUMENTED / PRIMARY TECHNICAL ACCOUNT:** monitoring/comparison continues through terminal descent/manual takeover.
- **IMPLEMENTED:** reusable decision-gate authority boundary.
- **OPEN IMPLEMENTATION:** site-facing model-lab selector/display.
- **DEFERRED:** exact P66 ground annunciation/keying/voice detail unless a player-facing dependency makes it material.