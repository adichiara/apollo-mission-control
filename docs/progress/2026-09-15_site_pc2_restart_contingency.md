# Progress — site-facing PC+2 premature-stop restart validation

Date: 2026-09-15

## Purpose

Expose the existing source-bounded premature-stop restart branch on the same deployed contingency-test surface used for ΔP and inverter validation.

## Implemented

`/contingency` now includes a guided restart section with:

1. synthetic premature engine stop with cause affirmatively classified outside the listed shutdown criteria;
2. conservative restart disposition;
3. the prebriefed crew sequence: PRO on Noun 97 → manual ullage → Engine Start → Descent Engine Command Override on;
4. separate explicit physical restart response;
5. final audit check that no post-stop FLIGHT/CAPCOM instruction was invented.

Two one-button negative tests are also exposed:

- unknown stop cause remains `INSUFFICIENT_CONTEXT` and blocks the crew procedure;
- a listed shutdown criterion produces `DO_NOT_RESTART_RULE_SHUTDOWN` even if the synthetic non-rule flag is also true.

## Causal boundary

Crew procedure steps do not set `engine_running=True`. The vehicle response remains a separate event.

The physical restart response deliberately leaves restart thrust level unspecified. No restart delay, thrust transient, chamber-pressure rise, or success probability is synthesized.

## Validation role

This is facilitator/test infrastructure, not a claim that Apollo 13 experienced a premature PC+2 engine stop. It makes the existing restart architecture inspectable on the deployed site and complements the automated HTTP tests.
