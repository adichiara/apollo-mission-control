# Roadmap addendum — first playable PC+2 integration

Date: 2026-09-12  
Status: **CURRENT — presentation research checkpoint complete; integration is now the active priority**

## Completed presentation checkpoint

The minimum first-slice player presentation set now exists for:

- CONTROL;
- GUIDO;
- TELMU;
- FIDO/RETRO;
- INCO;
- FLIGHT;
- CAPCOM.

These are intentionally implementation-oriented project renderings where exact historical CRT/console evidence is incomplete. They preserve controller-visible products, provenance, and information boundaries without exposing hidden simulator truth.

## Active priority — playable session orchestration

Build the smallest end-to-end session capable of running the Apollo 13 PC+2 slice from 77:55 GET through post-burn verification/power-down.

### 1. Session authority

- one authoritative mission state;
- synchronized GET;
- deterministic scenario advancement;
- explicit pause/start/end state;
- scenario event/audit log.

### 2. Station assignment and views

- assign/join a station;
- select the correct presentation builder for that station;
- do not give one player products belonging to another station;
- reconnect without altering authoritative mission state.

### 3. Controller reporting / FLIGHT integration

- controller readiness report event;
- FLIGHT receives reports, not hidden subsystem status;
- FLIGHT records GO/NO-GO decision explicitly;
- no automatic GO merely because the authoritative state is nominal.

### 4. FLIGHT → CAPCOM → crew communication

- explicit callout/instruction request from FLIGHT or a discipline;
- CAPCOM receives an approved queue item;
- CAPCOM transmits it to the crew;
- crew response/readback is a separate communication event;
- communications quality can affect transfer without mutating hidden target state.

### 5. Scenario progression

Support at minimum:

- final PAD transfer under weak communications;
- communications improvement;
- burn-configuration power-up;
- ranging/computer support;
- readiness / GO;
- P40 / ullage / DPS burn sequence;
- controller monitoring;
- nominal cutoff and residual review;
- power-down transition.

Existing nonnominal branches should plug into the same orchestration rather than use a separate scenario engine.

### 6. Audit / replay

Record enough information to reconstruct:

- authoritative state changes;
- controller-visible products;
- controller decisions/reports;
- CAPCOM/crew communications;
- crew operational actions;
- physical responses;
- injected nonnominal conditions.

## Explicitly deferred until integration exposes a need

- exact console pixel/character reconstruction;
- singular 150-psi inlet-pressure aggregation;
- exact onboard 77-percent thrust indication;
- detailed DPS transient dynamics;
- full RTCC trajectory propagator;
- backroom/staff-support simulation;
- low-player-count station aggregation;
- production framework/deployment implementation beyond the framework-neutral domain model.

## Success criterion

The next milestone is not another research note. It is a **single-process playable prototype** in which multiple logical station clients can observe their own PC+2 products, submit reports/actions, and advance one authoritative session through the nominal timeline with an inspectable event log.
