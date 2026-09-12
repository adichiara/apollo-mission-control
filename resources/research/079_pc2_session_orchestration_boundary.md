# Apollo 13 PC+2 — integrated session-orchestration boundary

Date: 2026-09-12  
Status: **REVIEWED / IMPLEMENTED-PARTIAL — framework-neutral session core added; network transport, persistence, reconnect, and station-client delivery remain future work**

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

The current evidence does **not** justify replacing that sequence with an automatically computed overall readiness boolean derived from authoritative subsystem state.

### During-burn continuation

The record also shows continuing Mission Control assessment during the burn and CAPCOM transmitting crew-facing continuation calls (for example, a three-minute GO). This reinforces the same separation: controller/system assessment is not identical to the air-ground callout.

## Software boundary

This session layer is explicitly **project architecture**, not a reconstruction of Apollo MCC software internals.

It must own:

- authoritative session GET;
- station/player assignment;
- controller readiness reports;
- explicit FLIGHT decisions;
- queued controller/FLIGHT callouts requiring crew transmission;
- CAPCOM-to-crew transmission events;
- ordered audit/replay events.

It must **not**:

- expose authoritative physical state directly to FLIGHT or CAPCOM;
- automatically infer a FLIGHT GO from hidden system health;
- automatically transmit a queued callout to the crew;
- invent exact internal voice-loop routing when the reviewed source does not establish it;
- treat CAPCOM acknowledgement as proof of physical spacecraft response.

## Implemented core

Added `src/apollo_mission_control/session_orchestration.py` with:

- `PC2Session`;
- monotonic `synchronize_get()`;
- unique current station assignment;
- current readiness state per station plus full audit history;
- explicit `record_flight_decision()`;
- `queue_crew_callout()`;
- distinct `capcom_transmit()`;
- monotonically sequenced `SessionEvent` audit entries.

Added `tests/test_session_orchestration.py` to lock the critical information-flow boundaries.

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

The next integration item should connect this session state to the existing controller projections/presentations so that:

1. station clients receive only their assigned station view;
2. FLIGHT receives player-submitted readiness reports;
3. FLIGHT's explicit decision updates the FLIGHT session product;
4. a FLIGHT GO can be queued for CAPCOM rather than directly appearing to the crew;
5. CAPCOM transmission records the crew-facing event;
6. all of this remains replayable from the audit trail.

Only after that domain integration is stable should transport/reconnect implementation become the main task.
