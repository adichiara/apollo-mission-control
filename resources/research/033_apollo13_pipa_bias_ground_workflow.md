# Apollo 13 PIPA-bias ground workflow

Date: 2026-09-11  
Status: **REVIEWED-PARTIAL — preflight ground-computation method documented; actual Apollo 13 mission use documented, but the full CRT/RTCC implementation path is not yet reconstructed.**

## Why this note exists

Apollo 13 MSK 1137 defines an attitude-section **BIAS** as a **ground-computed PIPA free-fall bias**, with a related **OCTAL** field for computed LGC PIPA-bias register loads.

Research Note 032 therefore left the calculation itself unresolved.

A February 27, 1970 Lunar Surface Branch note now gives a mission-specific Apollo 13 procedure for computing PIPA bias on the lunar surface. The actual Apollo 13 Mission Operations Report separately confirms that PIPA-bias monitoring and updating were active real-time guidance tasks during the flown mission.

This does not prove that the February surface algorithm is the only algorithm behind every MSK 1137 BIAS presentation. It does establish one intended H-2 ground-computation workflow and the operational significance of the quantity.

---

## Primary / contemporary sources

### 1. 27 February 1970 — “Note of Interest - Pipa Bias Measurements on the Lunar Surface”

Author: **John L. Nelson, GNC Section, LSB**

Public scan in the Lunar Surface Branch “Notes of Interest” compilation:

https://www.ibiblio.org/apollo/Documents/lsb_notes_of_interest_june_1970.pdf

Status for this research pass: **indexed-text inspected; full large PDF was not directly rendered by the web reader.** Treat exact typography/page placement as still requiring visual archival verification.

The note states that Apollo 13 planned:

- PIPA-bias calculations after touchdown for comparison with pre-PDI bias measurements;
- additional measurements during launch preparation to provide FIDO a PGNS delta-V error estimate;
- no lunar-surface PIPA-bias update on Apollo 13 because the procedure lacked real-time experience.

### Documented ground method

The note describes this calculation:

1. take MPAD's value of lunar gravity;
2. use gimbal angles and GUIDO's determination of local-vertical attitude;
3. resolve expected lunar gravity into the LM stable-member axes;
4. obtain measured lunar gravity from PIPA information;
5. difference expected versus measured gravity;
6. treat that difference as PIPA bias.

In schematic form:

```text
MPAD lunar gravity
      +
gimbal angles
      +
GUIDO local-vertical attitude
      ↓
expected gravity in LM stable-member axes
      ↓
difference from PIPA-measured gravity
      ↓
PIPA bias
```

The note says this technique had been applied retrospectively to Apollo 11 and Apollo 12 data and correlated well with in-flight bias measurements.

### Important operational implication

This is not a single-controller/raw-telemetry quantity.

The intended Apollo 13 calculation spans:

- PIPA measurement data;
- gimbal/orientation information;
- GUIDO's attitude determination;
- MPAD/ground reference data;
- a ground calculation;
- a resulting bias used for monitoring and potentially later computer-load preparation.

That is exactly the type of cross-layer provenance MSK 1137's “ground-computed” label implies.

---

## 2. Apollo 13 Mission Operations Report — actual mission evidence

Source:

*Mission Operations Report, Apollo 13*, Flight Control Division, MSC, 28 April 1970.

https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf

### CSM GNC postflight report

Appendix F reports that:

- the CSM Z-axis PIPA bias appeared slightly high before TLI;
- the controller chose **not** to update it because booster-venting acceleration contaminated the measurement and the effect was not significant for TLI monitoring;
- post-TLI measurements were more consistent;
- when the platform was powered for entry, Z-PIPA bias shifted;
- the measured bias of approximately **-0.0547 ft/s²** was updated in the CMC at EI-45 minutes.

This is a useful fidelity example: a measured bias can be deliberately withheld from an onboard update when its measurement context makes it operationally unsuitable.

### LM contingency evidence

Appendix H records that during the late LM/CSM power-up for MCC-7:

- the LGC and IMU were powered;
- PGNS was initialized;
- the **PIPA bias “looked good”** before the team proceeded into alignment and maneuver-planning decisions.

Apollo 13 never reached the planned lunar-surface PIPA-bias procedure, but the mission report confirms that bias assessment remained a real guidance/control concern during the contingency.

---

## Relationship to MSK 1137

### DOCUMENTED

Apollo 13 ASPO 45 defines:

- **BIAS** — ground-computed PIPA free-fall bias;
- **OCTAL** — computed octal loads for the LGC PIPA-bias registers.

The February 27 mission-planning note documents a concrete H-2 ground procedure for deriving PIPA bias on the lunar surface.

### PARTIALLY DOCUMENTED

It is reasonable to treat the following as established inputs/participants for that specific procedure:

- PIPA measurements;
- gimbal angles;
- local-vertical attitude from GUIDO;
- MPAD lunar-gravity reference;
- ground calculation.

### NOT YET DOCUMENTED

Do **not** yet assume:

- that the lunar-surface calculation was the only source of MSK 1137 BIAS values in every mission phase;
- which exact computer/process executed the calculation;
- how the result was routed into the DCS/CRT page;
- the exact update cadence;
- the exact conversion from engineering-unit bias to the displayed OCTAL load;
- whether GUIDO, CONTROL, or another station owned the request/display at each phase.

---

## Simulation consequence

PIPA bias should not be modeled as a static sensor offset that magically appears on a controller screen.

Where this fidelity is implemented, the architecture must be able to represent:

```text
physical accelerometer bias
        ↓
PIPA measurements
        ↓
measurement-context effects / validity
        ↓
ground reference + attitude inputs
        ↓
ground bias estimate
        ↓
controller judgment
        ↓
optional computer-load generation
        ↓
uplink / verification
```

The Apollo 13 pre-TLI example also shows why “latest value” and “best operational estimate” are not necessarily the same thing.

## Next research

1. Find the H-2 ground support/RTCC or MPAD implementation source for this computation.
2. Trace the BIAS engineering value into the ASPO 45 display field and the OCTAL load-generation path.
3. Identify mission rules/procedures governing when a measured bias should be updated versus only monitored.
4. Verify the February 27 note directly from a rendered archival page when an accessible scan/page image is found.
