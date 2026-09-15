# 162 — Second reference case assessment: Apollo 11 powered-descent program alarms

## Purpose

Identify a second reference case that stresses materially different simulator mechanisms from Apollo 13 PC+2 without redefining the simulator around either case.

PC+2 remains the first implemented vertical slice. This assessment selects an Apollo 11 powered-descent/program-alarm interval as the next **architecture pressure test**, not yet as a second playable runtime.

## Why Apollo 11 descent is complementary

PC+2 primarily exercises:

- maneuver preparation and load flow;
- staged propulsion commands;
- guidance/attitude monitoring;
- controller GO/NO-GO and shutdown rules;
- communications/uplink;
- post-burn assessment.

Apollo 11 powered descent adds dependencies that PC+2 does not force:

- a continuously evolving lunar-descent trajectory rather than a mostly impulse-oriented maneuver;
- landing radar acquisition/quality and radar-to-guidance update decisions;
- PGNS versus AGS cross-checks during powered flight;
- LGC program state and restart/program-alarm behavior;
- controller interpretation of computer alarms while other guidance cues remain valid;
- changing guidance phases (P63/P64 and later P66);
- crew manual-control transitions and landing-point decisions if scope is extended;
- tight coupling among guidance, trajectory, propulsion, radar, crew reports, and Mission Control decisions.

That makes it a useful test of what belongs in common causal state versus scenario/runtime-specific logic.

## Exact actual-flight anchor

The Apollo 11 Mission Report provides a high-resolution lunar-descent event table. Relevant events include:

- 102:37:51 — landing radar data good;
- 102:38:22 — first 1202 alarm, computer-determined;
- 102:38:45 — radar updates enabled;
- 102:38:50 — landing-radar velocity update begins under the stated velocity condition;
- 102:39:02 — 1202 alarm;
- 102:41:32 — P64;
- 102:41:53 — attitude-hold handling-qualities check;
- 102:42:03 — automatic guidance;
- 102:42:18 — 1201 alarm, computer-determined;
- 102:42:43 and 102:42:58 — additional 1202 alarms;
- 102:43:09 — landing-point redesignation;
- 102:43:13 — attitude hold;
- 102:43:20 — AGS attitude update;
- 102:43:22 — P66;
- 102:45:40 — landing / engine off.

The technical and onboard voice records separately preserve controller/crew reports and should remain communication observations rather than aliases of physical/computer state.

Primary sources:

- NASA, *Apollo 11 Mission Report*, November 1969: https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A11_MissionReport.pdf
- NASA, *Apollo 11 Technical Air-to-Ground Voice Transcription*: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transcript_tec.pdf
- NASA, *Apollo 11 Onboard Voice Transcription*: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transscript_cm.pdf

## Documented preflight simulation

Richard Koos's NASA oral history gives direct SimSup evidence for the final Apollo 11 landing simulation.

Koos recalls that a guidance-computer program alarm was deliberately inserted during the last landing simulation and Steve Bales called for an abort. Koos could not recall whether the alarm was 1201 or 1202.

In the debrief, Koos's criticism was that the team had two independent cues they had not used: the Abort Guidance System and primary guidance parameters agreed and were normal, while the program alarm itself was the only abort cue.

Koos states that program-alarm handling was not yet in the flight rules. Kranz directed Bales, Jack Garman, and MIT/Draper support to review the alarms and determine which required abort.

Source:

- NASA Oral History Project, Richard H. Koos interview, 24 August 2023, pp. 10–13: https://www.nasa.gov/wp-content/uploads/2025/08/koosrh-8-24-23.pdf

## Simulation-case evidence boundary

### Strongly documented

- a program alarm was deliberately inserted in the final Apollo 11 landing simulation;
- Bales called for abort;
- PGNS/AGS information provided normal corroborating cues;
- the program alarm alone was insufficient basis for that abort;
- the debrief caused explicit program-alarm rule work before flight;
- an alarm of the same family later appeared in the actual landing.

### Not sufficiently documented for exact replay

- whether the injected alarm was specifically 1201 or 1202;
- exact simulated GET / descent phase at injection;
- exact simulator input mechanism;
- complete set of simultaneous failures or background conditions;
- exact crew inputs and all controller-visible display values;
- exact debrief wording beyond surviving recollections.

Therefore the project should not create an "exact July 1969 SimSup case" by choosing these details.

## Recommended second reference boundary

Use the **actual Apollo 11 powered-descent program-alarm interval** as the second engineering reference, because its timing and observations are primary-source bounded.

Initial implementation/research window:

- begin shortly before landing-radar/guidance alarm interaction, approximately 102:37:30 GET;
- include the first 1202 sequence, radar-update decision path, PGNS/AGS cross-check, P64 transition, 1201/1202 sequence, and associated GO/abort decision logic;
- initial endpoint near the P66 transition at approximately 102:43:22 GET.

Touchdown/manual landing may be added later if the trajectory/control model is ready; it is not necessary to prove the program-alarm decision chain.

## Architecture implications

A second runtime should pressure-test the following reusable interfaces:

1. **Mission profile**
   - Apollo 11 Mission G profile;
   - TELCOM terminology rather than Apollo 13 TELMU.

2. **Guidance-computer state**
   - active program;
   - restart/alarm event;
   - retained/restarted critical functions;
   - controller-visible alarm/report path.

3. **Independent guidance observations**
   - PGNS-derived guidance state;
   - AGS-derived backup/cross-check state;
   - no hidden-truth shortcut.

4. **Radar/measurement path**
   - landing-radar availability/quality;
   - measurement acceptance/update state;
   - effect on guidance observations.

5. **Trajectory**
   - continuously evolving powered-descent state;
   - sufficient altitude/velocity/phase state to support sourced controller decisions.

6. **Decision rules**
   - alarm identity plus independent guidance/vehicle cues;
   - abort/continue should emerge from the evidence available to controllers, not a pre-authored outcome.

7. **Crew**
   - deterministic crew reports/actions separated from physical/computer truth, as already required by D-020.

## Development consequence

Do not fork the project into a separate Apollo 11 simulator.

The second reference should reuse:

- central session clock/authority;
- scenario catalog;
- mission profile catalog;
- observation/integrity model;
- CAPCOM/crew separation;
- audit/event model;
- generic numerical components where applicable.

It should add only the causal domains that powered descent requires.

## Next work

1. Define a runtime-adapter interface narrow enough to support both PC+2 and this descent slice.
2. Research the minimum Apollo 11 guidance/radar/controller product set for the 102:37:30–102:43:22 interval.
3. Identify the exact post-simulation program-alarm decision rule source if available.
4. Build the second runtime only after those inputs are source-bounded.
5. Keep the documented preflight SimSup case cataloged separately until its unresolved injection details can be recovered.
