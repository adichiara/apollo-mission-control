# Apollo 11 Descent Controller-Product Boundary

Status: **implemented source-backed field schema; exact Mission-G routing remains partially unresolved**

## Purpose

Define the Apollo 11 powered-descent controller-product boundary without filling missing
controller-visible values from hidden simulator state or guessing exact Mission-G
CCATS/RTCC/display-database routing.

Implementation:

- `src/apollo_mission_control/apollo11_descent_products.py`
- facilitator proof endpoint: `/api/admin/model-proof/apollo11-descent-products`
- Causal Model Lab: **Apollo 11 descent controller-product boundary**

## Source basis

Research note 502 establishes the descent landing-radar/controller workflow and the
MSK-1137 LR field family used in the front-room decision context.

Research note 600 extends the Apollo-11-specific MSK-1137 inventory with descent
timing, warning/caution, alarm-code, restart-count, computer-program, and DSKY fields.

The Apollo 11 LUMINARY 099 downlink evidence separately establishes an explicit landing-
radar velocity/altitude downlink family. It does **not** establish a one-to-one Mission-G
ground conversion/routing from those words to each displayed MSK-1137 field.

## Contract

The projector accepts an explicit mapping of controller-visible values.

Known fields that are not supplied are returned as **unavailable**. The projector does
not read authoritative spacecraft state, AGC memory, the landing-radar estimator, or any
other hidden model layer.

Unknown keys fail explicitly.

Each field also carries a routing-status classification:

- `downlink_family_route_unresolved` — Mission-G spacecraft downlink family is
  documented, but exact ground conversion/display routing is not;
- `mixed_downlink_rtcc_unresolved` — the field belongs to the documented ground display
  family but the current evidence does not permit choosing D/L versus RTCC/ground
  processing;
- `field_semantics_only` — field meaning is source-backed, exact ground route remains
  unresolved;
- `controller_reported` — source evidence establishes a controller call rather than a
  hidden telemetry product.

These statuses are evidence boundaries, not runtime failure states.

## Current field family

The schema currently covers the source-backed subset needed by the Apollo 11 descent and
program-alarm architecture:

- LR range-data GOOD/BAD;
- LR velocity-data GOOD/BAD;
- LR body-axis VXB/VYB/VZB;
- LR slant range;
- PGNS altitude;
- TGO;
- descent time-to-end-of-phase;
- LGC / ISS warnings;
- PGNCS / program cautions;
- first, second, and latest alarm codes;
- restart count;
- active computer program;
- DSKY verb, noun, and flasher;
- CONTROL LR antenna-position report.

## Preserved distinctions

The schema deliberately does not:

- compute `Delta-H` from LR range and PGNS altitude;
- equate CONTROL's LR-position call with LR validity or acceptance;
- infer alarm disposition from an alarm code;
- assign exact GUIDO/CONTROL display ownership from field availability;
- choose D/L versus RTCC when Mission-G routing is unresolved;
- treat unavailable values as zero, false, or nominal;
- infer FLIGHT or CAPCOM actions.

Those belong to separate causal, station, or human-decision layers.

## Next dependency

The product schema is sufficient for the current architecture and Causal Model Lab.

The next Apollo 11 controller-product work should be driven by one of these conditions:

1. recovery of Mission-G-effective per-field routing/external-name/computation identifiers;
2. a concrete player-facing CONTROL/GUIDO product prototype requiring a subset of this
   field family;
3. a sourced decision rule requiring additional controller-visible inputs.

Until then, exact DRK/FDK mapping, request cadence, channel identity, and display timing
remain source-gated rather than implementation assumptions.
