# PC+2 live multi-device playtest protocol

Date: 2026-09-12  
Status: **READY FOR PHYSICAL EXECUTION — structured evidence/debrief and reproducible player preparation added 2026-09-13**

Purpose: close the remaining first-playable boundary with actual phones/browsers and human operators while keeping historical findings distinct from modern browser/mobile usability findings.

Use `PC2_LIVE_PLAYTEST_REPORT_TEMPLATE.md` for each run. Research notes 095 and 096 define the evidence/debrief and player-preparation boundaries.

## Required player preparation

Before a run used for first-playable validation, use `PC2_PLAYER_PREPARATION.md` rather than an ad hoc oral briefing.

For every participant record that:

- [ ] the common briefing was reviewed;
- [ ] station-specific responsibilities, products, actions, and relevant rules/procedures were available;
- [ ] basic client-operation checks were completed;
- [ ] compact players, if used, practiced one substation switch and could identify the active original station;
- [ ] the briefing did **not** reveal whether/when a nonnominal branch would occur, hidden state, another station's private evidence, or the intended diagnosis/decision.

Players may consult their assigned rules/procedures during timed play. The validation target is use of available operational information and judgment, not memorization.

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
- `PLAYER_INSTRUCTION` — required project preparation/instructions were absent or insufficient, not mission information;
- `NORMAL_DECISION_UNCERTAINTY` — uncertainty is legitimate and should not automatically become a defect.

Before classifying an incident as `PLAYER_INSTRUCTION`, check the participant's preparation record. If the expected information was included and available but remained difficult to locate or understand, consider `STATION_PRESENTATION` or another appropriate class instead.

Player confusion or a difficult decision is **not by itself evidence for a historical change**. Any change to historical procedure, authority, information, terminology, or modeled Apollo behavior requires separate source review.

### Playability-specific observations

Research note 313 adds a second classification axis: **operational friction** versus **interface friction**.

During the run, record when any of the following occurs:

- player cannot tell which original station is active;
- player cannot find a product or rule that is actually present;
- player uses or asks about a developer/test term such as model provenance rather than operational information;
- a control or label reveals the likely malfunction/solution before the evidence warrants it;
- player attempts an action under the wrong original station;
- compact-role player misses information while working the paired station;
- facilitator has to rescue the player from UI/navigation rather than from legitimate mission uncertainty;
- player misses an operational opportunity primarily because of interface navigation/search time;
- browser/network interruption causes loss of orientation after rejoin.

For each such incident, record whether the best provisional interpretation is:

- OPERATIONAL_FRICTION — the difficulty belongs to the simulated controller job; or
- INTERFACE_FRICTION — the difficulty was introduced by the modern project interface.

This label is supplemental to the existing defect class; it does not replace it.

### Scenario-blind interaction check

Before the synthetic ΔP run, confirm that the ordinary player surface does not reveal the branch merely by exposing a dedicated malfunction-named action or hint. Known mission rules may remain available as neutral reference material; the UI should not imply which rule will become relevant.

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

- number of substation switches and whether each switch was intentional;
- whether the player could identify the active original station immediately after switching;
- whether any important update was missed while the other substation was active;
- TELMU↔CONTROL switching under time pressure;
- GUIDO↔FIDO/RETRO switching under time pressure;
- whether the active original station is always clear;
- whether readiness/actions are attributed to the intended original station;
- whether bundled presentation causes information leakage or missed information.

`LM SYSTEMS` and `FLIGHT DYNAMICS` remain modern player-group labels only. Incident and audit evidence must identify original Apollo station identities.

## Pass criteria

The live-device boundary is considered passed when:

- the documented player-preparation package was used and preparation records were captured;
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
- player-preparation record;
- result: PASS / PASS WITH NONBLOCKING DEFECTS / BLOCKED;
- incident-level evidence;
- blocking defects;
- nonblocking defects;
- research gaps requiring source review;
- changes made after the run;
- regression tests added for reproducible software defects.

## Historical boundary

The integrated-role concept is source-backed by Apollo/NASA simulation-training material. Apollo mission-rule evidence also supports observing how controllers use rules and judgment during training. Primary Apollo controller-training evidence supports giving players station responsibilities, procedures/rules, and system context before integrated simulation; it does not establish this project's briefing format or duration.

The checklist's phone/browser, reload, latency, token, compact-role, preparation-record, defect-taxonomy, and report-format criteria are modern project validation mechanics and are not presented as Apollo-era procedures.

Later NASA simulation/debrief practice is used only as supporting validation-process evidence, not as a claim about the exact Apollo 13 debrief format.

See research notes 090, 095, and 096; `resources/source-catalog/LIVE_HUMAN_PLAY_VALIDATION_SOURCES.md`; `docs/testing/PC2_PLAYER_PREPARATION.md`; and `docs/testing/PC2_LIVE_PLAYTEST_REPORT_TEMPLATE.md`.