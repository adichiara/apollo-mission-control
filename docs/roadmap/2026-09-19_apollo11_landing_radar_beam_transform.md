# Apollo 11 landing-radar beam-transform roadmap

Date: 2026-09-20
Updated: 2026-09-21
Parent: `docs/ROADMAP.md`

## Controlled chain

Apollo-11-effective LUMINARY 099 controls `SETPOS`, measurement-time CDU capture, Y-Z-X preparation, and `*NBSM*` direction semantics. Memo #95 controls antenna→NB beta-then-alpha semantics. The LM-5 Mission G prelaunch erasable load supplies the position-specific alpha/beta values.

## Completed

The equation-level SETPOS and SM/NB transforms are composed into the landing-radar velocity estimator chain, with a provenance-bearing LM-5 profile adapter. Mission-specific MSK-1137 evidence controls LR field identities, body-axis velocity frame, units/display masks, validity fields, and the ground-computed identity of `ACT ΔV`.

Apollo 11 MCC architecture is source-controlled as distinct spacecraft/downlink, CCATS/RTCC processing, Display/Control, and controller-presentation layers. PHO-TN401 is identified as the mission-specific Apollo 11 display-usage source but remains **BLOCKED** behind archival access.

NASA TN D-8316 separates buffered dynamic-data updates from CRT refresh and reference-slide access. PHO-FAM001 constrains the pre-Apollo-11 request transaction. NASA TN D-7685 constrains Apollo-program display-request/channel-allocation behavior, including the 36-channel computer-driven TV pool for lunar-landing missions.

Philco-Ford PHO-TR515, *Display Formats Manual* (12 Jan 1973), supplies a later-system provenance model: DTE dynamic groups carry source, coordinate/configuration, external-name, and downlist metadata. It does not establish Apollo-11-effective identifiers or tabular cadence.

A renewed inspection of the primary AC Electronics Apollo 11 MSK-1137 sheet adds one mission-effective constraint: the format itself visibly distinguishes `D/L` and `RTCC` source categories, while its field notes separately identify `ACT ΔV` as ground computed. The Apollo 11 controller display therefore cannot be modeled as a simple mirror of one spacecraft downlist. This is evidence for **mixed provenance on the mission-specific format**, not enough evidence to assign an external name/downlist/computation route to each field.

The Apollo 11 Mission Report constrains landing-radar use during powered descent: range and velocity were acquired at about 44,000 and 28,000 ft slant range; the crew decided whether to incorporate LR data based on reasonability and precalculated limits; and the report attributes two later brief tracking losses to expected zero-Doppler effects during manual maneuvering. Table 5-I closes the event-time intervals: `DATA NOT GOOD` at 102:44:11 returned `DATA GOOD` at 102:44:21, and `DATA NOT GOOD` at 102:44:59 returned `DATA GOOD` at 102:45:03. At the report's one-second event resolution these are 10-second and 4-second not-good intervals, not evidence for a generalized dropout law.

The AC Electronics Apollo 11 manual independently requires the LR `DATA GOOD` discrete to have been present for at least four seconds before range/velocity measurement tests permit state-vector updating. Historical replay therefore distinguishes radar data-good state from eligibility to resume LR-aided state updates.

MIT R-700 Vol. II closes the Apollo-11-specific onboard reasonableness gates: velocity `|delta q| <= 7.5 + 0.125 V_T` ft/s and range-derived altitude `|delta q| <= 200 + 0.125 h` ft, with the altitude test omitted above high gate. These are onboard admission rules, not MCC/GUIDO controls or an error distribution.

GAEC LSP-470-2D supplies 3-sigma LR range/velocity acceptance limits. NASA TN D-6849 supplies LM-5 flight experience and cautions against converting simulator behavior into a simple Gaussian law. NASA-CR-92466 remains a mission-period beam/Doppler mathematical-model source, not LM-5 flight-error statistics.

NASA TN D-6849 explicitly states that processed LR velocity and slant-range information was made available to the LGC in **serial binary form**, while LR information was separately supplied to LM displays as **pulse trains and dc analog voltages**. This establishes separate LGC-digital and crew-display electrical output paths.

The Apollo-era MIT/IL *LEM PGNCS Guidance System Operations Plan*, Section 3, independently exposes the LR/LGC electrical interface as two binary data-flow inputs, `LR in "1"` and `LR in "0"`, plus separate LR range/velocity-good, antenna-position, and range-low-scale discretes. AC Electronics ND-1021042 further identifies LGC `Readout command`, continuous 3,200-cps `Gate reset`, and separate range/Vx/Vy/Vz strobe pulses that enable the LR transfer gates. This constrains framing architecture: binary value is carried on the two LR data inputs while quantity selection/transfer timing is externally strobed by the LGC.

A direct check of the flown LUMINARY 099 `P20-P25.agc` now closes the software-side LR quantity-select mapping. The mission-effective lead-ins call `INITREAD` with octal `17` for `LRALT`, `16` for `LRVELZ`, `15` for `LRVELY`, and `14` for `LRVELX`. This independently ties the four LR read operations to distinct radar-selection command values in the flown program. It does **not** define the returned serial word's bit order, sign representation, bias, word length, or rounding/truncation.

**Apollo-11-effective scaling boundary:** the flown LUMINARY 099 listing supplies onboard converted/stored LR measurement bit weights. `ASSEMBLY_AND_OPERATION_INFORMATION.agc` gives low-scale altitude `1.079 ft` per low-order bit and X/Y/Z velocity low-order bit weights of `-0.6440`, `+1.212`, and `+0.8668 ft/s`; `PINBALL_NOUN_TABLES.agc` carries the corresponding constants; and `SERVICER.agc` independently labels stored `HMEAS` as `1.079 FT/BIT`. Revision-99 Memo #85 supplies a high/low altitude scale ratio of 5, so 5.395 ft/count high scale is a direct Apollo-11-effective derivation. These values control the LUMINARY-side converted measurement representation, not otherwise-unknown raw serial coding.

The later LM10-and-subsequent Apollo Operations Handbook and later R-567 revisions remain adjacent architecture cross-checks for 15-bit raw LR/LGC words and high/low raw conversion. No 15-bit Apollo 11 serial encoding is back-projected solely from those later sources.

## Next work

1. Continue seeking LM-5/Apollo-11-effective hardware-interface evidence for **raw word length, bit order, sign convention/integer bias, and rounding/truncation**. Quantity selection is now closed at the flown-software boundary (`LRVELX=14`, `LRVELY=15`, `LRVELZ=16`, `LRALT=17`, octal); do not confuse these command values with returned-data encoding.
2. Pursue Apollo-11-effective FDS/RTCC/CCATS material that maps individual MSK-1137 fields to the format's `D/L`/`RTCC` provenance categories and identifies external names/downlists or computation/logic identifiers.
3. Preserve the two Table 5-I not-good intervals as deterministic historical replay anchors and enforce the documented four-second `DATA GOOD` qualification separately; do not infer a random dropout process from them.
4. Retrieve and inspect MSC-69-EG-14 / NASA-TM-X-64374, requiring an explicit Mission-G/LM-5 applicability bridge before using any F-mission numbers.
5. Inspect NASA-CR-92466 only for model equations/beam physics; do not promote it to LM-5 stochastic-error authority without separate applicability evidence.
6. Keep Apollo 11 GUIDO exact DRK/MSK button mapping and powered-descent selection unresolved pending mission-effective station evidence.
7. Keep PHO-TN401 direct inspection **BLOCKED** pending archival retrieval/authenticated scan.
8. Keep sample/receive/process/display timestamps distinct; do not infer MCC tabular cadence from onboard LR timing.
9. Keep historical stochastic LR measurement generation **BLOCKED** until flight-effective numerical residual evidence is recovered.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** LM-5 geometry + SETPOS + measurement-time NB→SM transform through the estimator.
- **DOCUMENTED:** Apollo 11 MSK-1137 semantics and mixed `D/L`/`RTCC` provenance boundary.
- **DOCUMENTED, APOLLO 11 FLIGHT:** LR acquisition; two one-second-resolution not-good intervals; expected zero-Doppler/manual-maneuver cause.
- **DOCUMENTED, APOLLO-11-EFFECTIVE ONBOARD LOGIC:** four continuous seconds of `DATA GOOD` before LR measurement tests permit state-vector updating; Apollo-11-specific reasonableness gates.
- **DOCUMENTED, APOLLO-11-EFFECTIVE ONBOARD SCALING:** low-scale altitude `1.079 ft/bit`; derived high-scale altitude `5.395 ft/bit`; X/Y/Z velocity bit weights `-0.6440/+1.212/+0.8668 ft/s` at the converted/stored LUMINARY representation.
- **DOCUMENTED, APOLLO-11-EFFECTIVE QUANTITY SELECTION:** flown LUMINARY 099 maps `LRVELX/LRVELY/LRVELZ/LRALT` to `INITREAD` command values octal `14/15/16/17`.
- **DOCUMENTED, APOLLO-PROGRAM INTERFACE:** LR velocity/range delivered to LGC as serial binary data; two binary data-flow inputs plus LGC readout/reset/range-and-velocity strobes constrain transfer framing; separate pulse-train/dc-analog outputs feed LM displays.
- **DOCUMENTED, MISSION-PERIOD MODEL SOURCE:** NASA-CR-92466 for LR beam-bandwidth/Doppler model verification; not LM-5 flight-error statistics.
- **ADJACENT EFFECTIVITY ONLY:** later LM10/R-567 material confirms 15-bit raw LR/LGC architecture and later raw-data conversions; no complete Apollo 11 serial encoding is claimed.
- **DOCUMENTED:** Apollo MCC architectural separation and D/TV buffered-update behavior.
- **BLOCKED:** direct PHO-TN401 inspection; historical stochastic LR measurement generation.
- **UNRESOLVED:** per-field Apollo 11 MSK-1137 routing, exact GUIDO request workflow, MCC dynamic-data cadence/latency/freshness, LM-5 raw word length/bit order/sign/bias/rounding, and sub-second LR transition timing.
