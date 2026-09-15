# Progress — site-facing causal model lab

Date: 2026-09-15

## Purpose

Keep causal-engine development inspectable through the existing deployed validation surface rather than allowing reusable models to become API-only infrastructure.

## Implemented

The existing `/model-tests` page has been expanded from a DPS-only runner into a **Causal Model Lab**.

It now exposes three model-proof surfaces:

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

The admin MODEL drawer now links to the Causal Model Lab while keeping the fast single-burn proof available in-place.

## Validation boundary

The UI repeatedly identifies these as synthetic, not historically validated model proofs.

The browser does not provide a way to force downstream electrical-source state inside the composed resource-power chain. The server remains authoritative for causal coupling.

## Forward rule

As additional reusable causal-engine domains become useful enough for active development, their facilitator-facing proof should be added to the existing Causal Model Lab (or a clearly linked successor section) at the same time the model/API proof is integrated.

This is validation/test presentation, not the eventual historical player station UI.
