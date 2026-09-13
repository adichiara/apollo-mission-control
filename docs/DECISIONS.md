# Decisions Log

Only decisions explicitly established for the project are recorded as accepted. Historical facts belong in research notes and should carry sources.

## D-001 — Research-first authenticity

**Status:** Accepted  
**Date:** 2026-09-11

Apollo-specific behavior will be researched from actual documentation before implementation. Missing historical details will not be invented silently.

## D-002 — Simplification is deferred

**Status:** Accepted  
**Date:** 2026-09-11

The real workflow/complexity is established first. Simplification decisions are made only afterward.

## D-003 — Simulator presentation, not game presentation

**Status:** Accepted  
**Date:** 2026-09-11

The experience may be played for enjoyment, but operational screens and workflow should feel like a simulator rather than a conventional game. Player enjoyment comes from role performance, teamwork, interpretation, decision-making, and communication.

## D-004 — Mission outcome priority

**Status:** Accepted  
**Date:** 2026-09-11

Primary goal: accomplish mission objectives. If that becomes infeasible, controllers pursue the best valid alternate/contingency outcome, with safe return of the astronauts the ultimate priority. Abort is phase- and condition-dependent, not a generic success mechanic.

## D-005 — In-person cooperative play

**Status:** Accepted  
**Date:** 2026-09-11

Players are intended to be physically together and communicate as a team.

## D-006 — One controller station per player

**Status:** Superseded in part by D-018  
**Date:** 2026-09-11

The full-fidelity configuration assigns one Mission Control role/station per player. Low-player-count aggregation was left for later design; D-018 now defines the first compact PC+2 configuration while retaining original station identities underneath bundled player roles.

## D-007 — Phone-based station interface

**Status:** Accepted  
**Date:** 2026-09-11

Each player uses a phone as the station display/interface, connected to the live central simulation.

## D-008 — Physical controller documentation

**Status:** Accepted  
**Date:** 2026-09-11

Players use printed station documentation such as flight rules. Exact contents and amount of material remain to be determined from historical research and usability requirements.

## D-009 — Central authoritative simulation

**Status:** Accepted  
**Date:** 2026-09-11

A central server owns the live mission state. Player devices are station clients, not independent simulators.

## D-010 — Deployment target

**Status:** Accepted  
**Date:** 2026-09-11

Production deployment target is Render.

## D-011 — Paper exchange is not a formal subsystem

**Status:** Clarified  
**Date:** 2026-09-11

Apollo hard-copy workflows remain a historical research topic, but the simulation will not assume a formalized paper-delivery mechanic. Players may naturally write, pass, or share paper when useful. No decision has yet been made about which historical hard-copy products, if any, must be reproduced during live play.

## D-012 — Apollo 13-era MCC as default technical baseline

**Status:** Accepted in principle  
**Date:** 2026-09-11

Use the Apollo 13-era Mission Control configuration as the default technical/research baseline for the reusable simulation platform. Mission-specific profiles still override later features where contemporary documentation shows a difference; an Apollo 11 scenario must reproduce Apollo 11 rather than blindly expose Apollo 13-era nomenclature or capabilities.

## D-013 — First vertical slice: Apollo 13 PC+2

**Status:** Accepted as first implementation target  
**Date:** 2026-09-11

The first playable vertical slice centers on **Apollo 13 PC+2 preparation and execution**, using a working interval of approximately **74:00–80:00 GET** and the historical DPS burn at about **79:27:38 GET**. Research note `048_first_vertical_slice_candidate_assessment.md` records the evidence basis.

## D-014 — First playable web transport: FastAPI + Uvicorn

**Status:** Accepted for first playable prototype  
**Date:** 2026-09-12

Use **FastAPI + Uvicorn** as the first web transport while retaining framework-neutral domain logic. The initial server is deliberately single-process and in-memory. See `resources/research/080_web_transport_selection.md`.

## D-015 — Blocking controller gates pause the simulation

**Status:** Superseded by D-016  
**Date:** 2026-09-12

This provisional rule was rejected because it conflated controller readiness with mission time.

## D-016 — Continuous mission clock; gates affect eligibility, not time

**Status:** Accepted  
**Date:** 2026-09-12

The simulation engine uses a **continuous running mission clock**.

- GET advances whenever the session is running.
- Controller decisions and missing authorizations do not stop GET.
- Only an explicit game/session pause stops simulated mission time.
- Timed scenario entries are nominal milestones with prerequisites, not mandatory scene transitions.
- Ineligible nominal events are recorded as missed and are not replayed retroactively.

See `resources/research/084_continuous_mission_clock_architecture.md`.

## D-017 — Facilitator/SimSup authority is separate from controller identity

**Status:** Accepted for first playable prototype  
**Date:** 2026-09-12

Whole-exercise authority is distinct from Mission Control station identity.

Primary NASA simulation sources support an organizational distinction between the Simulation Supervisor/simulation-control organization and the flight controllers being trained. The project therefore protects exercise-wide operations with a separate facilitator credential rather than granting them through any controller station.

Protected operations include:

- session create/reset and lifecycle control;
- manual validation GET advancement;
- source/state injection;
- validation-harness crew/vehicle response operations;
- global audit-log access.

FLIGHT, CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, and CAPCOM remain controller identities with only their station-authorized actions.

The credential mechanism (`APOLLO_FACILITATOR_TOKEN` / `X-Apollo-Facilitator`) is a modern software safety measure, **not** a claim about Apollo-era authentication. Render deployments generate the secret through deployment configuration rather than storing it in source.

See `resources/research/088_facilitator_authority_boundary.md`.

## D-018 — Compact PC+2 mode uses five players while preserving original station identities

**Status:** Accepted; domain, HTTP, and browser integration implemented; physical compact-play validation pending  
**Date:** 2026-09-12

For the Apollo 13 PC+2 first playable, the recommended low-player-count configuration is five human players:

- FLIGHT;
- CAPCOM;
- LM SYSTEMS = TELMU + CONTROL;
- FLIGHT DYNAMICS = GUIDO + FIDO/RETRO;
- INCO.

This is a **project adaptation**, not a claim about historical Apollo 13 manning. Primary Apollo sources group TELMU/CONTROL within spacecraft systems operations and FIDO/RETRO/GUIDO within Flight Dynamics, but continue to document the underlying positions separately.

Implementation therefore allows one player to own multiple **original station identities** rather than replacing those identities with synthetic domain stations. Products, readiness, actions, authorization, presentations, and audit entries remain attributable to TELMU, CONTROL, GUIDO, FIDO/RETRO, etc.

The framework-neutral session layer implements station-set ownership and bundled snapshots. The HTTP layer now supports exact-set join/rejoin through `/api/session/join-set` while retaining the original single-station path. The browser persists the station set and active substation and exposes explicit original-call-sign navigation; it does not create a merged synthetic station.

FLIGHT and CAPCOM stay independent in the recommended compact mode because their final-decision and crew-voice functions are distinct authority boundaries. INCO also stays independent; a four-player CAPCOM+INCO bundle is not accepted at this stage.

Physical five-player human/device validation is still required before compact mode is recorded as play-validated.

See research notes 091–094 and `resources/source-catalog/PC2_LOW_PLAYER_COUNT_SOURCES.md`.

## D-019 — PC+2 spacecraft physics uses decision-relevant causal fidelity

**Status:** Accepted for the current first playable  
**Date:** 2026-09-13

The Apollo 13 PC+2 first playable does not attempt complete LM/CSM physical emulation. A spacecraft mechanism is modeled when it is required to generate sourced player information, enforce a sourced rule/procedure, or support a selected failure branch.

Required causal domains are:

- DPS/maneuver state;
- guidance/attitude/control state;
- coarse electrical configuration and equipment availability;
- communications/uplink/ranging availability;
- instrumentation/observation validity and freshness.

Full ECS/CSM subsystem physics, full six-degree-of-freedom propagation, pulse-level RCS dynamics, detailed battery/wiring physics, RF propagation/modulation, complete LM instrumentation, and internal RTCC/CCATS emulation remain deferred until a sourced controller decision or selected failure mechanism depends on them.

This is a scope boundary, not permission to invent or collapse unresolved historical mechanisms. The required chain is:

`historical/player decision dependency → physical cause → sensed/processed observation → station product/action`

See `resources/research/102_pc2_spacecraft_physical_model_scope.md` and `resources/source-catalog/PC2_SPACECRAFT_MODEL_SCOPE_SOURCES.md`.

## D-020 — Observation failures are layered and scenario-authored

**Status:** Accepted for the current first playable  
**Date:** 2026-09-13

The simulator does not use a generic or random `telemetry failure` mechanic for PC+2.

Observation faults must remain attributable to the layer where the evidence places them:

`physical source → sensor/transducer → conditioning/PCM → communications/telemetry path → ground processing → station product`

For the current first playable, the architecture may represent unavailable, stale/delayed, biased/shifted, warning-only, communications-path, or ground-product faults when a scenario specifically requires them. These are capabilities, not random events.

The nominal PC+2 run has no newly invented historical instrumentation failure. A future nonnominal observation fault requires a sourced or explicitly synthetic origin, observable effect, and player-decision consequence. Unsupported probabilities, durations, bias/noise magnitudes, recovery timing, and correlations are not added.

See `resources/research/104_pc2_sensor_telemetry_failure_scope.md` and `resources/source-catalog/PC2_OBSERVATION_FAILURE_SOURCES.md`.

## Not yet decided

The following are deliberately not decisions:

- four-player-or-smaller station aggregation;
- durable session persistence/storage architecture;
- realtime push mechanism (polling vs SSE/WebSockets);
- voice-loop implementation;
- time acceleration / realtime pacing multiplier;
- scenario-selection UI;
- named facilitator accounts or fine-grained facilitator permissions.
