# Station-status update — Apollo 11 descent voice evidence scope

Date: 2026-09-24
Research note: 517
Parent: `docs/STATION_RESEARCH_STATUS.md`

## Station consequence

NASA's Apollo 11 technical voice transcript is explicitly a **GOSS NET 1 air-to-ground** source. It is not evidence for internal MOCR or support-room traffic.

Keep the station model separated into:

- **crew-facing radio:** spacecraft ↔ CAPCOM, supportable from `AS11_TEC`/GOSS NET 1;
- **internal controller voice:** support-room/GUIDO/Flight traffic, requiring Historical Recorder GUIDO L/R, `792-AAI`, or Mission-G configuration evidence.

No station maturity is promoted. The supported role chain remains guidance-software support → GUIDO/Bales → Flight/ground decision → CAPCOM → crew, while exact internal wording, timing, named loop, and privilege matrix remain open.

## Recovery target

Directly compare GUIDO L/R and `792-AAI` around the five Mission Report alarm anchors; use the air-ground transcript only to bound the crew/CAPCOM side. PHO-TN401 and Mission-G-effective station/keyset/display configuration remain blocked archival targets.

Sources:
- https://ntrs.nasa.gov/citations/20160014392
- https://www.nasa.gov/history/mission-transcripts-mercury-gemini-and-apollo/
