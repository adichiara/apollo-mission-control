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

Primary Apollo 10 evidence supplies a recovery model. Apollo 10 Mission Report Supplement 7 is an MSC wrapper around the earlier TRW project technical report **11176-H314-R0-00**, _Apollo 10 LM-4 Descent Propulsion System Final Flight Evaluation_, dated **8 August 1969**, under **NAS 9-8166**. The December 1969 supplement retains the contractor report's title page and number while identifying the package as Supplement 7 to `MSC-00126`.

Search not only for the September-1970 MSC supplement wrapper, but for an earlier **Apollo 11 / LM-5 Descent Propulsion System Final Flight Evaluation project technical report**, particularly TRW `11176-H...-R0-00` material under NAS9-8166. Apollo 10 `H314` and Apollo 12 `H585` establish a report family, **not an interpolation rule**.

## New LM-5 FTP archival lead

The official Purdue University Libraries finding aid for the **Neil A. Armstrong papers (MSA 5)** identifies a contemporaneous Apollo 11 planning item titled **“Effect of fixed throttle point thrust on the time from loss of radial guidance control to DPS throttle-down,” dated 5 June 1969**. It appears in the Apollo Program working files, Mission Planning / A-11 Planning series alongside other Mission-G descent material.

This is a stronger LM-5-specific calibration lead than continuing to infer from later handbooks: its title explicitly concerns **fixed throttle point thrust** and Apollo 11 planning before flight. The finding aid establishes the item's existence, title, date, collection, and archival location; **it does not expose the item's numerical contents**. No thrust value is therefore extracted or inferred. The item is now a named archival recovery target in MSA 5.

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

1. Recover the **5 June 1969 Armstrong MSA 5 item, “Effect of fixed throttle point thrust on the time from loss of radial guidance control to DPS throttle-down,”** and inspect it for an explicit LM-5 FTP force/calibration and provenance.
2. Continue pursuit of the underlying **Apollo 11 / LM-5 DPS Final Flight Evaluation contractor report** and crosswalk any recovered contractor number to the September 1970 Supplement 7 wrapper.
3. Search LM-5 engine acceptance/performance records for delivered thrust/Isp.
4. Retain **LMA790-3-LM page 2.3-25 / Table 2.3-1** as a named blocked target until a legible September 1969 page image or clean LEP is recovered.
5. Continue Mission-G PDI-mass recovery only from explicitly event-identified primary records.

## Evidence status

**PARTIALLY DOCUMENTED.** A contemporaneous, Apollo-11-planning archival item explicitly about fixed-throttle-point thrust is now identified in Purdue's official MSA 5 finding aid, but its contents are **BLOCKED ON ARCHIVAL ITEM RECOVERY**. The finding aid is locator evidence, not force-calibration evidence. Page 2.3-25 remains blocked on legible primary-page recovery. Supplement 7 existence/title/date and the Apollo 10 contractor-report/MSC-wrapper packaging precedent are documented; Apollo 11's actual contractor/report identifiers and content remain blocked on bibliographic/archival recovery. Exact LM-5 force calibration/delivered performance and PDI mass remain unresolved; TRW Volume II remains **BLOCKED ON NAMED SOURCE RECOVERY**.