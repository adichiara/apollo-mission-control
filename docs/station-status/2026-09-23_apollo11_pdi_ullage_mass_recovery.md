# Station research status — Apollo 11 PDI ullage mass recovery

Date: 2026-09-23

## CONTROL / GUIDANCE / FIDO

**Status: improved primary mass and timing boundary.** Apollo 11 Mission Report Supplement 5, Table VIII explicitly records **33,329 lb** vehicle weight for the **DPS PDI ullage** event at **GET 102:32:57.6**, with an **8.0-s** firing duration. Table VII independently fixes the adjacent event timing: ullage **102:32:57.6–102:33:05.6** and **DPS PDI maneuver start 102:33:05.2**.

This supersedes the earlier status that only separation/DOI/landing masses were explicitly available near descent and narrows the mass checkpoint to within the actual ignition transition. It does not establish exact DPS-ignition mass, because the primary source associates the 33,329-lb weight with the ullage event and supplies no separate weight at 102:33:05.2.

## Implementation boundary

Use **33,329 lb at PDI ullage** and **102:33:05.2 DPS PDI start** as mission-specific historical checkpoints. Do not rename 33,329 lb `PDI ignition mass`, and do not subtract inferred RCS consumption without explicit evidence or a separately documented derivation.

All existing FTP-force, delivered thrust/Isp, 69-FM-156, calibration-volume, Supplement 7, and BET Volume II boundaries remain unchanged.

## Evidence status

- PDI-ullage vehicle weight: **DOCUMENTED — PRIMARY APOLLO 11 MISSION REPORT SUPPLEMENT 5, TABLE VIII; 33,329 LB**;
- PDI ullage / DPS start timing: **DOCUMENTED — TABLE VII; 102:32:57.6–102:33:05.6 / 102:33:05.2**;
- exact DPS-ignition vehicle weight: **UNRESOLVED**;
- new player-visible station product: **NONE CLAIMED**.