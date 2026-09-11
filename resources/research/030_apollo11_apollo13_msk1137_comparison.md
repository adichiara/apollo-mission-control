# Apollo 11 / Apollo 13 MSK 1137 comparison

Date: 2026-09-11.
Status: directly observed differences between the two guidance-summary scans; not certification of every operational mission revision.

## Sources inspected

- [Apollo 11 AC Electronics summary](https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf): PDF 205 (layout), 206–207 (definitions). 460-page scan; SHA-256 `239401d3979da31a6510615014829a52570c21a84c1371ea4debeea765b1c9d2`.
- [Apollo 13 AC Electronics summary](https://apollojournals.org/afj/ap13fj/pdf-hr/a13-ac-elect-g-n-summary.pdf): PDF 188–190 / ASPO-10–12.
- Both scans were rendered and visually compared. Apollo 11 OCR was used for navigation only.
- Page references are one-based PDF page numbers. Apollo 13 source hash is in note 029.

## Principal finding

The identifier **1137** is retained, but its information is not unchanged. The common spatial structure is a useful comparison framework; it is insufficient evidence for using one mission's entire field set for the other.

| Area | Apollo 11 evidence | Apollo 13 evidence | Implication |
|---|---|---|---|
| Attitude-section rows after LOCAL | CMD and SERVO | BIAS and OCTAL | Same row position now carries different information |
| Meaning of those rows | Gimbal/gyro/CDU commands in degrees; servo errors in volts | Ground-computed PIPA bias in cm/s²; octal register loads | More than a label change; data origin, units and formatting change |
| Landing-radar velocity labels | VXB, VYB, VZB; body-axis coordinates | VXS, VYS, VZS; converted to stable-member coordinates | A renderer cannot reuse the values without a validated coordinate transformation |
| Landing-radar altitude comparison definitions | PGNS-computed altitude in feet; AGS-computed altitude in nautical miles | Radar minus LGC altitude and radar minus AGS altitude, both in feet | Absolute estimates and residuals must remain distinct |
| Guidance velocity comparison columns | Layout headings PGNS and AGS | Layout markings PGNSΔ and AGSΔ; definitions describe radar-minus-guidance velocities with lunar-gravity correction | Apollo 13 residual semantics are explicit; do not retroactively assign them to Apollo 11 |
| LGC error area | LGC ERR; attitude-error definition | Error/rate alternatives in definition page | Selection logic and exact label mask still require research |

Sources for all rows: Apollo 11 PDF 205–207 compared with Apollo 13 PDF 188–190. These are document differences. A later revision of an Apollo 11 source could change interpretation; no such revision is established here.

## What appears continuous in the inspected material

Both documents include throttle commands and chamber-pressure indication, mass fields including RTCC-computed mass, channel/flagword information, warning/program status, DSKY registers, rate and delta-velocity information, radar validity, and electrical/temperature indications.

This is continuity of field families, not a claim that all masks, sampling, calculations, or operating behavior match. Even matching headings require field-level checking.

## Supporting check on 1123

Apollo 11 PDF 204 and Apollo 13 PDF 187 preserve many matching definition families: separate GET/MET/AGS/LGC clocks, downlist/site identity, body rates, attitudes, radar information, AGS DEDA, and DSKY. The Apollo 11 page also defines a two-second PIPA interval. This limited inspection does not certify complete 1123 equivalence; precision/masks and the layout must still be compared systematically.

## Design consequence

The established Apollo 13 default plus mission-specific profiles remains appropriate. These findings supply concrete evidence for profile overrides at the **field** level:

- identity and location;
- physical meaning;
- origin and transformation;
- units and numerical representation;
- reference frame;
- validity behavior.

Do not select one generic “MSK 1137” field model for both missions. Record an Apollo 11 source profile and Apollo 13 source profile, sharing only individually verified properties. This is a specification recommendation based on evidence, not a new simplification or first-scenario selection.

## Deliverables and next work

A [normalized Apollo 13 field inventory](031_apollo13_msk1137_field_inventory.md) covers the named definition groups across ASPO-11–12. It is not an executable parameter dictionary.

Next:
1. Complete the 1123 field and precision comparison.
2. Transcribe and compare CM 683/966.
3. Resolve 1137 calculations and downlink mappings before creating any live display.
