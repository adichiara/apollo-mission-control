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

Primary goal: accomplish mission objectives.

If that becomes infeasible, controllers pursue the best valid alternate/contingency outcome, with safe return of the astronauts the ultimate priority.

Abort is phase- and condition-dependent, not a generic success mechanic.

## D-005 — In-person cooperative play

**Status:** Accepted  
**Date:** 2026-09-11

Players are intended to be physically together and communicate as a team.

## D-006 — One controller station per player

**Status:** Accepted in principle  
**Date:** 2026-09-11

Each player assumes responsibility for a Mission Control role/station. Role aggregation for low player counts is expected to be necessary but is **not yet designed**.

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

Apollo hard-copy workflows remain a historical research topic, but the simulation will not assume a formalized paper-delivery mechanic.

Because play is in person, players may naturally write, pass, or share paper when useful, using whatever materials are available. The amount of printed/dynamic paper should not be increased merely for atmosphere and may ultimately be minimized where that does not remove historically important information.

No decision has yet been made about which historical hard-copy products, if any, must be reproduced during live play.

## D-012 — Apollo 13-era MCC as default technical baseline

**Status:** Accepted in principle  
**Date:** 2026-09-11

Use the Apollo 13-era Mission Control configuration as the default technical/research baseline for the reusable simulation platform because it represents a later, mature Apollo lunar-mission configuration and is unusually well documented.

This does **not** mean Apollo 13-specific details are automatically shown in earlier scenarios.

Each mission/scenario must support a mission-specific historical profile that can override, remove, or rename later features where contemporary documentation shows a difference. Known example: Apollo 11 uses the LM systems call sign **TELCOM**, while Apollo 13 mission documentation uses **TELMU**.

Therefore:

- shared simulation machinery should favor the later Apollo-compatible superset where practical;
- visible station nomenclature, available displays, procedures, spacecraft/ground configuration, rules, and capabilities remain mission-specific;
- an Apollo 11 scenario should reproduce Apollo 11 where a documented difference exists rather than presenting the Apollo 13 configuration unchanged.

## D-013 — First vertical slice: Apollo 13 PC+2

**Status:** Accepted as first implementation target  
**Date:** 2026-09-11

The first playable vertical slice will center on **Apollo 13 PC+2 preparation and execution**, using a working interval of approximately **74:00–80:00 GET** and the historical DPS burn at about **79:27:38 GET**.

This interval is selected because it combines strong primary-source coverage, substantial interaction among multiple controller disciplines, explicit maneuver/shutdown rules, compatibility with the Apollo 13-era baseline, and a more bounded initial physical model than either the oxygen-tank accident onset or Apollo 11 powered descent.

The vertical slice should model only the state and information required for the selected interval rather than treating unresolved details elsewhere in Apollo 13 as prerequisites.

Research note `048_first_vertical_slice_candidate_assessment.md` records the candidate comparison and evidence basis.

The Apollo 13 oxygen-tank accident remains a priority expansion scenario. Apollo 11 powered descent is the strongest early candidate for validating mission-profile portability.

## D-014 — First playable web transport: FastAPI + Uvicorn

**Status:** Accepted for first playable prototype  
**Date:** 2026-09-12

Use **FastAPI + Uvicorn** as the first web transport for exposing the framework-neutral Mission Control session model to phone/browser clients and deploying the prototype on Render.

This is a transport decision, not a simulation-domain decision:

- historical/session logic remains in framework-neutral Python modules;
- FastAPI adapts HTTP requests/responses to the domain API;
- ASGI preserves a later path to realtime/WebSocket transport if playtesting requires it;
- the first server is deliberately **single-process and in-memory** so one authoritative session object owns live state.

The in-memory prototype is not considered durable production infrastructure. Process restart, redeploy, or platform spin-down can lose the active session, and multiple workers would create divergent state unless shared persistence/session coordination is added.

See `resources/research/080_web_transport_selection.md` and `resources/source-catalog/WEB_TRANSPORT_SOURCES.md`.

## D-015 — Blocking controller gates pause the simulation

**Status:** Superseded by D-016  
**Date:** 2026-09-12

This provisional rule paused simulated GET while a blocking controller decision was pending. It was rejected after explicit project review because it conflated controller readiness with mission time and made the engine scene/gate-driven rather than continuously evolving.

The historical-source findings in `081_pc2_mission_clock_and_decision_gate_semantics.md` remain useful, but its former implementation policy is superseded.

## D-016 — Continuous mission clock; gates affect eligibility, not time

**Status:** Accepted  
**Date:** 2026-09-12

The simulation engine uses a **continuous running mission clock**.

- GET advances whenever the session is running.
- A controller decision, unresolved procedure, or missing authorization does **not** stop GET.
- Only an explicit game/session pause stops simulated mission time.
- Timed scenario entries are nominal milestones, not mandatory scene transitions.
- When a nominal event's operational prerequisites are absent at its scheduled GET, that event is recorded as missed/ineligible rather than executed anyway or replayed retroactively later.
- Player decisions may therefore be late, and lateness can change the mission state without an artificial score or timeout mechanic.

For PC+2, the final FLIGHT GO/NO-GO poll opens a decision requirement while GET continues. If GO is not recorded before later nominal prerequisites such as P40, ullage, or TIG, those nominal milestones may be missed. A later GO does not automatically rewind or replay them.

This establishes the engine as a **continuously evolving mission in which players intervene**, rather than a sequence of gated scenes.

See `resources/research/082_continuous_mission_clock_architecture.md`.

## Not yet decided

The following are deliberately not decisions:

- minimum player count
- exact controller combinations by player count
- durable session persistence/storage architecture
- realtime push mechanism (polling vs SSE/WebSockets)
- degree of RTCC/CCATS/MSFN emulation beyond what the first scenario requires
- degree of Staff Support Room simulation
- voice-loop implementation
- time acceleration / realtime pacing multiplier
- scenario-selection UI
- post-simulation evaluation format
