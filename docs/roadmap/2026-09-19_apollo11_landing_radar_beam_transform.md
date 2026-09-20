# Apollo 11 landing-radar beam-transform roadmap

Date: 2026-09-19
Parent: `docs/ROADMAP.md`

## Controlled chain

Apollo-11-effective LUMINARY 099 controls `SETPOS`, measurement-time CDU capture, Y-Z-X preparation, and `*NBSM*` direction semantics. Memo #95 controls antenna→NB beta-then-alpha semantics. The LM-5 Mission G prelaunch erasable load supplies the position-specific alpha/beta values.

## Completed

The equation-level SETPOS and SM/NB transforms are composed into the landing-radar velocity estimator chain, with a provenance-bearing LM-5 profile adapter. Mission-specific MSK-1137 evidence controls the LR field identities, body-axis velocity frame, units/display masks, validity fields, and ground-computed identity of `ACT ΔV`.

The next architecture boundary is now also source-controlled. The Apollo 11 Mission Operation Report describes MCC as distinct CCATS, RTCC, Voice Communications, Display/Control, and MOCR/SSR elements, with telemetry and operational data processed through CCATS/RTCC for flight-control use. NASA TN D-8316 independently describes Apollo real-time display as distinct input and display subsystems. Therefore an Apollo 11 controller product must preserve the boundary between spacecraft/downlink data, ground processing, and display projection rather than reading authoritative simulation state directly.

Neither source gives an Apollo-11 MSK-1137 per-field CCATS/RTCC route or numeric CRT refresh period. The onboard 2-second LR component cadence remains insufficient for that purpose.

## Next work

1. Pursue a mission-era MCC Display/Control, RTCC program, CCATS, console/display handbook, or controller procedure that directly identifies MSK-1137 routing, update behavior, or request semantics.
2. Until then, keep sample/receive/process/display timestamps distinct; any zero-delay or caller-selected display cadence is a labeled simulation simplification, not historical timing.
3. Keep historical stochastic LR measurement generation BLOCKED until flight-effective numerical error evidence is recovered.
4. Preserve optional yaAGC/fixed-point comparison as validation hardening if later required.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** LM-5 geometry + SETPOS + measurement-time NB→SM transform through the estimator.
- **DOCUMENTED:** Apollo 11 MSK-1137 LR field semantics/formatting at the field-definition level.
- **DOCUMENTED:** Apollo 11 MCC architectural separation of telemetry/CCATS/RTCC processing, Display/Control, and controller operations.
- **NOT CLAIMED:** bit-for-bit AGC fixed-point equivalence.
- **BLOCKED:** historical stochastic LR measurement generation.
- **UNRESOLVED:** exact per-field Apollo 11 CCATS/RTCC transformation/routing, controller-display cadence, latency, freshness policy, and request/key workflow.
