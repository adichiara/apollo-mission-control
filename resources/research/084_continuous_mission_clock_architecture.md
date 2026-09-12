# 084 — Continuous mission clock architecture

Date: 2026-09-12  
Status: **CURRENT IMPLEMENTATION ARCHITECTURE**

## Decision

The simulation is a **continuous-time mission model**, not a sequence of gated scenes.

Ground Elapsed Time (GET) advances whenever the session is running. Controller decisions, procedure state, and authorization requirements may affect what actions or nominal milestones are executable, but they do not stop the mission clock.

Only an explicit game/session pause stops simulated time.

## Why this matters

A controller decision and the passage of mission time are different state dimensions.

The engine therefore separates:

1. **mission GET** — current simulated mission time;
2. **authoritative physical/system state** — what the spacecraft and ground systems are doing;
3. **operational prerequisites / authorization** — whether a planned action or milestone is currently executable;
4. **controller decisions and reports** — player actions that may satisfy those prerequisites;
5. **explicit game pause** — the only mechanism that stops simulated GET.

This prevents a late or unresolved decision from freezing the universe merely because the software is waiting for input.

## Nominal timeline semantics

The historical PC+2 fixture contains source-backed nominal milestones such as:

- final GO/NO-GO poll;
- P40 preparation;
- two-jet ullage;
- DPS ignition/TIG;
- throttle-command milestones;
- guided cutoff;
- residual review;
- post-burn power-down.

These timestamps are now interpreted as **nominal event opportunities**, not unconditional scene transitions.

When a milestone arrives:

- if its operational prerequisites are satisfied, the event may execute;
- if required prerequisites are absent, the nominal event is recorded as **missed**;
- the clock continues;
- a later player action does not automatically rewind or replay the missed event.

## PC+2 example

At approximately 79:17 GET the historical final GO/NO-GO poll occurs.

The simulator opens a `flight_go` decision requirement but remains RUNNING.

If FLIGHT records GO before the nominal P40 milestone, the nominal sequence can continue.

If GET reaches the P40 milestone first, that nominal P40 event is missed. If GO is recorded afterward, the engine does not retroactively activate P40.

The same principle cascades through later dependent nominal milestones:

- ullage requires the required preceding state;
- ignition requires GO, P40, and nominal ullage;
- throttle milestones require a running DPS;
- nominal cutoff requires a running DPS;
- residual review requires cutoff;
- nominal post-burn power-down is not blindly applied after a burn sequence that never occurred.

This is deliberately conservative. It does not invent a late-burn retargeting procedure or an automatic recovery path. Such behavior must be modeled as explicit procedures/actions when historically or operationally justified.

## Explicit pause

`pause()` remains available as a game/session control.

While explicitly paused:

- GET does not advance;
- no timed scenario events are processed;
- the pause is labeled as a session/game pause, not a controller-decision condition.

Resuming the session restarts normal mission-time advancement regardless of whether controller decisions remain pending.

## Architectural consequence

This changes the engine from:

`scene → player gate → scene → player gate`

into:

`continuous mission evolution + player interventions + event prerequisites`

That distinction is foundational for later scenarios where timing itself creates consequences, including missed maneuver windows, delayed responses, communications timing, consumable evolution, and cascading nonnominal states.

## Current implementation

`src/apollo_mission_control/pc2_session.py` now:

- keeps the session RUNNING at the FLIGHT GO decision requirement;
- records `decision_gate_opened` with `simulation_paused=False`;
- advances GET normally while the decision remains pending;
- evaluates prerequisites for downstream nominal events;
- records ineligible nominal milestones as `scenario_event_missed` with a reason;
- never retroactively replays a missed source-timed event merely because a later decision becomes favorable;
- reserves `SessionStatus.PAUSED` for explicit game/session pause behavior.

Tests cover:

- continuous GET through a pending GO decision;
- GO before P40 allowing the nominal sequence to continue;
- late GO not replaying a missed P40 milestone;
- unresolved/NO-GO causing downstream nominal burn milestones to be missed while GET continues;
- explicit manual pause remaining the only ordinary mechanism that stops advancement.

## Remaining work

The current prerequisite logic is intentionally narrow to the PC+2 first slice. The next engine-level refinement should generalize event eligibility/dependencies so scenario authors can declare prerequisite relationships instead of hard-coding each nominal PC+2 event name.

The web transport also still advances GET through explicit API calls. A realtime pacing driver can now be added safely because the clock semantics are resolved: wall-clock pacing drives GET while RUNNING, and player decisions do not implicitly stop it.
