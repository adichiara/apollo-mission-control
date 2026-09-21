# Station research status — Apollo 11 descent LR controller workflow

Date: 2026-09-21
Parent: `docs/station-status/2026-09-21_apollo11_descent_trajectory_rules.md`

## GUIDO / Guidance

MSK-1137 now provides a documented Apollo-11 controller product containing LR range/velocity validity, body-axis LR velocity, LR slant range, PGNS altitude, and TGO. The preserved landing poll records Steve Bales responding `Go` for Guidance as a distinct front-room station call.

Kranz's retrospective operational account additionally describes the ground comparing incoming LR information with its own estimate and Bales working with a back-room guidance specialist during the descent.

**Boundary:** this does not prove an exact GUIDO arithmetic `Delta-H` display/algorithm or recover the exact GUIDO/back-room words.

## CONTROL

The preserved 20 July 1969 console recording assigns the call `We have position 2 on LR` to CONTROL Robert Carlton immediately before FLIGHT's landing go/no-go poll.

**Boundary:** LR antenna position is not interchangeable with LR data validity, LR acceptance/convergence, or Guidance readiness. Preserve these as separate states/products.

## FLIGHT

FLIGHT acknowledges the LR-position call, announces the impending landing poll, polls the front-room positions including Guidance and CONTROL separately, then directs CAPCOM after the go responses.

This supports an integrating/decision role rather than an omniscient master display.

## CAPCOM

After FLIGHT completes the poll, CAPCOM relays Mission Control's `go for landing` to the crew.

**Boundary:** CAPCOM transmits the integrated decision; the evidence does not support CAPCOM independently calculating or deciding LR acceptance.

## Current station consequence

The Apollo 11 descent reference can now preserve the historical front-room information separation while leaving the exact Mission-G ground-processing internals unresolved.

## Evidence status

- **DOCUMENTED:** MSK-1137 guidance/LR product fields; CONTROL LR-position call; separate Guidance and CONTROL poll calls; FLIGHT integration; CAPCOM relay.
- **PARTIALLY DOCUMENTED:** exact station procedure mapping from rule 5-89 to specific displayed comparisons.
- **BLOCKED:** per-field Mission-G LR source identifier, engineering conversion, and CCATS-versus-RTCC route.
- **DEFERRED:** exact GUIDO/back-room phraseology/timing until it becomes a player-facing dependency.
