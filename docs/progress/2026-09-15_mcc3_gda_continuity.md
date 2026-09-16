# MCC-3 nomenclature and GDA continuity

Date: 2026-09-15  
Latest research note: `resources/research/190_lm7_premission_mass_properties_source_boundary.md`

## Completed

- Reconciled the apparent `MCC-3` contradiction in the Flight Control Division report: CONTROL calls the 61:29 contingency free-return DPS burn `MCC-3 - DPS 1`, while trajectory/mission-summary material calls it MCC-4 and records the originally planned MCC-3 as omitted.
- Established from primary voice that `5.86 / 6.75` was commanded for the 61:29 burn and that CONTROL's preburn gimbal-trim checkout judged the observed state `within about 0.3` / `plenty close`. This is spacecraft-checkout acceptance, not the missing ground-computation criterion.
- Classified the later `5.85 / 6.74` PC+2 pair as a CAPCOM-issued desired/reference pair with an explicit `okay as it is from the last burn` disposition, not telemetry.
- Joined the ~59 GET `5.86 / 6.75` readback to the Flight Dynamics chronology, which says LM CONTROL challenged that trim using **premission mass properties** and later agreed with Flight Dynamics' better data.
- Established T-6 generation/load, T+25 RTCC run and `0.01°` no-update comparison, and the later update of RTCC **LM-burn** mass-property decks to T+55. Generation, loading, deck update, and downstream run consumption remain distinct states.
- Established the generic Apollo processor contract from primary RTACF material: configuration/consumables-sensitive mass properties and weight-c.g. products fed RTACF/RTCC trajectory processors computing pitch/yaw trim.
- Separated commanded trim, automatic powered-flight trim behavior, postflight actuator phase values, mechanism range, LM-7 telemetry channel semantics, feedback path, and later-LM engineering-unit presentation.
- Note 190 identifies a mission-specific preflight LM-7 mass-properties source family. A 17 March 1970 LM-7 DPS weight-characteristics table gives `4,523.0 lbm` DPS-stage inert, `18,434.8 lbm` loaded DPS propellant, `10,914.5 lbm` loaded APS stage and crew, and `33,872.3 lbm` LM weight at separation. Crucially, the source says these mass properties were used for that analysis and directs users to **Volume III, Spacecraft Operational Data Book, for current official mass-properties data**. The recovered values are therefore not promoted into CONTROL's undocumented ~59 GET inputs.
- Note 190 sharpens the premission-source target: recover the Apollo 13/LM-7 Volume III current official mass-properties set/revision and then determine which premission set CONTROL actually selected.

## Next

Priority remains an Apollo 13 T+55 weight/c.g. product or downstream RTCC/RTACF LM-burn request/run/output explicitly bridging the real-time deck to `5.86 / 6.75`. In parallel, recover the Volume III current official Apollo 13/LM-7 preflight mass-properties tables and revision trail, then seek controller material identifying CONTROL's selected premission set and alternative numerical trim. The ground-computation comparison/acceptance basis and job identity remain unresolved.

Do not reuse the `~0.3°` preburn checkout, T+25 `0.01°` result, later `0.01°` reference-pair difference, or Volume II DPS-analysis values as substitutes for missing evidence.