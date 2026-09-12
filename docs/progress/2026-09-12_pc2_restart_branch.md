# Progress — PC+2 premature shutdown / restart branch

Date: 2026-09-12

## Completed

- Researched the PC+2 premature DPS shutdown/restart branch using mission-specific primary sources.
- Confirmed the governing distinction: restart applied only when an early shutdown was **not** caused by one of the listed shutdown criteria.
- Recovered the crew-facing in-burn restart sequence from the contemporaneous NASA transcript: flashing Noun 97 → PRO → manual ullage → Engine Start push → Descent Engine Command Override on.
- Kept this distinct from the earlier backup procedure for failure to ignite at TIG.
- Added `resources/research/067_pc2_premature_shutdown_restart_branch.md`.
- Added `resources/source-catalog/PC2_RESTART_SOURCES.md`.
- Added `src/apollo_mission_control/restart_logic.py`.
- Extended operational-action state with restart ullage, Engine Start push, and Descent Engine Command Override actions.
- Added a procedural communication helper for the pre-briefed restart sequence.
- Added `tests/test_pc2_restart.py`.
- Tightened restart logic after review: absence of a modeled trigger is not enough to authorize restart because several historical criteria remain `NOT_EVALUABLE`; eligibility now requires affirmative classification that the stop cause is outside the listed rule set.

## Architecture consequence

A triggered listed criterion blocks the generic restart branch. If the cause is unresolved, the evaluator returns `INSUFFICIENT_CONTEXT`. `RESTART_ELIGIBLE` is returned only when the premature-stop cause is affirmatively known to be non-rule.

The evaluator does **not** issue an engine command and does not assume restart success.

Crew actions are recorded separately from physical DPS response; pressing Engine Start or selecting command override does not set `engine_running=True`.

No extra post-stop FLIGHT authorization is invented because the contingency had already been passed to and read back by the crew before PC+2.

## Test status

New tests are committed. A runtime execution could not be completed because the local container could not resolve `github.com`; tests are therefore not recorded as passing.

## Next work

Research and implement the first **ground-only shutdown callout → crew action** path. Fuel/oxidizer ΔP >25 psi is the best current candidate because the rule explicitly states that it is a ground callout only and the ground-derived product is already modeled.
