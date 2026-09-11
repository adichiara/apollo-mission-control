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


## 10A. Cross-mission CRT continuity evidence

Earlier Apollo AC/Delco guidance material identifies two LM CRT pages that align closely with CONTROL's documented workload:

### MSK 1123 — LM guidance/control/propulsion real-time

Documented field families include:

- DAP/body rates
- AGS rate/ASA rates
- commanded attitude
- gimbal/CDU/IMU/AGS attitude
- PGNS/AGS errors
- guidance-system velocity and delta-velocity
- propulsion/control quantities

### MSK 1137 — LM powered-descent/control

Documented fields include:

- throttle select
- manual/automatic/total throttle
- actuator position
- LGC-commanded thrust
- thrust-chamber pressure
- attitude/guidance error
- desired body rates
- engine-induced angular acceleration
- engine-gimbal direction
- attitude-hold/automatic stabilization state
- commanded control torque

Later Apollo telemetry tables map APS/DPS/RCS/radar measurements to these MSKs, strengthening continuity evidence.

However, until the Apollo 13 AC Electronics ASPO 45 section is extracted, the project does **not** claim that Apollo 13 used these pages unchanged.


## 12A. LM-7 mission-era measurement/redline source

The March 9, 1970 LM-7 redline book provides mission-specific measurement definitions and launch constraints for propulsion/control systems.

A particularly useful Apollo 13 measurement is:

**GQ 3435 P — Supercritical Helium Supply Tank Pressure**

The document records:

- range: 0–2000 psia;
- prelaunch rise-rate assumptions;
- launch redline derivation;
- measurement/system rationale.

It derives a maximum launch redline around **959 psia** based on projected pressure at the first DPS burn.

This must not be confused with CONTROL's later in-flight decision branches (660–770 / 770–800 / >800 psia during LM entry). The same telemetry parameter legitimately uses different criteria in different mission phases.

The redline book also contains RCS discrete/backup logic showing that suspect valve indications can be cross-checked through commanded jet firing and telemetered thrust-chamber pressure.

### Simulation implication

Thresholds belong to:

```text
parameter + vehicle configuration + mission phase + rule/procedure
```

—not to the parameter alone.


## 2026-09-11 evidence update — mission-specific CRT pages inspected

The former size/extraction blocker is resolved. Direct inspection of the Apollo 13 scan confirms MSK 683, 966, 1123, and 1137 in ASPO-1–12 (PDF pages 179–190). Layouts are on PDF 180, 182, 186, and 188 respectively. These identifiers/layout references are now **MISSION-SPECIFIC**, superseding earlier unresolved identifier status in this document. Unchanged field-level continuity from Apollo 11 remains unproven.

See [direct inspection and page map](../../resources/research/029_apollo13_aspo45_direct_inspection.md). Full transcription, refresh behavior, operational revisions, and station access remain open. No station maturity rating is raised by this update alone.


## 2026-09-11 field-provenance update

Mission-specific R-567 Rev. 8 now maps a substantial fraction of the guidance/control content behind MSK 1123/1137 to actual LGC Descent/Ascent downlist words. Directly supported families include:

- desired/actual body rates;
- desired/actual CDU angles;
- DAP/radar mode words;
- accumulated RCS command-on-time;
- moment offsets;
- LM/CSM mass;
- PIPA/delta-velocity data;
- guidance thrust command;
- radar measurements and time tags;
- alarm/restart state.

The same pass also proves that the CONTROL-oriented CRT cannot be modeled as one LGC packet. MSK 1137 combines:

1. LGC/downlink-derived quantities;
2. ground-computed/transformed values;
3. non-LGC spacecraft instrumentation such as actuator, chamber-pressure, voltage, and temperature information.

The stable-member landing-radar velocity display is a concrete example: R-567 transmits time-tagged antenna-axis samples one component at a time, while MSK 1137 presents three stable-member components and comparison residuals. Ground processing is therefore part of the display semantics.

See `resources/research/032_apollo13_lm_crt_field_provenance.md`.

### Revised CONTROL gap

Priority now shifts to locating:

- RTCC/ground algorithms for radar coordinate conversion and PGNS/AGS comparisons;
- PCM/telemetry sources for the non-LGC propulsion/control fields;
- exact CRT refresh/request behavior.


## 2026-09-11 non-LGC telemetry provenance

The MSK 1137 hardware/instrumentation side is now partially reconstructed rather than represented only as generic information families.

Mission-era LM-7/8/9 documentation identifies:

- **GQ6510P** — DPS thrust-chamber pressure;
- **GQ6806H** — variable-injector actuator position.

The March 9, 1970 LM Data Book identifies:

- **GN7563T** — landing-radar antenna temperature, explicitly **LM-7**;
- **GN7723T** — rendezvous-radar antenna temperature, **LM-6 and subsequent**.

A later NASA Apollo telemetry summary independently maps GQ6806H, GN7563T and GN7723T to primary display **MSK 1137**, giving a strong two-source chain from spacecraft measurement identity to display destination. The same summary maps several PGNCS electrical/temperature measurements to 1137, including PIPA supply, telemetry-bias voltage, 800-Hz IMU supply, 3.2-kHz suspension supply and PIPA temperature; Apollo-13-specific identifier/calibration confirmation remains pending for those fields.

A particularly important fidelity constraint comes from the LM-7 LR-temperature redline sheet: it states that the **CRT reading may not correspond directly to the physical heater trip values because instrumentation error is not included in those trip values**. The simulation therefore cannot treat physical state, telemetry measurement, and displayed engineering value as automatically identical.

See `resources/research/034_apollo13_msk1137_non_lgc_telemetry.md`.

### Revised CONTROL gap

The remaining high-value work is now:

1. certify GQ6510P routing to the Apollo 13 MSK 1137 TCP field;
2. establish Apollo-13-specific definitions for the PGNCS power/PIPA measurements;
3. recover engineering conversion / display precision and CRT update behavior;
4. continue the same provenance reconstruction for MSK 1123.


## 2026-09-11 MSK 1123 provenance pass

The first source-class reconstruction for **MSK 1123 — LM GUID, CONTROL AND PROP RT** is now documented.

The page is confirmed to mix:

- LGC/PGNS digital-downlink values;
- direct PCM control-hardware measurements;
- AGS/AEA information;
- radar information;
- APS/RCS propulsion state;
- ground context and processed comparisons.

Apollo telemetry routing tables explicitly associate named control measurements with 1123, including RGA yaw/pitch/roll rates and attitude-error channels, and also route selected APS/RCS measurements to the same page.

This materially strengthens the case that 1123 is one of CONTROL's cross-discipline real-time pages, but exact Apollo-13-specific routing/calibration and station access are still incomplete.

See `resources/research/035_apollo13_msk1123_field_provenance.md`.


## 2026-09-11 AGS burn-monitor evidence

Apollo 13's contingency burns provide direct operational evidence for AGS/CONTROL monitoring behavior.

For the final course correction, Mission Control instructed the crew to:

- perform a body-axis alignment;
- zero DEDA addresses 404/405/406;
- select address 470;
- inspect the pre-burn bias;
- execute the burn while using AGS as an independent monitor.

Haise reported about -0.2 bias at 470 as ignition occurred.

This supports modeling AGS burn monitoring as a stateful preparation/measurement process rather than a generic “backup guidance enabled” switch.

The exact relation between these DEDA variables and CONTROL-visible MSK 1123 fields still requires AEA telemetry-to-CRT mapping.

See `resources/research/036_apollo13_ags_fp7_deda_evidence.md`.
