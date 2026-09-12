# Apollo 13 / LM-7 AEA telemetry word list — recovery and evidence bounds

Date: 2026-09-11  
Status: **REVIEWED-PARTIAL — Table 2.1-7 structure and engineering definitions recovered from contemporary handbook copies; exact Apollo 13 flight-edition line-by-line certification remains bounded by source-version access.**

## Purpose

Research notes 037–045 identified the missing **Table 2.1-7, Abort Electronics Assembly — Telemetry Word List** as the principal gap between known Flight Program 7 / AEA variables and the AGS portion of MSK 1123.

This pass recovers the table's telemetry-word structure and engineering descriptions from contemporary Apollo Operations Handbook copies while preserving the distinction between:

1. the exact Apollo 13 **LM 7 and Subsequent** handbook edition dated 1 February 1970;
2. a publicly searchable **LM 10 and Subsequent** Volume I copy carrying the same 1 February 1970 basic date but a 15 June 1970 change date; and
3. adjacent-program AGS source/code evidence.

The result materially narrows the field-to-source problem, but it does **not** justify assigning a specific telemetry word to an MSK 1123 row without MCC/RTCC/display-routing evidence.

---

## 1. Mission-specific handbook anchor

The Apollo 13 Flight Journal indexes:

- **LMA790-3-LM, Apollo Operations Handbook, Lunar Module LM 7 and Subsequent, Volume I — Subsystems Data**;
- change date **1 February 1970**;
- Table **2.1-7 — Abort Electronics Assembly - Telemetry Word List** in the GN&C section.

A searchable index of the LM-7 edition also exposes the table title in the list of tables.

The high-resolution LM-7 scan is too large for the current web PDF reader, so this pass does not claim direct page-image verification of every LM-7 table row.

---

## 2. Searchable contemporary copy exposes the full table structure

A searchable LMA790-3-LM **LM 10 and Subsequent** Volume I copy has:

- **Basic Date:** 1 February 1970;
- **Change Date:** 15 June 1970;
- Table **2.1-7 — Abort Electronics Assembly - Telemetry Word List**;
- pages **2.1-97 through 2.1-98**.

This is a later changed copy and therefore is **continuity evidence**, not by itself proof that every row was identical in Apollo 13's April 1970 LM-7 flight configuration.

Nevertheless, it recovers the engineering structure that earlier notes had only reconstructed from FP6/FP8 source listings.

---

## 3. High-value telemetry entries

### Present LM inertial velocity

Telemetry words **28–30**, ID codes **34–36 octal**, are the three components of the **present LM inertial velocity vector**.

The table gives:

- lunar binary scaling: 13;
- least-significant-bit weight: 2^-2 ft/s;
- units: ft/s.

This strongly reinforces the existing candidate relationship:

```text
AEA present LM inertial velocity
        ↓
telemetry words 28–30 / IDs 34–36
        ↓
ground processing
        ↓
MSK 1123 AGS VEL candidate
```

It does not yet establish whether the CRT displays those components directly or after a frame transformation.

### Compensated 20-ms incremental velocity

Telemetry words **20–22**, ID codes **24–26 octal**, are compensated incremental velocity components accumulated per **20 milliseconds** along the LM X/Y/Z body axes by the corresponding accelerometers.

The table gives:

- lunar binary scaling: 3;
- least-significant-bit weight: 2^-14 ft/s;
- units: ft/s.

This confirms a distinct high-resolution incremental-velocity family in the transmitted AEA data.

### Ullage counter

Telemetry word **31**, ID code **37 octal**, is explicitly an **ullage counter for telemetry**.

It is a count/status quantity rather than a velocity engineering value.

This independently confirms the conclusion in research note 042:

> **MSK 1123 AGS ULL, which is displayed in ft/s, cannot simply be a direct rendering of the telemetry ullage counter.**

### Sensed body-axis velocity increments

The end of the table, telemetry words **48–50**, ID codes **60–62 octal**, describes a second family of **sensed velocity increments along the LM body axes**.

The table gives:

- lunar binary scaling: 13;
- least-significant-bit weight: 2^-2 ft/s;
- units: ft/s.

The searchable scan's rowspan/OCR presentation obscures individual equation-symbol formatting, so this note records the three-word vector family rather than inventing symbol text for each row.

---

## 4. Other table entries that corroborate the current provenance model

The same table includes:

- DEDA readout-mode flag;
- most recent DEDA data word;
- DEDA clear-mode flag;
- DEDA address;
- six direction cosines from rows 1 and 3 of the attitude matrix;
- LM altitude;
- LM inertial position;
- CSM inertial position;
- predicted LM radius;
- least- and most-significant AGS absolute-time portions;
- compensated incremental rotations about body axes;
- time to LM engine burnout;
- CSM inertial velocity;
- LM altitude rate;
- velocity-to-be-gained / rendezvous quantities;
- desired LM X-body pointing direction;
- function selector;
- discrete word one;
- orbit/perifocus quantities.

This strongly matches the architecture reconstructed from FP6/FP8 source listings and the Apollo 13 G&N Dictionary.

---

## 5. What is now resolved

### Strongly supported

- The AEA ground telemetry is a structured 50-word product with octal telemetry IDs.
- Present LM inertial velocity is a distinct three-component telemetry product.
- Compensated 20-ms body-axis incremental velocity is a separate three-component product.
- A second sensed body-axis velocity-increment family appears at the end of the telemetry list.
- The ullage counter is separately telemetered and dimensionless.
- DEDA state and attitude direction cosines are explicitly part of the telemetry list.

### Consequence for MSK 1123

The velocity-related CRT rows must **not** be collapsed into one generic AGS velocity value. At minimum, the historical source architecture distinguishes:

1. present inertial velocity;
2. compensated short-interval incremental velocity;
3. sensed body-axis velocity increments;
4. an ullage counter/status quantity;
5. crew-facing DEDA delta-V values;
6. any ground-computed or accumulated CRT products.

---

## 6. What remains unresolved

This pass does **not** establish:

- that every row of the 15 June 1970 changed LM-10 table was unchanged from the Apollo 13 LM-7 flight edition;
- the exact Flight Program 7 memory address behind every telemetry ID;
- which of the two transmitted incremental-velocity families feeds **AGS DEL VEL**;
- the exact engineering quantity used for **AGS ULL**;
- whether **ACT VEL** is calculated from AEA telemetry, another spacecraft source, or a ground accumulator;
- frame transformations applied to **AGS VEL**;
- CRT refresh/validity behavior;
- runtime semantics of the AEA/LGC/PCM header boxes.

Those remain MCC/RTCC/display-processing questions.

---

## 7. Source-version rule for implementation

For Apollo 13 implementation:

- treat the **LM-7 handbook** as the mission-specific authority when its pages can be directly verified;
- use the LM-10 searchable table as a **same-basic-date / later-change continuity source**;
- use the Apollo 13 G&N Dictionary for mission-specific Flight Program 7 variable/address semantics;
- use FP6/FP8 source listings only as adjacent-program continuity evidence;
- do not promote a telemetry-word-to-MSK-field mapping until a controller/display/RTCC source supports it.

---

## Sources

### Mission-specific anchor

- *Apollo Operations Handbook, Lunar Module LM 7 and Subsequent, Volume I — Subsystems Data*, LMA790-3-LM, 1 February 1970.
- Apollo 13 Flight Journal document index: https://apollojournals.org/afj/ap13fj/a13-documents.html
- Search-index copy of the LM-7 edition: https://www.scribd.com/document/942911911/a13-Lm-Aoh-v1-Lm7-Subs-300ppi

### Contemporary searchable continuity copy

- *Apollo Operations Handbook, Lunar Module LM 10 and Subsequent, Volume I — Subsystems Data*, LMA790-3-LM, Basic Date 1 February 1970, Change Date 15 June 1970, Table 2.1-7, pp. 2.1-97–2.1-98.
- Searchable scan: https://www.ibiblio.org/apollo/Documents/LMA790-3-LM10-ApolloOperationsHandbookLunarModuleLM10AndSubsequent-Volume1-SubsystemsData-SearchableText.pdf
- Original scan: https://www.ibiblio.org/apollo/Documents/LMA790-3-LM10-ApolloOperationsHandbookLunarModuleLM10AndSubsequent-Volume1-SubsystemsData.pdf
- Independent ALSJ mirror: https://apollojournals.org/alsj/LM10HandbookVol1.pdf

### Cross-checks already in the repository

- Apollo 13 G&N Dictionary, 25 March 1970.
- Flight Program 6 and Flight Program 8 AGS source listings.
- Research notes 037–045.

---

## Next work

1. Recover/directly inspect the LM-7 page image for Table 2.1-7 and compare it row-by-row with the June-changed searchable table.
2. Locate MCC/RTCC/display-format documentation that maps telemetry IDs into MSK 1123.
3. Resolve **AGS DEL VEL** selection between the distinct incremental-velocity families.
4. Resolve the ground calculation for **AGS ULL** and **ACT VEL**.
5. Keep GUIDO and CONTROL at maturity B until the controller-facing routing and transformations are documented.
