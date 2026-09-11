# Research Note 019 — Apollo 13 FIDO / RETRO

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Objective

Clarify the operational boundary between the two Apollo 13 flight-dynamics positions.

## Finding

The mission-specific reports support a clean distinction:

### FIDO
Owns the **ground trajectory solution** and its quality.

Questions include:

- Which tracking data are valid?
- Which vector should the RTCC ephemeris use?
- Are discrepancies caused by a real vehicle event or bad data/model state?
- What trajectory/impact/entry geometry follows from the accepted state?

### RETRO
Owns the **return/reentry plan** built on the accepted trajectory.

Questions include:

- Which return option is practical?
- What TIG/ΔV/propulsion system is required?
- When and where will landing occur?
- Is recovery/weather acceptable?
- What entry PAD / flight-path angle / backup plan should be used?

## Apollo 13 evidence

FIDO dealt directly with:

- invalid VAN/TEX tracking;
- vector selection among IU, CMC, high-speed, Select and MSFC sources;
- RTCC ephemeris anchoring/model mistakes;
- tracking glitches;
- communications interference that delayed valid LM tracking;
- final vector selection for entry.

RETRO dealt directly with:

- P37/RTE block data;
- launch/translunar abort return plans;
- free-return restoration;
- direct-return versus flyby/PC+2 options;
- landing-time and recovery-area tradeoffs;
- weather;
- entry PADs and entry flight-path angle;
- separation geometry;
- onboard/ground clock corrections.

## Architecture consequence

These roles should remain separate in the internal simulation model even if a future low-player-count game combines them.

That preserves the real information flow:

```text
tracking / network data
      ↓
RTCC / trajectory processing
      ↓
FIDO: accepted trajectory solution
      ↓
RETRO: return / entry plan
      ↓
GUIDO / GNC / CONTROL / CAPCOM as required
```

## Primary source

Apollo 13 Mission Operations Report, Appendices B and C:
https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
