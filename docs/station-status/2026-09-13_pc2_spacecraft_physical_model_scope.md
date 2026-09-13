# Station-status addendum — PC+2 spacecraft physical-model scope

Date: 2026-09-13  
Parent: `docs/STATION_RESEARCH_STATUS.md`

Historical maturity grades remain unchanged. Research note 102 changes simulator scope, not the strength of station evidence.

## CONTROL

Requires causal DPS/source-observation state sufficient for chamber pressure, fuel/oxidizer pressure/ΔP, shutdown/restart response, and sourced attitude/rate products. No complete engine thermofluid model is implied.

## GUIDO

Requires guidance/load state, attitude/error/rate state, maneuver result/residual state, and the already modeled load/uplink workflow. Full six-degree-of-freedom dynamics are not yet required.

## FIDO/RETRO

Requires maneuver-target/result and trajectory-product state sufficient for the selected PC+2 workflow. A full RTCC propagator remains deferred until a sourced controller decision depends on it.

## TELMU

Requires coarse electrical configuration/equipment-availability state sufficient for maneuver power-up, inverter-related evidence, and post-burn partial power-down. Detailed breaker/wire/battery chemistry is not required for the current slice.

## INCO

Requires communications, telemetry, ranging, and uplink availability/state where those affect the selected workflow. Detailed RF propagation/modulation is deferred.

## FLIGHT / CAPCOM

Continue to consume station-derived readiness, maneuver, communications, and crew-response information rather than hidden physical truth. No omniscient spacecraft state is added.

## Boundary

Deferred LM/CSM subsystem physics remain historically real. They are omitted only because no currently implemented PC+2 player decision depends on them. Any later sourced dependency reopens the relevant subsystem model.