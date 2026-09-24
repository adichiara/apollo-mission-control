# 603 — Apollo 11 program-alarm internal voice sequence

Date: 2026-09-24
Research thread: `apollo11-program-alarm-controller-flow`

## Question

Can primary participant evidence narrow the internal 1201/1202 decision sequence while the restored GUIDO recordings still await direct audio inspection?

## Primary-source result

Yes, but only to a participant-recollected sequence, not an exact timestamped transcript or named-loop assignment.

In his 27 March 2001 NASA Johnson Space Center Oral History Project interview, Jack Garman describes the first descent program-alarm assessment from his support-room position. He says he spoke to Steve Bales on a **back-room voice loop** and advised that the alarm was acceptable provided it did not recur too often. He separately describes Bales examining the rest of the data: the vehicle remained stable and the computer was recovering. Bales then made the GO call to Flight.

For a later alarm of the other executive-overflow type, Garman recalls calling **“Same type!”** into the loop, hearing Bales repeat “Same type,” and then hearing CAPCOM repeat it. This is firsthand participant evidence for a rapid support → GUIDO → crew-facing relay pattern.

## Boundary

Garman explicitly characterizes the circuit he used as a back-room voice loop, but he does **not name that loop** in the interview. The recollection therefore does not justify mapping the traffic to `FD LOOP`, `MOCR DYN`, or any other Mission-G loop name.

The oral history was recorded in 2001 and Garman himself notes uncertainty about some exact wording/order. It is strong participant evidence for roles and qualitative sequence, but it is not substituted for the restored 1969 audio. Exact words, alarm-by-alarm timing, overlap, and audible participants remain subject to direct GUIDO L/R recording verification.

The account also shows that Bales' disposition was not represented as a blind relay of Garman's advice: Garman recalls Bales checking the remaining vehicle/computer data before the GO. The simulator should therefore preserve GUIDO as an assessment/decision node rather than model the back room as directly commanding the crew.

## Simulator consequence

The Apollo 11 alarm interaction may represent:

1. guidance-software support assessing alarm class/recurrence;
2. GUIDO concurrently checking broader guidance/computer/vehicle indications;
3. GUIDO issuing the ground recommendation upward;
4. CAPCOM providing the crew-facing disposition.

For repeated same-class alarms, a compressed “same type” relay is historically supported at participant-recollection level. Do not assign a named conference loop, exact latency, exact wording for every occurrence, or direct support-room air-ground authority until the primary recordings/configuration evidence supports it.

## Sources

- NASA Johnson Space Center Oral History Project, John R. Garman interview, 27 March 2001: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/GarmanJR/GarmanJR_3-27-01.pdf

## Evidence status

- **DOCUMENTED / PRIMARY PARTICIPANT:** Garman used a back-room voice loop to advise Bales on the first program alarm; Bales checked other data before his GO.
- **DOCUMENTED / PRIMARY PARTICIPANT:** on a later different-but-same-class alarm, Garman recalls a rapid `Same type` support → Bales → CAPCOM relay.
- **UNRESOLVED:** exact named loop, exact per-alarm wording/timing/overlap, and complete audible participant set.
- **NEXT VERIFICATION:** inspect restored Apollo 11 GUIDO L/R recordings around the 1201/1202 interval; use automated transcripts only as navigation aids.
