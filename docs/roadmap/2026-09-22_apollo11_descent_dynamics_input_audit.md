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

## NARA/MSC records-series recovery path

A primary **NASA-MSC Standard Form 135-A records-transmittal index**, prepared 26 Oct 1971 and now scanned in the NARA Southwest overflow collection, identifies the records group containing Apollo 11 documentation. Page 17 lists **MSC-69-FM-156** with the Apollo 11 spacecraft dispersion-analysis series, including **Vol. IV — Descent and Ascent Dispersion Analysis, Part 1 — Lunar Descent**, under **3751-33 / WRCS 25, Item 1a**.

The same primary transmittal supplies a second, more directly useful CONTROL recovery target on page 15: **Operational Calibration Curves, Vol. II — Calibration Curves for LM-5, dated 12 June 1969**. A page-image inspection now makes the archival request substantially more specific: the transmittal is **Federal Records Center accession 72-A-1116, Record Group 255**, and the Apollo 11 launch-data page assigns the calibration-curves group to **agency box 71**. The FRC-only box field visibly carries **3751-30**, but that locator is struck/annotated on the scan; preserve it as a legacy locator rather than silently treating it as the canonical current box number. The accession/RG/agency-box combination is the preferred retrieval key.

This predates launch and is explicitly vehicle-specific. Its contents are not present in the index, so no calibration quantity or DPS force mapping is claimed. Because an operational-calibration volume is a plausible source for converting telemetry/control indications to engineering units, recovering this exact LM-5 volume now precedes further generic calibration searching.

This is archival provenance rather than numerical dynamics evidence. The transmittal does **not** show 69-FMZ2-149 in the scanned index, and no claim is made that memo 149 is in box 3751-33 or agency box 71.

There is also a bibliographic distinction that must remain explicit: the later H-2 lunar-descent document cites **69-FM-156, “G Mission Lunar Descent Dispersion Analysis,” 10 Jun 1969**, while Purdue catalogs **Internal Note 69-FM-156, Apollo 11 (Mission G) Spacecraft Dispersion Analysis, Vol. IV, Part 1 Lunar Descent (Addendum), 2 Jul 1969**. Treat the 10 June base analysis and 2 July addendum as related but distinct states until title pages are recovered.

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

1. Request/recover **Operational Calibration Curves, Vol. II — Calibration Curves for LM-5 (12 Jun 1969)** using **FRC accession 72-A-1116 / RG 255 / agency box 71**; retain struck/annotated `3751-30` only as a secondary legacy locator. Inspect the actual volume for DPS/throttle/pressure/control-to-engineering-unit calibration. Do not infer that it contains a thrust curve from its title alone.
2. Recover **John P. Mayer, MSC/MPAD memorandum 69-FMZ2-149 (5 Jun 1969)** and inspect the actual document for FTP-force/calibration values and assumptions.
3. Recover the two **8 July 1969 Armstrong MSA 5 throttle-down dispersion items** and inspect actual content for engine-dispersion, LM-weight, PDI-state, and throttle-down relationships.
4. Recover title pages/content for the **69-FM-156 base analysis and 2 July addendum**.
5. Continue pursuit of the underlying **Apollo 11 / LM-5 DPS Final Flight Evaluation contractor report** and LM-5 engine acceptance/performance records.
6. Retain **LMA790-3-LM page 2.3-25 / Table 2.3-1** as a named blocked target until a legible primary page image or clean LEP is recovered.
7. Continue Mission-G PDI-mass recovery only from explicitly event-identified primary records.

## Evidence status

**PARTIALLY DOCUMENTED.** Primary NASA-MSC records metadata establishes a mission-specific **LM-5 Operational Calibration Curves Volume II dated 12 June 1969** and now narrows its archival location to **FRC accession 72-A-1116 / RG 255 / agency box 71**; its contents remain **BLOCKED ON DOCUMENT RECOVERY** and no DPS calibration is inferred. The 5 June FTP study is identified by author, organization, title, date, and memo number, but its contents also remain blocked. The two 8 July companion studies and 69-FM-156 base/addendum content remain blocked on archival recovery. Page 2.3-25, Supplement 7 content/identifiers, exact LM-5 force calibration/delivered performance, PDI mass, and TRW Volume II remain unresolved/blocked as documented.