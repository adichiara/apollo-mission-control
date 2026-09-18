# Progress — player interaction and playability workstream

Date: 2026-09-18

## Completed

- Started player-interaction/playability work in parallel with the causal-engine and archival-recovery tracks without freezing a final historical station UI.
- Added research note 313 separating **operational friction** that belongs in the simulation from **interface friction** introduced by the modern implementation.
- Audited the current player client and identified three important final-interface hazards:
  - branch-specific CONTROL shutdown controls can reveal the synthetic contingency;
  - `ASSESS SHUTDOWN EVIDENCE` is validation scaffolding rather than controller work;
  - generic `validity · source_layer` metadata is useful for model verification but is not automatically controller-facing vocabulary.
- Added a working player-interaction design document covering phone layout, station/product hierarchy, communication/action verbs, compact-role switching, paper-reference use, onboarding, pacing, and debrief.
- Extended the live-play protocol/report so future physical runs distinguish **OPERATIONAL_FRICTION** from **INTERFACE_FRICTION** and capture findability, branch-hint exposure, compact-role switching, wrong-station actions, facilitator UI rescues, and rejoin/orientation problems.
- Added modern post-run 1–7 usability ratings as research evidence only; they are not mission scores or historical Apollo criteria.
- Activated this workstream in the canonical roadmap and added open interface questions around display density, scenario-neutral action grammar, push-vs-polling need, and inactive compact-substation awareness.
- Added modern NASA human-factors sources as design guidance only, explicitly separated from Apollo historical evidence.

## Current design rule

**Preserve operational difficulty; remove interface difficulty.**

A player may legitimately struggle because evidence is incomplete, another discipline owns needed information, GET keeps advancing, or a rule requires judgment.

A player should not struggle because the active original station is ambiguous, project-internal metadata is exposed, a malfunction-specific button gives away the exercise, or browser/navigation behavior gets in the way of the controller job.

## Interface direction

The candidate player interface is now treated as three layers:

1. **modern session strip** — original station identity, GET, phase, connection state, compact-role active station;
2. **station product area** — the dominant decision-relevant controller products;
3. **small contextual communication/action area** — readiness, report/callout/recommendation, FLIGHT disposition, CAPCOM transmission, and truly station-owned configuration actions.

This is a design framework, not an accepted final UI.

## Next

1. Finish repository reconciliation/CI for this workstream.
2. Prototype FLIGHT and CAPCOM interaction first because their gameplay depends more on coordination than exact CRT reconstruction.
3. Prototype CONTROL/GUIDO phone scanning with stable product layouts while keeping information content unchanged.
4. Keep final station UI free of branch-specific solution buttons and developer-only model metadata.
5. Continue Section 7 / Volume I archival retrieval in parallel; no new public Section 7 scan was recovered in this pass.
6. Run seven-seat nominal human play before the synthetic contingency; then repeat in five-player compact mode.
