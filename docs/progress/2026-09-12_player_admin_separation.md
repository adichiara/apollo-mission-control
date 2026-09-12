# Progress — player/admin client separation

Date: 2026-09-12

## Completed

- Rechecked the repository stopping point and confirmed notes 085–086 had already completed the HTTP crew-response and shutdown-evidence chain.
- Shifted from additional DPS integration to operational client cleanup.
- Added `web/admin.html` as a dedicated validation/SimSup console.
- Reworked `web/index.html` into a normal player station client.
- Added `/admin` static route in `web_app.py`.
- Added `tests/test_web_client_role_separation.py`.
- Added research note `087_player_admin_client_separation.md`.

## Player client boundary

The normal `/` interface no longer exposes create/reset, lifecycle, manual GET advancement, source injection, direct crew/vehicle validation controls, or audit-log inspection. It retains station join/rejoin, station products, and station-authorized actions.

## Admin validation boundary

`/admin` gathers the development/SimSup operations needed to exercise the nonnominal chain: session lifecycle, manual validation time, source injection, crew receipt/shutdown/report, physical response, evidence assessment, and audit inspection.

## Follow-up authorization — completed

At the time of this UI split, the admin interface was **not yet** an authorization boundary. That limitation has now been resolved by research note **088** and decision **D-017**:

- configured deployments require a separate facilitator credential for exercise-wide operations;
- controller station identity remains independent of facilitator authority;
- Render generates the deployment secret outside source control;
- the `/admin` page sends the facilitator credential in a dedicated HTTP header.

See `docs/progress/2026-09-12_facilitator_authority.md`.

## Test status

Tests are committed but the full suite remains unverified in this automation environment because there is no runnable checked-out repository available through the GitHub connector.

## Current stopping point

Runnable multi-client validation with one facilitator console and several station clients: continuous GET, pause/resume, reload/rejoin, station isolation, facilitator/player authority isolation, and the complete synthetic ΔP branch.
