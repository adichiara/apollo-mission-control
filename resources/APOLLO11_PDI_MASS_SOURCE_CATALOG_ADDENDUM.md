# Apollo 11 PDI mass source-catalog addendum

Date: 2026-09-23
Parent: `resources/APOLLO11_DESCENT_DYNAMICS_INPUT_SOURCE_CATALOG_ADDENDUM.md`

| Source | Direct evidence | Use / restriction |
| --- | --- | --- |
| **Apollo 11 Mission Report, MSC-00171 Supplement 5, Table VIII — Lunar Module RCS ΔV Performance** | `DPS PDI ullage`: GET **102:32:57.6**; firing duration **8.0 s**; vehicle weight **33,329 lb**. | **PRIMARY LM-5 AS-FLOWN EVENT CHECKPOINT.** Use as PDI-ullage/pre-PDI vehicle weight. Do not relabel as exact DPS-ignition mass or derive an ullage-consumption correction without explicit support. |
| **Apollo 11 Mission Report, MSC-00171 Supplement 5, Table VII — Flight Time Line** | `DPS PDI ullage`: **102:32:57.6–102:33:05.6**, 8.0 s. `DPS PDI maneuver`: starts **102:33:05.2**, ends **102:45:42.2**, duration **757.0 s**. | **PRIMARY LM-5 AS-FLOWN TIMING.** Establishes that the tabulated DPS start occurs 0.4 s before the ullage interval ends. It supplies no separate ignition weight; do not transfer the Table VIII 33,329-lb event weight to 102:33:05.2 as an exact mass. |
| **Apollo 11 Mission Report, MSC-00171, §9.8.1 — Descent Propulsion / Inflight Performance** | Powered-descent firing **756.3 s**; ΔV approximately **6775 ft/s**; engine at **13% minimum throttle** at firing start and advanced to **full throttle after approximately 26 s**; approximately **45-s data dropout during this period**. Figure 9.8-1 data are described as smoothed and not reflecting the dropout or final throttle fluctuations. | **PRIMARY LM-5 AS-FLOWN PROPULSION SEQUENCE.** Use the throttle settings/timing as historical checkpoints with the dropout caveat. Do **not** convert the 13% setting to FTP force from generic rated thrust. Preserve 756.3 s separately from Supplement 5's 757.0-s PDI-maneuver duration pending evidence on event/time conventions. |

## Source URLs

- https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11_MissionReport.pdf
- https://ntrs.nasa.gov/citations/19700008096
- https://ntrs.nasa.gov/citations/19720018196
- https://ntrs.nasa.gov/api/citations/19720018196/downloads/19720018196.pdf
- https://www.nasa.gov/wp-content/uploads/static/history/afj/ap11fj/pdf/19720018196_as11-mr-supp5-lm-rcs.pdf

## Evidence status

**DOCUMENTED / PARTIAL.** Apollo 11 PDI-ullage vehicle weight is directly reported as **33,329 lb**, the as-flown PDI transition is timed through DPS start at **102:33:05.2**, and the main Mission Report directly documents the initial **13% minimum throttle → full throttle at approximately +26 s** sequence. Exact DPS-ignition mass and exact FTP force remain **UNRESOLVED**.