# 097 — Live-play player reference-packet structure

Date: 2026-09-13  
Status: **RESEARCHED — first-run packet structure defined; physical usability still requires validation**

## Question

How should the PC+2 player reference material be organized so that prepared players can use source-backed rules and procedures during integrated play without turning the packet into a scenario solution sheet?

## Primary-source findings

### Flight Mission Rules were decision references, not a substitute for all procedure material

L. W. Keyser's *Apollo Experience Report: The Role of Flight Mission Rules in Mission Preparation and Conduct* (NASA TN D-7822 / JSC S-417) describes mission rules as preplanned guidance for real-time mission decisions, developed and reviewed through mission planning, testing, and training. The report also emphasizes responsibility/authority and training controllers and crews to respond to nonnominal situations, including situations for which no complete response had been preplanned.

Project consequence:

- source-backed decision criteria may be available to the relevant player before and during the run;
- a rule should identify the condition and responsible operational path without supplying hidden diagnosis or telling the player that the condition will occur;
- legitimate judgment remains part of play.

### Apollo procedure documentation separated systems knowledge from mission-phase execution

Paul C. Kramer's *Apollo Experience Report — Systems and Flight Procedures Development* (NASA TN D-7436 / JSC S-366) distinguishes systems procedures from flight procedures. Systems procedures covered system operating modes largely independent of the mission plan, while flight procedures integrated mission constraints and requirements into a time line for each mission phase. Final procedures were verified in simulations involving the flight crew, Mission Control Center, and Manned Space Flight Network.

Project consequence:

The player packet should not collapse everything into one ordered "do this next" checklist. It should keep separate:

1. station responsibility / available information;
2. applicable mission rules and criteria;
3. nominal PC+2 phase context and procedure sequence;
4. modern client-operation instructions.

That separation preserves the difference between reference knowledge and scenario-specific decisionmaking.

### Integrated simulation assumed prior controller preparation

Harold G. Miller's *Simulation Training for Flight Control Decisionmaking* (NASA SP-209) places integrated mission simulation after broader controller training and describes final simulation as exercising established procedures, interfaces, teamwork, adverse-condition response, and decisionmaking in the mission environment.

Project consequence:

The live playtest should measure whether prepared players can find, interpret, coordinate, and act on information under continuous mission time. It should not measure whether an unprepared player can infer an Apollo station from scratch.

## First-run packet design

For the first physical PC+2 validation, use a layered reference packet in this order:

### A. Common operational brief

All players receive:

- scenario phase and nominal objective;
- continuous-GET behavior;
- FLIGHT/CAPCOM/facilitator authority boundaries;
- rule that only assigned station information plus received communications may be used;
- statement that uncertainty is allowed and hidden simulator state must not be guessed.

### B. Original-station sheet

Each original station receives its own sheet, even when two stations belong to one compact player. The sheet contains only:

- station responsibility in this PC+2 implementation;
- station-visible product families;
- station-authorized player actions;
- coordination path to FLIGHT/CAPCOM or another station when explicitly modeled.

A compact player receives two separately titled original-station sheets rather than one synthetic historical station sheet.

### C. Rule / criterion sheet

Rules are grouped by responsible original station and written as neutral criteria, not as scenario cues.

Requirements:

- preserve ground-versus-onboard distinctions;
- preserve `NOT_EVALUABLE` where exact historical evidence remains unresolved;
- do not convert an unresolved criterion into a fabricated gauge or threshold;
- do not state whether a criterion will be exercised in the run;
- do not add a recommended diagnosis unless the reviewed historical procedure explicitly provides one.

For the current first playable, this means the source-backed CONTROL differential-pressure criterion may be present as a rule, but the packet must not say that a ΔP malfunction will be injected. The unresolved singular 150-psi ground inlet-pressure aggregation and exact onboard 77-percent thrust indication remain explicitly unresolved rather than being converted into playable shortcuts.

### D. Nominal phase/procedure sheet

Provide the normal PC+2 preparation/execution context needed to orient the player. This may identify expected phase transitions and responsibilities already represented by the simulator, but it must not contain facilitator-only injection timing or branch-specific expected actions.

### E. Modern client-operation sheet

Keep browser mechanics visibly separate from historical material:

- join/rejoin;
- active station identification;
- compact substation switching;
- readiness/action control location;
- reload/rejoin recovery.

These instructions are project infrastructure and should be labeled as such.

## Anti-hint rules

The packet must not contain:

- whether or when the synthetic ΔP branch will occur;
- hidden physical/instrument integrity state;
- another station's private data;
- facilitator controls;
- an incident diagnosis framed as the expected answer;
- a branch-specific sequence such as "when X appears, perform Y" unless X→Y is itself the source-backed rule/procedure being tested and would have been available to that station;
- invented historical detail introduced only to make the exercise easier.

## Physical-validation consequence

Question 23 in `docs/OPEN_QUESTIONS.md` can be treated as **resolved for the initial first-playable packet structure**, but not as a historically reconstructed Apollo handout format. Physical play must still test:

- whether players can find the relevant sheet quickly;
- whether original-station separation remains clear in compact mode;
- whether neutral rule wording is understandable without becoming a hint;
- whether modern client instructions remain visually distinct from historical reference material.

Any packet change prompted by player confusion must first be classified as instruction/usability versus historical-content deficiency. Historical content changes still require source review.

## Historical claim boundary

Supported:

- mission rules were premission decision references developed and exercised through training;
- Apollo procedures distinguished system-operation knowledge from mission-phase flight procedures;
- integrated simulations assumed broader controller preparation and exercised procedures/decisionmaking.

Project adaptation:

- the five-part packet layout;
- page order and visual grouping;
- one-sheet-per-original-station compact presentation;
- browser-operation section;
- packet length and typography.

Not supported:

- that Apollo 13 controllers used this exact packet or page order;
- that all PC+2 information historically appeared in one portable packet;
- that unresolved historical criteria may be simplified into fabricated displays for playability.

## Sources

1. L. W. Keyser, *Apollo Experience Report: The Role of Flight Mission Rules in Mission Preparation and Conduct*, NASA TN D-7822 / JSC S-417, November 1974. NTRS `19750002893`.
   - https://ntrs.nasa.gov/citations/19750002893
2. Paul C. Kramer, *Apollo Experience Report — Systems and Flight Procedures Development*, NASA TN D-7436 / JSC S-366, September 1973. NTRS `19730023040`.
   - https://ntrs.nasa.gov/citations/19730023040
3. Harold G. Miller, *Simulation Training for Flight Control Decisionmaking*, NASA SP-209, 1970. NTRS `19700013438`.
   - https://ntrs.nasa.gov/citations/19700013438

See also `resources/research/096_live_play_player_preparation_boundary.md`, `docs/testing/PC2_PLAYER_PREPARATION.md`, and `resources/source-catalog/LIVE_HUMAN_PLAY_VALIDATION_SOURCES.md`.