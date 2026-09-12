# Apollo 13 PC+2 Restart Contingency Sources

Status: active source supplement for the PC+2 premature-shutdown/restart branch.

## 1. Apollo 13 Mission Operations Report

- **Title:** *Mission Operations Report — Apollo 13*
- **Organization:** NASA Manned Spacecraft Center / Flight Control Division
- **Date:** 28 April 1970
- **Source class:** PRIMARY, mission-specific
- **Use:** Defines PC+2 shutdown criteria and states that an early shutdown not caused by those criteria was to be restarted by ullaging, depressing Engine Start, and turning on Descent Engine Command Override.
- **Implementation consequence:** Restart eligibility depends on shutdown cause; a listed-rule shutdown is not converted into a restart contingency.
- **Limitations:** Does not define an engine restart success model or detailed restart transient.

## 2. Apollo 13 Mission Commentary / air-ground transcript

- **Organization:** NASA
- **Mission time:** approximately 76:31–76:37 GET
- **Source class:** PRIMARY, contemporaneous mission transcript
- **Use:** Records CAPCOM's crew-facing instruction for an in-burn engine stop with flashing Noun 97: PRO, ullage, Engine Start push, Descent Engine Override on; also records crew readback of the shutdown rules and restart procedure.
- **Implementation consequence:** The contingency can be pre-briefed to the crew; no unsupported post-stop FLIGHT authorization step is required by the current model.
- **Limitation:** The transcript does not establish detailed LGC internal Noun-97 sequencing.

## 3. Apollo 13 Flight Journal — Day 4 Part 1

- **Source class:** TRANSCRIPT RECONSTRUCTION / SECONDARY COMMENTARY WITH PRIMARY TRANSCRIPT
- **Use:** Separates the earlier no-ignition backup procedure from the later in-burn premature-shutdown restart instruction and provides convenient chronology.
- **Implementation rule:** Governing historical claims remain tied to the NASA Mission Operations Report and NASA mission transcript.

## 4. Apollo Operations Handbook — Lunar Module LM10 and Subsequent, Volume I

- **Document:** LMA790-3-LM, 1 February 1970
- **Source class:** PRIMARY/CONTEMPORARY subsystem documentation
- **Use:** Establishes common LM DPS restartability and the manual engine-on path: START/engine-on command → pilot valves open → propellant shutoff valves open → propellant flow/combustion. Also documents the command-override alternate-voltage role.
- **Implementation consequence:** Supports a separate successful physical-response event after an eligible restart procedure.
- **Limitation:** Does not justify an Apollo 13 LM-7 restart transient, exact restart thrust level, pressure buildup, or success probability.

## Research record

- `resources/research/067_pc2_premature_shutdown_restart_branch.md`
- `resources/research/071_pc2_dps_restart_physical_response.md`

## Implementation follow-through

- `src/apollo_mission_control/restart_logic.py` — restart eligibility only.
- `src/apollo_mission_control/operational_actions.py` — crew actions only.
- `src/apollo_mission_control/dps_restart_response.py` — explicit successful physical response.
- `tests/test_pc2_restart.py`
- `tests/test_pc2_restart_response.py`

## Evidence rule

Do not equate:

- failure to ignite at TIG with premature shutdown after ignition;
- restart eligibility with successful restart;
- crew restart action with physical DPS response;
- physical restart with known thrust level or automatic telemetry confirmation;
- absence of a modeled triggered rule with proof that no historical fault existed.

Synthetic tests may exercise the branch, but their failure cause/timing must be labeled non-historical unless directly sourced.