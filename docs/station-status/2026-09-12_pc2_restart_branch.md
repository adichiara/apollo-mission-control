# Station research-status addendum — PC+2 premature shutdown/restart

Date: 2026-09-12

## CAPCOM

**Maturity remains B.**

Improved:

- contemporaneous PC+2 transcript now anchors the crew-facing premature-shutdown restart sequence;
- restart procedure is recognized as pre-briefed before ignition rather than requiring an invented post-stop authorization exchange.

Still unresolved:

- exact timing/voice behavior if the contingency had actually occurred;
- whether any additional ground confirmation would have been voiced before crew action in a real failure.

## CONTROL

**Maturity remains B.**

Improved:

- ground shutdown-rule evaluations now participate in restart eligibility: a listed-rule shutdown is explicitly excluded from the restart contingency;
- ground-only ΔP remains especially important because the crew could not independently determine that criterion from the documented rule.

## GUIDO

**Maturity remains B.**

Improved:

- LGC/ISS/program-alarm shutdown criteria are explicitly treated as reasons that block the generic restart branch when triggered.

## FLIGHT

**Maturity remains B.**

Improved:

- restart eligibility can be surfaced as controller/audit context without creating an omniscient automatic restart command;
- no unsupported mandatory post-stop FLIGHT approval step has been added.

## Research consequence

The next high-value station interaction is the explicit **ground-only fuel/oxidizer ΔP callout**. It creates a genuine information asymmetry: CONTROL can hold decisive information the crew does not independently possess under the documented PC+2 rule set.
