# First playable web transport selection — FastAPI / Uvicorn / Render

Date: 2026-09-12  
Status: **IMPLEMENTED FOR FIRST PLAYABLE PROTOTYPE — domain model remains framework-neutral**

## Question

What is the thinnest web transport that can expose the existing authoritative PC+2 session to several phone/browser clients, deploy cleanly on Render, and preserve the option for later realtime communication without moving simulation logic into the web framework?

## Current platform evidence

### Render

Render's current FastAPI guidance provides a native Python web-service path and a Uvicorn-based ASGI deployment model. Render supports Git-backed web services and dynamic port binding, and documents FastAPI as a supported Python framework.

Render also supports setting the Python runtime with a root `.python-version` file. The project pins the first transport prototype to Python 3.13 rather than relying on Render's changing default Python version.

### FastAPI / Uvicorn

FastAPI's official deployment documentation supports running the application through Uvicorn/ASGI. ASGI is also compatible with future WebSocket or streaming work if later playtesting shows polling is insufficient.

## Decision

Use **FastAPI + Uvicorn** as a thin transport adapter for the first playable prototype.

Reasons:

- direct JSON request/response mapping fits the existing dataclass/domain API;
- automatic request validation reduces transport boilerplate;
- ASGI leaves a clean path to later realtime push;
- Render has a straightforward supported deployment path;
- FastAPI can serve the temporary phone-first static shell without introducing a frontend build system;
- the simulation/session modules remain importable and testable without FastAPI.

This is a transport choice, not a simulation-architecture choice.

## First implementation

Added:

- `src/apollo_mission_control/web_app.py` — in-memory single-session API adapter;
- `web/index.html` — dependency-free phone-first prototype client;
- `requirements.txt` — `fastapi[standard]`;
- `.python-version` — Python 3.13;
- `render.yaml` — Render build/start/health-check configuration;
- `tests/test_web_app.py` — API/transport integration tests.

## API boundary

The first transport exposes operations for:

- create/reset PC+2 session;
- session status;
- station join/assignment;
- start/pause/resume;
- authoritative GET advancement;
- player-scoped snapshot retrieval;
- readiness reporting;
- FLIGHT GO/NO-GO decision;
- FLIGHT→CAPCOM queueing;
- CAPCOM transmission;
- audit retrieval for prototype validation.

The HTTP adapter converts domain `ValueError` conditions into client errors but does not reimplement simulation rules.

## Phone-first shell

The static client intentionally has no frontend framework/build chain. It provides:

- station assignment;
- current session status / GET / phase / decision gate;
- generic rendering of existing station presentation dataclasses;
- readiness reporting;
- FLIGHT GO/NO-GO and CAPCOM-queue controls;
- CAPCOM transmit controls;
- temporary manual GET advancement for integration testing.

Manual time advancement is explicitly prototype infrastructure, not a final game mechanic.

## Critical deployment limitation

The first web prototype stores the session **in process memory**.

Therefore:

- a process restart/deploy loses the live session;
- Render free-service spin-down would lose an in-memory game;
- multiple workers/instances would not share one authoritative session;
- this configuration must remain single-process until shared persistence/session coordination is deliberately added.

This limitation is acceptable for the first integration milestone because the purpose is to validate the multiplayer workflow and information boundaries, not production persistence.

## Deferred

- authentication/security beyond a simple player ID;
- durable session persistence;
- multiple concurrent mission sessions;
- WebSocket/server-sent-event push;
- wall-clock mission driver;
- reconnect tokens;
- production rate limiting;
- production-grade audit storage;
- frontend framework/build system.

## Sources

Current external platform documentation reviewed 2026-09-12:

- Render, **FastAPI** template/documentation: https://render.com/templates/fastapi
- Render, **Setting Your Python Version**: https://render.com/docs/python-version
- Render, **Your First Render Deploy**: https://render.com/docs/your-first-deploy
- FastAPI, **Run a Server Manually / Uvicorn**: https://fastapi.tiangolo.com/deployment/manually/

Repository basis:

- `resources/research/079_pc2_first_playable_session_boundary.md`
- `docs/roadmap/2026-09-12_first_playable_integration.md`

## Next priority

Validate the HTTP/mobile shell with the scripted nominal session path, then add a real-time mission clock/driver and reconnect-safe player identity before attempting a deployed playtest.
