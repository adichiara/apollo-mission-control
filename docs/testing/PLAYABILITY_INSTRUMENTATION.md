# Playability Instrumentation

Date: 2026-09-19  
Status: prototype instrumentation for research-note-314 validation

## Purpose

Record objective interaction timing and recovery evidence without mixing usability telemetry into the authoritative mission audit.

This instrumentation is modern test infrastructure. It is not Apollo behavior, does not alter simulation state, and does not score mission performance.

## Surfaces

The same event schema is used by:

- `validation_client` — the original `/` validation/player client;
- `player_lab` — the non-final FLIGHT/CAPCOM interaction prototype.

The `surface` field must remain explicit so observations from the two interfaces are not combined accidentally.

## Recorded fields

Each event contains:

- server-assigned sequence;
- authoritative GET at receipt;
- surface;
- event kind;
- player ID when available;
- original station when available;
- a short controlled target identifier;
- client elapsed milliseconds from page load.

The client does **not** send:

- readiness-note text;
- FLIGHT decision basis text;
- CAPCOM approval basis text;
- free-form player commentary;
- hidden model state.

Qualitative observer notes remain in the playtest report.

## Event kinds

- `page_load`
- `join_attempt`
- `join_success`
- `auto_rejoin_attempt`
- `auto_rejoin_success`
- `auto_rejoin_failure`
- `workspace_ready`
- `station_switch`
- `action_attempt`
- `action_success`
- `action_error`

Action targets use short identifiers such as:

- `readiness_ready`
- `readiness_not_ready`
- `flight_go`
- `flight_no_go`
- `queue_capcom`
- `transmit_capcom`
- `control_delta_p_callout`
- `shutdown_evidence`

## Storage and retrieval

Events are session-scoped and in memory. Creating/resetting a session clears the playability stream.

Player clients POST events to:

`/api/session/instrumentation`

Facilitator-only retrieval is:

`/api/session/admin/playability-events`

The facilitator console LOG drawer includes **COPY PLAYABILITY LOG**.

The authoritative mission audit at `/api/session/audit` remains separate.

## Measures supported now

### Join/recovery

Derive:

- elapsed time to successful join;
- automatic-rejoin attempts and outcomes;
- repeated page loads/rejoins;
- elapsed time from page load to workspace ready.

These support the note-314 **Recovery** dimension.

### Action interaction

For each action target, compare:

- `action_attempt`;
- `action_success`;
- `action_error`;
- client elapsed time;
- authoritative GET.

These support identification of interface-induced delays and failed interactions. They do not determine whether a player's operational judgment was correct.

### Compact switching

The validation client records `station_switch` with original-station identity.

This supports later compact-role measures:

- switching frequency;
- time spent between switches when combined with event timestamps;
- correlation of wrong/failed actions with recent switches.

No inactive-station anomaly hint is added.

### Findability

The event stream does **not** directly prove that a player visually found or understood a product or rule. Findability remains a combination of:

- elapsed time to the relevant action;
- observer classification (`FOUND`, `DELAYED`, `RESCUED`, `MISINTERPRETED`);
- qualitative note identifying whether the delay came from screen organization, paper/reference organization, or operational reasoning.

Do not convert elapsed time alone into a findability score.

## Interpretation rule

Instrumentation answers **what the interface interaction took and whether it failed**. The observer determines **why**.

Use the note-314 distinction:

- operational friction should generally be preserved;
- interface friction should be repaired.

The telemetry must not become a game score or an automated diagnosis of player competence.

## Future extension boundary

Do not add high-frequency pointer tracking, keystroke capture, free-text logging, or hidden-state correlations unless a specific playability question requires them.

If CONTROL/GUIDO product switching is added to the player lab, use the same event stream and add only the minimum stable target identifiers needed to measure switching/findability.
