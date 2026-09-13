# Station-status addendum — PC+2 inverter-switch identity

Date: 2026-09-13  
Parent: `docs/STATION_RESEARCH_STATUS.md`

Historical station maturity grades remain unchanged. Research note 111 narrows a PC+2 contingency detail without establishing a new exact console display reconstruction.

## TELMU

Maturity remains **B**.

New source-bounded detail:

- normal DPS-burn AC-source identity: **inverter 1**;
- contingency alternate: **inverter 2**;
- the positive shutdown criterion remains a continuing inverter caution/light after the crew has attempted the transfer.

Still unresolved for TELMU presentation:

- exact Apollo 13 CRT/telemetry field used for the inverter caution;
- whether the crew's switch state was independently visible on the ground;
- exact post-switch timing used to judge persistence.

## CONTROL

Maturity remains **B**.

CONTROL may depend on the maneuver shutdown-rule interpretation, but research note 111 does not prove an exact CONTROL-side display or independent switch-state indication. Do not silently give CONTROL telemetry or switch-position knowledge that the sources do not establish.

## CAPCOM

Maturity remains **B**.

The contemporaneous air-ground exchange confirms the crew-facing rule path: a continuing inverter light after trying the redundant inverter is a shutdown condition. CAPCOM transmission/readback is source-backed; automatic crew execution is not.

## FLIGHT

Maturity remains **B**.

FLIGHT may receive the resulting controller recommendation/evidence through the existing decision chain. No new direct inverter instrumentation is assigned to FLIGHT.

## First-playable boundary

The executable/procedural interpretation may now identify the transfer as **inverter 1 → inverter 2**. Exact switch chronology, delay, and ground display routing remain explicitly deferred.
