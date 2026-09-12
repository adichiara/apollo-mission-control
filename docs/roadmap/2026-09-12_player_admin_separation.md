# Roadmap addendum — player/admin separation and facilitator authority

Date: 2026-09-12  
Status: **COMPLETE FOR FIRST PLAYABLE — UI separation and server-side facilitator authority implemented**

## Completed

- [x] normal `/` client reduced to station join/rejoin, station products, and station-authorized actions;
- [x] validation/SimSup operations moved to separate `/admin` console;
- [x] manual time, injection, crew-response validation, vehicle response, and audit tools removed from normal player UI;
- [x] primary NASA simulation sources reviewed for Simulation Supervisor / simulation-control role separation;
- [x] facilitator authority kept distinct from controller station identity;
- [x] create/reset, lifecycle, manual validation GET, source injection, validation crew/vehicle operations, and audit access protected when a facilitator token is configured;
- [x] `/admin` supplies `X-Apollo-Facilitator` without exposing the credential to normal player UI;
- [x] Render deployment generates `APOLLO_FACILITATOR_TOKEN` outside source control;
- [x] Render fails closed if facilitator authorization is unexpectedly absent;
- [x] regression tests added for UI and authority separation;
- [x] continuous mission clock/realtime pacing preserved unchanged.

## Historical boundary

Primary NASA simulation material places Simulation Supervisor/simulation-control functions outside the flight-controller station organization. That supports the project authority separation.

The HTTP token itself is a modern software mechanism and is not claimed as historical Apollo authentication.

See research note `088_facilitator_authority_boundary.md` and decision D-017.

## Controller boundaries preserved

Facilitator credentials do not grant or replace controller station identity. Readiness reports, FLIGHT decisions, CONTROL operations, CAPCOM transmission, and station-scoped information remain governed by station assignment.

## Deferred

- production account system;
- named/persistent facilitator identities;
- fine-grained facilitator permissions;
- cryptographic player authentication;
- multiple concurrent session ownership;
- organization/team permissions.

## Next milestone

Runnable multi-client integration validation: several player station clients plus one facilitator console against one authoritative continuously running session, including the full synthetic ΔP branch and authority-isolation checks.
