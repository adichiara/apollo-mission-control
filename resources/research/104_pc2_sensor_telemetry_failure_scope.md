# Research Note 104 — PC+2 sensor / telemetry failure scope

**Date:** 2026-09-13  
**Status:** REVIEWED — first-playable boundary resolved

## Question

Which sensor, instrumentation, telemetry, and data-path failure modes are required for the Apollo 13 PC+2 first playable, and how should later nonnominal cases admit them without inventing generic failures?

This note resolves open question 14 **for the current first playable**. It does not define a universal failure library for all Apollo scenarios.

## Primary sources reviewed

1. **Apollo Experience Report — Lunar Module Instrumentation Subsystem**, David E. O'Brien III and Jared R. Woodfill IV, NASA TN D-6845 / MSC-S-294, June 1972.  
   NTRS: https://ntrs.nasa.gov/citations/19720018206  
   Accessible scan: https://www.ibiblio.org/apollo/Documents/19720018206.pdf  
   Relevant findings: approximately 250 LM measurements were processed for display, caution/warning, and telemetry; recorded inflight instrumentation problems included broken spacecraft wiring, shifted pressure-transducer data, a shifted water-quantity measurement, and nuisance caution/warning alarms. The report also records preflight pressure-transducer calibration shifts and signal-conditioning interface problems.
2. **Apollo Experience Report — Lunar Module Communications System**, NASA TN D-6974 / MSC-S-324, September 1972.  
   NTRS: https://ntrs.nasa.gov/citations/19720023255  
   Relevant finding: the LM communications system provided separate voice, telemetry, television, ranging, and MSFN/CSM communications functions. A communications-path problem is therefore not automatically a failed spacecraft sensor.
3. **Report of Apollo 13 Review Board, Appendix A — Baseline Data: Apollo 13 Flight Systems and Operations**, June 1970.  
   NTRS: https://ntrs.nasa.gov/citations/19700078804  
   Used with note 103 for the separation of spacecraft instrumentation/telemetry from CCATS/RTCC ground processing.
4. **Apollo 13 Mission Report**, MSC-02680 / NASA-TM-X-66449, September 1970.  
   NTRS: https://ntrs.nasa.gov/citations/19710003598  
   Used for mission-specific PC+2 communications/ranging context already documented in notes 050, 098, and 103.

## Findings

### 1. Real Apollo instrumentation failures were not one generic failure state

NASA TN D-6845 preserves several materially different failure classes:

- **loss/unavailability** — broken wiring could remove a measurement path;
- **bias/shift** — pressure transducers and a water-quantity measurement could shift away from the correct value;
- **warning-path anomaly** — nuisance caution/warning alarms could occur without being equivalent to a confirmed underlying subsystem failure;
- **conditioning/interface problems** — signal-conditioning electronics could create an instrumentation problem distinct from the physical parameter being measured.

A simulator should therefore not represent all of these as a single `telemetry_bad = true` diagnosis.

### 2. Communications/data-path impairment is separate from sensor failure

The LM communications system carried telemetry and ranging as communications functions alongside voice. The PC+2 record also contains changing S-band/link conditions and ranging availability.

Therefore a station product can be absent, delayed/stale, or unavailable because of a communications/ground-data path even when the source sensor itself is healthy. Conversely, a biased transducer can deliver fresh telemetry that is wrong.

The model must preserve:

`physical parameter → sensor/transducer → conditioning/PCM → communications path → ground processing → station product`

Failure or uncertainty at one layer must not silently rewrite another layer.

### 3. The current nominal PC+2 run does not require an added historical sensor failure

No primary source reviewed establishes a PC+2-specific sensor failure that must occur during the selected 77:55-through-post-burn nominal slice. The known weak communications conditions are already represented as communications/ranging availability rather than fabricated sensor failures.

Therefore the nominal first playable should not receive random transducer faults, invented dropouts, or arbitrary noisy telemetry merely to create difficulty.

### 4. The existing synthetic ΔP exercise does not require pretending that a historical transducer failed

The project's 26-psi ΔP branch is explicitly synthetic and is already designed around controller-observable evidence. Nothing in the source record requires that branch to be explained as a failed pressure transducer or telemetry channel.

If the exercise intends a real propulsion imbalance, the observation path should reflect that causal choice. If a future exercise intends an instrumentation fault, that fault must be separately authored and sourced to a plausible mechanism. These are different cases and should not be conflated.

## First-playable failure taxonomy

The current architecture only needs the ability to represent these observation-integrity classes when a scenario explicitly selects one:

1. **UNAVAILABLE** — no current measurement/product reaches the controller.
2. **STALE / delayed** — a previously valid product remains visible or available but is not current because of a data-path/update problem.
3. **BIASED / shifted** — fresh data arrive but the measurement is offset from the underlying physical quantity.
4. **WARNING-ONLY anomaly** — caution/warning indication is anomalous without automatically asserting the monitored physical parameter is out of limits.
5. **GROUND-PRODUCT invalid/qualified** — spacecraft telemetry may be valid while a ground computation/interpretation is bad; note 103 and the documented post-MCC-5 RTCC/AGS processing error already establish this separate layer.

These are **model capabilities**, not permission to inject them randomly.

## Admission rule for later nonnominal variants

A new sensor/telemetry failure enters a scenario only when the scenario has:

- a documented or deliberately synthetic failure mechanism stated explicitly;
- a defined layer where the fault originates;
- a source-supported or explicitly synthetic effect on the observation path;
- a controller decision, diagnosis, communication, or recovery action that depends on that effect.

Do not assign unsupported probabilities, random failure rates, magnitudes, durations, recovery times, correlations, or warning behavior.

## Station consequences

- **CONTROL / TELMU:** pressure, electrical, propulsion, and warning products may be unavailable or misleading without revealing hidden physical truth; the current PC+2 nominal case adds no random faults.
- **GUIDO / FIDO-RETRO:** ground-product quality remains separable from spacecraft telemetry integrity.
- **INCO:** communications, telemetry transport, uplink, and ranging availability are data-path concerns and should not be mislabeled as source-sensor failures.
- **FLIGHT:** receives controller conclusions/status, not an omniscient failure-layer diagnosis.
- **CAPCOM:** crew reports remain an independent evidence channel and may corroborate or contradict telemetry.

## Resolution

Open question 14 is **resolved for the current PC+2 first playable**:

> Do not add a generic or random sensor/telemetry-failure mechanic. The nominal PC+2 run requires no extra historical instrumentation failure. Preserve layered observation integrity so explicitly selected later branches can represent unavailable, stale, biased/shifted, warning-only, communications-path, or ground-product faults at the layer where evidence supports them.

Later scenarios remain free to add specific failures after source review. The model taxonomy is an architectural boundary, not a claim that every listed class occurred during PC+2.
