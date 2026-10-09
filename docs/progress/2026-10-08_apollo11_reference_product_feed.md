# Progress — Apollo 11 reference-event controller-product feed

Date: 2026-10-08

## Implemented

Added a source-bounded reference feed on top of the existing Apollo 11 descent controller-product schema.

The initial feed contains only:

- `program.alarm_latest` at the Mission Report 1201/1202 computer/event anchors;
- `program.number` at the Mission Report P64/P66 entry anchors.

No other controller product is populated.

## Timing boundary

Each feed event retains:

- source GET;
- source GET text;
- project activation GET;
- event label;
- field-scoped provenance.

For this first profile, project activation GET equals the source-event GET solely to make deterministic reference playback possible.

The feed explicitly reports:

`historical_ground_display_timing_claimed = false`

Exact Mission-G ground-display availability, routing, refresh cadence, and latency remain unresolved. The project activation time is not evidence for any of them.

## Hidden-state boundary

The feed is loaded from its own explicit data fixture and passes values through the existing Apollo 11 controller-product projector.

It does not read:

- scenario `program.*` variables;
- AGC hidden state;
- landing-radar estimator state;
- runtime alarm state;
- FLIGHT/CAPCOM decisions.

Known but unsupplied product fields remain unavailable.

## Site-facing proof

Added:

- `/api/admin/model-proof/apollo11-reference-product-feed`;
- Causal Model Lab section **Apollo 11 reference-event controller-product feed**;
- buttons for first 1202, P64, 1201, and P66 reference anchors.

The trace shows:

`source event -> project reference activation -> explicit products -> timing boundary`

## Not yet player-facing

No station ownership is assigned by this feed.

The exact Mission-G request/routing evidence remains blocked, and the existing player-interaction roadmap still requires human playability evidence before expanding CONTROL/GUIDO phone views.

## Next

Use the facilitator/reference feed during the existing playability/test workflow. If the product representation is understandable without hidden-state assumptions, select the minimum player-facing subset explicitly rather than exposing the full MSK-1137 schema.
