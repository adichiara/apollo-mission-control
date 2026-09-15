# Progress — PC+2 inverter contingency on deterministic simulated crew

Date: 2026-09-15

## Purpose

Move the already-researched inverter contingency from a standalone procedural/action test into the same authoritative simulated-crew architecture used by the ΔP shutdown branch.

## Source boundary

Research notes 112–114 establish:

- PC+2 retained **inverter 2**;
- the alternate is **inverter 1**;
- Apollo 13 LM Malfunction Procedures give the transfer sequence:
  1. `CB(11) EPS: INV 1 — close`;
  2. `INVERTER — 1`;
  3. `CB(16) EPS: INV 2 — open`;
- no numeric dwell is sourced before re-observing the INVERTER caution;
- exact hypothetical controller voice routing and crew-member assignment remain unresolved.

Older repository statements that the inverter identity or transfer chronology remained unresolved are retired under D-023.

## Authoritative-session chain

Implemented chain:

`synthetic inverter caution observation`
→ `FLIGHT authorizes sourced transfer`
→ `CAPCOM queue/transmission`
→ `simulated crew receipt`
→ `sourced inverter-2 → inverter-1 crew action`
→ `crew completion report`
→ `separate fresh post-transfer caution observation`
→ `derived inverter shutdown rule`

The crew action/report does **not** alter the caution observation. Before the fresh post-transfer observation, the rule remains `not_evaluable`. A later warning observation can make it `triggered`. Rule trigger still does not issue an automatic engine-off command.

## Validation surface

The deployed `/contingency` page is expanded from a ΔP-only test into **PC+2 Contingency Tests**. The original ΔP chain remains, and a second guided inverter test exposes the new sequence step-by-step.

The 0.1-second increment used by the browser test only establishes event ordering for a fresh observation. It is explicitly not a historical response/persistence dwell.

## API additions

- `POST /api/session/flight/{player_id}/inverter-transfer`
- `POST /api/session/crew/inverter-transfer/{item_id}`
- `POST /api/session/crew/inverter-transfer-report/{item_id}`
- `GET /api/session/admin/inverter-rule` (validation-only derived rule view)

The existing generic crew-receipt endpoint now accepts any action configured in the PC+2 deterministic crew actor rather than only the ΔP shutdown callout.

## Remaining boundary

This change does not establish:

- exact TELMU/CONTROL CRT routing for the caution;
- direct ground telemetry of selector position;
- a historical failure event during Apollo 13 PC+2;
- exact controller wording/loop sequence for a hypothetical inverter failure;
- a numeric post-transfer dwell;
- automatic shutdown when the rule becomes positive.
