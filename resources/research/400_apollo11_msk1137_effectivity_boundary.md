# 400 — Apollo 11 MSK-1137 effectivity boundary

Date: 2026-09-20

## Question

Does the surviving Apollo-11-effective evidence establish which controller requested MSK-1137, which request device was used, or the exact powered-descent request sequence?

## Primary-source findings

The AC Electronics *Apollo 11 Guidance and Navigation System Manual* explicitly groups MSK-683 (CM), MSK-966 (CM), MSK-1123 (LM), and MSK-1137 (LM) under `ASPO 45 CRT DISPLAYS`, and supplies the detailed MSK-1137 field definitions. This is strong Apollo-11-effective authority for the existence and content of the LM display format.

The same four-format `ASPO 45 CRT DISPLAYS` grouping survives in the Apollo 12 AC Electronics manual and the NASA-hosted Apollo 15 Delco manual. That continuity is useful as configuration-family evidence: MSK-1137 was not merely an Apollo-11-only ad hoc page. It does **not** identify the Apollo 11 MOCR station that requested it or the physical request device used at that station.

The Apollo 12 Saturn V Flight Manual remains the strongest recovered primary description of the request-device semantics: a DRK could request a specific RTCC format through a labeled PBI, while an MSK in display-request mode provided equivalent capability using thumbwheel selection. Its effectivity is Apollo 12, so those semantics cannot be converted into an Apollo 11 GUIDO hardware assignment.

A targeted search for Apollo-11-effective GUIDO/DRK/MSK assignment evidence did not recover a primary source that ties GUIDO to MSK-1137 or specifies a descent request sequence. PHO-TN401 remains the identified mission-specific display-usage source and remains inaccessible in the public digital corpus located to date.

## Consequence

The evidence now supports three separate claims and no stronger one:

1. **Apollo 11 had MSK-1137 as an LM CRT display format with documented field semantics.**
2. **Apollo-era MCC architecture supported MSK and DRK display-request mechanisms; Apollo 12 documents their relationship.**
3. **Apollo 11 GUIDO device assignment, exact request sequence, and powered-descent selection of MSK-1137 remain unresolved.**

Therefore the simulator must not render a historically labeled Apollo 11 GUIDO DRK button, MSK thumbwheel sequence, or automatic MSK-1137 selection until Apollo-11-effective station evidence is recovered. A project-facing display may use the sourced MSK-1137 field definitions only if its request mechanics remain explicitly reconstructed/unknown rather than presented as exact hardware workflow.

## Next discriminating evidence

- PHO-TN401 direct inspection (archival retrieval/authenticated scan).
- Apollo 11 Flight Control Operations Handbook material or console-configuration drawings that explicitly assign GUIDO display-request hardware/formats.
- Mission-G controller procedures or shift material that records powered-descent CRT format requests.

## Sources

Primary:
- AC Electronics, *Apollo 11 Guidance and Navigation System Manual*: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- AC Electronics, Apollo 12 manual: https://www.ibiblio.org/apollo/Documents/apollo12_delco.pdf
- Delco Electronics, Apollo 15 manual (NASA): https://www.nasa.gov/wp-content/uploads/static/history/alsj/a15/A15Delco.pdf
- NASA, *Apollo 12 Saturn V Flight Manual*, SA-507: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap12fj/pdf/a12_sa507-flightmanual.pdf

Archival target:
- Costis, Ortolani & Moreland, *NASA MCC Display/Control System Usage and Effectiveness, Apollo 11*, PHO-TN401, 24 Dec 1969; Box 078-65/66, JSC History Collection, University of Houston-Clear Lake.

## Evidence status

- **DOCUMENTED:** Apollo-11-effective MSK-1137 existence and field definitions.
- **DOCUMENTED:** MSK-1137 belongs to a recurring ASPO 45 LM CRT-display family across Apollo 11, 12, and 15 manuals.
- **DOCUMENTED, ADJACENT EFFECTIVITY:** Apollo 12 DRK/MSK request-device semantics.
- **BLOCKED:** direct PHO-TN401 inspection.
- **UNRESOLVED:** Apollo 11 GUIDO DRK/MSK assignment, exact request sequence, and powered-descent display selection.
