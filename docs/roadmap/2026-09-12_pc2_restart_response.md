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

Implementation:

- `src/apollo_mission_control/dps_restart_response.py`
- `tests/test_pc2_restart_response.py`
- `resources/research/071_pc2_dps_restart_physical_response.md`
- `resources/source-catalog/PC2_DPS_RESTART_RESPONSE_SOURCES.md`

## Immediate next work

Research the minimum source-backed **controller-observable evidence of a successful restart**. Prefer reuse of existing chamber-pressure/ground product paths if historically justified, but do not invent a restart-specific pressure threshold or crew report.

If no mission-specific confirmation rule can be recovered economically, preserve fresh GQ6510P as a generic propulsion observation and move to the next player-relevant PC+2 dependency.

## Deferred

- detailed restart transient dynamics;
- exact restart thrust command;
- exact LM-7 chamber-pressure rise;
- restart success probability;
- low-value CRT archaeology that does not affect a player decision.