# Apollo 13 MSK 1123 — AGS field provenance matrix

Date: 2026-09-11  
Status: **REVIEWED-PARTIAL — major AGS source paths are now separated; several exact field transformations remain unresolved.**

## Purpose

Research notes 035–043 progressively resolved the Apollo 13 MSK 1123 AGS section.

This note consolidates the current evidence into one field-oriented matrix so future implementation does not accidentally collapse:

- AEA digital telemetry;
- analog/control-system PCM;
- DEDA state;
- ground-derived values;
- crew-display outputs.

The Apollo 13 ASPO 45 source remains the mission-specific authority for the existence/layout of MSK 1123. Earlier Apollo AC Electronics definitions are used only where they clarify field semantics that are consistent with the directly inspected Apollo 13 family.

---

## Current matrix

| MSK 1123 family | Historical meaning | Best current source path | Confidence | Main unresolved issue |
|---|---|---|---|---|
| **AGS time** | Abort Guidance System time | AEA absolute-time telemetry, principally TA1/TA2 family | Strong continuity + Apollo 13 dictionary support | exact ground reconstruction/format into H:M:S |
| **RGA rate** | AGS body-mounted rate gyro outputs | CES/RGA analog measurement → PCM telemetry; GH1461V/GH1462V/GH1463V are routed to 1123 in Apollo telemetry tables | Strong routing continuity | LM-7-specific calibration/table verification |
| **ASA rate** | Abort Sensing Assembly body rates | ASA gyro pulses → AEA delta-angle quantities; DAX/DAY/DAZ are telemetered incremental rotations per 20 ms | Strong source-family candidate | exact MCC rate conversion and confirmation that 1123 uses DAX/DAY/DAZ |
| **AGS ATT** | AGS body angles | AEA direction-cosine state → six telemetered direction cosines → RTCC/ground angle conversion | Strong architecture; Apollo 13 ground-failure validated | exact FP7 telemetry IDs + RTCC angle equation |
| **AGS ERR** | AGS attitude errors | AEA computes Ex/Ey/Ez → analog outputs to CES/FDAI; attitude-error analogs measured in PCM and routed to 1123 | Strong source-path/routing continuity | mission-specific LM-7 measurement calibration and exact axis IDs |
| **AGS VEL** | AGS indicated velocity | AEA LM velocity vector telemetry VX/VY/VZ (0360–0362) is the strongest source candidate | Strong candidate | exact displayed frame/components/scaling |
| **AGS DEL VEL** | AGS measured delta velocity | multiple AEA delta-V layers exist: DVX/Y/Z telemetry (0350–0352), VD1X/Y/Z telemetry (0404–0406), VDX/Y/Z DEDA (0470–0472) | Partial / unresolved selection | exact MCC field source and transformation |
| **AGS ULL** | AGS ullage measurement, velocity units | X-axis sensed-velocity / thrust-acceleration chain; separate from MU8 counter/status | Strong source-family constraint | exact engineering value presented on 1123 |
| **DEDA block** | AGS DEDA address/readout/clear/data state | RMF / DD / CMF / ADST in AEA telemetry | Strong | exact Apollo 13 masks/formatting |
| **AGS mode/status** | AGS control/mode state | combination of AEA selector/discretes and PCM mode discretes depending on field | Partial | exact field-to-source assignment |

---

# 1. AGS time

The AEA telemetry block contains both portions of absolute time:

- **TA2** at 0353 — least-significant portion of absolute time;
- **TA1** at 0377 — most-significant absolute time.

The Apollo 13 G&N Dictionary independently defines address 377 as **AGS Computer Time** for DEDA purposes.

The MSK 1123 field is formatted as a conventional time readout rather than as raw AEA binary words.

Therefore the current source model is:

```text
AEA absolute time state
   ↓
TA1 / TA2 telemetry
   ↓
ground reconstruction / scaling
   ↓
MSK 1123 AGS time
```

The exact ground formatting algorithm remains to be documented.

---

# 2. RGA rate — direct hardware/PCM path

MSK 1123 distinguishes **RGA RATE** from ASA rate.

The Apollo telemetry summary explicitly identifies:

- **GH1461V — RGA yaw rate**
- **GH1462V — RGA pitch rate**
- **GH1463V — RGA roll rate**

with engineering units of degrees/second and primary MSK routing including **1123**.

These are CES/body-mounted rate-gyro signals.

This provides a clear non-AEA-digital path:

```text
body-mounted rate gyro
   ↓
CES / signal conditioning
   ↓
PCM analog telemetry
   ↓
ground engineering conversion
   ↓
MSK 1123 RGA RATE
```

The routing source is Apollo-wide/retrospective; exact LM-7 calibration should still be confirmed in a mission-era instrumentation source.

---

# 3. ASA rate — likely AEA delta-angle telemetry path

The Abort Sensing Assembly supplies gyro information to the AEA.

The surviving programmed-equation documentation defines:

- **DAX**
- **DAY**
- **DAZ**

as compensated incremental vehicle rotation about the X/Y/Z body axes per **20 ms**.

These quantities are in the AEA telemetry block at:

- 0354
- 0355
- 0356

and are explicitly marked as telemetry delta-alpha values in adjacent programs.

Because the MSK field is **ASA body rate** in degrees/second, DAX/DAY/DAZ form a strong source family:

```text
ASA gyro pulses
   ↓
AEA compensated delta-angle increments
   ↓
DAX / DAY / DAZ telemetry
   ↓
ground divide/scale to angular rate
   ↓
MSK 1123 ASA RATE
```

But the final divide/scale and exact Apollo 13 routing have not yet been found.

Therefore this is **not yet a certified field mapping**.

---

# 4. AGS attitude — ground-derived from orientation matrix telemetry

This is currently one of the strongest AGS provenance chains.

AEA telemetry carries six direction cosines:

- A11T/A12T/A13T
- A31T/A32T/A33T

representing the X-body and Z-body rows of the AEA attitude matrix.

The source code snapshots these values for telemetry.

The controller-facing display instead wants **AGS body angles**.

Therefore a ground conversion is necessary:

```text
AEA attitude matrix
   ↓
six telemetered direction cosines
   ↓
RTCC / ground transformation
   ↓
body-angle engineering values
   ↓
MSK 1123 AGS ATT
```

Apollo 13 provides direct operational validation of this separation: after MCC-5, RTCC incorrectly processed AGS body angles even though the vehicle had established the desired PTC condition.

See note 040.

---

# 5. AGS attitude error — separate analog output path

The AGS specification states that the AEA computes attitude error signals and outputs them to the Control Electronics Section for vehicle control and to flight displays.

The AEA interface specification describes Ex/Ey/Ez as **800-Hz analog attitude-error outputs**.

Independent LM instrumentation material identifies yaw/pitch/roll attitude-error measurements in the GH1455/GH1456/GH1457 family, and Apollo telemetry summary material routes the attitude-error channels to MSK 1123.

Thus the best current architecture is:

```text
AEA guidance / attitude solution
   ↓
computed Ex / Ey / Ez
   ↓
AEA DAC / analog outputs
   ↓
CES + FDAI
   ↓
instrumentation measurement / PCM
   ↓
Mission Control engineering conversion
   ↓
MSK 1123 AGS ERR
```

This is a different path from the AEA's 50-word digital telemetry block.

### Important implication

A digital AEA telemetry problem and an AGS-error analog-output/instrumentation problem are separable failure modes.

---

# 6. AGS indicated velocity

The AEA telemetry block contains:

- **VX / VY / VZ** at 0360–0362 — LM velocity components.

The Apollo 13 G&N Dictionary independently defines these addresses as the LM present inertial velocity components.

These are therefore the strongest current source candidates for the 1123 **AGS VEL** triplet.

However, the display definition's phrase “indicated velocity” does not by itself establish:

- displayed reference frame;
- component ordering;
- whether ground transforms the inertial vector;
- exact precision/scaling.

So the source family is strong, while the final renderer mapping remains partial.

---

# 7. AGS delta velocity — multiple plausible AEA layers

This field needs special caution because several distinct AEA quantities exist.

## DVX / DVY / DVZ — 0350–0352

Adjacent AGS source listings label these:

> BODY DELTA V'S THIS CYCLE

Programmed equations define them as compensated incremental velocity components accumulated per 20 ms along body X/Y/Z axes.

They are part of the 50-word telemetry block.

## VD1X / VD1Y / VD1Z — 0404–0406

Also in the telemetry block, described as 40-ms velocity accumulation variables used in navigation logic.

## VDX / VDY / VDZ — 0470–0472

Separate navigation-update / DEDA variables used by the crew as measured-delta-V readouts.

Apollo 13 mission-specific procedures validate the 470–472 interface.

### Current conclusion

The existence of **DVX/Y/Z at 0350–0352** makes the earlier assumption that MSK 1123 AGS DEL VEL would most naturally use VD1 incomplete.

At present, DVX/Y/Z are arguably the stronger direct-display candidate because:

- they are explicitly in the telemetry block;
- they are explicitly labeled body delta-V;
- they match the conceptual meaning of an AGS measured-delta-velocity display.

But no MCC source has yet certified the mapping.

Therefore:

> **Do not freeze AGS DEL VEL to DVX/Y/Z, VD1X/Y/Z, or DEDA 470–472 yet.**

Research note 041 remains valid in distinguishing the interfaces but should not be read as preferring VD1 for the CRT field.

---

# 8. AGS ullage

AGS ullage logic contains at least:

- sensed X-axis velocity increments;
- computed thrust acceleration AT;
- threshold comparison;
- MU8 consecutive-cycle counter;
- counter limit;
- acquired state.

MSK 1123's AGS ULL field is in velocity units, so it is not the counter or Boolean state.

The source family is constrained, but the exact field calculation remains unresolved.

See note 042.

---

# 9. DEDA status block

AEA digital telemetry explicitly contains:

- RMF — readout mode;
- DD — DEDA data;
- CMF — clear mode;
- ADST — DEDA address.

This is the strongest direct source for the MSK 1123 DEDA-status area.

See note 043.

---

# 10. AGS mode/status information

The page also includes AGS/vehicle mode indications.

Possible source classes include:

- AEA S0 function selector at telemetry address 0400;
- AEA discrete word(s), including DISC1C;
- direct spacecraft mode discretes in PCM telemetry;
- CES switch/configuration measurements.

Do not assign a generic “AGS mode” source without field-level work.

---

# 11. Revised implementation model

The AGS section of MSK 1123 now requires at least four independent channels:

```text
AEA DIGITAL TELEMETRY
  time, vectors, direction cosines,
  DEDA state, delta-angle/delta-V data
            |
            v
      ground processing
            |
            +------> derived CRT values

AEA ANALOG OUTPUTS
  attitude errors / display-control outputs
            |
            v
      PCM instrumentation
            |
            v
          CRT

CES / RGA HARDWARE
  body rates, mode discretes
            |
            v
      PCM instrumentation
            |
            v
          CRT

GROUND CONTEXT / TRANSFORMS
  frame conversions, time formatting,
  validity logic, comparisons
            |
            v
          CRT
```

This source separation should become part of the eventual parameter dictionary.

---

# 12. Corrections / refinements to earlier notes

### AGS DEL VEL

Research note 041 correctly separates VD1 telemetry from DEDA VDX values, but the discovery/confirmation of **DVX/DVY/DVZ at 0350–0352 as body delta-V telemetry** means the final CRT-source question now has an additional—and likely stronger—candidate.

No previous architecture conclusion is reversed; the field source simply remains unresolved.

### Attitude-error measurement identifiers

OCR/transcription of Apollo telemetry tables can duplicate or distort short measurement identifiers. The LM instrumentation family supports the sequence:

- GH1455V — yaw attitude error;
- GH1456V — pitch attitude error;
- GH1457V — roll attitude error.

Use those identities only with source/version provenance attached.

---

# 13. Evidence status

## Strong / directly supported source paths

- AGS time → AEA time telemetry family.
- RGA rate → direct PCM rate-gyro measurements routed to 1123.
- AGS ATT → direction-cosine telemetry + ground conversion.
- AGS ERR → AEA analog error outputs + PCM measurement.
- DEDA block → AEA digital telemetry.

## Strong candidates, not yet certified to exact field

- ASA RATE → DAX/DAY/DAZ.
- AGS VEL → VX/VY/VZ.
- AGS DEL VEL → DVX/DVY/DVZ versus other delta-V layers.
- AGS ULL → sensed X-axis velocity/thrust-acceleration chain.

## Still needed

- exact Apollo 13 FP7 telemetry table;
- RTCC/display-calculation definitions;
- mission-specific LM-7 instrumentation calibration/routing;
- Apollo 13 CRT masks/precision;
- refresh/update behavior.

---

# 14. Sources

- Apollo 13 AC Electronics Guidance & Navigation Summary — mission-specific MSK 1123.
- Apollo 13 G&N Dictionary — mission-specific FP7 addresses.
- FP6/FP8 AGS source listings and programmed equations — adjacent-program architecture.
- AGS Performance and Interface Specification — AEA interfaces and analog attitude-error outputs.
- NASA Apollo Experience Report / LM Telemetry Data Summary — Primary MSK routing.
- LM elementary functional diagrams / instrumentation documentation — measurement identities.
- Apollo 13 Mission Operations Report — RTCC AGS body-angle processing anomaly.

---

# 15. Next work

1. Search for MCC/RTCC definitions of AGS VEL / DEL VEL / ULL calculations.
2. Recover the exact FP7 Table 2.1-7 to certify the digital-telemetry side.
3. Re-transcribe Apollo 13 ASPO-9 so exact masks/precision can be attached to each row.
4. Locate LM-7 instrumentation definitions for GH1455–GH1463.
5. Convert this matrix into the first normalized implementation-oriented parameter dictionary only after those sources are resolved.
