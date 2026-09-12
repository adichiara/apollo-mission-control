# Apollo 13 PC+2 GUIDO Presentation Sources

Status: active source supplement for the first player-facing GUIDO rendering.

## 1. Apollo 13 Guidance & Navigation Summary — ASPO 45 CRT Displays

- **Organization:** AC Electronics / Apollo 13 mission documentation
- **Source class:** PRIMARY, mission-specific
- **Use:** Confirms Apollo 13 MSK 1123 and 1137 layouts and definition families relevant to LGC/guidance status, program/alarm information, rates, velocity-change/guidance quantities, and processed comparisons.
- **Direct-inspection record:** `resources/research/029_apollo13_aspo45_direct_inspection.md`
- **Limitation:** Exact PC+2 GUIDO display-selection sequence, coordinates, refresh cadence, and field-by-field routing are not fully reconstructed.

## 2. MIT Instrumentation Laboratory R-567 — LUMINARY 1C Data Links

- **Title:** *Guidance System Operations Plan for Manned LM Earth Orbital and Lunar Missions Using Program LUMINARY 1C (LM131 Rev. 1), Section 2 — Data Links*
- **Revision:** 8
- **Date:** March 1970
- **Source class:** PRIMARY, Apollo 13 LM software-era
- **Use:** Supports program-dependent LGC downlinks; P27/update verification; DSKY/display-table state; failure/restart status; desired/actual guidance quantities; PIPA/velocity-change data; TIG/maneuver quantities; snapshot/coherency behavior.
- **Public scan:** https://www.ibiblio.org/apollo/NARA-SW/R-567-sec2-rev8.pdf
- **Limitation:** Downlink membership does not prove verbatim appearance on a specific GUIDO CRT field.

## 3. Apollo 13 Mission Operations Report

- **Organization:** NASA Manned Spacecraft Center / Flight Control Division
- **Date:** 28 April 1970
- **Source class:** PRIMARY, mission-specific
- **Use:** Establishes GUIDO responsibility in guidance/computer/alignment monitoring and records nominal PC+2 PGNS residuals after the burn.
- **Limitation:** Does not provide a complete CRT field/coordinate transcription for the implemented project products.

## Repository cross-checks

- `resources/research/032_apollo13_lm_crt_field_provenance.md`
- `resources/research/035_apollo13_msk1123_field_provenance.md`
- `resources/research/052_pc2_controller_product_projection.md`
- `resources/research/074_pc2_guido_player_presentation_boundary.md`

## Implementation rule

Use exact Apollo terminology only where semantics are sufficiently established. Otherwise use a clearly labeled project rendering while preserving value, units, validity, source layer, and provenance. Never expose hidden integrity metadata or turn deferred implementation fields into simulated telemetry failures.
