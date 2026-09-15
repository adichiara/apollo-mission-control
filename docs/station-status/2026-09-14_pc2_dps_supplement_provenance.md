# Station-status addendum — PC+2 DPS and mass-properties provenance

Date: 2026-09-14

Historical station maturity grades are unchanged. This pass improves the source boundary for propulsion and Flight Dynamics mass-properties state, not console/display reconstruction.

## CONTROL

Maturity remains **B**.

Mission-specific sources establish staged PC+2 throttle-command behavior, terminal blowdown, and the nominal Apollo 13 full-thrust baseline. At ~59 hours GET, LM Control challenged a PC+2 DPS trim and later accepted Flight Dynamics data after the report identified LM Control's premission mass properties as not the best available basis. This supports a simulator behavior in which CONTROL/LM Control can challenge a derived trim whose mass-properties provenance is stale.

Research note 147 adds an official postflight event-mass anchor: the September 1970 Apollo 13 Mission Report gives PC+2/transearth-injection mass as `95,424.0 lb` at ignition and `87,456.0 lb` at cutoff. These are not silently substituted for the final P30 module weights.

Still unresolved for CONTROL-facing historical numerical fidelity: measured LM-7 thrust-versus-time, startup transient, throttle calibration, mass flow/mixture ratio/effective Isp, blowdown behavior, exact display/loading, numerical trim discrepancy, and whether the accepted ~59-hour trim explicitly used `T+55`.

## FIDO / Flight Dynamics

Maturity remains **B**, with a stronger numerical validation boundary.

The evidence now establishes:

- mission-relative RTCC mass-properties reference states (`T-6`, `T+6`, `T+25`, `T+55`);
- `T±N` is distinct from generation/load time;
- Apollo RTCC mass properties were structured operational state supporting module summation, depletion tables, weight/CG, and trim;
- stale premission versus current Flight Dynamics mass-property provenance could cause a controller-visible PC+2 trim disagreement;
- the official postflight PC+2/TEI event mass was **`95,424.0 lb` at ignition**, versus a **`95,932 lb`** sum of final P30 CSM/LM module weights.

The 508-lb difference is now a documented reconciliation target, not an error to normalize away.

Still unresolved:

- exact `T+55` epoch semantics;
- H-2 deck field layout, module/depletion values, and processor mapping;
- whether the accepted ~59-hour trim explicitly used `T+55`;
- the accounting relationship between `T+55`, the final P30 module weights, and the mission-report PC+2 event mass;
- which of these values, if any, was the exact mass input to the final RTCC targeting solution.

The simulator should keep physical mass/CG, official postflight event mass, mission-control mass-properties state, module/depletion state, reference epoch, load timestamp, calculation provenance, targeting weights, and controller-visible products separate.

## FLIGHT

Maturity remains **B**.

No new decision authority or display behavior is inferred. The new result strengthens the numerical provenance model: two official mission-specific products give different PC+2 mass representations, so FLIGHT-facing summaries should preserve source/product identity rather than present a single falsely exact spacecraft-weight field.

## Research priority

First priority is H-2 RTCC/Flight Dynamics material that explains the accounting relationship among the `T+55` operational mass-properties state, final P30 `62,480 / 33,452 lb` module weights, and the September mission report's `95,424.0 lb` PC+2/TEI ignition event mass. In parallel, continue recovery of the October 1970 Apollo 13 *Descent Propulsion System Final Flight Evaluation*. No unsupported explanation for the 508-lb difference is promoted into the station model.