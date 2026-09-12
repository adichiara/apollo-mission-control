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

The normal `/` interface no longer exposes:

- create/reset;
- start/pause/resume;
- manual GET advancement;
- source injection;
- direct crew-response validation controls;
- direct physical engine-off response;
- audit-log inspection.

It retains only station join/rejoin, station products, and station-authorized actions.

## Admin validation boundary

`/admin` now gathers the development/SimSup operations needed to exercise the complete nonnominal chain independently:

- session lifecycle;
- manual validation time advancement;
- source injection;
- crew receipt/shutdown/report;
- physical DPS response;
- CONTROL shutdown-evidence assessment;
- audit inspection.

## Important limitation

This is **not yet an authorization boundary**. The separate admin UI reduces accidental player exposure but the underlying admin/validation API operations are not yet protected by facilitator credentials.

## Test status

Tests are committed but the full suite remains unverified in this automation environment because there is no runnable checked-out repository available through the GitHub connector.

## Next stopping point

Define and implement the minimum server-side facilitator/admin authority needed to protect lifecycle, manual-time, injection, crew/vehicle validation, and audit operations without conflating facilitator authority with controller station identity.
