# Roadmap addendum — player/admin separation and facilitator authority

Date: 2026-09-12  
Status: **CURRENT — player/admin UI separation complete; server-side facilitator authority is next**

## Completed

- [x] normal `/` client reduced to station join/rejoin, station products, and station-authorized actions;
- [x] validation/SimSup operations moved to separate `/admin` console;
- [x] manual time, injection, crew-response validation, vehicle response, and audit tools removed from normal player UI;
- [x] `/admin` explicitly labeled as a validation harness rather than a player station;
- [x] regression tests added for player/admin UI separation;
- [x] continuous mission clock and realtime pacing preserved unchanged by the UI split.

## Active priority — server-side facilitator authority

The current UI split is not security. The next implementation should establish a small capability boundary so normal station clients cannot call facilitator/validation operations merely by knowing endpoint paths.

### Minimum protected operation set

Protect at least:

- create/reset session;
- start/pause/resume;
- manual validation GET advancement;
- scenario/source injection;
- explicit crew-response validation operations where these remain facilitator-driven;
- explicit vehicle-response validation operations;
- audit/replay inspection intended for facilitation/validation.

### Preserve controller boundaries

Do **not** turn facilitator authority into a super-controller player role.

Controller operations should remain tied to station identity:

- readiness reports;
- FLIGHT GO/NO-GO;
- CONTROL ground callout/evidence assessment;
- CAPCOM transmission.

Facilitator authority governs session/scenario administration, not hidden omniscient access inside normal controller presentations.

### Keep SimSup distinct where useful

The prototype may initially use one facilitator/admin capability, but architecture should leave room to distinguish:

- ordinary session administration;
- SimSup/scenario injection;
- validation-only direct physical-response controls.

Do not expose those distinctions to players unless future play requires them.

## Deferred

- production account system;
- internet-facing identity management;
- multiple concurrent session ownership;
- persistent facilitator accounts;
- organization/team permissions.

## Success criterion

A player using the normal client can perform only station-authorized operations. Facilitator/validation endpoints reject requests without the required server-side capability, while the `/admin` console can supply that capability and operate the same authoritative continuous-time session.
