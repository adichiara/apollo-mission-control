# Research Note 018 — Apollo 13 INCO Station

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Objective

Determine what a historically grounded Apollo 13 INCO station must model before visual reconstruction.

## Main finding

INCO’s task is best understood as **communications-system state + network geometry + command-path management**, not as a radio signal-strength display.

Contemporary documentation shows several simultaneous cues:

- digital uplink strength;
- calibrated uplink/downlink meters;
- telemetry dropout;
- voice noise;
- antenna look-angle display;
- spacecraft attitude;
- active network site;
- two-way lock;
- bitrate;
- command subcarrier;
- command margin.

## Apollo 13 display identifier

The Apollo 13 Mission Operations Report explicitly identifies:

**LM Look Angle Display — MSK 1475**

It did not operate when receiving LM low-bit-rate telemetry.

This was known from simulation before Apollo 13 but accepted rather than triggering major RTCC reprogramming.

The problem should therefore be preserved in an Apollo 13 mission profile if MSK 1475 is implemented.

## RTCC dependency

The same report states that manual MED inputs to **CLAD and LAD** had to be made by Computer Dynamics personnel in the RTCC area.

Communications SSR coordinated this on the Dynamics loop, which FIDO also used.

This establishes that the communications display itself could depend on work outside the INCO console.

## PTC command timing

Contemporary Apollo communications documentation describes INCO switching omnidirectional antennas during PTC just before command-uplink capability disappeared.

Telemetry rate, link margin, ground site, voice noise and antenna geometry all contributed to the decision.

Apollo 13 documented a real command failure/retry case involving loss of two-way lock and ground-site handling of the command subcarrier.

## Simulation criticism

INCO’s Apollo 13 postflight report contains unusually direct comments about simulator quality.

It states that incorrectly represented communications dependencies produced **negative training**.

This is a strong validation rule for our scenario engine:

> failure injection must operate through subsystem dependencies, not through independent scripted symptoms.

## Sources

- Apollo 13 Mission Operations Report, Appendix I
- AS-508 MCC/MSFN Mission Configuration/System Description
- Alan Glines and Joseph A. Lazzaro, *Telemetry and Communications to Apollo Flight Controllers*, International Telemetering Conference, 1970; NTRS 19710030221: https://ntrs.nasa.gov/citations/19710030221
- Apollo 13 Technical Air-to-Ground Transcript
