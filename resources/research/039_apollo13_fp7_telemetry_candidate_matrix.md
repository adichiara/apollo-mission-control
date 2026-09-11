# Apollo 13 FP7 telemetry candidate matrix — 0325 through 0406

Date: 2026-09-11  
Status: **EVIDENCE MATRIX — not a certified Flight Program 7 telemetry table.**

## Purpose

Research note 038 established that both surviving adjacent AGS programs, FP6 and FP8, place their 50-word AEA telemetry block at the same contiguous octal memory range:

**0325–0406**

This matrix compares those two surviving program listings against Apollo 13 mission-specific G&N Dictionary evidence.

It is deliberately called a **candidate matrix**, not the Apollo 13 telemetry table.

### Status meanings

- **Mission-specific meaning verified** — Apollo 13 G&N Dictionary indexed text defines the address/quantity.
- **Continuity candidate** — FP6 and FP8 agree, but no Apollo 13 source has yet been found for the address.
- **Partial** — Apollo 13 source confirms the address but OCR/semantic detail is not yet sufficiently clean.
- **Conflict** — adjacent programs differ; Apollo 13 source governs if available.

## Matrix

| AEA octal address | FP6 symbol | FP8 symbol | Apollo 13 evidence | Status |
|---|---|---|---|---|
| 0325 | RMF | RMF | No direct mission-specific meaning yet | Continuity candidate |
| 0326 | DD | DD | No direct mission-specific meaning yet | Continuity candidate |
| 0327 | CMF | CMF | No direct mission-specific meaning yet | Continuity candidate |
| 0330 | A11T | A11T | No direct mission-specific meaning yet | Continuity candidate |
| 0331 | A12T | A12T | No direct mission-specific meaning yet | Continuity candidate |
| 0332 | A13T | A13T | No direct mission-specific meaning yet | Continuity candidate |
| 0333 | ADST | ADST | No direct mission-specific meaning yet | Continuity candidate |
| 0334 | A31T | A31T | No direct mission-specific meaning yet | Continuity candidate |
| 0335 | A32T | A32T | No direct mission-specific meaning yet | Continuity candidate |
| 0336 | A33T | A33T | No direct mission-specific meaning yet | Continuity candidate |
| 0337 | H | H | Apollo 13 dictionary: LM altitude | Mission-specific meaning verified |
| 0340 | RX | RX | Apollo 13 dictionary: LM X position | Mission-specific meaning verified |
| 0341 | RY | RY | Apollo 13 dictionary: LM Y position | Mission-specific meaning verified |
| 0342 | RZ | RZ | Apollo 13 dictionary: LM Z position | Mission-specific meaning verified |
| 0343 | QL | QL | No indexed Apollo 13 definition recovered yet | Continuity candidate |
| 0344 | RCX | RCX | Apollo 13 dictionary: CSM X position | Mission-specific meaning verified |
| 0345 | RCY | RCY | Apollo 13 dictionary: CSM Y position | Mission-specific meaning verified |
| 0346 | RCZ | RCZ | Apollo 13 dictionary: CSM Z position | Mission-specific meaning verified |
| 0347 | RF | RF | Apollo 13 dictionary: predicted altitude at TIG / predicted OI burnout altitude | Mission-specific meaning verified |
| 0350 | DVX | DVX | No direct indexed definition recovered in this pass | Continuity candidate |
| 0351 | DVY | DVY | No direct indexed definition recovered in this pass | Continuity candidate |
| 0352 | DVZ | DVZ | No direct indexed definition recovered in this pass | Continuity candidate |
| 0353 | TA2 | TA2 | No direct indexed definition recovered in this pass | Continuity candidate |
| 0354 | DAX | DAX | No direct indexed definition recovered in this pass | Continuity candidate |
| 0355 | DAY | DAY | No direct indexed definition recovered in this pass | Continuity candidate |
| 0356 | DAZ | DAZ | No direct indexed definition recovered in this pass | Continuity candidate |
| 0357 | TBO | TBO | Apollo 13 dictionary: time to burnout | Mission-specific meaning verified |
| 0360 | VX | VX | Apollo 13 dictionary: LM X velocity | Mission-specific meaning verified |
| 0361 | VY | VY | Apollo 13 dictionary: LM Y velocity | Mission-specific meaning verified |
| 0362 | VZ | VZ | Apollo 13 dictionary: LM Z velocity | Mission-specific meaning verified |
| 0363 | MU8S12 | MU8S12 | No direct mission-specific meaning yet | Continuity candidate |
| 0364 | VCX | VCX | Apollo 13 dictionary: CSM X velocity | Mission-specific meaning verified |
| 0365 | VCY | VCY | Apollo 13 dictionary: CSM Y velocity | Mission-specific meaning verified |
| 0366 | VCZ | VCZ | Apollo 13 dictionary: CSM Z velocity | Mission-specific meaning verified |
| 0367 | HDOT | HDOT | Apollo 13 dictionary: LM altitude rate | Mission-specific meaning verified |
| 0370 | VG | VG | No direct indexed definition at 370 recovered yet | Continuity candidate |
| 0371 | VT | VF | Apollo 13 dictionary: mode-dependent maneuver ΔV (CDH / direct transfer + braking) | Mission-specific meaning verified; adjacent programs differ |
| 0372 | TA0 | TA0 | No direct indexed definition recovered in this pass | Continuity candidate |
| 0373 | TIG | TIG | Apollo 13 dictionary: AGS TIG for CSI/CDH/TPI/TPM | Mission-specific meaning verified |
| 0374 | A11BD | A11BD | No direct indexed definition recovered in this pass | Continuity candidate |
| 0375 | A12BD | A12BD | No direct indexed definition recovered in this pass | Continuity candidate |
| 0376 | A13BD | A13BD | No direct indexed definition recovered in this pass | Continuity candidate |
| 0377 | TA1 | TA1 | Apollo 13 dictionary: AGS computer time | Mission-specific meaning verified |
| 0400 | S0 | S0 | Apollo 13 dictionary: AGS function selector | Mission-specific meaning verified |
| 0401 | DISC1C | DISC1C | No direct indexed definition recovered in this pass | Continuity candidate |
| 0402 | Q1DEDA | Q1DEDA | Apollo 13 dictionary: mode-dependent coelliptic/TPI altitude quantity | Mission-specific meaning verified; exact OCR wording needs visual check |
| 0403 | QLTELE | QLTELE | Apollo 13 dictionary exposes an address-403 altitude/orbit quantity; exact OCR wording needs visual check | Mission-specific address verified; semantic wording partial |
| 0404 | VD1X | VD1X | Apollo 13 dictionary: ΔVX reset word; 470 readout | Mission-specific meaning verified |
| 0405 | VD1Y | VD1Y | Apollo 13 dictionary: ΔVY reset word; 471 readout | Mission-specific meaning verified |
| 0406 | VD1Z | VD1Z | Apollo 13 dictionary: ΔVZ reset word; 472 readout | Mission-specific meaning verified |

## Quantitative status

- Total candidate positions: **50**
- Adjacent-program symbol agreement: **49/50**
- Direct/partial Apollo 13 address evidence currently captured here: **24/50**
- Clear adjacent-program symbol conflict: **1/50** — address 0371 (`VT` in FP6, `VF` in FP8)

The 49/50 agreement describes **symbols in the compared source listings**, not guaranteed semantic identity. Even a stable symbol can have revised logic, scaling, or use.

## Important findings

### 1. The telemetry block is structurally very stable

The same 50 memory positions bracketed by START/END TELEMETRY LIST appear in FP6 and FP8.

That makes the 0325–0406 range a strong structural continuity candidate for FP7.

### 2. Apollo 13 directly verifies nearly half the address meanings already

The mission-specific dictionary independently confirms many navigation/time/control values inside this region.

This is especially useful because it allows the project to populate a future FP7 table from Apollo 13 evidence rather than merely interpolating between FP6 and FP8.

### 3. Address 0371 proves why interpolation must remain evidence-based

FP6 and FP8 use different symbols at 0371.

Apollo 13's own dictionary defines the mission's semantics, so the mission-specific source resolves the ambiguity for operational meaning without requiring a speculative choice between adjacent programs.

### 4. Telemetry membership is still not fully certified

Even though FP6 and FP8 both use this address region, the exact February 1970 LM-7 Table 2.1-7 remains the authority for Apollo 13 telemetry membership and ID ordering.

Until it is recovered:

- do not mark all 50 as flight-certified FP7 telemetry words;
- do not derive the 6-bit telemetry ID solely from address arithmetic;
- do not infer scaling for unresolved addresses from FP6/FP8 without explicit qualification.

## Next work

1. Query Apollo 13 indexed sources for the unresolved addresses.
2. Locate Table 2.1-7 in the February 1970 LM-7 handbook.
3. Add scaling/reference-frame metadata for mission-specific verified entries.
4. Map verified AGS telemetry quantities to MSK 1123 fields.
5. Track any RTCC transformation separately from the raw AEA telemetry value.

## Sources

- FP6 source listing: https://www.ibiblio.org/apollo/listings/FP6/FP6.aea.html
- FP8 source listing: https://www.ibiblio.org/apollo/listings/FP8/FP8.aea.html
- Apollo 13 G&N Dictionary — NASA indexed text / Apollo 13 Flight Journal archive
- Apollo Operations Handbook, LM-7 and Subsequent, 1 February 1970 — Table 2.1-7 identified but not yet directly extracted
