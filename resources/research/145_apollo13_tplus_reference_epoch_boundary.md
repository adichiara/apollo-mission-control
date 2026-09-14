# Research note 145 — Apollo 13 `T±N` mass-properties reference-epoch boundary

Date: 2026-09-14

## Question

Can the Apollo 13 Flight Control Division Mission Operations Report distinguish the `T±N` mass-properties label from the time at which a deck/product was actually generated or loaded into RTCC?

## Primary source

NASA, Flight Control Division, *Mission Operations Report — Apollo 13*, April 28, 1970.

NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf/a13-mission-ops-report-19700428.pdf

## Finding

The Flight Dynamics prelaunch narrative states that the lift-off **`T-6` mass properties** — weights, centers of gravity, and aerodynamic data — were **generated and loaded in the RTCC by T-2:46**.

This gives two distinct time references in one mission-specific statement:

1. the mass-properties label/state: `T-6`;
2. the generation/loading completion time: `T-2:46`.

Because the product identified as `T-6` was generated/loaded at a different mission-relative time, the `T±N` label cannot simply mean the deck-generation or RTCC-loading timestamp.

Combined with the same report's later `T+25` mass-properties run, comparison against `T+6` trims, and update to `T+55` LM-burn decks, the safest interpretation is that `T±N` identifies the **mission-relative reference state/epoch represented by the mass-properties product**.

## What this resolves

The project may now retire **deck-generation time** as a live interpretation of the `T+55` label.

For simulation/data modeling, keep separate fields for:

- mass-properties reference epoch label (`T±N`);
- actual product generation/update time, when documented;
- actual RTCC load time, when documented;
- physical vehicle state;
- targeting/P30 weight values.

## Boundary retained

This evidence does **not** prove that `T+55` means an exact instantaneous physical state at precisely 55:00:00 GET. It does not distinguish among an exact reference epoch, a nominal/scheduled epoch, or a propagated computational state referenced to approximately +55 hours.

It also does not provide H-2 deck fields, module/depletion-table values, or the mapping from the `T+55` deck to the final PC+2 P30 weights.

## Next archival target

Prioritize H-2 RTCC/Flight Dynamics requirements, deck/listing definitions, processor descriptions, or maneuver-support worksheets that define how a `T±N` reference epoch was instantiated and propagated into mass/CG, trim, and targeting products.