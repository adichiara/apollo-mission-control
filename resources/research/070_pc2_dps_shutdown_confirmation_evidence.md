# Apollo 13 PC+2 — DPS shutdown confirmation evidence

Date: 2026-09-12  
Status: **REVIEWED / IMPLEMENTED — evidence channels established; no unsourced binary ground confirmation threshold invented**

## Question

After a crew DPS STOP action and the physical engine-off response, what could Mission Control actually observe to determine that the descent engine had shut down?

## Primary-source findings

### Apollo 13 PC+2 mission operations record

The Apollo 13 Mission Operations Report establishes **thrust chamber pressure** as a ground-observed PC+2 shutdown-rule quantity: 85 psi on the ground, paired with a separate 77-percent onboard thrust criterion.

That proves chamber pressure was part of the ground monitoring path relevant to the maneuver. It does **not** state that 85 psi, zero psi, or any other numeric value was the formal ground definition of “engine off.”

### GQ6510P measurement continuity

Contemporary LM documentation identifies `GQ6510P` as **PRESS, THRUST CHAMBER**. Apollo 10 LM DPS raw-data plots show this measurement rising with ignition/thrust and falling rapidly during shutdown.

This supports using a fresh post-command chamber-pressure observation as **ground evidence about engine response**.

It does not justify importing Apollo 10 shutdown timing, numerical tailoff values, or an engine-off threshold into Apollo 13.

### Actual PC+2 voice sequence

The PC+2 air-ground record includes Commander Lovell reporting “Shutdown,” immediately acknowledged by CAPCOM. This is a mission-specific controller-observable evidence channel independent of ground analog telemetry.

The voice report does not, by itself, prove what exact ground telemetry simultaneously showed, and it should not be collapsed into authoritative physical state.

## Supported evidence model

The minimum defensible controller-observable loop is therefore:

```text
crew STOP action
      ↓
physical DPS response
      ↓
(A) crew voice report: shutdown
(B) fresh post-command GQ6510P chamber-pressure observation, if available
      ↓
controller interpretation
```

The simulator may record whether one or both evidence channels are available.

## What is deliberately not inferred

The project does **not** invent:

- an Apollo 13 controller-visible `ENGINE OFF` discrete;
- a formal GQ6510P pressure threshold meaning “engine off”;
- an exact shutdown-confirmation delay;
- an LM-7 chamber-pressure decay curve;
- a rule that a crew voice report automatically proves physical shutdown;
- a rule that any particular post-command pressure value automatically proves shutdown.

A chamber-pressure observation that predates the STOP/engine-off event cannot serve as confirmation evidence for that event.

## Implementation consequence

Add an evidence aggregator that reports only which independent channels are available:

- `NONE`
- `CREW_REPORTED`
- `GROUND_PRESSURE_OBSERVED`
- `CORROBORATED`

The aggregator carries the post-command pressure value and observation time when present, but does not convert it into a hidden `engine_off_confirmed=True` verdict.

This preserves the project architecture:

`physical response ≠ telemetry evidence ≠ crew report ≠ controller conclusion`

## Sources

Primary / contemporary:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970 — PC+2 shutdown criteria and maneuver chronology.
- Apollo 13 air-ground / mission commentary record for the actual PC+2 cutoff report and CAPCOM acknowledgement.
- Grumman LM elementary-functional-diagram measurement index identifying `GQ6510P` as thrust-chamber pressure.
- Apollo 10 LM DPS raw-data report, NASA NTRS 19690026326, showing `GQ6510P` behavior through ignition and shutdown; used only for measurement-behavior continuity, not Apollo 13 timing or numeric values.

Repository context:

- `resources/research/055_pc2_dps_chamber_pressure_observation_path.md`
- `resources/research/068_pc2_delta_p_ground_callout_shutdown_loop.md`
- `resources/research/069_pc2_dps_shutdown_command_and_physical_response.md`

## Research stop condition

The minimum observable confirmation evidence is sufficiently bounded. Do not pursue an exact engine-off CRT field or pressure threshold unless a later scenario decision requires it.

The next useful step is to integrate this evidence into the shutdown loop, then advance to the next unresolved PC+2 decision dependency rather than reconstructing low-value display details.
