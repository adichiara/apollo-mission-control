# Research note 518 — Apollo 11 air-ground alarm timing anchors

Date: 2026-09-24

## Question

Can the primary Apollo 11 GOSS NET 1 transcript close the crew/CAPCOM side of the descent-alarm chronology without implying unsupported internal-loop timing?

## Primary-source finding

Yes. NASA's contemporary _Apollo 11 Technical Air-to-Ground Voice Transcription (GOSS NET 1)_ gives Mission-G-specific radio timestamps around the alarm sequence.

For the first 1202 window, the transcript records the crew identifying `1202` at GET **102:38:30** and again at **102:38:32**, Armstrong asking for a reading on the 1202 program alarm at **102:38:48**, and CAPCOM answering that the ground is GO on the alarm at **102:38:53**.

For the later 1201 window, the transcript records CAPCOM acknowledging the program alarm at **102:42:19**, Armstrong identifying `1201` at **102:42:24**, and CAPCOM responding at **102:42:25**: `Roger. 1201 alarm. We're GO. Same type. We're GO.`

The same transcript records CAPCOM at **102:42:58** acknowledging a subsequent 1202.

## Cross-source timing consequence

The Apollo 11 Mission Report event table (note 516) places the first 1202 computer/event anchor at **102:38:22** and the 1201 computer/event anchor at **102:42:18**. The air-ground record therefore demonstrates directly that computer/event time and spoken radio time are not interchangeable:

- first 1202: event anchor 102:38:22 → explicit crew `1202` at 102:38:30 (8 s later) → CAPCOM GO at 102:38:53;
- 1201: event anchor 102:42:18 → CAPCOM alarm acknowledgement at 102:42:19 → Armstrong `1201` at 102:42:24 → CAPCOM GO/same-type disposition at 102:42:25.

These intervals bound the **observable radio path only**. They do not establish when Garman spoke, when Bales decided, which internal circuit carried either call, or whether an internal utterance overlapped a crew transmission. Those require direct GUIDO L/R and `792-AAI` inspection on their native timing.

## Simulator consequence

Do not collapse alarm generation, crew recognition/report, ground internal assessment, and CAPCOM disposition into one timestamp. Model them as distinct events. The Mission-G radio timestamps above may be used as reference-validation anchors; internal decision latency remains unresolved rather than guessed.

## Sources

- NASA, _Apollo 11 Technical Air-to-Ground Voice Transcription (GOSS NET 1)_, NTRS 20160014392, tape 66/7–66/10, pp. 312–315: https://ntrs.nasa.gov/citations/20160014392
- NASA, _Apollo 11 Mission Report_, event chronology used in research note 516.

## Evidence status

- **DOCUMENTED / PRIMARY / MISSION-G-SPECIFIC:** crew/CAPCOM alarm-radio timestamps above.
- **DOCUMENTED:** event time and voice time are distinct observables.
- **OPEN:** exact Garman→Bales→Flight timing, overlap, named internal circuit, and clock reconciliation between internal recordings.