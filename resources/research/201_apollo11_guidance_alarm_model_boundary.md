# 201 — Apollo 11 guidance-computer alarm/restart model boundary

## Purpose

Define the minimum reusable guidance-computer behavior needed for the Apollo 11 powered-descent program-alarm reference without encoding an automatic abort/continue outcome.

## Primary evidence

Grumman memo LAV-500-940, *Program Alarms in Powered Descent — Apollo 11* (31 July 1969), states that:

- 1202 occurs when a new job is requested after all eight Executive core sets are in use;
- 1201 occurs when a job requiring a VAC area is requested after all five VAC areas are assigned;
- both conditions transfer through the alarm/abort path, illuminate the program alarm indication, store the code, and lead to a software restart;
- restart processing clears the Executive job list and uses restart protection to resume the interrupted mission program;
- P63 and P64 continued across the Apollo 11 Executive overflows because they were restart-protected.

The Apollo 11 Mission Report separately records the actual alarm chronology during powered descent.

The surviving postflight analysis also makes clear that continued guidance performance and independent information were operationally relevant to the GO/abort judgment. Therefore the simulator must keep alarm state separate from guidance validity, backup-guidance agreement, trajectory state, and controller decision.

## Implemented reusable boundary

The generic guidance-computer model now represents:

1. active program identity;
2. program-alarm indication and code;
3. caller-defined alarm meaning;
4. caller-defined software-restart classification;
5. restart count/history;
6. caller-defined restart-protected programs;
7. whether a restart-protected program resumed or whether recovery is unspecified.

The model explicitly does **not** generate an abort/continue recommendation.

## Why this is reusable

The code contains no Apollo 11 alarm constants. Alarm rules and restart-protected programs are supplied by the caller/profile. That permits later Apollo/Luminary or other computer-state scenarios to reuse the same state mechanism without making 1201/1202 universal simulator assumptions.

## Apollo 11 historical profile boundary

For the second reference case, the model profile records the guidance-computer domain as **partial** rather than validated.

Source-backed:

- 1201/1202 Executive-overflow meanings;
- software restart behavior;
- P63/P64 restart protection;
- actual powered-descent alarm chronology.

Still unresolved or deliberately separate:

- exact instantaneous CPU workload/resource occupancy;
- complete alarm display/downlink/controller presentation path;
- exact real-time PGNS/AGS values at every alarm;
- complete post-simulation alarm decision rules;
- landing-radar measurement/update equations;
- LM-5 powered-descent propulsion calibration;
- historical descent trajectory initial state and acceptance tolerance.

## Scenario consequence

A new Apollo 11 powered-descent reference fixture is added to the scenario catalog with runtime adapter `apollo11_descent_v1`, which is intentionally unsupported.

This makes the second historical reference visible to readiness tooling while keeping `executable = false` until the required causal domains exist.

## Sources

- NASA, *Apollo 11 Mission Report*, November 1969.
- Grumman Aircraft Engineering Corp., LAV-500-940, *Program Alarms in Powered Descent — Apollo 11*, 31 July 1969.
- MIT Instrumentation Laboratory, *Exegesis of the 1201 and 1202 Alarms Which Occurred During the Mission G Lunar Landing*.
- NASA Oral History Project, Richard H. Koos interview, 24 August 2023.
