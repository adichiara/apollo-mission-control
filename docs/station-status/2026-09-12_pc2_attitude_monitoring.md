# Station Status Addendum — PC+2 attitude error and rate monitoring

Date: 2026-09-12  
Parent: `docs/STATION_RESEARCH_STATUS.md`

## CONTROL

CONTROL remains maturity **B**, but PC+2 attitude/rate evidence is materially stronger.

Documented:

- PC+2 used approximately ±10 deg attitude-error and ±10 deg/s attitude-rate shutdown criteria;
- contemporaneous CAPCOM read-up and Haise readback both attach the startup-transient exception to attitude error, not rate;
- the postflight Mission Operations Report reverses that attachment, and the discrepancy remains explicitly recorded;
- CONTROL's postflight account reports a maximum observed PC+2 error of approximately 7 deg in roll and rates never exceeding 1 deg/s;
- Apollo LM instrumentation sources establish separate three-axis attitude-error and rate measurement families.

Implementation disposition:

- the operational simulator follows the contemporaneous rule actually transmitted/read back by the crew;
- attitude error >10 deg can trigger outside startup transient;
- rate >10 deg/s can trigger without a startup exception;
- the exact duration/definition of the startup transient is not invented;
- absent numerical observations remain `NOT_EVALUABLE` rather than implicitly nominal.

Still unresolved:

- exact Apollo 13 LM-7 PCM assignments and CONTROL CRT field routing for all attitude/rate channels;
- exact historical sample/display cadence;
- exact formal definition of the startup-transient interval.

## GUIDO

GUIDO remains maturity **B**.

Attitude error is clearly guidance-relevant, but this research pass does not prove that GUIDO independently owned the same PC+2 error/rate observations used by CONTROL. The implementation therefore does not duplicate the CONTROL monitoring product into GUIDO merely for convenience.

## CAPCOM

CAPCOM remains maturity **B**.

The mission-specific rule communication is now especially strong evidence: CAPCOM delivered the rule and the crew read it back consistently. This makes the air-ground operational exchange the implementation basis for allocating the startup exception while retaining the postflight-report conflict as a documentation discrepancy.

## Research record

See `resources/research/062_pc2_attitude_error_rate_shutdown_path.md`.
