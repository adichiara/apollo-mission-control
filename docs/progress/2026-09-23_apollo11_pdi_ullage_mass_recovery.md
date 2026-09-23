# Progress — Apollo 11 PDI ullage mass recovery

Date: 2026-09-23
Parent: `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`

## Finding

A primary mission-specific source closes most of the previously open pre-PDI mass boundary. **Apollo 11 Mission Report Supplement 5 (MSC-00171 Supplement 5), Table VIII, Lunar Module RCS ΔV Performance** lists the **DPS PDI ullage** event at **GET 102:32:57.6**, firing duration **8.0 s**, with **vehicle weight 33,329 lb**.

A second pass through the same primary supplement adds the exact event relationship from **Table VII, Flight Time Line**: PDI ullage runs **102:32:57.6–102:33:05.6**, and the **DPS PDI maneuver begins at 102:33:05.2**. Thus the tabulated DPS start occurs **0.4 s before the ullage interval ends**. The DPS PDI maneuver is tabulated through **102:45:42.2**, duration **757.0 s**.

A separate primary source, the main **Apollo 11 Mission Report, MSC-00171, §9.8.1 Inflight Performance**, now constrains the early powered-descent throttle history. It states that the powered-descent firing lasted **756.3 s**, produced approximately **6775 ft/s** velocity change, began at the **minimum throttle setting (13 percent)**, and was advanced to **full throttle after approximately 26 s**. It also reports about a **45-s data dropout during this period**, with normal throttle-up inferred from crew reports, and states that Figure 9.8-1's pressure/throttle data were smoothed and do not reflect the dropout or the throttle fluctuations just before touchdown.

The 756.3-s §9.8.1 firing duration and Supplement 5 Table VII's 757.0-s PDI-maneuver duration are both preserved as source-reported values. They are not silently forced to agree or used to redefine one another without evidence about their event/time conventions.

## Boundary

The sources do **not** label 33,329 lb as the vehicle weight at DPS ignition itself. Table VIII associates that weight with the ullage event; Table VII supplies timing but no separate mass at 102:33:05.2. Exact ignition-state mass therefore remains unresolved unless another primary record identifies it directly or a bounded propellant/consumables correction is demonstrated.

The Mission Report §9.8.1 evidence also does not establish Mayer's fixed-throttle-point force calibration. `13 percent` is the report's throttle-setting description; it must not be converted to an LM-5 FTP force by multiplying it by a generic rated-thrust value. No numerical correction from the eight-second RCS ullage firing is inferred here.

## Consequence

The simulation now has a primary Apollo 11 checkpoint of **33,329 lb at PDI ullage**, a primary as-flown **DPS PDI start time of 102:33:05.2**, and a mission-specific early-descent throttle sequence of **13% minimum throttle at firing start → full throttle at approximately +26 s**, subject to the documented telemetry dropout. These can be used as historical validation checkpoints while `mass_kg` at DPS ignition and exact FTP force remain caller-supplied/unresolved.

## Sources

NASA, *Apollo 11 Mission Report*, MSC-00171, §9.8.1, Inflight Performance.

- https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11_MissionReport.pdf
- https://ntrs.nasa.gov/citations/19700008096

NASA, *Apollo 11 Mission Report*, MSC-00171 Supplement 5, Tables VII and VIII.

- https://ntrs.nasa.gov/api/citations/19720018196/downloads/19720018196.pdf
- https://ntrs.nasa.gov/citations/19720018196

## Evidence status

**DOCUMENTED — PRIMARY APOLLO 11 MISSION REPORT / SUPPLEMENT.** PDI-ullage vehicle weight is **33,329 lb** at GET **102:32:57.6**; PDI ullage ends at **102:33:05.6** and the DPS PDI maneuver starts at **102:33:05.2**. The main Mission Report independently documents **13% minimum throttle at powered-descent start and full throttle after approximately 26 s**, with a roughly 45-s data dropout. Exact DPS-ignition mass and exact FTP force remain **UNRESOLVED**.