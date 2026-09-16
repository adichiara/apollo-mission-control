# Progress — GDA position-feedback signal path

Date: 2026-09-16

## Completed

- Added research note 186 using primary LM documentation.
- Cross-checked LM-7/8/9 measurement identities against the Apollo Operations Handbook DECA trim-control diagram.
- Established that `GH1313V` and `GH1314V` belong to the physical GDA actuator-position feedback path, while the LGC extend/retract trim commands are separate measurements/signals.
- Preserved the evidence boundary: no voltage-to-inch calibration, EXT/RET sign mapping, LM-7 exact degrees-per-inch conversion, or mapping to the crew-facing `5.86 / 6.75` pair was inferred.
- Updated the dedicated PC+2 GDA roadmap and source catalog/status documentation to keep the command-versus-observation distinction explicit.

## Remaining priority

The principal unresolved item remains the T+55 LM-burn mass-properties deck -> RTCC/RTACF run -> `5.86 / 6.75` lineage. The parallel GDA target is now an LM-7 calibration/PCM definition for `GH1313V`/`GH1314V`.