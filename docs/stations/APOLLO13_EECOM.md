# Apollo 13 EECOM Station Specification

Status: **research specification — not yet implementation-ready**

Purpose: define the documented Apollo 13 CSM EECOM station as precisely as current sources allow.

The goal is to create a station specification that can later drive a phone client without inventing display content, alerts, controls, or controller responsibilities.

---

## 1. Position

**Call sign / position:** EECOM  
**Apollo 13 Mission Operations Report expansion:** Electrical, Environmental, Sequential Systems Engineer for CSM

### Documented responsibility

EECOM monitored and troubleshot Command and Service Module:

- electrical power
- environmental control
- sequential systems

Apollo 13 made EECOM one of the central contingency positions because the oxygen-tank failure rapidly became an electrical-power and consumables problem.

---

## 2. Documented console hardware

Apollo 13 Review Board figure B7-7 identifies the following EECOM console components:

| Figure location | Component |
|---:|---|
| 3 | Event indicator |
| 5 | Event indicator |
| 6 | Voice communication position |
| 7 | Precision TV monitor |
| 8 | Precision TV monitor |
| 9 | Event indicator |
| 10 | Display Request Keyboard |
| 12 | Manual Select Keyboard |
| 13 | Status / status report |
| 14 | Summary message enable keyboard |
| 18 | Analog meter |
| 21 | Voice communication position |

### What is established

- two CRT/precision-TV monitors
- selectable display formats
- DRK and MSK present
- three event-indicator groups
- voice positions
- status / summary-message controls
- analog meter

### What is not yet established

- exact Apollo 13 DRK key labels/layout
- exact MSK legends/layout
- exact indicator legends beyond what the Review Board text specifies
- exact analog-meter use/selection
- whether every control in later reconstructions matches Apollo 13 flight configuration

A modern Apollo 13 EECOM reconstruction by Andy Anderson is useful as a discovery aid, but its author explicitly noted that parts of the DRK and limit-light layout were reconstructed from later documentation and photographs. It therefore cannot be treated as primary evidence for those details.

---

## 3. CRT display behavior

The Review Board states:

- EECOM had several display formats available.
- Figures B7-8 and B7-9 show the **two displays most frequently in use**.
- These displays were updated **once per second**.

This one-second cadence is currently the best-supported default update behavior for the two preserved EECOM displays.

It should not automatically be applied to every EECOM format or every Apollo controller display.

---

# 4. Display A — CSM EPS HIGH DENSITY

Source: Apollo 13 Review Board, figure B7-8.

The preserved snapshot is headed:

```text
LM1885
CSM EPS HIGH DENSITY
CTE 055:46:51
GET 055:46:53
0518
```

The figure is a dense numerical telemetry/status page, not a graphical systems schematic.

## 4.1 DC electrical values

Documented fields include:

| Measurement | Label | Example snapshot |
|---|---|---:|
| CC0206 | VMA | 29.5 |
| CC0207 | VMB | 29.4 |
| CC0210 | VBA | 36.4 |
| CC0211 | VBB | 39.5* |
| CC0232 | VBR | 35.8 |
| CD0200 | VMLA | 0.15 |
| CD0201 | VMLB | 0.15 |
| CD0005 | VMQA | 0.15 |
| CD0006 | VMQB | 0.15 |

The screen also contains calculated/summary DC-current values:

- total spacecraft current
- total fuel-cell current
- fuel-cell percentage of spacecraft load
- total battery current
- battery percentage of spacecraft load

## 4.2 Individual currents / loads

Documented fields include:

| Measurement | Label | Example snapshot |
|---|---|---:|
| SC2113 | FC 1 | 21.4 |
| SC2114 | FC 2 | 21.3 |
| SC2115 | FC 3 | 24.9 |
| CC0222 | BAT A | 0.0 |
| CC0223 | BAT B | 0.0 |
| CC0224 | BAT C | 0.0 |
| CC0215 | CHRGR | 1.12* |
| CC2962 | LM | 1.6 |

## 4.3 AC power

Documented examples:

| Measurement | Label | Example snapshot |
|---|---|---:|
| CC0200 | AC 1 | 115.6 |
| CC0203 | AC 2 | 115.7 |

## 4.4 Fuel-cell pressures

The display includes nitrogen, oxygen, and hydrogen pressure-related values for each fuel cell.

Documented fields include:

- SC2060 — 1 N2
- SC2061 — 2 N2
- SC2062 — 3 N2
- SC2066 — 1 O2
- SC2067 — 2 O2
- SC2068 — 3 O2
- SC2069 — 1 H2
- SC2070 — 2 H2
- SC2071 — 3 H2

It also shows differential-pressure values:

- O2-N2 ΔP for fuel cells 1–3
- H2-N2 ΔP for fuel cells 1–3

## 4.5 Fuel-cell flow

Documented fields:

- SC2139 — FC 1 H2 flow
- SC2140 — FC 2 H2 flow
- SC2141 — FC 3 H2 flow
- SC2142 — FC 1 O2 flow
- SC2143 — FC 2 O2 flow
- SC2144 — FC 3 O2 flow

Units are shown on the display as lb/hr.

## 4.6 Fuel-cell thermal data

The display includes:

### Fuel-cell skin temperature

- SC2084 — 1 SKN
- SC2085 — 2 SKN
- SC2086 — 3 SKN

### Condenser / TCE-related temperature

- SC2081 — 1 TCE
- SC2082 — 2 TCE
- SC2083 — 3 TCE

### Radiator temperatures

- SC2087 — FC 1 OUT
- SC2088 — FC 2 OUT
- SC2089 — FC 3 OUT
- SC2090 — FC 1 IN
- SC2091 — FC 2 IN
- SC2092 — FC 3 IN

## 4.7 Fuel-cell load balance

The page explicitly shows percent total fuel-cell load for:

- FC 1
- FC 2
- FC 3

This is operationally important because the controller can observe redistribution of electrical load among cells.

## 4.8 Instrumentation/status area

The official figure includes an instrumentation/status section with entries such as:

- PCM
- HBR
- TMG
- CTE
- SS
- PROBE

and parameter identifiers including CT0120, CT0125, CT0126, CT0340, CT0015–CT0018, CT0620, and CS0220.

Exact interpretation of every abbreviation is not yet documented in the project and should not be guessed.

---

# 5. Display B — CSM ECS-CRYO TAB

Source: Apollo 13 Review Board, figure B7-9.

The preserved snapshot is headed:

```text
LM1839
CSM ECS-CRYO TAB
CTE 055:46:51
GET 055:46:53
0613
```

This page combines environmental-control, water, coolant, cryogenic, and total fuel-cell-current information.

## 5.1 Life support

Documented fields include:

| Measurement | Display label |
|---|---|
| CF3571 | LM CABIN P |
| CF0001 | CABIN P |
| CF0012 | SUIT P |
| CF0003 | SUIT ΔP |
| CF0015 | COMP ΔP |
| CF0006 | SURGE P |
| — | SURGE QTY |
| — | O2 TK 1 CAP ΔP |
| — | O2 TK 2 CAP ΔP |
| CF0036 | O2 MAN P |
| CF0035 | O2 FLOW |
| CF0008 | SUIT T |
| CF0002 | CABIN T |
| CF0005 | CO2 PP |

Units shown include psia, psid, inches H2O, lb/hr, °F, and mmHg.

## 5.2 Water

Fields include:

- waste quantity — percent and pounds
- potable quantity — percent and pounds
- urine-nozzle temperature
- water-nozzle temperature

Documented measurement labels include CF0009, CF0010, CF0460, and CF0461.

## 5.3 Primary coolant

Documented fields include:

- accumulator quantity
- pump pressure
- radiator inlet temperature
- radiator outlet temperature
- evaporator inlet temperature
- steam temperature
- steam pressure
- evaporator outlet temperature
- radiator valve state
- glycol flow

## 5.4 Secondary coolant

Documented fields include:

- accumulator quantity
- pump pressure
- radiator inlet temperature
- radiator outlet temperature
- steam pressure
- evaporator outlet temperature
- water-reservoir pressure

## 5.5 Cryogenic supply

The display explicitly groups four cryogenic tanks:

- O2 tank 1
- O2 tank 2
- H2 tank 1
- H2 tank 2

For the cryogenic supply, the page includes:

- pressure
- quantity percent
- temperature
- quantity in pounds

The figure identifies the pressure group as:

- SC0037-38-39-40

quantity group as:

- SC0032-33-30-31

temperature group as:

- SC0041-42-43-44

The example snapshot at GET 055:46:53 shows O2 tank 2 quantity already near the abnormal/off-scale condition associated with the known quantity-gauge anomaly.

## 5.6 Total fuel-cell current

The ECS/CRYO page also includes **TOTAL FC CUR AMPS**, providing an electrical cross-check on a primarily environmental/cryogenic display.

This overlap is important: the historical display design let EECOM correlate related systems without requiring every datum to exist on only one page.

---

# 6. Event and limit-sense indications

The Review Board documents three groups of event indicators at the top of the console.

## 6.1 Limit-sense behavior

A limit-sense light illuminated when a monitored parameter went outside high/low limits **manually set by EECOM**.

Panel 3 had 72 lights.

Among those 72 were 12 limit-sense lights covering pressure, temperature, and quantity for each of the four cryogenic tanks:

- O2 tank 1
- O2 tank 2
- H2 tank 1
- H2 tank 2

EECOM normally set tight limits so that small parameter variations would be noticed.

Therefore:

> Several limit-sense lights illuminated at once was not automatically an emergency condition.

This behavior should be preserved in any faithful simulation of the indicator system.

## 6.2 Master caution indication

The Review Board states that an indicator in the upper row of panel 9 showed the presence of a spacecraft master caution and warning.

## 6.3 Apollo 13 accident significance

The Review Board concluded that a limit-sense indication of abnormal O2 tank 2 pressure **should have appeared approximately 30 seconds before tank failure**, but there was no way to establish whether the light actually illuminated or whether it was simply not observed.

The Board later recommended making MCC limit sensing a more positive backup warning system.

This is important simulator evidence:

- alerts could be subtle,
- alerts could coexist with other out-of-limit indications,
- controllers could miss a real signal,
- the simulation should not turn every threshold crossing into an unmistakable modern alarm.

---

# 7. Historical playback / HSD Format 30

The Apollo 13 EECOM postmission report states that **HSD Format 30** was available for the first time on Apollo 13 and was used extensively for data playback related to the O2 tank 2 anomaly.

This is **not the same thing** as the live display named CSM EPS HIGH DENSITY.

Format 30 belongs to the high-speed telemetry/playback workflow.

The Philco-Ford Display Formats Manual describes subformats of high-speed data Format 30 being used to produce long-burn overlays and related flight-control products.

### Simulation implication

A mature EECOM implementation may eventually need a way to inspect historical/high-rate data after an anomaly.

That function should not be confused with simply scrolling backward through the normal live display.

Exact user workflow remains unresolved.

---

# 8. Staff Support Room relationship

Apollo 13 EECOM's postmission report specifically praises the EECOM Staff Support Room and particularly the electrical-power specialists.

The report notes that the O2 tank 2 anomaly rapidly became a power-management problem both:

- during the immediate anomaly,
- and later during entry planning.

Backroom support is therefore historically important to understanding the station, even if the final game does not represent every backroom position explicitly.

No simplification decision is being made here.

---

# 9. Real-time information uncertainty

The Apollo 13 accident demonstrates why the simulator must distinguish physical truth from telemetry.

Immediately after the accident:

- the EECOM saw many implausible values,
- the O2 tank 2 quantity gauge had already failed earlier in the mission,
- several telemetry values appeared unrealistic,
- Mission Control initially suspected instrumentation failure.

The Review Board describes the first several minutes as an effort to validate readings and determine whether the problem was instrumentation/electrical rather than immediately recognizing the actual physical failure.

Therefore the EECOM station must never be designed as an omniscient spacecraft-health dashboard.

---

# 10. Commands and crew actions

Current evidence establishes EECOM monitoring, diagnosis, recommendations, and coordination.

The project has **not yet established a documented Apollo 13 EECOM direct ground-command panel/capability equivalent to the early CSM command-panel material**.

Do not add generic subsystem command buttons to the EECOM client.

Many operational actions in Apollo 13 were performed by the crew after recommendations/instructions were relayed through Mission Control/CAPCOM.

Exact ground-command authority for the Apollo 13 EECOM station remains an explicit research question.

---

# 11. Implementation-readiness checklist

Before implementing an authentic Apollo 13 EECOM client, still resolve:

- [ ] exact display format/channel identifiers for CSM EPS HIGH DENSITY
- [ ] exact display format/channel identifiers for CSM ECS-CRYO TAB
- [ ] exact DRK key layout for Apollo 13 EECOM
- [ ] exact MSK layout/labels
- [ ] exact event-indicator legends
- [ ] exact status/status-report keyboard behavior
- [ ] exact summary-message-enable keyboard behavior
- [ ] analog meter function/selection
- [ ] exact voice-loop selections
- [ ] Apollo 13 EECOM command authority
- [ ] interpretation of unresolved instrumentation/status abbreviations
- [ ] visual verification of all OCR/transcribed parameter codes against high-resolution figures
- [ ] complete catalog of other EECOM display formats
- [ ] nominal/limit values and mission-phase-specific monitoring practices

Until those are resolved, the two preserved displays can support a **research prototype**, not a claim of a complete EECOM console simulation.

---

## Primary sources

1. *Report of Apollo 13 Review Board, Appendix B*, Mission Control section and figures B7-7, B7-8, B7-9.  
   NASA-TM-X-66472 / NTRS 19700078726.

2. *Mission Operations Report — Apollo 13*, Appendix E, EECOM Post Mission Report, 28 April 1970.

3. Philco-Ford, *Display Formats Manual*, PHO-TR515, 12 January 1973.

## Secondary/discovery sources

Andy Anderson's Apollo 13 EECOM console reconstruction is useful for locating and interpreting surviving console material but contains explicitly reconstructed/inferred portions. It must not override primary documentation.
