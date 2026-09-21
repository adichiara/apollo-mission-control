# Station-status addendum — Apollo 11 powered-descent phase profile

Date: 2026-09-21
Parent: `docs/STATION_RESEARCH_STATUS.md`

The Apollo 13 station maturity table remains unchanged. This addendum applies only to the D-024 Apollo 11 powered-descent architecture reference.

## New source-backed boundary

Mission-effective primary sources now support a nominal/flown powered-descent phase skeleton: initial minimum throttle, throttle-up near TFI +26 s, throttle recovery, high gate/approach, low gate/landing, and touchdown. The final Flight Plan gives nominal phase/state anchors; the Mission Report gives flown burn duration and propulsion observations.

## Station consequence

No station is promoted in maturity from these vehicle/mission sources alone. In particular, a nominal flight-plan value is not automatically a GUIDO, CONTROL, or FLIGHT display field. The approximately 45-second early propulsion-data dropout in the Mission Report also prevents treating the smoothed postflight propulsion plot as a continuous observed controller product.

For the Apollo 11 reference, station products should therefore expose only separately sourced controller-visible data. Hidden phase state may drive the causal model, but it must not be aliased to a station display.

## Next station research target

Find Apollo-11-effective controller documentation for propulsion/trajectory monitoring at throttle recovery and high gate: display fields, source/provenance, and decision/call rules. Prefer Mission-G display/configuration material, controller handbooks/checklists, Flight Mission Rules, and contemporary loop/transcript evidence.

## Sources

- NASA, *Apollo 11 Flight Plan*, final 1 July 1969: https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/a11final-fltpln.pdf
- NASA, *Apollo 11 Mission Report*, MSC-00171, §9.8: https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A11_MissionReport.pdf
- NASA, *Apollo 11 AS-506 Mission Operation Report*, M-932-69-11: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11_MissionOpReport.pdf

## Evidence status

- **DOCUMENTED:** mission-level powered-descent phase/event anchors and flown DPS start/throttle-up/burn-duration observations.
- **UNRESOLVED:** which exact phase variables/propulsion values were visible to each controller at throttle recovery/high gate and what mission-effective rule governed calls/actions.
- **UNCHANGED:** Apollo 13 station maturity.