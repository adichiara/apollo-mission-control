# Apollo 13 PC+2 — integrated session-orchestration boundary

Date: 2026-09-12  
Status: **REVIEWED / IMPLEMENTED-PARTIAL — authoritative single-process session now integrates scenario progression and station views; player-report/callout presentation and network delivery remain future work**

## Question

What is the minimum integrated session behavior required to connect the existing PC+2 station products into a playable multi-controller sequence without inventing Apollo workflow or exposing hidden simulator state?

## Primary-source first pass

### Final readiness / GO sequence

The contemporaneous PC+2 record preserves a useful ordering boundary:

- at approximately **78:57 GET**, Flight Director Gene Kranz tells the team he will go around the room near minus 10 minutes for a final GO/NO-GO;
- at approximately **79:17 GET**, the Flight Director is reported as going around the room for team status and the control room is reported GO for the burn;
- at **79:18:15 GET**, CAPCOM tells the crew, "you are Go for the burn";
- the crew acknowledges that instruction at 79:18:20.

The player model should therefore preserve at least three distinct operational events:

```text
controller readiness report(s)
        -> FLIGHT decision
        -> CAPCOM crew-facing transmission
```

The evidence does **not** justify replacing that sequence with an automatically computed overall readiness Boolean derived from authoritative subsystem state.

### During-burn continuation

The record also shows continuing Mission Control assessment during the burn and CAPCOM transmitting crew-facing continuation calls. This reinforces the same separation: controller/system assessment is not identical to the air-ground callout.

## Software boundary

This session layer is explicitly **project architecture**, not a reconstruction of Apollo MCC software internals.

It must own:

- authoritative session GET and scenario progression;
- station/player assignment;
- station-scoped presentation selection;
- controller readiness reports;
- explicit FLIGHT decisions;
- queued FLIGHT/controller callouts requiring crew transmission;
- CAPCOM-to-crew transmission events;
- ordered audit/replay events.

It must **not**:

- expose authoritative physical state directly to FLIGHT or CAPCOM;
- automatically infer a FLIGHT GO from hidden system health;
- automatically transmit a queued callout to the crew;
- invent exact internal voice-loop routing when the reviewed source does not establish it;
- treat CAPCOM acknowledgement as proof of physical spacecraft response.

## Implemented core

The canonical implementation is `src/apollo_mission_control/pc2_session.py`.

It now:

- owns the authoritative `PC2State` and deterministic scenario event stream;
- supports CREATED / RUNNING / PAUSED / COMPLETE session states;
- enforces unique station/player assignment;
- selects the correct existing station presentation for the assigned player;
- records controller readiness reports without deriving a GO automatically;
- intercepts the nominal `final_go_no_go_poll` event at **79:17 GET** and converts it into an explicit `flight_go` decision gate;
- permits only the assigned FLIGHT player to record the GO/NO-GO decision;
- writes that explicit decision into `state.flight_go`, which is then available to the normal FLIGHT projection;
- keeps a FLIGHT-approved CAPCOM queue distinct from actual CAPCOM transmission;
- records ordered audit events for session lifecycle, scenario events, reports, decisions, and communications handoffs.

`tests/test_pc2_session.py` locks the critical information-flow boundaries, including the requirement that the deterministic nominal event cannot silently set FLIGHT GO in playable orchestration.

A smaller parallel session prototype created during this work was removed after the richer `pc2_session.py` implementation landed, leaving one canonical session model.

## Deliberately deferred

This pass does not choose or implement:

- HTTP/WebSocket framework;
- database schema;
- Render deployment topology;
- authentication/session tokens;
- reconnect/resume protocol;
- phone UI routing;
- historical voice-loop switching;
- automated low-player-count station aggregation.

Those are subsequent implementation decisions. The framework-neutral domain boundary should remain stable underneath them.

## Primary sources

1. **Apollo 13 Technical Air-to-Ground Voice Transcription**, final PC+2 preparation/burn interval. NASA transcript collection: `AS13_TEC.PDF`.
2. **Mission Operations Report — Apollo 13**, NASA Manned Spacecraft Center, Flight Control Division, 28 April 1970; Flight Director/controller appendices and PC+2 chronology.

## Supporting repository context

- `resources/research/078_pc2_flight_capcom_player_presentation_boundary.md`
- `docs/SIMULATION_ARCHITECTURE.md`
- `docs/scenarios/APOLLO13_PC2_STATE_MACHINE.md`
- `docs/scenarios/APOLLO13_PC2_PLAYER_PRODUCTS.md`

## Stop condition / next work

The session now reaches farther than the original boundary: assigned clients can already obtain station-scoped views, and the explicit FLIGHT decision already drives the normal FLIGHT state/product path.

The next integration item is therefore narrower:

1. surface player-submitted readiness reports in the FLIGHT player view as a project session product;
2. surface pending approved callouts in the CAPCOM player view without exposing hidden subsystem state;
3. connect CAPCOM transmission to the existing procedural-communication log;
4. validate the nominal integrated PC+2 sequence through readiness poll, crew-facing GO, burn, shutdown report, residual review, and immediate power-down;
5. then move to transport/reconnect/client delivery.

Further display or subsystem research remains demand-driven by a concrete integration or player-decision dependency.
