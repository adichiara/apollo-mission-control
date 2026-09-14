# Apollo 13 PC+2 — inverter ground-observation path

Date: 2026-09-13  
Status: **RESOLVED for first-playable ground-observation provenance; exact controller routing/display and selector-position visibility remain unresolved.**

## Question

Research note 115 established how the crew should re-observe the INVERTER caution after transferring from inverter 2 to inverter 1. The remaining station-model question was narrower: **what primary-source electrical quantities were actually telemetered to the ground, and how do they relate to the onboard INVERTER caution?**

## Primary evidence

### Apollo Experience Report — Lunar Module Instrumentation Subsystem

NASA TN D-6845 / MSC-S-294, *Apollo Experience Report — Lunar Module Instrumentation Subsystem* (June 1972), documents the measurement, caution/warning, and telemetry paths used by the LM instrumentation system. The report states that conditioned spacecraft measurements were supplied to the pulse-code-modulation and timing electronics assembly (PCMTEA) for transmission through the communications system to the Manned Space Flight Network.

NTRS: https://ntrs.nasa.gov/citations/19720018206  
Public scan: https://www.ibiblio.org/apollo/Documents/19720018206.pdf

Figure 27, **Electrical power subsystem inverter voltage and frequency failure-detection circuit**, directly separates the underlying electrical measurements from the derived caution indication:

- inverter-bus frequency is measurement **`GC0155`**;
- inverter-bus voltage is measurement **`GC0071`**;
- both measurement paths pass through isolation to **Telemetry PCMTEA**;
- the frequency failure-detection limits shown are **greater than 402.0 Hz** and **less than 398.0 Hz**;
- the voltage failure-detection limit shown is **less than 112.0 V ac**;
- the derived electrical-power-system inverter caution is identified as **`GL4046`**, with caution indicator **`6DS26`**;
- the voltage path also feeds the onboard **`4M2` volts indicator**.

The same figure shows the INV 1 / INV 2 / OFF selection feeding the common monitored inverter-bus path. It does **not** show a PCM telemetry output for selector position itself, and it does not show a PCM telemetry tap from the `GL4046` caution relay-driver output.

## What this resolves

There is now direct primary-source support for a ground telemetry path for the two electrical quantities that drive the onboard inverter caution:

```text
selected inverter / inverter bus
        ↓
GC0155 frequency + GC0071 voltage
        ↓
SCEA conditioning / isolation
        ↓
PCMTEA telemetry
        ↓
communications / MSFN
        ↓
[exact MCC station routing/display still unresolved]
```

The onboard caution remains a separate derived indication path:

```text
GC0155 / GC0071 failure-detection logic
        ↓
GL4046 inverter caution
        ↓
6DS26 onboard caution indicator
```

This distinction matters. Ground controllers need not be treated as having no inverter electrical evidence merely because the crew caution is onboard; the source explicitly telemeters inverter-bus frequency and voltage.

## Evidence boundary

This source does **not** establish:

- that the `GL4046` caution state itself was directly telemetered to the ground for Apollo 13;
- that INV 1 versus INV 2 selector position was independently telemetered;
- the exact MSFN/CCATS/RTCC routing from `GC0155` or `GC0071` to TELMU or CONTROL;
- the exact Apollo 13 CRT/MSK page, field, label, or update cadence used by either controller;
- exact ground-display latency;
- the numeric LM-7 inverter-selection caution-inhibit duration;
- exact controller-to-CAPCOM voice wording after a transfer.

Those details remain unresolved and must not be reconstructed by assumption.

## Canonical first-playable interpretation

For first-playable information architecture, a ground-side electrical product may be based on the source-backed inverter-bus measurements `GC0155` and `GC0071`, provided it is clearly represented as a **project rendering of sourced telemetry**, not as a recovered Apollo 13 CRT format.

Do not display a historically styled ground **INVERTER caution light** merely by assuming that `GL4046` was telemetered. Do not infer which inverter is selected from `GC0155`/`GC0071` alone. Until selector-position ground visibility is sourced, the transfer identity remains known through the explicit scenario-authored crew action/report path established in notes 112–115.

The first-playable post-transfer evidence chain can therefore preserve both channels without conflating them:

```text
crew performs sourced inverter transfer
      ↓
onboard caution logic reaches a fresh valid state
      ↓
crew can report whether the INVERTER caution remains

and independently

selected inverter bus → GC0155 / GC0071 → PCMTEA/MSFN → source-backed ground electrical product
```

## Relationship to earlier notes

- Note 112 remains canonical for initial inverter-2 selection.
- Note 113 remains canonical for alternate inverter-1 identity.
- Note 114 remains canonical for the cockpit transfer sequence.
- Note 115 remains canonical for fresh-valid caution re-observation without an invented dwell timer.
- This note resolves the **underlying ground electrical-observation provenance** while deliberately leaving direct caution-discrete routing, selector-position telemetry, exact TELMU/CONTROL display routing, and latency unresolved.
