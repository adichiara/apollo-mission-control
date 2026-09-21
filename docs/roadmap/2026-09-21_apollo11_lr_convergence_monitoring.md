# Roadmap continuation — Apollo 11 LR convergence monitoring

Date: 2026-09-21
Parent: `docs/roadmap/2026-09-21_apollo11_descent_trajectory_rules.md`

## Bounded question

What Apollo-11-effective evidence establishes the observable landing-radar convergence sequence and the ground's role in monitoring the descent trajectory, without inventing a CRT layout or controller call procedure?

## Primary-source result

Floyd V. Bennett's NASA MSC Technical Memorandum **TM X-58040, Apollo Lunar Descent and Ascent Trajectories** (March 1970) supplies a direct Apollo 11 postflight account of the LR update sequence. It states that LR lock occurred during the face-up rotation at about **37,000 ft**; the initial altitude difference was **Δh = -2,200 ft**; because no limits were violated, LR altitude data were incorporated after a short monitoring period at about **31,600 ft**; Δh then converged to about **100 ft within 30 seconds**; and LR velocity updates began nominally at about **29,000 ft**.

The same primary source states that altitude and altitude rate were monitored in real time for flight safety by both flight controllers and crew. Because of ground communication delay, flight controllers could only advise on projected trends. This establishes a ground monitoring/decision role but does **not** identify the exact Mission-G CRT fields, display request, back-room/front-room split, or voice-loop ownership of each LR comparison.

The Apollo 11 Mission Report independently timestamps the flown sequence: LR data good at 102:37:51, radar updates enabled at 102:38:45, the velocity-update condition at 102:38:50, and P64 entry at 102:41:32. These timestamps are compatible with Bennett's postflight description and give a bounded event order without requiring reconstruction of an unsupported display path.

## Implementation consequence

A historical Apollo 11 descent reference may represent the LR monitoring sequence as distinct evidence states:

`LR lock/data good → monitored pre-acceptance altitude difference → altitude updates enabled/incorporated → Δh convergence → velocity updates active → continued trajectory monitoring toward P64`

For the documented Apollo 11 reference, the postflight anchors above may be used as observed values/events. They must not be generalized into universal thresholds or an invented automatic ground decision algorithm. In particular, **-2,200 ft** was the observed initial Apollo 11 Δh, not an abort limit, and **100 ft in 30 s** describes the flown convergence, not a generic acceptance requirement.

The simulator should preserve the distinction between onboard LR acceptance/update state, ground-observed trajectory quantities, controller interpretation, and any subsequent FLIGHT/CAPCOM advice.

## What remains unresolved

- exact Mission-G controller CRT field(s) used to observe Δh/convergence;
- whether a dedicated GUIDO display or another product supplied each comparison during the Apollo 11 descent;
- exact front-room/back-room call sequence for declaring convergence and supporting the landing GO;
- parameter-level routing already separately BLOCKED on Mission-G PHO-TR155/data-pack/Data Formats recovery.

## Next bounded target

Search Apollo-11-effective Mission Techniques, Flight Controller Operations Handbook material, controller-loop/transcript records, or postflight controller reports for the **voice/call workflow around LR acceptance/convergence and the GO for landing**. Accept a workflow claim only where the source identifies the station or speaker; do not infer ownership from generic GUIDO responsibilities.

## Sources

- Floyd V. Bennett, NASA MSC, *Apollo Lunar Descent and Ascent Trajectories*, NASA TM X-58040, March 1970: https://ntrs.nasa.gov/citations/19700024568
- NASA MSC, *Apollo 11 Mission Report*, MSC-00171 / NASA TM X-62633, November 1969: https://ntrs.nasa.gov/citations/19700008096
- NASA MSC Flight Control Division, *Flight Mission Rules, Apollo 11 (AS-506/107/LM-5)*, April 16, 1969: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11missionrules.pdf

## Evidence status

- **DOCUMENTED / APOLLO 11 POSTFLIGHT:** LR lock near 37,000 ft; initial Δh -2,200 ft; altitude data incorporated near 31,600 ft; Δh converged to about 100 ft within 30 seconds; velocity updates began near 29,000 ft.
- **DOCUMENTED / GROUND ROLE:** flight controllers and crew monitored altitude and altitude rate; ground advice was trend-based because of communication delay.
- **DOCUMENTED / EVENT ORDER:** Mission Report timestamps bound LR-good, update-enable, velocity-update-condition, and P64-entry events.
- **UNRESOLVED:** exact Mission-G display fields and station-specific voice/call workflow.