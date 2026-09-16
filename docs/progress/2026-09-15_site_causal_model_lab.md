# Progress — site-facing causal model lab

Date: 2026-09-15

## Purpose

Keep causal-engine development inspectable through the existing deployed validation surface rather than allowing reusable models to become API-only infrastructure.

## Implemented

The existing `/model-tests` page has been expanded from a DPS-only runner into a **Causal Model Lab**.

It now exposes reusable model-proof surfaces including:

1. **DPS numerical suite**
   - preserves the existing shareable synthetic regression suite;
   - retains complete request/response capture and report export.

2. **Trajectory → tracking observation**
   - calls `/api/admin/model-proof/trajectory-tracking`;
   - exposes synthetic trajectory/propulsion inputs and observation delay/bias/availability;
   - shows authoritative trajectory and controller-visible observation separately;
   - preserves the geometric-truth layer as an explicit intermediate boundary.

3. **Resource → power → observation**
   - calls `/api/admin/model-proof/resource-power-observation`;
   - displays remaining resource, derived source availability, receiver supply state, and downstream tracking availability;
   - includes a before/after-depletion comparison that demonstrates model-to-model consequence propagation.

4. **Guidance comparison / consensus**
   - calls `/api/admin/model-proof/guidance-crosscheck` and `/api/admin/model-proof/guidance-consensus`;
   - displays independent observations, residual/freshness relationships, and consensus topology separately;
   - never selects hidden truth, diagnoses a failed source, or issues a mission decision.

5. **Landing-radar quality → update eligibility**
   - calls `/api/admin/model-proof/landing-radar-quality-update`;
   - preserves the boundary from raw Data Good/channel state through qualification and qualified measurement into update eligibility;
   - rejects implicit unit conversion at the API boundary.

6. **Guidance-computer alarm → restart recovery**
   - calls `/api/admin/model-proof/guidance-alarm`;
   - exposes caller-supplied alarm/restart classification and restart-protection configuration;
   - shows alarm indication/restart/recovery state without producing an abort/continue decision.

7. **Exercise malfunction → explicit causal insertions**
   - calls `/api/admin/model-proof/malfunction-plan`;
   - allows one exercise-level malfunction to expand into multiple explicit layer/target insertions;
   - supports manual, preprogrammed, and time-dependent scheduling;
   - never applies downstream effects or emits a diagnosis/outcome.

The admin MODEL drawer now links to the Causal Model Lab while keeping the fast single-burn proof available in-place.

## Validation boundary

The UI repeatedly identifies these as synthetic, not historically validated model proofs.

The browser does not provide a way to force downstream electrical-source state inside the composed resource-power chain. The server remains authoritative for causal coupling.

## Forward rule

As additional reusable causal-engine domains become useful enough for active development, their facilitator-facing proof should be added to the existing Causal Model Lab (or a clearly linked successor section) at the same time the model/API proof is integrated.

This is validation/test presentation, not the eventual historical player station UI.


8. **PC+2 correct / late / omitted / wrong action matrix**
   - calls `/api/admin/model-proof/pc2-action-consequences`;
   - runs four isolated authoritative reference sessions;
   - proves timely GO, missed-milestone late GO, omitted GO, and wrong-actor GO produce different downstream state/audit outcomes;
   - defines “late” only as D-016 missed-event ordering, not as a historical grace-period threshold.


9. **Apollo 11 historical guidance-monitoring profile**
   - loads the historical profile through the protected model-proof API;
   - shows 10-Hz MSFN tracking input and 0.2/0.4-s PFP processing/time-tag cadence recovered from MSC Internal Note 69-FM-36;
   - explicitly displays the historical execution gate as blocked because processor cadence is not an inter-source freshness rule;
   - retains `max_time_separation_s = null` for all Apollo 11 comparisons.
