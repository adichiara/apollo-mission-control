# Station-status addendum — PC+2 ground data processing

Date: 2026-09-13  
Parent: `docs/STATION_RESEARCH_STATUS.md`

Historical station maturity grades are unchanged. Research note 103 clarifies the ground-support/data-path boundary rather than adding exact console reconstruction.

## FIDO / RETRO

Maturity remains **B**.

Trajectory and ephemeris products are downstream of RTCC processing and tracking-data selection. The first playable may expose solution readiness and data-quality status to Flight Dynamics, but must not give FIDO/RETRO unrestricted raw MSFN truth or imply that the station itself operates RTCC internals.

## GUIDO

Maturity remains **B**.

Guidance/load products may depend on RTCC-generated solution/load state. Existing final-load staging remains valid. Exact RTCC computation, Cartesian-vector internals, and support-console keying remain deferred.

## INCO

Maturity remains **B**.

Communications, uplink, telemetry, and ranging availability depend on the MCC/MSFN/CCATS path. INCO may receive operational path/status consequences where sourced, but is not treated as the operator of CCATS computer internals.

## CAPCOM

Maturity remains **B**.

CAPCOM retains crew-facing communication responsibility. Ground command/load computation and routing remain upstream support functions rather than CAPCOM authority.

## FLIGHT

Maturity remains **B**.

FLIGHT may coordinate consequences of unavailable/questionable tracking, telemetry, or load products, but no omniscient ground-computer status panel is inferred.

## First-playable consequence

Use the functional chain:

`MSFN source/path → CCATS routing/processing → RTCC processing/product → station-visible product/status → controller decision`

Only represent ground-system states that materially affect a sourced PC+2 player decision or selected failure path. Do not invent exact software, hardware operation, timing, failure rates, or support-role actions for completeness.
