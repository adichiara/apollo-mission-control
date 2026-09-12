# Progress — PC+2 onboard thrust-monitor research

Date: 2026-09-12

## Research completed

Added `resources/research/061_pc2_onboard_thrust_monitor_observation_path.md`.

Primary mission evidence confirms the crew-side PC+2 shutdown criterion as a **thrust monitor readout of 77 percent or below**, distinct from the ground 85-psi chamber-pressure criterion.

The pass tested three plausible implementation mappings and rejected all three as currently unsupported:

1. **LGC P47** — Apollo guidance documentation identifies P47 as “Thrust Monitor,” but PC+2 was executed in P40 and no reviewed procedure states that the 77-percent rule used P47.
2. **LM thrust-to-weight indicator** — NASA technical material establishes this as an accelerometer/thrust-to-weight display in lunar-gravity terms, not a percent-thrust display.
3. **Ground `GQ6510P` chamber pressure** — the Mission Operations Report explicitly treats the ground 85-psi and onboard 77-percent criteria separately.

The exact onboard percent-thrust readout/source therefore remains unresolved.

## Implementation decision

`crew_thrust_monitor` remains `NOT_EVALUABLE`.

No synthetic crew percent-thrust gauge, P47 mapping, thrust-to-weight conversion, ground-pressure alias, or startup applicability time gate has been added.

This is an explicit implementation gap, not a claim that Apollo 13 lacked the crew indication historically.

## Documentation updated

- `resources/research/061_pc2_onboard_thrust_monitor_observation_path.md`
- `resources/source-catalog/PC2_THRUST_MONITOR_SOURCES.md`
- `docs/station-status/2026-09-12_pc2_thrust_monitor.md`
- `docs/ROADMAP.md`

## New stopping point

Proceed to the **attitude-error / attitude-rate PC+2 shutdown criteria**, focusing first on the documented source conflict over which criterion carries the startup-transient exception.

The goal is not merely to choose wording. The next pass should establish:

- what crew/onboard attitude-error and body-rate quantities were available during P40;
- what ground/controller products represented them;
- whether flight rules/checklists resolve the Mission Operations Report vs air-ground readback difference;
- whether the start-transient exception can be implemented without inventing a duration.
