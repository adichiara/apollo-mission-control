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

## 5. Apollo Experience Report — Lunar Module Instrumentation Subsystem

- **Report:** NASA TN D-6845 / MSC-S-294, June 1972
- **Source class:** PRIMARY technical
- **Use:** establishes source-backed inverter-bus frequency `GC0155` and voltage `GC0071` PCMTEA telemetry paths while keeping the derived `GL4046` / `6DS26` onboard caution distinct.
- **Presentation consequence:** TELMU may receive a project-rendered electrical product based on the underlying source-backed voltage/frequency measurements without pretending that the onboard caution itself was directly telemetered.
- **Limitation:** does not establish the exact Apollo 13 TELMU display format, selector position telemetry, or a direct `GL4046` telemetry bit.

## 6. Apollo Experience Report — Flight-Control Data Needs, Terminal Display Devices, and Ground System Configuration Requirements

- **Report:** NASA TN D-7685 / JSC S-396, May 1974
- **NTRS:** https://ntrs.nasa.gov/citations/19740015284
- **Source class:** PRIMARY Apollo-experience / ground-display architecture
- **Use:** documents that an individual console could request a computer-driven TV display format and receive it on the next available dynamically assigned TV channel; consoles could also attach to an already active TV channel.
- **Presentation consequence:** do not fabricate a permanently assigned TELMU TV channel for `GC0155` / `GC0071`. A project rendering can remain source-compatible without reproducing a fixed channel assignment.
- **Limitation:** does not identify the Apollo 13 PC+2 inverter display-format number/name, exact fields, which station selected it, MSK/DRK action, cadence, or latency.

## Repository research

- `resources/research/059_pc2_inverter_warning_after_switch.md`
- `resources/research/060_pc2_inverter_contingency_action_report_loop.md`
- `resources/research/075_pc2_telmu_player_presentation_boundary.md`
- `resources/research/116_pc2_inverter_ground_observation_path.md`
- `resources/research/117_pc2_inverter_direct_caution_selector_telemetry_boundary.md`
- `resources/research/118_pc2_inverter_mcc_display_routing_boundary.md`
- `docs/stations/APOLLO13_TELMU.md`

## Evidence rule

The first TELMU interface is an explicitly labeled **project rendering**.

Do not:

- present 38–40 A as live measured telemetry;
- invent an exact TELMU CRT layout;
- invent a fixed historical TV-channel number or permanent TELMU channel assignment for inverter voltage/frequency;
- expose hidden product-integrity metadata;
- turn deferred measured current into a historical telemetry failure;
- collapse inverter warning, switch action, re-observation, and shutdown-rule result into one status flag.

Source-backed `GC0155` / `GC0071` ground electrical evidence may be rendered for play, but exact Apollo 13 display-format identity, field placement, selection action, cadence, and latency remain unresolved.
