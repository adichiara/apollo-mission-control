# Station-status addendum — Apollo 11 descent monitoring products

Date: 2026-09-23
Parent: `docs/STATION_RESEARCH_STATUS.md`

The Apollo 13 station maturity table remains unchanged. This addendum applies only to the D-024 Apollo 11 powered-descent architecture reference.

## Source-backed boundary

NASA/MSC 70-FM-20 preserves Apollo 11 `AGS−PGNCS` and `MSFN−PGNCS` descent comparisons. The AC Electronics Apollo 11 manual defines `MSK-1137` ground-display fields relevant to powered descent/program alarms. The air-ground transcript establishes crew request/CAPCOM disposition, while Jack Garman's NASA oral history establishes guidance-software back-room support to GUIDO/Steve Bales.

Apollo 11 Flight Mission Rules document Mission-G loop vocabulary. PHO-FAM001 documents local conference/intersite loops and talk/listen versus monitor-only keyset circuits. Exact Mission-G station-to-loop assignment remains unresolved.

NASA History Division reproduces an Apollo 11 Historical Recorder #1 track sheet assigning channels 21/22 to `GUIDO [L]/[R]`, positions 018/019. Research note 510 connects this to restored GUIDO L/R audio; automated transcripts are navigation aids only.

Research notes 511–513 establish Apollo-generic display request/channel attach behavior, DRK/FDK interaction semantics, and Mission-G display-resource evidence: one GUIDO D/TV channel in the mandatory prelaunch minimum and two GUIDO analog chart recorders listed as highly desirable on D/TV. These are not evidence for actual Apollo 11 GUIDO DRK/FDK mapping or descent callups.

Research note 514 adds primary participant evidence for the internal alarm workflow. Garman says he used an unnamed back-room voice loop to advise Bales; Bales checked broader data before making the GO call; a later same-class alarm produced a rapid `Same type` relay. This establishes participant-recollected role behavior, not a named loop or exact transcript.

Research note 515 identifies NASA `792-AAI`, cataloged by DVIDS under `Apollo11Audio`, as **Flight Director's Loop** audio including **Lunar Descent 1955–2025**. The catalog states that the material was digitized, cataloged, and archived by the Houston Audio Control Room at JSC. This provides an independent primary-recording route for calls that reached the Flight loop during descent.

## Station consequence

The supported alarm-assessment chain remains **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**. GUIDO remains an active assessment node.

The simulator may represent central display requests and distinguish MSK numeric request, DRK fast request, and FDK alert/format lookup. For Apollo 11 it may represent the documented GUIDO D/TV resource and analog chart recorders, but must not assign fixed channel identity, unsupported DRK labels/formats, FDK loading, or program-alarm behavior.

For voice research, GUIDO L/R and `792-AAI` now provide complementary station-local and Flight-loop primary recordings. Cross-comparison may establish audible relay order, but hearing a voice on either recording does not prove the originating named loop or transmit privilege. Do not map Garman's `back-room voice loop` to `FD LOOP`, `MOCR DYN`, or another Mission-G circuit without configuration evidence.

No broader station maturity is promoted. Exact internal loop assignment, complete per-console keyset privileges, GUIDO DRK mapping, FDK configuration, exact powered-descent display callups/cadence, channel identity, and exact per-alarm wording/timing remain unresolved.

## Recovery target

Inspect restored GUIDO L/R around 1201/1202 and cross-compare with NASA `792-AAI` lunar-descent Flight Director-loop audio. PHO-TN401 remains at the **Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, Box 078-65/66**. A Mission-G-effective station/keyset/display record remains the discriminating configuration target.

## Sources

- NASA/MSC, _Flight Mission Rules, Apollo 11_: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11MissionRules.pdf
- NASA/JSC, NASA TN D-7685: https://ntrs.nasa.gov/citations/19740015284
- NASA/MSFC, _Saturn V Flight Manual, SA-507_: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap12fj/pdf/a12_sa507-flightmanual.pdf
- NASA History Division, _News & Notes_ 35(3): https://www.nasa.gov/wp-content/uploads/2023/01/NewsNotes-35-3-Fall-2018.pdf
- Apollo in Real Time, Apollo 11 Mission Control Audio: https://apolloinrealtime.org/11/MOCRviz/MOCRviz.html
- DVIDS / NASA, `Apollo11Audio`, `792-AAI`: https://www.dvidshub.net/audio/32176/apollo-11
- NASA JSC Oral History Project, John R. Garman: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/GarmanJR/GarmanJR_3-27-01.pdf

## Evidence status

- **DOCUMENTED / SUFFICIENT:** Apollo-11-specific MSK-1137 field semantics; guidance-software back-room → GUIDO relationship; CAPCOM-mediated crew disposition.
- **DOCUMENTED / PRIMARY PARTICIPANT:** unnamed back-room voice-loop alarm advice; Bales checks broader data before GO; later `Same type` relay recollection.
- **DOCUMENTED / MISSION-SPECIFIC:** Apollo 11 MOCR loop vocabulary/internal-versus-A/G separation.
- **DOCUMENTED / PRIMARY / MISSION-G-SPECIFIC DISPLAY RESOURCE:** one GUIDO D/TV channel in prelaunch minimum; two GUIDO analog chart recorders highly desirable on D/TV.
- **DOCUMENTED / MISSION-SPECIFIC ARCHIVAL:** Historical Recorder #1 channels 21/22 map to GUIDO L/R, positions 018/019.
- **DOCUMENTED / PRIMARY-AUDIO RECOVERY ROUTE:** restored GUIDO L/R plus NASA `792-AAI` Flight Director-loop lunar-descent audio.
- **DOCUMENTED / PRIMARY TECHNICAL:** talk/listen versus monitor-only circuit architecture.
- **DOCUMENTED / PRIMARY NASA / APOLLO-GENERIC:** display-request/channel-attach modes.
- **DOCUMENTED / PRIMARY / NEAR-CONTEMPORARY GENERIC:** DRK fast-request and FDK alert-to-format-code semantics.
- **RESTRICTED TO NAVIGATION:** automated/derivative transcripts; direct audio verification required.
- **UNRESOLVED / MISSION-G-SPECIFIC:** named GUIDO/support loop, exact per-alarm wording/timing/overlap, complete keyset privilege matrix, GUIDO DRK labels/format mapping, FDK configuration, exact powered-descent display callups/cadence, and channel identity.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 and Mission-G-effective station/keyset/display configuration.
- **UNCHANGED:** Apollo 13 station maturity.
