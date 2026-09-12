# Roadmap addendum — first playable PC+2 integration

Date: 2026-09-12  
Status: **CURRENT — single-process playable integration core complete; transport/mobile shell is now the active priority**

## Completed presentation checkpoint

The minimum first-slice player presentation set exists for:

- CONTROL;
- GUIDO;
- TELMU;
- FIDO/RETRO;
- INCO;
- FLIGHT;
- CAPCOM.

These remain implementation-oriented project renderings where exact historical CRT/console evidence is incomplete. They preserve controller-visible products, provenance, and information boundaries without exposing hidden simulator truth.

## Completed single-process session checkpoint

### 1. Session authority — implemented

- [x] one authoritative mission state;
- [x] synchronized GET;
- [x] deterministic historical scenario advancement;
- [x] explicit start/pause/resume/complete state;
- [x] chronological scenario/audit log.

### 2. Station assignment and views — implemented

- [x] unique logical player→station assignment;
- [x] correct presentation builder selected by assignment;
- [x] player snapshots contain only the assigned station presentation;
- [x] serializable player-scoped snapshot DTO added.

Reconnection policy remains a future transport concern; authoritative session state is already independent of presentation instances.

### 3. Controller reporting / FLIGHT integration — implemented

- [x] controller readiness-report event;
- [x] readiness reports surfaced in the FLIGHT presentation;
- [x] FLIGHT records GO/NO-GO explicitly;
- [x] historical final poll opens a gameplay gate rather than automatically setting GO;
- [x] NO-GO blocks advancement toward P40;
- [x] GO clears the gate and permits progression.

### 4. FLIGHT → CAPCOM communication — implemented at minimum integration level

- [x] explicit FLIGHT-approved CAPCOM queue item;
- [x] pending/transmitted queue state surfaced in CAPCOM presentation;
- [x] CAPCOM transmission is an explicit session action;
- [x] transmission does not directly mutate spacecraft truth.

Specific procedure/readback semantics continue to use the existing procedural/action layers and can be connected incrementally.

### 5. Scenario progression — nominal integrated path implemented

The single-process session can now run the source-backed nominal sequence through:

- final PAD transfer under weak communications;
- communications improvement;
- burn-configuration power-up;
- ranging/computer support;
- readiness / explicit FLIGHT GO;
- P40 / ullage / DPS burn sequence;
- nominal cutoff;
- residual review;
- power-down transition.

A scripted multi-station integration harness exercises this path through the same public session operations intended for future clients. Its readiness notes/sequence are explicitly software validation fixtures, not claims about the exact historical spoken GO-poll roster.

### 6. Audit / replay substrate — implemented at first level

The session records:

- station assignments;
- session lifecycle;
- authoritative historical scenario events;
- readiness reports;
- FLIGHT decision gate and GO/NO-GO decision;
- CAPCOM queue/transmission events;
- session completion.

Further action/failure-event unification remains future integration work, but the basic replay substrate now exists.

## Active priority — thin transport and mobile shell

The next milestone should make the working single-process session reachable by actual browser/phone clients without redesigning the domain model.

### A. Transport/framework decision

Choose the thinnest production-compatible web stack that:

- can host on Render;
- keeps one authoritative server-side session object;
- provides simple JSON station snapshots/actions;
- supports multiple phone clients;
- permits later realtime push or polling without coupling simulation code to the web framework.

### B. Minimum API surface

Target operations:

- create/load PC+2 session;
- join/assign station;
- start/pause/resume session;
- get player snapshot;
- submit readiness;
- record FLIGHT GO/NO-GO;
- queue/transmit CAPCOM item;
- advance/tick authoritative GET;
- retrieve limited audit/replay data for validation.

### C. Minimum phone interface

- station identity and GET always visible;
- render the existing station presentation model;
- station-specific action controls only where implemented;
- no omniscient cross-station dashboard;
- responsive phone-first layout;
- no attempt yet to reproduce every historical CRT pixel.

### D. Integration validation

- exercise seven logical station clients against one session;
- confirm information isolation;
- confirm FLIGHT gate behavior;
- confirm CAPCOM handoff behavior;
- confirm reconnect does not alter mission state;
- confirm nominal timeline reaches power-down;
- then exercise one already-implemented nonnominal branch through the same transport/session path.

## Explicitly deferred until integration exposes a need

- exact console pixel/character reconstruction;
- singular 150-psi inlet-pressure aggregation;
- exact onboard 77-percent thrust indication;
- detailed DPS transient dynamics;
- full RTCC trajectory propagator;
- backroom/staff-support simulation;
- low-player-count station aggregation;
- production-scale persistence/authentication;
- historical SimSup operator UI.

## Current success criterion

The next milestone is a **phone-accessible local/web prototype** in which multiple clients connect to one authoritative PC+2 session, each sees only its station products, FLIGHT controls the readiness gate, CAPCOM receives/transmits approved items, and the source-backed nominal scenario can be played through to post-burn power-down.
