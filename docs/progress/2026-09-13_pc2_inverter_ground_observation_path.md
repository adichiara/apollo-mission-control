# Progress — PC+2 inverter ground-observation path

Date: 2026-09-13

## Completed

Primary-source review of NASA TN D-6845 / MSC-S-294, *Apollo Experience Report — Lunar Module Instrumentation Subsystem*, resolved the provenance of the electrical measurements behind the LM INVERTER caution.

Figure 27 explicitly routes inverter-bus frequency **`GC0155`** and inverter-bus voltage **`GC0071`** through isolation to **PCMTEA telemetry**; the report's subsystem description places PCMTEA telemetry on the communications/MSFN path. The same figure identifies the derived onboard inverter caution as **`GL4046` / `6DS26`** and shows frequency limits above 402 Hz or below 398 Hz and a voltage limit below 112 V ac.

## First-playable consequence

TELMU/CONTROL no longer need to treat inverter electrical condition as ground-invisible. A project-rendered ground product may expose source-backed `GC0155`/`GC0071` telemetry with explicit validity/freshness semantics.

The research does **not** prove direct ground telemetry of the `GL4046` caution discrete, INV1/INV2 selector position, exact TELMU/CONTROL CRT routing, exact update/latency, or a numeric selection-inhibit duration. Those remain unresolved and are not invented.

## Repository consistency

Added research note 116 and updated the active inverter source catalog, canonical roadmap/open-question tracking, station research status/addendum, research index, and PR documentation. No new physical-play PASS claim or unsupported executable historical behavior is introduced.
