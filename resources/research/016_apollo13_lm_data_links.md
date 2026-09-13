# Research Note 016 — Apollo 13 LM Guidance-Computer Data Links

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Source

**R-567 — Guidance System Operations Plan for Manned LM Earth Orbital and Lunar Missions Using Program LUMINARY 1C (LM131 Rev. 1), Section 2: Data Links, Revision 8**

March 1970.

https://www.ibiblio.org/apollo/NARA-SW/R-567-sec2-rev8.pdf

This is directly mission-specific to Apollo 13's flown LM AGC revision.

## Importance

This document is the first source in the project that gives a detailed mission-specific definition of what an Apollo 13 onboard guidance computer could send to and receive from the ground.

It constrains both:

- the simulated spacecraft/telemetry layer;
- the Mission Control GUIDO/CONTROL information layer.

## Uplink

Ground control could issue LGC inputs through an encoded uplink equivalent to DSKY keyboard characters.

Update functions include:

- Verb 70 — liftoff-time increment;
- Verb 71 — contiguous-block update;
- Verb 72 — scatter update;
- Verb 73 — octal-clock increment.

P27 provided the update-processing context. Independent Apollo GN&CS program documentation identifies **P27 as LGC Update** and **P21 as Ground Track Determination**; P21 must not be labeled as an LGC update program.

The ground could monitor update state through downlinked registers including UPBUFF, UPVERB, UPOLDMOD, COMPNUMB and UPCOUNT.

The document explicitly describes correction behavior after an improperly coded uplink word.

## Downlink families

Program-dependent lists:

- Orbital Maneuvers
- Coast and Align
- Rendezvous and Prethrust
- Descent and Ascent
- Lunar Surface Align
- AGS Initialization and Update

The active program changes which downlist is transmitted.

### Descent/Ascent activation

Used in P12, P63, P64, P66, P68, P70 and P71.

The list contains fields for landing/rendezvous/navigation data, computer/status words, DAP state, body rates, attitude/gimbal quantities, masses, timing and guidance/control channels.

### Lunar Surface Align

Used in P22 and P57.

### AGS Initialization / Update

The list is associated with AGS initialization/update data-link activity, including R47. A previous repository revision incorrectly described this as “Used in P21 and R47” by interpreting the downlist-list selection as a program-title mapping. Because P21 is independently documented as Ground Track Determination, that wording is withdrawn. The exact list-selection condition in R-567 should be cited directly before assigning another major-program number here.

## Snapshot behavior

The GSOP explicitly protects time coherence for certain multiregister arrays by snapshotting selected words before transmission.

This means the downlink itself has timing semantics that should be preserved if rapid changes are ever simulated at that level.

## Important distinction

These are **spacecraft LGC downlink structures**, not Mission Control CRT pages.

The path remains:

```text
LGC downlist
   ↓
spacecraft telemetry
   ↓
MSFN / ground processing
   ↓
RTCC / controller processing
   ↓
selected MCC display format
```

Do not render the raw GSOP downlist directly as the final GUIDO/CONTROL phone screen unless a historical display did so.

## Additional value

The document revision history is unusually useful because it records exactly which telemetry capabilities changed across Luminary versions, including additions involving:

- landing radar raw data;
- jet-control torque;
- desired/actual rates;
- abort/descent data;
- landing-site and target quantities.

This reinforces the need for mission profiles: AGC telemetry genuinely changed mission to mission.

## Next work

- extract exact Apollo 13 ASPO 45 CRT pages;
- map downlist mnemonics to engineering meanings/units;
- determine which fields belonged on GUIDO versus CONTROL displays;
- combine with LM instrumentation telemetry (non-AGC) for CONTROL/TELMU;
- locate the Lunar Module Simulator Console Directory/output tables.

## Sources

- R-567 Section 2, Rev. 8: https://www.ibiblio.org/apollo/NARA-SW/R-567-sec2-rev8.pdf
- *User's Guide to Apollo GN&CS Major Modes and Routines, Colossus 3 and Luminary 1E*, E-2448 Rev. 4, §4.1: identifies LM P21 as Ground-track Determination and LM P27 as an update program: https://www.ibiblio.org/apollo/Documents/j2-80-E-2448-REV4_text.pdf
