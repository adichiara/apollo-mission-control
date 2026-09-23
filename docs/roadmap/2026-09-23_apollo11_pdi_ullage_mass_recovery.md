# Roadmap continuation — Apollo 11 PDI ullage mass recovery

Date: 2026-09-23
Parent: `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`

## Resolved boundary

Apollo 11 Mission Report Supplement 5 provides two complementary primary tables. Table VIII explicitly gives the **DPS PDI ullage** event at **GET 102:32:57.6**, duration **8.0 s**, vehicle weight **33,329 lb**. Table VII gives the as-flown event timing: PDI ullage **102:32:57.6–102:33:05.6**, while the **DPS PDI maneuver starts at 102:33:05.2** and runs to 102:45:42.2 (757.0 s).

This is the nearest explicitly event-identified primary Apollo 11 mass checkpoint immediately before powered descent, and Table VII narrows the temporal gap further: DPS ignition begins **0.4 s before the tabulated ullage interval ends**. The source nevertheless does not assign a separate vehicle weight to the DPS PDI maneuver start.

Do not relabel 33,329 lb as exact DPS-ignition mass. Table VIII associates the weight with the PDI-ullage event, and no RCS-consumption correction is derived without source support.

## Model decision

| Model input | Status | Decision |
| --- | --- | --- |
| `mass_kg` pre-PDI checkpoint | Primary mission-specific event value recovered | Validate against **33,329 lb at PDI ullage** |
| PDI timing | Primary as-flown timing recovered | Ullage 102:32:57.6–102:33:05.6; DPS PDI start 102:33:05.2 |
| `mass_kg` at DPS ignition | Exact value not explicitly recovered | Keep caller supplied / unresolved |

## Next

1. Continue recovery of **John P. Mayer memo 69-FMZ2-149** as the highest-priority direct FTP source.
2. Recover the two **8 July 1969** throttle-down dispersion items and **69-FM-156** base/addendum pages; inspect whether they explicitly state the nominal PDI vehicle state used in Mission-G analysis.
3. Search primary Apollo 11 consumables/weight statements for a directly labeled **PDI ignition** mass before considering any derived correction from the 33,329-lb ullage checkpoint.
4. Keep the LM-5 Operational Calibration Curves and DPS Final Flight Evaluation on their documented archival recovery paths.

## Evidence status

**PARTIALLY CLOSED.** Pre-PDI mass is directly documented at the PDI-ullage event (**33,329 lb**), and as-flown PDI timing is now explicit. Exact DPS-ignition mass remains unresolved. No D-022 closure is claimed for exact PDI ignition mass.