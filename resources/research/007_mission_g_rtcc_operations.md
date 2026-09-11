# Research Note 007 — Mission G RTCC Operations

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Source

**Project Apollo 500 RTCC Operations Support Plan for Mission G**  
MSC Internal Note No. 69-FS-2  
Flight Support Division, Flight Software Branch  
Manned Spacecraft Center  
April 1969

https://www.ibiblio.org/apollo/Documents/RTCC%20Operations%20Support%20Plan%20for%20Mission%20G.pdf

Mission G is Apollo 11.

## Why this source matters

Unlike later generic Apollo Experience Reports, this is a mission-specific preflight ground-operations document for Apollo 11.

It provides direct evidence about the RTCC procedures supporting the mission.

## Findings

### Controller/ground inputs are explicit system inputs

The document states that during RTCC machine restart or initialization, the following were inhibited:

- PBI inputs
- MED inputs
- display requests
- other switches

This confirms that these were active interfaces into the operational computing system.

### Telemetry-reference displays are identified by MSK number

Table 2.6-2 provides a list of computer telemetry-reference displays, including:

- 1616 — APOLLO SMEK MSG LOG (SLV/LM)
- 1617 — APOLLO SMEK MSG LOG (CSM)
- 1621 — MED INPUTS (CSM/AGC SLV AGS AMD)
- 1625 — MED INPUTS (LM/LGC)
- 2001 — TLM STATUS DISPLAY PAGE 1
- 2002 — TLM STATUS DISPLAY PAGE 2
- 2009–2018 — telemetry center/reference/message displays for SIC, CSM, IU, AGC, SII, LM, LGC, AGS, AMD

### Mission-specific MSK usage

A procedure calls for generation of the **Landmark Acquisition Display (MSK 1508)** with specified input parameters.

This supports preserving historical display numbers when known.

### Documentation hierarchy inside RTCC operations

The plan names several reference-document classes, including:

- PHO-TR170A — basic program requirements
- PHO-TR170B — detailed television display formats
- PHO-TR155 — MCC hardware-configuration requirements for DDDs/CIM inputs
- Data Acquisition Plan Annex B — Telemetry Data Formats Control Handbook
- calibration printouts
- parameter numbers for limit MEDs
- Flight Controllers Operations Handbook
- D/TV telemetry-reference displays

This gives the project a concrete research chain for reconstructing individual operational displays.

### Hard-copy verification

RTCC procedures include verification of transmissions using:

- online indications
- teletype hard copy

This is a mission-specific Apollo 11 example of paper output being part of operational verification.

## Research implications

Highest-priority missing sources now include:

1. PHO-TR170A
2. PHO-TR170B
3. Apollo-11-era revision of PHO-TR155 if it survives
4. Mission G Flight Controllers Operations Handbook
5. Mission G Flight Controller Console Handbooks
6. Data Acquisition Plan Annex B / Telemetry Data Formats Control Handbook

If these can be located, controller display reconstruction may be substantially more exact than initially expected.

## Caution

An MSK number appearing in the RTCC support plan does not by itself identify which MOCR controller normally used that display.

Station ownership/use must be established separately.
