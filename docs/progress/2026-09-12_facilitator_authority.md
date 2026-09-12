# Progress — facilitator / SimSup authority

Date: 2026-09-12

## Completed

- Researched the simulation-control role from primary NASA sources before implementation.
- Confirmed that Apollo simulation control/SimSup authority was organizationally distinct from flight-controller stations.
- Added server-side facilitator authorization for exercise-wide operations.
- Added `APOLLO_FACILITATOR_TOKEN` and `X-Apollo-Facilitator` handling.
- Protected create/reset, lifecycle, manual time advancement, injection, validation crew/vehicle operations, and global audit access.
- Left station-authorized controller actions independent from facilitator credentials.
- Updated `/admin` to accept a facilitator token for the current browser tab only.
- Updated `render.yaml` to generate the deployment secret without storing it in source.
- Added `tests/test_facilitator_authority.py`.
- Added research note 088 and `FACILITATOR_AUTHORITY_SOURCES.md`.

## Boundary

The facilitator credential is a modern application-security mechanism. It is **not** presented as an Apollo-era authentication reconstruction.

Historical evidence supports the role separation; modern Render documentation supports the secret-delivery mechanism.

Local development remains permissive when no token is configured. Render fails closed if the token is absent.

## Validation status

The new tests are committed but the full suite is not recorded as executed/passing in this automation environment.

## Next stopping point

Run the full multi-client integration path with one facilitator console and several station clients, validating continuous GET, pause/resume, rejoin, station isolation, and the complete synthetic ΔP branch.