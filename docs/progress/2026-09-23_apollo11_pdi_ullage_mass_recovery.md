# Progress — Apollo 11 PDI ullage mass recovery

Date: 2026-09-23
Parent: `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`

## Finding

A primary mission-specific source closes most of the previously open pre-PDI mass boundary. **Apollo 11 Mission Report Supplement 5 (MSC-00171 Supplement 5), Table VIII, Lunar Module RCS ΔV Performance** lists the **DPS PDI ullage** event at **GET 102:32:57.6**, firing duration **8.0 s**, with **vehicle weight 33,329 lb**.

This is stronger than reconstructing PDI mass from DOI cutoff or later landing mass because the table explicitly identifies the event as PDI ullage and supplies its vehicle weight.

## Boundary

The table does **not** label 33,329 lb as the vehicle weight at DPS ignition itself. It is therefore recorded as an **explicit pre-PDI / PDI-ullage event mass**, not silently promoted to exact PDI ignition mass. Exact ignition-state mass remains unresolved unless another primary record identifies it directly or a bounded propellant/consumables correction is demonstrated.

No numerical correction from the eight-second RCS ullage firing is inferred here.

## Consequence

The prior statement that no explicitly event-identified primary pre-PDI mass had been recovered is superseded. The simulation now has a primary Apollo 11 checkpoint of **33,329 lb at PDI ullage**. This can be used as a historical validation checkpoint while `mass_kg` at DPS ignition remains caller-supplied/unresolved.

## Source

NASA, *Apollo 11 Mission Report*, MSC-00171 Supplement 5, Table VIII, *Lunar Module RCS ΔV Performance*.

- https://ntrs.nasa.gov/api/citations/19720018196/downloads/19720018196.pdf
- https://ntrs.nasa.gov/citations/19720018196

## Evidence status

**DOCUMENTED — PRIMARY APOLLO 11 MISSION SUPPLEMENT.** PDI-ullage vehicle weight is **33,329 lb** at GET **102:32:57.6**. Exact DPS-ignition mass remains **UNRESOLVED**; no ullage-consumption correction is inferred.