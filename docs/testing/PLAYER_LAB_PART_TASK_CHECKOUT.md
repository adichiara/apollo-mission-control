# FLIGHT/CAPCOM player-lab part-task checkout

Date: 2026-09-18  
Status: **READY FOR HUMAN PART-TASK USE**

Purpose: test whether the non-final `/player-lab` coordination workflow is understandable under continuous GET without facilitator explanation of project-internal state.

This is a modern usability/playability checkout, not an Apollo training reconstruction and not a mission-performance score.

## Scope

The checkout tests only:

`controller report → FLIGHT disposition → FLIGHT approval → CAPCOM pending → CAPCOM transmission → crew receipt`

It does not test historical console reconstruction, CONTROL/GUIDO product scanning, a malfunction branch, or mission outcome.

## Setup

- Use the normal authoritative PC+2 session.
- Staff one FLIGHT player and one CAPCOM player.
- A facilitator/test controller may submit one neutral controller readiness report so FLIGHT has information to integrate.
- Keep GET running continuously.
- Do not expose the facilitator/admin client to either player.
- Do not explain internal terms such as `pending_gate`, runtime state names, model provenance, or hidden audit state.
- Do not tell the players which UI element to press after the initial task briefing.
- Confirm the session's playability stream is empty after CREATE/RESET; instrumentation is session-scoped.

## Player brief

Give both players only this task context:

> You are checking the Mission Control coordination interface before a full exercise. FLIGHT receives controller reports and records a disposition. Crew-facing material approved by FLIGHT must pass through CAPCOM. Approval, transmission, and crew receipt are different events. Use the interface and communicate with each other as needed.

Do not describe where those states are displayed.

## FLIGHT tasks

The FLIGHT player should be able to:

1. identify the active original station and current GET;
2. find the controller-report stream;
3. recognize the supplied readiness report;
4. record a GO or NO-GO disposition with a basis;
5. approve the nominal crew-facing continuation item for CAPCOM;
6. explain, in their own words, whether approval means the crew has already received anything.

## CAPCOM tasks

The CAPCOM player should be able to:

1. identify the active original station and current GET;
2. locate the FLIGHT-approved item;
3. recognize that the item is approved but not yet transmitted;
4. deliberately transmit it;
5. recognize the post-transmission state as **awaiting crew receipt** rather than complete;
6. recognize the later **crew received** state after the facilitator records the modeled receipt;
7. explain, in their own words, that transmission and receipt are distinct.

## Facilitator sequence

The facilitator should:

1. create/start the session;
2. allow FLIGHT and CAPCOM to join themselves;
3. provide one neutral readiness report from a test controller through the normal readiness API;
4. allow FLIGHT to make the disposition and queue the nominal item without coaching;
5. allow CAPCOM to transmit without coaching;
6. after CAPCOM has identified the transmitted/awaiting-receipt state, record crew receipt through the supported simulated-crew receipt path;
7. allow CAPCOM to identify the crew-received state;
8. end the part-task checkout.

Do not insert a failure or perform a crew operational action.

## Observation categories

For each task, record:

- **FOUND** — player located the required information/action without facilitator UI help;
- **DELAYED** — player found it but hesitated, searched substantially, or misread another control first;
- **RESCUED** — facilitator had to explain where/how to operate the interface;
- **MISINTERPRETED** — player operated the UI but misunderstood the state or authority boundary.

Also record:

- wrong-station action attempts;
- whether either player interpreted approved as transmitted;
- whether either player interpreted transmitted as received;
- whether either player expected transmission to cause a spacecraft action;
- any developer/internal terminology that required explanation;
- any browser/rejoin problem;
- approximate GET at each major handoff.

## Pass condition for this interface checkpoint

The checkpoint passes when both players can complete the sequence without **RESCUED** or **MISINTERPRETED** events on the approval/transmission/receipt boundary.

A slow or imperfect mission-style decision is not an interface failure if the required information was findable and the player understood the authority/state boundary.

The checkpoint fails if the interface itself causes any of these:

- FLIGHT cannot tell whether an item has merely been approved;
- CAPCOM cannot tell whether an approved item still needs transmission;
- CAPCOM cannot distinguish transmitted from crew received;
- a player believes CAPCOM transmission itself performs the crew action or spacecraft response;
- facilitator explanation of project-internal state is required.

## Instrumentation capture

At the end of the checkout, use the facilitator LOG drawer's **COPY PLAYABILITY LOG** action, or retrieve `/api/session/admin/playability-events`.

Use the event stream to recover:

- page-load → join-success elapsed time;
- automatic-rejoin attempts/outcomes;
- workspace-ready elapsed time;
- action attempts, successes, and errors;
- authoritative GET at each recorded interaction.

Do not infer findability or player competence from elapsed time alone. Pair the event stream with the observer categories below. The playability stream is separate from the authoritative mission audit and contains no free-text decision/readiness basis.

See `docs/testing/PLAYABILITY_INSTRUMENTATION.md`.

## After the checkout

Classify findings using the existing playability distinction:

- **OPERATIONAL_FRICTION** — difficulty belongs to controller judgment/coordination;
- **INTERFACE_FRICTION** — difficulty comes from navigation, labeling, state ambiguity, or client operation.

Only interface-friction findings should drive this prototype before the CONTROL/GUIDO expansion.

See:

- `docs/PLAYER_INTERACTION_PLAYABILITY.md`
- `docs/testing/PC2_LIVE_PLAYTEST_PROTOCOL.md`
- `docs/testing/PC2_LIVE_PLAYTEST_REPORT_TEMPLATE.md`
