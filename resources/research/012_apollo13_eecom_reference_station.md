# Research Note 012 — Apollo 13 EECOM Reference Station

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Objective

Determine whether one Apollo 13 controller station is documented well enough to become the first high-fidelity reference implementation.

## Conclusion

**CSM EECOM is the strongest current reference station.**

Enough survives to reconstruct the logical station behavior without inventing a generic dashboard:

- official console component diagram;
- two frequently used real-time display formats;
- exact field labels, telemetry identifiers, units, and example values;
- one-second update cadence for those two displays;
- controller-set limit-sense behavior;
- spacecraft-event indication;
- documented use of high-speed telemetry playback after anomalies.

The station is still incomplete because the Apollo 13 DRK, MSK, SMEK, event-panel legends, analog-meter selection, full display catalog, and exact station command authority are not yet fully documented.

## Preserved primary displays

### CSM EPS HIGH DENSITY

Figure B7-8 preserves a dense real-time electrical page containing:

- DC bus and battery voltages;
- AC bus voltages;
- total and individual currents;
- battery/charger currents;
- fuel-cell reactant pressures;
- fuel-cell H2/O2 flows;
- fuel-cell temperatures;
- radiator temperatures;
- fuel-cell load percentages;
- inverter temperatures;
- instrumentation/status values.

The source preserves actual channel/parameter identifiers such as CC0206, CC0207, SC2113, SC2060, SC2139, and SC2084.

### CSM ECS-CRYO TAB

Figure B7-9 preserves a combined environmental/cryogenic page containing:

- cabin/suit pressures;
- O2 manifold pressure and flow;
- cabin/suit temperatures;
- CO2 partial pressure;
- water quantities;
- primary/secondary coolant data;
- O2/H2 cryogenic tank pressure, quantity, temperature, and mass;
- total fuel-cell current.

The page likewise preserves telemetry identifiers and units.

## Limit-sense system

Apollo 13 Review Board Appendix B states:

- EECOM manually set high/low limits;
- controllers normally used tight limits to detect drift early;
- panel 3 contained 72 indicators, including 12 cryogenic pressure/temperature/quantity limit-sense lights;
- a master caution-and-warning event indication existed on panel 9.

The Apollo 13 Review Board later concluded that O2 tank 2 pressure should have triggered a Mission Control limit-sense indication roughly 30 seconds before tank failure, but could not determine whether the light came on and was missed.

This supports a simulator in which a correct signal can exist without being made artificially obvious to the player.

## HSD Format 30

Apollo 13 introduced a high-speed playback capability called Format 30.

AS-508 configuration documentation describes it as:

- 2.4 kbps;
- post-pass playback;
- 29 available CSM subformats and 21 LM subformats;
- per subformat: four analogs at 50 samples/s, four analogs at 10 samples/s, seven discretes at 10 samples/s, plus timing.

The EECOM mission report states that Format 30 was used extensively for O2 tank 2 anomaly playback.

This must remain distinct from the ordinary one-second real-time CRT display path.

## Reconstruction caution

The well-known modern Apollo 13 EECOM console drawing by Andy Anderson is useful as a discovery aid, but Anderson explicitly states that portions of the DRK and limit-light layout were inferred from Apollo 14/15 information.

Those inferred elements are not being adopted into the project as Apollo 13 facts.

## Next research targets

1. AS-508 revision of PHO-TR155 / operational console configuration.
2. Apollo 13 EECOM DRK assignment list.
3. EECOM MSK/SMEK assignments.
4. Event-indicator panel legend.
5. limit-setting procedure.
6. telemetry data dictionary for B7-8/B7-9 field codes.
7. voice-loop selection.
8. complete EECOM display catalog.
9. exact station command authority after communications functions moved toward INCO.

## Sources

- Apollo 13 Review Board, Appendix B: https://ntrs.nasa.gov/citations/19700078726
- Apollo 13 Mission Operations Report: https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
- AS-508 MCC/MSFN Mission Configuration/System Description: https://ntrs.nasa.gov/citations/19700024253
- Apollo 13 Mission Documents index: https://apollojournals.org/afj/ap13fj/a13-documents.html
