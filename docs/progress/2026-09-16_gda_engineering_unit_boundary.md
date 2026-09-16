# Progress — GDA engineering-unit boundary

Date: 2026-09-16

## Completed

- Added research note 187 using primary LM instrumentation documentation.
- Recovered the LM-10-and-subsequent Instrumentation Packet entries for the same `GH1313V` / `GH1314V` GDA position channel family identified in LM-7/8/9 documentation.
- Established that the later instrumentation system presents both Pitch and Roll GDA position over an engineering range of `-6..+6 DEG`.
- Corrected the research framing: the unresolved Apollo 13 question is no longer generically "are these raw voltage channels convertible to engineering units?"; it is specifically whether LM-7 used the same conversion and what its signed EXT/RET polarity/reference was.
- Preserved the configuration boundary: no LM-10 conversion was transferred to LM-7, and no mapping to the Apollo 13 Mission Report inch values or crew-facing `5.86 / 6.75` pair was inferred.
- Updated the PC+2 GDA roadmap, CONTROL station status, and source catalog.

## Remaining priority

The principal unresolved item remains the T+55 LM-burn mass-properties deck -> RTCC/RTACF run -> `5.86 / 6.75` lineage. The parallel GDA target is narrowed to mission-block LM-7 calibration/polarity evidence and the crew-facing trim-number reference definition.