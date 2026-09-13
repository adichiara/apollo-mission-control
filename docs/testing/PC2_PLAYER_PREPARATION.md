# PC+2 player preparation package

Date: 2026-09-13  
Status: **READY FOR LIVE-PLAY USE**

This package defines the minimum reproducible preparation players should receive before a physical PC+2 validation run. It is a project training aid constrained by Apollo flight-controller training evidence; it is not an Apollo-era handout reconstruction.

## Common briefing for all players

Players should know before the run:

- the scenario represents Apollo 13 PC+2 preparation/execution beginning near 77:55 GET and continuing through immediate post-burn verification/power-down;
- mission time normally continues while controllers think and coordinate;
- each original Apollo station has its own information and authority boundary;
- players should act only from information available to their assigned station(s), plus communications actually received during play;
- FLIGHT owns the modeled GO/NO-GO decision;
- CAPCOM is the modeled path for approved crew-facing transmissions;
- facilitator/admin controls are not player controls;
- players may consult their assigned rules/procedure material during the run;
- uncertainty is allowed: the goal is to make and communicate operational judgments, not to guess hidden simulator state.

Do not brief players on whether a nonnominal branch will occur.

## Station preparation

### FLIGHT

Know:

- FLIGHT integrates controller readiness and retains the modeled final GO/NO-GO authority;
- FLIGHT should not infer private station evidence that has not been reported or presented;
- approved crew-facing information must still pass through CAPCOM.

Player should be familiar with the FLIGHT presentation and readiness/decision controls before timed play.

### CAPCOM

Know:

- CAPCOM is the modeled crew voice path;
- an item entering the CAPCOM queue is not automatically transmitted;
- CAPCOM must deliberately transmit approved items;
- CAPCOM should not invent technical content or bypass FLIGHT/controller authority.

Player should be familiar with queued-message and transmit controls before timed play.

### CONTROL

Know:

- CONTROL monitors the modeled LM descent-stage propulsion/system evidence assigned to the station;
- the PC+2 rule set includes the source-backed fuel/oxidizer differential-pressure criterion used by the project;
- a controller conclusion, crew report, telemetry observation, and hidden physical state are distinct evidence types;
- CONTROL must explicitly initiate modeled callouts/actions when warranted.

Do not reveal whether the synthetic ΔP branch will occur.

### TELMU

Know:

- TELMU monitors the modeled LM electrical/environmental/system products assigned to the station;
- TELMU and CONTROL remain separate original station identities even in compact play;
- TELMU should report readiness and issues from its own presentation rather than infer CONTROL evidence.

### GUIDO

Know:

- GUIDO monitors the modeled guidance/navigation/attitude information assigned to the station;
- attitude-related criteria are evaluated from the station's presented evidence, not hidden truth;
- GUIDO and FIDO/RETRO remain separate original station identities even in compact play.

### FIDO/RETRO

Know:

- this project presents the PC+2 flight-dynamics functions needed by the first slice under the FIDO/RETRO player surface;
- the player should use only the displayed trajectory/burn information and modeled coordination path;
- compact FLIGHT DYNAMICS is a player grouping, not a historical combined Apollo station.

### INCO

Know:

- INCO is responsible for the modeled communications/data-path evidence assigned to the station;
- INCO is not CAPCOM and does not replace the crew voice function;
- communications/data-path reasoning remains active in the selected PC+2 window.

## Compact-mode additions

For the five-player compact configuration:

- LM SYSTEMS player owns TELMU + CONTROL;
- FLIGHT DYNAMICS player owns GUIDO + FIDO/RETRO;
- the player must deliberately switch between original substations;
- readiness, actions, and audit provenance remain attributed to the active original station;
- the compact labels are modern project groupings only.

Before timed play, compact-role players should practice one substation switch and confirm that the active original call sign is visible.

## Client-operation preparation

Before timed play each participant should demonstrate that they can:

- join the assigned station or approved station set;
- identify the current GET;
- recognize the active original station;
- reload/rejoin without changing ownership;
- locate readiness/action controls relevant to the assigned station;
- distinguish player controls from facilitator/admin controls.

These are modern simulator-use skills, not Apollo procedures.

## Facilitator briefing boundary

The facilitator may answer questions about:

- how to operate the browser client;
- which documented station responsibilities apply;
- where assigned rules/procedures are located.

During timed play, the facilitator should not disclose:

- hidden state;
- another station's private evidence;
- whether/when a nonnominal injection will occur;
- the intended diagnosis or decision;
- the next required action unless correcting a confirmed client-operation failure.

## Preparation record

Before each validation run, record for every player:

- assigned role/station set;
- whether this package was reviewed;
- whether station-specific rules/procedures were available;
- whether client-operation checks were completed;
- any known prior familiarity with the prototype.

This record allows later incidents to distinguish `PLAYER_INSTRUCTION` from presentation, simulation, or legitimate decisionmaking issues.

## Historical basis

See research note `096_live_play_player_preparation_boundary.md` and `resources/source-catalog/LIVE_HUMAN_PLAY_VALIDATION_SOURCES.md`.