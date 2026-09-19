# Apollo 11 R-567 LUMINARY 1A coordination status

Date: 2026-09-19

This coordination note keeps the D-024 portfolio, roadmap, progress, station research, and source catalog aligned through research note 333 and its primary PCR-700A crosswalk update.

## Portfolio status

The Apollo 11 powered-descent exception remains **OPEN**, but exact P66 ROD computation cadence and the PCR-700/PCR-700A crosswalk are no longer unresolved gates. LUMINARY Memo #67 records PCR-700/PCR-670 implementation in Revision 72; Memo #73 records P66 total-lag compensation in Revision 80; the Mission G LUMINARY 99 erasable-load document carries `LAG/TAU = 0.413333`; and the LUMINARY 099 assembly listing directly schedules the P66 `RODTASK` at `1SEC`.

The assembly path is explicit: `P66VERTA` loads `1SEC`, calls `TWIDDLE`, and schedules `RODTASK`; `RODTASK` dispatches `RODCOMP`; `RODCOMP` updates `VDGVERT` and `HDOTDISP` and consumes `LAG/TAU`. This confirms the January change-intent's one-second **ROD computation** behavior in the Apollo 11 program.

MIT/IL Apollo Project Memo 9-69 supplies the missing primary identifier crosswalk: PCR-700A, “Improve the Rate-of-Descent Mode (P66) Performance,” is explicitly described as a clarifying rewrite of PCR-700. The action was already assigned. This reconciles Section 2 Revision 4's PCR-700 with the recovered Section 5 Revision 5 index's PCR-700A without treating them as unrelated changes.

The remaining bounded archival items are the Section 5 Revision 5 descriptive-equation/page ancestry/effectivity and `69-FS-3`. These are not prerequisites for the computation interval or the PCR-number crosswalk. Crew-visible Noun 63 timing and station-visible timing are separate dependency-triggered questions.

## Controlled boundary

Do not infer a one-second DSKY refresh, telemetry cadence, MCC display refresh, or controller-facing product from the internal one-second `RODTASK` schedule. `HDOTDISP` is updated in `RODCOMP`, but display/downlink/ground-processing timing requires separate evidence. Likewise, the 700→700A crosswalk does not establish that every Section 5 Revision 5 equation page is Apollo 11-effective.

No station maturity or controller-facing product changes from this update.

## Synchronized records

- research: `resources/research/329_apollo11_p66_pcr700_final_implementation.md`
- research: `resources/research/330_apollo11_r567_section5_rev4_control_index.md`
- research: `resources/research/331_apollo11_r567_section5_rev4_change_scope.md`
- research: `resources/research/332_apollo11_p66_later_equation_boundary.md`
- research: `resources/research/333_apollo11_p66_flight_listing_cadence.md`
- roadmap: `docs/roadmap/2026-09-19_apollo11_p66_pcr700_implementation.md`
- progress: `docs/progress/2026-09-19_apollo11_p66_pcr700_implementation.md`
- station status: `docs/station-status/2026-09-19_apollo11_p66_pcr700_implementation.md`
- source catalog: `resources/APOLLO11_R567_LUMINARY1A_SOURCE_CATALOG_ADDENDUM.md`