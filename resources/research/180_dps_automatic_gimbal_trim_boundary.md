# Research Note 180 — DPS automatic gimbal-trim boundary

Date: 2026-09-16

## Question

Can the commanded `5.86 / 6.75` GDA pair for the 61:29 free-return burn be treated as a fixed gimbal state throughout powered flight or as the exact postburn actuator state?

## Primary evidence

### Apollo 13 press kit / mission reference material

NASA's Apollo 13 mission material states that the LM descent engine is gimbaled and that gimbal trim compensates for changing vehicle center of gravity. It further states that this trim is automatically accomplished by either PGNS or AGS.

Primary PDF: https://ntrs.nasa.gov/api/citations/19700076776/downloads/19700076776.pdf

### Apollo 13 flown LM guidance software

The reconstructed listing for the final Apollo 13 LM131 revision includes `TRIM_GIMBAL_CONTROL_SYSTEM.agc`. Its original program comments describe a trim-gimbal control law operating when the descent engine and digital autopilot are on.

Listing: https://ibiblio.org/apollo/listings/LM131R1/TRIM_GIMBAL_CONTROL_SYSTEM.agc.html

This source is useful for system behavior, not for reconstructing the missing ground mass-properties computation.

## Finding

The `5.86 / 6.75` values are supported as commanded/preburn GDA trim values, but they must not be modeled as an invariant physical actuator state through the burn. Apollo 13 documentation explicitly provides for automatic DPS gimbal trim during powered flight as center of gravity changes.

This strengthens the existing evidence boundary around the unrecovered post-61:29 GDA state: the exact postburn actuator angles cannot be inferred simply by carrying the commanded pair forward unchanged.

## What this does not establish

- It does not recover the T+55 mass-properties deck contents.
- It does not connect T+55 directly to `5.86 / 6.75`.
- It does not recover CONTROL's competing numerical trim.
- It does not establish the ground-computation comparison criterion.
- It does not yield the exact automatic gimbal history or final postburn actuator angles.
- It does not prove which individual ground artifact supplied the initial commanded pair.

## Simulation implication

Treat `5.86 / 6.75` as a sourced commanded/preburn trim reference. If powered-flight gimbal motion is represented, it must either be driven by a separately validated guidance/control model or explicitly labeled as synthetic/project behavior. Do not freeze the physical GDA state at the initial commanded values and call that historical telemetry.

## Next archival target

The principal provenance target remains a T+55 generation/load record or downstream RTCC/RTACF LM-burn run/request/output, ideally carrying weight/c.g. and trim values. Separately, a mission telemetry or controller record giving actual GDA positions during/after the 61:29 burn would close the actuator-state branch.