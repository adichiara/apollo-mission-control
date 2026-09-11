# Apollo 13 TELMU Station Specification

Status: **research specification — partial**

Purpose: reconstruct the Apollo 13 Lunar Module Electrical, Environmental, and EMU controller from mission-specific evidence.

TELMU is the LM systems/life-support counterpart to CSM EECOM. Apollo 13 gives unusually strong evidence because the LM became the crew's lifeboat and TELMU had to continuously determine whether its consumables could support the selected return trajectory.

---

## 1. Position

**Call sign / position:** TELMU  
**Apollo 13 Mission Operations Report:** LM Electrical, Environmental, and EMU Officer

### Documented responsibility

TELMU monitored and troubleshot LM:

- electrical power
- environmental control
- consumables
- instrumentation/sequential systems within the LM systems discipline
- EMU/lunar-surface-related systems as applicable

Apollo 13's contingency transformed the position into a continuous **LM lifetime / consumables-management** function.

---

# 2. Known preflight anomalies

TELMU records that Apollo 13 launched with three known LM anomalies:

1. leaking ascent-stage O2 tank 2 shutoff valve
2. RCS A/B-2 Quad 1 circuit breaker mechanically maintained closed
3. apparent heat leak in the DPS supercritical-helium system

The first two were considered minor; the SHe issue required a flight-plan/procedure change.

This demonstrates that a scenario may start with known nonnominal conditions that are not the primary crisis.

---

# 3. CSM accident transition

Immediately after the CSM oxygen-tank event, TELMU could observe effects on the dormant/docked LM through its power relationship with the CSM:

- LM heater current about 1.3 A
- Main Bus B voltage approximately 3.9 V
- heater current rising slightly
- later Main Bus B falling to 0 V
- LM heater current dropping to zero
- probable relay opening

By about 57:44 GET the LM was on internal power; LM telemetry was received at 57:57 GET.

Initial LM power-up reached roughly **45–50 A**.

### Simulation implication

TELMU must understand both LM internal systems and the LM/CSM electrical interface during docked phases.

---

# 4. The central Apollo 13 TELMU problem: LM lifetime

Once the return trajectory was chosen, TELMU's immediate concern was whether the LM could sustain the crew until entry.

Based on approximately 59:00 GET status, TELMU established consumable constraints.

## 4.1 Electrical current

Required average current:

**≤24 A**

for the remainder of the mission under the initial return assumptions.

## 4.2 Cooling water

Required average water usage:

**≤3.5 lb/hr**

The report directly ties water usage to heat/electrical load.

## 4.3 Oxygen

Oxygen was not initially limiting.

Average O2 usage settled around:

**0.23 lb/hr**

although a temporarily higher value was observed because of the known leaking ascent O2 tank valve.

## 4.4 Lithium hydroxide

LM-only LiOH capacity was inadequate.

The LM carried:

- 2 primary cartridges
- 3 secondary/PLSS-type cartridges

with estimated capability of about 53 hours under the assumptions used.

A method of using CSM cartridges therefore became necessary.

### Simulation significance

The station's main challenge is not a single "life support health" value.

TELMU has several independent consumables with different:

- remaining quantities
- usage rates
- projected exhaustion times
- dependencies on current spacecraft configuration

The controlling consumable can change over time.

---

# 5. Progressive power-down

TELMU records staged power reduction:

- initial LM power-up approximately 45–50 A
- reduced to about 35–40 A
- planned approximately 27 A while retaining PGNS through the major DPS burn
- planned low configuration around 17 A / 2.7 lb/hr water
- actual full power-down approximately **12 A**
- actual water usage eventually about **2.5–2.8 lb/hr**

The full power-down turned off:

- RCS heaters
- ASA heaters
- most displays

while retaining the **CWEA**.

### Simulation implication

Power conservation should be represented through actual load/configuration changes and resulting consumable/thermal effects, not through an abstract "conserve power" command.

---

# 6. Thermal tradeoffs

Low power caused the LM cabin temperature to fall to roughly **45–50 °F**.

A proposed use of the SUIT TEMP control at FULL HOT did not help and further lowered temperature at the low-power condition.

Later the LM was powered up earlier than planned before reentry partly to provide crew warmth.

This shows a real systems trade:

```text
more electrical load
    ↕
more water/cooling use
    ↕
thermal environment / crew comfort
    ↕
remaining lifetime
```

TELMU must therefore reason about interacting resource domains rather than separate gauges.

---

# 7. Consumable status at LM jettison

At approximately 141:30 GET, TELMU reported usable remaining margins:

- **EPS:** 189.6 A-h — projected lifetime to about 146:00 GET
- **Water:** 28.2 lb — projected lifetime to about 147:06 GET
- **O2:** 28.5 lb — projected lifetime to about 265:30 GET
- **LiOH:** about 37 hours remaining from LM/PLSS cartridges

The point is not simply that supplies remained.

The controller continuously translated current configuration and usage rate into **time margin against mission milestones**.

That projected-lifetime calculation is a core station function.

---

# 8. Environmental Control System evidence

## 8.1 Water

Water usage initially reached approximately **7.7 lb/hr** during powered-up operation and later fell to 2.5–2.8 lb/hr in the low-power state.

The report attributes the early high rate partly to cooling the spacecraft structure and powered equipment.

Therefore usage rate has dynamic thermal causes; it should not be a fixed linear drain.

## 8.2 CO2 / LiOH

TELMU tracked CO2 partial pressure and cartridge state.

Examples:

- primary LM cartridge used until CO2 PP approached **14.9 mmHg**
- secondary/PLSS-type cartridge selected
- ground-developed adapter enabled CSM cartridges to be used with the LM suit loop
- CSM cartridges were selected when CO2 PP later reached about **7.5 mmHg**

This is a clear example of real-time procedure development altering the resource model.

## 8.3 Oxygen

Average oxygen usage remained about 0.23 lb/hr.

The known ascent O2 tank 2 valve leak created a misleading/high usage condition and pressure above the nominal published redline.

SPAN later confirmed that the nominal redline was not valid for the existing configuration.

### Simulation implication

A historical "redline" is not necessarily a universal physical-failure threshold. Rules/limits can depend on system configuration and may be reassessed by support teams.

---

# 9. Electrical Power System evidence

TELMU's report shows load sharing and battery management as continuous work.

Examples include:

- descent-battery load sharing
- opening/closing electrical crossties
- different CDR/LMP bus loading
- ascent batteries brought online later
- LM power transferred to/used by CSM
- command-module entry batteries charged from LM power

A battery-malfunction indication occurred on descent battery 2.

Voltages/currents remained nominal, so the battery was disconnected to cool and later restored; an overtemperature-sensor failure was inferred.

This again separates:

- warning indication
- underlying electrical performance
- controller diagnosis/action

---

# 10. TELMU information families justified by Apollo 13

## Electrical

- bus voltage
- total/current load
- battery voltage/current/state
- battery sharing/crossties
- battery temperature/malfunction indication
- heater current
- LM/CSM power-transfer configuration
- projected amp-hour lifetime

## Water / thermal

- water quantity
- water usage rate
- glycol/cooling state
- equipment heat load
- cabin temperature
- projected water lifetime

## Oxygen

- tank quantity
- tank/manifold pressure
- O2 usage rate
- valve/leak state where observable
- projected O2 lifetime

## Atmosphere / CO2

- cabin pressure
- suit-loop state
- CO2 partial pressure
- LiOH cartridge configuration/capacity
- suit-fan / cartridge-adapter configuration

## General consumables

For each limiting consumable:

- current quantity
- current rate
- projected exhaustion GET
- margin relative to critical mission milestone

---

# 11. TELMU versus CONTROL

## TELMU

Concerned with whether the LM can **keep the crew and its systems alive**:

- power
- water
- oxygen
- CO2 removal
- temperature
- consumable lifetime

## CONTROL

Concerned with whether the LM can **control attitude and produce maneuvers**:

- DPS
- RCS
- GDA
- rates/attitude
- control modes
- propulsion constraints

They share some dependencies—for example, heaters and power influence propulsion/control hardware—but their responsibilities are distinct.

---

# 12. Backroom / SPAN relevance

Apollo 13 TELMU evidence includes cases where system limits and unusual behavior required deeper analysis.

Example: the ascent O2 tank pressure exceeded a nominal redline but SPAN determined that the published redline was not valid under the actual configuration.

This supports continued research into backroom relationships even if the final simulator later minimizes explicit backroom representation.

---

# 13. Implementation status

## DOCUMENTED

- mission-specific TELMU chronology
- major consumables and load tradeoffs
- resource targets/rates
- dynamic projected lifetime calculations
- CO2/LiOH procedure changes
- battery-warning/sensor ambiguity
- LM/CSM power-transfer role
- thermal consequences of low-power operation

## PARTIAL

- likely telemetry families and calculations
- importance of CWEA and warning indications

## UNRESOLVED

- exact Apollo 13 TELMU console layout
- exact CRT formats/display numbers
- MSK/DRK configuration
- event/limit panel layout
- exact telemetry parameter identifiers
- exact projected-lifetime calculation products/displays
- exact ground-command authority
- exact voice-loop configuration

---

# 14. Research targets

1. Locate Apollo 13 TELMU display-format documentation.
2. Locate H-2 PHO-TR155 Revision C.
3. Locate LM systems console handbook / Grumman support material.
4. Identify exact telemetry identifiers for battery, water, oxygen, CO2, and thermal parameters.
5. Determine whether consumable lifetime projections were shown on CRT, calculated in SSR, or communicated by another product.
6. Reconstruct the CWEA/ground-warning relationship relevant to TELMU.

## Primary sources

- *Mission Operations Report — Apollo 13*, Appendix G: TELMU Post Mission Report.
- *Apollo 13 Mission Report*, sections 7.2.3–7.2.5.
