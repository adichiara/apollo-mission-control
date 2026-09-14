# Apollo 13 PC+2 — inverter telemetry sample/display continuity boundary

Date: 2026-09-14  
Status: **REVIEWED / PARTIALLY RESOLVED — later LM telemetry documentation identifies concrete MSFN sample rates and primary MSK destinations for `GC0071V` and `GC0155F`, but no reviewed Apollo 13 / LM-7 source yet establishes that exact loading for PC+2. Apollo 13 display cadence therefore remains unfrozen.**

## Question

Research note 118 established that Apollo MCC computer-driven TV formats were requested/attached dynamically and that a fixed TELMU/CONTROL TV channel must not be invented.

The next unresolved question is whether surviving primary instrumentation material can narrow the remaining presentation/cadence gap for the two source-backed inverter electrical measurements:

- `GC0071V` — AC/inverter bus voltage;
- `GC0155F` — AC/inverter bus frequency.

## Primary evidence

### LM-10 Instrumentation Packet — telemetry summary

The surviving LM-10 instrumentation packet contains a `LUNAR MODULE TELEMETRY DATA SUMMARY` table with columns for measurement identity, engineering range, MSFN-format sample rates, strip-chart setup, and **Primary MSK number**.

For the two inverter measurements it lists:

| Measurement | Title | Range | MSFN format sample rates | Strip chart | Primary MSK numbers |
|---|---|---|---|---|---|
| `GC0071V` | AC BUS VOLT | 0–120 VRMS | format 1: **1 sample/s**; formats 3, 4, 5: **0.2 sample/s** | LP-1 | 1001, 1002, 1071, 1091, 1127 |
| `GC0155F` | AC BUS FREQ | 380–420 Hz | format 1: **1 sample/s**; formats 3, 4, 5: **0.2 sample/s** | LP-1 | 1001, 1002, 1091, 1127 |

Source: *LM-10 Instrumentation Packet*, Lunar Module Telemetry Data Summary, public archival scan at ibiblio/Virtual AGC: https://www.ibiblio.org/apollo/Documents/LM-10_Instrumentation_Packet.pdf

### LM-7/8/9 Elementary Functional Diagrams — mission-family identity cross-check

The LM-7/8/9 Elementary Functional Diagram measurement index independently identifies:

- `GC0071V` — VOLT INVERTER BUS;
- `GC0155F` — FREQ INVERTER BUS.

That establishes continuity of the measurement identities into Apollo 13's LM-7 vehicle family. It does **not** by itself establish LM-7's exact MSFN format loading, sample cadence, or primary MSK list.

Source: *Lunar Module 7, 8, & 9 Elementary Functional Diagrams*, LED-267-37C, measurement index, public archival scan: https://www.ibiblio.org/apollo/Documents/lm-7%2C8%2C9_elementary_functional_diagrams.pdf

### NASA TN D-6845 — instrumentation architecture cross-check

NASA's Lunar Module Instrumentation Subsystem experience report independently shows both measurements routed through isolation/conversion to PCM telemetry while feeding the inverter failure-detection logic. This remains the primary architecture evidence already used in notes 116–118.

Source: O'Brien and Woodfill, *Apollo Experience Report — Lunar Module Instrumentation Subsystem*, NASA TN D-6845 / MSC-S-294, June 1972, especially figure 27. NTRS: https://ntrs.nasa.gov/citations/19720018206

## Interpretation

This materially narrows, but does not close, the cadence/presentation question.

The later LM-10 packet demonstrates that these exact measurement identifiers were not merely engineering schematic labels. They were operational telemetry products with:

- explicit MSFN-format sampling schedules;
- strip-chart support;
- multiple primary MSK destinations.

It also demonstrates why one universal update rate must not be invented. The same measurement could be sampled at **1 sample/s** in one MSFN format and **0.2 sample/s** in several others.

However, LM-10 was the Apollo 15 lunar module, not Apollo 13 LM-7. The packet therefore cannot establish that Apollo 13 PC+2 used the same format loading, sample schedule, primary MSKs, or controller-selected display.

## First-playable boundary

For Apollo 13 PC+2:

```text
GC0071V / GC0155F
    ↓
source-backed PCM/MSFN telemetry
    ↓
MCC dynamic display capability
    ↓
project-rendered electrical evidence
```

Rules:

- do **not** promote the LM-10 1 Hz or 0.2 Hz values into an Apollo 13 historical display refresh rate;
- do **not** claim MSK 1001/1002/1071/1091/1127 as Apollo 13 PC+2-selected displays without an Apollo 13/LM-7 loading or display source;
- do use the LM-10 table as strong continuity evidence that voltage/frequency were normal operational telemetry products and that sampling depended on MSFN format;
- continue to separate **spacecraft telemetry sample cadence** from **MCC processing/display refresh latency**;
- a project rendering may update on the simulator's own cadence only if labeled as a project presentation rather than a recovered historical CRT timing model.

## What this resolves

The prior broad question, “were these measurements operationally displayable telemetry, or merely schematic signals?” is now better bounded:

> **Later primary LM telemetry documentation explicitly treats `GC0071V` and `GC0155F` as MSFN-sampled measurements with primary MSK destinations.**

It also establishes a concrete architectural warning: **sample rate was format-dependent**.

## What remains unresolved

- Apollo 13 / LM-7 MSFN format loading for `GC0071V` and `GC0155F`;
- Apollo 13 primary MSK destination list for those measurements;
- which display(s), if any, TELMU or CONTROL had selected during PC+2;
- exact Apollo 13 CRT field label/location/precision;
- CRT processing/display refresh cadence and end-to-end latency;
- any Apollo 13 strip-chart use of these parameters during PC+2.

## Next archival target

Prefer, in order:

1. an LM-7 / Apollo 13 instrumentation packet or telemetry-format loading record;
2. Apollo 13 MCC display-format/load documentation tying these IDs to an MSK;
3. controller console logs or configuration records showing an actual PC+2 format selection.

Until one is recovered, the cadence and exact display identity remain **NOT HISTORICALLY FROZEN**.

## Project consequence

No station maturity grade changes and no physical-play PASS claim is added. This research improves provenance and narrows the remaining archival target without changing the current project-rendered inverter evidence behavior.
