# Progress — Apollo 11 LR velocity-sign boundary

Date: 2026-09-21

## Question

Can primary Apollo hardware evidence narrow the unresolved landing-radar sign-encoding problem without importing later LM raw-word details into Apollo 11?

## Primary-source result

NASA TN D-6849, *Apollo Experience Report — Lunar Module Landing Radar and Rendezvous Radar*, states that landing-radar velocity data are produced as pulse trains superimposed on a 15.3-kHz reference frequency to facilitate determination of velocity sign. Those velocity pulse trains, together with the range pulse train, are then routed to the Signal Data Converter. The converter accepts LGC strobe signals and uses them to assemble and read out range and velocity data in serial binary form to the LGC.

This is consistent with the already documented MIT/IL GSOP and AC Electronics ND-1021042 interface boundary: binary data flow to the LGC is distinct from the LGC readout/reset/quantity-selection strobes.

## Controlled conclusion

The unresolved generic `sign` question can be split more precisely. Velocity sign is a real measurement attribute determined upstream of Signal Data Converter serialization; it is not created by LUMINARY after receipt. The SDC/LGC serial path must preserve that signed measurement information.

The source does **not** state how sign is represented in the resulting serial binary word. It therefore does not establish a sign bit, polarity convention, one's/two's complement encoding, integer bias, serial bit order, LM-5 word length, or rounding/truncation. None of those are inferred.

No controller-visible consequence follows from this hardware-path evidence, and station maturity does not change.

## Repository updates

- `docs/roadmap/2026-09-19_apollo11_landing_radar_beam_transform.md`
- `docs/station-status/2026-09-20_apollo11_lr_scale_selection.md`
- `resources/APOLLO11_LR_SCALE_SELECTION_SOURCE_CATALOG_ADDENDUM.md`
- this progress record

## Next discriminating target

Continue searching for LM-5/Apollo-11-effective Signal Data Converter or LGC-LM electrical-interface documentation that specifies raw serial word length, bit order, and serial representation of velocity sign. Treat integer bias and rounding/truncation as separate unresolved properties unless the recovered source explicitly defines them.

## Evidence status

- **DOCUMENTED, APOLLO-PROGRAM HARDWARE:** velocity sign is determined in the LR measurement pulse-train path before Signal Data Converter serialization.
- **DOCUMENTED INTERFACE:** SDC serializes velocity/range data under LGC strobe control.
- **UNRESOLVED:** LM-5 raw word length, bit order, serial sign representation/bias, and rounding/truncation.
- **NO STATION MATURITY CHANGE.**
