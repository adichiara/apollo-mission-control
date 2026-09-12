# Apollo 13 PC+2 — first playable session orchestration boundary

Date: 2026-09-12  
Status: **IMPLEMENTED-PARTIAL — single-process authoritative session core added; network/web client layer not yet selected**

## Purpose

Convert the already-researched PC+2 domain model and station presentations into one playable authoritative session without changing the historical information boundaries.

This is primarily an implementation/architecture note. Historical behavior is inherited from the existing mission-specific research chain and state-machine documentation.

## Primary-source ordering boundary — readiness, FLIGHT decision, CAPCOM transmission

The contemporaneous PC+2 record gives a useful operational ordering constraint for the session model:

- at approximately **78:57 GET**, Flight Director Gene Kranz tells the team he will go around the room near minus 10 minutes for a final GO/NO-GO;
- at approximately **79:17 GET**, the Flight Director is reported as going around the room for team status and the control room is reported GO for the burn;
- at **79:18:15 GET**, CAPCOM tells the crew that they are GO for the burn;
- the crew acknowledges at approximately **79:18:20 GET**.

The software therefore preserves three separate events:

```text
controller readiness report(s)
        -> FLIGHT decision
        -> CAPCOM crew-facing transmission
```

The reviewed evidence does not justify an automatically computed overall GO derived from hidden authoritative subsystem state, nor does a FLIGHT decision automatically constitute a crew transmission.

The same separation is visible during the burn, when Mission Control continues assessing the maneuver and CAPCOM carries crew-facing continuation calls.

Primary basis:

- Apollo 13 Technical Air-to-Ground Voice Transcription, final PC+2 preparation/burn interval (`AS13_TEC.PDF` in NASA's mission transcript collection);
- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970.

## First implemented session responsibilities

`PC2Session` now owns:

- authoritative PC+2 state;
- authoritative synchronized GET;
- chronological scenario-event application;
- unique logical station assignment;
- station-scoped presentation selection;
- controller readiness reports;
- FLIGHT GO/NO-GO decision gating;
- explicit FLIGHT→CAPCOM queue handoff;
- CAPCOM transmission event;
- pause/resume state;
- chronological audit log.

## Critical integration correction — GO is no longer automatic in play

The original deterministic nominal prototype applies the timed `final_go_no_go_poll` fixture event by setting `flight_go=True`. That behavior is useful for historical nominal validation, but the scenario research explicitly states that:

> FLIGHT GO is a decision state produced from controller reports. It must not be generated merely because the authoritative simulation is nominal.

The new session layer therefore intercepts the **79:17 GET** poll event.

Instead of automatically setting GO it:

1. advances to the poll time;
2. opens a `flight_go` decision gate;
3. holds scenario progression at final readiness;
4. waits for an explicitly assigned FLIGHT player to record GO or NO-GO.

A NO-GO leaves the session blocked at readiness. A later explicit GO clears the gate and permits progression toward P40.

The deterministic nominal validation model remains unchanged so its historical fixture tests can continue to reproduce the nominal timeline independently of gameplay policy.

## Station information boundary

A player is assigned exactly one logical station in this prototype.

`get_station_view(player_id)`:

1. projects the current authoritative state into all controller products;
2. selects only the assigned station projection;
3. invokes that station's presentation builder.

This prevents the session layer from solving gameplay by giving every client an omniscient state object.

Supported first-slice station views:

- CONTROL;
- GUIDO;
- TELMU;
- FIDO_RETRO;
- INCO;
- FLIGHT;
- CAPCOM.

Low-player-count role aggregation remains deferred.

## Controller readiness reporting

`submit_readiness(...)` records:

- GET;
- player;
- station;
- ready / not-ready decision;
- optional human note.

Reports are audit/session events. They do not mutate spacecraft state.

The FLIGHT GO event records a snapshot of the latest reported station readiness but does not calculate GO automatically from it. The Flight Director player remains responsible for the decision.

## FLIGHT → CAPCOM handoff

The prototype includes an explicit approved-message queue:

1. FLIGHT queues a crew-facing action/instruction with a basis;
2. CAPCOM receives the queue item;
3. CAPCOM explicitly transmits it;
4. the transmission is recorded independently in the audit log.

The queue item itself does not mutate crew or spacecraft state. Specific historical procedures remain represented by the existing procedural/action layers.

This first implementation deliberately permits only FLIGHT to approve queue items. More detailed discipline→FLIGHT→CAPCOM routing can be added when gameplay requires it; exact historical loop routing is not invented here.

## Audit model

The session audit trail records, in sequence:

- station assignments;
- session start/pause/resume;
- historical scenario events applied;
- opening of the GO/NO-GO gate;
- controller readiness reports;
- FLIGHT decision;
- CAPCOM queue/transmission events;
- eventual session completion.

This is the beginning of the post-simulation replay substrate rather than an in-play scoring system.

## What is not implemented yet

- web/network transport;
- authentication/join codes;
- reconnection protocol;
- actual phone UI;
- wall-clock real-time driver;
- controller readiness UX;
- CAPCOM queue UX;
- crew simulator/client;
- automatic mapping from CAPCOM transmissions to crew actions;
- low-player-count role aggregation;
- persistent replay storage;
- post-burn FIDO trajectory propagation.

## Code

- `src/apollo_mission_control/pc2_session.py`
- `tests/test_pc2_session.py`

## Historical/project basis

- `docs/scenarios/APOLLO13_PC2_STATE_MACHINE.md`
- `docs/scenarios/APOLLO13_PC2_PLAYER_PRODUCTS.md`
- research notes 048–078;
- NASA Flight Control Division, *Mission Operations Report — Apollo 13*;
- Apollo 13 Technical Air-to-Ground Voice Transcription.

## Next implementation priority

Continue integration rather than returning to subsystem archaeology:

1. add a thin session-facing snapshot/API DTO independent of Python presentation dataclasses;
2. add explicit readiness-report visibility to FLIGHT;
3. expose CAPCOM pending/transmitted queue state to the CAPCOM view;
4. connect CAPCOM transmission to the existing procedural-communication log;
5. add a deterministic session driver for the nominal PC+2 timeline;
6. run an end-to-end scripted multi-station playthrough against the single-process session;
7. only then choose/implement the web framework and mobile presentation shell.
