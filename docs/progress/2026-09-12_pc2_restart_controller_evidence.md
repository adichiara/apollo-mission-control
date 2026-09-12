# Progress — PC+2 controller evidence after DPS restart

Date: 2026-09-12

## Completed

- Researched the minimum controller-visible evidence after a successful contingency DPS restart.
- Reused the existing LM-7-family `GQ6510P` thrust-chamber-pressure path rather than creating a scenario-specific confirmation product.
- Documented the negative finding that no reviewed primary/contemporary source establishes a dedicated `RESTART CONFIRMED` ground discrete, restart-only pressure threshold, required crew success report, or fixed confirmation latency.
- Added `resources/research/072_pc2_restart_controller_evidence.md`.
- Confirmed that no runtime code change is needed: the common CONTROL chamber-pressure product already preserves observation timing and can accept a fresh post-restart sample when a scenario supplies one.

## Architecture rule

A physical restart does not fabricate telemetry. A pre-restart chamber-pressure sample cannot be reused as fresh restart evidence, and a pressure value remains an observation rather than hidden engine-state truth.

## Next work

Move away from DPS transient detail and begin the first-pass player-facing CONTROL information presentation using already-researched PC+2 products. Exact historical CRT routing should be used where known and explicitly labeled as unresolved/project-rendered where it is not.