# GDA engineering-unit source catalog

Date: 2026-09-16

## LM-7/8/9 Elementary Functional Diagrams

- Document: `LED-267-37C`, *Lunar Module 7, 8, & 9 Elementary Functional Diagrams*
- Source: https://www.ibiblio.org/apollo/Documents/lm-7%2C8%2C9_elementary_functional_diagrams.pdf
- Source class: primary mission-block engineering documentation

### Supports

`GH1313V` = `VOLT, PITCH GDA POS (RET/EXT)` and `GH1314V` = `VOLT, ROLL GDA POS (EXT/RET)`. Separate LGC extend/retract command discretes establish that position observation and trim command are distinct.

### Boundary

The recovered measurement index does not give the engineering conversion coefficients or signed EXT/RET mapping.

## LM-10 and Subsequent Instrumentation Packet

- Document: *LM-10 and Subsequent Instrumentation Packet*
- Source: https://www.ibiblio.org/apollo/Documents/LM-10_Instrumentation_Packet.pdf
- Source class: primary NASA/Grumman instrumentation documentation; later LM configuration

### Supports

The same measurement family is listed as:

- `GH1313V` — `PITCH GDA POS` — `-6 6 DEG`;
- `GH1314V` — `ROLL GDA POS` — `-6 6 DEG`.

This establishes that the later-LM instrumentation system converted/presented these channels in angular engineering units over a ±6° range.

### Boundary

This is not LM-7 calibration evidence. Do not transfer its numerical conversion coefficients or polarity to Apollo 13, infer the sign of the Mission Report inch values, or equate the channel values with the crew-facing `5.86 / 6.75` trim pair.

## Apollo Operations Handbook, LM 10 and Subsequent

- Relevant item: figure 2.1-50, *Descent Engine Control Assembly — Trim Control Diagram*
- NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/alsj/LM10HandbookVol1.pdf
- Source class: primary subsystem documentation; later configuration used for signal-path continuity

### Supports

Places Pitch/Roll GDA position measurement on the physical actuator-position feedback side of the DECA architecture, separate from LGC trim-error/extend/retract paths.

## Current synthesis

Mission-block evidence fixes channel identity and direction labels; later-LM primary evidence fixes the engineering-unit class as angular and the documented later range as `-6..+6 DEG`. What remains missing is the mission-specific bridge: LM-7 conversion coefficients/polarity and the independent definition of the crew-facing trim-number reference. Until recovered, preserve Apollo 13's postflight actuator-inch summary, GH1313V/GH1314V telemetry family, and `5.86 / 6.75` commanded trim as distinct representations.