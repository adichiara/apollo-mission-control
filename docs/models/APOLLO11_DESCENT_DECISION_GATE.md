# Apollo 11 Descent Decision-Gate Contract

Status: **implemented bounded contract; not an automatic landing-decision algorithm**

## Purpose

Translate research note 502 into a reusable software boundary without inventing the
Mission-G ground LR comparison algorithm or collapsing distinct controller states.

The documented chain represented here is:

`controller-visible LR state + station interpretation/readiness -> FLIGHT decision -> CAPCOM relay`

The implementation is in:

- `src/apollo_mission_control/descent_decision_gate.py`
- `tests/test_descent_decision_gate.py`

## Preserved distinctions

The contract keeps the following separate:

- LR range-data `GOOD/BAD`;
- LR velocity-data `GOOD/BAD`;
- LR antenna position, including the documented CONTROL `position 2` call;
- LR body-axis velocity values;
- LR slant range;
- PGNS altitude;
- TGO;
- Guidance readiness;
- CONTROL readiness;
- FLIGHT's integrated decision;
- CAPCOM's air-ground relay.

No one of these fields silently sets another.

In particular:

- `antenna_position == 2` does not imply LR data good;
- LR data good does not imply convergence/acceptance;
- Guidance and CONTROL GO calls do not automatically create a FLIGHT GO;
- FLIGHT GO does not itself mean CAPCOM has relayed it;
- CAPCOM relay does not change spacecraft state.

## Historical boundary

Research 502 establishes that Apollo 11 MSK-1137 exposed LR range/velocity validity,
LR body-axis velocities, LR slant range, PGNS altitude, and TGO. A preserved
20 July 1969 Mission Control console recording assigns the LR position-2 call to
CONTROL, then records a separate Guidance response in FLIGHT's landing poll before
FLIGHT directs CAPCOM to transmit the landing GO.

The exact Mission-G per-field LR source route, engineering conversion, and any ground
Delta-H computation remain unresolved/BLOCKED on the previously identified
PHO-TR155/Data Formats material. This module therefore contains **no** inferred
`RNG - ALT` decision rule and no historical numerical threshold beyond what is
already modeled in source-backed lower layers.

## What the contract does

It records a station/communication snapshot and provides only two derived checks:

1. whether the currently modeled Guidance and CONTROL readiness calls are explicit;
2. whether an already-recorded CAPCOM relay is consistent with an already-recorded
   FLIGHT decision.

Neither check decides whether Apollo should land.

## Site-facing proof

The Causal Model Lab now exposes this contract directly, including the sourced
automatic→manual/P66 authority transition.

The paired proof holds the controller-visible LR snapshot, Guidance readiness,
CONTROL readiness, FLIGHT decision, and CAPCOM relay constant while changing only
`control_mode`. The result demonstrates that trajectory/guidance abort constraints
are applicable in automatic control but are not themselves abort causes after manual
takeover under Apollo 11 Flight Mission Rule 5-11.

The proof does not infer P66 entry, an abort, a landing GO/NO-GO, or a CAPCOM relay.
Those remain explicit scenario/controller events.

## Evidence status

- **DOCUMENTED:** station-product ingredients and FLIGHT -> CAPCOM landing-poll topology.
- **PARTIALLY DOCUMENTED:** mapping from Mission Rule 5-89 comparison semantics to
  individual displayed fields.
- **BLOCKED:** exact Mission-G per-field LR provenance/engineering conversion.
- **DEFERRED:** exact GUIDO/back-room phraseology/timing until player interaction
  requires it.
