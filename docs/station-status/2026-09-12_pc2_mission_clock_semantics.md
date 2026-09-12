# Station status addendum — PC+2 mission-clock / FLIGHT decision gate

Date: 2026-09-12  
Stations affected: **FLIGHT, CAPCOM, all reporting disciplines**  
Maturity change: **none**

## Historical result

Primary-source review of the Apollo 13 Flight Control Division *Mission Operations Report* confirms that the final PC+2 readiness/GO and TIG are distinct timed events in GET. The same report states that PC+2 ignition time was **not time critical**, but does not provide a numeric allowable delay and does not indicate that GET stopped while controllers deliberated.

Therefore no station is given an invented clock-control authority or timing margin.

## Simulation boundary

The first playable PC+2 session now treats the final FLIGHT GO/NO-GO gate as an explicit **simulation pause**:

- FLIGHT still receives discipline readiness reports rather than hidden consolidated health;
- reaching the gate pauses simulation progression with `pause_reason=decision_gate:flight_go`;
- reporting disciplines may submit readiness while paused;
- FLIGHT alone may clear the gate with GO;
- NO-GO leaves the session paused;
- CAPCOM workflow remains downstream of FLIGHT authorization;
- later source-timed events are not retroactively executed while the gate is unresolved.

This pause is a project playability device. It is not presented as historical Mission Control clock behavior.

## Station implications

### FLIGHT

No maturity change. The implementation now makes the decision authority clearer: the historical GO is represented as an explicit player/controller decision with a bounded simulation hold, not as a hidden automatic state transition.

### CAPCOM

No maturity change. CAPCOM does not clear the gate and does not receive new subsystem truth. Crew-facing communication remains separate from the FLIGHT decision.

### CONTROL / GUIDO / TELMU / FIDO-RETRO / INCO

No maturity change. Their readiness reports can be submitted during the explicit simulation pause; this does not add new display evidence or change their historical product boundaries.

## Sources

- NASA Manned Spacecraft Center, Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, NTRS 19710010485.
- `resources/research/081_pc2_mission_clock_and_decision_gate_semantics.md`
- `resources/source-catalog/PC2_SESSION_INTEGRATION_SOURCES.md`

## Next station-facing work

No further station-display research is opened by this result. The next work remains integration-oriented: browser rejoin persistence, runnable multi-client smoke validation, and then one already-modeled nonnominal branch through the same session/API path.
