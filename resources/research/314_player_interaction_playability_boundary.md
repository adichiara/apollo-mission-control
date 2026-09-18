# Research note 314 — Player interaction and playability boundary

Date: 2026-09-18  
Status: **RESEARCHED DESIGN BOUNDARY — Apollo evidence separated from modern human-factors/playability guidance**

## Question

How should player interaction and interface development proceed so that the simulation remains recognizably Mission Control while becoming learnable, usable on phones, and viable as an in-person cooperative experience?

## Historical evidence

### Apollo flight-controller simulation trained an operational job, not interface discovery

Harold G. Miller's 1970 NASA paper *Simulation Training for Flight Control Decisionmaking* describes the flight controller as planner, implementer, systems/trajectory expert, operator, and decisionmaker. Training culminated in mission-environment simulations intended to verify contingency handling and established procedures, and to build confidence in the system used during the mission.

Source:

- NASA SP-209 / NTRS `19700013438`
- https://ntrs.nasa.gov/citations/19700013438

Project consequence:

- integrated play should exercise interpretation, judgment, communication, and coordination;
- players should arrive knowing their station responsibility, rules/procedures, and basic client operation;
- the timed run should not be used to discover arbitrary project UI conventions.

This reinforces research note 096.

### Apollo decisionmaking depended on interfaces among controllers

Miller explicitly frames flight-controller work in terms of organization and the people with whom controllers interface in the decisionmaking process. The project already has primary Apollo evidence for distinct FLIGHT, CAPCOM, Systems Operations, and Flight Dynamics responsibilities and for station-specific products.

Project consequence:

- the cooperative mechanic is not merely simultaneous monitoring;
- it is the need to package station evidence into a recommendation or callout that another controller can use;
- UI that automatically consolidates all evidence for FLIGHT or resolves cross-station disagreements would remove the job being simulated.

### Mission rules/procedures are working tools

Keyser's Apollo flight-mission-rules report documents rules as real-time decision tools developed and exercised through training, including nonnominal situations without fully preplanned responses.

Source:

- NASA-TN-D-7822 / NTRS `19750002893`
- https://ntrs.nasa.gov/citations/19750002893

Project consequence:

- printed or quickly accessible station references are part of play;
- the interface should make it practical to correlate a product with a rule, but should not evaluate the rule for the player unless the historical system itself did so.

## Modern NASA human-factors evidence used only as design guidance

The following sources do **not** establish Apollo behavior. They are used to identify modern usability risks worth testing.

### Workload and teamwork

NASA Space Flight Resource Management work notes that high workload can degrade performance and that effective teams adapt communication, decisionmaking, and task distribution under stress.

Source:

- NTRS `20090041872`
- https://ntrs.nasa.gov/citations/20090041872

Design implication:

- compact-role play is not just a smaller-player convenience; it changes workload;
- substation switching and information search should be measured explicitly;
- difficulty caused by more responsibilities may be legitimate, but difficulty caused by ambiguous active-station state is not.

### Display format affects controller performance

A 2026 NASA operational evaluation of controller-facing EVA telemetry display concepts found measurable differences in response time, workload, and usability among instrument-panel, schematic, and tabular presentations.

Source:

- NTRS `20260005145`
- https://ntrs.nasa.gov/citations/20260005145

Design implication:

- there is no reason to assume the most visually authentic dense rendering is automatically the most usable phone rendering;
- the project should test presentation form while preserving the same sourced information and decision boundary;
- authentic content and authentic information relationships are higher priority than pixel-for-pixel density when the latter makes the role unplayable on the accepted device class.

### Simulation speed is not neutral

NASA human-in-the-loop research found simulation speed affects workload and controllability.

Source:

- NTRS `20080042275`
- https://ntrs.nasa.gov/citations/20080042275

Design implication:

- time acceleration is a workload/difficulty change, not merely a convenience;
- D-016's continuous-clock semantics remain sound;
- any later accelerated mode needs explicit validation and should not be introduced casually to repair pacing.

## Central playability distinction

The project should distinguish **operational friction** from **interface friction**.

### Preserve operational friction

Preserve when historically or causally justified:

- incomplete or conflicting evidence;
- separate station information;
- waiting for another discipline's judgment;
- finite mission time;
- the need to consult rules/procedures;
- uncertain diagnosis;
- delayed crew response;
- consequences of late, omitted, or wrong actions;
- workload created by legitimately owning more than one original station.

### Remove interface friction

Treat as a modern design defect unless deliberately justified:

- not knowing which original station is active;
- scrolling past the one product the station is expected to monitor because of project layout;
- ambiguous modern button labels;
- exposing internal model terminology the controller would not have used;
- requiring a player to understand JSON/model architecture;
- duplicate or unnecessary confirmations;
- branch-specific controls that reveal which malfunction may occur;
- test-harness actions presented as if they were controller actions;
- losing state because of browser reload/rejoin behavior.

## Current prototype audit

The current `web/index.html` is an effective validation client, but several elements should be considered **test-surface behavior**, not final player-interface precedent.

### 1. Branch-specific CONTROL action can reveal the exercise

The player client permanently exposes:

`CALL OUT ΔP SHUTDOWN CRITERION`

before the synthetic branch occurs.

The player reference packet may legitimately provide the >25 psi ground criterion before the run, but a dedicated red branch-specific action button can turn a known rule into an implied scenario hint.

Final-interface direction:

- do not expose malfunction-specific game buttons simply because an exercise supports that branch;
- prefer a general controller communication/recommendation mechanism whose content is grounded in the station's rules and observations;
- keep the semantic event in the domain/audit model even if the UI verb becomes generic.

### 2. `ASSESS SHUTDOWN EVIDENCE` is validation scaffolding

The CONTROL action currently asks the server to assess the shutdown evidence and returns a machine-readable evidence result.

That is useful for integration testing. It is not a natural controller interaction. The player should inspect the fresh observation/crew report and form the assessment.

Final-interface direction:

- keep automated evaluation internally for scenario/debrief/validation;
- do not make a final player press a button whose purpose is to tell them whether the evidence is sufficient.

### 3. Developer metadata is visible on every field

The current generic field renderer shows:

`validity · source_layer`

This is valuable during model development because the truth/observation boundary is inspectable. It should not automatically survive into the final station UI.

Final-interface direction:

- expose historical/source-appropriate data-quality/status cues only when supported;
- keep provenance and hidden-integrity metadata available to facilitator/debrief tooling;
- do not require players to reason in project-internal terms such as `source_layer`.

### 4. Generic readiness controls are always present

Readiness reporting is a legitimate modeled action, but the current prototype presents it as a permanent generic form.

Final-interface direction:

- FLIGHT poll/readiness should become a clear operational interaction when relevant to the phase;
- avoid a game-like modal prompt that freezes the world;
- readiness reporting can remain possible without dominating the station during unrelated work.

## Player interaction loop

The existing gameplay model's loop remains strong:

`orient -> scan -> interpret -> consult rule/procedure -> communicate/recommend -> act -> verify`

Interface design should support that loop without collapsing steps.

### Orient

Persistent modern/session infrastructure may show:

- original station identity;
- authoritative GET;
- current mission/case phase;
- connection/synchronization state;
- for compact players, active original station.

These should be visually separated from the historical/project station product so they are not mistaken for Apollo console fields.

### Scan

The dominant area should be the station's actual decision-relevant products.

Requirements:

- critical values do not move unpredictably;
- related fields are spatially stable;
- historical/project format identity is clear;
- a compact player must switch stations deliberately rather than view merged data.

### Interpret

The screen should present evidence, not diagnosis.

Avoid:

- generic green/red health summaries;
- automatic rule evaluation presented as advice;
- anomaly highlighting unsupported by the historical system;
- cross-station aggregation that answers the player's question for them.

### Consult

Printed references remain functional. The project should optimize **findability**, not eliminate paper.

A future packet revision should test:

- short table of contents/index;
- call-sign-specific rule tabs;
- field name/measurement identifier cross-reference where historically justified;
- no branch-revealing “if this exercise happens” language.

### Communicate/recommend

Communication is the main cooperative verb.

Initial in-person direction:

- retain natural spoken communication across the table;
- keep CAPCOM's privileged crew-facing path explicit in software;
- keep FLIGHT decisions explicit;
- preserve station/action provenance in the audit log;
- do not implement elaborate simulated voice-loop audio until a scenario requires loop isolation for meaningful information asymmetry.

### Act

Player-facing actions should correspond to real controller decisions or communications, not test-harness state transitions.

The preferred pattern is:

`evidence -> controller judgment -> controller communication/authorized action -> simulated crew/system response`

not:

`evidence -> click scenario-specific solution button`

### Verify

After an action, the interface should expose the next historically appropriate observation/report. It should not label the result “correct.”

## Role-specific interaction priorities

### FLIGHT

Highest early UI priority because FLIGHT is coordination-heavy and data-light.

Needs:

- GET/phase;
- incoming readiness/recommendations with station identity and time;
- decision/poll state;
- crew-facing items approved for CAPCOM;
- enough timeline context to understand the cost of delay;
- no raw omniscient subsystem dashboard.

### CAPCOM

Needs a queue that makes three states unmistakable:

1. approved/queued;
2. transmitted;
3. crew receipt/readback/report.

The player should not have to invent technical content that another station owns.

### Technical stations

Need stable products and a small set of communication/action verbs.

A technical station should not become a dashboard of every modeled variable merely because the server has them.

### Compact roles

The active original station must be unmistakable.

Useful neutral aids that do not diagnose the vehicle may include:

- persistent original call-sign label;
- stable two-tab navigation;
- per-substation last-product-update GET;
- action confirmation naming the original station.

Avoid anomaly badges on inactive substations unless the corresponding alert is historically/player-visible; otherwise the UI becomes an unsolicited hint system.

## Onboarding and learning

Apollo controllers did not enter integrated simulation unprepared. The project's first-run experience therefore needs **part-task familiarization before full-team timed play**.

Minimum pre-run drills should cover:

- locate GET and current station identity;
- find one nominated field;
- locate one relevant rule/procedure;
- submit/read a readiness report;
- for FLIGHT, make a practice decision;
- for CAPCOM, transmit a practice queued item;
- for compact players, switch original substations and confirm attribution.

These drills should use neutral/practice data and should not reveal the live case's nonnominal injection.

A later short onboarding case may be preferable to relying on time acceleration to make PC+2 approachable.

## Pacing

Do not solve pacing by making the world wait for the player.

Preferred order of attack:

1. choose case boundaries that contain meaningful work;
2. improve player preparation and product findability;
3. create short part-task/onboarding cases;
4. only then reconsider time acceleration as an explicit, validated workload change.

PC+2 remains valuable as an integration case even if it eventually has a shorter training derivative initialized closer to the high-workload interval.

## Playability validation dimensions

Physical play should record at least these dimensions.

### Findability

- Could the player find the needed product/rule without facilitator help?
- Was the problem missing information or poor organization?

### Interpretation

- Could the player distinguish measured value, reference value, crew report, and controller conclusion?
- Did project-internal vocabulary create confusion?

### Interaction

- Were authorized actions clear?
- Did any control imply the intended diagnosis?
- Were accidental/wrong-station actions caused by UI ambiguity?

### Coordination

- Could players package useful callouts?
- Could FLIGHT understand what mattered without direct subsystem access?
- Did CAPCOM preserve the approved-message/actual-transmission distinction?

### Temporal workload

- Did the interface consume enough time to cause a missed operational opportunity?
- If so, was that because the job was difficult or because navigation was poor?

### Compact-role workload

- switching frequency;
- whether the player knew which station was active;
- missed updates while on the other station;
- wrong-station action attempts.

### Recovery

- reload/rejoin;
- transient network loss;
- resuming orientation after interruption.

## Suggested modern post-run ratings

These are usability evidence only, not a mission score and not Apollo procedure.

Use a 1–7 scale after the run for each player:

- I could tell which original station I was operating.
- I could find the information I needed in time.
- I understood what actions were available to my station.
- The interface helped me distinguish evidence from conclusions.
- The paper/reference material was easy to use during play.
- Communication with the other controllers was manageable.
- My workload came mainly from the operational problem rather than the interface.

Also ask one free-response question:

> What part of the interface most interfered with doing your controller job?

## Implementation sequence

1. **Instrument and classify** the existing validation client before redesign.
2. **Separate final-player concepts from test-harness concepts**: branch buttons, evidence-assessment controls, internal metadata.
3. **Prototype FLIGHT and CAPCOM first**, because their workload is interaction/coordination rather than dense telemetry reproduction.
4. **Prototype CONTROL and GUIDO product scanning** with stable phone layouts and the same sourced content.
5. **Exercise compact switching** without adding anomaly hints.
6. **Run seven-seat nominal human play**, then synthetic contingency.
7. **Run five-player compact play** and compare the defect/workload profile.
8. Only after those runs decide whether exact-format density, push transport, clock acceleration, or additional hard-copy aids are necessary.

## Decision boundary

This note does not accept a new final interface design, time-acceleration policy, voice-loop implementation, or historical console simplification.

It establishes which problems may be solved as modern usability design and which difficulties must remain because they are part of the simulated controller work.
