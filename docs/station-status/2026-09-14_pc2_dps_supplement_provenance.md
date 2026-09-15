# Station-status addendum — PC+2 DPS and mass-properties provenance

Date: 2026-09-14

Historical station maturity grades are unchanged. This pass improves the source boundary for propulsion and Flight Dynamics mass-properties state, not console/display reconstruction.

## CONTROL

Maturity remains **B**.

Mission-specific sources establish staged PC+2 throttle-command behavior, terminal blowdown, and the nominal Apollo 13 full-thrust baseline. At ~59 hours GET, LM Control challenged a PC+2 DPS trim and later accepted Flight Dynamics data after the report identified LM Control's premission mass properties as not the best available basis. This supports a simulator behavior in which CONTROL/LM Control can challenge a derived trim whose mass-properties provenance is stale.

The September 1970 Apollo 13 Mission Report gives PC+2/transearth-injection mass as `95,424.0 lb` at ignition and `87,456.0 lb` at cutoff. Research note 148 establishes that these table values are **postflight reconstructed mass properties** based on analyses of expendable loadings/usage and updated spacecraft properties. They are validation references, not values to silently substitute for the final operational P30 module weights.

Still unresolved for CONTROL-facing historical numerical fidelity: measured LM-7 thrust-versus-time, startup transient, throttle calibration, mass flow/mixture ratio/effective Isp, blowdown behavior, exact display/loading, numerical trim discrepancy, and whether the accepted ~59-hour trim explicitly used `T+55`.

## FIDO / Flight Dynamics

Maturity remains **B**, with a stronger numerical validation boundary.

The evidence now establishes:

- mission-relative RTCC mass-properties reference states (`T-6`, `T+6`, `T+25`, `T+55`);
- `T±N` is distinct from generation/load time;
- Apollo RTCC mass properties were structured operational state supporting module summation, depletion tables, weight/CG, and trim;
- stale premission versus current Flight Dynamics mass-property provenance could cause a controller-visible PC+2 trim disagreement;
- the final P30 carried `62,480 / 33,452 lb` operational module weights (`95,932 lb` sum);
- the official postflight reconstruction gives **`95,424.0 lb` at PC+2 ignition**, with event weight/CG/inertia referenced to the LM coordinate system for post-accident maneuver phases.

The 508-lb difference is now explicitly a cross-product reconciliation target, not an error to normalize away. The postflight value must not be treated as a demonstrated RTCC input.

Still unresolved:

- exact `T+55` epoch semantics;
- H-2 deck field layout, module/depletion values, and processor mapping;
- whether the accepted ~59-hour trim explicitly used `T+55`;
- how the operational P30 module weights were generated from the available mass/depletion state;
- the specific accounting causes of the difference from the later postflight reconstruction;
- which operational mass value(s), if any, were the exact inputs to the final RTCC targeting solution.

The simulator should keep physical mass/CG, postflight reconstructed event mass properties, mission-control mass-properties state, module/depletion state, reference epoch, load timestamp, calculation provenance, targeting weights, and controller-visible products separate.

## FLIGHT

Maturity remains **B**.

No new decision authority or display behavior is inferred. The result strengthens the numerical provenance model: the P30 module weights are an operational product while the mission-report event mass is explicitly a later postflight reconstruction. FLIGHT-facing summaries should preserve source/product identity rather than present a single falsely exact spacecraft-weight field.

## Research priority

First priority is H-2 RTCC/Flight Dynamics material exposing the operational module/depletion accounting behind the `T+55` mass-properties state and final P30 `62,480 / 33,452 lb` module weights. In parallel, continue recovery of the October 1970 Apollo 13 *Descent Propulsion System Final Flight Evaluation*. No unsupported explanation for the 508-lb difference is promoted into the station model.