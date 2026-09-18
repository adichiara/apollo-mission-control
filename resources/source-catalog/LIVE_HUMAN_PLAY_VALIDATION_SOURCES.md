# Live human-play validation sources

Status: **IMPLEMENTATION-SOURCE — protocol/evidence/preparation/reference-packet boundaries defined; physical execution pending**

This supplement supports the project's first real-device/human integrated play validation. It distinguishes historical Mission Control training principles from modern browser/mobile usability validation, player-preparation mechanics, reference-packet mechanics, and debrief mechanics.

## Primary historical sources

### Martikan & Nassiff — Integrated operating mode of the Apollo mission simulator

- AIAA Paper 65-266.
- NTRS records: `19650039405` and `19660033487`.
- https://ntrs.nasa.gov/citations/19650039405
- https://ntrs.nasa.gov/citations/19660033487
- Relevant evidence: Apollo mission simulator integration with the Mission Control Center for combined flight- and ground-crew training.

Implementation use:

- supports validating the prototype as an integrated multi-role environment;
- supports treating isolated station testing as insufficient for the final first-playable boundary;
- supports capturing incidents in the context of the integrated mission rather than as detached UI events.

Does not establish:

- browser/mobile layout criteria;
- network latency limits;
- project facilitator authentication;
- exact prototype test sequence or report fields.

### Harold G. Miller — Simulation Training for Flight Control Decisionmaking

- NASA SP-209, 1970.
- NTRS document: `19700013438`.
- https://ntrs.nasa.gov/citations/19700013438
- Relevant evidence: flight-controller training included formal, intrinsic/on-the-job, and simulation training; final simulation occurred in the mission environment and emphasized decisionmaking, controller interfaces, procedures, adverse-condition response, and readiness.

Implementation use:

- supports observing information acquisition, decisionmaking, coordination, and procedure use during live play rather than measuring only software correctness;
- supports recording what information a controller had and what operational judgment/action followed;
- supports giving project players station responsibility, system/procedure context, and relevant rules before integrated timed play rather than treating zero prior preparation as historically representative;
- supports treating the reference packet as previously learned/available operational material rather than a scenario-reveal device.

Does not establish:

- a historical Apollo usability questionnaire;
- exact pass/fail UI timing metrics;
- modern mobile-device behavior;
- this project's defect taxonomy;
- a specific player briefing or packet format/duration.

### L. W. Keyser — The role of flight mission rules in mission preparation and conduct

- *Apollo experience report: The role of flight mission rules in mission preparation and conduct*.
- NASA-TN-D-7822 / JSC-S-417, November 1974.
- NTRS document: `19750002893`.
- https://ntrs.nasa.gov/citations/19750002893
- Relevant evidence: mission rules were developed through mission planning and testing/training, applied to real-time decisionmaking, defined operational responsibility/authority, and were used in training controllers/crews for nonnominal situations including circumstances without a preplanned response.

Implementation use:

- supports evaluating whether players can use station information, rules, judgment, and communication to reach operational decisions;
- supports preserving legitimate uncertainty rather than automatically classifying hesitation as a defect;
- supports making relevant PC+2 rules and authority boundaries available during player preparation without revealing whether a specific nonnominal event will occur;
- supports presenting rule criteria as neutral premission references rather than branch-specific hints.

Does not establish:

- a particular PC+2 playtest questionnaire;
- a browser presentation standard;
- that every difficult player decision indicates missing historical information;
- pre-briefing a trainee on the exact malfunction or intended solution for an exercise;
- this project's five-part reference-packet layout.

### Paul C. Kramer — Systems and Flight Procedures Development

- *Apollo Experience Report — Systems and Flight Procedures Development*.
- NASA-TN-D-7436 / JSC-S-366, September 1973.
- NTRS document: `19730023040`.
- https://ntrs.nasa.gov/citations/19730023040
- Relevant evidence: Apollo flight procedures integrated mission rules/requirements with spacecraft procedures; systems procedures and flight procedures were distinct categories; flight procedures were organized around mission phases; final procedures were verified during simulations involving crew, Mission Control, and the Manned Space Flight Network.

Implementation use:

- supports the general preparation principle that mission-phase procedures and rules existed before execution and were available as operational reference material;
- supports allowing project players to consult assigned rules/procedures rather than turning the live test into a memorization exercise;
- supports keeping station/system knowledge, decision criteria, and nominal mission-phase procedure context as distinct sections rather than collapsing them into a scenario solution checklist.

Scope warning:

- this source describes Apollo systems and flight-procedures development; it is not evidence for the exact content or format of a flight-controller training handout;
- it does not establish this project's station briefing pages, five-part packet order, browser instructions, compact-role instructions, or briefing duration.

### Apollo training / mission simulator history

- NTRS document: `19720005243`.
- https://ntrs.nasa.gov/citations/19720005243
- Relevant evidence: integration of Apollo mission simulators with the Mission Control Center as a major step in realistic crew/ground-controller training.

Implementation use:

- supports requiring simultaneous human roles and a shared mission context for the live validation milestone.

## Supporting official NASA training/debrief practice

### Evolution of Training in NASA's Mission Operations Directorate

- NTRS document: `20120002563`.
- https://ntrs.nasa.gov/citations/20120002563
- Relevant evidence: NASA's later explicit "train like you fly" framing — replicating the operational environment and using the same operational mindset in training.

Implementation use:

- supports using the normal player/facilitator authority boundaries and continuous mission-time behavior during play validation rather than creating a special simplified test mode.

This later source is supporting doctrine, not evidence that the exact phrase or modern training method was used during Apollo.

### NASA — Artemis I launch-team simulation practice

- NASA, *Simulations are 'Great Days' for NASA's Artemis I Launch Team*.
- https://www.nasa.gov/humans-in-space/simulations-are-great-days-for-nasas-artemis-i-launch-team/
- Relevant evidence: when an actual problem is uncovered during a simulation, the team documents it and collects useful data; after simulations, controllers conduct a team debrief covering problems, strengths, improvements, and possible procedure/requirement changes.

Implementation use:

- supports capturing material incidents during live play rather than relying on memory after the run;
- supports a structured post-run team debrief;
- supports keeping observed problems and proposed changes traceable.

Does not establish:

- the Apollo 13 debrief format;
- this project's incident schema or defect classes;
- any Apollo-era browser/mobile metric.

## Supporting modern human-factors / controller-training evidence

These sources are **not Apollo reconstruction evidence**. They are used only to define modern playability/usability questions worth measuring.

### NASA — Space Flight Resource Management training

- NTRS document: `20090041872`.
- https://ntrs.nasa.gov/citations/20090041872
- Relevant evidence: high workload can degrade performance; effective controller teams use communication, decisionmaking, and adaptive task distribution to manage demanding situations.

Implementation use:

- treat five-player compact mode as a workload change, not merely a player-count convenience;
- measure substation switching, missed information, and communication burden;
- distinguish legitimate operational workload from avoidable UI/navigation workload.

### NASA — Operational Evaluation of Artemis EVA Telemetry Display Concepts

- NTRS document: `20260005145`.
- https://ntrs.nasa.gov/citations/20260005145
- Relevant evidence: controller-facing display format affected response time, workload, and usability in operationally representative telemetry-monitoring tasks.

Implementation use:

- compare phone rendering approaches empirically while holding information content constant;
- do not assume exact visual density is automatically the most usable representation on the accepted device class;
- keep this as modern design guidance only, not historical evidence for Apollo display layout.

### NASA — Using Simulation Speeds to Differentiate Controller Interface Concepts

- NTRS document: `20080042275`.
- https://ntrs.nasa.gov/citations/20080042275
- Relevant evidence: simulation speed changed workload and controllability in a human-in-the-loop study.

Implementation use:

- treat any future time acceleration as a workload/difficulty intervention rather than a neutral convenience;
- prefer case-boundary and onboarding solutions before using acceleration to repair pacing.

## Derived project boundary

The live human-play run should validate:

- coherent shared mission time;
- separate station information/authority;
- distinct facilitator/simulation-control authority;
- human readiness and FLIGHT/CAPCOM coordination;
- phone/browser readability and rejoin behavior;
- reproducible pre-run player preparation covering station identity/responsibility, available products/actions, relevant PC+2 phase/rules/procedures, authority/coordination boundaries, and modern client-operation controls;
- a layered player reference packet that keeps common context, original-station responsibilities, rule criteria, nominal phase/procedure context, and modern client-operation instructions distinct;
- scenario blindness during preparation/reference use: no disclosure of whether/when the synthetic ΔP branch will occur, hidden state, another station's private evidence, or intended diagnosis/decision;
- explicit preservation of unresolved historical criteria rather than converting them into fabricated playable shortcuts;
- explicit classification of defects as historical/research, simulation, UI, network, instruction/training, or legitimate decision uncertainty;
- incident-level provenance tying observations to GET, run/build, player role, active original station, visible evidence, action, observed result, and audit/event references where available;
- a post-run debrief that separates observed fact, participant interpretation, reproducible defects, historical questions, and usability-only changes.

Modern browser, phone, HTTP, localStorage/sessionStorage, token mechanics, compact-role mechanics, player-preparation/reference-packet format, defect taxonomy, and report format remain project infrastructure, not Apollo reconstruction.

Player difficulty alone is not evidence for changing historical behavior. Any historical/procedural change prompted by play requires a separate source basis before implementation.

See `resources/research/090_live_device_human_play_validation_boundary.md`, `resources/research/095_live_play_evidence_capture_and_debrief.md`, `resources/research/096_live_play_player_preparation_boundary.md`, `resources/research/097_live_play_reference_packet_structure.md`, `docs/testing/PC2_PLAYER_PREPARATION.md`, `docs/testing/PC2_PLAYER_REFERENCE_PACKET.md`, `docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md`, and `docs/testing/PC2_LIVE_PLAYTEST_REPORT_TEMPLATE.md`.