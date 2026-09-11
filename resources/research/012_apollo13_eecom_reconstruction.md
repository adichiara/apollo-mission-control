# Research Note 012 — Apollo 13 EECOM Reconstruction

**Date:** 2026-09-11  
**Status:** REVIEWED-PARTIAL

## Objective

Determine whether the Apollo 13 EECOM position is documented well enough to serve as the first reference controller station.

## Conclusion

Yes — **for a partial research prototype**.

EECOM is currently the strongest station because official Apollo 13 documentation preserves:

- console component anatomy
- two most-frequently-used live display formats
- one-second update cadence
- limit-sense behavior
- master-caution event indication
- postmission operational commentary
- high-speed playback usage
- the accident chronology showing how EECOM interpreted ambiguous telemetry

It is **not** yet documented enough to reproduce every keyboard, light, display, and command function.

## Official console evidence

Apollo 13 Review Board figure B7-7 identifies:

- three event-indicator areas
- two voice positions
- two precision TV monitors
- DRK
- MSK
- status/status-report controls
- summary-message-enable keyboard
- analog meter

## Official display evidence

### CSM EPS HIGH DENSITY

Figure B7-8 is a dense live electrical/fuel-cell display.

Information families include:

- DC buses
- batteries
- AC buses
- spacecraft/fuel-cell/battery current
- individual fuel-cell current
- fuel-cell reactant pressure
- fuel-cell flow
- fuel-cell thermal state
- radiator temperatures
- fuel-cell load split
- instrumentation/status values

### CSM ECS-CRYO TAB

Figure B7-9 combines:

- cabin/suit environmental data
- O2 manifold/flow
- CO2
- water quantities
- primary coolant
- secondary coolant
- cryogenic tank pressure/quantity/temperature
- total fuel-cell current

Both displays update once per second.

## Limit-sense behavior

The limit system is especially important for simulation fidelity.

The Review Board states:

- EECOM manually set high/low limits.
- Tight limits were normally used.
- Multiple illuminated limit-sense lights were therefore common.
- Panel 3 contained 72 lights, including 12 cryogenic pressure/temperature/quantity limit lights.
- A spacecraft master caution indication was also repeated on the console.

This means an authentic EECOM client should not use a simplistic red/yellow/green alarm model.

## Accident-specific evidence

The Review Board determined that an O2 tank 2 pressure limit-sense light should have appeared roughly 30 seconds before tank failure, but it may not have been observed.

Immediately after the accident, telemetry looked sufficiently inconsistent that Mission Control initially suspected instrumentation failure.

That provides direct evidence for:

- uncertain telemetry
- misleading data
- attention limits
- non-obvious alarm conditions

## HSD Format 30

The EECOM Post Mission Report says Format 30 was new for Apollo 13 and extensively used for O2 tank 2 anomaly playback.

This should be kept separate from the live display named **CSM EPS HIGH DENSITY**.

## Reconstruction-source caution

The widely circulated Andy Anderson Apollo 13 EECOM-console drawing is valuable but not primary evidence for every control.

Anderson publicly stated that:

- the monitor data and communications panels were reasonably accurate,
- the Summary Message Keyboard was incomplete,
- the DRK was largely a mystery and partly reconstructed from Apollo 14 material,
- the limit-sense layout relied in part on Apollo 15 PHO-TR155 material and indistinct photographs.

This makes the drawing a useful discovery aid but not an authoritative configuration source.

## Missing source target

The most important missing document for finishing the console configuration is the **H2 / Apollo 13 revision of PHO-TR155, MCC Operational Configuration**, reportedly Revision C around March 1970.

Locating this document is now a high-priority archival research target.

## Source list

- Apollo 13 Review Board Appendix B — NTRS 19700078726
- Apollo 13 Mission Operations Report — EECOM appendix
- PHO-TR515 — Display Formats Manual
- Andy Anderson reconstruction discussion — collectSPACE, used only as source-quality caution
