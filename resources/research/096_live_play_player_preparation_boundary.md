# 096 — Live-play player preparation boundary

Date: 2026-09-13  
Status: **RESEARCHED — pre-run player preparation boundary defined; physical execution still pending**

## Question

What should a player be expected to know before the first physical PC+2 playtest so that the run tests Mission Control decisionmaking and simulator usability rather than merely testing whether an unbriefed participant can infer Apollo controller work from the interface?

## Primary-source findings

### Apollo flight-controller simulation was the culmination of broader training

Harold G. Miller's *Simulation Training for Flight Control Decisionmaking* (NASA SP-209, 1970) states that flight-controller training began when the controller started work and included formal, intrinsic, and simulation training. The final simulation exercises were intended to verify that controllers could handle specified contingencies, use established procedures, and make decisions in the mission environment.

For this project, that means the physical playtest should not assume a historically authentic controller entered an integrated simulation with no prior knowledge of station responsibility, spacecraft/system context, mission rules, procedures, or console information.

It does **not** support requiring project players to complete an Apollo-era certification syllabus, nor does it establish a specific number of briefing minutes or pages.

### Mission rules were prepared before flight and exercised in training

L. W. Keyser's Apollo experience report on flight mission rules explains that premission mission-rule preparation defined responsibility and authority and that rules were developed through planning, testing, and training. The report also emphasizes training controllers and crews in determining responses to nonnominal situations, including cases without a fully preplanned response.

For PC+2, this supports giving players the source-backed rules, responsibility boundaries, and normal procedural context relevant to their stations before the run. It does not support revealing the upcoming synthetic ΔP event or its expected solution.

### Flight procedures integrated rules and mission requirements

Paul C. Kramer's *Apollo Experience Report — Systems and Flight Procedures Development* describes flight procedures as integrating mission rules and requirements with spacecraft procedures, with final procedures organized by mission phase and incorporated into mission planning/data packages.

For the project, this supports preparing players with the procedures/products they are expected to use during the selected phase instead of forcing discovery by trial and error during the timed run.

## Project decision

Before a run used for first-playable validation, every player must receive a short station-specific preparation package containing only information they could reasonably be expected to know before an integrated simulation:

1. station identity and responsibility boundary;
2. what information/products the station can see in this implementation;
3. station actions the player is authorized to take;
4. relevant PC+2 mission phase context and nominal objective;
5. the source-backed rules/procedures the station may need during the run;
6. communication/coordination expectations, including FLIGHT and CAPCOM authority boundaries where applicable;
7. modern project controls needed only to operate the client, such as join/rejoin and compact substation switching.

The package must **not** reveal:

- whether the facilitator will inject the synthetic ΔP branch;
- the timing of any nonnominal injection;
- the intended diagnosis or recommended decision for an injected malfunction;
- hidden state unavailable to the station;
- facilitator-only actions;
- another station's private information.

Players should be allowed to consult their assigned rules/procedures during the run. The validation target is operational use of available information under continuous mission time, not memorization.

## Validation consequence

The live-play report must distinguish:

- a player who was not given required preparation (`PLAYER_INSTRUCTION`);
- a player who was given the preparation but cannot find or understand information that should be usable (`STATION_PRESENTATION` or another appropriate defect class);
- legitimate controller uncertainty (`NORMAL_DECISION_UNCERTAINTY`).

A first-playable PASS should therefore require that the run use the documented preparation package rather than an ad hoc oral briefing that cannot be reproduced.

## Historical claim boundary

Supported:

- Apollo flight-controller simulation training followed broader formal/on-the-job preparation;
- integrated simulation exercised established procedures, mission rules, system knowledge, and decisionmaking;
- mission rules and procedures were developed before flight and used in training/operations.

Project adaptation:

- the exact contents and format of the PC+2 player-preparation package;
- browser-operation instructions;
- compact-role switching instructions;
- any chosen briefing length.

Not supported:

- that Apollo used this project's player handout format;
- that Apollo controllers were trained from phone-sized interfaces;
- exposing scenario-specific nonnominal events before the run.

## Sources

1. Harold G. Miller, *Simulation Training for Flight Control Decisionmaking*, NASA SP-209, 1970. NTRS `19700013438`.
   - https://ntrs.nasa.gov/citations/19700013438
2. L. W. Keyser, *Apollo experience report: The role of flight mission rules in mission preparation and conduct*, NASA-TN-D-7822 / JSC-S-417, 1974. NTRS `19750002893`.
   - https://ntrs.nasa.gov/citations/19750002893
3. Paul C. Kramer, *Apollo Experience Report — Systems and Flight Procedures Development*, NASA-TN-D-7436, 1973. NTRS `19730023040`.
   - https://ntrs.nasa.gov/citations/19730023040

See `resources/source-catalog/LIVE_HUMAN_PLAY_VALIDATION_SOURCES.md` and `docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md`.