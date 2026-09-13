# Live human-play validation sources

Status: **IMPLEMENTATION-SOURCE — protocol/evidence boundary defined; physical execution pending**

This supplement supports the project's first real-device/human integrated play validation. It distinguishes historical Mission Control training principles from modern browser/mobile usability validation and debrief mechanics.

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
- Relevant evidence: simulation in a mission environment as final readiness training for flight controllers; emphasis on decisionmaking, controller interfaces, procedures, and adverse-condition response.

Implementation use:

- supports observing information acquisition, decisionmaking, coordination, and procedure use during live play rather than measuring only software correctness;
- supports recording what information a controller had and what operational judgment/action followed.

Does not establish:

- a historical Apollo usability questionnaire;
- exact pass/fail UI timing metrics;
- modern mobile-device behavior;
- this project's defect taxonomy.

### L. W. Keyser — The role of flight mission rules in mission preparation and conduct

- *Apollo experience report: The role of flight mission rules in mission preparation and conduct*.
- NASA-TN-D-7822 / JSC-S-417, November 1974.
- NTRS document: `19750002893`.
- https://ntrs.nasa.gov/citations/19750002893
- Relevant evidence: mission rules were developed through mission planning and testing/training, applied to real-time decisionmaking, and used in training controllers/crews for nonnominal situations including circumstances without a preplanned response.

Implementation use:

- supports evaluating whether players can use station information, rules, judgment, and communication to reach operational decisions;
- supports preserving legitimate uncertainty rather than automatically classifying hesitation as a defect.

Does not establish:

- a particular PC+2 playtest questionnaire;
- a browser presentation standard;
- that every difficult player decision indicates missing historical information.

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

## Derived project boundary

The live human-play run should validate:

- coherent shared mission time;
- separate station information/authority;
- distinct facilitator/simulation-control authority;
- human readiness and FLIGHT/CAPCOM coordination;
- phone/browser readability and rejoin behavior;
- explicit classification of defects as historical/research, simulation, UI, network, instruction/training, or legitimate decision uncertainty;
- incident-level provenance tying observations to GET, run/build, player role, active original station, visible evidence, action, observed result, and audit/event references where available;
- a post-run debrief that separates observed fact, participant interpretation, reproducible defects, historical questions, and usability-only changes.

Modern browser, phone, HTTP, localStorage/sessionStorage, token mechanics, defect taxonomy, and report format remain project infrastructure, not Apollo reconstruction.

Player difficulty alone is not evidence for changing historical behavior. Any historical/procedural change prompted by play requires a separate source basis before implementation.

See `resources/research/090_live_device_human_play_validation_boundary.md`, `resources/research/095_live_play_evidence_capture_and_debrief.md`, `docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md`, and `docs/testing/PC2_LIVE_PLAYTEST_REPORT_TEMPLATE.md`.