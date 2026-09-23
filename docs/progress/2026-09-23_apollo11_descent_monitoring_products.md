# Progress — Apollo 11 descent monitoring products

Date: 2026-09-23

Continued the open Apollo 11 powered-descent architecture reference from the throttle-recovery/high-gate controller-product question.

## Primary-source result

NASA/MSC internal note **70-FM-20, MSC-01562, _The Apollo 11 Adventure_ (5 February 1970)** materially narrows the controller-monitoring boundary. Its Apollo 11 descent discussion says the actual descent remained very close to the nominal automatic trajectory through entry into P66, that throttle recovery occurred within one second of the preflight prediction, and that high-gate altitude and altitude rate were slightly lower than nominal.

More importantly for the simulator boundary, the report preserves an Apollo 11 descent strip-chart product (Figure 9) with separate comparison traces labeled for **AGS−PGNCS** and **MSFN−PGNCS**, plus descent-event markers including throttle-up, altitude updating, throttle-down, P64, velocity updating, P66, and touchdown. The same report also preserves a powered-descent monitoring flowchart with pre-PDI and in-plane/crossrange comparison logic.

## What this closes

This is primary NASA/MSC evidence that the Apollo 11 ground-monitoring problem was not simply a hidden-state trajectory check. It used explicit disagreement products between independent navigation/guidance sources and related those products to descent-event progression. That supports the repository's existing pairwise/consensus architecture and provides a mission-specific provenance target for controller products.

## Boundary preserved

The report is a post-mission MPAD reconstruction/summary. Figure 9 demonstrates the monitored comparison quantities and event context, but it does **not** by itself establish:

- which exact CRT/MSK request displayed each trace in the MOCR;
- exact field names/external names or telemetry routing;
- display refresh/cadence/latency;
- which controller physically viewed each plotted trace at each event;
- that the plotted postflight strip chart was itself the live controller display.

No such details are inferred.

## Next discriminating target

Recover Apollo-11-effective Mission G display/configuration or controller documentation that maps the demonstrated `AGS−PGNCS` / `MSFN−PGNCS` descent comparison quantities to station-visible products, requests, and call/decision rules. PHO-TN401 remains the strongest named archival display/control target.

## Source

- NASA Manned Spacecraft Center, Mission Planning and Analysis Division, _The Apollo 11 Adventure_, MSC Internal Note 70-FM-20, MSC-01562, 5 February 1970 (supersedes 69-FM-270): https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf

## Evidence status

- **DOCUMENTED:** Apollo 11 descent monitoring used explicit AGS−PGNCS and MSFN−PGNCS comparison products in the preserved descent strip-chart analysis.
- **DOCUMENTED:** the preserved monitoring material ties those comparisons to descent-event progression and separate in-plane/crossrange monitoring logic.
- **UNRESOLVED:** exact live MOCR display/request/routing/cadence and station assignment for those quantities.
- **BLOCKED:** PHO-TN401 direct inspection remains dependent on archival recovery.