# Apollo 13 PC+2 — inverter re-observation timing boundary

Date: 2026-09-13  
Status: **RESOLVED for first-playable timing semantics; no numeric crew dwell is authorized.**

## Question

Research note 114 recovered the exact inverter-2-to-inverter-1 transfer sequence but left open whether the crew had to wait a specified number of seconds before deciding that the INVERTER caution remained on.

## Primary evidence

### Apollo 13 LM Malfunction Procedures

The mission-specific Apollo 13 *LM Malfunction Procedures* INVERTER caution flowchart gives the alternate-inverter selection and then immediately branches on whether the `INVERTER` caution light is off. No stopwatch interval, count, or other numeric persistence dwell is printed between completing the transfer and evaluating the caution.

For inverter 2 operating, the sourced sequence is:

1. `CB(11) EPS: INV 1 — close`
2. `INVERTER — 1`
3. `CB(16) EPS: INV 2 — open`
4. evaluate `INVERTER lt — off?`

Public scan: https://www.ibiblio.org/apollo/Documents/Apollo%2013%20Malfunction%20Procedures.pdf

### Apollo Experience Report — Lunar Module Instrumentation Subsystem

NASA TN D-6845, *Apollo Experience Report — Lunar Module Instrumentation Subsystem* (1972), documents the inverter caution/monitoring design and the LM-5-and-subsequent inverter-selection transient-inhibit behavior. Apollo 13 LM-7 is within that configuration family.

The important simulation consequence is architectural: the spacecraft caution system itself suppresses the normal switching transient until valid processed inverter data are established. That is different from a crew rule requiring an additional fixed waiting period after the transfer.

NTRS: https://ntrs.nasa.gov/citations/19720018206

## Canonical first-playable interpretation

The inverter criterion should use **valid-state re-observation**, not a fabricated timer:

```text
INVERTER caution on inverter 2
      ↓
crew executes sourced transfer to inverter 1
      ↓
selection transient handled by spacecraft caution/inhibit logic
      ↓
fresh valid INVERTER caution observation
      ↓
light remains → PC+2 shutdown criterion satisfied
light clears   → criterion not satisfied on this evidence
```

The implementation may model the observation as unavailable/transitioning until the selected-inverter caution path is valid. It must not add an arbitrary 1 s, 2 s, 5 s, or other persistence timer merely to make the sequence playable.

## Evidence boundary

This research does **not** recover:

- a numeric inhibit duration for the Apollo 13 PC+2 configuration;
- an exact telemetry sample/display latency for the caution;
- which astronaut performs the transfer;
- exact controller-to-CAPCOM phrasing;
- independent TELMU/CONTROL visibility of selector position;
- the exact ground CRT field or telemetry word used for the inverter warning.

Those details remain unresolved unless a later scenario or physical play exposes a concrete need.

## Relationship to earlier notes

- Note 112 remains canonical for initial inverter 2 selection.
- Note 113 remains canonical for alternate inverter 1 identity.
- Note 114 remains canonical for the cockpit transfer sequence.
- This note closes the remaining **numeric persistence-dwell** question for first-playable semantics by establishing that no crew-specified timer is present in the mission procedure and that normal selection-transient suppression belongs to spacecraft indication logic.
