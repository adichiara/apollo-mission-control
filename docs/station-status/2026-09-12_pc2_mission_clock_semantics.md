# Station status addendum — PC+2 mission-clock / FLIGHT decision gate

Date: 2026-09-12  
Stations affected: **FLIGHT, CAPCOM, all reporting disciplines**  
Maturity change: **none**  
Status: **historical source findings retained; original pause-policy section superseded by D-016**

## Historical result

Primary-source review of the Apollo 13 Flight Control Division *Mission Operations Report* confirms that the final PC+2 readiness/GO and TIG are distinct timed events in GET. The report states that PC+2 ignition time was **not time critical**, but does not provide a numeric allowable delay and does not indicate that GET stopped while controllers deliberated.

Therefore no station is given an invented clock-control authority or timing margin.

## Current simulation boundary

Decision D-016 supersedes the earlier provisional pause-at-gate implementation.

- FLIGHT receives discipline readiness reports rather than hidden consolidated health;
- reaching the final poll opens the `flight_go` decision requirement but does **not** pause GET;
- reporting disciplines may continue to report while mission time advances;
- FLIGHT alone records the GO/NO-GO decision;
- CAPCOM workflow remains downstream of FLIGHT authorization;
- nominal downstream events execute only if their prerequisites exist when their scheduled GET arrives;
- an ineligible nominal event is recorded as missed and is not replayed retroactively after a late decision;
- only an explicit game/session pause normally stops GET.

See `resources/research/084_continuous_mission_clock_architecture.md`.

## Station implications

### FLIGHT

No maturity change. FLIGHT decision authority is explicit, but the controller does not control mission time by withholding a decision.

### CAPCOM

No maturity change. CAPCOM does not clear the decision requirement and receives no new subsystem truth. Crew-facing communication remains separate from the FLIGHT decision.

### CONTROL / GUIDO / TELMU / FIDO-RETRO / INCO

No maturity change. Their reporting and station-information boundaries are unchanged; late reporting may now have operational consequences because GET continues.

## Sources

- NASA Manned Spacecraft Center, Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, NTRS 19710010485.
- `resources/research/081_pc2_mission_clock_and_decision_gate_semantics.md` — source findings plus superseded provisional policy.
- `resources/research/084_continuous_mission_clock_architecture.md` — current implementation architecture.
- `resources/source-catalog/PC2_SESSION_INTEGRATION_SOURCES.md`.

## Current station-facing priority

No additional station-display research is opened by this result. Current work is runnable multi-client integration validation, including continuous GET, rejoin, information isolation, and facilitator/player authority isolation.
