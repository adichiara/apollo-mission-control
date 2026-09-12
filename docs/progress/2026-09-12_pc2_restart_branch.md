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

## Architecture consequence

Restart eligibility is derived from the observed premature stop plus the existing shutdown-rule audit. It does **not** issue an engine command and does not assume restart success.

Crew actions are recorded separately from physical DPS response; pressing Engine Start or selecting command override does not set `engine_running=True`.

No extra post-stop FLIGHT authorization is invented because the contingency had already been passed to and read back by the crew before PC+2.

## Test status

New tests are committed. No successful execution is recorded in this pass yet.

## Next work

Research and implement the first **ground-only shutdown callout → crew action** path. Fuel/oxidizer ΔP >25 psi is the best current candidate because the rule explicitly states that it is a ground callout only and the ground-derived product is already modeled.
