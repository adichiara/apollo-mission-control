# Roadmap continuation — Apollo 11 descent dynamics input audit

Date: 2026-09-22
Parent: `docs/roadmap/2026-09-22_apollo11_descent_continuous_trajectory_boundary.md`

## Bounded question

Which generic DPS/translational inputs can be tied to primary Apollo 11 evidence without promoting design or later-vehicle values to LM-5 delivered-flight truth?

## Established primary boundaries

- Apollo 11 Press Kit: **9,870 lbf** maximum-rated DPS thrust, mission-specific preflight specification.
- Apollo 11 Mission Report: LM-5 advances to **FTP about 26 s after PDI**; postflight throttle/pressure histories; named LM masses at separation, DOI ignition, DOI cutoff, and landing.
- NASA TN D-7143: **10,500-lbf** maximum-rated design requirement and design Isp envelope; not LM-5 delivered performance.
- NASA Apollo News Reference GN&C material: descent-engine throttle hard stop at **92.5 percent thrust**; automatic-throttle counter increments correspond to **2.7 lb thrust per pulse**.
- LMA790-3-LM control-electronics material in the **15 December 1968 basic-date lineage**, with a page changed **15 March 1969**, independently describes the automatic-throttle ceiling as **92.5 percent thrust**.
- Later LMA790-3-LM Volume I: **9,870-lbf fixed-full-throttle** mature-design semantics; surviving full-copy provenance is LM-7-and-subsequent or later and cannot silently become LM-5 force calibration.

## LM-5 handbook recovery advance

LM-5-and-subsequent **Volume II — Operational Procedures** is publicly recovered but does not contain the required calibration.

A NASA Apollo Lunar Surface Journal-hosted excerpt from **LMA790-3-LM, Apollo Operations Handbook, Subsystems Data** carries **Basic Date 15 December 1968** and explicitly distinguishes hardware **“On LM 5”** from **“LM 6 and subsequent vehicles.”** This directly establishes a configuration-aware LM-5-era Volume I, although the excerpt is not the DPS section.

A further publication-lineage check now establishes that **LMA790-3-LM 6 and Subsequent, Volume I, dated 15 September 1969, explicitly superseded LMA790-3-LM 5 and Subsequent dated 15 June 1969**. Its effective-page history retains pages dated 15 March and 15 June 1969. This is useful provenance: a discrete **LM-5-and-subsequent Volume-I issue existed on 15 June 1969, before Apollo 11**, and later copies can preserve unchanged pages from that issue. It does not make a September 1969 replacement page LM-5 evidence, and the DPS performance table itself has not yet been recovered with a 15 June-or-earlier effective date.

The control evidence therefore remains strong for **92.5-percent FTP/control-law semantics**, while the engine-specific mapping from that control state to exact LM-5 force and flight-effective performance remains unresolved.

### Search consequence

The next exact target is:

> **Recover the LMA790-3-LM 5 and Subsequent Volume-I DPS performance/design pages from the 15 June 1969 issue (or pages demonstrably unchanged into the 15 September LM-6 issue), preserving each page's effective/change date.**

Engine acceptance/performance records and Apollo 11 Mission Report Supplement 7 remain parallel preferred sources for delivered performance.

## PDI mass

SNA-8-D-027(III) is the correct mass-properties family but the surviving public binder contains later replacement pages. The Mission Report provides named postflight checkpoints but no PDI row. Exact Mission-G PDI mass remains unresolved; secondary/reconstructed event relabelings remain rejected.

## Model decisions

| Model input | Status | Decision |
| --- | --- | --- |
| `thrust_n` / `end_thrust_n` | Apollo 11 9,870-lbf preflight specification; LM-5 FTP timing; pre-Apollo-11 92.5-percent control ceiling; exact LM-5 force mapping absent | Keep caller supplied; no exact LM-5 conversion |
| `specific_impulse_s` | Design requirement only; no LM-5 flight-effective history | Keep caller supplied |
| `mass_kg` | Named event masses documented; PDI absent | Keep PDI mass unresolved |
| burn duration | 756.3 s documented | Historical checkpoint |
| continuous trajectory | Reconstruction methodology documented; NAT listing unrecovered | Keep RECONSTRUCTED |

## D-022 result

No D-022 closure is claimed for PDI mass, delivered thrust, FTP force calibration, or flight-effective Isp. No sourced LM-5 calibration range has yet been recovered whose endpoints can be tested for demonstrated irrelevance.

## Next

1. Recover the **15 June 1969 LM-5-and-subsequent Volume-I DPS performance/design pages**, or prove individual DPS pages were unchanged into the 15 September LM-6 issue using effective-page dates.
2. Continue targeted recovery of **Apollo 11 DPS Supplement 7** and LM-5 engine acceptance/performance records.
3. Continue Mission-G PDI-mass recovery only from explicitly event-identified primary records.

## Evidence status

**PARTIALLY DOCUMENTED.** The LM-5 Volume-I publication state is now bounded to a **15 June 1969 LM-5-and-subsequent issue**, and 92.5-percent FTP/control-law semantics are documented in pre-Apollo-11 primary/control documentation. Exact LM-5 force calibration/delivered performance and PDI mass remain unresolved. Apollo 11 DPS Supplement 7 and TRW Volume II remain **BLOCKED ON NAMED SOURCE RECOVERY**.