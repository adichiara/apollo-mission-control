# Roadmap addendum — first playable PC+2 integration

Date: 2026-09-12  
Status: **CURRENT — mission-clock semantics resolved; rejoin persistence and executable smoke validation are now active**

## Completed presentation checkpoint

Minimum first-slice player presentations exist for CONTROL, GUIDO, TELMU, FIDO/RETRO, INCO, FLIGHT, and CAPCOM. They remain project renderings where exact historical CRT/console evidence is incomplete and preserve controller-visible information boundaries without exposing hidden simulator truth.

## Completed single-process session checkpoint

- [x] one authoritative mission state and synchronized GET;
- [x] deterministic historical scenario advancement;
- [x] start/pause/resume/complete lifecycle and audit log;
- [x] unique logical player→station assignment;
- [x] station-scoped presentation dispatch and serializable player snapshots;
- [x] controller readiness reports surfaced to FLIGHT;
- [x] final-poll FLIGHT GO/NO-GO decision gate;
- [x] explicit FLIGHT-approved CAPCOM queue and CAPCOM transmission event;
- [x] scripted seven-station nominal playthrough through post-burn power-down.

The deterministic historical validator still has its nominal timed GO event, but playable session orchestration intercepts that event so hidden nominal state cannot auto-authorize the burn.

## Completed first web/mobile transport checkpoint

The first phone-accessible shell uses **FastAPI + Uvicorn** as a thin adapter over the framework-neutral session model.

Implemented:

- [x] JSON API for create/status/join/start/pause/resume/advance/snapshot/readiness/FLIGHT decision/CAPCOM queue/transmit;
- [x] prototype audit endpoint for validation;
- [x] responsive dependency-free phone client;
- [x] Render service configuration and health endpoint;
- [x] Python runtime pin;
- [x] API-level transport tests;
- [x] same-player/same-station join is idempotent;
- [x] assignment conflicts and station switching are rejected.

Current deployment architecture remains deliberately **single-process and in-memory**. Restart, redeploy, or platform spin-down loses the live session; multiple workers are not supported until shared state/persistence is deliberately designed.

## Mission-clock / decision-gate semantics — resolved

Primary-source review confirms two important boundaries:

- Apollo GET is a mission time reference; the reviewed sources do not say it stopped for controller deliberation.
- The Apollo 13 Mission Operations Report explicitly says PC+2 ignition time was **not time critical**, but supplies no numerical delay tolerance.

Therefore the project does not invent a historical clock stop or a delay margin.

For the first deterministic playable slice:

- [x] a blocking controller decision gate explicitly pauses the **simulation**;
- [x] the pause is machine-readable (`decision_gate:flight_go`);
- [x] manual resume cannot bypass an unresolved gate;
- [x] FLIGHT GO clears the gate and resumes the simulation;
- [x] NO-GO leaves the gate/pause active;
- [x] later source-timed events are not applied retroactively while players deliberate;
- [x] API/player snapshots expose the pause reason so clients can distinguish a gameplay pause from ordinary running GET.

This is a **project playability policy**, not a claim that Apollo GET historically stopped. See `resources/research/081_pc2_mission_clock_and_decision_gate_semantics.md`.

A future realtime/nonnominal timing model may separate wall-clock time, mission time, and event eligibility more fully, but no such complexity is added until gameplay requires it.

## Active priority 1 — reconnect/player identity hardening

The HTTP API permits idempotent same-player/same-station rejoin. Still needed before a deployed playtest:

- browser-side persistence of local player/station choice or equivalent automatic rejoin;
- lightweight reconnect credential only if needed to prevent casual player-ID collision;
- explicit server-restart behavior while the architecture remains in-memory.

This remains prototype identity, not production authentication.

## Active priority 2 — integration validation

When a runnable environment is available:

- execute the domain/session/API test suite;
- exercise seven logical clients against one server process;
- confirm information isolation;
- confirm explicit decision-pause behavior;
- confirm FLIGHT gate behavior and automatic resume after GO;
- confirm CAPCOM handoff behavior;
- confirm rejoin does not alter mission state;
- confirm nominal timeline reaches power-down;
- then route one already-implemented nonnominal branch through the same session/API path.

## Explicitly deferred until integration exposes a need

- exact console pixel/character reconstruction;
- singular 150-psi inlet-pressure aggregation;
- exact onboard 77-percent thrust indication;
- detailed DPS transient dynamics;
- full RTCC trajectory propagator;
- backroom/staff-support simulation;
- low-player-count station aggregation;
- multi-session/durable production persistence;
- historical SimSup operator UI;
- numeric PC+2 allowable-delay model or retargeting logic without direct evidence.

## Current success criterion

The next milestone is a **rejoin-safe, phone-accessible local/web prototype** in which several clients share one authoritative PC+2 session, each sees only its station information, controller-decision holds are explicit simulation pauses, FLIGHT controls the readiness decision, CAPCOM transmits approved items, and the nominal source-backed timeline can run through post-burn power-down without hidden automatic decisions.
