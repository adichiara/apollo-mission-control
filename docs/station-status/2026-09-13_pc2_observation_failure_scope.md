# Station-status addendum — PC+2 observation integrity

Date: 2026-09-13  
Research basis: note 104

## Cross-station boundary

The PC+2 first playable now has an explicit observation-failure scope. No station receives a generic `telemetry failure` diagnosis or random instrumentation faults.

- **CONTROL / TELMU:** propulsion, pressure, electrical, and warning observations may differ from hidden physical state only through an explicitly modeled/sourced observation-path fault. Nominal PC+2 adds none.
- **GUIDO / FIDO-RETRO:** spacecraft telemetry integrity remains separate from RTCC/ground-product integrity.
- **INCO:** telemetry transport, ranging, uplink, and communications availability are data-path states, not automatic source-sensor failures.
- **CAPCOM:** crew voice reports remain an independent evidence channel that can corroborate or conflict with telemetry.
- **FLIGHT:** sees controller conclusions/status rather than a privileged diagnosis of which observation layer failed.

## Maturity effect

No station maturity grade changes. This work constrains cross-station data integrity and failure semantics rather than adding exact console/display evidence.

## First-playable consequence

The nominal seven-seat run should contain no newly invented sensor failure. Later nonnominal observation faults require a specific sourced or explicitly synthetic origin/effect and must preserve the layer where the fault occurs.
