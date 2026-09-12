# 085 — Apollo 13 PC+2 HTTP crew-response integration

Date: 2026-09-12  
Status: **IMPLEMENTED — validation API now reaches explicit physical DPS-off response**

## Question

How should the already-source-bounded crew-response chain be exposed through the first playable HTTP/session interface without turning communication into automatic compliance or inventing a response delay?

## Primary-source check

The implementation boundary was rechecked against the same primary evidence that supports research note 083:

- NASA Flight Control Division Apollo 13 mission-operations material identifies `fuel/oxidizer ΔP >25 psi` as a shutdown criterion based on a **ground call-out**.
- NASA *Apollo 13 Technical Air-To-Ground Voice Transcription* (NTRS 20160014370) records the pre-PC+2 rule briefing in which the differential-pressure item is identified as a ground call and the crew reads back the shutdown-rule relationship.
- Contemporary LM operations documentation supports a crew descent-engine STOP/off-command path and a separate physical engine/valve response.

The sources do **not** supply an exact response latency, verbatim hypothetical exceedance call/readback, unique crewmember assignment, or LM-7 engine-off delay for this branch.

## HTTP integration decision

The transport exposes the existing domain operations directly rather than inventing an automated sequence:

```text
CAPCOM transmit endpoint
        ↓
POST /api/session/crew/receipt/{item_id}
        ↓
POST /api/session/crew/shutdown/{item_id}
        ↓
POST /api/session/admin/vehicle/dps-engine-off
        ↓
separate controller-evidence path
```

### Crew receipt

The receipt endpoint calls `record_crew_receipt(...)` and accepts only an already-transmitted DPS-shutdown callout.

The default response value `received` is **semantic test metadata**, not asserted historical wording.

### Crew shutdown command

The shutdown endpoint calls `command_dps_shutdown_from_callout(...)` and therefore requires a prior recorded receipt. It records the existing operational action `command_dps_shutdown` but does not set the physical engine state to off.

### Physical response

The vehicle endpoint calls `apply_session_engine_off_response(...)` at the synchronized current authoritative GET.

It does not:

- infer a response delay;
- advance time secretly;
- synthesize chamber-pressure decay;
- create controller-visible shutdown confirmation;
- convert the crew command into automatic physical response.

## Realtime-clock interaction

Because the web layer now uses the monotonic realtime session clock, every endpoint first synchronizes authoritative GET. The physical-response endpoint then applies the response at that current GET.

This preserves continuous-time semantics while avoiding an invented fixed delay between crew command and engine response.

For deterministic validation, the retained manual-advance endpoint can still position GET before the response operation.

## Validation

`tests/test_web_crew_response.py` covers:

- shutdown command rejected before crew receipt;
- explicit receipt succeeds after CAPCOM transmission;
- crew command remains a distinct operation;
- physical DPS-off response remains a separate operation;
- physical response is rejected without a prior crew command;
- audit ordering preserves transmission → receipt → command → physical response.

## Historical boundaries retained

This transport work does not add any claim about:

- exact internal Apollo CONTROL/FLIGHT/CAPCOM routing;
- exact crew response wording;
- response latency;
- which crewmember presses STOP;
- chamber-pressure tailoff;
- a binary ground engine-off threshold.

## Next boundary

The next integration step is to expose and exercise the already-modeled **fresh shutdown evidence** architecture from research note 070:

1. an explicit crew shutdown report as one controller-observable channel;
2. a fresh post-command `GQ6510P` chamber-pressure observation as an independent channel;
3. evidence aggregation without converting either channel into an automatic `engine_off_confirmed` verdict.
