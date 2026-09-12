# Progress — PC+2 ΔP ground-callout shutdown loop

Date: 2026-09-12

## Completed

- Researched the documented fuel/oxidizer ΔP >25 psi PC+2 shutdown criterion.
- Confirmed from mission-specific primary sources that this criterion required a **ground callout** to the crew.
- Confirmed from the contemporaneous rules read-up/readback that the crew was to shut down when the criterion occurred.
- Added `resources/research/068_pc2_delta_p_ground_callout_shutdown_loop.md`.
- Added `resources/source-catalog/PC2_DELTA_P_CALLOUT_SOURCES.md`.
- Extended `controller_decisions.py` with an explicit ground shutdown-callout decision event.
- Extended `procedural_exchange.py` with a CAPCOM→CREW ΔP shutdown callout event.
- Extended operational actions/state with a crew DPS shutdown command that does not force physical engine response.
- Added `tests/test_pc2_delta_p_callout.py`.

## Architecture consequence

The implemented path is now:

`ground-derived ΔP product → CONTROL threshold assessment → controller callout decision → CAPCOM ground callout → crew shutdown command`

Each layer is distinct. The crew command does not directly set `engine_running=False`.

No exact CONTROL→FLIGHT→CAPCOM approval sequence is encoded because the reviewed sources establish only that it is a ground call to the crew, not the exact hypothetical internal voice-loop handling if the threshold were exceeded.

No exact cockpit shutdown switch/button sequence is asserted.

## Boundary behavior

- exactly 25 psi: clear;
- synthetic 26 psi: triggered;
- 26 psi is a software boundary-test value, not a historical Apollo 13 measurement.

A ΔP-triggered shutdown is a listed-rule shutdown and therefore does not enter the generic premature-shutdown restart branch.

## Test status

New tests are committed. A successful execution is not yet recorded in this progress entry.

## Next work

Research the separation between crew DPS shutdown command and physical engine shutdown/confirmation. Proceed only if primary LM/DPS sources establish a useful response/indication chain without requiring deep low-value hardware archaeology; otherwise move to the next PC+2 controller decision path.
