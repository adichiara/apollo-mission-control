# Progress — FLIGHT/CAPCOM player interaction lab

Date: 2026-09-18

## Completed

- Added a separate site-facing `/player-lab` prototype without replacing the existing `/` validation client.
- Limited the first prototype to FLIGHT and CAPCOM, the two positions whose first-playable workload depends most on coordination/communication rather than dense console reconstruction.
- Reused the authoritative session API for join/rejoin, snapshots, readiness, FLIGHT decision, FLIGHT→CAPCOM approval queue, and CAPCOM transmission.
- Added a persistent modern session strip for original call sign, GET, phase, and session/connection state.
- Added a FLIGHT controller-report stream and kept FLIGHT free of an omniscient subsystem dashboard.
- Added distinct CAPCOM approved/pending, transmitted, and crew-report surfaces.
- Suppressed generic developer/model metadata such as `source_layer` and provenance from the player rendering.
- Omitted the branch-specific CONTROL ΔP solution button and automated shutdown-evidence assessment entirely from this prototype.
- Linked the facilitator console to the interaction lab.
- Added contract tests protecting the lab's scope and scenario-blind/player-facing boundaries.

## Boundary

This is a **playability prototype**, not:

- an exact Apollo FLIGHT or CAPCOM console reconstruction;
- the new canonical player client;
- a change to station authority or scenario behavior;
- evidence that FLIGHT/CAPCOM human play has passed.

The existing `/` client remains the validated integration surface.

## Next

1. Exercise the lab against nominal PC+2 with real FLIGHT/CAPCOM users.
2. Observe whether readiness → FLIGHT disposition → approval → CAPCOM transmission is understandable without facilitator UI explanation.
3. Refine only presentation/interaction defects; do not auto-resolve legitimate operational uncertainty.
4. Add CONTROL and GUIDO scanning prototypes after the FLIGHT/CAPCOM interaction shape is stable.
5. Continue archival/model work in parallel.
