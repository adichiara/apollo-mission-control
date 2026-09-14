# Apollo 13 PC+2 — MCC inverter-display routing boundary

Date: 2026-09-14  
Status: **REVIEWED / PARTIALLY RESOLVED — Apollo MCC architecture supports dynamically requested/attached computer-driven TV displays rather than a necessary fixed parameter-to-console channel. Exact Apollo 13 TELMU/CONTROL format identity, field placement, cadence, and latency for `GC0155` / `GC0071` remain unresolved.**

## Question

Research notes 116–117 established that inverter-bus frequency `GC0155` and voltage `GC0071` had PCMTEA/MSFN ground-telemetry paths, while the derived `GL4046` caution and INV1/INV2 selector position were not established as direct telemetry.

The next unresolved question was narrower: does the surviving primary MCC documentation justify assigning those inverter measurements to a fixed historical TELMU or CONTROL display/channel for Apollo 13 PC+2?

## Primary evidence

### NASA TN D-7685 — flight-control data/display architecture

Richard A. Hoover's Apollo experience report describes the Apollo MCC ground display architecture from the flight-control user perspective.

For lunar missions, high-speed telemetry formats reaching the MCC were made available to computer-driven TV displays. The report states that the TV system used two control modes:

- **display request mode** — an individual console requested a display format; the computer generated/formatted it, assigned the next available computer-driven TV channel, and automatically connected that channel to the requesting console;
- **channel attach mode** — a console requested an already active TV channel and received the data on that channel.

The report explicitly describes channel assignment as dynamic rather than permanently consigning channels to particular displays or consoles. It also records 36 computer-driven TV channels for Apollo lunar-landing missions.

Source: Richard A. Hoover, NASA/JSC, *Apollo Experience Report — Flight-Control Data Needs, Terminal Display Devices, and Ground System Configuration Requirements*, NASA TN D-7685 / JSC S-396, May 1974, pp. 4–5 (PDF pages 5–6).

### Apollo 15 MCC Operational Configuration — later-mission architecture cross-check

The Apollo 15 operational-configuration document lists separate **LM TELMU Engineer** and **LM Control Engineer** consoles. This corroborates that those remained distinct controller stations in the post-Apollo-13 MCC configuration.

Because this is a 1971 J-mission configuration, it is used only as a later architectural cross-check. It does **not** establish which Apollo 13 PC+2 display format contained `GC0155` or `GC0071`, nor which controller had that format selected at a particular instant.

Source: Manned Spacecraft Center, *MCC Operational Configuration for Mission J1, AS-510 / SC-112 / LM-10, Apollo 15*, PHO-TR155, 15 April 1971.

## Interpretation

The MCC evidence changes the meaning of the remaining routing gap.

A source-backed spacecraft-to-ground chain exists:

```text
selected inverter bus
    ↓
GC0155 frequency + GC0071 voltage
    ↓
PCMTEA / MSFN
    ↓
MCC telemetry / display-processing capability
```

But the reviewed MCC architecture does **not** require a permanent one-parameter/one-console channel such as:

```text
GC0155 → dedicated TELMU channel
GC0071 → dedicated CONTROL channel
```

Computer-driven TV channels were dynamically assigned to requested formats, and consoles could also attach to channels already in use. Therefore, the missing historical artifact is principally the **Apollo 13 display-format/configuration record** that identifies the relevant format and parameter placement—not proof of a permanently wired TELMU/CONTROL TV channel.

## First-playable boundary

For the current PC+2 first playable:

- do not invent a fixed historical TV-channel number for `GC0155` or `GC0071`;
- do not claim that either measurement was permanently wired to TELMU or CONTROL;
- retain TELMU/CONTROL responsibility and project presentation boundaries already established elsewhere, but label the inverter electrical presentation as a **project rendering** unless an Apollo 13 format source is recovered;
- it is historically compatible for a project rendering to present source-backed inverter voltage/frequency data to the appropriate station without reproducing a specific channel assignment, because Apollo computer-driven TV access was request/attach based;
- do not infer a specific MSK/DRK key, display number, row/column location, update rate, or latency.

## What this resolves

This pass resolves one architectural ambiguity:

> **Exact inverter ground routing should not be modeled as an unknown fixed console channel. Apollo's computer-driven TV system dynamically associated requested display formats with available channels and requesting consoles.**

The first playable therefore does not need to invent a permanent TELMU/CONTROL channel to preserve historical MCC behavior.

## What remains unresolved

- the Apollo 13 display-format number/name containing `GC0155` and/or `GC0071`, if any;
- the exact field labels, row/column placement, engineering-unit rendering, and limit/event treatment;
- which Apollo 13 controller(s) had the relevant format selected during PC+2;
- the precise MSK/DRK request action used for that format;
- parameter update cadence and end-to-end ground/display latency;
- any Staff Support Room presentation of these measurements.

These are archival reconstruction targets, not current first-playable blockers.

## Project consequence

The canonical first-playable interpretation is now:

```text
GC0155 / GC0071 source-backed telemetry
    ↓
MCC dynamic display-format system
    ↓
project-rendered TELMU/CONTROL electrical evidence
```

The final arrow is explicitly a project presentation until an Apollo 13 format/configuration artifact establishes the exact historical display.

No station maturity grade changes and no physical-play PASS claim is added.

## Sources

1. Richard A. Hoover, NASA Lyndon B. Johnson Space Center, *Apollo Experience Report — Flight-Control Data Needs, Terminal Display Devices, and Ground System Configuration Requirements*, NASA TN D-7685 / JSC S-396, May 1974. NTRS: https://ntrs.nasa.gov/citations/19740015284
2. Manned Spacecraft Center, *MCC Operational Configuration for Mission J1, AS-510 / SC-112 / LM-10, Apollo 15*, PHO-TR155, 15 April 1971. Public scan: https://ibiblio.org/apollo/Documents/MCC%20Operational%20Configuration%20Apollo%2015.pdf
