# Apollo 13 PC+2 — inverter TELMU indicator continuity boundary

Date: 2026-09-14  
Status: **REVIEWED / PARTIALLY RESOLVED — primary records before and after Apollo 13 show stable inverter-bus measurement identities and later direct TELMU console indicators, but no reviewed source yet establishes the Apollo 13/AS-508 console-09 indicator loading.**

## Question

Research note 120 left the exact Apollo 13 display destination for `GC0071V` and `GC0155F` unresolved. The next archival question is:

> Is there primary configuration evidence tying the inverter-bus voltage/frequency measurements to a specific Mission Control station, without borrowing an unsupported Apollo 15 layout into Apollo 13?

## Primary evidence

### SA-204/LM-1 Data Evaluation Guide — 16 January 1968

The LM-1 data-evaluation guide lists both measurements as explicit ground display/telemetry products:

- `GC0071V` — **VOLT, INVERTER BUS** — display request **5746** — telemetry channel/loading **1022069 15**;
- `GC0155F` — **FREQ, INVERTER BUS** — display request **5771** — telemetry channel/loading **1041069 15**.

This is early LM evidence, not an Apollo 13 configuration record. It establishes that both identifiers were designed as selectable ground display products well before Apollo 13.

### Apollo 15 MCC Operational Configuration — PHO-TR155, 26 March 1971

The Apollo 15 configuration identifies **console 09 as LM TELMU**. In that console's module 05 operational-indicator listing it places:

- indicator 07: `GC0071V * AC BUS V`, equipment source `MOC`, measurement `GC0071`;
- indicator 16: `GC0155F * AC BUS F`, equipment source `MOC`, measurement `GC0155`.

This is the first reviewed primary MCC operational-configuration source that directly ties these two inverter measurements to a named front-room station and physical console indicators.

The same later-mission evidence is consistent with the LM-10 instrumentation packet reviewed in note 119, which retains loading numbers `1022069` for `GC0071V` and `1041069` for `GC0155F` and gives operational MSFN sample schedules/MSKs. The continuity is meaningful, but it does not prove that Apollo 13 used the Apollo 15 module/indicator layout.

## Interpretation

The evidence materially narrows the presentation question:

1. `GC0071V` and `GC0155F` were ground-display telemetry products from at least LM-1 onward.
2. By Apollo 15, both were explicitly presented on **TELMU console 09** as direct operational indicators sourced from MOC.
3. Their spacecraft/ground loading numbers show strong continuity between LM-1 and LM-10 documentation.
4. No reviewed Apollo 13 source yet proves that console 09 module 05 indicators 07/16, display requests 5746/5771, or the Apollo 15 TELMU indicator arrangement were loaded for AS-508.

Therefore **TELMU is now strongly supported as the historical station-family destination for inverter electrical evidence**, but the exact Apollo 13 hardware presentation remains unfrozen.

## First-playable boundary

For the first playable, the source-bounded presentation chain may be described as:

```text
GC0071V inverter-bus voltage + GC0155F inverter-bus frequency
        ↓
PCM/MSFN / MCC processing
        ↓
TELMU electrical-system responsibility
        ↓
project-rendered TELMU electrical evidence
```

The following are **not** historical Apollo 13 facts unless a mission-specific source is recovered:

- console-09 module-05 indicator positions 07 and 16;
- Apollo 15 indicator labels/layout as an AS-508 panel reconstruction;
- LM-1 display-request numbers 5746 / 5771 as Apollo 13 request numbers;
- LM-10 sample rates or MSK destinations as Apollo 13 values;
- a claim that CONTROL directly received either measurement on an equivalent physical indicator;
- a fixed CRT/channel selection inferred from the later TELMU panel.

## What this resolves

The prior broad station-routing uncertainty can be tightened:

> **The project no longer needs to treat TELMU versus CONTROL ownership of inverter-bus electrical evidence as equally unconstrained. Primary Apollo 15 MCC configuration explicitly puts both `GC0071V` and `GC0155F` on TELMU, while earlier LM-1 documentation proves both were already ground-display products.**

This is continuity evidence, not an Apollo 13 layout recovery.

## What remains unresolved

- exact AS-508 / Apollo 13 TELMU operational-indicator loading;
- whether Apollo 13 used the same console/module/indicator positions;
- whether either measurement also appeared on a CRT/MSK used during PC+2;
- exact Apollo 13 normal-format sample cadence;
- exact Apollo 13 display-request/MSK number(s), field precision, refresh, and latency;
- actual PC+2 display/indicator selections and controller use;
- any direct CONTROL presentation of these measurements.

## Next archival target

Prefer, in order:

1. Apollo 13 / AS-508 MCC operational-configuration or MOC console-loading sheets for TELMU console 09;
2. AS-508 display-request / MOC indicator-loading tables containing `GC0071V` or `GC0155F`;
3. Apollo 13 TELMU console logs, controller handbook/checklists, or configuration change records identifying the PC+2 electrical display/indicator set;
4. mission-specific telemetry-format loading sufficient to close live sample cadence.

Until one is recovered, use **TELMU as the source-backed station-family owner**, but keep exact Apollo 13 panel placement and timing explicitly project-defined.

## Project consequence

No station maturity grade or scenario mechanics change. The first playable may continue to expose inverter voltage/frequency evidence to TELMU. This note strengthens the station assignment while preserving the project's rule against copying Apollo 15 console coordinates or LM-10 timing into Apollo 13 without mission-specific support.
