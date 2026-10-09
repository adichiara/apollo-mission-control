# Progress — Apollo 11 descent runtime adapter

Date: 2026-10-08

## Completed

The cataloged `apollo11_descent_v1` runtime adapter/fixture is now implemented as an architecture-testable runtime while remaining unavailable for live historical session creation.

The adapter:

- reuses `GenericScenarioSession` lifecycle, GET, station ownership, readiness, FLIGHT decision, CAPCOM queue/transmission, and audit behavior;
- binds the source-controlled Apollo 11 PDI GET and nominal powered-descent phase profile;
- opens the explicit `landing_go` gate at the nominal high-gate architecture anchor;
- maps the player-facing `GUIDO` station into the bounded Guidance-readiness input without creating a synthetic `GUIDANCE` player station;
- binds CONTROL separately;
- uses explicit CAPCOM GO/NO-GO action identifiers;
- composes the existing read-only Apollo 11 descent projection.

## Information boundary

The fixture's station views remain empty. Reference-event variables such as program number, alarm code, LR DATA GOOD, and update-enable state are internal scenario/reference state and are not projected into controller products automatically.

The bound `project_descent()` method requires these inputs separately:

- landing-radar controller state;
- controller-product values;
- guidance-computer state.

This preserves the existing rule that hidden onboard state cannot populate controller-visible products merely because the runtime knows it.

## Human-authority boundary

At the nominal high-gate architecture anchor:

`GUIDO readiness + CONTROL readiness -> FLIGHT decision -> CAPCOM relay`

remain separate explicit events.

Station GO calls do not create a FLIGHT decision. FLIGHT GO does not transmit through CAPCOM. The adapter test covers the complete chain using the actual catalog fixture.

The nominal high-gate scheduling is an architecture anchor, not a claim that the historical FLIGHT decision occurred at exactly that nominal time.

## Execution policy

Adapter availability and live execution are now distinct catalog states.

The Apollo 11 scenario has:

- `adapter_available = true`;
- `execution_enabled = true`;
- `execution_requires_validated_model = true`;
- `executable = false` while any required model domain is not validated.

PC+2 keeps its separately accepted partial-model prototype policy and therefore does not inherit this Apollo 11 execution gate.

## Next

Apply D-024 to the remaining Apollo 11 required model domains. Identify which partial/unresolved domains materially block historical execution at the current player/product resolution, rather than broadening the adapter or continuing open-ended research.
