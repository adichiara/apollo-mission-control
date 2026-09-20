# Apollo 11 landing-radar beam-transform roadmap

Date: 2026-09-19
Parent: `docs/ROADMAP.md`

## Controlled chain

Apollo-11-effective LUMINARY 099 controls `SETPOS`, measurement-time CDU capture, Y-Z-X preparation, and `*NBSM*` direction semantics. Memo #95 controls antenna→NB beta-then-alpha semantics. The LM-5 Mission G prelaunch erasable load supplies the position-specific alpha/beta values.

## Completed

The equation-level SETPOS and SM/NB transforms are composed into the landing-radar velocity estimator chain, with a provenance-bearing LM-5 profile adapter. Mission-specific MSK-1137 evidence controls the LR field identities, body-axis velocity frame, units/display masks, validity fields, and ground-computed identity of `ACT ΔV`.

The next architecture boundary is source-controlled. The Apollo 11 Mission Operation Report describes MCC as distinct CCATS, RTCC, Voice Communications, Display/Control, and MOCR/SSR elements, with telemetry and operational data processed through CCATS/RTCC for flight-control use. NASA TN D-8316 independently describes Apollo real-time display as distinct input and display subsystems. Therefore an Apollo 11 controller product must preserve the boundary between spacecraft/downlink data, ground processing, and display projection rather than reading authoritative simulation state directly.

A mission-specific primary source for display usage/request behavior has now been identified precisely: Costis, Ortolani, and Moreland, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*, PHO-TN401 (24 Dec 1969). HAER TX-109-C cites it to Box 078-65/66 of the Johnson Space Center History Collection at University of Houston-Clear Lake. No public digital copy was located. Direct use of PHO-TN401 is therefore BLOCKED pending archival retrieval or an authenticated scan; HAER's aggregate usage statistics are not promoted into exact request/timing semantics.

Neither the accessible architecture sources nor the indirect PHO-TN401 citation gives an Apollo-11 MSK-1137 per-field CCATS/RTCC route or numeric CRT refresh period. The onboard 2-second LR component cadence remains insufficient for that purpose.

## Next work

1. Continue accessible mission-era MCC Display/Control, RTCC program, CCATS, console/display handbook, or controller-procedure research for direct MSK-1137 routing, update behavior, or request semantics.
2. Treat direct PHO-TN401 inspection as a BLOCKED archival retrieval thread; retrieve it from the identified JSC History Collection holding if/when physical/archive access is pursued.
3. Until timing is sourced, keep sample/receive/process/display timestamps distinct; any zero-delay or caller-selected display cadence is a labeled simulation simplification, not historical timing.
4. Keep historical stochastic LR measurement generation BLOCKED until flight-effective numerical error evidence is recovered.
5. Preserve optional yaAGC/fixed-point comparison as validation hardening if later required.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** LM-5 geometry + SETPOS + measurement-time NB→SM transform through the estimator.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR field semantics/formatting at the field-definition level.
- **DOCUMENTED:** Apollo 11 MCC architectural separation of telemetry/CCATS/RTCC processing, Display/Control, and controller operations.
- **DOCUMENTED:** PHO-TN401 identity and archival location; HAER aggregate Apollo 11 display-usage reporting is secondary/indirect evidence only.
- **NOT CLAIMED:** bit-for-bit AGC fixed-point equivalence.
- **BLOCKED:** direct PHO-TN401 inspection; historical stochastic LR measurement generation.
- **UNRESOLVED:** exact per-field Apollo 11 CCATS/RTCC transformation/routing, controller-display cadence, latency, freshness policy, and GUIDO request/key workflow.