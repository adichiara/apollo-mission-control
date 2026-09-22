# Progress — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## Completed

Audited the next unresolved LM-5 descent inputs against primary Apollo documentation, preserving the distinction among design values, planned/commanded behavior, as-flown telemetry, reconstructed trajectory, and model inputs.

### As-flown DPS evidence tightened

Apollo 11 Mission Report §9.8 documents the 756.3-second powered descent, approximately 6775 ft/s velocity change, a 13% minimum-throttle start, throttle-up to full after about 26 seconds, and an approximately 45-second early data dropout. Figure 9.8-1 records flight throttle position, chamber pressure, regulator outlet pressure, and fuel/oxidizer interface pressures versus mission time.

This is stronger as-flown validation evidence than the previous documentation reflected. It does **not** justify converting throttle percentage or chamber pressure into an exact delivered thrust time series without a sourced LM-5 calibration/performance relationship, nor does it close flight-effective Isp.

### Named propulsion source identified

Primary NASA mission-report supplement tables identify **Apollo 11 Mission Report Supplement 7, _Descent Propulsion System Final Flight Evaluation_, published September 1970**. Targeted searches using the exact title, mission/supplement number, publication date, NTRS terminology, and neighboring supplement patterns did not recover a public copy. Public Apollo document indexes located in this pass list the Apollo 11 Mission Report and Supplement 5 but not Supplement 7.

Result: Supplement 7 is now **BLOCKED ON NAMED SOURCE RECOVERY** and becomes the preferred archival propulsion target. No values were borrowed from Apollo 10, 12, 14, or 15 DPS supplements.

### Existing boundaries retained

TRW 70-FMT-819 Volume II remains archive-triggered and blocked on named-source recovery. NASA TN D-6846 remains the primary descent validation/checkpoint envelope. LM-5 launch bookkeeping remains documented but is not PDI mass.

## Boundary preserved

No launch mass was substituted for PDI mass. No design Isp was promoted to flight-effective Isp. No throttle percentage was converted into unsupported exact thrust. No neighboring-mission DPS supplement was treated as Apollo 11 performance. No reconstructed state was relabeled raw telemetry.

## Repository updates

- `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/station-status/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `resources/APOLLO11_DESCENT_DYNAMICS_INPUT_SOURCE_CATALOG_ADDENDUM.md`

## Next

Continue the active LM-5 PDI mass/state bookkeeping search through mission-specific mass-property and operational-data records. Pursue Apollo 11 Mission Report Supplement 7 through archival/catalog routes as the parallel highest-value propulsion source. Do not spend another broad-web pass on TRW Volume II absent a new archival lead.

## Evidence status

**PARTIALLY DOCUMENTED.** Apollo 11 as-flown DPS throttle/pressure telemetry is now explicitly bounded. Exact PDI mass and delivered thrust/Isp remain unresolved. Apollo 11 DPS Supplement 7 and TRW BET Volume II are **BLOCKED ON NAMED SOURCE RECOVERY**.