# Station-status addendum — Apollo 11 descent monitoring products

Date: 2026-09-23
Parent: `docs/STATION_RESEARCH_STATUS.md`

The Apollo 13 station maturity table remains unchanged. This addendum applies only to the D-024 Apollo 11 powered-descent architecture reference.

## Source-backed boundary

NASA/MSC 70-FM-20 preserves Apollo 11 `AGS−PGNCS` and `MSFN−PGNCS` descent comparisons. The mission-specific AC Electronics Apollo 11 manual defines `MSK-1137` ground-display fields relevant to powered descent/program alarms. The air-ground transcript establishes crew request/CAPCOM disposition, while Jack Garman's NASA oral history establishes guidance-software back-room support to GUIDO/Steve Bales.

Apollo 11 Flight Mission Rules document Mission-G loop vocabulary. PHO-FAM001 documents local conference/intersite loops and talk/listen versus monitor-only keyset circuits; Garman supplies compatible participant evidence for support-room talk/listen semantics and restricted A/G transmit authority. Exact Mission-G station-to-loop assignment remains unresolved.

NASA History Division reproduces an original Apollo 11 Historical Recorder #1 track sheet assigning channels 21/22 to `GUIDO [L]/[R]`, positions 018/019. Research note 510 now establishes an accessible primary-audio recovery route: the restored Apollo 11 Mission Control corpus exposes GUIDO L/R recordings and documents IRIG-B timing provenance. Its automated transcripts are explicitly imperfect and are navigation aids only.

## Station consequence

The supported alarm-assessment chain remains **guidance-software back-room support → GUIDO/Bales → FLIGHT/ground decision chain → CAPCOM → crew**.

The next station-level evidence can come directly from the restored GUIDO L/R audio for audible participants and sequence. However, a voice captured on a GUIDO station recording does not prove which named conference loop supplied it or whether the speaker had transmit privilege on that loop. Do not grant back-room AGC support direct A/G transmit authority or assign Bales/Garman traffic to `FD LOOP`, `MOCR DYN`, or another named loop from the present evidence.

No broader station maturity is promoted. Exact Apollo 11 internal loop assignment, complete per-console keyset privileges, station display request procedure, DRK mapping, routing, cadence, and directly verified per-alarm call timing remain unresolved.

## Recovery target

Inspect restored GUIDO L/R audio around 1201/1202. PHO-TN401 remains at the **Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, Box 078-65/66**. A Mission-G-effective station/keyset record remains the discriminating voice-routing target.

## Sources

- NASA History Division, _News & Notes_ 35(3): https://www.nasa.gov/wp-content/uploads/2023/01/NewsNotes-35-3-Fall-2018.pdf
- Apollo in Real Time, Apollo 11 Mission Control Audio: https://apolloinrealtime.org/11/MOCRviz/MOCRviz.html
- NASA, _Apollo 11 Mission Audio_: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11MissionAudio.html

## Evidence status

- **DOCUMENTED / SUFFICIENT:** Apollo-11-specific MSK-1137 field semantics; guidance-software back-room → GUIDO relationship; CAPCOM-mediated crew disposition.
- **DOCUMENTED / MISSION-SPECIFIC:** Apollo 11 MOCR loop vocabulary/internal-versus-A/G separation.
- **DOCUMENTED / MISSION-SPECIFIC ARCHIVAL:** Historical Recorder #1 channels 21/22 map to GUIDO L/R, positions 018/019.
- **DOCUMENTED / PRIMARY-AUDIO RECOVERY ROUTE:** restored GUIDO L/R audio with IRIG-B timing provenance.
- **DOCUMENTED / PRIMARY TECHNICAL:** talk/listen versus monitor-only circuit architecture.
- **RESTRICTED TO NAVIGATION:** automated Mission Control transcripts; direct audio verification required.
- **UNRESOLVED:** exact station-to-loop assignment, complete keyset privilege matrix, live request/routing/DRK mapping/cadence, and directly verified internal alarm-call sequence.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 and Mission-G-effective station/keyset configuration.
- **UNCHANGED:** Apollo 13 station maturity.
