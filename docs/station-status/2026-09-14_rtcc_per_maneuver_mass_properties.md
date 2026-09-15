# Station-status addendum — RTCC per-maneuver mass-properties workflow

Date: 2026-09-14  
Parent: `docs/STATION_RESEARCH_STATUS.md`

Historical station maturity grades are unchanged. Research note 150 improves the operational-computation boundary rather than reconstructing an H-2 console display.

## FIDO / RETRO / Flight Dynamics

**Evidence strengthened.** The Apollo 12 Flight Control Division RETRO postflight report states that mass properties were computed by RTCC controllers in an offline computer in lieu of RTACF and were run prior to each maneuver. Computed SPS trims agreed within 0.1 degree with onboard postburn values for CSM-alone and docked configurations.

For simulator design, Flight Dynamics mass-properties support may therefore be represented as an explicit pre-maneuver calculation workflow with provenance and freshness, rather than a static spacecraft-weight field.

## CONTROL / LM systems

**No maturity-grade change.** Apollo 13 mission-specific evidence remains controlling: LM Control's use of premission mass properties produced the documented PC+2 trim challenge. The Apollo 12 source explains a plausible operational calculation workflow but does not prove which H-2 run/deck generated the accepted trim.

## FLIGHT

**No maturity-grade change.** Cross-console reconciliation can expose disagreement between products generated from different mass-properties bases. No new source establishes a specific Flight Director display or action sequence.

## Boundary

Do not import Apollo 12's exact software, staffing, run cadence, table layout, or constants into Apollo 13. The next evidence threshold is an H-2 RTCC/Flight Dynamics procedure, listing, worksheet, or processor record connecting `T+55` to a specific pre-PC+2 mass-properties run and derived trim/P30 products.