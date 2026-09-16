# Research Note 186 — GDA position-feedback signal path

Date: 2026-09-16

## Question

Can primary LM documentation narrow what `GH1313V` and `GH1314V` physically represent, beyond the LM-7/8/9 measurement-index labels recovered in note 185?

## Primary sources

1. **Apollo Operations Handbook, Lunar Module LM 10 and Subsequent, Volume I — Subsystems Data**, figure 2.1-50, *Descent Engine Control Assembly — Trim Control Diagram* (NASA/Grumman; basic date 1 February 1970, change date 15 June 1970).
   - NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/alsj/LM10HandbookVol1.pdf
2. **Lunar Module 7, 8, & 9 Elementary Functional Diagrams**, `LED-267-37C`, measurement index.
   - Public scan: https://www.ibiblio.org/apollo/Documents/lm-7%2C8%2C9_elementary_functional_diagrams.pdf

The later handbook is used only for subsystem signal-path continuity; `LED-267-37C` remains the mission-block authority for LM-7 channel identities.

## Finding

Figure 2.1-50 shows the Gimbal Drive Actuator feeding an **ACTUATOR POSITION FEEDBACK** path into the Descent Engine Control Assembly. The same diagram places the `GH1313V` Pitch GDA Position and `GH1314V` Roll GDA Position measurements at the actuator/feedback side of the trim-control architecture. It separately shows LGC positive/negative trim-error inputs and extend/retract motor commands.

Combined with `LED-267-37C`, this establishes a stronger signal-class boundary:

- `GH1313V` and `GH1314V` are actuator-position feedback measurements associated with the physical GDA position path;
- they are not merely the LGC trim-command discretes (`GH1318X`, `GH1319X`, `GH1343X`, `GH1344X`);
- commanded trim direction and measured actuator position therefore remain distinct state variables in the simulation model.

## What remains unresolved

Neither recovered source supplies the mission-block engineering conversion needed to map the analog channel to signed inches or EXT/RET direction. They also do not define the crew-facing `5.86 / 6.75` trim-number zero/reference or prove a conversion between those numbers and the postflight actuator positions.

Accordingly, do **not** infer:

- voltage-to-inch calibration for `GH1313V`/`GH1314V`;
- which sign of the Mission Report inch values means EXT or RET;
- an exact LM-7 degrees-per-inch calibration;
- a mapping from `5.86 / 6.75` to the Mission Report actuator values.

## Simulation implication

Model GDA state with at least two conceptually separate layers:

1. **command/control** — LGC trim error and extend/retract commands;
2. **physical observation** — GDA actuator-position feedback represented by the GH1313V/GH1314V measurement family.

The four Apollo 13 Mission Report actuator positions can remain the mission-specific physical-state anchors at their published resolution, without inventing a command-to-position calibration.

## Next target

The principal unresolved target remains the T+55 LM-burn deck -> RTCC/RTACF run -> `5.86 / 6.75` lineage. The parallel representation target is now specifically an LM-7 measurement-calibration/PCM definition for `GH1313V` and `GH1314V` that supplies engineering conversion and polarity.