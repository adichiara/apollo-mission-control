# Station research-status addendum — PC+2 CONTROL player presentation

Date: 2026-09-12

## CONTROL

**Maturity remains B.**

Improved:

- mission-specific MSK 1123/1137 evidence now directly constrains the first player-facing CONTROL presentation;
- the minimum PC+2 CONTROL product set has a concrete presentation model;
- exact historical semantics are preserved where known, including the fact that MSK 1137 `TCP` is a percent quantity;
- the sourced GQ6510P psi measurement is therefore deliberately presented as a project field rather than falsely labeled `TCP`;
- deferred implementation gaps are omitted rather than shown as failed telemetry;
- hidden integrity metadata remains outside the player view.

Still unresolved:

- exact CONTROL CRT selection/request behavior during PC+2;
- exact field coordinates for the executable product subset;
- exact GQ6510P-to-MSK-1137 TCP engineering conversion;
- exact display placement of the ground-only fuel/oxidizer ΔP criterion;
- exact display routing for the modeled CES/gimbal/attitude/rate subset;
- refresh cadence and controller display-switching sequence.

## GUIDO

**Maturity remains B.**

No direct implementation change in this pass. The CONTROL presentation pattern establishes the next useful task: build a corresponding GUIDO view while preserving the stronger LGC/PGNS provenance already recovered for MSK 1123/1137.

## FLIGHT / CAPCOM / TELMU / INCO / FIDO-RETRO

No maturity change.

## Research consequence

Do not pursue exact CONTROL CRT coordinates merely for visual authenticity. The current evidence is sufficient for a usable, provenance-preserving player interface. Reopen exact layout/routing only where it changes a controller decision or is cheaply recoverable from a primary source.
