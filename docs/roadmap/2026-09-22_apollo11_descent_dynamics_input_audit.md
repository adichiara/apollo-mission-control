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

The September 1969 LM-6-and-subsequent Volume-I table of contents/list of illustrations identifies **§2.3.5, Descent Propulsion Section Performance and Design Data**, beginning at **page 2.3-25**, with **Table 2.3-1** at that location.

A follow-on pass reached the same primary issue's **List of Effective Pages**. It confirms page-by-page revision control through Original, 15 March, 15 June, and 15 September 1969 states in the relevant handbook. The available indexed rendering is too OCR-corrupted around the 2.3 ranges to assign an issue date specifically to page 2.3-25 without guessing. The table body is likewise not exposed reliably.

Therefore page 2.3-25 is **BLOCKED ON LEGIBLE PRIMARY PAGE-IMAGE / LEP RECOVERY**. A later NASA-hosted handbook remains locator evidence only; its later values cannot establish LM-5 configuration.

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

1. Make **Apollo 11 DPS Supplement 7, _Descent Propulsion System Final Flight Evaluation_**, the active propulsion recovery target; prefer NTRS/NASA/MSC holdings and contemporaneous report indexes before secondary mirrors.
2. Search LM-5 engine acceptance/performance records for delivered thrust/Isp or an explicit FTP force mapping.
3. Retain **LMA790-3-LM page 2.3-25 / Table 2.3-1** as a named blocked target until a legible September 1969 page image or clean LEP is recovered.
4. Continue Mission-G PDI-mass recovery only from explicitly event-identified primary records.

## Evidence status

**PARTIALLY DOCUMENTED.** The handbook target and its revision-control context are documented, but page 2.3-25 is blocked on legible primary-page recovery. Exact LM-5 force calibration/delivered performance and PDI mass remain unresolved; Supplement 7 and TRW Volume II remain **BLOCKED ON NAMED SOURCE RECOVERY**.