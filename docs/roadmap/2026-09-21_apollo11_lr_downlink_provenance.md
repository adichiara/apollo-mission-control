# Apollo 11 LR downlink-provenance roadmap update

Date: 2026-09-21
Parent: `docs/roadmap/2026-09-20_apollo11_lr_scale_selection.md`

## Newly closed boundary

Flown LUMINARY 099 identifies `DNLRVELX`, `DNLRVELY`, `DNLRVELZ`, and `DNLRALT` as landing-radar downlink storage and explicitly includes them in LM downlink lists. Combined with the Apollo 11 MSK-1137 definition, the supported chain is now:

`LR → LGC processing/storage → explicit LR downlink words → ground processing → controller LR display products`.

This closes the former broad question of whether an Apollo-11-effective LR downlink source family existed. It does not close the ground mapping from those words to individual MSK-1137 fields.

TRW's Apollo-11-specific *Trajectory Reconstruction and Postflight Analysis, Volume 1* constrains the next layer. Section 7.4 says LR data were obtained by processing **downlink telemetry** with a special-purpose computer program to produce onboard observations for HOPE-compatible analysis. The same section separately identifies an RTCC descent trajectory obtained in real time. This proves a telemetry-derived LR-observation path and cautions against collapsing that path into RTCC trajectory processing. Because the described program is a postflight analysis path, it does not itself establish the real-time MSK-1137 routing.

Apollo 11 M-932-69-11 establishes the mission-control framework as distinct CCATS, RTCC, and Display/Control systems. PHO-FAM001 further establishes two real-time display-source classes: Display/Control could receive **selected telemetry data from CCATS**, or display/control data from RTCC. Therefore CRT presentation alone does not prove RTCC ownership of a parameter.

The archival target can now be made more specific. Mission-G RTCC Operations Support Plan 69-FS-2 explicitly lists `PHO-TR155` and `Data Formats` among the reference documents maintained in the RTCC computer-control area. Contemporaneous Philco-Ford quarterly report PHO-TR460 states that the third-floor display system had a final **Mission G configuration**, that Mission-G configuration testing was 100 percent at launch, and that the display system was released from Mission G configuration on 28 July 1969. The same report identifies PHO-TR155 as the operational-configuration documentation family. Later PHO-TR515 explains the configuration-control mechanism: display requirements were gathered through data packs and computer listings were used to prepare PHO-TR155. These sources do not supply the LR parameter mapping themselves, but they identify the mission-specific configuration/data-format records most likely to contain the discriminating evidence.

## Source-recovery gate — 2026-09-21

Archive-focused searches using the display number, Mission-G configuration family, LR field labels, landing-radar terminology, and Data Formats terminology did not recover the parameter-level Mission-G record. The search re-recovered 69-FS-2 and the Apollo 11 AC Electronics manual but no Mission-G PHO-TR155 MSK-1137 parameter package, associated display data pack/computer listing, or Mission-G Data Formats LR table.

Under D-024, the **parameter-level MSK-1137 LR ground route is therefore BLOCKED on named source recovery**. This is not evidence that the records did not exist; the primary configuration-control evidence says they did. It means further broad searching is not the next discriminating step.

Reopen this subquestion when one of the following becomes accessible:

1. Mission-G/Apollo-11-effective PHO-TR155 material covering MSK-1137;
2. the associated MSK-1137 display data pack/computer listing; or
3. Mission-G Data Formats material identifying LR dynamic-data source identifiers/conversions.

The broader Apollo 11 powered-descent/program-alarm reference remains active because it has other current model/runtime dependencies.

## Next work

1. Do **not** continue broad searches for the blocked MSK-1137 mapping absent a source-availability change. Preserve the named recovery targets above.
2. If a target is recovered, trace each dynamic MSK-1137 LR field to its source identifier and source class (CCATS-selected telemetry versus RTCC display/control data), preserving any engineering-unit conversion specified there.
3. Do not use the available Apollo-15 PHO-TR155 as Apollo-11 parameter evidence. It may be used only to understand document structure until a Mission-G record is recovered.
4. Continue the next decision-relevant Apollo 11 powered-descent/program-alarm item that is not dependent on this blocked ground-route mapping.
5. Keep sample time, downlink transmission, ground processing, and CRT refresh distinct; do not invent latency/cadence.
6. Keep historical stochastic LR measurement generation **BLOCKED** pending flight-effective residual/distribution evidence.
7. Treat exact SDC gate-edge pulse inclusion as below the current model boundary unless implementation requires it.

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** explicit named LGC LR downlink words for X/Y/Z velocity and altitude.
- **DOCUMENTED, APOLLO-11 CONTROLLER DISPLAY:** LR status, body-axis velocity, and slant range on MSK-1137.
- **DOCUMENTED, APOLLO-11-SPECIFIC POSTFLIGHT:** LR observations were derived from downlink telemetry processing for trajectory analysis.
- **DOCUMENTED, APOLLO-11-SPECIFIC:** the report treats the RTCC real-time descent trajectory separately from the telemetry-derived LR observations.
- **DOCUMENTED, APOLLO-11 MISSION CONFIGURATION:** MCC used CCATS, RTCC, and Display/Control as distinct cooperating systems.
- **DOCUMENTED, PRIMARY MCC ARCHITECTURE:** Display/Control accepted both selected telemetry from CCATS and display/control data from RTCC.
- **DOCUMENTED, MISSION-G CONFIGURATION CONTROL:** 69-FS-2 names PHO-TR155 and Data Formats as RTCC-area reference documents; PHO-TR460 records final Mission-G display configuration and 100-percent configuration test status at launch.
- **DOCUMENTED, CONFIGURATION PROCESS:** PHO-TR515 describes data packs/computer listings feeding PHO-TR155 display configuration documentation.
- **BLOCKED ON SOURCE RECOVERY:** exact LR engineering conversion, parameter identifiers, and which documented real-time display-source class supplied MSK-1137.
- **NOT ESTABLISHED:** an RTCC transform in the MSK-1137 LR measurement path.
- **BLOCKED:** stochastic historical LR error generator.
