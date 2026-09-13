# Station-status addendum — PC+2 crew-action representation

Date: 2026-09-13  
Parent: `docs/STATION_RESEARCH_STATUS.md`

Historical station maturity grades are unchanged. Research note 105 clarifies the boundary between controller stations and spacecraft-crew execution.

## CAPCOM

CAPCOM remains the player-facing station through which ground instructions/procedures reach the crew in the first playable. The simulation must distinguish message preparation/transmission from crew receipt and action.

## FLIGHT and specialist controllers

FLIGHT, CONTROL, TELMU, GUIDO, FIDO/RETRO, and INCO may generate decisions, recommendations, products, or information that ultimately affect crew action, but they do not directly mutate crew or spacecraft state merely by reaching an internal conclusion.

## Crew boundary

The crew is not added as an eighth playable station for PC+2. Crew actions are scenario-authored external events with explicit receipt/action steps. Physical response and resulting telemetry/report evidence remain downstream and separate.

This is a project scope decision, not a claim that Apollo crews behaved deterministically or without discretion.

## Reopen condition

Reopen the crew-role boundary when a selected scenario depends on astronaut discretion, manual flying skill, competing onboard workload, ambiguous onboard observations, or detailed checklist execution that materially changes controller decisions.
