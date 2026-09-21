# Progress — Apollo 11 LR quantity-select mapping

Date: 2026-09-21

## Question

Can the Apollo-11-effective software identify which radar-read command selects LR Vx, Vy, Vz, and range/altitude without importing the later LM-6 fixed-extension table?

## Primary evidence

The flown LUMINARY 099 `P20-P25.agc` radar lead-ins provide the mapping directly:

- `LRVELX` calls `INITREAD` with octal `14`.
- `LRVELY` calls `INITREAD` with octal `15`.
- `LRVELZ` calls `INITREAD` with octal `16`.
- `LRALT` calls `INITREAD -1` with octal `17`; the source annotates this path `ONE SAMPLE PER READING`.

The separate `RADAR_LEADIN_ROUTINES.agc` dispatch table maps its LR indices to `LRVELX`, `LRVELY`, `LRVELZ`, and `LRALT`, confirming these are the flown program's four LR read lead-ins.

This mission-effective software evidence is consistent with, but does not depend on, the later LM10 handbook's radar fixed-extension mapping.

## Controlled conclusion

Apollo 11's flown software closes the **quantity-selection command** boundary: Vx/Vy/Vz/range correspond to octal `14/15/16/17` at `INITREAD`. This is useful interface behavior and should be preserved if the simulator models the LGC/LR transaction.

It does not close the raw returned-data encoding. No claim is made here about LM-5 serial word length, first/last bit, sign representation, integer bias, or radar-side rounding/truncation.

## Repository updates

- `docs/roadmap/2026-09-19_apollo11_landing_radar_beam_transform.md`
- `docs/station-status/2026-09-20_apollo11_lr_scale_selection.md`
- `resources/APOLLO11_LR_SCALE_SELECTION_SOURCE_CATALOG_ADDENDUM.md`

## Next target

Continue primary-source search for LM-5/Apollo-11-effective raw LR serial word length, bit order, sign/bias, and rounding/truncation. Keep later LM-6/R-567 encoding details adjacent-effectivity only until an applicability bridge is recovered.

## Sources

- https://github.com/chrislgarry/Apollo-11/blob/master/Luminary099/P20-P25.agc
- https://github.com/chrislgarry/Apollo-11/blob/master/Luminary099/RADAR_LEADIN_ROUTINES.agc

## Evidence status

- **DOCUMENTED, APOLLO-11-EFFECTIVE:** LR quantity-select command mapping at the flown LUMINARY 099 software boundary.
- **UNRESOLVED:** raw LM-5 serial word length, bit order, sign/bias, and rounding/truncation.
