# Roadmap continuation — Apollo 11 descent decision-gate contract

Date: 2026-09-21
Parent: `docs/roadmap/2026-09-21_apollo11_descent_lr_controller_workflow.md`

## Implementation dependency

The historical workflow boundary is sufficient, but the reusable engine needs a way to carry those cues and station calls without hard-coding a landing decision.

## Implemented

Added an implementation-neutral controller decision-gate contract plus a partial Apollo 11 Mission-G profile.

The generic layer can:

- identify documented station cues;
- preserve historical poll order/call labels;
- accept station readiness reports;
- expose cue/poll completeness for audit and UI scaffolding;
- preserve FLIGHT decision authority and CAPCOM relay ownership.

It cannot produce a mission GO/NO-GO result.

The Mission-G profile supplies the source-backed Apollo 11 topology from research 502 and leaves unresolved comparison/processing details explicit.

## Boundary preserved

No new historical threshold, timing value, ground-processing route, or `RNG-ALT` calculation is introduced.

An all-GO station poll remains evidence available to FLIGHT, not an automatic simulator decision.

## Next bounded target

Bind already sourced Apollo 11 controller products into the decision-gate cue contract at a non-runtime proof level first. Specifically determine which existing LR/guidance model outputs can legitimately populate MSK-1137-style cue values and which still require a distinct ground/display adapter.

Do not implement the historical landing decision or a full `apollo11_descent_v1` runtime until those product mappings are source-bounded.

## Evidence status

- **DOCUMENTED:** Apollo 11 station/call topology represented by the profile.
- **IMPLEMENTED:** generic non-decision gate contract and profile validation.
- **PARTIALLY DOCUMENTED:** rule-to-cue mapping.
- **BLOCKED:** exact Mission-G LR parameter processing/provenance.
