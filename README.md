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
- [Research resources](resources/README.md)
- [Evidence verification audit](resources/audits/2026-09-11_EVIDENCE_VERIFICATION.md)

## Current status

The first implementation-oriented vertical slice is **Apollo 13 PC+2 preparation and execution**.

The domain/session model now includes source-backed PC+2 progression, declarative event prerequisites, station-specific products, shutdown/restart branches, explicit communication/action/physical/evidence layers, first-pass views for CONTROL/GUIDO/TELMU/FIDO-RETRO/INCO/FLIGHT/CAPCOM, one authoritative continuous-time session, browser rejoin, CAPCOM handoff, audit logging, a complete source-bounded synthetic ΔP branch through fresh CONTROL evidence, and framework-neutral multi-station player ownership for compact play.

Automated integrated validation passes both in-process and over real TCP/HTTP on the established full-station path. The remaining major validation boundary is real-device/browser and human-play validation; compact HTTP/browser integration is also still pending.

## Phone-accessible first playable shell

The repository contains a thin **FastAPI + Uvicorn** transport with two browser surfaces:

- `/` — ordinary station player client;
- `/admin` — facilitator/SimSup validation console.

The player client contains station-authorized information and actions only. Exercise-wide functions such as reset/lifecycle, manual validation time, source injection, simulated crew/vehicle response, and global audit access are facilitator operations.

### Facilitator authority

Primary NASA simulation sources support treating Simulation Supervisor / simulation-control authority as organizationally distinct from the flight controllers being trained. The project therefore keeps facilitator authority separate from every controller station.

When `APOLLO_FACILITATOR_TOKEN` is configured, protected operations require the `X-Apollo-Facilitator` HTTP header. Render deployments receive a generated secret through `render.yaml`; no credential value is committed to the repository. A Render instance fails closed if the secret is unexpectedly absent.

This token mechanism is a modern software safety boundary, **not** a reconstruction of Apollo-era authentication. See research note `088_facilitator_authority_boundary.md` and decision D-017.

### Rejoin behavior

A browser/client may repeat the same player ID + station assignment to rejoin its existing station without modifying mission state. The same player ID cannot silently switch stations, and a different player cannot take an occupied station.

This is lightweight prototype player identity, not cryptographic authentication. The current HTTP/browser contract is still single-station; compact station-set rejoin is the next transport/client boundary.

## Compact five-player mode

Primary Apollo 13 organizational sources constrain the first compact project configuration without establishing it as historical staffing:

- FLIGHT;
- CAPCOM;
- LM SYSTEMS = TELMU + CONTROL;
- FLIGHT DYNAMICS = GUIDO + FIDO/RETRO;
- INCO.

`LM SYSTEMS` and bundled `FLIGHT DYNAMICS` are simulator role labels only. The domain layer continues to represent the original station identities separately.

`PC2Session` now supports one player owning multiple original stations through `assign_stations()`, with separate station presentations, station-qualified readiness/actions, and original-station audit provenance. HTTP join/rejoin and browser navigation for this mode remain to be implemented.

See research notes 091–092 and decision D-018.

## Core engine rule: mission time is continuous

The engine is a **continuously evolving mission**, not a sequence of scenes waiting for player input.

- GET advances whenever the session is running;
- pending controller decisions do not stop GET;
- missing prerequisites may make a nominal event ineligible when its time arrives;
- missed nominal events are recorded and not replayed retroactively;
- only an explicit game/session pause stops simulated mission time.

For the PC+2 final readiness sequence, the approximately **79:17 GET** FLIGHT poll opens a `flight_go` requirement while the clock continues. A late GO does not rewind the mission or retroactively activate missed P40/ullage/ignition milestones.

See research notes 081 and 084 and decision D-016.

## First nonnominal end-to-end chain

The source-bounded synthetic ΔP branch reaches fresh controller evidence through:

`source observation → CONTROL product/rule → CONTROL decision → CAPCOM queue/transmission → crew receipt → crew shutdown command → physical DPS response → crew report / fresh GQ6510P evidence → CONTROL evidence assessment`

Every step remains explicit. CAPCOM transmission does not imply crew receipt, crew command does not imply physical engine shutdown, physical response does not fabricate telemetry evidence, and CONTROL assessment never reads hidden `engine_running` truth.

No pressure magnitude is interpreted as a binary engine-off threshold.

## Integrated validation

Primary NASA simulation-training material supports validating flight controllers together in a mission environment while keeping simulation control distinct. The project uses that historical boundary without treating its modern HTTP/browser mechanics as Apollo hardware/software.

Two validation artifacts exist:

- `tests/test_web_multiclient_integration.py` — independent FLIGHT, CONTROL, CAPCOM, GUIDO, and facilitator clients sharing one in-process authoritative session;
- `scripts/pc2_multiclient_smoke.py` — destructive real-network smoke runner for a dedicated local or deployed validation server.

GitHub Actions executes the complete unit/integration suite and launches an ephemeral authorized Uvicorn server to run the network smoke over actual TCP/HTTP. The established full-station paths are recorded as passing; compact ownership regression coverage was added with the new domain implementation.

The network runner checks simultaneous station polling, rejoin, explicit pause, facilitator/player authority isolation, the complete synthetic ΔP branch, fresh CONTROL evidence, and audit ordering.

Example against a local server:

```bash
python scripts/pc2_multiclient_smoke.py http://127.0.0.1:8000
```

For an authorized deployment, set `APOLLO_FACILITATOR_TOKEN` or pass `--facilitator-token`.

See research note `089_multiclient_integrated_validation_boundary.md`.

## Historical/presentation boundaries retained

- Apollo 13 MSK 1137 `TCP` percent is not equated to modeled `GQ6510P` psi.
- TELMU's documented **38–40 A** PC+2 burn figure remains a reference value, not fabricated live telemetry.
- GUIDO residuals are not substituted for a missing FIDO propagated trajectory solution.
- INCO link quality, voice, telemetry, ranging, and uplink remain distinct products.
- Hidden product integrity never appears automatically in a player view.
- Exact CRT/console layouts are not invented where evidence is incomplete.

## Remaining bounded historical gaps

The singular PC+2 150-psi ground **engine inlet pressure** criterion remains intentionally `NOT_EVALUABLE`; the exact historical ground selection/aggregation rule is unresolved.

The onboard **77-percent thrust-monitor** criterion also remains `NOT_EVALUABLE`; the rule is documented but the exact crew indication/source is unresolved.

Detailed DPS transients, exact display routing/cadence, and a post-burn FIDO trajectory propagator remain deferred until a concrete integration dependency requires them.

## Immediate priorities

Two tracks can proceed without weakening the historical boundary.

### Live full-station validation

1. run several real phone/browser station clients plus one facilitator console against one dedicated authoritative server;
2. verify continuous GET, facilitator pause/resume, reload/rejoin, station isolation, and authority isolation under actual browser/network conditions;
3. run the nominal PC+2 sequence with human operators and assess FLIGHT/CAPCOM handoff ergonomics;
4. repair usability/integration problems exposed by actual realtime play;
5. run the synthetic ΔP branch after nominal coordination is coherent.

### Compact transport/client integration

1. extend HTTP join/rejoin to approved station sets while retaining the existing single-station contract;
2. return bundled snapshots for multi-station players;
3. add browser persistence and station-switch/subpanel navigation with original call signs visible;
4. test readiness attribution, action authority, rejoin, and information isolation;
5. run five-player human validation after the seven-seat baseline.

Historical research is reopened only when integrated play or compact implementation exposes a concrete missing dependency.

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
