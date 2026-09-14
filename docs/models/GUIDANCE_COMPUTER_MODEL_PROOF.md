# Guidance Computer Alarm / Restart Model Proof

Status: **implemented reusable model proof; Apollo 11 domain partial, not historically validated**

## Purpose

Represent the causal state transition:

`program alarm -> alarm indication/code -> optional software restart -> restart-protected recovery state`

without turning the alarm itself into an abort/continue decision.

The implementation is mission-neutral:

`src/apollo_mission_control/guidance_computer_model.py`

## Generic state

- current time;
- active program identity;
- program-alarm indication;
- active alarm code;
- restart count;
- recovery status;
- alarm history.

## Caller-supplied configuration

- alarm-code meanings;
- whether each alarm invokes software restart;
- which programs are restart-protected;
- applicability/provenance.

No Apollo alarm code or program number is embedded in the implementation.

## Important separation

The model does **not** infer:

- whether primary guidance is currently valid;
- whether backup guidance agrees;
- whether trajectory is acceptable;
- whether radar data are valid;
- whether the crew/controller should abort or continue.

Those are separate observations and controller decisions.

## Apollo 11 evidence boundary

For the Apollo 11 powered-descent reference, Grumman LAV-500-940 directly supports:

- 1202: Executive core-set exhaustion;
- 1201: VAC-area exhaustion;
- both enter software restart;
- the alarm code is stored and the program-alarm indication is activated;
- P63/P64 were restart-protected and continued after the Executive overflows.

The Apollo 11 Mission Report supplies the actual alarm chronology.

This evidence supports a **partial** Apollo 11 guidance-computer model profile, not a complete LGC emulator.

## Tests

Synthetic tests verify:

- restart-protected recovery;
- unprotected restart remains explicitly unresolved;
- non-restart alarm behavior;
- accumulated alarm/restart history;
- alarm-indication clearing without erasing history;
- unknown alarms and time reversal are rejected;
- no abort/continue recommendation appears in model output.

## Next dependencies for Apollo 11 descent

- independent PGNS/AGS observation representation;
- landing-radar measurement/update model;
- source-bounded descent trajectory initialization and propulsion;
- controller-visible guidance/alarm product definition;
- sourced GO/abort decision rules.

Only after those exist should an `apollo11_descent_v1` runtime adapter be implemented.
