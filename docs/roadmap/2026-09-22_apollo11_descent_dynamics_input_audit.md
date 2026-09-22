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

The September 1969 LM-6-and-subsequent Volume-I table of contents/list of illustrations identifies the exact propulsion target as **§2.3.5, Descent Propulsion Section Performance and Design Data**, beginning at **page 2.3-25**; the corresponding table is **Table 2.3-1, Descent Propulsion Section — Performance and Design Data**. This is primary handbook structure, but the currently searchable copy does not yield a sufficiently reliable page-level effective date or legible table contents for page 2.3-25. Therefore no LM-5 thrust or Isp value is promoted from it yet.

A later NASA-hosted LM handbook independently preserves the same §2.3.5 / page 2.3-25 / Table 2.3-1 structure. It is useful only as a locator/cross-check, not as LM-5 configuration evidence.

### Search consequence

The next exact target is now **page 2.3-25 / Table 2.3-1 in the 15 September 1969 LM-6 Volume-I scan**, with its footer/effective date and table values read from the page image. It qualifies as LM-5 evidence only if its individual effective date is **15 June 1969 or earlier**.

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

1. Recover/read **page 2.3-25 / Table 2.3-1** from the September 1969 LM-6 Volume-I scan and verify its individual effective date.
2. Continue targeted recovery of **Apollo 11 DPS Supplement 7** and LM-5 engine acceptance/performance records.
3. Continue Mission-G PDI-mass recovery only from explicitly event-identified primary records.

## Evidence status

**PARTIALLY DOCUMENTED.** The LM-5 DPS search is now narrowed to an exact handbook page/table, but its LM-5-effective date and values remain unresolved. Exact LM-5 force calibration/delivered performance and PDI mass remain unresolved; Supplement 7 and TRW Volume II remain **BLOCKED ON NAMED SOURCE RECOVERY**.