# Roadmap addendum — player interaction and playability workstream

Date: 2026-09-18  
Parent: `docs/ROADMAP.md`

## Direction change

Player-facing UI implementation remains downstream of historical/product boundaries, but **playability and interaction design no longer need to be completely deferred** while causal-engine research continues.

Research note 313 separates two kinds of difficulty:

- operational friction that belongs in the simulation;
- interface friction that should be removed as a modern design defect.

This permits useful work now without freezing a final historical console rendering.

## Immediate workstream

1. Audit existing player-client controls for scenario hints, test-harness leakage, and developer terminology.
2. Instrument live play to classify findability, interpretation, coordination, temporal, compact-role, and recovery problems.
3. Prototype FLIGHT/CAPCOM interaction structure first; they are less dependent on exact dense CRT reconstruction.
4. Prototype CONTROL/GUIDO phone product layouts using the already constrained minimum product sets.
5. Keep source/model provenance visible in model-proof/facilitator/debrief tooling, not automatically in final player products.
6. Keep exact pixel/character reconstruction optional until physical play shows that it materially improves or harms controller work.
7. Run seven-seat nominal human play before the synthetic contingency, then five-player compact play.
8. Feed only concrete historical gaps back into the research queue.

## Specific current-client risks

- permanent branch-specific CONTROL shutdown action can reveal the ΔP exercise;
- player-facing `ASSESS SHUTDOWN EVIDENCE` is validation scaffolding rather than controller work;
- generic `validity · source_layer` labels are developer/model metadata unless a product-specific historical analogue is sourced;
- compact navigation needs testing under continuous GET.

## Pacing

Do not use time acceleration as the first remedy for idle time or long setup. Prefer:

- tighter case boundaries;
- part-task familiarization;
- shorter onboarding cases;
- concurrent station work.

Any later time-scale feature remains a separate decision because simulation speed changes workload.

## No implementation claim

This addendum does not accept a final UI, voice-loop system, acceleration policy, or display-density rule. It establishes the next design/test sequence.
