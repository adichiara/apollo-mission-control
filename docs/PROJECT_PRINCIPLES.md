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

Historical research is complete enough for a feature or phase when the evidence establishes the behavior that materially affects controller work and the remaining gaps can be isolated explicitly.

Do not keep drilling into one topic merely because some archival detail remains unresolved. Move on when one or more of these conditions applies:

- the next evidence appears to require inaccessible or obscure archival material;
- repeated searches are returning the same sources rather than new evidence;
- the unresolved detail has little effect on player decisions or simulation behavior;
- the uncertainty can be represented honestly as unresolved without forcing invented behavior;
- another project area has substantially higher expected value.

A blocked detail should be logged with the best known evidence, its likely implementation impact, and the source that would resolve it if later found.

Research may return to a deferred gap when implementation reveals that it is actually consequential.

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
