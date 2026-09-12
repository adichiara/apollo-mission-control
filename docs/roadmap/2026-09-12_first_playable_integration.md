# Roadmap addendum — first playable PC+2 integration

Date: 2026-09-12  
Status: **CURRENT — phone-accessible transport shell implemented; mission-clock/reconnect hardening is now the active priority**

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

The first phone-accessible shell now uses **FastAPI + Uvicorn** as a thin adapter over the framework-neutral session model.

Implemented:

- [x] JSON API for create/status/join/start/pause/resume/advance/snapshot/readiness/FLIGHT decision/CAPCOM queue/transmit;
- [x] prototype audit endpoint for validation;
- [x] responsive dependency-free phone client;
- [x] Render service configuration and health endpoint;
- [x] Python runtime pin;
- [x] API-level transport tests;
- [x] same-player/same-station join is idempotent so a browser can rejoin an existing assignment;
- [x] another player cannot take an occupied station;
- [x] an existing player ID cannot silently switch stations.

Current deployment architecture remains deliberately **single-process and in-memory**. Restart, redeploy, or platform spin-down loses the live session; multiple workers are not supported until shared state/persistence is deliberately designed.

## Active priority 1 — mission-clock semantics

Before replacing manual GET advancement with a realtime driver, resolve a gameplay/historical timing distinction exposed by integration:

- historical GET continues continuously;
- the current prototype holds GET at the FLIGHT decision gate until GO;
- holding GET is effectively a simulation pause, not historical mission behavior.

Do **not** silently implement a realtime clock that either:

1. freezes historical GET at every pending decision without an explicit pause policy; or
2. advances later historical events past an unresolved gate and then applies them retroactively without defined semantics.

Next design work should explicitly separate, where necessary:

- mission/session clock time;
- scenario event eligibility;
- explicit game pause state;
- decision gates.

Time acceleration and exact pause policy remain undecided project decisions.

## Active priority 2 — reconnect/player identity hardening

The HTTP API now permits idempotent same-player/same-station rejoin, which is enough to survive a browser refresh if the player reuses the same ID.

Still needed before a deployed playtest:

- browser-side persistence of the local player/station choice or an equivalent rejoin mechanism;
- a lightweight generated reconnect credential if the prototype must prevent another person from claiming the same player ID;
- explicit behavior when the server itself restarts and in-memory assignments disappear.

This is prototype identity, not production authentication.

## Active priority 3 — integration validation

When a runnable environment is available:

- execute the domain/session/API test suite;
- exercise seven logical clients against one server process;
- confirm information isolation;
- confirm FLIGHT gate behavior;
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
- historical SimSup operator UI.

## Current success criterion

The next milestone is a **rejoin-safe, phone-accessible local/web prototype with explicit mission-clock semantics**, in which several clients share one authoritative PC+2 session, each sees only its station information, FLIGHT controls the readiness decision, CAPCOM transmits approved items, and the nominal source-backed timeline can run through post-burn power-down without hidden automatic decisions.
