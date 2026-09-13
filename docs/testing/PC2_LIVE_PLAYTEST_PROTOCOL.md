# PC+2 live multi-device playtest protocol

Date: 2026-09-12  
Status: **READY FOR PHYSICAL EXECUTION — structured evidence/debrief package added 2026-09-13**

Purpose: close the remaining first-playable boundary with actual phones/browsers and human operators while keeping historical findings distinct from modern browser/mobile usability findings.

Use `PC2_LIVE_PLAYTEST_REPORT_TEMPLATE.md` for each run. Research note 095 defines the evidence/debrief boundary.

## Minimum setup

- one dedicated authoritative server;
- one facilitator on `/admin`;
- separate players/devices for FLIGHT, CONTROL, CAPCOM, GUIDO;
- preferably TELMU, FIDO/RETRO, and INCO when enough players/devices are available;
- facilitator credential configured;
- no shared player credentials/stations;
- normal realtime pacing and continuous GET.

## Run 1 — nominal PC+2

### Pre-run checks

- [ ] each player joins only the assigned station;
- [ ] attempting to take an occupied station is rejected;
- [ ] facilitator-only operations are unavailable from player clients;
- [ ] all clients show a coherent GET;
- [ ] facilitator pause/resume is reflected on all devices;
- [ ] one player reloads the page and rejoins the same station automatically;
- [ ] reload does not permit silent station switching;
- [ ] no station exposes another station's private operational collections.

### Mission run

- [ ] resume/start normal realtime PC+2 operation;
- [ ] do not pause merely because a player is thinking;
- [ ] do not provide out-of-band facilitator coaching about hidden state;
- [ ] subsystem players form readiness judgments from their own displays;
- [ ] FLIGHT receives/understands readiness state and makes the modeled GO/NO-GO decision;
- [ ] CAPCOM receives the approved communication item and deliberately transmits it;
- [ ] nominal events whose prerequisites are satisfied occur at the modeled times;
- [ ] any missed prerequisite remains missed rather than replaying automatically;
- [ ] players can complete the immediate post-burn path without facilitator interpretation of station data.

### Human factors / evidence observations

For each blocking, confusing, or materially informative incident record at minimum:

- incident ID;
- GET and wall-clock time;
- scenario/run ID and server commit;
- player role and active **original station**;
- device/browser;
- what the player was trying to determine/do;
- what was actually visible to that station;
- action/communication taken, if any;
- what the player expected;
- what occurred;
- whether another station or facilitator had to explain the interface or hidden/project information;
- relevant audit/event reference where available;
- provisional defect class below;
- whether historical source review is required before changing behavior.

Defect classes:

- `HISTORICAL_RESEARCH_GAP` — sourced information/procedure/authority may be missing;
- `SIMULATION_BEHAVIOR` — modeled state/action/evidence behavior is wrong or incomplete;
- `STATION_PRESENTATION` — correct information exists but is unclear/poorly organized;
- `NETWORK_CLIENT` — latency/reconnect/browser behavior;
- `PLAYER_INSTRUCTION` — player lacks project instructions/training, not mission information;
- `NORMAL_DECISION_UNCERTAINTY` — uncertainty is legitimate and should not automatically become a defect.

Player confusion or a difficult decision is **not by itself evidence for a historical change**. Any change to historical procedure, authority, information, terminology, or modeled Apollo behavior requires separate source review.

## Run 2 — synthetic ΔP branch

Only after the nominal run is coherent.

- [ ] facilitator injects the existing source-bounded synthetic ΔP condition;
- [ ] CONTROL detects/evaluates the >25 psi rule using its own product;
- [ ] CONTROL explicitly initiates the callout action;
- [ ] CAPCOM receives and explicitly transmits the queued message;
- [ ] crew receipt, shutdown command, and physical response remain separate explicit modeled steps;
- [ ] fresh crew-report / chamber-pressure evidence reaches CONTROL without hidden engine-state leakage;
- [ ] stale pre-command chamber pressure does not count as shutdown-response evidence;
- [ ] no player treats the synthetic 26 psi or validation pressure values as historical Apollo measurements.

## Five-player compact repeat

After the seven-seat path is coherent, repeat the nominal run with:

- FLIGHT;
- CAPCOM;
- LM SYSTEMS = TELMU + CONTROL;
- FLIGHT DYNAMICS = GUIDO + FIDO/RETRO;
- INCO.

Record especially:

- TELMU↔CONTROL switching under time pressure;
- GUIDO↔FIDO/RETRO switching under time pressure;
- whether the active original station is always clear;
- whether readiness/actions are attributed to the intended original station;
- whether bundled presentation causes information leakage or missed information.

`LM SYSTEMS` and `FLIGHT DYNAMICS` remain modern player-group labels only. Incident and audit evidence must identify original Apollo station identities.

## Pass criteria

The live-device boundary is considered passed when:

- all required real-device identity/rejoin and authority-isolation checks work;
- shared GET remains coherent enough for normal play;
- the nominal PC+2 coordination path is completed by human operators without hidden facilitator guidance;
- FLIGHT/CAPCOM handoff is understandable in actual play;
- no station information-boundary leak is observed;
- no blocking phone-readability or interaction defect remains unresolved;
- any historical change prompted by play has a separate primary-source basis before implementation.

## Required debrief

At the end of each run, use the report template to record separately:

- what worked as intended;
- problems actually observed;
- player misunderstandings that are instructional rather than software defects;
- legitimate decision uncertainty that should remain;
- reproducible simulation/presentation/network defects;
- historical/procedural questions requiring source review;
- usability-only changes that are explicitly modern simulator adaptations.

Do not collapse participant interpretation into observed fact. Preserve incident/audit references where available.

## Report template

Use `docs/testing/PC2_LIVE_PLAYTEST_REPORT_TEMPLATE.md`. At minimum the completed report must contain:

- date/server build or commit;
- participating stations and devices;
- nominal or ΔP scenario;
- result: PASS / PASS WITH NONBLOCKING DEFECTS / BLOCKED;
- incident-level evidence;
- blocking defects;
- nonblocking defects;
- research gaps requiring source review;
- changes made after the run;
- regression tests added for reproducible software defects.

## Historical boundary

The integrated-role concept is source-backed by Apollo/NASA simulation-training material. Apollo mission-rule evidence also supports observing how controllers use rules and judgment during training. The checklist's phone/browser, reload, latency, token, defect-taxonomy, and report-format criteria are modern project validation mechanics and are not presented as Apollo-era procedures.

Later NASA simulation/debrief practice is used only as supporting validation-process evidence, not as a claim about the exact Apollo 13 debrief format.

See research notes 090 and 095 and `resources/source-catalog/LIVE_HUMAN_PLAY_VALIDATION_SOURCES.md`.