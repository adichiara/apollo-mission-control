# Apollo 13 PC+2 Update and Sampling Semantics

Status: **implementation contract — historically bounded**

## Purpose

Define how first-slice values move from authoritative state to controller-visible products without inventing unsupported Apollo 13 display refresh rates.

## Timing fields

Every time-varying controller product should support, where applicable:

- `source_time_get` — time represented by the originating physical/onboard state;
- `sample_time_get` — sensor/onboard sampling time;
- `receive_time_get` — time the ground system receives the product;
- `process_time_get` — time a ground-derived product is computed;
- `display_time_get` — time the controller-facing representation is updated;
- `validity` — `valid`, `stale`, `invalid`, or `unavailable`;
- `provenance` — physical/onboard/telemetry/ground-derived/crew-report path.

These fields must remain structurally separate even when the nominal prototype initially sets several timestamps equal.

## Historical evidence boundary

The current PC+2 source package does not establish an exact mission-specific CRT refresh cadence for GUIDO, CONTROL, FIDO/RETRO, TELMU, or INCO products during this interval.

Therefore:

- do not assign a fabricated 1-second or 2-second display refresh rate to PC+2 products;
- do not infer CRT update cadence from unrelated EECOM formats whose one-second updates are documented;
- retain timestamp/age metadata so a later primary source can supply exact cadence without architectural change;
- event-driven crew voice/readback and discrete warnings should remain event-based rather than forced into a common display tick.

## Nominal prototype behavior

Until stronger source evidence is required:

1. The authoritative simulation may advance at a fixed internal integration step chosen for numerical stability.
2. Sensor/onboard values update according to the owning subsystem model.
3. Telemetry products carry explicit sample/receive times and validity.
4. Ground-derived products are recomputed when their required inputs are available/current.
5. Station clients receive changed products through the simulation service; the first prototype does not claim that this transport cadence reproduces historical CRT refresh timing.

This is an implementation convenience, not a historical assertion.

## Product classes

### Continuous/near-continuous engineering quantities

Examples:

- DPS chamber/inlet pressure;
- attitude error and rates;
- electrical current;
- guidance velocity-to-be-gained/residual quantities.

Represent as time-varying products with sample age and validity.

### Discrete/state products

Examples:

- LGC warning;
- program alarm;
- engine-gimbal warning;
- CES DC failure;
- inverter warning;
- communication availability.

Represent as state changes with timestamps. Do not convert them into generic health scores.

### Ground products

Examples:

- PC+2 target solution;
- RTCC trajectory-solution validity;
- post-burn trajectory assessment.

These may have independent computation/update timing and can be stale or wrong even if raw spacecraft data are valid.

### Crew reports

Examples:

- PAD readback;
- thrust report;
- shutdown report;
- residual report.

Treat these as timestamped communication events, not telemetry aliases.

## Staleness policy

Historical staleness thresholds remain unresolved unless a procedure or rule supplies one. The first implementation should therefore expose data age to the product layer but must not invent controller-visible `STALE` thresholds unless source-backed.

## Research stop condition

Do not continue archival searching solely to find exact CRT refresh rates unless one of the following becomes true:

- a PC+2 decision depends on data age;
- a failure scenario specifically requires stale/update-rate behavior;
- a directly accessible primary source is identified that resolves the cadence cheaply.

Otherwise this gap remains documented and non-blocking.
