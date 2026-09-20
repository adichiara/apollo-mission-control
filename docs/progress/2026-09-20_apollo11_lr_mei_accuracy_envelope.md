# Progress — Apollo 11 landing-radar MEI accuracy envelope

Date: 2026-09-20

## Work completed

The next unresolved landing-radar item was whether a primary source could provide a quantitative, mission-relevant error magnitude without inventing a stochastic distribution.

A NASA primary-source PDF (NTRS 19700004489) contains **Table 1, Landing Radar Specifications**, explicitly reproduced from Grumman Aircraft Engineering Corporation specification **LSP-470-2D, Master End Item Specification for Lunar Module**. The table gives landing-radar accuracy requirements as 3-sigma limits.

Recovered range limits:

- 2,000 ft < range < 25,000 ft: 3-sigma error = `1.4% + 15 ft`;
- 10 ft < range < 2,000 ft: 3-sigma error = `1.4% + 5 ft`.

The table also gives altitude-banded 3-sigma velocity-component accuracy limits to the LGC. Because the available OCR is imperfect in the column alignment, the individual velocity cells are not transcribed into executable data in this pass; the source must be inspected visually before those cells are encoded.

NASA TN D-6849 supplies the necessary interpretation guardrail. During LM-5 functional verification, a one-count velocity bias caused by a logic race was corrected before flight. The same report states that the Gaussian distribution assumed for Doppler-spectrum-simulator test limits had to be corrected because the simple simulator approximation placed more energy in the tails. Apollo 11 flight data were subsequently reported within specification limits except for a few low/near-zero-Doppler points where tracking was not expected.

## Result

The project now has a primary-source **quantitative performance envelope** for the landing radar. It still does **not** have evidence for a historical probability distribution or random process.

Therefore:

1. LSP-470-2D limits may be used for validation/bounds after exact cells are verified;
2. a `3 sigma` label must not be converted automatically into Gaussian `sigma = limit / 3` noise;
3. no historical stochastic generator has been added;
4. the unresolved item is narrowed from "no numerical error basis" to "no flight-effective stochastic distribution/process beyond the MEI envelope";
5. MSC-69-EG-14 remains worth retrieving for adjacent-effectivity detail, but is no longer the only quantitative lead.

## Documentation synchronized

- focused Apollo 11 landing-radar roadmap;
- landing-radar station-status addendum;
- Apollo 11 / Luminary 1A source-catalog addendum;
- this progress record.

## Next discriminating evidence

Visually inspect the LSP-470-2D velocity-accuracy table before encoding individual component limits. Continue searching LM-5 qualification/acceptance and Apollo 11 flight-data reduction material for bias, correlation, quantization, dropout, and distribution evidence. In parallel, the higher-level MSK-1137 per-field D/L-versus-RTCC routing and GUIDO console-workflow gaps remain unresolved.

## Evidence status

**DOCUMENTED PERFORMANCE ENVELOPE; STOCHASTIC PROCESS UNRESOLVED/BLOCKED.** The primary material establishes 3-sigma accuracy requirements, while TN D-6849 explicitly cautions against treating the relevant simulator test distribution as simply Gaussian. No unsupported random-error model has been introduced.
