# PC+2 live playtest preflight

Date: 2026-09-13  
Status: **modern validation infrastructure**

Purpose: establish the exact server build and basic deployment health before a physical PC+2 run. This is a project testing procedure, not an Apollo-era operating procedure.

## Before assigning players

1. Open `/api/health` on the dedicated server and confirm `status` is `ok`.
2. Open `/api/build` and copy the returned `commit` into the live-play report's server build/commit field.
3. On Render, the commit is supplied from `RENDER_GIT_COMMIT`; the endpoint does not infer a commit from application state.
4. If the endpoint reports `commit: "unknown"`, do not claim a reproducible server build. Supply `APOLLO_BUILD_COMMIT` for a local/test deployment or record the build manually before using the run as validation evidence.
5. Confirm the facilitator credential works on `/admin` and that a player client cannot use facilitator-only operations.
6. Create/reset the session only after the build identity has been recorded.

## Evidence boundary

Build provenance is intentionally separate from scenario state and controller products. It must never appear as an Apollo station datum, affect event eligibility, or reveal hidden simulation truth.

## CI contract

GitHub Actions launches the same deployment entrypoint used by Render, sets `APOLLO_BUILD_COMMIT` to the workflow commit, calls `/api/build` over real HTTP, and fails if the returned commit does not match. The normal multi-client network smoke then runs against that same server process.
