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
- LMA790-3-LM page 2.2-222, **Change Date 15 March 1969**, independently describes the automatic-throttle ceiling as **92.5 percent thrust**.
- LMA790-3-LM figure 2.2-62 on **page 2.2-215, Change Date 15 June 1969**, labels the TTCA throttle hard-stop position **92.5% THRUST**. Because the September LM-6 issue explicitly supersedes the LM-5-and-subsequent issue of that same date, this page is directly within the LM-5 handbook state.
- Later LMA790-3-LM Volume I: **9,870-lbf fixed-full-throttle** mature-design semantics; later-effective force statements cannot silently become LM-5 force calibration.

## LM-5 handbook recovery advance

LM-5-and-subsequent **Volume II — Operational Procedures** is publicly recovered but does not contain the required calibration.

A NASA ALSJ-hosted excerpt from Volume I explicitly distinguishes hardware **“On LM 5”** from **“LM 6 and subsequent vehicles.”** More importantly for propulsion control, the September 1969 LM-6 Volume-I scan retains page-level material from the superseded **15 June 1969 LM-5-and-subsequent issue**. Page 2.2-215 is one such page and directly documents the **92.5-percent TTCA throttle hard stop**.

This closes the configuration-provenance question for the 92.5-percent control limit: it was present in the LM-5 handbook state. It does **not** close the engine-force mapping. The remaining discriminating source is the DPS §2.3 performance/design material itself, with page dates at or before 15 June 1969, or vehicle-specific acceptance/postflight evidence.

### Search consequence

The next exact target is:

> **Recover DPS §2.3 performance/design pages in the September 1969 LM-6 scan whose individual effective/change dates are 15 June 1969 or earlier, and determine whether they supply LM-5-applicable force/Isp values.**

Engine acceptance/performance records and Apollo 11 Mission Report Supplement 7 remain parallel preferred sources for delivered performance.

## PDI mass

SNA-8-D-027(III) is the correct mass-properties family but the surviving public binder contains later replacement pages. The Mission Report provides named postflight checkpoints but no PDI row. Exact Mission-G PDI mass remains unresolved; secondary/reconstructed event relabelings remain rejected.

## Model decisions

| Model input | Status | Decision |
| --- | --- | --- |
| `thrust_n` / `end_thrust_n` | Apollo 11 9,870-lbf preflight specification; LM-5 FTP timing; LM-5-effective 92.5-percent control hard stop; exact LM-5 force mapping absent | Keep caller supplied; no exact LM-5 conversion |
| `specific_impulse_s` | Design requirement only; no LM-5 flight-effective history | Keep caller supplied |
| `mass_kg` | Named event masses documented; PDI absent | Keep PDI mass unresolved |
| burn duration | 756.3 s documented | Historical checkpoint |
| continuous trajectory | Reconstruction methodology documented; NAT listing unrecovered | Keep RECONSTRUCTED |

## D-022 result

No D-022 closure is claimed for PDI mass, delivered thrust, FTP force calibration, or flight-effective Isp. No sourced LM-5 calibration range has yet been recovered whose endpoints can be tested for demonstrated irrelevance.

## Next

1. Recover **DPS §2.3 pages with 15 June 1969-or-earlier page dates** and inspect the performance/design table.
2. Continue targeted recovery of **Apollo 11 DPS Supplement 7** and LM-5 engine acceptance/performance records.
3. Continue Mission-G PDI-mass recovery only from explicitly event-identified primary records.

## Evidence status

**PARTIALLY DOCUMENTED.** The **92.5-percent throttle hard stop is now directly LM-5-effective handbook evidence** via page 2.2-215 dated 15 June 1969. Exact LM-5 force calibration/delivered performance and PDI mass remain unresolved. Apollo 11 DPS Supplement 7 and TRW Volume II remain **BLOCKED ON NAMED SOURCE RECOVERY**.