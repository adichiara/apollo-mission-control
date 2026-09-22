# Roadmap continuation — Apollo 11 descent dynamics input audit

Date: 2026-09-22
Parent: `docs/roadmap/2026-09-22_apollo11_descent_continuous_trajectory_boundary.md`

## Bounded question

Which generic DPS/translational inputs can be tied to primary Apollo 11 evidence without promoting design or later-vehicle values to LM-5 delivered-flight truth?

## Established primary boundaries

- Apollo 11 Press Kit: **9,870 lbf** maximum-rated DPS thrust, mission-specific preflight specification.
- Apollo 11 Mission Report: LM-5 advances to **FTP about 26 s after PDI**; postflight throttle/pressure histories; named LM masses at separation, DOI ignition, DOI cutoff, and landing.
- NASA TN D-7143: **10,500-lbf** maximum-rated design requirement and design Isp envelope; not LM-5 delivered performance.
- Later LMA790-3-LM Volume I: **92.5-percent FTP / 9,870-lbf fixed-full-throttle** mature-design semantics; surviving full-copy provenance is LM-7-and-subsequent or later and cannot silently become LM-5 calibration.

## LM-5 handbook recovery advance

LM-5-and-subsequent **Volume II — Operational Procedures** is publicly recovered but does not contain the required calibration.

A subsequent primary-source pass recovered a NASA Apollo Lunar Surface Journal-hosted excerpt from **LMA790-3-LM, Apollo Operations Handbook, Subsystems Data**. The pages carry **Basic Date 15 December 1968** and explicitly distinguish hardware **“On LM 5”** from **“LM 6 and subsequent vehicles.”** This is direct page-level evidence of a configuration-aware LM-5-era **Volume I**.

The excerpt is limited to spacecraft/crew-equipment and waste-management material. It contains no DPS pages and therefore does **not** establish LM-5 FTP percentage-to-force calibration, delivered thrust, or flight-effective Isp.

### Search consequence

The prior target “find LM-5 Volume I” is now too broad and should be retired. The next exact target is:

> **Recover the descent-propulsion-system section/pages from the LM-5-era LMA790-3-LM Volume-I change state represented by the 15 December 1968 basic-date pages, and preserve page-level change-date/configuration provenance.**

Engine acceptance/performance records and Apollo 11 Mission Report Supplement 7 remain parallel preferred sources for delivered performance.

## PDI mass

SNA-8-D-027(III) is the correct mass-properties family but the surviving public binder contains later replacement pages. The Mission Report provides named postflight checkpoints but no PDI row. Exact Mission-G PDI mass remains unresolved; secondary/reconstructed event relabelings remain rejected.

## Model decisions

| Model input | Status | Decision |
| --- | --- | --- |
| `thrust_n` / `end_thrust_n` | Apollo 11 9,870-lbf preflight specification; LM-5 FTP timing; LM-5 Volume-I provenance now demonstrated but DPS pages missing | Keep caller supplied; no exact LM-5 conversion |
| `specific_impulse_s` | Design requirement only; no LM-5 flight-effective history | Keep caller supplied |
| `mass_kg` | Named event masses documented; PDI absent | Keep PDI mass unresolved |
| burn duration | 756.3 s documented | Historical checkpoint |
| continuous trajectory | Reconstruction methodology documented; NAT listing unrecovered | Keep RECONSTRUCTED |

## D-022 result

No D-022 closure is claimed for PDI mass, delivered thrust, FTP calibration, or flight-effective Isp. No sourced LM-5 calibration range has yet been recovered whose endpoints can be tested for demonstrated irrelevance.

## Next

1. Search NASA/ALSJ/Virtual AGC/archive holdings for **LM-5-era Volume-I DPS pages**, keyed to the demonstrated **15 December 1968 basic date** and page-level change provenance.
2. Continue targeted recovery of **Apollo 11 DPS Supplement 7** and LM-5 engine acceptance/performance records.
3. Continue Mission-G PDI-mass recovery only from explicitly event-identified primary records.

## Evidence status

**PARTIALLY DOCUMENTED.** LM-5-era Volume-I provenance is now directly documented from NASA-hosted primary pages, narrowing rather than closing the propulsion question. Exact LM-5 DPS calibration/delivered performance and PDI mass remain unresolved. Apollo 11 DPS Supplement 7 and TRW Volume II remain **BLOCKED ON NAMED SOURCE RECOVERY**.