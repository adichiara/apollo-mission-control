# Progress — Apollo 11 descent dynamics input audit

Date: 2026-09-22

## Completed

Audited the generic DPS and translational model inputs against primary Apollo documentation.

Key result: the reusable model interfaces do not need new hidden physics constants. NASA TN D-7143 maps cleanly onto existing thrust, effective-Isp, direction/gimbal, and depletion semantics, but its 10,500-lbf maximum-rated thrust, 10:1 throttling ratio, ±6-degree gimbal capability, and 305-second end-of-duty-cycle Isp are design-envelope evidence rather than an LM-5 delivered-flight profile.

The Apollo 11 press kit provides LM-5 launch mass/resource bookkeeping, including 18,100 lb DPS propellant and 33,205 lb total launch weight, but this is not the powered-descent-initiation mass. The Mission Report's 756.3-second powered-descent duration is a useful checkpoint but cannot define a continuous throttle history.

A targeted follow-on recovered TRW Note 70-FMT-819 / NASA CR-108349, *Apollo Mission 11, Trajectory Reconstruction and Postflight Analysis, Volume 1*. Its descent section documents a postflight best-estimate trajectory derived first from low-speed MSFN data and landing-site constraint, then a subsequent reconstruction combining onboard and high-speed MSFN data with pre-PDI relative tracking. The report states that this combination produced a consistent continuous LM trajectory from DOI to touchdown.

This materially improves the validation path: a mission-specific continuous reference trajectory exists. It remains **RECONSTRUCTED**, because the source explicitly describes fitting, data combination, and constraint rather than a raw continuous truth record.

### Follow-on extraction result

Audited Volume I for extractable state/checkpoint and frame products. The report explicitly places the actual 45-day BET listing in **Volume II** in NASA Apollo Trajectory (NAT) format and says that Volume II was not generally distributed. Volume I therefore does not supply a machine-usable continuous state listing.

The audit did recover useful method detail: six descent trajectory solutions were compared; the Lear solution used 10-sample/s high-speed MSFN data over 232 seconds immediately before PDI; the combined onboard/MSFN high-speed HOPE solution used compacted high-speed Doppler plus CSM sextant/VHF relative tracking and telemetered acceleration in the IGS burn model. The report also defines the CSM-centered UVW-type axes used for relative-trajectory comparison figures. Those axes are not assumed to be the unrecovered NAT listing's frame.

## Boundary preserved

No launch mass was substituted for PDI mass. No design thrust or Isp was promoted to an Apollo 11 as-flown value. No postflight reconstructed state was relabeled as raw telemetry or exact physical truth. No state series was digitized from plots and presented as the Volume-II BET. No NAT frame/epoch convention was inferred from a different comparison coordinate system.

## Repository updates

- `docs/roadmap/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/progress/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `docs/station-status/2026-09-22_apollo11_descent_dynamics_input_audit.md`
- `resources/APOLLO11_DESCENT_DYNAMICS_INPUT_SOURCE_CATALOG_ADDENDUM.md`

## Next

Recover TRW 70-FMT-819 Volume II / the Apollo 11 45-day BET NAT listing or a traceable archival derivative preserving its epochs, frames, units, and provenance. Continue the narrower LM-5 PDI mass and DPS delivered-performance search.

## Evidence status

**PARTIALLY DOCUMENTED.** Reconstruction methodology and comparison semantics are now bounded. The tabulated 45-day BET state history is **BLOCKED ON NAMED SOURCE RECOVERY** (Volume II). PDI mass and delivered DPS thrust/Isp history remain unresolved.