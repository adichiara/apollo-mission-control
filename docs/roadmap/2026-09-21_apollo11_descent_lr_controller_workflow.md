# Roadmap continuation — Apollo 11 descent LR controller workflow

Date: 2026-09-21
Parent: `docs/roadmap/2026-09-21_apollo11_descent_trajectory_rules.md`

## Bounded question

What controller-visible products and front-room call topology supported Apollo 11 landing-radar decisions approaching P64 and the landing go/no-go?

## Result

Research 502 closes the current workflow boundary without claiming an exact Mission-G signal-processing route.

The Apollo 11 MSK-1137 definition documents the controller-visible guidance ingredients needed for the descent decision problem: LR range/velocity `GOOD/BAD`, LR body-axis velocities, LR slant range, PGNS altitude, and TGO.

A preserved 20 July 1969 Mission Control intercom segment from CONTROL Robert Carlton's console then supplies the front-room topology immediately before the landing poll:

`CONTROL LR position call → FLIGHT acknowledgment → station go/no-go poll (including separate Guidance and CONTROL calls) → FLIGHT decision → CAPCOM relay to crew`

Kranz's independent oral-history account supports the separate guidance function: the ground compared incoming landing-radar information with its own estimate, advised the crew whether to accept the radar, and Bales used back-room guidance support during the descent.

## Controlled implementation boundary

The Apollo 11 reference may preserve distinct station-scoped states for:

- LR measurement validity and values on the guidance-monitoring product;
- LR antenna-position state reported by CONTROL;
- Guidance readiness;
- CONTROL readiness;
- FLIGHT's integrated landing decision;
- CAPCOM's relay of that decision.

Do not collapse `LR position 2`, LR `GOOD/BAD`, LR acceptance/convergence, and PGNS-versus-LR disagreement into one boolean.

Do not implement a guessed `RNG - ALT` controller algorithm. The visible ingredients are documented; the exact Mission-G ground transformation remains blocked on named PHO-TR155/Data Formats recovery.

## Closure

This bounded workflow question is **SUFFICIENT** for current architecture under D-024. The broader Apollo 11 powered-descent reference remains **OPEN**.

## Next bounded target

Translate the documented rule semantics and station workflow into an implementation-neutral descent decision-gate contract. Reuse existing landing-radar/guidance state where possible, and add no historical constants or automatic decisions unless a source requires them.

## Sources

- `resources/research/502_apollo11_descent_lr_controller_call_workflow.md`
- Apollo 11 Flight Mission Rules, rule 5-89
- AC Electronics Apollo 11 MSK-1137 definition
- JSC Robert L. Carlton oral history / embedded 20 July 1969 console recording transcript
- JSC Eugene F. Kranz oral history
- Apollo 11 air-ground descent transcript

## Evidence status

- **DOCUMENTED:** controller display ingredients and front-room landing-poll topology.
- **PARTIALLY DOCUMENTED:** exact mapping from rule-5-89 comparison semantics to individual displayed fields.
- **BLOCKED:** Mission-G per-field LR source/engineering conversion and CCATS-versus-RTCC route.
- **DEFERRED:** exact GUIDO/back-room phraseology and timing unless a future player interaction requires it.
