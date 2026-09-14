# Apollo 13 PC+2 — AS-508 telemetry-format / Format 30 boundary

Date: 2026-09-14  
Status: **REVIEWED / PARTIALLY RESOLVED — Apollo 13's mission-specific MCC/MSFN configuration confirms LM-capable high-speed formats and a separate high-rate Format 30 playback path, but does not establish the live PC+2 sampling cadence or controller display identity for `GC0071V` / `GC0155F`.**

## Question

Research note 119 showed that later LM-10 telemetry documentation assigns `GC0071V` and `GC0155F` format-dependent sample rates and primary MSK destinations, while Apollo 13 LM-7/8/9 documentation confirms the measurement identities. The next archival target is Apollo 13's own March 1970 MCC/MSFN mission configuration:

> Does the AS-508 configuration establish a mission-specific live sample/display cadence for the inverter voltage/frequency measurements, or otherwise justify adopting the later LM-10 rates?

## Primary evidence

### AS-508 MCC/MSFN Mission Configuration/System Description — March 1970

Primary source: Manned Spacecraft Center, Flight Support Division, *AS-508 MCC/MSFN Mission Configuration/System Description*, March 1970. NASA NTRS citation 19700024253; archival copies also survive through the Apollo Flight Journal / Apollo Lunar Surface Journal.

The AS-508 utilization matrix identifies multiple 2.4-kb/s transmission formats with LM content, including:

- **Format 4 — LM ONLY**;
- **Format 5 — CSM-LM PCM**;
- **Format 6 — CSM + LM BACKUP**;
- **Format 14 — ASCENT/DESCENT**.

The same document states that remote-site format selection could be changed from MCC by Computer Event Functions (CEFs), with mission-phase applicability defined by the AS-508 utilization matrix.

Most importantly for the current question, section 3.2.2.3 describes **High Speed Format 30** as a distinct capability for **post-pass playback of high-sample-rate CSM/LM analog data**. It could retrieve any of 29 CSM or 21 LM pre-defined subformats. Each subformat could contain:

- four analogs at 50 samples/s;
- four analogs at 10 samples/s;
- seven discretes at 10 samples/s;
- CTE or MET timing.

The subformats were defined premission and selected in real time by CEF at the Telemetry Instrumentation Controllers Console (TICC). Format 30 and the older FM/FM contingency formats were selectable to the same dedicated chart recorder.

## Interpretation

This resolves an important ambiguity created by the high-rate figures.

The 50-s/s and 10-s/s values in AS-508 **must not be interpreted as the normal live PC+2 CRT refresh or routine spacecraft-telemetry sample cadence for `GC0071V` / `GC0155F`**. In the mission-specific Apollo 13 configuration they belong to a separately described **post-pass playback** facility.

AS-508 does establish that:

1. the Apollo 13 ground network had normal LM-capable transmission formats;
2. MCC could alter remote-site format selection;
3. a dedicated high-rate LM analog replay path existed for post-pass analysis;
4. high-rate replay selection was an instrumentation-controller / TICC function, not evidence that TELMU or CONTROL continuously received those parameters at 10 or 50 samples/s.

It does **not** identify `GC0071V` or `GC0155F` inside a specific AS-508 normal format, Format-30 subformat, MSK page, or PC+2 controller selection.

## First-playable boundary

For Apollo 13 PC+2:

```text
LM inverter voltage/frequency telemetry
    ↓
normal LM-capable AS-508 network formats
    ↓
MCC processing / dynamic display capability
    ↓
project-rendered electrical evidence
```

A separate historical path existed for high-rate post-pass replay:

```text
predefined LM Format-30 subformat
    ↓
remote-site stored/high-rate data
    ↓
MCC/TICC CEF selection
    ↓
dedicated chart-recorder playback
```

Rules:

- do **not** use AS-508 Format 30's 50-s/s or 10-s/s rates as a live PC+2 station refresh rate;
- do **not** infer that `GC0071V` / `GC0155F` were members of a particular Format-30 subformat without the missing subformat definition/load record;
- do **not** promote LM-10's 1-s/s / 0.2-s/s schedule into LM-7 merely because AS-508 confirms mission-specific LM-capable network formats;
- preserve normal real-time telemetry, MCC display refresh, and post-pass high-rate playback as three distinct concepts.

## What this resolves

The Apollo 13 mission-specific configuration closes the most dangerous cadence inference:

> **AS-508's 10- and 50-sample/s LM values describe high-speed post-pass playback, not a sourced live PC+2 controller-update rate.**

It also confirms that mission-specific LM-capable formats were part of AS-508's normal network configuration, strengthening the continuity basis for treating inverter voltage/frequency as legitimate ground telemetry without inventing a display cadence.

## What remains unresolved

- exact AS-508 / LM-7 normal-format placement for `GC0071V` and `GC0155F`;
- exact Apollo 13 sample cadence for those measurements during PC+2;
- whether either measurement was included in a Format-30 LM subformat and, if so, which one;
- exact Apollo 13 primary MSK destination(s);
- TELMU/CONTROL selection during PC+2;
- field labels/location/precision;
- CRT refresh and end-to-end latency;
- whether high-rate playback of these measurements was actually requested around PC+2.

## Next archival target

Prefer, in order:

1. AS-508 / LM-7 telemetry-format loading or measurement-assignment tables identifying `GC0071V` / `GC0155F`;
2. the AS-508 Format-30 LM subformat definition/load record;
3. mission-specific MCC display-format/MSK loading tying these IDs to a TELMU/CONTROL product;
4. TICC or controller logs showing actual PC+2 format/replay selections.

Until one is recovered, the exact live cadence and display identity remain **NOT HISTORICALLY FROZEN**.

## Project consequence

No simulation behavior or station maturity grade changes. The current project-rendered inverter electrical evidence remains permissible as source-backed telemetry, but its presentation cadence must remain explicitly project-defined rather than mislabeled as recovered Apollo 13 timing.
