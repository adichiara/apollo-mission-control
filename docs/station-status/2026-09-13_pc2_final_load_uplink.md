# Station-status addendum — PC+2 final state-vector / target-load / uplink

Date: 2026-09-13  
Parent: `docs/STATION_RESEARCH_STATUS.md`

Historical station maturity grades are unchanged. Research note 098 strengthens scenario-specific workflow evidence but does not add exact console/display reconstruction.

## FIDO / RETRO

Maturity remains **B**.

The final PC+2 trajectory solution is now explicitly upstream of the final LGC load workflow. Mission-specific evidence supports an earlier PC+2 load followed by a final solution/load cycle during final preparation. Exact RTCC Cartesian state-vector components and exact trajectory-display/key workflow remain deferred.

## GUIDO

Maturity remains **B**.

The final state vector and target load should be represented as staged readiness/load states rather than one generic `pending_final_verification` flag. GUIDO owns the guidance-side consistency/readiness relationship, but the project does not infer hidden load correctness merely from successful communications.

## INCO

Maturity remains **B**.

The final load depends on an explicitly configured uplink path. Flight-loop and air-ground evidence place INCO uplink work and crew UPDATA LINK configuration in the final-load chain. Ranging remains a separate final-preparation data-path dependency. Exact command routing, CCATS internals, and MSK/key sequences remain unresolved.

## CAPCOM

Maturity remains **B**.

CAPCOM obtains the crew-side configuration required for the update: P00, DATA/ACCEPT, and UPDATA LINK configuration, then returns the computer to the crew after the ground load. This is a communication/procedure responsibility, not direct ownership of the guidance solution.

## FLIGHT

Maturity remains **B**.

FLIGHT coordinates the cross-station readiness path and receives the operational completion state; no omniscient vector-validity display is inferred.

## First-playable consequence

Source-supported chain:

`FIDO/RTCC final solution → GUIDO load readiness/consistency → INCO uplink configuration → CAPCOM/crew P00 + DATA/ACCEPT + UPDATA LINK configuration → state-vector + target-load transmission → completion / computer returned to crew`

Do not add exact vector components, RTCC/CCATS command strings, exact transmission duration, or fabricated verification semantics without stronger primary evidence.