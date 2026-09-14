# PC+2 observation-failure source supplement

Status: **REVIEWED for first-playable scope boundary**  
Date: 2026-09-13

This supplement records the primary sources used by research note 104 to constrain sensor, telemetry, communications-path, and ground-product failure behavior. It does not assert that every documented Apollo instrumentation anomaly occurred during the Apollo 13 PC+2 interval.

## 1. Apollo Experience Report — Lunar Module Instrumentation Subsystem

- Authors: David E. O'Brien III; Jared R. Woodfill IV
- Report: NASA TN D-6845 / MSC-S-294
- Date: June 1972
- NTRS: https://ntrs.nasa.gov/citations/19720018206
- Accessible scan: https://www.ibiblio.org/apollo/Documents/19720018206.pdf
- Status: **REVIEWED**
- Use in project:
  - establishes the LM instrumentation chain as the source of display, caution/warning, and telemetry measurements;
  - records actual inflight instrumentation problems including broken wiring, shifted pressure-transducer data, a shifted water-quantity measurement, and nuisance caution/warning alarms;
  - records pressure-transducer calibration shifts and signal-conditioning interface problems during development/check-out;
  - supports treating loss, biased/shifted values, and warning-path anomalies as distinct observation-integrity classes.
- Limitation:
  - these Apollo-program examples are not evidence that such faults occurred during the selected PC+2 interval.

## 2. Apollo Experience Report — Lunar Module Communications System

- Report: NASA TN D-6974 / MSC-S-324
- Date: September 1972
- NTRS: https://ntrs.nasa.gov/citations/19720023255
- Status: **REVIEWED-PARTIAL**
- Use in project:
  - establishes voice, telemetry, ranging, television, and MSFN/CSM links as communications-system functions;
  - supports keeping telemetry transport/ranging availability separate from source-sensor health.

## 3. Report of Apollo 13 Review Board, Appendix A — Baseline Data

- Date: June 1970
- NTRS: https://ntrs.nasa.gov/citations/19700078804
- Status: **REVIEWED-PARTIAL for this question**
- Use in project:
  - together with research note 103, establishes CCATS/RTCC as ground-processing layers downstream of spacecraft telemetry;
  - supports a separate ground-product-validity layer rather than treating every bad controller product as bad spacecraft telemetry.

## 4. Apollo 13 Mission Report

- Report: MSC-02680 / NASA-TM-X-66449
- Date: September 1970
- NTRS: https://ntrs.nasa.gov/citations/19710003598
- Status: **REVIEWED-PARTIAL for PC+2 communications context**
- Use in project:
  - mission-specific context for weak-link/S-band/ranging conditions already documented in the PC+2 research chain;
  - supports treating the known PC+2 communications issue as a path-availability concern rather than inventing a sensor failure.

## Implementation boundary supported by this catalog

For the current first playable:

- do not inject random or generic telemetry faults;
- nominal PC+2 requires no additional historical sensor failure;
- preserve explicit layers for source measurement, instrumentation/conditioning, telemetry/communications transport, ground processing, and station presentation;
- admit a nonnominal observation failure only when its origin, observable effect, and controller consequence are sourced or explicitly labeled synthetic;
- do not invent probabilities, durations, biases, noise distributions, recovery timing, or correlations.
