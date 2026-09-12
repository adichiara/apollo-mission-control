# Web Transport / Deployment Sources

Status: active implementation-source supplement for the first playable web transport.

## 1. Render — FastAPI deployment

- **Provider:** Render
- **Source class:** CURRENT PLATFORM DOCUMENTATION
- **URL:** https://render.com/templates/fastapi
- **Use:** Supports FastAPI/Uvicorn as a normal Render Python web-service deployment pattern.
- **Implementation consequence:** The first playable transport uses FastAPI with Uvicorn and binds to Render's `$PORT` through `render.yaml`.

## 2. Render — Python version configuration

- **Provider:** Render
- **Source class:** CURRENT PLATFORM DOCUMENTATION
- **URL:** https://render.com/docs/python-version
- **Use:** Documents `.python-version` as a supported way to select the Python runtime.
- **Implementation consequence:** The prototype pins Python 3.13 rather than relying on a changing platform default.

## 3. Render — first deploy / web services

- **Provider:** Render
- **Source class:** CURRENT PLATFORM DOCUMENTATION
- **URL:** https://render.com/docs/your-first-deploy
- **Use:** Deployment/build/start-command context for Git-backed web services.

## 4. FastAPI — Uvicorn/ASGI server

- **Provider:** FastAPI
- **Source class:** CURRENT FRAMEWORK DOCUMENTATION
- **URL:** https://fastapi.tiangolo.com/deployment/manually/
- **Use:** Supports running the FastAPI application with Uvicorn/ASGI.
- **Implementation consequence:** ASGI keeps a future path open for realtime/WebSocket behavior without moving the simulation domain into the framework.

## Repository implementation record

- `resources/research/080_web_transport_selection.md`
- `src/apollo_mission_control/web_app.py`
- `web/index.html`
- `requirements.txt`
- `.python-version`
- `render.yaml`
- `tests/test_web_app.py`

## Architectural limitation

The first transport deliberately keeps the authoritative session **in process memory** and uses one Uvicorn process/worker.

This is acceptable for workflow validation but is not a durable production architecture:

- process restart/deploy loses the active session;
- multiple workers would create divergent in-memory authoritative states;
- free-service spin-down would also lose the session;
- persistent/multi-instance session coordination must be designed before relying on the deployment for durable live games.

## Evidence rule

Platform documentation justifies deployment mechanics, not Apollo behavior. Historical simulation semantics continue to come from the mission-specific research/source catalogs.
