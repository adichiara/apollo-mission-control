# 904 — Apollo 11 P66 erasable-load constant boundary

Research thread: `apollo11-descent-runtime`

## Bounded question

Which P66 numerical inputs are fixed in Apollo-11-effective LUMINARY 1A, and which require separate mission-load evidence?

## Findings

The Apollo-11-effective LUMINARY 1A build 099 listing separates P66 logic from numerical load inputs. `LUNAR_LANDING_GUIDANCE_EQUATIONS.agc` consumes `RODSCAL1`, `TAUROD`, `LAG/TAU`, `MINFORCE`, and `MAXFORCE`; `ERASABLE_ASSIGNMENTS.agc` allocates the corresponding ROD scale, time constant, lag ratio, and force limits as erasable I-values. They are not fixed numerical constants in the P66 code.

A surviving Apollo-era MIT printout, *Apollo 11 Landing Digital Simulation (1969)*, supplies a separate simulation-load snapshot. It identifies LMY99/APLIROPE context and lists RODSCALE = 0.003048 M/CS, TAUROD = 150 CS, LAG/TAU = 0.413333, plus MINFORCE and MAXFORCE words.

The printout was produced after the landing. It is strong Apollo-era simulation evidence but is not, by itself, proof that the same erasables were loaded aboard LM-5.

## Runtime consequence

The bounded P66 runtime may implement the flight-code topology and may carry these recovered values as a named simulation-load validation profile. It must not label them Apollo-11 as-flown until an Apollo 11 erasable-memory/pad-load authority or equivalent flight-effective source confirms them.

The numerical gate is now narrower: mission effectivity of the P66 erasable load values remains open, separately from the blocked LM-5 continuous propulsion calibration.

## Sources

1. MIT Instrumentation Laboratory / NASA, LUMINARY 1A build 099 Apollo 11 AGC source hardcopy, `LUNAR_LANDING_GUIDANCE_EQUATIONS.agc` and `ERASABLE_ASSIGNMENTS.agc`, transcribed from MIT Museum page images by Virtual AGC.
2. MIT Instrumentation Laboratory, *Apollo 11 Landing Digital Simulation (1969)*, Apollo-era digital-simulation printout preserved from Don Eyles's collection and scanned by Virtual AGC.
3. Virtual AGC Luminary provenance page documenting LUMINARY 99 Rev 1 flight identity and the surviving Apollo 11 digital simulations.

## Evidence status

- **DOCUMENTED:** Apollo-11-effective P66 code consumes ROD scale, ROD time constant, lag ratio, and force limits from erasable storage.
- **DOCUMENTED:** the 1969 Apollo 11 digital simulation contains explicit P66 load values including RODSCALE 0.003048 M/CS, TAUROD 150 CS, and LAG/TAU 0.413333.
- **PARTIALLY DOCUMENTED:** these are authentic Apollo-era simulation inputs associated with the Apollo 11 landing software/configuration.
- **UNRESOLVED:** whether those exact values were LM-5 flight-loaded erasables.
- **SUFFICIENT FOR CURRENT IMPLEMENTATION:** a clearly labeled simulation-load P66 validation profile may use the recovered values.
- **BLOCKED FOR AS-FLOWN CLAIM:** numerical P66 flight-load effectivity requires Apollo 11 pad-load/erasable-memory evidence.
