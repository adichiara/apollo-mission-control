# Apollo 13 ASPO 45 CRT section: direct inspection

Date: 2026-09-11
Status: REVIEWED-PARTIAL — identifiers, layout pages, and selected LM definitions visually verified; complete field transcription and cross-mission comparison pending.

## Source and reproducibility

AC Electronics, *Apollo 13 Guidance & Navigation Summary*.
- [Flight Journal index](https://apollojournals.org/afj/ap13fj/a13-documents.html)
- [Full scan](https://apollojournals.org/afj/ap13fj/pdf-hr/a13-ac-elect-g-n-summary.pdf)
- Downloaded size: 256,134,043 bytes; 570 PDF pages.
- SHA-256: `81a4f6b54cd8cfe67fce3fe863045b9ee85dfa5d558bf3cfd46c5fd45fc9921b`.
- Page numbers below are **one-based PDF pages**, followed by printed section labels.
- PDF text extraction returned no useful text. Findings were checked against rendered images, not inferred from OCR.
- The web reader rejected the file for size; direct download and local rendering succeeded. This supersedes the earlier extraction-blocker status.
- Full scan mirroring remains undecided. The source URL, hash, and page map allow this inspection to be reproduced.

## Verified page map

| PDF page | Printed page | Content |
|---|---|---|
| 179 | ASPO-1 | Section title; MSK 683 (CM), 966 (CM), 1123 (LM), 1137 (LM) |
| 180 | ASPO-2 | 0683 layout: CSM GNC PRIMARY TAB |
| 181 | ASPO-3 | MSK 683 definition page; full transcription pending |
| 182 | ASPO-4 | 0966 layout: CMC COMMON H/S |
| 183–184 | ASPO-5–6 | Definition pages following 0966; full transcription pending |
| 185 | ASPO-7 | Intentional blank page |
| 186 | ASPO-8 | 1123 layout: LM GUID, CONTROL AND PROP RT |
| 187 | ASPO-9 | MSK 1123 definitions |
| 188 | ASPO-10 | 1137 layout |
| 189–190 | ASPO-11–12 | MSK 1137 definitions and continuation |

The section ends before Launch and Burn Schedule on PDF page 191. Rotate the sideways pages clockwise for reading.

**DOCUMENTED:** the Apollo 13 summary contains these four identifiers and their layouts. This does not establish that every field was unchanged from Apollo 11, or that the summary captures every operational revision.

## Selected mission-specific LM definitions

From ASPO-9 / PDF 187:

- GET and MET are separately defined as ground elapsed time and mission elapsed time. Do not silently merge their historical labels.
- LGC FMT identifies the transmitted downlist; SITE identifies the receiving site.
- TGO represents time until engine cutoff; TTF/8 represents time until end of a descent-program phase.
- PGNS RATE, RGA, and ASA represent distinct rate sources; their units are degrees/second.
- LGC DEL VEL is PIPA output for a two-second interval, in feet/second. This is a measurement interval, **not evidence of CRT refresh cadence**.
- Landing radar velocity/range validity, rendezvous-radar data, AGS DEDA, LGC restart count, and DSKY information appear on the page.

From ASPO-11–12 / PDF 189–190:

- WT is LM mass; RTCC is RTCC-computed LM or LM+CSM mass; CSM is CSM mass. Display units are pounds.
- ACT ΔV is explicitly ground-computed actual delta velocity gained.
- BIAS in the attitude section is a ground-computed PIPA free-fall bias. A separate BIAS in the power section means 28-V bias voltage: labels alone cannot uniquely identify a parameter.
- Throttle selection, manual/automatic/total command, actuator position, commanded thrust, and chamber pressure are distinct quantities.
- Radar validity and comparisons between landing-radar measurements and guidance quantities are present.
- Restart count, alarm codes, program/verb/noun, mode discretes, voltages, and temperatures are also included.

## Consequences for the simulation specification

These are source-derived requirements, not an authorization to begin implementation:

1. Give each field a display ID and field identity, source page, units, and data origin; repeated labels are insufficient keys.
2. Preserve downlist/site context and distinguish ground-computed products from spacecraft telemetry.
3. Keep sample/accumulation intervals distinct from transport and display refresh rates.
4. Preserve multiple measurements and validity indications rather than replacing them with a single system-health value.
5. Use the Apollo 13 layouts as mission-specific references; compare Apollo 11 separately before defining shared fields.

## Remaining work

- Transcribe every field and visually verify ambiguous glyphs, precision, and octal/decimal notation.
- Map each field to telemetry/downlist/ground-processing sources.
- Establish refresh cadence, stale-data behavior, operational revisions, and station access.
- Compare Apollo 11 and Apollo 13 page by page.
- Keep station maturity unchanged until console and operational evidence meet the existing criteria.
