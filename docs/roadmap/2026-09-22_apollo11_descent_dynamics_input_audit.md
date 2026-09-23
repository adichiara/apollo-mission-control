# Roadmap continuation — Apollo 11 descent dynamics input audit

Date: 2026-09-22
Parent: `docs/roadmap/2026-09-22_apollo11_descent_continuous_trajectory_boundary.md`

## Bounded question

Which generic DPS/translational inputs can be tied to primary Apollo 11 evidence without promoting design or later-vehicle values to LM-5 delivered-flight truth?

## Established primary boundaries

- Apollo 11 Press Kit: **9,870 lbf** maximum-rated DPS thrust, mission-specific preflight specification.
- Apollo 11 Mission Report: LM-5 advances to **FTP about 26 s after PDI**; postflight throttle/pressure histories; named LM masses at separation, DOI ignition, DOI cutoff, and landing.
- NASA TN D-7143: **10,500-lbf** maximum-rated design requirement and design Isp envelope; not LM-5 delivered performance.
- LMA790-3-LM figure 2.2-62 on **page 2.2-215, Change Date 15 June 1969**, labels the TTCA throttle hard-stop position **92.5% THRUST** and is directly within the LM-5 handbook state.
- Later LMA790-3-LM Volume I: **9,870-lbf fixed-full-throttle** mature-design semantics; later-effective force statements cannot silently become LM-5 force calibration.

## DPS handbook target narrowed

The September 1969 LM-6-and-subsequent Volume-I material identifies **§2.3.5, Descent Propulsion Section Performance and Design Data**, beginning at **page 2.3-25**, with **Table 2.3-1** at that location. The available primary LEP rendering is too OCR-corrupted around the 2.3 ranges to assign page 2.3-25's issue date without guessing. Therefore page 2.3-25 is **BLOCKED ON LEGIBLE PRIMARY PAGE-IMAGE / LEP RECOVERY**.

## Supplement 7 recovery boundary

Later NASA mission-report supplement tables provide positive primary evidence that **Apollo 11 Mission Report Supplement 7, _Descent Propulsion System Final Flight Evaluation_, was published in September 1970**. A bounded current NASA/NTRS catalog pass did not recover its public record. Apollo 10 primary evidence shows its corresponding MSC Supplement 7 wraps TRW **11176-H314-R0-00**, so search for an earlier Apollo 11 / LM-5 contractor report without interpolating a report number.

## LM-5 FTP archival lead now identified by memo number

Purdue MSA 5 identifies **“Effect of fixed throttle point thrust on the time from loss of radial guidance control to DPS throttle-down,” 5 June 1969**. A primary NASA/MSC mission-techniques document independently cites that exact title as **John P. Mayer, Manned Spacecraft Center/Mission Planning and Analysis Division, NASA MSC Memorandum 69-FMZ2-149, 5 June 1969**. The OCR branch code is retained as `FMZ2` pending a clean title-page recovery.

This changes the recovery strategy: search **69-FMZ2-149 + Mayer + title** directly before further broad FTP searches. The citation identifies the document but does not expose its result, so no numerical FTP calibration is claimed.

Two companion Purdue items remain active:

- **“Effects of DPS engine dispersions and LM weight on throttle-down time”** — 8 Jul 1969, File 2, Item 20.
- **“Effects of known dispersions at PDI on throttle-down time”** — 8 Jul 1969, File 2, Item 21.

Their titles establish analyzed variables only; no numerical values are inferred.

## PDI mass

Exact Mission-G PDI mass remains unresolved; secondary/reconstructed event relabelings remain rejected.

## Model decisions

| Model input | Status | Decision |
| --- | --- | --- |
| `thrust_n` / `end_thrust_n` | Apollo 11 9,870-lbf preflight specification; LM-5 FTP timing; LM-5-effective 92.5-percent control hard stop; exact LM-5 force mapping absent | Keep caller supplied; no exact LM-5 conversion |
| `specific_impulse_s` | Design requirement only; no LM-5 flight-effective history | Keep caller supplied |
| `mass_kg` | Named event masses documented; PDI absent | Keep PDI mass unresolved |
| burn duration | 756.3 s documented | Historical checkpoint |
| continuous trajectory | Reconstruction methodology documented; NAT listing unrecovered | Keep RECONSTRUCTED |

## D-022 result

No D-022 closure is claimed for PDI mass, delivered thrust, FTP force calibration, or flight-effective Isp.

## Next

1. Recover **John P. Mayer, MSC/MPAD memorandum 69-FMZ2-149 (5 Jun 1969)** and inspect the actual document for FTP-force/calibration values and assumptions.
2. Recover the two **8 July 1969 Armstrong MSA 5 throttle-down dispersion items** and inspect actual content for engine-dispersion, LM-weight, PDI-state, and throttle-down relationships.
3. Continue pursuit of the underlying **Apollo 11 / LM-5 DPS Final Flight Evaluation contractor report**.
4. Search LM-5 engine acceptance/performance records for delivered thrust/Isp.
5. Retain **LMA790-3-LM page 2.3-25 / Table 2.3-1** as a named blocked target until a legible primary page image or clean LEP is recovered.
6. Continue Mission-G PDI-mass recovery only from explicitly event-identified primary records.

## Evidence status

**PARTIALLY DOCUMENTED.** The 5 June FTP study is now identified by author, organization, title, date, and memo number from a primary NASA/MSC reference list, materially narrowing archival recovery. Its contents remain **BLOCKED ON DOCUMENT RECOVERY**. The two 8 July companion studies remain blocked on archival item recovery. Page 2.3-25, Supplement 7 content/identifiers, exact LM-5 force calibration/delivered performance, PDI mass, and TRW Volume II remain unresolved/blocked as documented.