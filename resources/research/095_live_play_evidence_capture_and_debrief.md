# 095 — Live-play evidence capture and debrief boundary

Date: 2026-09-13  
Status: **RESEARCHED — structured evidence/debrief package defined; physical execution still pending**

## Question

Before the remaining real-device/human PC+2 validation is run, what evidence should be captured so that the project can distinguish a historical deficiency from a simulation defect, a presentation problem, a network/client problem, player-training confusion, or legitimate controller uncertainty?

## Primary-source findings

### Apollo integrated simulations were intended to exercise the combined operational system

Martikan and Nassiff's Apollo mission-simulator work describes integrated operation of the Apollo mission simulator with the Mission Control Center for combined flight- and ground-crew training. Harold G. Miller's *Simulation Training for Flight Control Decisionmaking* describes simulation in the mission environment as readiness training for flight controllers, emphasizing controller decisionmaking, interfaces, procedures, and response to adverse conditions.

For this project, those sources support evaluating the live run as an integrated operational exercise rather than as a collection of isolated page checks.

They do **not** provide a historical Apollo browser-usability questionnaire, phone-readability score, HTTP latency threshold, or modern defect taxonomy.

### Apollo mission rules were training and decision tools, not merely static documentation

Keyser's Apollo experience report on flight mission rules describes mission-rule development through testing/training and their use in real-time decisionmaking, including training controllers and crews to determine responses to nonnominal situations for which no action had been preplanned.

For PC+2 validation, this supports observing whether players can use the information and modeled rules available to their stations to make and communicate decisions. It does not justify treating every hesitation or disagreement as a defect.

## Supporting NASA operational-training evidence

Later NASA practice makes the debrief boundary explicit. NASA's Artemis launch-team simulation description states that real problems discovered during simulations are documented and data are collected for later resolution; after a simulation, controllers conduct a team debrief covering problems, what worked, what needs improvement, and possible procedure/requirement changes.

This later practice is used only as a validation-process analogue. It is **not** claimed to describe the exact Apollo 13 debrief format.

## Project decision

The physical PC+2 run must leave an inspectable evidence trail. For each material incident, capture:

1. mission GET and wall-clock timestamp;
2. scenario/run identifier and server commit;
3. player role plus original station currently active;
4. device/browser;
5. player intent — what they were trying to determine or do;
6. evidence actually visible to that station at the time;
7. action/communication taken, if any;
8. expected result;
9. observed result;
10. whether another player or facilitator had to explain hidden/project information;
11. audit/event identifiers or relevant log excerpt where available;
12. one provisional defect class;
13. whether the incident requires historical research before any behavior change.

The debrief must then separate:

- facts observed during the run;
- participant interpretation;
- reproducible software defects;
- historical questions requiring source review;
- changes proposed for usability only;
- legitimate uncertainty that should remain part of play.

No historical behavior should be changed solely because a player found a decision difficult. A historical/procedural change requires separate source support.

## Implementation consequence

The live-play protocol now uses a dedicated report template rather than free-form post-run notes. The template carries the existing defect classes, adds run/build provenance and incident-level evidence fields, and includes a debrief section that forces proposed historical changes into a separate research queue.

This improves validation traceability without adding any Apollo-era behavior to the simulator.

## Historical claim boundary

Supported:

- Apollo integrated simulation joined spacecraft simulation and Mission Control for combined crew/controller training;
- flight-controller simulation emphasized mission-environment decisionmaking, interfaces, procedures, and adverse-condition response;
- Apollo mission rules were developed and exercised through testing/training and supported real-time nonnominal decisionmaking.

Supporting later NASA practice:

- simulation issues can be documented during the run and reviewed in a structured team debrief;
- procedure/requirement changes can be outcomes of that debrief.

Not supported:

- that Apollo 13 used this project's incident fields or defect taxonomy;
- that Apollo used phones, browsers, HTTP, local/session storage, or facilitator tokens;
- any numeric latency/usability threshold not directly sourced elsewhere.

## Sources

1. F. O. Martikan and S. H. Nassiff, *Integrated operating mode of the Apollo mission simulator*, AIAA Paper 65-266, 1965. NTRS `19650039405` / `19660033487`.
   - https://ntrs.nasa.gov/citations/19650039405
   - https://ntrs.nasa.gov/citations/19660033487
2. Harold G. Miller, *Simulation Training for Flight Control Decisionmaking*, NASA SP-209, 1970. NTRS `19700013438`.
   - https://ntrs.nasa.gov/citations/19700013438
3. L. W. Keyser, *Apollo experience report: The role of flight mission rules in mission preparation and conduct*, NASA-TN-D-7822, 1974. NTRS `19750002893`.
   - https://ntrs.nasa.gov/citations/19750002893
4. NASA, *Simulations are 'Great Days' for NASA's Artemis I Launch Team*, updated 2023.
   - https://www.nasa.gov/humans-in-space/simulations-are-great-days-for-nasas-artemis-i-launch-team/

See `resources/source-catalog/LIVE_HUMAN_PLAY_VALIDATION_SOURCES.md` and `docs/testing/PC2_LIVE_PLAYTEST_REPORT_TEMPLATE.md`.