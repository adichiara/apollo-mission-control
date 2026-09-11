# Apollo 13 MSK 1123 — first field-provenance pass

Date: 2026-09-11  
Status: **REVIEWED-PARTIAL — mission-specific Apollo 13 layout/definitions are established; provenance is now separated into LGC/PGNS, AGS, PCM/control-hardware, and ground-context classes. Exact field-by-field routing remains incomplete.**

## Purpose

MSK 1123 is the Apollo 13 **LM GUID, CONTROL AND PROP RT** display documented in the mission-specific AC Electronics *Apollo 13 Guidance & Navigation Summary*.

Research notes 029–034 concentrated primarily on MSK 1137. This note begins the same provenance analysis for 1123.

The objective is not to reproduce the page yet. It is to determine what source system each displayed quantity belongs to so the simulation does not fill one CRT from one idealized state object.

---

## Mission-specific source

AC Electronics, *Apollo 13 Guidance & Navigation Summary*:

- ASPO-8 / PDF 186 — MSK 1123 layout
- ASPO-9 / PDF 187 — MSK 1123 definitions

Direct inspection was recorded in research note 029.

The Apollo 13 page contains, among other families:

- GET / MET / AGS / LGC time context;
- LGC downlist identity;
- receiving site;
- TGO / descent phase time;
- PGNS DAP rates;
- RGA rates;
- ASA rates;
- attitude commands;
- local-vertical/body attitude relationships;
- resolver/gimbal/CDU attitude quantities;
- PGNS/AGS attitude/error quantities;
- moment/offset quantities;
- AGS velocity;
- LGC delta velocity;
- AGS delta velocity / ullage;
- radar state/data;
- AGS DEDA information;
- LGC restart count;
- program / verb / noun / DSKY registers.

This is a mixed-source page by design.

---

# 1. LGC / PGNS digital-downlink class

R-567 Rev. 8, the Apollo-13-specific LUMINARY 1C data-link specification, supplies direct onboard-computer sources for several 1123 families.

Strong examples include:

- downlist identity;
- LGC timing/state;
- DSKY display-table content;
- restart/failure state;
- desired/actual CDU quantities;
- DAP/radar mode words;
- PIPA / delta-velocity data;
- radar measurements and validity state;
- guidance timing such as TGO / phase timing in the applicable programs.

The important distinction is:

> MSK 1123 is not the downlist itself.

LGC words are decoded, scaled, combined with other sources, and formatted by the ground system before becoming the CRT page.

See research note 032 for the LGC-side word mapping already established.

---

# 2. PGNS/control PCM class

NASA's Apollo telemetry summary provides independent evidence that some 1123 fields also came from spacecraft instrumentation/PCM rather than from the LGC digital downlink.

Clean examples:

| Measurement | Meaning | Primary MSK evidence |
|---|---|---|
| **GG2219V** | Pitch attitude error | 1123, 1127, 1137, 1145 |
| **GH1457V** | Roll attitude error | 1123, 1137 |
| **GH1461V** | RGA yaw rate | 1123, 1137 |
| **GH1462V** | RGA pitch rate | 1123, 1137 |
| **GH1463V** | RGA roll rate | 1123, 1137 |
| **GH1644X** | PGNS mode — attitude hold | 1123, 1137 |

The exact Apollo 13 calibration/configuration of each measurement still requires mission-era source confirmation, but the routing evidence proves that 1123 accepted direct PCM/control-system measurements in addition to LGC data.

## Consequence

For a field such as **RGA RATE**, do not assume the CRT value comes through the LGC because the page is adjacent to PGNS quantities.

The historical architecture supports:

```text
rate gyro hardware
   ↓
signal conditioning / PCM
   ↓
ground telemetry processing
   ↓
MSK 1123
```

while another nearby field can follow:

```text
LGC internal guidance state
   ↓
digital downlink
   ↓
ground processing
   ↓
MSK 1123
```

---

# 3. APS / propulsion-system PCM continuity

The Apollo telemetry summary also routes multiple propulsion measurements to primary MSK 1123.

Clean examples include:

- **GP0002P** — APS helium supply 2 pressure → 1123 / 1125 / 1169;
- **GP0025P** — APS helium regulator pressure → 1123 / 1125 / 1169;
- **GP0318X** — APS helium 1 valve closed indication → 1123;
- **GP0320X** — APS helium 2 valve closed indication → 1123;
- **GP0908X** — APS fuel-low indication → 1123.

The same Apollo-wide source shows RCS manifold/valve/quad information routed to 1123, though several OCR-damaged identifiers still require direct source verification before being entered into the Apollo 13 profile.

### Interpretation

The label **LM GUID, CONTROL AND PROP RT** is literal: 1123 is not only a guidance page. It integrates guidance/control and selected propulsion-state information.

This matches CONTROL's documented operational responsibility and supports using 1123 as one of the principal cross-discipline LM pages.

---

# 4. AGS class

Apollo 13 MSK 1123 includes a substantial AGS section:

- AGS clock/time;
- RGA rate;
- ASA rate;
- AGS attitude;
- AGS errors;
- AGS velocity;
- AGS delta velocity;
- AGS ullage;
- DEDA address/readout/clear/register content.

These are not LGC quantities.

The Apollo 13 Flight Crew G&N Dictionary is especially important because Apollo 13 used **AGS Flight Program 7**, for which surviving public source-code coverage is poorer than for earlier versions.

The Virtual AGC document index identifies the Apollo 13 Data Dictionary as uniquely valuable for Flight Program 7 variable/address information.

### Next AGS task

Map:

```text
MSK 1123 AGS field
→ Flight Program 7 / AEA variable or telemetry word
→ spacecraft telemetry path
→ CRT engineering representation
```

No generic AGS state object should be substituted before that mapping is complete.

---

# 5. Ground/context class

Some 1123 information is necessarily ground-generated or ground-contextual rather than a spacecraft measurement:

- GET;
- receiving site identity;
- display/downlist context;
- any field requiring frame conversion/comparison;
- ground interpretation of validity/status where a processed product is displayed.

The presence of these fields reinforces that MSK 1123 is a Mission Control product, not a spacecraft-native page.

---

# 6. Current provenance model

A first-pass source-class map is now:

| 1123 family | Current source class |
|---|---|
| LGC format / DSKY / restart / program state | LGC digital downlink |
| PGNS desired/actual guidance quantities | LGC and/or PGNS PCM depending on field |
| RGA rates | PCM/control hardware |
| attitude-error analogs | PCM/control hardware |
| AGS/AEA state | AGS telemetry / AEA variables |
| APS/RCS status and pressures | PCM propulsion telemetry |
| radar measurement/state | mixed LGC + radar/instrumentation path depending on field |
| GET / SITE | ground context |
| comparisons / transformed quantities | ground-derived where documented |

This classification is more important than a premature exact renderer because it determines which subsystem can fail independently.

---

# 7. Simulation implications

MSK 1123 needs to tolerate disagreement among source classes.

Examples that must remain possible in the eventual simulator:

- LGC guidance state valid while a PCM analog rate channel is bad;
- AGS solution disagreeing with PGNS while both telemetry links remain valid;
- radar hardware valid but LGC radar acceptance/status invalid;
- propulsion pressure telemetry stale while guidance data is current;
- DSKY/restart state correct while a ground-derived comparison is wrong because of RTCC/configuration state.

A single synthetic `lm_guidance_state` object feeding every field would erase these historically important failure modes.

---

# 8. Confidence / evidence boundaries

## DOCUMENTED

- Apollo 13 used MSK 1123.
- Mission-specific Apollo 13 layout and definition page survive.
- The page mixes PGNS/LGC, AGS, radar, control and propulsion information.
- R-567 provides Apollo-13-specific LGC/downlink source data.
- NASA Apollo telemetry tables route named PCM/control/propulsion measurements to 1123.

## PARTIAL

- mission-specific Apollo 13 calibration/routing of the PCM measurements;
- exact AGS Flight Program 7 variable-to-field mapping;
- ground transformations/comparison logic;
- station access/request behavior;
- CRT refresh cadence.

## NOT YET ESTABLISHED

- a complete Apollo-13-specific 1123 parameter dictionary;
- exact field-by-field transport path for every value;
- exact display update timing;
- whether all Apollo-wide 1123 telemetry routing entries were unchanged for LM-7.

---

# 9. Sources

## Mission-specific

- AC Electronics, *Apollo 13 Guidance & Navigation Summary*, ASPO 45, PDF 186–187.
- MIT/MSC R-567 Rev. 8, *LUMINARY 1C Data Links*, March 1970.
- Apollo 13 Flight Crew G&N Dictionary, 25 March 1970 — identified for AGS Flight Program 7 follow-up.

## Apollo-wide routing / continuity

- NASA TN D-7993, *Apollo Experience Report — Engineering and Analysis Mission Support*, 1975, LM Telemetry Data Summary.
- LM instrumentation packet tables preserving Primary MSK routing.

## Repository cross-references

- `029_apollo13_aspo45_direct_inspection.md`
- `032_apollo13_lm_crt_field_provenance.md`
- `034_apollo13_msk1137_non_lgc_telemetry.md`

---

# 10. Next work

1. Extract Apollo 13 G&N Dictionary AGS Flight Program 7 addresses relevant to the 1123 AGS/DEDA section.
2. Find mission-era LM-7 definitions for the clean PCM measurements currently supported only by Apollo-wide routing.
3. Visually verify OCR-damaged RCS telemetry identifiers before recording them.
4. Trace radar state fields into their exact LGC-versus-PCM origins.
5. Build a normalized 1123 inventory only after those mappings are stable enough to avoid encoding ambiguities as facts.
