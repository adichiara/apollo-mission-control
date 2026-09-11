# Apollo 13 MSK 1137 — non-LGC telemetry provenance

Date: 2026-09-11  
Status: **REVIEWED-PARTIAL — several Apollo 13/LM-7 measurement identities are established; complete Apollo-13-specific display routing remains incomplete.**

## Purpose

Research note 032 established that Apollo 13 MSK 1137 is a composite display. Some fields derive from the LGC downlist, some are ground-computed, and others must come from spacecraft instrumentation/PCM telemetry.

This note traces the third category: **non-LGC spacecraft measurements**.

The goal is not to infer missing telemetry. Only measurement identities and display relationships supported by source material are recorded.

---

## Evidence classes used here

### Mission-/vehicle-specific evidence

Preferred for the Apollo 13 profile:

- LM-7/8/9 Elementary Functional Diagrams;
- March 9, 1970 LM Data Book launch-redline material with LM-7 or LM-6-and-subsequent effectivity.

### Apollo-wide / later continuity evidence

NASA's 1975 Apollo Experience Report, *Engineering and Analysis Mission Support*, contains a Lunar Module Telemetry Data Summary with a **Primary MSK Number** column.

This is highly useful for connecting measurement identifiers to MSK 1137, but it is retrospective and Apollo-wide. It is used here as **routing/continuity evidence**, not by itself as proof of an Apollo 13 console database revision.

---

# 1. DPS thrust-chamber pressure

## Mission-era measurement identity

**GQ6510P — PRESS, THRUST CHAMBER**

The LM-7/8/9 Elementary Functional Diagrams list GQ6510P as the thrust-chamber-pressure measurement.

The Apollo 13 ASPO 45 MSK 1137 definition includes **TCP — thrust chamber pressure**.

### Status

**DOCUMENTED:**
- GQ6510P is a real LM-7-era DPS thrust-chamber-pressure measurement.
- Apollo 13 MSK 1137 contains a thrust-chamber-pressure field.

**PARTIALLY DOCUMENTED:**
- The later NASA telemetry-summary row for GQ6510P gives DPS TCP, 0–200 psia, but its parsed Primary-MSK entry is blank.

Therefore the project should **not yet claim that GQ6510P is proven by an Apollo-13-specific source to be the exact feed for the MSK 1137 TCP field**, even though it is the obvious mission-era measurement candidate.

### Implementation consequence

Use a provisional provenance edge, not a frozen mapping:

```text
DPS physical chamber pressure
   ↓
GQ6510P spacecraft measurement
   ↓
PCM / ground processing
   ↓
[display routing still to certify]
   ↓
MSK 1137 TCP
```

---

# 2. Variable injector actuator position

## Mission-era measurement identity

**GQ6806H — POS, VARIABLE INJECTOR ACTUATOR**

The LM-7/8/9 Elementary Functional Diagrams list this measurement explicitly.

The Apollo 13 MSK 1137 definition includes **VAR ACT — variable actuator position**.

## Display-routing continuity

The NASA Apollo telemetry summary identifies:

- **GQ6806H**
- title: **VAR INJT ACT POS**
- units: percent
- approximate range: 0–100
- primary MSK: **1123, 1137**

### Status

**STRONG DOCUMENTED MAPPING:**

This is currently the strongest non-LGC provenance chain for the Apollo 13 LM display:

```text
DPS variable injector actuator
   ↓
GQ6806H
   ↓
PCM telemetry
   ↓
MSK 1137 VAR ACT
```

The measurement identity is confirmed in the LM-7/8/9 hardware documentation and the display destination is independently documented in the Apollo telemetry summary.

The remaining caution is that the Primary-MSK table is retrospective rather than an Apollo-13-specific display-loading record.

---

# 3. Landing-radar antenna temperature

## Apollo 13 / LM-7 source

The March 9, 1970 LM Data Book gives:

**GN7563T — Temp., LR Antenna**  
**SC effectivity: LM-7**

Documented characteristics include:

- units: °F;
- PCM data range: ±200°F;
- bit value: 1.6°F.

The rationale states that the sensor is associated with the LR heater/control behavior.

Most importantly for simulation fidelity, the document cautions that:

> CRT readings may not correspond exactly to the physical heater trip values because instrumentation error is not included in those trip values.

The Apollo 13 MSK 1137 definition includes landing-radar antenna temperature.

## Display-routing continuity

The later NASA telemetry summary identifies:

- **GN7563T**
- LR ANT TEMP
- primary MSK including **1137**.

### Status

**STRONG DOCUMENTED MAPPING**, with a mission-specific measurement definition and cross-Apollo display-routing confirmation.

### Simulation consequence

Do not collapse:

```text
physical antenna temperature
= telemetry measurement
= controller-displayed value
```

The measurement system itself has error. Historical rule thresholds and physical heater trip points can therefore differ from the value visible on the CRT.

This is a concrete example of why the telemetry layer must remain separate from physical mission state.

---

# 4. Rendezvous-radar antenna temperature

## Mission-era source

The same March 1970 LM Data Book gives:

**GN7723T — Temp., RR Antenna**  
**SC effectivity: LM-6 & subsequent**

Apollo 13's LM-7 is within that effectivity.

The Apollo 13 MSK 1137 definition includes rendezvous-radar antenna temperature.

## Display-routing continuity

The NASA telemetry summary identifies GN7723T as RR ANT TEMP with primary MSK including **1137**.

### Status

**STRONG DOCUMENTED MAPPING**.

---

# 5. Landing/rendezvous radar validity discretes

The later NASA telemetry summary provides additional non-LGC field candidates tied to MSK 1137:

- **GN7557X — LR VEL BAD** → primary MSK includes 1137;
- **GN7621X — RR NO TRACK** → primary MSK includes 1137.

These align with Apollo 13 MSK 1137's landing-radar velocity-validity and rendezvous-radar data/status information.

### Status

**CROSS-APOLLO ROUTING EVIDENCE ONLY** in this pass.

Mission-specific Apollo 13 / LM-7 measurement-definition sources for these discretes still need to be checked before their profile mappings are frozen.

---

# 6. PGNCS electrical / temperature measurements

The Apollo telemetry summary maps several instrumentation measurements directly to MSK 1137:

| Measurement | Telemetry title | MSK 1137 relationship |
|---|---|---|
| GG1040V | VDC PIPA SUPPLY | primary MSK 1137 |
| GG1110V / source OCR variants | 2.5 VDC TM BIAS | primary MSK 1137 |
| GG1201V / source OCR variants | IMU 28 VAC 800 | primary MSK 1137 |
| GG1331V | IRIG SUSP 3.2 KC | primary MSK 1137 |
| GG2300T | PIPA TEMP | primary MSK 1137 |

These map naturally onto the Apollo 13 ASPO 45 power/temperature fields:

- 120V;
- BIAS;
- 800~;
- 3200~;
- PIP temperature.

### Caution on identifiers

The retrospective telemetry source is affected by OCR/transcription variation in some short measurement numbers (for example GG110V versus GG1110V, GG120V versus GG1201V). Later LM instrumentation material supports the longer forms for several of these measurements.

Do **not** normalize the identifiers silently in executable data until the applicable Apollo 13 instrumentation source is inspected.

### Status

**PARTIALLY DOCUMENTED / STRONG CONTINUITY.**

The display relationship is explicit in the Apollo telemetry summary; the remaining task is to establish the exact LM-7 measurement identifiers/calibration from mission-era instrumentation documentation.

---

# 7. PIPA temperature

The later telemetry summary gives:

**GG2300T — PIPA TEMP**  
approximately 119–139°F in the tabulated range  
primary MSK **1137**.

This aligns directly with the Apollo 13 ASPO definition's PIP temperature field.

### Status

**DISPLAY RELATIONSHIP DOCUMENTED IN APOLLO-WIDE SOURCE; APOLLO-13-SPECIFIC CALIBRATION/IDENTIFIER CHECK PENDING.**

---

# 8. Important architecture result

MSK 1137 now has at least three independently documented data paths:

```text
A. LGC / PGNS
   LGC state and computed quantities
       ↓
   digital downlink
       ↓
   ground processing
       ↓
   CRT

B. Spacecraft instrumentation
   physical hardware
       ↓
   transducer / discrete
       ↓
   PCM telemetry
       ↓
   ground processing
       ↓
   CRT

C. Ground-derived products
   telemetry + reference/model data
       ↓
   RTCC / controller-support computation
       ↓
   CRT
```

Examples:

- **LGC-derived:** desired rates, CDU angles, DAP/radar words, DSKY state.
- **PCM instrumentation:** actuator position, radar temperatures, PIPA power/temperature, likely TCP.
- **Ground-derived:** PIPA bias, stable-member radar velocity transformations, PGNS/AGS comparison residuals, RTCC mass.

This is strong evidence against implementing a display as a direct view into one simulated subsystem.

---

# 9. Measurement error is operational state

The LM-7 LR-temperature redline source explicitly distinguishes the controller-visible CRT reading from the actual hardware trip values because of instrumentation error.

That implies the simulator's parameter model eventually needs, when applicable:

```text
true_value
measurement_value
measurement_error_model
measurement_validity
engineering_conversion
display_value
rule/procedure threshold
```

A flight rule may apply to the controller's measured value, while a physical failure threshold belongs to the underlying hardware state.

Do not automatically compare both against one idealized number.

---

# 10. Current confidence table

| MSK 1137 field | Candidate measurement | Apollo 13 / LM-7 measurement evidence | 1137 routing evidence | Confidence |
|---|---|---:|---:|---|
| VAR ACT | GQ6806H | Yes — LM-7/8/9 EFD | Yes — NASA telemetry summary | Strong |
| TCP | GQ6510P | Yes — LM-7/8/9 EFD | Not yet explicit in current routing table | Partial |
| LR temp | GN7563T | Yes — LM-7 redline | Yes — NASA telemetry summary | Strong |
| RR temp | GN7723T | Yes — LM-6 & subsequent redline | Yes — NASA telemetry summary | Strong |
| LR velocity valid | GN7557X | not yet mission-specific in this pass | Yes | Partial |
| RR track/data state | GN7621X | not yet mission-specific in this pass | Yes | Partial |
| 120V PIPA supply | GG1040V | LM handbook baseline confirms identity; exact preflight page revision still to verify | Yes — Apollo telemetry summary routes to 1137 | Strong continuity / mission-profile freeze pending |
| TM bias voltage | GG1110V / identifier check pending | mission-specific check pending | Yes | Partial |
| 800-Hz IMU supply | GG1201V / identifier check pending | mission-specific check pending | Yes | Partial |
| 3.2-kHz suspension supply | GG1331V | mission-specific check pending | Yes | Partial |
| PIPA temp | GG2300T | mission-specific check pending | Yes | Partial |

---

# 11. Sources

## Mission-/vehicle-specific

### Lunar Module 7, 8 & 9 Elementary Functional Diagrams
- Document family: LED-267-37C
- Public scan:
  https://www.ibiblio.org/apollo/Documents/lm-7%2C8%2C9_elementary_functional_diagrams.pdf
- Status this pass: **indexed-text inspected**; file was too large for the current web PDF renderer.
- Relevant measurement-index evidence:
  - GQ6510P — PRESS, THRUST CHAMBER
  - GQ6806H — POS, VARIABLE INJECTOR ACTUATOR

### CSM/LM Spacecraft Operational Data Book, Volume II, Part 2 — LM Launch Mission Rule Redlines
- SNA-8-D-027(II)PT2
- Revision 5, March 9, 1970
- Public scan:
  https://ibiblio.org/apollo/Documents/HSI-41196.pdf
- Directly rendered and checked:
  - PDF 87 / printed 3-55: GN7563T, LM-7 LR antenna temperature
  - PDF 88 / printed 3-56: GN7723T, LM-6 & subsequent RR antenna temperature

## Display-routing / continuity

### Apollo Experience Report — Engineering and Analysis Mission Support
- NASA TN D-7993
- NTRS document ID: 19750018953
- 1975
- https://ntrs.nasa.gov/citations/19750018953
- Use: Lunar Module Telemetry Data Summary including measurement IDs, ranges/sample information, and Primary MSK numbers.
- Caution: retrospective Apollo-wide source; do not treat as an Apollo-13-specific configuration revision by itself.

## Display definition

- AC Electronics, *Apollo 13 Guidance & Navigation Summary*, ASPO 45 CRT Displays.
- See research notes 029–032.

---

# 12. Next work

1. Locate Apollo-13/LM-7 instrumentation definitions for:
   - GG1040V;
   - GG1110V;
   - GG1201V;
   - GG1331V;
   - GG2300T;
   - GN7557X;
   - GN7621X.
2. Find an Apollo-13-specific display loading/routing source that confirms GQ6510P → MSK 1137.
3. Identify the engineering conversion and display precision for the strong mappings.
4. Determine the actual CRT update cadence, which must remain separate from telemetry sample rate.
5. Apply the same provenance method to MSK 1123.


## 2026-09-11 identifier correction and handbook check

A follow-up check corrected one transcription error in this note:

- **GG1040V**, not `GG0104V`, is the 120-VDC PIPA pulse-torque reference measurement.

This is independently supported by:
- the LM Apollo Operations Handbook signal-conditioner table, which names **GG1040V** as the 120-VDC pulse-torque reference;
- NASA's Apollo telemetry summary, which lists **GG1040V / PLS TORG REF** and routes it to primary MSKs including **1137**.

The same handbook table supports these identities:
- **GG1110V** — PCM 2.5-VDC telemetry bias;
- **GG1201V** — IMU 28-V, 800-cps 1% supply;
- **GG1331V** — 3,200-cps / 28-V supply;
- **GG2300T** — PIPA temperature.

However, the readily searchable handbook pages carrying this table show a June 15, 1970 change date. The Apollo 13 Flight Journal separately preserves the **LM-7 and Subsequent handbook dated 1970-02-01**, but its 639-MB scan was too large for the current web renderer. Until the February scan's relevant pages are directly verified, these PGNCS identities remain **strong mission-era continuity evidence, not frozen Apollo-13 profile proof**.

The Apollo 13 mission document index confirms the existence/date of that preflight LM-7 handbook. The exact February-page content remains a verification task.
