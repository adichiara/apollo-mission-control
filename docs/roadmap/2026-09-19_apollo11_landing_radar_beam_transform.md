# Apollo 11 landing-radar beam-transform roadmap

Date: 2026-09-19
Parent: `docs/ROADMAP.md`

## Completed in this step

The Apollo 11 landing-radar velocity-reference gate is now closed through the attitude transformation used by `VELUPDAT`.

Primary Apollo-11-effective evidence controls both legs:

- LUMINARY 099 `SETPOS1`/`SETPOS2` select the position-specific alpha/beta pair;
- `SETPOS` constructs antenna-to-navigation-base velocity/range beam vectors;
- LUMINARY Memo #95 fixes the sign/order convention;
- the LM-5 Mission G prelaunch erasable load supplies all four position-angle values;
- LUMINARY 099 supplies the fixed `HBEAMANT` antenna-frame range-beam constant;
- `LRVJOB` schedules `RDGIMS` during the five-sample velocity read;
- `RDGIMS` time-tags and stores the IMU CDU angles and PIPA snapshot;
- `VELUPDAT` restores the saved CDU angles in Y-Z-X order, runs `QUICTRIG`, and transforms the selected navigation-base beam with `*NBSM*`;
- the LUMINARY 099 powered-flight subroutines explicitly define `*NBSM*` as NB-to-SM using those computed CDU sines/cosines.

The historical profile therefore does not need an arbitrary normalized beam or current-time attitude substitute.

## Revised next work

1. Recover the **downstream velocity estimator/update** in `VELUPDAT`: measured-velocity reconstruction, propagated estimate, reasonableness threshold, failure/inhibit handling, and update weights.
2. Resolve the Apollo-11-effective values and semantics of `LRVF`, `LRVMAX`, `LRWVZ/Y/X`, `LRWVFZ/Y/X`, and `LRWVFF`, including the P65/P66/P67 override.
3. If that chain closes, implement the historical landing-radar profile on top of the existing lower-level projection proof and add source-backed tests.
4. Keep controller-visible radar/guidance product cadence and formatting separate; onboard computation/update behavior is not automatically a Mission Control display contract.
5. Keep direct `69-FS-3` recovery preferred but dependency-triggered where the final LUMINARY 099 listing and LM-5 pad-load chain already establish behavior.

## Repository rule correction

Do not allocate this independent landing-radar thread inside the existing 400–499 P66/PCR-700 block. The invalid 405 note that caused the index/audit failure has been removed rather than silently extending another thread's numbering allocation.

## Evidence status

- **DOCUMENTED:** static antenna-position transform and LM-5 geometry inputs.
- **DOCUMENTED:** time-tagged IMU-CDU capture and NB-to-SM velocity-beam transformation used by `VELUPDAT`.
- **PARTIALLY DOCUMENTED:** velocity reasonableness/update estimator and weights.
- **UNRESOLVED:** controller-visible product timing/formatting.
