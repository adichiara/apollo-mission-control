# Progress — live-device / human-play validation preparation

Date: 2026-09-12

## Completed in this pass

- Researched the remaining live-device/human-play boundary using primary Apollo/NASA simulation-training sources first.
- Confirmed that Apollo training integrated mission simulators with Mission Control for combined crew/ground-controller training.
- Confirmed that flight-controller simulation emphasized mission-environment decisionmaking, controller interfaces, procedure use, and readiness rather than isolated display inspection.
- Kept browser/mobile mechanics, facilitator credentials, reload behavior, and usability criteria explicitly modern project infrastructure.
- Added research note 090.
- Added `resources/source-catalog/LIVE_HUMAN_PLAY_VALIDATION_SOURCES.md`.
- Added `docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md` with separate nominal and synthetic ΔP runs, pass criteria, defect classification, and a report template.

## Key project decision

The first live validation is a structured mission rehearsal, not an open-ended UI review.

The minimum run uses separate human FLIGHT, CONTROL, CAPCOM, and GUIDO clients plus a separate facilitator, one authoritative server, continuous GET, normal station information boundaries, and no out-of-band facilitator coaching that supplies hidden mission information.

UI/network defects and historical/research gaps must be classified separately. Player uncertainty alone is not evidence that a historical behavior or procedure is missing.

## Physical execution status

**NOT YET EXECUTED.**

The new protocol is ready, but this repository/tool environment cannot substitute for several actual phones/browsers and human operators. No live-device PASS claim is recorded.

## Current stopping point

Execute `docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md` against a dedicated authoritative server.

Run nominal PC+2 first. Repair blocking real-device/usability defects and add regression coverage where reproducible. Then run the existing synthetic ΔP branch. Reopen historical research only for concrete operational dependencies exposed by play.
