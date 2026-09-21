# Controller Decision-Gate Contract

Status: **implemented reusable contract + Apollo 11 partial historical profile; no automatic mission decision**

## Purpose

Represent a Mission Control decision point as a separation between:

`documented station cues → station readiness reports → controller judgment → crew relay`

without replacing the controller judgment with hidden simulator logic.

Implementation:

- `src/apollo_mission_control/decision_gate.py`
- `src/apollo_mission_control/decision_gate_profiles.py`
- `data/decision_gate_profiles/apollo11_g_descent_landing_partial.json`

## Generic contract

The reusable contract carries:

- a gate identifier and phase context;
- documented cue ownership by station;
- the source-backed poll order and historical call labels;
- the controller holding decision authority;
- the station that relays the resulting decision;
- provenance.

A runtime snapshot may attach cue observations and station readiness reports. It reports only two mechanical completeness facts:

- whether every documented cue has an explicit available observation in the snapshot;
- whether every station in the documented poll has reported.

Neither fact is a mission GO/NO-GO recommendation.

The serialized snapshot deliberately contains `controller_decision_required: true` and no `mission_decision`, `go_for_landing`, or abort result.

## Apollo 11 profile

The current Mission-G profile records the bounded topology established by research 502:

- MSK-1137 LR range/velocity `GOOD/BAD`, `VXB/VYB/VZB`, LR slant range, PGNS altitude, and TGO as GUIDO/Guidance decision cues;
- CONTROL's separate landing-radar antenna-position call;
- the preserved landing-poll order: RETRO, FIDO, GUIDANCE, CONTROL, TELCOM, GNC, EECOM, SURGEON;
- FLIGHT as decision authority;
- CAPCOM as crew relay.

The profile preserves `GUIDO` as the repository station identifier while retaining `GUIDANCE` as the historical poll label.

## Critical non-collapses

The contract does not equate:

- LR antenna position with LR data `GOOD/BAD`;
- LR data validity with LR convergence/acceptance;
- PGNS altitude with LR slant range;
- cue completeness with station readiness;
- an all-GO poll with an automatic FLIGHT decision;
- FLIGHT's decision with CAPCOM's relay.

The exact Mission-G parameter-processing path and the exact rule-5-89 comparison computation remain outside this contract.

## Historical execution boundary

This profile is sufficient to implement the **information and authority topology**, but not a complete historical landing-decision algorithm.

Still unresolved or blocked:

- exact mapping between rule 5-89 convergence/PGNS-versus-LR semantics and individual MSK-1137 fields;
- Mission-G per-field LR engineering conversion and CCATS-versus-RTCC route;
- exact GUIDO/back-room words and timing;
- exact ground `Delta-H` algorithm, if one was used.

Therefore the current profile must not be used to auto-generate a landing GO, abort, or radar-accept recommendation.

## Validation

Synthetic tests verify:

- the Apollo 11 profile preserves the documented station/call topology;
- cue and poll completeness are separate;
- even a complete all-GO poll produces no mission decision;
- unknown/duplicate poll reports are rejected;
- a profile requesting automatic decision mode is rejected;
- profile discovery IDs remain unique.

## Next integration boundary

A future Apollo 11 runtime adapter may bind sourced controller products to these cue IDs and record an explicit FLIGHT decision through the controller-decision layer. That integration should occur only after the required product values and any rule-evaluation inputs are themselves source-bounded at the player-visible resolution.
