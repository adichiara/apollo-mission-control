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

Research note 515 identifies NASA `792-AAI`, cataloged by DVIDS under `Apollo11Audio`, as **Flight Director's Loop** audio including **Lunar Descent 1955–2025**. This provides an independent primary-recording route for calls that reached the Flight loop during descent.

Research note 516 establishes the Mission-G event anchors for audio inspection from NASA/MSC _Apollo 11 Mission Report_ table 5-I: 1202 at `102:38:22`, 1202 at `102:39:02`, 1201 at `102:42:18`, 1202 at `102:42:43`, and 1202 at `102:42:58`; P64 entry is `102:41:32` and P66 entry `102:43:22`. These are postflight computer/event timestamps and are not promoted to exact spoken-call timestamps.

## Station consequence

The supported alarm-assessment chain remains **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**. GUIDO remains an active assessment node.

The simulator may represent central display requests and distinguish MSK numeric request, DRK fast request, and FDK alert/format lookup. For Apollo 11 it may represent the documented GUIDO D/TV resource and analog chart recorders, but must not assign fixed channel identity, unsupported DRK labels/formats, FDK loading, or program-alarm behavior.

For voice research, GUIDO L/R and `792-AAI` provide complementary station-local and Flight-loop primary recordings. Use the Mission Report alarm times as search anchors, not as voice timestamps. Hearing a voice on either recording does not prove the originating named loop or transmit privilege. Do not map Garman's `back-room voice loop` to `FD LOOP`, `MOCR DYN`, or another Mission-G circuit without configuration evidence.

No broader station maturity is promoted. Exact internal loop assignment, complete per-console keyset privileges, GUIDO DRK mapping, FDK configuration, exact powered-descent display callups/cadence, channel identity, exact per-alarm spoken wording/timing, and recording-clock reconciliation remain unresolved.

## Recovery target

Inspect restored GUIDO L/R and NASA `792-AAI` around the five Mission Report alarm anchors with enough lead/lag to capture the complete relay sequence; reconcile recording clocks before freezing timing. PHO-TN401 remains at the **Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, Box 078-65/66**. A Mission-G-effective station/keyset/display record remains the discriminating configuration target.

## Sources

- NASA/MSC, _Apollo 11 Mission Report_, MSC-00171: https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A11_MissionReport.pdf
- NASA/MSC, _Flight Mission Rules, Apollo 11_: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11MissionRules.pdf
- NASA/JSC, NASA TN D-7685: https://ntrs.nasa.gov/citations/19740015284
- NASA/MSFC, _Saturn V Flight Manual, SA-507_: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap12fj/pdf/a12_sa507-flightmanual.pdf
- NASA History Division, _News & Notes_ 35(3): https://www.nasa.gov/wp-content/uploads/2023/01/NewsNotes-35-3-Fall-2018.pdf
- Apollo in Real Time, Apollo 11 Mission Control Audio: https://apolloinrealtime.org/11/MOCRviz/MOCRviz.html
- DVIDS / NASA, `Apollo11Audio`, `792-AAI`: https://www.dvidshub.net/audio/32176/apollo-11
- NASA Apollo Lunar Surface Journal, landing chronology: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11.landing.html
- NASA JSC Oral History Project, John R. Garman: https://historycollection.jsc.nasa.gov/JSCHistoryPortal/history/oral_histories/GarmanJR/GarmanJR_3-27-01.pdf

## Evidence status

- **DOCUMENTED / SUFFICIENT:** Apollo-11-specific MSK-1137 field semantics; guidance-software back-room → GUIDO relationship; CAPCOM-mediated crew disposition.
- **DOCUMENTED / PRIMARY / MISSION-G-SPECIFIC TIMING:** five alarm-event anchors and P64/P66 boundaries; not exact spoken timing.
- **DOCUMENTED / PRIMARY PARTICIPANT:** unnamed back-room voice-loop alarm advice; Bales checks broader data before GO; later `Same type` relay recollection.
- **DOCUMENTED / MISSION-SPECIFIC:** Apollo 11 MOCR loop vocabulary/internal-versus-A/G separation.
- **DOCUMENTED / PRIMARY / MISSION-G-SPECIFIC DISPLAY RESOURCE:** one GUIDO D/TV channel in prelaunch minimum; two GUIDO analog chart recorders highly desirable on D/TV.
- **DOCUMENTED / MISSION-SPECIFIC ARCHIVAL:** Historical Recorder #1 channels 21/22 map to GUIDO L/R, positions 018/019.
- **DOCUMENTED / PRIMARY-AUDIO RECOVERY ROUTE:** restored GUIDO L/R plus NASA `792-AAI` Flight Director-loop lunar-descent audio.
- **DOCUMENTED / PRIMARY TECHNICAL:** talk/listen versus monitor-only circuit architecture.
- **DOCUMENTED / PRIMARY NASA / APOLLO-GENERIC:** display-request/channel-attach modes.
- **DOCUMENTED / PRIMARY / NEAR-CONTEMPORARY GENERIC:** DRK fast-request and FDK alert-to-format-code semantics.
- **RESTRICTED TO NAVIGATION:** automated/derivative transcripts; direct audio verification required.
- **UNRESOLVED / MISSION-G-SPECIFIC:** named GUIDO/support loop, exact per-alarm spoken wording/timing/overlap, recording-clock reconciliation, complete keyset privilege matrix, GUIDO DRK labels/format mapping, FDK configuration, exact powered-descent display callups/cadence, and channel identity.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 and Mission-G-effective station/keyset/display configuration.
- **UNCHANGED:** Apollo 13 station maturity.
