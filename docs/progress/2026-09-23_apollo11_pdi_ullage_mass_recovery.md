# Progress — Apollo 11 PDI ullage mass recovery

Date: 2026-09-23
Parent: `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`

## Finding

A primary mission-specific source closes most of the previously open pre-PDI mass boundary. **Apollo 11 Mission Report Supplement 5 (MSC-00171 Supplement 5), Table VIII, Lunar Module RCS ΔV Performance** lists the **DPS PDI ullage** event at **GET 102:32:57.6**, firing duration **8.0 s**, with **vehicle weight 33,329 lb**.

A second pass through the same primary supplement adds the exact event relationship from **Table VII, Flight Time Line**: PDI ullage runs **102:32:57.6–102:33:05.6**, and the **DPS PDI maneuver begins at 102:33:05.2**. Thus the tabulated DPS start occurs **0.4 s before the ullage interval ends**. The DPS PDI maneuver is tabulated through **102:45:42.2**, duration **757.0 s**.

This is stronger than reconstructing PDI mass from DOI cutoff or later landing mass because the source explicitly identifies the PDI-ullage event, its vehicle weight, and the adjacent DPS-start timing.

## Boundary

The source does **not** label 33,329 lb as the vehicle weight at DPS ignition itself. Table VIII associates that weight with the ullage event; Table VII supplies timing but no separate mass at 102:33:05.2. Exact ignition-state mass therefore remains unresolved unless another primary record identifies it directly or a bounded propellant/consumables correction is demonstrated.

No numerical correction from the eight-second RCS ullage firing is inferred here.

## Consequence

The simulation now has a primary Apollo 11 checkpoint of **33,329 lb at PDI ullage** plus a primary as-flown **DPS PDI start time of 102:33:05.2**. These can be used as historical validation checkpoints while `mass_kg` at DPS ignition remains caller-supplied/unresolved.

## Source

NASA, *Apollo 11 Mission Report*, MSC-00171 Supplement 5, Tables VII and VIII.

- https://ntrs.nasa.gov/api/citations/19720018196/downloads/19720018196.pdf
- https://ntrs.nasa.gov/citations/19720018196

## Evidence status

**DOCUMENTED — PRIMARY APOLLO 11 MISSION SUPPLEMENT.** PDI-ullage vehicle weight is **33,329 lb** at GET **102:32:57.6**; PDI ullage ends at **102:33:05.6** and the DPS PDI maneuver starts at **102:33:05.2**. Exact DPS-ignition mass remains **UNRESOLVED**; no ullage-consumption correction is inferred.