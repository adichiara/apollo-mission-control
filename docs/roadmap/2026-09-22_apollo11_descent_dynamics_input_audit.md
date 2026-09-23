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

Later NASA mission-report supplement tables provide positive primary evidence that **Apollo 11 Mission Report Supplement 7, _Descent Propulsion System Final Flight Evaluation_, was published in September 1970**. A bounded current NASA/NTRS catalog pass did not recover its public record.

Primary Apollo 10 evidence now supplies a stronger recovery model. Apollo 10 Mission Report Supplement 7 is an MSC wrapper around the earlier TRW project technical report **11176-H314-R0-00**, _Apollo 10 LM-4 Descent Propulsion System Final Flight Evaluation_, dated **8 August 1969**, under **NAS 9-8166**. The December 1969 supplement retains the contractor report's title page and number while identifying the package as Supplement 7 to `MSC-00126`.

This changes the highest-value Apollo 11 retrieval target. Search not only for the September-1970 MSC supplement wrapper, but for an earlier **Apollo 11 / LM-5 Descent Propulsion System Final Flight Evaluation project technical report**, particularly TRW `11176-H...-R0-00` material under NAS9-8166. The Apollo 10 `H314` and Apollo 12 `H585` numbers establish a report family, **not an interpolation rule**; no Apollo 11 H-series suffix may be inferred.

NTRS catalogs Apollo 11 Supplement 5 under parent report `MSC-00171` plus separate supplement/TM identifiers, while Apollo 12 DPS Supplement 5 carries `MSC-01855-SUPPL-5`, TRW, NASA-TM, and accession identifiers. Therefore **`MSC-00171-SUPPL-7` remains a search string only**, not Apollo 11 metadata.

The Apollo 16 DPS final-flight-evaluation catalog record confirms that this report family can contain FTP thrust/Isp corrected to standard inlet conditions and comparison against engine acceptance-test values. That establishes why the missing Apollo 11 report is discriminating evidence; it does not authorize transfer of neighboring-mission values to LM-5.

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

1. Pursue the **underlying Apollo 11 / LM-5 DPS Final Flight Evaluation contractor report** in TRW Systems Group project-report indexes, NAS9-8166 records, MSC bibliographies, and archival holdings; crosswalk any recovered contractor number to the September 1970 Supplement 7 wrapper.
2. Search LM-5 engine acceptance/performance records for delivered thrust/Isp or an explicit FTP force mapping.
3. Retain **LMA790-3-LM page 2.3-25 / Table 2.3-1** as a named blocked target until a legible September 1969 page image or clean LEP is recovered.
4. Continue Mission-G PDI-mass recovery only from explicitly event-identified primary records.

## Evidence status

**PARTIALLY DOCUMENTED.** The handbook target and its revision-control context are documented, but page 2.3-25 is blocked on legible primary-page recovery. Supplement 7 existence/title/date and the Apollo 10 contractor-report/MS C-wrapper packaging precedent are documented; Apollo 11's actual contractor/report identifiers and content remain **BLOCKED ON BIBLIOGRAPHIC / ARCHIVAL RECOVERY**. Pattern-derived identifiers remain prohibited as evidence. Exact LM-5 force calibration/delivered performance and PDI mass remain unresolved; TRW Volume II remains **BLOCKED ON NAMED SOURCE RECOVERY**.