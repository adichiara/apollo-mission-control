# Progress — model-profile catalog boundary

Date: 2026-09-14

## Completed

- Added a separate model-profile catalog for causal/numerical configuration readiness.
- Added explicit per-domain states: `unresolved`, `partial`, `validated`, and `not_applicable`.
- Added the first Apollo 13 H-2 model profile without inventing missing constants:
  - mass properties: partial;
  - propulsion: partial;
  - translational dynamics: unresolved;
  - tracking observation: unresolved.
- Added `model_profile_id` to scenario metadata.
- Session creation now verifies that a scenario's model profile belongs to its selected mission profile.
- Added `/api/model-profiles` and active model-profile/validation-state fields to session status.
- Added catalog and API tests.

## Consequence

The reusable simulator now has three distinct configuration concepts:

1. **mission profile** — historical mission-era configuration/nomenclature;
2. **model profile** — evidence/readiness state of executable causal/numerical domains;
3. **scenario** — exercise-specific initial conditions, chronology, objectives, and failures.

This makes it possible for multiple scenarios to share historical model configuration while preventing scenario fixtures from silently hard-coding unresolved physics.

## Boundary

The current model profile is metadata/readiness only. It does not yet inject numerical constants into the live runtime. That should happen domain-by-domain only when the required historical inputs are sufficiently sourced and validated.
