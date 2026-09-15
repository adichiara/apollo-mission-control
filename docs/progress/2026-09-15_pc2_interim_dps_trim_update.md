# Progress — PC+2 interim DPS-trim update boundary

Date: 2026-09-15
Research note: `resources/research/152_pc2_interim_dps_trim_update_boundary.md`

## Completed

- Re-examined the primary Apollo 13 Flight Control Division Mission Operations Report around the documented ~59-hour PC+2 mass-properties disagreement.
- Cross-checked the restored mission-audio transcript for the corresponding controller-to-crew P30 sequence.
- Recovered the interim DPS gimbal trim pair communicated at GET ~59:03: pitch `5.86°` and second GDA value `6.75°`; Haise's accepted readback identifies the second axis as roll.
- Preserved CAPCOM's explicit statement that these angles **will be updated**, preventing the interim pair from being misclassified as the final PC+2 trim.
- Kept the primary-source boundary intact: the Flight Dynamics report establishes that the ~59-hour trim was challenged because LM Control had used inferior premission mass properties, but does not explicitly identify the accepted basis as `T+55` or provide a PC+2 mass-properties job number.
- Distinguished the ~59-hour interim product from the Flight Dynamics report's later final PC+2 pad at ~78 hours based on the GYM 289 vector.
- Updated the numerical-validation roadmap, station-status addendum, and RTCC mass-properties source catalog.

## Result

The simulation provenance model now needs a separate maneuver-product lifecycle/finality dimension. A historically valid product can be communicated to the crew while still marked for later update; source basis, job identity, communicated value, and finality must not be collapsed.

## Next

Search the Apollo 13 Flight Director Log and H-2 Flight Dynamics/RETRO/RTCC working records for GET 55–59 and 77–78 hours. Highest-value recovery would identify the mass-properties job/run behind the interim `5.86° / 6.75°` pair and a later replacement trim, explicitly tying one or both to `T+55`, GYM 289, or the final `62480 / 33452 lb` P30 weights.