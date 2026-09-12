# Station research-status addendum — first playable session integration

Date: 2026-09-12

## Overall

Historical maturity grades do not change in this pass. The change is architectural: researched station information is now routed through one authoritative playable-session layer.

## CONTROL / GUIDO / TELMU / FIDO-RETRO / INCO

**Maturity remains B** for the first-slice implementation boundary.

Improved:

- each station now has a session-scoped player view selected from its own controller projection;
- station assignment prevents the first prototype from exposing another discipline's products by default;
- readiness decisions can be reported to the session without mutating vehicle state.

## FLIGHT

**Maturity remains B.**

Improved:

- the 79:17 final GO/NO-GO point is now an explicit gameplay decision gate;
- FLIGHT must record GO before the session can advance toward P40;
- the FLIGHT decision audit captures the latest controller readiness reports rather than calculating GO automatically.

Remaining integration work:

- render readiness reports directly in the FLIGHT player presentation;
- represent later discipline assessments/callouts through the same event layer.

## CAPCOM

**Maturity remains B.**

Improved:

- an explicit FLIGHT-approved CAPCOM queue now exists;
- CAPCOM transmission is a separate player/session action;
- queued/transmitted communications do not directly mutate spacecraft truth.

Remaining integration work:

- surface queue state in the CAPCOM presentation;
- connect specific transmitted procedures/callouts to the existing procedural communication helpers where appropriate.

## Research stop condition

No station requires additional historical display research before the next integration milestone. New research should be opened only when the playable session exposes an ambiguity that affects player information or decisions.
