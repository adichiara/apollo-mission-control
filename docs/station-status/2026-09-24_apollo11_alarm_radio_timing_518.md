# Station-status update — Apollo 11 alarm radio timing

Date: 2026-09-24
Research note: 518
Parent: `docs/STATION_RESEARCH_STATUS.md`

## Station consequence

The crew-facing radio side of the Apollo 11 descent alarm sequence now has primary Mission-G timestamps from GOSS NET 1. This strengthens the CAPCOM/crew interface model without promoting unsupported internal-loop detail.

The reference station model should preserve four separable stages:

1. onboard computer/event occurrence;
2. crew recognition/report on air-ground;
3. internal ground assessment/decision;
4. CAPCOM disposition to the crew.

The primary record shows these are not a single instantaneous event. For the first 1202, the Mission Report event anchor is 102:38:22, explicit crew identification is 102:38:30/32, and CAPCOM's GO is 102:38:53. For the 1201 window, the event anchor is 102:42:18, CAPCOM acknowledges the alarm at 102:42:19, Armstrong identifies it at 102:42:24, and CAPCOM gives the GO/same-type disposition at 102:42:25.

No internal station maturity is promoted: exact Garman/Bales/Flight timing, overlap, named loop, and privilege matrix remain open.

## Recovery target

Use the radio anchors to align and inspect GUIDO L/R and `792-AAI`; establish internal chronology only from those recordings or equivalent Mission-G primary evidence.

Source: https://ntrs.nasa.gov/citations/20160014392