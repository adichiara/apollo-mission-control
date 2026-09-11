# Apollo 13 LM CONTROL Station Specification

Status: **research specification — partial**

Purpose: reconstruct the Apollo 13 Lunar Module CONTROL station from mission-specific operational evidence.

CONTROL is the LM counterpart to CSM GNC for guidance/control/propulsion hardware. It must remain distinct from GUIDO's onboard-computer/navigation role and TELMU's LM electrical/environmental role.

---

## 1. Position

**Call sign / position:** CONTROL  
**Apollo 13 Mission Operations Report:** LM Control Officer

### Documented responsibility

Apollo MCC organizational documentation assigns LM CONTROL responsibility for monitoring and troubleshooting LM:

- guidance/control hardware
- propulsion
- reaction control
- associated vehicle-control systems

Apollo 13 made CONTROL especially important because the LM became the propulsion and attitude-control vehicle for the combined CSM/LM stack.

---

# 2. Premission / pre-accident workload: supercritical helium

Apollo 13 launched with an already-known concern involving the Descent Propulsion System supercritical-helium (SHe) pressure rise.

## 2.1 Prelaunch

CONTROL reported:

- SHe pressure rise rate approximately **8 psi/hr**
- T-10-minute readout approximately **356 psia**

## 2.2 Translunar LM entry decision tree

Because SHe loading had behaved erratically during CDDT, an onboard pressure reading was deliberately obtained during LM entry.

CONTROL had already established explicit branches:

- **660–770 psia:** nominal/acceptable; no further action
- **770–800 psia:** obtain another onboard reading 2–3 hours later
- **>800 psia:** periodically turn on telemetry so ground can calculate an accurate rise rate and extrapolate to PDI
- if predicted SHe pressure at PDI was **≥1800 psia:** proposed short DPS burn followed by SHe venting

The actual onboard reading cycled around **710–720 psia**, corresponding to a nominal rise rate near 6.5 psi/hr.

### Simulation significance

This is nearly an ideal documented controller problem:

```text
measured value
   ↓
compare against explicit thresholds
   ↓
select monitoring/procedure branch
   ↓
project future state
   ↓
recommend intervention only if needed
```

No game-generated warning or hidden scoring is required.

---

# 3. LM activation after the CSM accident

At the CSM anomaly, full LM CONTROL console manning was called for.

When LM telemetry returned:

- LGC and IMU were powered
- crew performed docked alignment
- attitude control initially failed because the ATCA-PGNS circuit breaker had not been closed
- after closure, PGNS attitude control became available

Shortly afterward an RCS thrust-chamber pressure switch failed closed, compromising the caution/warning failed-off indication for that jet.

Again, an indication fault and the physical thruster state were not necessarily the same thing.

---

# 4. MCC-3 / DPS-1

CONTROL supported the first LM descent-engine return-to-free-return burn.

The preparation included:

- DPS pressurization
- Gimbal Drive Actuator (GDA) trim
- PGNS-guided burn setup
- TTCA maneuver to burn attitude
- RCS ullage
- manually throttled DPS profile

The burn was nominal overall, but there was excessive vertical (+X) jet firing because a checklist callout to disable U/V jets via extended verb V65 had not been performed.

### Station information implied

CONTROL needs enough information to monitor:

- DPS pressure/readiness
- GDA trim/state
- thrust level
- RCS jet activity
- attitude/rate behavior
- propellant consumption
- control configuration

---

# 5. RCS conservation and deadband

After MCC-3 the LM was partially powered down.

The LGC/IMU remained operating for attitude control and for the next DPS maneuver.

The normal docked DAP used approximately a ±1.4° deadband and RCS consumption was high—about 1 percent/hour.

Based on simulation runs, the crew was given a software load increasing docked deadband to approximately ±5°.

All +X jets were also disabled because plume-deflector effects reduced their useful thrust and increased propellant consumption.

### Simulation significance

CONTROL workload includes optimization, not merely failure response:

- monitor RCS usage trend
- understand DAP/deadband effects
- alter vehicle-control configuration
- trade pointing performance against consumables

---

# 6. PC+2 / DPS-2 rules

The CONTROL report records mission rules passed to the crew for the major PC+2 DPS burn.

Because the spacecraft was already on a free-return trajectory, shutdown criteria were deliberately tight.

DPS shutdown criteria included:

- insufficient thrust
- engine inlet pressure below limit
- excessive fuel/oxidizer inlet pressure differential
- excessive vehicle rates or attitude errors
- LGC/GDA/CES failures
- ISS warning combined with program alarm

One criterion—fuel/oxidizer inlet differential pressure—was explicitly a **ground callout only**.

This is important for the simulator:

> Some criteria existed only in Mission Control's information/decision path; the crew did not have to independently possess every monitored value.

The burn was executed in PGNS P40 and completed successfully.

CONTROL monitored:

- GDA movement
- attitude error
- rates
- thrust profile
- regulator configuration
- DPS/RCS remaining capability

---

# 7. PTC / attitude-control work after PC+2

Following PC+2, CONTROL attempted to establish passive thermal control while minimizing RCS usage.

The operational record shows several interacting factors:

- PGNS minimum-impulse mode
- docked vehicle geometry
- pitch/roll moment arm
- cross-coupling due to large yaw angle
- FDAI indications
- control-axis strategy
- RCS consumption

This is a useful example of non-failure workload in which understanding vehicle/control geometry matters.

---

# 8. Later contingency maneuver planning

For a planned midcourse burn, CONTROL evaluated:

- whether to use DPS or RCS
- RCS plume-deflector impingement constraints
- DPS minimum-thrust operation
- GDA enable/disable choice
- AGS body-axis reference
- manual TTCA attitude control
- effects of possible GDA mistrim

This shows CONTROL integrating propulsion constraints, control-system configuration, and mission maneuver requirements.

---

# 9. Information families justified by Apollo 13 evidence

## DPS

- SHe pressure and rise rate
- propellant inlet pressures
- fuel/oxidizer differential pressure
- pressurization/regulator state
- thrust level
- remaining ΔV / propellant capability
- GDA position/trim
- engine warnings/status

## LM RCS

- system A/B quantities
- usable quantity
- jet/thruster activity
- thrust-chamber-pressure indications
- jet enable/disable configuration
- plume/impingement constraints
- propellant consumption trend

## Attitude/control

- PGNS/AGS/control mode
- DAP configuration
- deadband
- attitude error
- angular rates
- axis/control authority
- TTCA/manual-control configuration
- FDAI-related control state
- vehicle configuration (docked stack versus LM alone)

## Guidance/control hardware interfaces

- LGC/IMU operational state where relevant to CONTROL
- GDA state/warnings
- CES/control-electronics status
- ATCA/PGNS control availability

These information families do not yet prove which values appeared on which Apollo 13 CRT display.

---

# 10. CONTROL versus GUIDO

## CONTROL

Answers questions such as:

- Can the LM physically control attitude?
- Is DPS/RCS hardware ready and healthy?
- What propulsion/control configuration should be used?
- Are rates, GDA behavior, pressures, and propellant within limits?
- Which hardware/control constraint requires a shutdown or reconfiguration?

## GUIDO

Answers questions such as:

- Is the LGC/CMC navigation state valid?
- Is the guidance platform aligned?
- What guidance program/state is active?
- What targeting/alignment/computer update is required?

Both may care about PGNS/LGC information, but for different reasons.

---

# 11. Implementation status

## DOCUMENTED

- mission-specific CONTROL workload
- SHe monitoring and decision thresholds
- DPS/RCS operational constraints
- DAP/deadband/RCS conservation work
- burn shutdown criteria
- attitude/rate/GDA monitoring
- indication failures and configuration dependencies

## PARTIAL

- information families needed by CONTROL
- interaction with PGNS/AGS and GUIDO

## UNRESOLVED

- exact Apollo 13 CONTROL console layout
- exact CRT display names/numbers
- MSK/DRK configuration
- event/limit indicators
- exact telemetry parameter codes and units for the station
- exact voice loops
- exact command authority from the ground console

---

# 12. Research targets

1. Locate Apollo 13 LM CONTROL CRT/display documentation.
2. Locate H-2 PHO-TR155 Revision C.
3. Search AC/Delco/Grumman mission-support material for LM control display formats.
4. Map DPS and RCS telemetry parameter identifiers.
5. Identify CONTROL console handbook and mission-rule sections.
6. Identify whether historical display sets changed after the CSM accident or only the selected formats/workload changed.

## Primary source

- *Mission Operations Report — Apollo 13*, Appendix H: LM Control Officer (Control), 24 April / 28 April 1970.
