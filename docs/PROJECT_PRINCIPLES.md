# Project Principles

## 1. Document first, design second

Before implementing an Apollo-specific feature, determine how it actually worked from primary or near-primary documentation.

Preferred evidence order:

1. Mission-specific primary documents: mission rules, flight plans, mission reports, controller documentation, procedures, checklists, transcripts, console/display documentation.
2. NASA/JSC technical reports and Apollo Experience Reports.
3. Contemporary contractor documentation.
4. NASA oral histories and technical debriefings.
5. Secondary sources for discovery/context only when stronger sources are unavailable.

## 2. Do not invent historical behavior

Every historical claim used by the simulation should be classifiable as:

- **DOCUMENTED** — directly supported by source material.
- **PARTIALLY DOCUMENTED** — some required details are supported; others remain unresolved.
- **UNRESOLVED** — documentation has not yet been found or is insufficient.

Unresolved details are brought forward for an explicit project decision. They are not filled in automatically.

## 3. Do not simplify before understanding the real system

Simplification is a separate design decision from historical research.

First establish the real workflow, information, responsibilities, and complexity. Then decide whether simplification is required for a particular player count or practical constraint.

Any simplification that changes documented Apollo behavior should be recorded in the decisions log.

## 4. Research to sufficiency, not exhaustion

Historical research is judged against a **bounded research question and a current implementation dependency**, not against an entire subject area.

A question is **SUFFICIENT** when the evidence supports every decision-relevant behavior needed at the current implementation resolution, each remaining gap has an explicit non-blocking disposition, material source conflicts are settled or exposed, and a focused closure challenge finds no new evidence that changes the implementation conclusion.

Research may also stop as **DEFERRED** when no current dependency justifies more work, or **BLOCKED** when a material dependency remains but the next discriminating evidence has a concrete access barrier. Neither state licenses invented historical behavior.

Sufficiency does not mean historical completeness and does not upgrade an `UNRESOLVED` claim. Reopen research only when a defined trigger makes the gap materially relevant again.

The operational gate, thread states, closure record, and reopen triggers are defined in `docs/RESEARCH_SUFFICIENCY.md` and decision D-024.

## 5. The simulation should not feel game-like

The software should present the controller's work rather than an external game layer.

Avoid, unless historically justified:

- scores during play
- achievement notifications
- artificial damage/health meters
- quest markers
- unsolicited diagnostic hints
- color-coded game alerts
- arbitrary "easy/normal/hard" mechanics
- telling the player the correct decision

Player skill should come from understanding the station, interpreting data, applying rules and procedures, making decisions, and communicating effectively.

## 6. Mission outcome hierarchy

The objective is mission success. If mission objectives can no longer be achieved, the priority becomes the best historically valid alternate/contingency outcome and ultimately safe return of the astronauts.

An abort is a mission-control action available only where the spacecraft state, mission phase, procedures, and rules make it applicable. It is not a generic success condition.

## 7. Information boundaries matter

A controller should receive the information historically available to that role, through historically appropriate displays and communications to the extent practical.

The underlying authoritative simulation state is not itself a player display.

## 8. Paper documentation is part of the interface

Printed station references are intended to be functional working documents, not props. Flight rules, procedures, tables, and controller references should be based on the corresponding historical sources.

## 9. Provenance is part of implementation

Research notes should identify the source and, where possible, document/page/section used to justify an implementation.

The source catalog is maintained under `resources/`.
