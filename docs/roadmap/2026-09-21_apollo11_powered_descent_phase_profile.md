# Roadmap continuation — Apollo 11 powered-descent phase profile

Date: 2026-09-21
Parent: `docs/ROADMAP.md`

## Bounded question

What mission-effective propulsion/trajectory phase anchors can the Apollo 11 powered-descent architecture reference use without reconstructing unsupported continuous dynamics?

## Primary-source result

The final Apollo 11 Flight Plan (1 July 1969) supplies the nominal powered-descent profile and marks fixed-throttle operation, radar altitude update, throttle recovery, radar velocity update, high gate/P63→P64, low gate, and touchdown on the same mission profile. Its high-gate-to-touchdown panel gives nominal event/state anchors including high gate at about TFI 8:24, low gate at about TFI 10:08 and touchdown at about TFI 11:58.

The Apollo 11 Mission Report supplies the flown propulsion boundary: powered descent lasted 756.3 s and produced approximately 6775 ft/s delta-V; the DPS began at minimum throttle (13 percent), advanced to full throttle after approximately 26 s, and had normal engine transients/throttle response. The report also warns that approximately 45 s of data were lost during the early throttle-up interval, so a smooth plotted trace is not direct flight measurement through that gap.

The Apollo 11 Mission Operation Report independently defines the three operational phases: braking uses maximum DPS thrust for most of the phase; approach begins near 7,600 ft at high gate; landing begins at 500 ft at low gate.

## Implementation consequence

The second architecture reference may now use a source-backed **phase/event skeleton** for powered descent. Keep nominal planned anchors and flown propulsion observations distinct. Do not interpolate a historically exact thrust/trajectory history through the Mission Report data gap, and do not treat the flight-plan nominal high/low-gate values as exact flown transition states.

This is enough to define deterministic phase transitions for an architecture proof while continuous trajectory/propulsion reconstruction remains a separate unresolved model question.

## Implementation update — 2026-10-07

The phase/event skeleton is now executable through `powered_descent_phase.py` and the Apollo 11 profile `apollo11_g_powered_descent_phase_skeleton`.

Only the nominal PDI/high-gate/low-gate/planned-touchdown anchors drive phase state. The Mission Report's flown propulsion observations are carried beside the phase result but do not alter it. This explicitly preserves plan-versus-flight differences.

## Next bounded target

Compose this phase state with the already implemented descent decision gate, controller-product schema, landing-radar state, and program-alarm state into a bounded Apollo 11 runtime projection. Do not expose hidden vehicle state or convert a nominal phase boundary into an automatic historical controller decision.

## Sources

- NASA, *Apollo 11 Flight Plan, AS-506, CSM-107/LM-5*, final, 1 July 1969: https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/a11final-fltpln.pdf
- NASA, *Apollo 11 Mission Report*, MSC-00171, November 1969, §9.8: https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A11_MissionReport.pdf
- NASA, *Apollo 11 AS-506 Mission Operation Report*, M-932-69-11, 24 June 1969: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11_MissionOpReport.pdf

## Evidence status

- **DOCUMENTED / MISSION PLAN:** powered descent contains fixed-throttle, throttle-recovery, high-gate, low-gate, and touchdown anchors; nominal high gate is about 7,600 ft and low gate 500 ft.
- **DOCUMENTED / FLOWN:** powered descent lasted 756.3 s; DPS began at 13-percent minimum throttle and advanced to full throttle after about 26 s; engine transients and throttle response were reported normal.
- **DOCUMENTED / LIMITATION:** approximately 45 s of propulsion data were lost during the early throttle-up interval; the Mission Report's smoothed figure does not reproduce that gap.
- **UNRESOLVED:** historically exact continuous thrust/trajectory history between anchors and controller-visible product/rule mapping at those phase boundaries.