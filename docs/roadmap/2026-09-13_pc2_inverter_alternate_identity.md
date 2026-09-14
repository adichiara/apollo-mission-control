# Roadmap Addendum — PC+2 inverter alternate identity

Date: 2026-09-13

## Resolved boundary

Research note 113 closes the remaining inverter **identity** gap left by note 112.

Primary-source chain:

1. Apollo 13's mission-specific PC+2 read-up retains **inverter 2** and scratches the normal `Select Inverter 1` step.
2. The contemporaneous burn rule says to judge an inverter caution after **switching inverters**.
3. The LM Operations Handbook documents **two identical redundant inverters**.

Therefore, from the sourced PC+2 starting state, the other redundant inverter is necessarily **inverter 1**.

First-playable representation may now use:

`inverter 2 → warning → crew transfer attempt to inverter 1 → fresh warning observation → persistent warning means shutdown`

## Scope guardrail

Only the inverter identity is closed. Do not reconstruct or imply unsupported details of:

- exact switch/circuit-breaker chronology;
- reset steps;
- transfer duration or persistence dwell;
- crew-member assignment;
- ground visibility of the selector position;
- TELMU/CONTROL display-field identity;
- exact hypothetical controller call wording.

## Roadmap effect

This archival refinement does not change the primary first-playable priority. The next major boundaries remain physical seven-seat nominal execution, synthetic ΔP contingency validation, and five-player compact execution. Historical research should continue only where it closes a concrete decision or implementation dependency.
