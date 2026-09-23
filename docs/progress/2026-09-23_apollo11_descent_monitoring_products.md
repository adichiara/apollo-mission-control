# Progress — Apollo 11 descent monitoring products

Date: 2026-09-23

Continued the open Apollo 11 powered-descent architecture reference from the throttle-recovery/high-gate controller-product question.

## Primary-source result

NASA/MSC internal note **70-FM-20, MSC-01562, _The Apollo 11 Adventure_ (5 February 1970)** materially narrows the controller-monitoring boundary. Its Apollo 11 descent discussion says the actual descent remained very close to the nominal automatic trajectory through entry into P66, that throttle recovery occurred within one second of the preflight prediction, and that high-gate altitude and altitude rate were slightly lower than nominal.

More importantly for the simulator boundary, the report preserves an Apollo 11 descent strip-chart product (Figure 9) with separate comparison traces labeled for **AGS−PGNCS** and **MSFN−PGNCS**, plus descent-event markers including throttle-up, altitude updating, throttle-down, P64, velocity updating, P66, and touchdown. The same report also preserves a powered-descent monitoring flowchart with pre-PDI and in-plane/crossrange comparison logic.

## What this closes

This is primary NASA/MSC evidence that the Apollo 11 ground-monitoring problem was not simply a hidden-state trajectory check. It used explicit disagreement products between independent navigation/guidance sources and related those products to descent-event progression. That supports the repository's existing pairwise/consensus architecture and provides a mission-specific provenance target for controller products.

## Boundary preserved

The report is a post-mission MPAD reconstruction/summary. Figure 9 demonstrates the monitored comparison quantities and event context, but it does **not** by itself establish exact CRT/MSK presentation, field names, telemetry routing, refresh/cadence, or definitive station ownership. No such details are inferred.

## Archival recovery advance

A primary-source-first web pass still did not recover PHO-TN401 itself. However, the Library of Congress/NPS Historic American Engineering Record for the Apollo Mission Control Center cites the report directly and supplies a precise repository locator:

- B. Costis, W. Ortolani, W. Moreland, _NASA MCC Display/Control System Usage and Effectiveness, Apollo 11_, PHO-TN401, Contract NAS 9-1261, Philco-Ford Corporation for NASA, 24 December 1969.
- Johnson Space Center History Collection, University of Houston-Clear Lake.
- Apollo Program → Mission Documents: Apollo 11 → **Box 078-65/66**.

HAER footnote 37 specifically cites PHO-TN401 p. 5-5, demonstrating that the document was directly consulted in that archival holding. This is an archival locator, not evidence for uninspected PHO-TN401 contents beyond the bibliographic facts above.

## Next discriminating target

Request or inspect the identified UHCL Box 078-65/66 holding and extract only Apollo-11-effective display/control findings relevant to the demonstrated `AGS−PGNCS` / `MSFN−PGNCS` descent comparisons, station-visible products, requests, routing, cadence, and call/decision rules.

## Sources

- NASA Manned Spacecraft Center, Mission Planning and Analysis Division, _The Apollo 11 Adventure_, MSC Internal Note 70-FM-20, MSC-01562, 5 February 1970: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf
- Library of Congress / National Park Service, Historic American Engineering Record, _Johnson Space Center, Apollo Mission Control_, HAER No. TX-109-C, footnote 37 and bibliography: https://tile.loc.gov/storage-services/master/pnp/habshaer/tx/tx1100/tx1134/data/tx1134data.pdf

## Evidence status

- **DOCUMENTED:** Apollo 11 descent monitoring used explicit AGS−PGNCS and MSFN−PGNCS comparison products in preserved mission analysis.
- **DOCUMENTED:** PHO-TN401 archival holding identified as UHCL JSC History Collection, Apollo Program, Mission Documents: Apollo 11, Box 078-65/66.
- **UNRESOLVED:** exact live MOCR display/request/routing/cadence and station assignment for those quantities.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 contents remain uninspected.