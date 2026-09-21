# Apollo 11 LR downlink-provenance roadmap update

Date: 2026-09-21
Parent: `docs/roadmap/2026-09-20_apollo11_lr_scale_selection.md`

## Newly closed boundary

Flown LUMINARY 099 identifies `DNLRVELX`, `DNLRVELY`, `DNLRVELZ`, and `DNLRALT` as landing-radar downlink storage and explicitly includes them in LM downlink lists. Combined with the Apollo 11 MSK-1137 definition, the supported chain is now:

`LR → LGC processing/storage → explicit LR downlink words → ground processing → controller LR display products`.

This closes the former broad question of whether an Apollo-11-effective LR downlink source family existed. It does not close the ground mapping from those words to individual MSK-1137 fields.

TRW's Apollo-11-specific *Trajectory Reconstruction and Postflight Analysis, Volume 1* now constrains the next layer. Section 7.4 says LR data were obtained by processing **downlink telemetry** with a special-purpose computer program to produce onboard observations for HOPE-compatible analysis. The same section separately identifies an RTCC descent trajectory obtained in real time. This proves a telemetry-derived LR-observation path and cautions against collapsing that path into RTCC trajectory processing. Because the described program is a postflight analysis path, it does not itself establish the real-time MSK-1137 routing.

## Next work

1. Seek Apollo-11-effective **real-time** telemetry/FDS/CCATS/display-database documentation mapping `DNLRVELX/Y/Z/DNLRALT` or their downlink word positions to engineering-unit/display parameter identifiers.
2. Search specifically for the measurement definitions underlying MSK-1137 `VXB/VYB/VZB/RNG`; do not assume RTCC ownership merely because RTCC supplied a real-time descent trajectory.
3. Determine whether MSK-1137 fields are direct engineering conversions of the LGC words or undergo another ground transformation; do not infer the answer from matching semantics alone.
4. Keep sample time, downlink transmission, ground processing, and CRT refresh distinct; do not invent latency/cadence.
5. Keep historical stochastic LR measurement generation **BLOCKED** pending flight-effective residual/distribution evidence.
6. Treat exact SDC gate-edge pulse inclusion as below the current model boundary unless implementation requires it.

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** explicit named LGC LR downlink words for X/Y/Z velocity and altitude.
- **DOCUMENTED, APOLLO-11 CONTROLLER DISPLAY:** LR status, body-axis velocity, and slant range on MSK-1137.
- **DOCUMENTED, APOLLO-11-SPECIFIC POSTFLIGHT:** LR observations were derived from downlink telemetry processing for trajectory analysis.
- **DOCUMENTED, APOLLO-11-SPECIFIC:** the report treats the RTCC real-time descent trajectory separately from the telemetry-derived LR observations.
- **UNRESOLVED:** exact real-time telemetry-word/engineering-conversion/CCATS/FDS/display routing.
- **NOT ESTABLISHED:** an RTCC transform in the MSK-1137 LR measurement path.
- **BLOCKED:** stochastic historical LR error generator.
