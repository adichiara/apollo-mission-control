# Apollo MSK 1123 — velocity-row semantics and mixed-source ground format

Date: 2026-09-11  
Status: **REVIEWED-PARTIAL — field meanings and display precision are better constrained; exact Apollo 13 routing remains unresolved.**

## Purpose

Research note 044 separated the principal AGS information paths feeding MSK 1123, but four adjacent velocity-related rows still had incomplete semantic boundaries:

- AGS VEL
- AGS DEL VEL
- AGS ULL
- ACT VEL

This pass uses contemporary/cross-mission AC/Delco display definitions plus a January 1970 MIT Instrumentation Laboratory ground-console figure to tighten what those rows mean without pretending that the exact Apollo 13 Flight Program 7 telemetry source or RTCC routing has been recovered.

---

## 1. Cross-mission display definitions separate the four rows

The Apollo 11 AC Electronics Guidance & Navigation Summary and the Apollo 12 Delco summary define the MSK 1123 rows separately.

| Field | Display meaning in Apollo 11/12 source family | Display format | Units |
|---|---|---:|---|
| **AGS VEL** | Abort Guidance System indicated velocity | `XXXX` | ft/sec |
| **LGC DEL VEL** | PIPA output for a 2-second interval | `XX.X` | ft/sec |
| **AGS DEL VEL** | Abort Guidance System measured velocity | `XX.X` | ft/sec |
| **AGS ULL** | Abort Guidance ullage measurement | `XX.X` | ft/sec |
| **ACT VEL** | Accumulated velocity along thrust | `XX.X` | ft/sec |

The Apollo 12 source is especially useful because its scan resolves the row clearly as **AGS ULL**, avoiding the OCR ambiguity seen in some Apollo 11 text extractions.

### Consequence

These are not interchangeable labels for one velocity quantity.

- **AGS VEL** is the relatively coarse indicated-velocity row.
- **AGS DEL VEL** is explicitly a measured-velocity quantity at tenths of a foot per second.
- **AGS ULL** is specifically an ullage measurement in velocity units, reinforcing the conclusion from note 042 that it is not merely the MU8 counter or an ullage-acquired Boolean.
- **ACT VEL** is explicitly accumulated velocity along thrust and therefore must remain separate from AGS DEL VEL and AGS ULL.
- **LGC DEL VEL** is explicitly tied to a two-second PIPA interval. The two-second interval describes that measurement, not the CRT refresh cadence.

These semantic distinctions constrain the eventual source mapping but do not by themselves identify the Flight Program 7 memory word or ground computation used for each row.

---

## 2. January 1970 MIT report independently preserves the same ground-console format

J. L. Nevins' January 1970 MIT Instrumentation Laboratory report, *Man-Machine Design for the Apollo Navigation, Guidance, and Control System — Revisited*, reproduces a **Typical Data Format for Ground Consoles** as Figure 16(a).

The figure visibly contains:

- display number 1123;
- the header boxes **AEA / LGC / PCM**;
- AGS VEL;
- LGC DELVEL;
- AGS DELVEL;
- AGS ULL;
- ACTVEL;
- the DEDA and DSKY regions;
- the same general guidance/control monitoring layout now seen in the Apollo mission-summary family.

This is important because it is not merely a later retrospective telemetry table. It is a contemporary January 1970 description of Apollo GN&C monitoring that explicitly presents the 1123-style page as a ground-console data format.

The surrounding text states that during powered descent the ground compared guidance-system state vectors and displayed residuals between primary guidance, backup guidance, and ground-tracking-derived quantities. It also describes a ground powered-flight processor using tracking data and Kalman filtering to generate an independent state vector.

### Architecture consequence

The display should continue to be treated as an integrated Mission Control product rather than a screen directly bound to one onboard computer.

The page can legitimately combine:

- AEA/AGS telemetry;
- LGC/PGNS telemetry;
- PCM/instrumentation data;
- ground-derived comparison or transformed values.

This strengthens the source-separation architecture already adopted in notes 032–044.

---

## 3. What the AEA / LGC / PCM header boxes do **not** yet prove

Figure 16(a) clearly shows labeled boxes for **AEA**, **LGC**, and **PCM**.

No source inspected in this pass defines those boxes as dynamic validity lamps, data-good flags, source-selection controls, or simple static headings.

Therefore:

> **Do not implement dynamic AEA/LGC/PCM validity behavior from the graphic alone.**

The source establishes the labels and the composite nature of the page, but the runtime semantics of those header boxes remain unresolved.

---

## 4. Effect on the current AGS source candidates

### AGS VEL

The semantic definition **indicated velocity** remains consistent with VX/VY/VZ as the strongest current AEA source family, but this pass does not establish the exact ground frame, scaling, or FP7 telemetry IDs.

### AGS DEL VEL

The definition **measured velocity** narrows the intended engineering meaning but does not select among the known AEA delta-V layers:

- DVX/DVY/DVZ;
- VD1X/VD1Y/VD1Z;
- DEDA 470–472 VDX/VDY/VDZ.

The exact MSK source remains unresolved.

### AGS ULL

The definition **ullage measurement**, with `XX.X ft/sec` display precision, confirms that the field is a continuous engineering quantity rather than the MU8 counter or an acquired/not-acquired state.

The likely source family remains the AGS sensed-X-axis velocity / thrust-acceleration chain, but the exact quantity and ground scaling still need a controller/RTCC or FP7 source.

### ACT VEL

The definition **accumulated velocity along thrust** establishes a distinct engineering role. It should not be collapsed into AGS DEL VEL or AGS ULL in the eventual parameter dictionary.

---

## 5. Apollo 13 evidence boundary

Apollo 13's own AC Electronics ASPO 45 section directly confirms that MSK 1123 exists in the mission-specific document and preserves the page layout family.

The exact semantic definitions and masks above are being used here as **cross-mission continuity evidence** from Apollo 11/12, not as proof that every Apollo 13 mask or transformation was unchanged.

The Apollo 13 page still requires direct field-by-field transcription before masks are frozen in implementation.

---

## 6. Implementation constraints now justified

The eventual MSK 1123 parameter specification should keep separate columns for at least:

1. field label;
2. historical semantic definition;
3. display mask/precision;
4. spacecraft source class;
5. exact telemetry measurement or onboard variable;
6. ground transformation/calculation;
7. mission-profile applicability;
8. update/validity behavior;
9. evidence status.

This prevents a cross-mission field definition from being mistaken for proof of Apollo 13 routing, and prevents a known telemetry source from being mistaken for proof of the exact CRT calculation.

---

## Sources

### Contemporary Apollo ground-console context

- J. L. Nevins, *Man-Machine Design for the Apollo Navigation, Guidance, and Control System — Revisited: Apollo, A Transition in the Art of Piloting a Vehicle*, MIT Instrumentation Laboratory, January 1970, Figure 16(a), “Typical Data Format for Ground Consoles.”
- Public scan: https://web.mit.edu/digitalapollo/Documents/Chapter7/nevinsrevisited.pdf

### Cross-mission display definitions

- AC Electronics, *Apollo 11 Guidance & Navigation Summary*, ASPO 45 CRT display definitions.
- Public scan: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- Delco/AC Electronics, *Apollo 12 Guidance & Navigation Summary*, MSK 1123 definitions.
- Public scan: https://ibiblio.org/apollo/Documents/apollo12_delco.pdf

### Mission-specific anchor

- AC Electronics, *Apollo 13 Guidance & Navigation Summary*, ASPO 45 CRT Displays; see research notes 029–032 and 035–044.

---

## Next work

1. Directly transcribe the Apollo 13 MSK 1123 velocity rows and masks from the mission-specific ASPO page.
2. Recover the February 1970 LM-7 Table 2.1-7 Flight Program 7 AEA telemetry list.
3. Locate MCC/RTCC/display-processing definitions that select and transform AGS VEL, AGS DEL VEL, AGS ULL, and ACT VEL.
4. Determine the runtime meaning, if any, of the AEA/LGC/PCM header boxes.
5. Keep the velocity rows as separate parameters until their exact source paths are certified.
