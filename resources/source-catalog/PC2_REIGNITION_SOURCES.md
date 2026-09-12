# Apollo 13 PC+2 Re-ignition Sources

Status: active source supplement for the premature-shutdown restart / physical re-ignition boundary.

## 1. Apollo 13 Mission Operations Report

- **Title:** *Mission Operations Report — Apollo 13*
- **Organization:** NASA Manned Spacecraft Center / Flight Control Division
- **Date:** 28 April 1970
- **Source class:** PRIMARY, mission-specific
- **Use:** Establishes that an early PC+2 shutdown not caused by the listed shutdown criteria was to be followed by a descent-engine restart attempt using ullage, ENGINE START, and Descent Engine Command Override.
- **Limitation:** Does not provide exact restart delay, pressure-rise trace, or post-restart throttle profile.

## 2. Apollo 13 mission commentary / air-to-ground transcript

- **Source class:** PRIMARY, contemporaneous mission communications
- **Relevant interval:** approximately 76:31–76:37 GET
- **Use:** CAPCOM transmits and Haise reads back the restart sequence: flashing Noun 97 → PRO → manual ullage → ENGINE START → Descent Engine Command Override.
- **Limitation:** Procedure evidence, not proof of physical restart timing or success.

## 3. Report of Apollo 13 Review Board — Appendix B

- **Source class:** PRIMARY, postflight investigation
- **Use:** Independently records the final rule that an early shutdown not due to the specified criteria should be followed by a relight attempt using ENGINE START and Descent Engine Command Override.
- **Limitation:** Does not specify detailed physical response timing.

## 4. Apollo Operations Handbook — Lunar Module, LMA790-3-LM

- **Organization:** Grumman / NASA
- **Basic date:** 1 February 1970
- **Source class:** PRIMARY / contemporary subsystem documentation
- **Use:** Establishes descent-engine manual on/off command architecture: START/STOP commands route through DECA to the descent-engine pilot valves, which operate the fuel/oxidizer shutoff-valve system. Supports a distinct physical engine-on response after crew command.
- **Limitation:** The currently accessible searchable continuity copy is LM10-and-subsequent material; exact LM-7 line-by-line certification was not required for this bounded architecture step.

## Research record

- `resources/research/067_pc2_premature_shutdown_restart_branch.md`
- `resources/research/071_pc2_restart_command_and_physical_reignition.md`

## Implementation rule

Do not equate restart procedure completion with restart success.

A successful physical re-ignition must be represented as a distinct vehicle-response event. Do not fabricate:

- ignition delay;
- chamber-pressure buildup;
- throttle ramp;
- controller confirmation threshold.
