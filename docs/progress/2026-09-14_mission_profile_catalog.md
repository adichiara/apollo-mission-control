# Progress — mission profile catalog

Date: 2026-09-14

## Completed

- Implemented the first reusable mission-era configuration catalog.
- Added a partial Apollo 13 H-2 profile with:
  - AS-508;
  - CSM-109 / LM-7;
  - source-backed TELMU / CONTROL nomenclature;
  - AS-508 MCC/MSFN configuration reference.
- Added a partial Apollo 11 Mission G profile with:
  - AS-506;
  - CSM-107 / LM-5;
  - source-backed TELCOM nomenclature;
  - Mission G RTCC Operations Support Plan reference.
- Linked the PC+2 scenario explicitly to `apollo13_h2`.
- Scenario metadata now carries `mission_profile_id`.
- Session creation resolves and validates the profile against the scenario mission.
- Added `GET /api/mission-profiles`.
- Session status now identifies the active mission profile.
- Added tests for:
  - profile discovery;
  - known Apollo 11 / Apollo 13 nomenclature differences;
  - duplicate/invalid profile rejection;
  - scenario-to-profile linkage;
  - HTTP profile discovery and active-profile status.

## Boundary retained

Mission profiles currently provide configuration identity and provenance only.

They do **not** yet:

- rename or remap runtime station identities;
- change controller authority;
- enable/disable displays;
- inject mission-specific physics constants;
- imply that the two partial profiles are complete mission reconstructions.

That behavior will be generalized only when a second executable scenario establishes which configuration differences genuinely belong in reusable platform code.

## Next

1. Validate this profile boundary through CI.
2. Identify a second reference scenario that stresses materially different mechanisms from PC+2.
3. Use that second runtime to determine the first shared station/configuration interface rather than abstracting further from PC+2 alone.
