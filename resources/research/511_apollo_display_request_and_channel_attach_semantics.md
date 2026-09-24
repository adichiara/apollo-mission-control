# Research Note 511 — Apollo display-request and channel-attach semantics

**Date:** 2026-09-23  
**Status:** REVIEWED-PARTIAL

## Question

What historically supported interaction can the simulator use for controller CRT display selection while exact Apollo 11 GUIDO DRK mapping and Mission-G display routing remain unresolved?

## Primary source

Richard A. Hoover, NASA Johnson Space Center, _Apollo Experience Report: Flight-Control Data Needs, Terminal Display Devices, and Ground System Configuration Requirements_, NASA TN D-7685 / JSC S-396, May 1974.

NASA NTRS record: https://ntrs.nasa.gov/citations/19740015284

## Findings

The Apollo flight-control display architecture deliberately followed a **“display a few parameters at a time with rapid access to all others”** concept. For lunar missions, the computer-driven television system expanded to 36 channels.

NASA TN D-7685 describes two controller access modes:

1. **Display request mode.** An individual console requested a display format. The computer generated/formatted the display, assigned it to the next available computer-driven TV channel, and automatically connected that channel to the requesting console's monitor. Channel assignment was first-come/first-served rather than permanently binding channels to particular displays or consoles.
2. **Channel attach mode.** A console requested an existing TV channel and received whatever data were already on that channel.

When channel saturation caused difficulty obtaining additional critical displays, the system added a display that identified which format occupied each channel and which console had requested it. The flight-control team could then determine which displays should be released.

The report separately identifies **display-system configuration** (including computer-driven TV format layout) and **intercommunication-panel configuration** (access to loops and loop arrangement) as configuration-requirement categories. This reinforces the project's existing rule that display-selection evidence must not be used to infer voice-loop assignment.

## Simulator consequence

The generic Apollo console interaction can now be modeled as **request a display format → system allocates an available TV channel → requested display appears on the console monitor**, with an optional historically supported channel-attach path. A fixed modern one-screen-per-function dashboard is not required by the evidence.

This does **not** establish the exact Apollo 11 GUIDO DRK keys, which formats Bales had preassigned to fast-access keys, which displays he actually called during P63/P64/P66, or the Mission-G request cadence/latency. Those remain open pending mission-specific configuration evidence such as PHO-TN401 or another Mission-G-effective display/keyset record.

The source also means the current open item should be narrowed: **generic display request/routing semantics are documented; Apollo-11-specific GUIDO DRK mapping, display selection, and operational cadence remain unresolved.**

## Evidence status

- **DOCUMENTED / PRIMARY NASA / APOLLO-GENERIC:** display-request mode; automatic assignment to next available computer-driven TV channel; automatic connection to requesting console; first-come/first-served channel allocation.
- **DOCUMENTED / PRIMARY NASA / APOLLO-GENERIC:** channel-attach mode for viewing an already occupied TV channel.
- **DOCUMENTED / PRIMARY NASA / APOLLO-GENERIC:** channel-usage display identifying active format and requesting console when saturation management was required.
- **DOCUMENTED / PRIMARY NASA:** display-system and intercommunication-panel configuration were distinct configuration categories.
- **UNRESOLVED / MISSION-G-SPECIFIC:** GUIDO DRK key mapping, exact powered-descent display callups, station-specific request cadence/latency, and exact display configuration.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection remains the strongest Apollo-11-specific display/control recovery target.
