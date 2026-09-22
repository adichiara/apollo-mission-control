# Roadmap continuation — Apollo 11 descent propellant countdown

Date: 2026-09-21
Parent: `docs/roadmap/2026-09-21_apollo11_program_alarm_chain.md`

## Bounded question

What source-backed state and crew/controller-visible events should the Apollo 11 powered-descent reference preserve once the descent-propellant low-level indication occurs?

## Primary-source result

The Apollo 11 Mission Report, section 9.8.3, separates the physical/gaging facts that are often collapsed into one number. The low-level signal occurred at **102:44:30.4 GET**. Based on sensor location it nominally represented about **116 seconds of firing time remaining**. The report's postflight timeline explicitly distinguishes that event from **engine cutoff with 45 seconds to calculated depletion**, a **landing go/no-go decision point at 20 seconds to calculated depletion**, and depletion itself. Postflight reconstruction gave about **50 seconds to oxidizer-tank-2 depletion at cutoff**, within the stated gaging accuracy of the 45-second indication.

The primary air-to-ground record fixes the player-visible voice sequence: CAPCOM called **“60 seconds” at 102:45:02** and **“30 seconds” at 102:45:31** before contact light at about 102:45:40 and engine stop immediately afterward.

## Controller ownership / timer result

The previously open station-ownership question can now be narrowed substantially. Robert L. Carlton's NASA Johnson Space Center Oral History identifies his Apollo role and describes the LM propellant instrumentation available to the ground, including telemetry pressure measurement. NASA's later Apollo 11 historical treatment, explicitly based on Carlton's oral history, identifies Carlton as **LEM CONTROL on Gene Kranz's White Team** and records that, once low level occurred, **Carlton started a stopwatch** marked for the remaining-time calls. Carlton's own oral-history recollection of the landing describes watching that stopwatch and altitude together; at engine shutdown he retained **18 seconds to the abort point**.

This supports the operational chain:

`descent low-level indication → CONTROL (Bob Carlton) starts procedural stopwatch → CONTROL remaining-time call → CAPCOM relay to crew → landing/abort decision`

The countdown therefore does **not** require an inferred RTCC calculation, GUIDANCE product, or continuously computed exact fuel-remaining field. The evidence supports a human procedural timer at CONTROL triggered by the low-level condition.

Evidence hierarchy matters: the Mission Report and air-to-ground transcript remain the contemporary primary records for the physical event and crew-facing calls. Carlton's JSC oral history is retrospective first-person evidence for the controller procedure. It closes ownership/procedure sufficiently for simulator behavior but does not establish an exact CRT field, telemetry parameter mnemonic, support-room routing, or the precise Apollo-11-effective written checklist wording.

## Implementation boundary

Preserve these as distinct concepts:

`physical/gaging state → low-level observation → CONTROL procedural timer → CONTROL call → CAPCOM transmission → crew decision → physical depletion`

Do **not** reinterpret CAPCOM's 60/30 calls as direct tank quantity, exact seconds to engine flameout, or a hidden-state depletion clock exposed to players. The Mission Report itself shows why: the low-level indication and actual postflight depletion estimate differed materially.

For the historical Apollo 11 reference, CONTROL may receive the low-level event and operate a stopwatch/countdown procedure, with the historically recorded 60/30 calls passed to CAPCOM. A reusable causal implementation should trigger the procedural timer from the modeled low-level observation, not authoritative hidden propellant truth.

## Remaining question

The station/procedure dependency is now **research-sufficient for implementation**. A narrower archival question remains optional: recover the Apollo-11-effective written CONTROL procedure/checklist or Mission-G product definition that specifies the timer start condition and call marks. Do not block the causal implementation on that artifact, and do not invent CRT fields or RTCC involvement while it is absent.

The powered-descent research thread should proceed to the next unresolved player-visible/controller decision dependency rather than continue broad searching for countdown provenance.

## Sources

- NASA, *Apollo 11 Mission Report*, MSC-00171, November 1969, §9.8.3, Gaging System Performance: https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A11_MissionReport.pdf
- NASA, *Apollo 11 Technical Air-to-Ground Voice Transcription (GOSS NET 1)*, July 1969: https://ntrs.nasa.gov/citations/20160014392
- NASA Johnson Space Center Oral History Project, Robert L. Carlton interview, 19 April 2001: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/CarltonRL/CarltonRL_4-19-01.pdf
- NASA, *Houston We Have a Podcast: Lesser-Known Stories of Apollo 11* (2019), historical discussion based on the JSC Oral History Project: https://www.nasa.gov/podcasts/houston-we-have-a-podcast/lesser-known-stories-of-apollo-11/

## Evidence status

- **DOCUMENTED / PRIMARY POSTFLIGHT ENGINEERING:** low-level event at 102:44:30.4; nominal 116-second sensor-location basis; 45-second indicated / approximately 50-second postflight depletion margin at cutoff; distinct 20-second landing go/no-go point.
- **DOCUMENTED / PRIMARY TRANSCRIPT:** CAPCOM 60-second and 30-second calls and the subsequent contact/engine-stop sequence.
- **DOCUMENTED / RETROSPECTIVE FIRST-PERSON:** Bob Carlton/CONTROL used a stopwatch during the final descent and monitored it with altitude; his recollection places 18 seconds remaining to the abort point at engine shutdown.
- **RESEARCH-SUFFICIENT:** CONTROL ownership and procedural-stopwatch nature of the late-descent countdown.
- **UNRESOLVED BUT NOT REQUIRED:** exact Apollo-11-effective written timer procedure, CRT field/parameter mnemonic, or internal telemetry/display route that alerted CONTROL to low level.