# Station research-status addendum — INCO / FLIGHT / CAPCOM presentations

Date: 2026-09-12

## INCO

**Maturity remains B.**

Improved:

- minimum PC+2 player view now exposes separate link quality, voice availability, telemetry availability, ranging state, and uplink state;
- the 78:21:54 ranging-verification dependency is represented without reconstructing antenna geometry or a detailed INCO CRT.

Still unresolved / deferred:

- exact INCO CRT identifiers/layout;
- antenna look-angle presentation;
- detailed S-band/RF configuration beyond what the player decision needs.

## FLIGHT

**Maturity remains B.**

Improved:

- first-pass player view now preserves mission phase and explicit GO-for-burn decision state;
- no omniscient subsystem-health summary is exposed.

Still unresolved / deferred:

- controller readiness-report stream, which is now explicitly a session-layer requirement;
- exact historical console presentation.

## CAPCOM

**Maturity remains B.**

Improved:

- first-pass player view now exposes air-ground condition, final PC+2 PAD/procedure material, and crew-report stream;
- CAPCOM remains a communications/procedure role rather than a hidden systems-data role.

Still unresolved / deferred:

- controller-to-CAPCOM callout queue;
- explicit readback tracking;
- exact historical console presentation.

## Research stop condition

The player-facing presentation layer is sufficient for first-slice integration. Further station-display research should be triggered only by a concrete integration, usability, or player-decision problem.
