# Apollo 13 AGS telemetry and ground-processing path

Date: 2026-09-11  
Status: **REVIEWED-PARTIAL — telemetry architecture and an Apollo 13 ground-processing failure are documented; exact Flight Program 7 telemetry word-to-memory mapping remains unresolved.**

## Purpose

Research note 036 established operational Flight Program 7 DEDA address behavior for Apollo 13.

This note separates a second interface that must not be conflated with DEDA:

> the **AEA digital telemetry output used by Mission Control**.

It also documents an actual Apollo 13 case in which the spacecraft/AGS attitude state was satisfactory but **RTCC ground processing of AGS body angles was wrong**.

That event is direct evidence for keeping physical state, raw telemetry, ground processing, and controller display as independent simulation layers.

---

# 1. Mission-specific Apollo 13 handbook evidence

## Source

**Apollo Operations Handbook — Lunar Module LM 7 and Subsequent, Volume I, Subsystems Data**  
Document: **LMA790-3-LM**  
Date: **1 February 1970**

The handbook explicitly supersedes the 15 September 1969 LM-6-and-subsequent edition and is the correct preflight vehicle family for Apollo 13's LM-7.

Its GN&C section includes:

- §2.1.8 — Telemetry Measurements;
- Table 2.1-5 — Abort Electronics Assembly Input Signal Characteristics;
- Table 2.1-6 — Abort Electronics Assembly Output Signal Characteristics;
- **Table 2.1-7 — Abort Electronics Assembly Telemetry Word List**;
- Table 2.1-8 — PGNS Downlink Data Update Sequence;
- Table 2.1-36 — DEDA Input List;
- Table 2.1-37 — DEDA Output List;
- Table 2.1-38 — DEDA Accessible Constants.

### Current extraction boundary

The surviving high-resolution Apollo 13 handbook scan is extremely large. The searchable web index confirms the February 1970 title/date and these table locations, but this pass has **not yet directly extracted the full LM-7 Table 2.1-7 contents**.

Therefore:

- the existence of a mission-era AEA telemetry word list is documented;
- the exact Flight Program 7 word-to-memory mapping remains unresolved.

Do not substitute an earlier Flight Program 6 table as the Apollo 13 table.

---

# 2. AEA telemetry architecture

Surviving Apollo LM Operations Handbook material and AGS technical documentation establish the AEA telemetry transport architecture.

## Output telemetry register

The AEA contains a **24-bit output telemetry register**.

A telemetry output word consists of:

- a **6-bit identification code**;
- followed by an **18-bit AEA central-computer word**.

The identification code represents the sequential position in the telemetry list.

## Telemetry block

The telemetry list is a **50-word block**.

General AGS documentation describes a 50-word digital telemetry downlink from the AEA repeated **once per second**.

This is an important distinction from:

- AEA internal computation cycles;
- DEDA display update behavior;
- Mission Control CRT update behavior.

These cadences must not be merged.

### Architecture

```text
AEA internal memory / computed state
           |
           v
mission-program telemetry list
      (50 selected words)
           |
           v
AEA 24-bit output telemetry register
  [6-bit ID + 18-bit data word]
           |
           v
LM instrumentation / telemetry path
           |
           v
ground reception / decoding
           |
           v
RTCC / display processing
           |
           v
Mission Control CRT product
```

The **selection of the 50 AEA memory words is software/version dependent**. The transport architecture is stable evidence; the Apollo 13 Flight Program 7 list itself still needs direct extraction.

---

# 3. DEDA is a separate interface

The DEDA is the crew's manual data-entry/readout interface to AEA memory.

Apollo AGS documentation treats DEDA communication separately from the AEA telemetry output register.

Conceptually:

```text
                    +--> DEDA address/readout --> crew
AEA internal state -|
                    +--> 50-word telemetry --> ground --> MCC
```

Selecting a DEDA address should therefore **not** be assumed to change which telemetry words Mission Control receives.

Likewise, a crew-visible DEDA quantity and a Mission Control CRT quantity can share an underlying AEA variable without being the same interface or refresh path.

This is especially important for MSK 1123, which contains both:

- AGS engineering/state quantities;
- DEDA address/readout/status information.

---

# 4. Apollo 13 actual ground-processing failure

## Source

*Mission Operations Report — Apollo 13*, LM Control Officer report, post-MCC-5 sequence.

After MCC-5:

1. the crew maneuvered to passive-thermal-control attitude using AGS;
2. pitch and roll rates were nulled;
3. yaw pulses were applied to establish PTC;
4. the crew switched to low-bit-rate telemetry.

The last high-bit-rate ground attitude indication did **not** agree with the desired attitude, so Mission Control requested a return to high bit rate.

The report then states that it became apparent that:

> the RTCC was incorrectly processing AGS body angles.

Mission Control **disregarded the improper readout** and used the FDAI reference system, which showed that PTC had actually been established correctly.

LM power-down then continued.

---

# 5. Why the Apollo 13 event matters

This is a direct historical example of four states diverging:

```text
actual spacecraft attitude
        !=
ground-computed/displayed AGS attitude
```

while the crew's independent attitude reference was good enough to establish the correct condition.

The error was not simply:

- bad spacecraft control;
- bad AGS hardware;
- bad raw sensor data;
- or bad crew execution.

The problem was specifically in **ground processing**.

That means an authentic simulator must allow:

```text
PHYSICAL STATE ................. correct
RAW / RECEIVED TELEMETRY ....... potentially correct
GROUND TRANSFORMATION ........... wrong
CONTROLLER DISPLAY PRODUCT ...... wrong
INDEPENDENT CREW/FDAI CUE ....... correct
```

A controller can then diagnose that discrepancy and reject the bad ground product.

---

# 6. Consequence for MSK 1123

Research note 035 classified MSK 1123 as a composite page containing:

- LGC/PGNS information;
- PCM control-hardware measurements;
- AGS/AEA information;
- propulsion/radar information;
- ground context and derived values.

This note strengthens the AGS side of that model.

For every AGS-derived MSK 1123 field, the eventual parameter dictionary should distinguish:

```text
AEA internal variable
Flight Program 7 telemetry-list membership
telemetry word ID
engineering scaling
ground coordinate/frame transformation
ground validity / processing state
CRT field representation
```

A field such as an AGS body angle cannot safely be represented as:

```text
display_value = spacecraft.ags.body_angle
```

because Apollo 13 itself demonstrates that the ground transformation could be wrong.

---

# 7. Failure-model implication

The project now has a historically documented basis for **ground-processing faults**.

These should be separate failure classes from spacecraft faults.

Possible implementation categories, only when supported by scenario evidence:

- wrong coordinate transformation;
- wrong reference-frame selection;
- incorrect vehicle/configuration selection;
- stale computational product;
- wrong RTCC model/input;
- valid telemetry decoded or processed incorrectly.

Apollo 13 already provides examples in more than one discipline:

- FIDO encountered incorrect RTCC model/configuration state and competing trajectory vectors;
- AGS body angles were incorrectly processed by RTCC after MCC-5.

This reinforces a general project rule:

> Mission Control displays are observations/products, not omniscient access to simulation truth.

---

# 8. Update-rate distinctions

Current documented timing should remain separated:

### AEA computation
Various functions execute on 20-ms, 40-ms, and 2-second cycles depending on function.

### AEA digital telemetry
50-word telemetry list repeated once per second in general AGS documentation.

### DEDA
Crew display/update behavior follows its own interface timing.

### MCC CRT
Exact MSK 1123 refresh/update cadence remains unresolved.

Therefore **1 Hz AEA telemetry does not prove a 1 Hz CRT refresh**.

---

# 9. Evidence status

## DOCUMENTED

- Apollo 13 LM-7 handbook contains an AEA telemetry word-list table and separate DEDA tables.
- AEA telemetry uses a dedicated output path distinct from DEDA.
- General AGS telemetry is a 50-word digital list repeated once per second.
- Telemetry words use an identification code plus an AEA computer data word.
- Apollo 13 experienced an RTCC error processing AGS body angles after MCC-5.
- Mission Control recognized the discrepancy, rejected the improper ground readout, and used an independent FDAI reference.

## PARTIALLY DOCUMENTED

- continuity of the exact telemetry register/word format into Apollo 13 is strongly supported by the mission-era handbook family but still needs direct LM-7 page extraction.
- relationship between AEA telemetry words and individual MSK 1123 AGS fields.

## NOT YET ESTABLISHED

- complete Flight Program 7 Table 2.1-7 word list;
- exact telemetry IDs for each Apollo 13 AGS variable;
- exact RTCC equations that produced the erroneous body-angle result;
- which MSK 1123 fields were affected by that specific RTCC processing problem;
- exact CRT refresh behavior.

---

# 10. Sources

## Apollo 13 / LM-7

- **Apollo Operations Handbook — Lunar Module LM 7 and Subsequent, Volume I**, LMA790-3-LM, 1 February 1970.
  - Apollo 13 Flight Journal document collection preserves the high-resolution scan.
  - Searchable archival copy confirms GN&C tables 2.1-5 through 2.1-8 and DEDA tables 2.1-36 through 2.1-38.
- **Mission Operations Report — Apollo 13**, 28 April 1970, LM Control Officer report — RTCC AGS body-angle processing anomaly after MCC-5.

## Architecture continuity

- Apollo LM Operations Handbook GN&C descriptions of AEA input/output telemetry registers.
- Apollo AGS technical documentation describing the 50-word AEA telemetry list repeated once per second.

---

# 11. Next work

1. Extract the February 1970 LM-7 **Table 2.1-7** through an alternate archival/page-level source.
2. Compare it with the earlier Flight Program 6 telemetry word list and identify exactly which words changed for Flight Program 7.
3. Map Flight Program 7 telemetry words to the DEDA/address variables documented in note 036.
4. Trace those telemetry outputs into MSK 1123 AGS fields and identify any RTCC coordinate transformations.
5. Preserve the post-MCC-5 RTCC body-angle anomaly as a future validation test for the ground-processing layer.
