# Apollo 11 LR downlink-provenance roadmap update

Date: 2026-09-21
Parent: `docs/roadmap/2026-09-20_apollo11_lr_scale_selection.md`

## Newly closed boundary

Flown LUMINARY 099 identifies `DNLRVELX`, `DNLRVELY`, `DNLRVELZ`, and `DNLRALT` as landing-radar downlink storage and explicitly includes them in LM downlink lists. Combined with the Apollo 11 MSK-1137 definition, the supported chain is now:

`LR → LGC processing/storage → explicit LR downlink words → ground processing → controller LR display products`.

This closes the former broad question of whether an Apollo-11-effective LR downlink source family existed. It does not close the ground mapping from those words to individual MSK-1137 fields.

## Next work

1. Seek Apollo-11-effective telemetry/FDS/RTCC/CCATS documentation mapping `DNLRVELX/Y/Z/DNLRALT` or their downlink word positions to engineering-unit/display parameter identifiers.
2. Determine whether MSK-1137 `VXB/VYB/VZB/RNG` are direct engineering conversions of those words or undergo a ground transformation; do not infer the answer from matching semantics alone.
3. Keep sample time, downlink transmission, ground processing, and CRT refresh distinct; do not invent latency/cadence.
4. Keep historical stochastic LR measurement generation **BLOCKED** pending flight-effective residual/distribution evidence.
5. Treat exact SDC gate-edge pulse inclusion as below the current model boundary unless implementation requires it.

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** explicit named LGC LR downlink words for X/Y/Z velocity and altitude.
- **DOCUMENTED, APOLLO-11 CONTROLLER DISPLAY:** LR status, body-axis velocity, and slant range on MSK-1137.
- **UNRESOLVED:** exact telemetry-word/engineering-conversion/CCATS/RTCC/MSK routing.
- **BLOCKED:** stochastic historical LR error generator.
