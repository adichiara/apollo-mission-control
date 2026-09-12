# Apollo 13 PC+2 — first-pass FLIGHT and CAPCOM presentation boundary

Date: 2026-09-12  
Status: **REVIEWED / IMPLEMENTED-PARTIAL — minimum player-facing decision/communication views defined; readiness-report stream and callout queue remain session-layer work**

## Question

What is the minimum historically defensible FLIGHT and CAPCOM presentation required before shifting the project from station rendering to playable-session integration?

## Primary-source / mission-specific basis

### FLIGHT

The Apollo 13 Mission Operations Report and PC+2 chronology show the Flight Director integrating discipline status and making the final mission decision. The PC+2 state-machine research therefore preserves the distinction:

`station observations/reports → FLIGHT interpretation/decision → CAPCOM crew-facing transmission`

The final GO is not derived automatically from hidden simulator health.

### CAPCOM

The technical air-to-ground record documents CAPCOM as the normal crew-facing Mission Control voice path during the PC+2 interval. CAPCOM:

- transmits the final maneuver PAD;
- manages readback/clarification through changing communications quality;
- transmits procedure/rule information;
- receives crew reports such as throttle and shutdown callouts.

The communication record does not justify giving CAPCOM direct authoritative access to subsystem truth merely to simplify gameplay.

## FLIGHT presentation

The current common projection contains:

- `mission.phase`;
- `flight.go_for_burn`.

`controller.readiness_reports` is still an implementation-deferred field. The first FLIGHT view therefore omits it rather than replacing it with a synthetic consolidated readiness dashboard.

The first FLIGHT rendering is deliberately sparse:

- mission phase / scenario orientation;
- GO-for-burn decision state.

The GO field is a **controller decision product**, not an automatically calculated vehicle-health flag.

## CAPCOM presentation

The current common projection contains:

- air-ground quality;
- final PC+2 maneuver/procedure PAD;
- crew-report stream.

The first CAPCOM view exposes those products only.

A future common session/communication layer may add:

- controller callout queue;
- readiness/GO transmission requests;
- procedural instruction queue;
- explicit readback status.

Those should be session events, not direct reads of hidden subsystem state.

## Deferred

Do not invent for these views:

- a FLIGHT master subsystem-health dashboard;
- an automatic GO/NO-GO computation from authoritative state;
- exact historical FLIGHT console layout;
- exact CAPCOM console layout;
- exact internal voice-loop routing for every callout;
- a CAPCOM subsystem-data dashboard;
- readiness reports before the common session layer models controller-to-FLIGHT reporting.

## Code

- `src/apollo_mission_control/flight_presentation.py`
- `src/apollo_mission_control/capcom_presentation.py`
- `tests/test_flight_capcom_presentations.py`

## Sources

Primary / mission-specific:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, Flight Director and PC+2 controller chronology.
- Apollo 13 Technical Air-to-Ground Voice Transcription, final PC+2 preparation/burn interval.

Repository context:

- `docs/scenarios/APOLLO13_PC2_STATE_MACHINE.md`
- `docs/scenarios/APOLLO13_PC2_PLAYER_PRODUCTS.md`
- `resources/research/052_pc2_controller_product_projection.md`

## Stop condition / project transition

The minimum player-facing station presentation set is now sufficient to stop display expansion for the first slice.

The next project priority is **integrated playable PC+2 session orchestration**:

1. session state / synchronized GET;
2. station assignment and station-view selection;
3. controller-to-FLIGHT readiness reporting;
4. FLIGHT decision events;
5. FLIGHT/CAPCOM callout handoff;
6. CAPCOM-to-crew communication events;
7. authoritative scenario progression and nonnominal branch handling;
8. replay/audit trail.

Further historical/display research should now be demand-driven by an integration or player-decision problem.
