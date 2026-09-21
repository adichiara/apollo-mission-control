# Apollo 11 landing-radar controller-visibility closure

Date: 2026-09-21

## Question

Does the Apollo 11 PCR-775 / landing-radar scale-selection state have a documented player-visible MCC/GUIDO consequence?

## Primary-source finding

The Apollo 11 AC Electronics mission-control manual defines MSK-1137 fields for:

- `LR RNG` — status of landing-radar range data, `GOOD/BAD`;
- `VEL` — status of landing-radar velocity data, `GOOD/BAD`;
- `VXB, VYB, VZB` — velocity data in body-axis coordinates, ft/sec;
- `RNG` — landing-radar slant-range altitude, ft.

This is direct mission-specific evidence that processed LR validity and measurement products were controller-visible on MSK-1137.

The recovered MSK-1137 definition does not list `ALTSCBIT`, high/low scale state, `RADSKAL`, `SKALSKAL`, PCR-775 compensation selection, raw LR serial words, or the onboard rescaling operation. No separate controller control/annunciator for those implementation details is supported by this source.

## Controlled interpretation

Close the generic `controller visibility` item in two parts:

1. **Positive:** LR range/velocity validity, body-axis velocity, and slant range are documented Apollo 11 controller display products.
2. **Negative boundary:** do not expose PCR-775 selection or onboard scale/rescaling state directly unless additional primary evidence is recovered.

MSK-1137 is a display definition, not proof that its LR values are raw downlist quantities. The ground-processing/provenance chain that produced `VXB/VYB/VZB` and `RNG` remains unresolved and becomes the next research target.

## Documentation synchronized

- `docs/roadmap/2026-09-20_apollo11_lr_scale_selection.md`
- `docs/station-status/2026-09-20_apollo11_lr_scale_selection.md`
- `resources/APOLLO11_LR_SCALE_SELECTION_SOURCE_CATALOG_ADDENDUM.md`
- this progress record

## Source

- AC Electronics, *Apollo 11 Manual*, MSK-1137 definition: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf

## Evidence status

- **DOCUMENTED, APOLLO-11 MISSION-SPECIFIC:** MSK-1137 exposes LR range/velocity `GOOD/BAD`, body-axis LR velocity, and LR slant range.
- **NOT DOCUMENTED AS CONTROLLER-VISIBLE IN RECOVERED DISPLAY DEFINITION:** PCR-775 selection, `RADSKAL`/`SKALSKAL`, `ALTSCBIT`, high/low scale state, raw LR serial encoding, or onboard rescaling.
- **UNRESOLVED:** source/ground-processing chain for the MSK-1137 LR measurement fields.
- **BLOCKED:** stochastic historical LR error generation remains blocked pending flight-effective residual/distribution evidence.
