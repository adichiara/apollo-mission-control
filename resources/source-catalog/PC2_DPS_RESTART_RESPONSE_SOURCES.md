# Apollo 13 PC+2 DPS Restart-Response Sources

Status: active source supplement for the premature-shutdown physical restart and controller-evidence boundaries.

## 1. Apollo 13 Mission Operations Report

- **Organization:** NASA MSC / Flight Control Division
- **Date:** 28 April 1970
- **Source class:** PRIMARY, mission-specific
- **Use:** States that an early PC+2 shutdown for reasons other than listed shutdown criteria was to be restarted by ullaging, pressing Engine Start, and using Descent Engine Command Override. Also establishes thrust chamber pressure as a ground-observed PC+2 quantity.
- **Consequence:** Establishes intended restartability and reuse of the common chamber-pressure monitoring path, but not a guaranteed successful response or restart-specific confirmation threshold.

## 2. Apollo 13 mission commentary / air-ground transcript

- **Organization:** NASA
- **Mission time:** approximately 76:31–76:37 GET
- **Source class:** PRIMARY, contemporaneous mission transcript
- **Use:** Records the crew-facing flashing-Noun-97 restart sequence: PRO, ullage, Engine Start, Descent Engine Override on.
- **Limitation:** Does not describe physical restart timing, pressure buildup, success criteria, or a required post-restart success report.

## 3. Apollo Operations Handbook — Lunar Module LM10 and Subsequent, Volume I

- **Document:** LMA790-3-LM, 1 February 1970
- **Source class:** PRIMARY/CONTEMPORARY subsystem documentation
- **Use:** Establishes that the DPS is restartable; manual START produces an engine-on command; engine-on energizes pilot valves and opens propellant shutoff valves, routing propellant to the injector/combustion chamber. Also describes Descent Engine Command Override as an alternate voltage path capable of keeping the engine firing if DECA power fails.
- **Limitation:** LM10-and-subsequent handbook material is used for common LM DPS architecture; this pass does not claim exact LM-7 restart transient certification.

## 4. Lunar Module 7, 8 & 9 Elementary Functional Diagrams

- **Source class:** PRIMARY/CONTEMPORARY, LM-7-family
- **Use:** Identifies `GQ6510P` as `PRESS, THRUST CHAMBER`.
- **Consequence:** Supports reuse of the already-modeled CONTROL chamber-pressure product for fresh post-restart evidence.
- **Limitation:** Does not establish an Apollo 13 restart-specific threshold, dedicated `RESTART CONFIRMED` discrete, or exact CRT routing.

## 5. Apollo 10 LM-4 Descent Propulsion System Final Flight Evaluation

- **Organization:** TRW / NASA MSC
- **Date:** 8 August 1969
- **Source class:** PRIMARY/CONTEMPORARY propulsion flight-evaluation report
- **Use:** Supports `GQ6510P` instrumentation continuity as a thrust-chamber-pressure measurement used in contemporary DPS flight analysis.
- **Limitation:** Apollo 10 LM-4 timing and numerical traces are not imported into Apollo 13 LM-7.

## Research record

- `resources/research/067_pc2_premature_shutdown_restart_branch.md`
- `resources/research/071_pc2_dps_restart_physical_response.md`
- `resources/research/072_pc2_restart_controller_evidence.md`

## Evidence rule

Do not equate:

- restart eligibility with successful restart;
- completed crew commands with physical engine response;
- physical restart with known thrust level;
- physical restart with automatic telemetry confirmation;
- a fresh chamber-pressure observation with an unsourced binary `restart confirmed` flag.

No exact restart delay, thrust setting, chamber-pressure trace, success probability, restart-specific pressure threshold, or required crew success report is asserted.