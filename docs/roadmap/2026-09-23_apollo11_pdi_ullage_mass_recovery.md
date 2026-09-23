# Roadmap continuation — Apollo 11 PDI ullage mass recovery

Date: 2026-09-23
Parent: `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`

## Resolved boundary

Apollo 11 Mission Report Supplement 5 provides two complementary primary tables. Table VIII explicitly gives the **DPS PDI ullage** event at **GET 102:32:57.6**, duration **8.0 s**, vehicle weight **33,329 lb**. Table VII gives the as-flown event timing: PDI ullage **102:32:57.6–102:33:05.6**, while the **DPS PDI maneuver starts at 102:33:05.2** and runs to 102:45:42.2 (757.0 s).

The main Apollo 11 Mission Report, **MSC-00171 §9.8.1**, independently documents the powered-descent engine sequence: firing duration **756.3 s**, approximately **6775 ft/s** velocity change, **13% minimum throttle at firing start**, and advance to **full throttle after approximately 26 s**. It reports an approximately **45-s data dropout during this period** and says Figure 9.8-1 was smoothed and does not reflect that dropout or the final throttle fluctuations.

The 756.3-s main-report firing duration and 757.0-s Supplement 5 maneuver duration remain separate source-reported quantities. Do not normalize one to the other without evidence establishing their timing conventions.

The 33,329-lb checkpoint remains the nearest explicitly event-identified primary Apollo 11 mass immediately before powered descent. Do not relabel it as exact DPS-ignition mass, and do not derive an RCS-consumption correction without source support.

## Model decision

| Model input | Status | Decision |
| --- | --- | --- |
| `mass_kg` pre-PDI checkpoint | Primary mission-specific event value recovered | Validate against **33,329 lb at PDI ullage** |
| PDI timing | Primary as-flown timing recovered | Ullage 102:32:57.6–102:33:05.6; DPS PDI start 102:33:05.2 |
| Early PDI throttle sequence | Primary mission-specific sequence recovered | **13% minimum throttle at start → full throttle at ~+26 s**; retain documented telemetry-dropout caveat |
| `mass_kg` at DPS ignition | Exact value not explicitly recovered | Keep caller supplied / unresolved |
| FTP force calibration | Not recovered | Do not derive force from the 13% throttle-setting statement |

## Next

1. Continue recovery of **John P. Mayer memo 69-FMZ2-149** as the highest-priority direct FTP-force source. The newly recovered 13% throttle-setting evidence does not replace it.
2. Recover the two **8 July 1969** throttle-down dispersion items and **69-FM-156** base/addendum pages; inspect their explicit throttle/FTP definitions and nominal PDI state.
3. Search primary Apollo 11 consumables/weight statements for a directly labeled **PDI ignition** mass before considering any derived correction from the 33,329-lb ullage checkpoint.
4. Preserve the **756.3 s vs 757.0 s** source distinction until a primary source explains the event/time convention difference.
5. Keep the LM-5 Operational Calibration Curves and DPS Final Flight Evaluation on their documented archival recovery paths.

## Evidence status

**PARTIALLY CLOSED.** Pre-PDI mass, event timing, and the early powered-descent throttle sequence are directly documented. Exact DPS-ignition mass and exact FTP force remain unresolved. No D-022 closure is claimed for either.