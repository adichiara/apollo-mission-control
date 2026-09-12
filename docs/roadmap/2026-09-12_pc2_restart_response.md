# Roadmap addendum — PC+2 DPS restart physical response

Date: 2026-09-12  
Status: **CURRENT — supersedes the Phase 4 “Immediate next work” restart-response item in `docs/ROADMAP.md` until the next roadmap consolidation**

## Completed boundary

The premature-shutdown restart path now separates:

1. shutdown-cause classification / restart eligibility;
2. crew-facing restart procedure;
3. crew operational actions;
4. successful physical DPS engine-on response;
5. later controller-observable evidence.

The successful response is source-bounded to engine-on command, pilot-valve opening, propellant-shutoff-valve opening, and engine thrusting. It does not synthesize an LM-7 restart delay, restart thrust setting, GQ6510P buildup, or guaranteed success.

Follow-up research also found no source-backed reason to create a special `restart confirmed` product. A fresh post-restart `GQ6510P` sample should reuse the common CONTROL chamber-pressure path; no restart-specific pressure threshold, crew success report, or dedicated discrete is invented.

Implementation/research:

- `src/apollo_mission_control/dps_restart_response.py`
- `tests/test_pc2_restart_response.py`
- `resources/research/071_pc2_dps_restart_physical_response.md`
- `resources/research/072_pc2_restart_controller_evidence.md`
- `resources/source-catalog/PC2_DPS_RESTART_RESPONSE_SOURCES.md`

## Immediate next work

Move away from DPS transient detail and begin the **first-pass player-facing CONTROL information presentation** for the PC+2 slice using already-researched products.

Use exact Apollo display structure where directly sourced. Where exact CRT routing/layout remains unresolved, preserve the product provenance and label any project rendering explicitly rather than implying a historical screen reconstruction.

## Deferred

- detailed restart transient dynamics;
- exact restart thrust command;
- exact LM-7 chamber-pressure rise;
- restart success probability;
- low-value CRT archaeology that does not affect a player decision.