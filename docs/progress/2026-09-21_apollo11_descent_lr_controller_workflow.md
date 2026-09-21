# Progress — Apollo 11 descent LR controller workflow

Date: 2026-09-21

Continued the open Apollo 11 powered-descent reference from mission-rule semantics into the controller-visible landing-radar and landing-poll workflow.

## Completed

- Extended the Apollo-11-specific MSK-1137 inventory to the decision-relevant `ALT` and `TGO` fields alongside the already documented LR validity, velocity, and slant-range fields.
- Recovered a preserved 20 July 1969 Mission Control intercom segment from CONTROL Robert Carlton's console that assigns the LR-position-2 call to CONTROL and records Guidance as a separate FLIGHT poll response.
- Recorded the front-room chain from station readiness calls through FLIGHT integration to CAPCOM relay.
- Cross-checked the operational interpretation against Gene Kranz's independent account of ground landing-radar comparison/acceptance and Bales's back-room guidance support.
- Kept the crew air-ground LR-lock/`Delta-H`/P64 calls as corroboration rather than using them to invent internal station ownership.
- Closed this bounded controller-workflow question as **SUFFICIENT** under D-024.
- Preserved the existing **BLOCKED** status for exact Mission-G LR parameter provenance and engineering conversion.

## New/updated records

- `resources/research/502_apollo11_descent_lr_controller_call_workflow.md`
- `docs/roadmap/2026-09-21_apollo11_descent_lr_controller_workflow.md`
- `docs/station-status/2026-09-21_apollo11_descent_lr_controller_workflow.md`
- `resources/APOLLO11_DESCENT_TRAJECTORY_RULES_SOURCE_CATALOG_ADDENDUM.md`
- `docs/RESEARCH_PORTFOLIO_STATUS.md`

## Next

Define the implementation-neutral descent decision-gate contract that joins the existing LR/guidance causal state to the documented rule and station workflow without adding guessed historical constants, exact ground-processing ownership, or automatic controller decisions.

## Evidence status

- **DOCUMENTED:** player-relevant display ingredients and landing-poll decision topology.
- **PARTIALLY DOCUMENTED:** exact rule-input-to-display-field mapping.
- **BLOCKED:** Mission-G per-field LR ground-processing provenance.
- **DEFERRED:** exact GUIDO/back-room phraseology and timing.
