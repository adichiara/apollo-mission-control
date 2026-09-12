# Apollo 13 PC+2 — crew response after a ground shutdown call

Date: 2026-09-12  
Status: **REVIEWED / IMPLEMENTED AT DOMAIN LAYER — explicit receipt, crew command, and physical response remain separate**

## Question

After CAPCOM transmits the source-backed PC+2 ground shutdown call for fuel/oxidizer differential pressure greater than 25 psi, what can the simulation require from the crew without inventing historical timing or cockpit detail?

## Primary-source evidence

### Apollo 13 Mission Operations Report — 28 April 1970

The PC+2 Mission Rules review lists `ΔP fuel/oxidizer greater than 25 psi (based on a ground call-out)` as a maneuver shutdown criterion. The same rules review distinguishes shutdowns caused by listed criteria from an otherwise unexplained premature shutdown that could enter the restart branch.

### Apollo 13 Technical Air-To-Ground Voice Transcription — April 1970

NASA NTRS document **20160014370** preserves the Apollo 13 technical air-ground transcript. During the PC+2 rules briefing at about 76:30 GET, CAPCOM read the >25 psi fuel/oxidizer differential-pressure item as a ground call and told the crew that a listed condition meant shutting the engine down. Fred Haise read the rule back, confirming the operational relationship between the ground call and crew shutdown responsibility.

This establishes a communication/action relationship. It does **not** establish a historical occurrence of this hypothetical exceedance during PC+2.

### Apollo Operations Handbook — Lunar Module

Contemporary LM operations documentation establishes crew STOP control and the descent-engine off-command path. Existing project research note 069 already bounds this layer: a crew STOP/off command is an operational action, while pilot-valve/propellant-shutoff-valve response belongs to the physical vehicle layer.

## Supported minimum chain

```text
CAPCOM transmitted shutdown call
        ↓
explicit crew receipt / acknowledgment event
        ↓
explicit crew DPS shutdown command
        ↓
separate physical DPS engine-off response
        ↓
separate crew report / fresh controller evidence
```

The new integration implements only through physical engine-off response. Confirmation/evidence remains the existing note-070 architecture.

## What is deliberately not invented

The reviewed sources do not establish for this hypothetical ΔP exceedance:

- a crew response delay after the CAPCOM call;
- exact words of the response/readback;
- which crewmember would operate the shutdown control;
- a unique cockpit switch/button choreography beyond the already-supported generic DPS off-command model;
- an LM-7 engine-off response delay;
- a chamber-pressure tailoff curve;
- a binary chamber-pressure value that proves engine shutdown;
- automatic crew compliance merely because CAPCOM transmitted the instruction.

## Implementation decision

A new `crew_response.py` integration layer reuses, rather than replaces, the existing models:

1. `record_crew_receipt(...)` accepts only a transmitted DPS-shutdown CAPCOM item and records a crew communication event at the current authoritative GET.
2. `command_dps_shutdown_from_callout(...)` requires prior receipt and applies the existing `OperationalAction(action="command_dps_shutdown")` model.
3. The operational action sets the crew-command state but does **not** set `engine_running=False`.
4. `apply_session_engine_off_response(...)` reuses `dps_response.apply_engine_off_response(...)` as a distinct vehicle event and requires the caller to provide the response GET.
5. No chamber-pressure observation is synthesized by the physical-response helper.

This preserves the project's source/state → controller product → controller decision → CAPCOM communication → crew response → operational command → physical response → controller evidence layering.

## Synthetic validation

The existing synthetic 26 psi case is retained only as a boundary exercise. It is not an Apollo 13 measurement. New tests verify that:

- CAPCOM transmission alone does not imply crew receipt or shutdown command;
- receipt alone does not command or stop the engine;
- crew shutdown command requires recorded receipt;
- crew shutdown command does not itself stop the physical engine;
- physical engine-off response is explicit and occurs only at a supplied GET;
- audit ordering preserves communication → receipt → command → physical response.

## Sources

Primary:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, PC+2 Mission Rules review.
- NASA, *Apollo 13 Technical Air-To-Ground Voice Transcription*, April 1970, NTRS 20160014370: https://ntrs.nasa.gov/citations/20160014370
- *Apollo Operations Handbook — Lunar Module*, contemporary LM operations documentation; project source details are cataloged in `PC2_DPS_SHUTDOWN_RESPONSE_SOURCES.md`.

Repository context:

- `resources/research/068_pc2_delta_p_ground_callout_shutdown_loop.md`
- `resources/research/069_pc2_dps_shutdown_command_and_physical_response.md`
- `resources/research/070_pc2_dps_shutdown_confirmation_evidence.md`
- `src/apollo_mission_control/operational_actions.py`
- `src/apollo_mission_control/dps_response.py`

## Current stopping point

The domain-layer nonnominal chain now reaches explicit physical engine-off response. The next unresolved integration boundary is to expose the crew-response operations through the HTTP/test harness and then feed the resulting shutdown into the already-modeled controller-evidence path without inventing an automatic confirmation threshold.
