# Research Note 027 — Apollo 13 Known AGC Program / Operational Notes

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Primary source

NASA Manned Spacecraft Center memorandum:

**COLOSSUS 2D and LUMINARY 1C Program and Operational Notes, First Edition for Mission H2**  
COMANCHE 72 Rev. 3 / LM131 Rev. 1  
Flight Support Division  
Reference: **70-FSS5-34**

Public scan:
https://www.ibiblio.org/apollo/Documents/apollo_13_program_notes.pdf

## Why this source matters

This document is a mission-specific list of **known software/operational behaviors** supplied to crew, flight controllers, planning personnel, and engineering/support organizations before Apollo 13.

It is therefore ideal evidence for a new mission-profile category:

> known quirks / known limitations / established workarounds

These are not hidden simulator failures.

Players who are expected to know the relevant role/procedure should be able to have these behaviors in their station documentation or training material.

## Document organization

The memorandum classifies notes by:

### Audience / situation

1. Crew notes and checklist items
2. Ground notes
3. Restarts and priorities

### Technical area

1. Nouns, verbs and displays
2. Selection of programs / extended verbs
3. Ground updates and pad loads
4. Navigation / W-matrix
5. Rendezvous and targeting
6. Optics, IMU and radars
7. Guidance/control, boost and entry

This is a useful historical taxonomy for guidance-software knowledge.

## Example: restart effects can suppress later failure indications

For certain CSM IMU/optics mode transitions, a restart could leave failure-inhibit bits set longer than intended.

The document gives exact vulnerable timing intervals such as roughly:

- ~5 s during coarse-to-fine alignment;
- ~10–15 s for several IMU/CDU/PIPA transition cases.

### Simulator implication

A restart can modify future diagnostic behavior.

It is not enough to simulate:

```text
restart = temporary computer interruption
```

The state model may need to preserve post-restart inhibit bits and their effect on subsequent alarms.

## Example: high computer activity / program alarms

The notes warn that during high computer activity, selecting certain extended verbs could produce **1201/1202-type program alarms** and lose the extended-verb activity.

This is important evidence that program alarms are contextual consequences of computer scheduling/load, not arbitrary warning events.

## Example: LM restart underburn effect

The LUMINARY notes document a known case in which, after a restart, a velocity term could be subtracted twice from VG.

The consequence could be:

- an underburn;
- residuals after engine shutdown that did not show the full error.

The recovery was a manually determined ground correction.

### Simulator implication

This couples:

- computer restart;
- internal guidance state;
- maneuver result;
- misleading residual indication;
- ground-computed corrective action.

That is exactly the kind of multi-role anomaly a high-fidelity scenario can reproduce if the specific case is chosen.

## Example: CSM-docked LM control limitations

The mission notes document several docked-vehicle constraints, including:

- careful ACA use to avoid exciting structural bending;
- maneuver-rate restrictions;
- RCS plume-deflector-related control effects;
- selection/configuration limitations.

These are relevant to CONTROL/GUIDO/GNC coordination during Apollo 13.

## Example: radar and restart behavior

The LUMINARY notes describe:

- radar data-good / reasonability constraints;
- specific radar-mode limitations;
- P20 tracking behavior after hardware restart;
- priority-display behavior;
- automatic-attitude-maneuver termination after restart.

Again, the impact of a failure depends on current program/mode.

## Known issue versus injected failure

The simulator must distinguish:

### Known mission-profile behavior

Something documented preflight and expected to be understood.

Examples:

- known software limitation;
- known display quirk;
- known workaround;
- known spacecraft anomaly at launch.

### Injected unknown malfunction

A condition introduced by the scenario/SimSup that controllers must detect and diagnose.

The two should not be conflated.

If the project recreates Apollo 13 before the tank accident, the crew/controllers already know about the published H2 program notes; the player should not have to “discover” those known characteristics as surprise failures.

## Research targets

1. Tag each Apollo 13 program note by responsible controller(s).
2. Identify which notes are relevant to:
   - GUIDO
   - GNC
   - CONTROL
   - FIDO/RETRO
   - crew/CAPCOM
3. Cross-reference FSRR discrepancy status to determine which notes represent:
   - flown software behavior;
   - workaround;
   - resolved issue;
   - simulator-only issue.
4. Add applicable known issues to mission-profile data only when the software/system behavior is modeled.

## Source

https://www.ibiblio.org/apollo/Documents/apollo_13_program_notes.pdf
