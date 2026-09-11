# Research Note 024 — Apollo 13 LM-7 Redline Data

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Primary source

**CSM/LM Spacecraft Operational Data Book, Volume II — LM Data Book, Part 2 — LM-6 and Subsequent Launch Mission Rule Redlines, Revision 5**

Document family: SNA-8-D-027(II)PT2  
Revision date: **March 9, 1970**  
Apollo 13 LM: **LM-7**

Public scan:
https://www.ibiblio.org/apollo/Documents/HSI-41196.pdf

## Scope caution

This source is specifically a **launch mission rule redline** support book.

Its purpose is to provide:

- mandatory prelaunch measurements;
- launch redline values;
- backup values;
- supporting rationale;
- measurement accuracy/range;
- configuration-dependent limits.

Therefore its numeric redlines must **not** be treated automatically as general in-flight operating limits.

It is nevertheless highly valuable for the simulator because it provides mission-era:

- telemetry measurement IDs;
- units/ranges;
- instrumentation accuracy;
- causal rationale;
- backup/cross-check measurements;
- explicit distinction between physical failure and indication failure.

## LM-7 specificity

Revision 5 explicitly incorporated Apollo 13 / LM-7 updates including:

- LM-7 consumable guidelines;
- ECS consumable redlines;
- EPS battery redlines;
- DPS prelaunch redlines;
- APS prelaunch redlines;
- landing-radar antenna-temperature redlines.

This makes the document directly relevant to the Apollo 13 mission profile.

## Example: EPS battery current

The book identifies LM-7 battery-current telemetry including:

- GC/CC 1201 C — Battery 1 current
- GC/CC 1202 C — Battery 2 current
- GC/CC 1203 C — Battery 3 current
- GC/CC 1204 C — Battery 4 current

The exact OCR prefix varies in the scan and must be visually verified before freezing telemetry IDs.

The data sheet explicitly says violation of the total-current redline might indicate:

- instrumentation trouble;
- a short in equipment connected to the bus;
- an inadvertently closed circuit breaker.

### Simulation implication

A redline crossing is evidence to investigate, not an automatic diagnosis.

## Example: LM bus voltage

The book includes:

- GC 0301 V — Commander's Bus voltage
- GC 0302 V — Systems Engineer's Bus voltage

The sheet provides:

- PCM range/accuracy;
- nominal/critical limits;
- rationale tied to equipment voltage requirements;
- backup reasoning.

Again, the launch limits are configuration-specific, but the measurement definitions are useful for TELMU simulation.

## Example: DPS supercritical helium

Apollo 13 / LM-7 specific measurement:

**GQ 3435 P — Pressure, Supercritical Helium Supply Tank**

Documented characteristics include:

- range 0–2000 psia;
- telemetry accuracy context;
- acceptable prelaunch pressure-rise behavior;
- launch redline rationale based on preventing burst-disc pressure from being exceeded before the first DPS burn.

The sheet derives a maximum launch redline of approximately **959 psia**, based on:

- maximum allowable pressure at burn;
- expected coast pressure-rise rate;
- mission duration to first DPS burn;
- measurement error.

### Important distinction

The Apollo 13 CONTROL postflight report later uses different *in-flight* decision thresholds (for example the 660–770 / 770–800 / >800 psia logic during LM entry).

This is a strong example of why:

> one parameter can have different limits depending on mission phase and configuration.

The simulation data model should therefore never attach one universal redline to a telemetry channel.

## Example: RCS indication cross-check

The book explains that some RCS valve/discrete instrumentation could give false indications under certain failure conditions.

For a TCA isolation-valve closure, the actual anomaly could also be inferred by:

- commanding the jet;
- observing lack of thrust-chamber pressure.

The backup indication feeds caution/warning and is telemetered.

### Simulation implication

The same physical state can be inferred through multiple independent signals.

The controller should be able to reason:

```text
valve indication questionable
        +
jet commanded
        +
no chamber pressure
        ↓
evidence supports real valve / thrust failure
```

rather than being handed a resolved subsystem status.

## Redline-book data model fields

This source suggests a useful future parameter-provenance structure:

- measurement ID
- description
- units
- raw/data range
- measurement accuracy
- spacecraft effectivity
- mission phase / configuration
- nominal range
- critical limit
- redline
- caution & warning threshold
- backup measurement/value
- violation consequence
- rationale
- source/page/revision

This is a research-derived structure, not yet an implementation schema.

## Research targets

1. Transcribe all Apollo 13-relevant TELMU and CONTROL channels from the LM-7 redline book.
2. Visually verify OCR-sensitive measurement IDs.
3. Separate:
   - prelaunch redlines;
   - inflight flight-rule limits;
   - caution/warning thresholds;
   - controller-set monitoring limits.
4. Cross-reference measurement IDs against LM instrumentation packets and simulator output tables.
5. Determine which measurements appear on which MCC displays.

## Source

https://www.ibiblio.org/apollo/Documents/HSI-41196.pdf
