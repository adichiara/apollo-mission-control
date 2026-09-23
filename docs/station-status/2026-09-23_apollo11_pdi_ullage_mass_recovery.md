# Station research status — Apollo 11 PDI ullage mass recovery

Date: 2026-09-23

## CONTROL / GUIDANCE / FIDO

**Status: improved primary mass, timing, and throttle boundary.** Apollo 11 Mission Report Supplement 5, Table VIII explicitly records **33,329 lb** vehicle weight for the **DPS PDI ullage** event at **GET 102:32:57.6**, with an **8.0-s** firing duration. Table VII independently fixes the adjacent event timing: ullage **102:32:57.6–102:33:05.6** and **DPS PDI maneuver start 102:33:05.2**.

The main Apollo 11 Mission Report, MSC-00171 §9.8.1, now adds the mission-specific engine sequence: powered descent began at the **13% minimum throttle setting** and advanced to **full throttle after approximately 26 s**. The report records a roughly **45-s data dropout during this period** and describes the plotted throttle/pressure data as smoothed. It gives powered-descent firing duration as **756.3 s**, versus **757.0 s** for the Supplement 5 Table VII PDI maneuver; both values remain attached to their respective source definitions.

This does not establish exact DPS-ignition mass or Mayer's fixed-throttle-point force. In particular, CONTROL must not convert the report's 13% throttle-setting statement into force by applying a generic rated-thrust value.

## Implementation boundary

Use **33,329 lb at PDI ullage**, **102:33:05.2 DPS PDI start**, and **13% minimum throttle → full throttle at ~+26 s** as mission-specific historical checkpoints. Preserve the telemetry-dropout caveat. Do not rename 33,329 lb `PDI ignition mass`, infer an RCS correction, or treat 13% as an independently calibrated LM-5 force.

All existing exact FTP-force, delivered thrust/Isp, 69-FM-156, calibration-volume, Supplement 7, and BET Volume II boundaries otherwise remain unchanged.

## Evidence status

- PDI-ullage vehicle weight: **DOCUMENTED — PRIMARY APOLLO 11 MISSION REPORT SUPPLEMENT 5, TABLE VIII; 33,329 LB**;
- PDI ullage / DPS start timing: **DOCUMENTED — TABLE VII; 102:32:57.6–102:33:05.6 / 102:33:05.2**;
- powered-descent initial throttle sequence: **DOCUMENTED — PRIMARY MSC-00171 §9.8.1; 13% MINIMUM → FULL AT ~26 S**;
- early-descent telemetry continuity: **DOCUMENTED LIMITATION — ~45-S DATA DROPOUT**;
- exact DPS-ignition vehicle weight: **UNRESOLVED**;
- exact FTP force: **BLOCKED ON DIRECT SOURCE RECOVERY**;
- new player-visible station product: **NONE CLAIMED**.