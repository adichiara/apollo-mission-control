# Apollo 13 PC+2 TELMU Presentation Sources

Status: active source supplement for the first-pass TELMU player-facing presentation.

## 1. Apollo 13 Mission Operations Report

- **Title:** *Mission Operations Report — Apollo 13*
- **Organization:** NASA Manned Spacecraft Center / Flight Control Division
- **Date:** 28 April 1970
- **Source class:** PRIMARY, mission-specific
- **Use:** Establishes PC+2 power-up beginning around 78:12 GET, approximately 38–40 A required to maintain the burn configuration, PC+2 ignition timing, immediate post-burn power-down beginning around 79:34 GET, and the inverter-light shutdown criterion after switching inverters.
- **Presentation consequence:** The 38–40 A value is rendered only as a reference/configuration figure unless a live measured-current path is later modeled.
- **Limitation:** Does not establish the exact TELMU CRT layout or field names for these project products.

## 2. TELMU Apollo 13 Post Mission Report

- **Source class:** PRIMARY, mission-specific controller report
- **Use:** Establishes TELMU responsibility for LM electrical/environmental/consumable systems and the operational importance of current/load and configuration management during the contingency.
- **Presentation consequence:** Supports a configuration-centered TELMU view for the bounded PC+2 slice.
- **Limitation:** Does not provide an exact PC+2 TELMU CRT reconstruction in the currently reviewed material.

## 3. Report of Apollo 13 Review Board — Appendix B

- **Source class:** PRIMARY, postflight investigation
- **Use:** Documents the LM electrical-conservation strategy, retaining guidance capability through the major abort maneuver and reducing power afterward.
- **Presentation consequence:** Supports burn-configuration and post-burn power-down context without inventing a generalized health score.

## 4. Apollo 13 technical air-to-ground / mission commentary

- **Relevant interval:** approximately 76:31–76:37 GET
- **Source class:** PRIMARY, contemporaneous mission communications
- **Use:** Confirms the crew-facing inverter rule: shutdown if the inverter light remains after switching inverters.
- **Presentation consequence:** Inverter warning and inverter-switch action must remain separate products/events.

## Repository research

- `resources/research/059_pc2_inverter_warning_after_switch.md`
- `resources/research/060_pc2_inverter_contingency_action_report_loop.md`
- `resources/research/075_pc2_telmu_player_presentation_boundary.md`
- `docs/stations/APOLLO13_TELMU.md`

## Evidence rule

The first TELMU interface is an explicitly labeled **project rendering**.

Do not:

- present 38–40 A as live measured telemetry;
- invent an exact TELMU CRT layout;
- expose hidden product-integrity metadata;
- turn deferred measured current into a historical telemetry failure;
- collapse inverter warning, switch action, re-observation, and shutdown-rule result into one status flag.
