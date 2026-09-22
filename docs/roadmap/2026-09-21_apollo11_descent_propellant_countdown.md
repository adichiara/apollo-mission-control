# Roadmap continuation — Apollo 11 descent propellant countdown

Date: 2026-09-21
Parent: `docs/roadmap/2026-09-21_apollo11_program_alarm_chain.md`

## Bounded question

What source-backed state and crew/controller-visible events should the Apollo 11 powered-descent reference preserve once the descent-propellant low-level indication occurs?

## Primary-source result

The Apollo 11 Mission Report, section 9.8.3, separates the physical/gaging facts that are often collapsed into one number. The low-level signal occurred at **102:44:30.4 GET**. Based on sensor location it nominally represented about **116 seconds of firing time remaining**. The report's postflight timeline explicitly distinguishes that event from **engine cutoff with 45 seconds to calculated depletion**, a **landing go/no-go decision point at 20 seconds to calculated depletion**, and depletion itself. Postflight reconstruction gave about **50 seconds to oxidizer-tank-2 depletion at cutoff**, within the stated gaging accuracy of the 45-second indication.

The primary air-to-ground record then fixes the player-visible voice sequence: CAPCOM called **“60 seconds” at 102:45:02** and **“30 seconds” at 102:45:31** before contact light at about 102:45:40 and engine stop immediately afterward.

## Implementation boundary

Preserve these as distinct concepts:

`low-level sensor event → ground/crew awareness → countdown/decision-time estimate → CAPCOM 60/30 calls → landing or abort decision → physical propellant depletion`

Do **not** reinterpret CAPCOM's 60/30 calls as direct tank quantity, exact seconds to engine flameout, or a hidden-state depletion clock exposed to players. The Mission Report itself shows why: the low-level indication and actual postflight depletion estimate differed materially.

For the historical Apollo 11 reference, the recorded low-level event and 60/30 calls may be replayed as dated scenario events. A reusable causal implementation should derive any countdown only after its source, estimator, ownership, and decision rule are established; it must not simply expose authoritative remaining propellant time.

## Remaining question

The next discriminating dependency is **controller ownership/product provenance for the countdown**: which Mission-G station/product converted the low-level indication into the countdown used for the 60/30 CAPCOM calls, and what source/estimate it used. Until recovered, do not assign that calculation to CONTROL, GUIDANCE, FLIGHT, RTCC, or an invented generic fuel timer.

## Sources

- NASA, *Apollo 11 Mission Report*, MSC-00171, November 1969, §9.8.3, Gaging System Performance: https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A11_MissionReport.pdf
- NASA, *Apollo 11 Technical Air-to-Ground Voice Transcription (GOSS NET 1)*, July 1969: https://ntrs.nasa.gov/citations/20160014392

## Evidence status

- **DOCUMENTED / PRIMARY POSTFLIGHT ENGINEERING:** low-level event at 102:44:30.4; nominal 116-second sensor-location basis; 45-second indicated / approximately 50-second postflight depletion margin at cutoff; distinct 20-second landing go/no-go point.
- **DOCUMENTED / PRIMARY TRANSCRIPT:** CAPCOM 60-second and 30-second calls and the subsequent contact/engine-stop sequence.
- **UNRESOLVED BUT NOT INFERRED:** exact Mission-G controller station, display/product, computation, and source path that produced the countdown for CAPCOM.