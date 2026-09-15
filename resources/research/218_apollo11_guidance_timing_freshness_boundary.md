# Research note 218 — Apollo 11 powered-descent guidance timing / freshness boundary

Date: 2026-09-15  
Status: **PARTIALLY RESOLVED — Mission G MSFN/PFP input and processor cadence are source-backed; inter-source PGNCS/AGS/MSFN freshness remains unresolved and historical execution stays blocked.**

## Question

Can the Apollo 11 powered-descent guidance-monitoring profile now freeze a historical observation-freshness value for the PGNCS/AGS/MSFN velocity comparisons?

## Primary source recovered

NASA Manned Spacecraft Center, Mission Planning and Analysis Division:

**MSC Internal Note 69-FM-36 — _RTCC Requirements for Mission G: MSFN Tracking Data Processor for Powered Flight Lunar Ascent/Descent Navigation_**, 7 February 1969.

Authors:

- W. M. Lear;
- H. G. deVezin Jr.;
- A. D. Wylie;
- E. R. Schiesser.

Historical NTRS document identifier: **19700076511**.

Archived public copy:

- https://web.archive.org/web/20100519200610/http://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19700076511_1970076511.pdf

This is a Mission G requirements document for the MSFN powered-flight tracking-data processor. It is stronger timing evidence than an adjacent-mission technique document, but it must still be read as a processor/interface requirement rather than as an automatically valid controller comparison-freshness rule.

## Source-backed timing evidence

The requirements describe high-speed S-band tracking data supplied at an expected rate of:

- **10 measurements per second**.

For powered-flight navigation processing, the expected measurement-processing interval is:

- **0.2 second**, or
- **0.4 second**.

The report also indicates that slower processing rates such as 0.5 or 0.6 second could require logic revisions.

The processor explicitly time-tags its observation/state products. Its observation time is quantized consistently with the selected 0.2- or 0.4-second processing mode.

The requirements define timing quantities including:

- an interval between usable observations; and
- a constant lag between real time and the current observation time.

The reviewed source establishes the existence and semantics of that real-time lag but does **not** supply a safely recoverable numeric value for the lag in the material extracted for this pass.

## Controller-monitoring relationship

The same requirements family supports the ground powered-flight processor used as the independent MSFN source in the Apollo 11 guidance-monitoring architecture.

Separate Apollo 11 evidence already establishes that Mission Control compared:

1. PGNCS;
2. AGS;
3. MSFN / powered-flight-processor results.

Research notes 204 and 210 remain canonical for the residual fields, limits, and two-out-of-three topology.

The new timing evidence therefore constrains the **MSFN/PFP source production path**. It does not, by itself, define when two or three independently produced controller inputs are sufficiently contemporaneous to be compared.

## Why this does not close `max_time_separation_s`

It would be incorrect to infer:

`PFP processing every 0.2 or 0.4 s → maximum allowed PGNCS/AGS/MSFN time separation = 0.2 or 0.4 s`

Those are different quantities.

The source-backed processor cadence tells us how frequently the ground processor may consume/process tracking measurements and how it time-tags its output. A controller comparison-freshness rule would require evidence about the allowed relative age or synchronization of:

- PGNCS telemetry/navigation state;
- AGS telemetry/navigation state;
- MSFN/PFP-derived state.

No reviewed primary source yet states that allowable inter-source separation.

Therefore the historical profile must retain:

`max_time_separation_s = null`

for every Apollo 11 comparison.

The profile loader must continue refusing to construct an executable historical `GuidanceCrosscheckConfig`.

## Profile consequence

The Apollo 11 historical guidance-monitoring profile may now expose typed timing metadata:

- tracking input rate: **10 Hz**;
- PFP processing interval options: **0.2 s / 0.4 s**;
- PFP observation-time quantization: **0.2 s / 0.4 s**;
- numeric real-time lag: **unresolved**.

This metadata is evidence for source production/cadence only and is explicitly marked as **not a comparison freshness rule**.

## Remaining timing gap

Still required before historical guidance comparison can execute:

1. maximum permissible inter-source observation-time separation / age;
2. exact controller display refresh and cross-source synchronization behavior;
3. numeric PFP real-time lag if it materially affects the controller-visible product;
4. phase/source-pair applicability where the timing rule changes across descent.

If no explicit comparison-freshness rule survives, a future D-022 analysis would still require a fully sourced range for the same timing quantity before demonstrated irrelevance could close the gate.

## Architecture consequence

Preserve these separate concepts:

`tracking measurement cadence`
≠ `PFP processing interval`
≠ `PFP real-time lag`
≠ `controller display refresh`
≠ `inter-source comparison freshness`

This prevents a recovered timing constant from being promoted into a different layer merely because the executable model needs a number.

## Related evidence

- research note 204 — Apollo 11 guidance-monitoring fields and numerical residual limits;
- research note 210 — PGNCS/AGS/MSFN three-source/two-out-of-three topology;
- `data/guidance_monitoring_profiles/apollo11_g_powered_descent_monitoring_partial.json`.
