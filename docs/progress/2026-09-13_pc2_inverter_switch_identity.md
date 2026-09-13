# Progress — PC+2 inverter-switch identity

Date: 2026-09-13  
Status: **RESOLVED FOR FIRST-PLAYABLE IDENTITY; timing/display-routing details remain deferred**

## Completed

- Reopened the exact alternate-inverter identity left unresolved by research notes 059–060.
- Reviewed the LM Operations Handbook electrical-power section and Apollo 13 mission-specific PC+2 checklist read-up before using secondary commentary.
- Confirmed the LM design rule that **inverter 1 is the operating inverter during DPS/APS engine burns**.
- Confirmed Apollo 13 PC+2 preparation checked inverter 2 then inverter 1, temporarily left the inverter-2 feed open, and later closed `CB(16) INVERTER 2` before the burn sequence continued.
- Rechecked the contemporaneous 76:30–76:38 GET rule transmission/readback: the crew was to try switching inverters before treating a continuing inverter light as a shutdown criterion.
- Added research note `111_pc2_inverter_switch_identity.md`.
- Updated the focused inverter source catalog and station/roadmap addenda.

## First-playable decision

Use the following bounded interpretation:

`DPS burn on inverter 1 → inverter light → crew attempts transfer to inverter 2 → light remains → shutdown criterion satisfied`

This is a source-bounded synthesis, not a verbatim recovered Apollo 13 contingency sentence specifying both inverter numbers.

## Still unresolved / not invented

- exact post-warning switch-toggle and breaker chronology;
- a persistence/wait interval after switching;
- exact ground telemetry/display field for the warning;
- whether ground knew the switch state independently of crew procedure/report.

These remain non-blocking unless physical play or a later failure branch requires them.

## Validation status

No physical-play PASS claim is added. Seven-seat nominal, synthetic ΔP, and five-player compact human/device validation remain the primary open validation boundaries.
