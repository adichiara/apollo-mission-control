# Apollo 11 LR real-time display architecture — progress

Date: 2026-09-21

## Question

What mission-effective primary evidence constrains the real-time MCC path between Apollo 11 telemetry and controller CRT products, without assuming that RTCC transformed the landing-radar fields on MSK-1137?

## Primary evidence recovered

The Apollo 11 prelaunch *Mission Operation Report*, M-932-69-11 (24 June 1969), describes MCC as a set of distinct but cooperating systems: CCATS, RTCC, Display/Control, MOCR, and SSRs. It states that telemetry and operational data can be processed by CCATS and RTCC for mission verification or computation. This is mission-specific evidence that both CCATS and RTCC participate in real-time data handling, but it does not assign the MSK-1137 LR fields to either processor.

Philco-Ford's *Mission Control Center Houston Familiarization Manual*, PHO-FAM001, revised through 30 June 1967, gives the more discriminating display architecture. It states that the Display/Control System generates displays from either (a) display/control data received from RTCC or (b) **selected telemetry data received from CCATS**. It further states that RTCC display/control data normally follows a request, except for preprogrammed automatic digital-readout transfers. Thus a controller CRT product need not, merely by being a CRT display, imply an RTCC engineering transformation; the documented architecture includes a CCATS-selected-telemetry path into Display/Control.

PHO-FAM001 is system-level architecture rather than an Apollo-11 parameter-routing table. M-932-69-11 establishes that the same CCATS/RTCC/Display-Control framework was the Apollo 11 mission-control configuration.

## Controlled conclusion

The former unresolved layer can be narrowed from a generic `CCATS/FDS/display` ambiguity to two historically documented real-time display-source classes:

`telemetry → CCATS → selected telemetry → Display/Control → controller display`

or

`telemetry/operational data → RTCC processing → display/control data → Display/Control → controller display`.

The evidence does **not** yet identify which class supplied MSK-1137 `VXB/VYB/VZB/RNG`, nor the engineering-unit conversion or display-database parameter identifiers. Therefore do not assign those LR fields to RTCC solely because they appear on a CRT, and do not assert a direct CCATS route solely because a selected-telemetry route existed.

## Simulation consequence

Preserve a generic ground telemetry/display adapter for the LR fields. Its external contract may produce the documented MSK-1137 engineering products, but its internal ownership should remain unassigned between CCATS-selected telemetry and RTCC-derived display/control data until a parameter-level Apollo-11-effective source is recovered.

## Sources

- NASA Apollo Program Office, *Mission Operation Report — Apollo 11 (AS-506) Mission*, M-932-69-11, 24 June 1969, Mission Support section. https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11_MissionOpReport.pdf
- Philco-Ford / Western Development Laboratories, *Mission Control Center Houston Familiarization Manual*, PHO-FAM001, revised through 30 June 1967, especially §§3-2 through 3-2-5 and Display/Control discussion. https://www.ibiblio.org/apollo/Documents/Familiarization%20Manual%20Mission%20Control%20Center%20Houston.pdf

## Next target

Seek the Apollo-era telemetry measurement/format definition, CCATS parameter table, display-format source listing, or other mission-effective record that ties the LGC LR downlink word positions to MSK-1137 `VXB/VYB/VZB/RNG`. Parameter-level evidence is required before choosing the CCATS-selected-telemetry path or RTCC display/control path for those fields.

## Evidence status

- **DOCUMENTED, APOLLO-11 MISSION CONFIGURATION:** MCC used CCATS, RTCC, Display/Control, MOCR, and SSR systems, with telemetry/operational data processable by CCATS and RTCC.
- **DOCUMENTED, PRIMARY MCC ARCHITECTURE:** Display/Control could generate displays from selected CCATS telemetry independently of RTCC display/control data.
- **DOCUMENTED, PRIMARY MCC ARCHITECTURE:** RTCC also supplied display/control data to Display/Control.
- **UNRESOLVED:** which path supplied MSK-1137 LR fields and the exact engineering-unit/parameter mapping.
- **NOT ESTABLISHED:** RTCC ownership/transformation of MSK-1137 `VXB/VYB/VZB/RNG`.
