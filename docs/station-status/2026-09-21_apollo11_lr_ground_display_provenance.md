# Station research status — Apollo 11 LR ground-display provenance

Date: 2026-09-21
Parent: `docs/station-status/2026-09-20_apollo11_lr_scale_selection.md`

## GUIDO / guidance-monitoring status

The controller-visible boundary remains unchanged: Apollo 11 MSK-1137 documents LR range/velocity validity, body-axis velocities `VXB/VYB/VZB`, and LR slant range. Flown LUMINARY 099 documents `DNLRVELX/Y/Z` and `DNLRALT` in the LM downlink. The exact real-time ground mapping between those two documented ends remains unresolved.

Mission-G RTCC Operations Support Plan 69-FS-2 names `PHO-TR155` and `Data Formats` as operational references. Contemporaneous PHO-TR460 records a final Mission-G third-floor display configuration, reports Mission-G configuration test status at 100 percent at launch, and records removal of that configuration after Apollo 11. Later PHO-TR515 explains that display data packs and computer listings fed PHO-TR155 configuration documentation.

An archive-focused follow-up using `MSK-1137`, Mission-G PHO-TR155, `VXB/VYB/VZB/RNG`, landing-radar, and Data Formats terms did not recover the parameter-level Mission-G package. It re-recovered the Mission-G RTCC plan and Apollo 11 AC Electronics display documentation, but not a PHO-TR155 MSK-1137 parameter table, display data pack/listing, or Mission-G Data Formats LR table.

Accordingly, this **parameter-level provenance subquestion is BLOCKED on named source recovery**. Reopen it when Mission-G PHO-TR155 material covering MSK-1137, its associated display data pack/computer listing, or Mission-G Data Formats LR material becomes accessible. Do not substitute Apollo-15 configuration evidence.

## Player-facing boundary

Keep the current neutral telemetry/engineering-processing adapter. It may deliver the documented LR validity, body-axis velocity, and slant-range products to the GUIDO/guidance-monitoring display, but its historical ownership remains unspecified. Do not label the conversion as CCATS or RTCC and do not invent parameter mnemonics, conversion coefficients, latency, or refresh cadence.

This block does not close the broader Apollo 11 powered-descent/program-alarm research thread; work may continue on other decision-relevant dependencies.

## Evidence status

- **DOCUMENTED:** Apollo-11-effective LGC LR downlink quantities and Apollo-11 MSK-1137 LR display products.
- **DOCUMENTED, MISSION-G:** PHO-TR155 and Data Formats were operational reference classes for RTCC mission support.
- **DOCUMENTED, CONTEMPORANEOUS:** a tested final Mission-G display configuration existed.
- **BLOCKED ON SOURCE RECOVERY:** per-field MSK-1137 source identifier, engineering conversion, and CCATS-selected-telemetry versus RTCC display/control path.
- **IMPLEMENTATION HOLD:** no historical ownership should be encoded until parameter-level Mission-G evidence is recovered.
