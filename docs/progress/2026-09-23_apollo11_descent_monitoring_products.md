# Progress — Apollo 11 descent monitoring products

Date: 2026-09-23

Continued the open Apollo 11 powered-descent controller-product reference.

## Primary-source result — comparison products

NASA/MSC **70-FM-20, _The Apollo 11 Adventure_** preserves Apollo 11 descent strip-chart comparisons labeled `AGS−PGNCS` and `MSFN−PGNCS`, with descent-event markers and in-plane/crossrange monitoring logic. This supports the repository's pairwise/consensus architecture without establishing exact live CRT presentation.

## Primary-source result — program-alarm/descent fields

A further pass through the mission-specific AC Electronics _Apollo 11 Manual_ recovered a stronger controller-product boundary from `ASPO 45 CRT DISPLAYS`, `MSK-1137 (CONTINUED)`. In addition to the previously cataloged landing-radar and guidance fields, MSK-1137 explicitly defines ground-visible:

- `TIG` and `TGO`;
- time of last/next significant event;
- **time to end of phase (descent only)**;
- LGC and ISS warning-lamp status;
- PGNCS and program caution-lamp status;
- first, second, and most recent alarm code;
- **number of restarts**;
- computer program number;
- DSKY verb, noun, flasher status, and rows 1–3.

This is directly useful to the Apollo 11 powered-descent/program-alarm pressure test: the simulator can expose historically sourced ground products for alarm/restart/program/DSKY context rather than inventing a modern alarm panel or leaking hidden AGC state.

## Boundary preserved

MSK-1137 field semantics do **not** establish which station requested the display at a given moment, the exact DRK legend/button mapping, update cadence/latency, or controller decision rules. Those remain configuration/routing questions. Likewise, 70-FM-20 Figure 9 is not treated as an exact live MOCR display.

## Archival target

PHO-TN401 remains the leading direct display/control recovery target. The known holding is Johnson Space Center History Collection, University of Houston-Clear Lake, Apollo Program, Mission Documents: Apollo 11, **Box 078-65/66**. The Library of Congress/NPS HAER TX-109-C bibliography and footnote 37 cross-check that locator and cite PHO-TN401 p. 5-5.

## Next discriminating target

Recover PHO-TN401 or another Apollo-11-effective configuration source to map the now-documented MSK-1137 and comparison-product semantics to exact station requests/routing/DRK mapping and cadence. Do not infer those details from the field inventory.

## Sources

- AC Electronics, _Apollo 11 Manual_, `ASPO 45 CRT DISPLAYS`, `MSK-1137`: https://www.ibiblio.org/apollo/Documents/AcElectronicsApollo11.pdf
- NASA/MSC MPAD, _The Apollo 11 Adventure_, MSC Internal Note 70-FM-20, MSC-01562, 5 February 1970: https://www.ibiblio.org/apollo/NARA-SW/TheApollo11Adventure.pdf
- LOC/NPS, HAER No. TX-109-C, _Johnson Space Center, Apollo Mission Control_: https://tile.loc.gov/storage-services/master/pnp/habshaer/tx/tx1100/tx1134/data/tx1134data.pdf

## Evidence status

- **DOCUMENTED / SUFFICIENT:** MSK-1137 alarm/restart/program/DSKY/descent field semantics for current controller-product architecture.
- **DOCUMENTED:** Apollo 11 AGS−PGNCS and MSFN−PGNCS comparison-product family.
- **UNRESOLVED:** exact live station request/routing/DRK mapping/cadence and call ownership.
- **BLOCKED ON DOCUMENT RECOVERY:** PHO-TN401 direct inspection.