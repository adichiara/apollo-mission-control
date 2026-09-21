# Apollo 11 landing-radar beam-transform roadmap

Date: 2026-09-20
Updated: 2026-09-21
Parent: `docs/ROADMAP.md`

## Controlled chain

Apollo-11-effective LUMINARY 099 controls `SETPOS`, measurement-time CDU capture, Y-Z-X preparation, `*NBSM*` direction semantics, LR quantity selection, and onboard LR scale handling. Memo #95 controls antenna→NB beta-then-alpha semantics. The LM-5 Mission G prelaunch erasable load supplies position-specific alpha/beta values and the PCR-775 compensation selection.

## Completed

The equation-level SETPOS and SM/NB transforms are composed into the landing-radar velocity estimator chain with a provenance-bearing LM-5 profile adapter. Mission-specific MSK-1137 evidence controls LR field identities, body-axis velocity frame, units/display masks, validity fields, mixed `D/L`/`RTCC` provenance, and the ground-computed identity of `ACT ΔV`; per-field routing remains unresolved.

Apollo 11 MCC architecture is source-controlled as distinct spacecraft/downlink, CCATS/RTCC processing, Display/Control, and controller-presentation layers. NASA TN D-8316 separates buffered dynamic-data updates from CRT refresh/reference-slide access; PHO-FAM001 constrains the pre-Apollo-11 request transaction; NASA TN D-7685 constrains Apollo-program display-request/channel allocation. PHO-TR515 supplies a later-system provenance model only. PHO-TN401 remains **BLOCKED** behind archival access.

The Apollo 11 Mission Report constrains powered-descent LR acquisition and two later expected zero-Doppler/manual-maneuver tracking losses. Table 5-I gives `DATA NOT GOOD`→`DATA GOOD` intervals of 102:44:11→102:44:21 and 102:44:59→102:45:03: 10 s and 4 s at one-second event resolution, not a generalized dropout law. The AC Electronics Apollo 11 manual separately requires four continuous seconds of `DATA GOOD` before measurement tests permit state-vector updating. MIT R-700 Vol. II supplies the Apollo-11 onboard reasonableness gates.

GAEC LSP-470-2D supplies 3-sigma LR range/velocity acceptance limits. NASA TN D-6849 supplies LM-5 flight experience and cautions against converting simulator behavior into a simple Gaussian law. NASA-CR-92466 remains a mission-period beam/Doppler mathematical-model source, not LM-5 flight-error statistics.

NASA TN D-6849 establishes separate LGC-digital and crew-display electrical output paths and states that velocity sign is determined in the measurement pulse-train path before Signal Data Converter serialization. The MIT/IL GSOP exposes `LR in "1"` / `LR in "0"` binary inputs separately from status discretes. AC Electronics ND-1021042 supplies LGC readout/reset/quantity-selection behavior and states that radar control terminates sync and requests `RUPT9` after **15 received radar pulses**.

A mission-specific Apollo 11 engineering note explaining the LGC 520 alarm on DSKY circuit-breaker closure supplies the effectivity bridge for raw transfer length: an 80-ms gate, a 5-ms delay, **15 readout pulses at 3200 pps**, then radar interrupt. MIT/MSC R-700 Volume II now closes the remaining serial-order question: radar shift-register contents cross the interface **most-significant-bit first**, with `1` and `0` bits transferred on separate ones/zeros buses. An MIT/IL functional description independently states that the 15-bit LR range/velocity word is shifted out MSB first on two lines. Serial sign representation/integer bias and Signal Data Converter rounding/truncation remain unresolved.

Flown LUMINARY 099 `P20-P25.agc` closes software-side LR quantity selection: `LRVELX/LRVELY/LRVELZ/LRALT` invoke `INITREAD` with octal `14/15/16/17`. These command values are not returned-data encoding.

**Apollo-11-effective scaling boundary:** flown LUMINARY 099 gives low-scale altitude 1.079 ft/count and X/Y/Z converted/stored velocity bit weights of -0.6440/+1.212/+0.8668 ft/s. Revision-99 Memo #85 gives high/low ratio 5, directly deriving 5.395 ft/count high scale. Memo #85 also resolves the zero `RADSKAL`/`SKALSKAL` mission load as radar-performed slant-range Doppler compensation rather than a zero scale ratio.

Later LM10/R-567 material remains adjacent architecture corroboration. Its 15-bit result is now independently bridged to Apollo 11 by the mission-specific 520-alarm note and ND-1021042.

## Next work

1. Seek LM-5/Apollo-11-effective hardware-interface evidence for **serial sign representation/integer bias**. Raw word length (15 bits/pulses) and serial order (MSB first) are closed. Keep rounding/truncation as a separate Signal Data Converter conversion question.
2. Pursue Apollo-11-effective FDS/RTCC/CCATS material mapping individual MSK-1137 fields to `D/L`/`RTCC` provenance and external names/downlists or computation identifiers.
3. Preserve the two historical not-good intervals as deterministic replay anchors and enforce the four-second `DATA GOOD` qualification separately; do not infer a random dropout process.
4. Retrieve MSC-69-EG-14 / NASA-TM-X-64374, requiring an explicit Mission-G/LM-5 applicability bridge before using F-mission numbers.
5. Use NASA-CR-92466 only for model equations/beam physics absent separate LM-5 stochastic-error applicability evidence.
6. Keep Apollo 11 GUIDO exact DRK/MSK button mapping and powered-descent selection unresolved pending mission-effective station evidence.
7. Keep PHO-TN401 direct inspection **BLOCKED** pending archival retrieval/authenticated scan.
8. Keep sample/receive/process/display timestamps distinct; do not infer MCC tabular cadence from onboard LR timing.
9. Keep historical stochastic LR measurement generation **BLOCKED** until flight-effective numerical residual evidence is recovered.

## Evidence status

- **DOCUMENTED / IMPLEMENTED / COMPOSED:** LM-5 geometry + SETPOS + measurement-time NB→SM transform through estimator.
- **DOCUMENTED:** Apollo 11 MSK-1137 semantics and mixed `D/L`/`RTCC` provenance boundary.
- **DOCUMENTED, APOLLO 11 FLIGHT:** LR acquisition and two one-second-resolution not-good intervals with expected zero-Doppler/manual-maneuver cause.
- **DOCUMENTED, APOLLO-11-EFFECTIVE ONBOARD LOGIC:** four seconds continuous `DATA GOOD` qualification and Apollo-11-specific reasonableness gates.
- **DOCUMENTED, APOLLO-11-EFFECTIVE ONBOARD SCALING:** low/high altitude 1.079/derived 5.395 ft/count; X/Y/Z converted/stored velocity weights -0.6440/+1.212/+0.8668 ft/s.
- **DOCUMENTED, APOLLO-11-EFFECTIVE QUANTITY SELECTION:** `LRVELX/LRVELY/LRVELZ/LRALT` = octal `14/15/16/17`.
- **DOCUMENTED, APOLLO-11-SPECIFIC RAW TRANSFER LENGTH:** 15 readout pulses at 3200 pps followed by radar interrupt; independently consistent with ND-1021042's 15-pulse radar-control sequence.
- **DOCUMENTED, PRIMARY APOLLO INTERFACE:** serial binary LR data is transferred MSB first over complementary ones/zeros lines; status/selection/timing are separate paths; velocity sign is determined before serialization.
- **DOCUMENTED, MISSION-PERIOD MODEL SOURCE:** NASA-CR-92466 for beam-bandwidth/Doppler model verification, not LM-5 flight-error statistics.
- **DOCUMENTED:** Apollo MCC architectural separation and D/TV buffered-update behavior.
- **BLOCKED:** direct PHO-TN401 inspection; historical stochastic LR measurement generation.
- **UNRESOLVED:** per-field MSK-1137 routing, exact GUIDO request workflow, MCC cadence/latency/freshness, LR serial sign representation/integer bias/rounding, and sub-second LR transition timing.
