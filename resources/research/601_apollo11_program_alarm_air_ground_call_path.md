# 601 — Apollo 11 program-alarm air-ground call path

Date: 2026-09-23
Research thread: `apollo11-program-alarm-controller-flow`

## Question

Can the unresolved Apollo 11 program-alarm **call ownership** be narrowed without inferring internal MOCR routing from MSK-1137?

## Primary-source result

Yes, at the spacecraft/ground interface. NASA's Apollo 11 air-to-ground voice transcription (GOSS NET 1), Tape 66/7 p. 312, records the first powered-descent program-alarm exchange:

- `04 06 38 26` — CDR: `PROGRAM ALARM.`
- `04 06 38 30` — CDR: `It's a 1202.`
- `04 06 38 32` — LMP: `1202.`
- `04 06 38 48` — CDR asks Houston for a reading on the 1202 program alarm.
- `04 06 38 53` — `CC` (CAPCOM) answers that the crew is GO on the alarm.

The same transcript then records Houston continuing to monitor `DELTA-H` and communicating that monitoring to Eagle.

This directly establishes the **external communication path** for the first 1202: the spacecraft reported/requested disposition over air-ground, and CAPCOM returned the ground's GO disposition to the crew. It does not identify which internal controller/support-room position generated the recommendation, what display that person was viewing, or the internal loop/routing used to reach CAPCOM.

## Consequence

For the Apollo 11 reference architecture, alarm disposition to the crew should be represented as a CAPCOM-mediated ground call. The simulator should not have a GUIDO/GNC/etc. station speak directly to the spacecraft merely because MSK-1137 exposes alarm fields.

Internal alarm assessment ownership remains unresolved pending controller-loop/configuration evidence. PHO-TN401 remains relevant to display/control routing but must not be presumed to answer the voice-loop ownership question until inspected.

## Sources

- NASA, _Apollo 11 Air-to-Ground Voice Transcription (GOSS NET 1)_, Tape 66/7, p. 312: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11transcript_tec.pdf

## Evidence status

- **DOCUMENTED / SUFFICIENT:** spacecraft reports/requests program-alarm disposition over air-ground; CAPCOM communicates the ground GO disposition back to the crew.
- **UNRESOLVED:** internal controller/support-room assessment ownership and loop path feeding CAPCOM.
- **NO INFERENCE:** MSK-1137 field availability is not treated as proof of station ownership.
