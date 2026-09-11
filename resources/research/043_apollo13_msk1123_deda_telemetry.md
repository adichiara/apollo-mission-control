# Apollo 13 MSK 1123 — DEDA telemetry provenance

Date: 2026-09-11  
Status: **STRONG CONTINUITY / APOLLO-13 DISPLAY FAMILY CONFIRMED — AEA telemetry semantics are explicit; exact Apollo 13 CRT masks/labels still need direct transcription.**

## Purpose

Apollo 13 MSK 1123 includes an AGS/DEDA section.

The AEA telemetry architecture makes this section unusually reconstructable because the telemetry block itself carries the state of the DEDA interaction.

This note traces the crew DEDA interface into AEA telemetry and constrains the corresponding Mission Control display path.

---

# 1. The AEA telemetry block explicitly carries DEDA state

The Flight Program 6 AGS Operating Manual gives the first telemetry words as:

| Telemetry word | ID code | AEA quantity | Meaning |
|---|---:|---|---|
| 1 | 01 | readout-mode flag | sign bit set when DEDA processing is in readout mode |
| 2 | 02 | DD | most recent DEDA data word in computer units |
| 3 | 03 | clear-mode flag | sign bit set when DEDA processing is in clear mode |
| 7 | 07 | ADST | octal address associated with the most recent DEDA communication |

The surviving FP6 and FP8 source listings place these at:

- **0325 — RMF** — readout mode flag
- **0326 — DD** — DEDA data
- **0327 — CMF** — clear mode flag
- **0333 — ADST** — DEDA address

The same basic arrangement appears in both adjacent AGS flight programs.

### Important architecture fact

The ground does not need to infer DEDA state from the crew's physical display.

The AEA itself telemeters enough information to reconstruct:

```text
selected address
current/most-recent data
readout mode
clear mode
```

---

# 2. DEDA and telemetry remain different interfaces

The DEDA is the astronaut's local interface to the AEA.

The AEA telemetry block independently sends DEDA-related state to the ground.

Conceptually:

```text
crew keypress / DEDA
        ↓
AEA DEDA processing
        ├────────────→ DEDA physical display
        │
        └────────────→ RMF / DD / CMF / ADST
                         ↓
                    AEA telemetry
                         ↓
                    ground processing
                         ↓
                    MCC CRT product
```

Therefore a Mission Control DEDA-status display should not be modeled as a direct copy of a rendered crew display. It is a ground reconstruction from AEA state.

---

# 3. Source-code behavior supports the meanings

The surviving AGS source code independently shows the same variables in DEDA processing.

Examples:

- readout entry stores the readout-mode state in **RMF**;
- entering an address stores it into **ADST**;
- **DD** is cleared/loaded as DEDA data is processed;
- **CMF** tracks clear mode.

This is stronger than a static telemetry table because it shows that these are live DEDA-processing variables.

---

# 4. Mission Control display evidence

The Apollo 13 ASPO 45 source directly confirms that **MSK 1123 contains AGS DEDA information**.

The earlier AC Electronics display family exposes a DEDA block with labels corresponding to:

- address;
- readout;
- clear;
- data/register content.

That earlier layout is useful continuity evidence, but the exact Apollo 13 masks/labels must come from the mission-specific PDF 186–187 before the final renderer is frozen.

### What is safe now

It is safe to define the historical source chain as:

```text
AEA DEDA-processing state
   ↓
RMF / DD / CMF / ADST telemetry
   ↓
ground decoding
   ↓
MSK 1123 DEDA-status block
```

### What is not yet safe

Do not yet freeze:

- exact Apollo 13 label abbreviations;
- decimal/octal formatting masks;
- sign handling;
- which portions of DD are reformatted versus shown in computer units;
- exact refresh cadence;
- whether additional DEDA flags/fields are included from other telemetry words.

---

# 5. DEDA word formatting is not identical to telemetry formatting

The AGS Operating Manual distinguishes:

## AEA telemetry word

24 bits:

- 6-bit telemetry ID;
- 18-bit AEA computer word.

## Complete DEDA display word

36 bits:

- three 4-bit groups for the address;
- one 4-bit group for data sign;
- five 4-bit groups for displayed data.

Therefore the ground cannot simply place the raw 24-bit AEA telemetry word onto the CRT and call it a DEDA display.

Ground software must interpret the telemetered AEA values and construct a controller-readable representation.

---

# 6. DEDA display cadence versus telemetry cadence

General AGS documentation establishes:

- AEA telemetry: 50-word block repeated every second;
- DEDA user-interface updates have their own timing;
- the AGS executive periodically services DEDA processing separately from telemetry.

Therefore:

```text
crew DEDA display timing
≠
AEA telemetry timing
≠
MCC CRT refresh timing
```

A ground DEDA-status block can legitimately lag, differ from, or momentarily represent a different processing state than the astronaut's local display.

---

# 7. Failure modes enabled by the historical architecture

A high-fidelity simulator can later distinguish:

### DEDA hardware/interface issue

Crew cannot read/enter normally, while AEA internal state may still be valid.

### AEA DEDA-processing issue

RMF/DD/CMF/ADST themselves can be wrong or stale.

### Telemetry issue

Crew DEDA is correct but Mission Control cannot see current DEDA state.

### Ground-decoding/display issue

Raw AEA telemetry is valid but the MCC DEDA block is wrong.

These are separate from guidance-state errors.

---

# 8. Relationship to actual Apollo 13 procedures

Apollo 13 contingency procedures repeatedly use DEDA addresses such as:

- 400 selector modes;
- 404/405/406 delta-V resets;
- 470/471/472 measured delta-V readouts.

Because DEDA address/state is itself telemetered, Mission Control could in principle monitor whether the crew was in the expected AGS interaction state while guiding them through these procedures.

The exact Apollo 13 operational use of the MSK 1123 DEDA block during those specific calls has not yet been established from loop transcripts.

Do not claim real-time controller verification of every crew keystroke without that evidence.

---

# 9. Evidence status

## DOCUMENTED / STRONG CONTINUITY

- AEA telemetry explicitly includes:
  - readout-mode flag;
  - DEDA data;
  - clear-mode flag;
  - DEDA address.
- FP6 and FP8 source listings preserve those variables at the same telemetry-block locations.
- Apollo 13 MSK 1123 contains AGS DEDA information.
- Apollo 13 actually used DEDA extensively during contingency guidance procedures.

## PARTIAL

- exact Apollo 13 field labels/masks for the DEDA block;
- formatting from AEA computer units into CRT representation;
- relationship of the DEDA block to specific GUIDO/CONTROL console workflow;
- refresh behavior.

## NOT YET ESTABLISHED

- whether Apollo 13 Flight Program 7 altered any of RMF/DD/CMF/ADST semantics;
- exact February 1970 Table 2.1-7 telemetry IDs;
- whether MCC displayed additional DEDA-processing flags beyond those four basic telemetry items.

---

# 10. Sources

### AGS telemetry

- *LM Abort Guidance System Flight Program 6 Operating Manual*, Table 5.2:
  - telemetry word 1 — DEDA readout mode;
  - word 2 — DEDA data;
  - word 3 — DEDA clear mode;
  - word 7 — DEDA address.
- FP6 and FP8 assembly listings — RMF/DD/CMF/ADST memory locations and DEDA processing code.

### Apollo 13 display

- AC Electronics, *Apollo 13 Guidance & Navigation Summary*, ASPO 45:
  - PDF 186 — MSK 1123 layout;
  - PDF 187 — definitions.
- Research note 029 — direct mission-specific inspection.

### Apollo 13 operational use

- Apollo 13 G&N Dictionary and mission voice records for DEDA guidance procedures.

---

# 11. Next work

1. Re-open/render Apollo 13 PDF 186–187 and transcribe the exact DEDA block masks/labels into a normalized 1123 inventory.
2. Recover the LM-7 FP7 Table 2.1-7 and certify RMF/DD/CMF/ADST telemetry IDs.
3. Determine ground formatting rules for DD and ADST.
4. Search GUIDO/CONTROL loops for explicit use of the ground DEDA-status block during Apollo 13 procedures.
