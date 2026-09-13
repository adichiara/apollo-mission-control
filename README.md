# Apollo Mission Control

A cooperative, historically grounded simulation of Apollo-era Mission Control.

Players sit together as flight controllers. Each player uses a phone as the display/interface for one or more assigned controller stations and printed controller material as needed. A central authoritative server owns the live mission simulation.

## Project standard

This project is **research first**. Apollo operations, terminology, displays, roles, procedures, telemetry, mission timelines, failure behavior, and simulator scenarios are implemented from historical documentation wherever documentation exists.

If a required detail is not documented or has not yet been found, it is recorded as unresolved. It is not silently invented.

See:

- [Project principles](docs/PROJECT_PRINCIPLES.md)
- [Roadmap](docs/ROADMAP.md)
- [Current first-playable integration roadmap](docs/roadmap/2026-09-12_first_playable_integration.md)
- [Decisions](docs/DECISIONS.md)
- [Simulation architecture](docs/SIMULATION_ARCHITECTURE.md)
- [Gameplay model](docs/GAMEPLAY_MODEL.md) — design proposal, not accepted
- [PC+2 player products](docs/scenarios/APOLLO13_PC2_PLAYER_PRODUCTS.md)
- [PC+2 player preparation](docs/testing/PC2_PLAYER_PREPARATION.md)
- [PC+2 player reference packet](docs/testing/PC2_PLAYER_REFERENCE_PACKET.md)
- [Live playtest protocol](docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md)
- [Live playtest report template](docs/testing/PC2_LIVE_PLAYTEST_REPORT_TEMPLATE.md)
- [Research resources](resources/README.md)
- [Evidence verification audit](resources/audits/2026-09-11_EVIDENCE_VERIFICATION.md)

## Current status

The first implementation-oriented vertical slice is **Apollo 13 PC+2 preparation and execution**.

The model now includes source-backed PC+2 progression, continuous mission time, station-specific products, shutdown/restart branches, explicit communication/action/physical/evidence layers, first-pass views for CONTROL/GUIDO/TELMU/FIDO-RETRO/INCO/FLIGHT/CAPCOM, browser rejoin, CAPCOM handoff, audit logging, the source-bounded synthetic ΔP branch through fresh CONTROL evidence, facilitator authority, automated multi-client validation, end-to-end compact station-set ownership through the HTTP/browser layer, a structured live-play evidence/debrief package, a reproducible scenario-blind player-preparation package, a source-constrained first-run player reference packet, and a source-bounded staged final state-vector/target-load/uplink workflow.

The compact HTTP/browser path and staged final-load regression coverage are recorded as passing automated CI. The remaining major validation boundary is real-device/browser and human-play execution.

## Phone-accessible first playable shell

The repository contains a thin **FastAPI + Uvicorn** transport with two browser surfaces:

- `/` — ordinary station player client;
- `/admin` — facilitator/SimSup validation console.

The player client contains station-authorized information and actions only. Exercise-wide functions such as reset/lifecycle, manual validation time, source injection, simulated crew/vehicle response, and global audit access are facilitator operations.

### Facilitator authority

When `APOLLO_FACILITATOR_TOKEN` is configured, protected operations require the `X-Apollo-Facilitator` header. Render deployments receive a generated secret through `render.yaml`; no credential value is committed to the repository. This token mechanism is a modern software safety boundary, not Apollo-era authentication reconstruction.

### Rejoin behavior

Single-station clients use `/api/session/join`. Compact clients use `/api/session/join-set` with the exact original-station set they own.

Rejoin is idempotent only for the same player and same assignment. A player cannot silently switch stations or mutate its compact station set, and another player cannot take an occupied original station.

Browser identity is prototype persistence, not cryptographic authentication.

## Compact five-player mode

Primary Apollo organizational sources constrain the compact project configuration without establishing it as historical staffing:

- FLIGHT;
- CAPCOM;
- LM SYSTEMS = TELMU + CONTROL;
- FLIGHT DYNAMICS = GUIDO + FIDO/RETRO;
- INCO.

`LM SYSTEMS` and `FLIGHT DYNAMICS` are simulator role labels only. Original station identities remain authoritative.

The compact path is implemented end to end:

- `PC2Session.assign_stations()` owns multiple original stations for one player;
- bundled snapshots retain separate station presentations;
- readiness/actions remain station-qualified;
- `/api/session/join-set` exposes exact station-set join/rejoin;
- player snapshot polling returns bundled data for multi-station players;
- the browser persists the station set and active substation;
- TELMU/CONTROL and GUIDO/FIDO-RETRO are navigated through explicit original-call-sign tabs rather than a merged synthetic console.

Research note 094 resolves the previously open general four-player question for this PC+2 fidelity target: **five players are the minimum supported configuration**. CAPCOM and INCO remain separate because Apollo sources distinguish crew-facing voice authority from communications-system monitoring/troubleshooting, and communications/data-path state is active during PC+2 preparation. This is a simulator-design boundary, not a historical minimum-staffing claim.

See research notes 091–094 and decision D-018.

## Core engine rule: mission time is continuous

GET advances whenever the session is running. Pending controller decisions do not stop GET. Missing prerequisites may make a nominal event ineligible when its time arrives; missed nominal events are recorded and not replayed retroactively. Only an explicit game/session pause stops simulated mission time.

See research notes 081 and 084 and decision D-016.

## Final PC+2 state-vector / target-load path

Research notes 098–099 replace the former generic final-load verification state with a source-bounded staged workflow:

`FIDO/RTCC final solution → GUIDO load readiness/consistency → INCO uplink configuration → CAPCOM/crew configuration → state-vector + target-load transmission → load complete / computer returned to crew`

The authoritative model distinguishes `preliminary` → `final_ready` → `final_stable` solution state and `preliminary_loaded` → `final_pending` → `transmitting` → `final_loaded` load state. The earlier approximately 75:35 GET load is treated as completed context before the 77:55 scenario start. Ranging remains a separate final-preparation dependency.

This does **not** reconstruct exact Cartesian vector contents, RTCC/CCATS commands, controller keying, byte/word load contents, or exact transmission duration. Those remain explicitly deferred.

## First nonnominal end-to-end chain

The source-bounded synthetic ΔP branch reaches fresh controller evidence through:

`source observation → CONTROL product/rule → CONTROL decision → CAPCOM queue/transmission → crew receipt → crew shutdown command → physical DPS response → crew report / fresh GQ6510P evidence → CONTROL evidence assessment`

Every step remains explicit. CAPCOM transmission does not imply crew receipt, crew command does not imply physical shutdown, physical response does not fabricate telemetry evidence, and CONTROL assessment never reads hidden `engine_running` truth. No pressure magnitude is interpreted as a binary engine-off threshold.

## Integrated validation

- `tests/test_web_multiclient_integration.py` covers independent station clients plus facilitator authority in-process.
- `scripts/pc2_multiclient_smoke.py` exercises the established full-station path over real TCP/HTTP.
- `tests/test_web_compact_roles.py` covers compact station-set join/rejoin, bundled snapshots, station-qualified readiness, station conflicts, and CONTROL authority inside a bundle.
- `tests/test_web_client_contract.py` covers compact browser persistence/navigation and active-station attribution.
- `tests/test_pc2_final_load_workflow.py` covers staged final-solution/load transitions and station-separated workflow products.

The automated compact HTTP/browser path is recorded as passing GitHub Actions. Staged final-load regression coverage passed GitHub Actions run 118. Physical seven-seat and five-player compact human/device validation are not yet claimed.

Research note 095 adds the evidence discipline for those physical runs: material incidents should retain run/build, GET, player role, active original station, visible evidence, action, expected/observed result, and audit/event references where available. The debrief must distinguish reproducible defects and historical questions from player instruction issues and legitimate controller uncertainty. Player difficulty alone is not grounds for inventing or changing Apollo behavior.

Research note 096 closes the preparation ambiguity behind `PLAYER_INSTRUCTION`. Apollo controller-training and mission-rule sources support prior station/system/procedure preparation before integrated simulation, so the project now uses `PC2_PLAYER_PREPARATION.md` before timed play. Players receive station responsibilities, relevant products/actions/rules/procedures, authority context, and modern client-operation knowledge, but are not told whether or when the synthetic nonnominal branch will occur or given hidden/other-station information. The package format itself is a modern validation aid.

Research note 097 resolves the initial reference-packet organization question for first physical play. `PC2_PLAYER_REFERENCE_PACKET.md` keeps common operational context, original-station sheets, neutral rule/criterion references, nominal phase/procedure context, and visibly modern client-operation instructions separate. Compact players still receive separate original-station references. The layout is a project adaptation, and unresolved historical criteria remain unresolved rather than being turned into hints.

## Historical/presentation boundaries retained

- Apollo 13 MSK 1137 `TCP` percent is not equated to modeled `GQ6510P` psi.
- TELMU's documented 38–40 A PC+2 burn figure remains a reference value, not fabricated live telemetry.
- GUIDO residuals are not substituted for a missing FIDO propagated trajectory solution.
- INCO link quality, voice, telemetry, ranging, uplink configuration, and load-transmission state remain distinct products.
- Hidden product integrity never appears automatically in a player view.
- Exact CRT/console layouts are not invented where evidence is incomplete.

## Remaining bounded historical gaps

The singular PC+2 150-psi ground engine-inlet-pressure criterion remains `NOT_EVALUABLE`; the exact historical ground selection/aggregation rule is unresolved. The onboard 77-percent thrust-monitor criterion also remains `NOT_EVALUABLE`; the rule is documented but the exact crew indication/source is unresolved.

Detailed DPS transients, exact display routing/cadence, exact final-load RTCC/CCATS internals, and a post-burn FIDO trajectory propagator remain deferred until a concrete dependency requires them.

## Immediate priorities

1. Prepare each participant from `docs/testing/PC2_PLAYER_PREPARATION.md`, provide `docs/testing/PC2_PLAYER_REFERENCE_PACKET.md`, record completion, and preserve scenario blindness.
2. Run `docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md` with actual simultaneous station phones/browsers and one facilitator console.
3. Record the run in `docs/testing/PC2_LIVE_PLAYTEST_REPORT_TEMPLATE.md` so preparation, defects, and research questions remain traceable to build/GET/station evidence.
4. Run nominal PC+2 first, including the staged final-solution/load/uplink handoff, then the synthetic ΔP branch.
5. Run the approved five-player compact configuration and evaluate TELMU↔CONTROL and GUIDO↔FIDO/RETRO switching, readiness/action attribution, information isolation, and reference-packet findability.
6. Repair reproducible network/mobile/presentation/instruction defects and add regression coverage.
7. Reopen historical research only when validation exposes a concrete missing procedure, authority, information, terminology, or player-count dependency.

## Apollo 13 station specifications

Detailed research specifications are under `docs/stations/`:

- [EECOM](docs/stations/APOLLO13_EECOM.md)
- [GNC](docs/stations/APOLLO13_GNC.md)
- [GUIDO](docs/stations/APOLLO13_GUIDO.md)
- [TELMU](docs/stations/APOLLO13_TELMU.md)
- [CONTROL](docs/stations/APOLLO13_CONTROL.md)
- [INCO](docs/stations/APOLLO13_INCO.md)
- [FIDO](docs/stations/APOLLO13_FIDO.md)
- [RETRO](docs/stations/APOLLO13_RETRO.md)