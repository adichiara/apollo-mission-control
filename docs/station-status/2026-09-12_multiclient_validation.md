# Station research status — integrated multi-client validation

Date: 2026-09-12

## Status

**VALIDATION ARCHITECTURE ESTABLISHED — live network/phone execution pending**

## Cross-station boundary

Primary Apollo-era simulation-training evidence supports exercising controller roles together in a mission-like environment rather than validating each station only in isolation.

For the first playable PC+2 slice, integrated validation therefore treats these station surfaces as distinct clients over one authoritative mission state:

- FLIGHT;
- CONTROL;
- CAPCOM;
- GUIDO;
- additional station clients as needed during live smoke testing.

Facilitator/SimSup remains separate from every controller station.

## Information-boundary checks now covered

- FLIGHT receives readiness-report aggregation that ordinary subsystem stations do not.
- CAPCOM receives the approved communication queue that ordinary subsystem stations do not.
- CONTROL receives its own product/rule/evidence view and does not receive the CAPCOM queue representation.
- GUIDO remains on its own guidance presentation and does not receive CAPCOM/FLIGHT operational collections.
- player reload/rejoin preserves an existing player/station assignment without permitting silent station switching or takeover of an occupied station.
- facilitator-only lifecycle, pause, injection, crew/vehicle validation, and audit operations remain unavailable to ordinary station clients when authorization is configured.

## Nonnominal integration check

The new multi-client test/harness crosses station and facilitator boundaries explicitly:

`facilitator source injection → CONTROL callout → CAPCOM queue/transmission → facilitator-modeled crew receipt/command/vehicle response → crew report + fresh pressure observation → CONTROL evidence assessment`

No stage implies the next automatically.

## Historical limits

- Browser clients are project infrastructure, not historical consoles.
- HTTP concurrency is not presented as an Apollo mechanism.
- Facilitator-token authorization is modern infrastructure.
- The 26 psi ΔP and 100 psi post-command pressure values used by validation remain synthetic and non-historical.

## Remaining station-validation work

- execute simultaneous real-phone/browser clients against one server;
- check station readability and interaction under continuous GET;
- verify reload/rejoin on actual mobile browsers;
- verify FLIGHT/CAPCOM handoff ergonomics during live play;
- verify no station presentation leaks another station's operational collections;
- expand the multi-client smoke set only when live testing exposes a concrete need.

See research note 089 and `resources/source-catalog/INTEGRATED_SIMULATION_VALIDATION_SOURCES.md`.
