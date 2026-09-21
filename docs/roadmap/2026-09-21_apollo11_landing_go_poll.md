# Roadmap continuation — Apollo 11 landing GO poll workflow

Date: 2026-09-21
Parent: `docs/roadmap/2026-09-21_apollo11_lr_convergence_monitoring.md`

## Bounded question

What station-specific voice workflow can be established for the Apollo 11 landing GO, and does that evidence prove a separate LR-convergence declaration by GUIDO?

## Primary-source result

The surviving Apollo 11 descent audio establishes a distinct **FLIGHT-led go/no-go poll for landing** late in powered descent. Gene Kranz calls the poll; the front-room stations answer in sequence: RETRO, FIDO, GUIDANCE, CONTROL, TELCOM, GNC, EECOM, and SURGEON. After the affirmative responses, FLIGHT tells CAPCOM that the team is go for landing; Charlie Duke then transmits the landing GO to Eagle. The primary Apollo 11 technical air-to-ground transcript independently preserves the crew-facing end of that chain: CAPCOM's landing-GO transmission and the crew acknowledgement.

This is enough to implement the landing GO as a **team poll → FLIGHT decision/handoff → CAPCOM crew call**, rather than an invented direct GUIDO-to-crew procedure.

The evidence does **not** establish a separate spoken `LR converged` call from GUIDO immediately before the poll. GUIDANCE's affirmative poll response proves that GUIDANCE participated in the landing GO decision, but it does not identify which display fields or internal support-room inputs Steve Bales used for that response. The previously documented LR acceptance/convergence sequence therefore remains an input context, not a newly invented voice protocol.

## Implementation consequence

For an Apollo 11 reference descent, the simulator may model the late-descent landing gate as:

`FLIGHT initiates landing go/no-go poll → named front-room controllers return status → FLIGHT commits team GO → CAPCOM transmits GO for landing → crew acknowledges`

GUIDANCE must be included in the poll. Do not encode `GUIDO declares LR converged` as a prerequisite call unless a separate primary controller-loop or procedure source is recovered.

This poll is distinct from the earlier GO for powered descent and from subsequent program-alarm calls.

## Evidence boundary

- The primary air-to-ground transcript identifies CAPCOM/crew speech but does not transcribe the internal controller loop.
- The internal poll is preserved in the Apollo 11 descent audio record and reproduced in later NASA-supported historical presentations; it identifies the called station positions and FLIGHT/CAPCOM handoff.
- Exact Mission-G CRT fields, parameter routing, and any back-room-to-GUIDANCE LR-convergence call remain unresolved/BLOCKED under the existing archival boundary.

## Next bounded target

Research the **1201/1202 program-alarm decision chain during the same descent** from primary controller/audio and Apollo-11-effective alarm/procedure documentation: specifically distinguish the AGC support-room assessment, GUIDANCE recommendation, FLIGHT disposition, and CAPCOM crew call. Do not generalize later recollections where the contemporary record is sufficient.

## Sources

- NASA, *Apollo 11 Technical Air-to-Ground Voice Transcription (GOSS NET 1)*, July 1969: https://ntrs.nasa.gov/citations/20160014392
- NASA Apollo Lunar Surface Journal / Apollo Flight Journal descent material; Apollo 11 PDI-to-touchdown presentation includes the Flight Director loop with crew voice. NASA's 2022 *Apollo Lunar Landing Experience Report* presentation points researchers to this combined Apollo 11 descent record: https://www.nasa.gov/wp-content/uploads/2023/06/eppler-slides-apollo-lunar-landing-experience-report-20070-r4.pdf
- Don E. Wilhelms, *To a Rocky Moon: A Geologist's History of Lunar Exploration*, University of Arizona Press/USGS historical account, reproduced by Lunar and Planetary Institute, for an independent published transcription of the landing poll: https://www.lpi.usra.edu/publications/books/rockyMoon/12Chapter11.pdf

## Evidence status

- **DOCUMENTED / PRIMARY AUDIO:** FLIGHT-led station poll and FLIGHT→CAPCOM landing-GO handoff.
- **DOCUMENTED / PRIMARY TRANSCRIPT:** CAPCOM transmits the landing GO to Eagle and the crew acknowledges.
- **DOCUMENTED:** GUIDANCE is a voting station in the landing poll.
- **UNRESOLVED:** any separate GUIDO LR-convergence declaration, support-room call chain, or exact display basis for GUIDANCE's vote.