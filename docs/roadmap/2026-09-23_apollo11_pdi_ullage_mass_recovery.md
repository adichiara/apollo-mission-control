# Roadmap continuation — Apollo 11 PDI ullage mass recovery

Date: 2026-09-23
Parent: `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`

## Resolved boundary

Apollo 11 Mission Report Supplement 5, Table VIII explicitly gives the **DPS PDI ullage** event at **GET 102:32:57.6**, duration **8.0 s**, vehicle weight **33,329 lb**. This is now the nearest explicitly event-identified primary Apollo 11 mass checkpoint immediately before powered descent.

Do not relabel this value as DPS-ignition mass. The table labels the event as PDI ullage, not PDI ignition, and no RCS-consumption correction is derived without source support.

## Model decision

| Model input | Status | Decision |
| --- | --- | --- |
| `mass_kg` pre-PDI checkpoint | Primary mission-specific event value recovered | Validate against **33,329 lb at PDI ullage** |
| `mass_kg` at DPS ignition | Exact value not explicitly recovered | Keep caller supplied / unresolved |

## Next

1. Continue recovery of **John P. Mayer memo 69-FMZ2-149** as the highest-priority direct FTP source.
2. Recover the two **8 July 1969** throttle-down dispersion items and **69-FM-156** base/addendum pages; inspect whether they explicitly state the nominal PDI vehicle state used in Mission-G analysis.
3. Search primary Apollo 11 consumables/weight statements for a directly labeled **PDI ignition** mass before considering any derived correction from the 33,329-lb ullage checkpoint.
4. Keep the LM-5 Operational Calibration Curves and DPS Final Flight Evaluation on their documented archival recovery paths.

## Evidence status

**PARTIALLY CLOSED.** Pre-PDI mass is now directly documented at the PDI-ullage event (**33,329 lb**). Exact DPS-ignition mass remains unresolved. No D-022 closure is claimed for exact PDI ignition mass.