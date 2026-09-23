# Station research status — Apollo 11 PDI ullage mass recovery

Date: 2026-09-23

## CONTROL / GUIDANCE / FIDO

**Status: improved primary mass boundary.** Apollo 11 Mission Report Supplement 5, Table VIII explicitly records **33,329 lb** vehicle weight for the **DPS PDI ullage** event at **GET 102:32:57.6**, with an **8.0-s** firing duration.

This supersedes the earlier status that only separation/DOI/landing masses were explicitly available near descent. It does not establish exact DPS-ignition mass, because the primary table identifies the weight with the ullage event rather than ignition.

## Implementation boundary

Use **33,329 lb at PDI ullage** as a mission-specific historical checkpoint. Do not rename it `PDI ignition mass`, and do not subtract inferred RCS consumption without explicit evidence or a separately documented derivation.

All existing FTP-force, delivered thrust/Isp, 69-FM-156, calibration-volume, Supplement 7, and BET Volume II boundaries remain unchanged.

## Evidence status

- PDI-ullage vehicle weight: **DOCUMENTED — PRIMARY APOLLO 11 MISSION REPORT SUPPLEMENT 5, TABLE VIII; 33,329 LB**;
- exact DPS-ignition vehicle weight: **UNRESOLVED**;
- new player-visible station product: **NONE CLAIMED**.