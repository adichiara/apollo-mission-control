# Apollo 13 PC+2 ~59 GET trim-provenance sources

Date: 2026-09-16  
Related notes: `resources/research/170_pc2_59h_trim_provenance.md` through `resources/research/193_lm7_sequential_mass_properties_table_recovery.md`

## NASA/MSC Flight Control Division Mission Operations Report — Apollo 13

Primary mission-specific controller report. Supports T-6 generation/load, T+25 RTCC mass-properties run and `0.01°` no-update result, later update of RTCC LM-burn decks to T+55, and CONTROL's ~59 GET challenge using premission mass properties. Does not print the T+55 deck, CONTROL alternative trim, comparison criterion, job identity, or direct T+55-to-`5.86 / 6.75` linkage.

## NASA/MSC CSM/LM Spacecraft Operational Data Book Volume III — LM-7 Amendment 79

- Document: SNA-8-D-027(III) Rev. 2
- Amendment: 79
- Date on recovered LM-7 pages: **30 March 1970**
- Source class: primary mission-specific preflight operational mass-properties documentation

### Supports
- Concrete late-preflight official LM-7 mass-properties source state twelve days before Apollo 13 launch.
- Directly recovered **Table 3.3-3, `LM-7 Effective Sequential Mass Properties`**, with weight, c.g., inertia/product-of-inertia, and dispersion fields.
- A legible `LM PRE P.D.I.` row: **33,980.1 lb**, X/Y/Z c.g. approximately **188.1 / -0.0 / -0.8 in**.
- Table 3.3-8: `LM-7 Consumables Change Summary`, mission-event consumable accounting across separation, pre-PDI, touchdown, ascent, rendezvous/docking, and jettison.
- Table 3.3-18: `LM-7 Propellant Loading Uncertainties`, including quantities whose uncertainty/values depend on actual loading.

### Table-number boundary
Table 3.3-8 says it is `to be used in conjunction with the LM sequential mass properties Table 3-3.2`. Directly recovered LM-7 sequential pages, however, are headed **Table 3.3-3**; Table 3.3-2 in the same document is CSM 109 effective sequential mass properties. Preserve this source-internal cross-reference mismatch. Do not assert whether it is a typo, amendment artifact, or other numbering convention without evidence.

### Provenance boundary
This establishes **official data available preflight**, not **data selected by CONTROL**. No Amendment 79/Table 3.3-3 value is assigned to CONTROL's ~59 GET calculation without controller-selection evidence, and no preflight row is substituted for T+55.

## NASA Apollo 13 Review Board — Table 3-I weight summary

- Report: *Report of Apollo 13 Review Board*, NASA-TM-X-65270, June 1970; NTRS 19700076776.
- Source class: primary postflight NASA mission/accident-review report.
- Table 3-I reports Lunar Module final separation weight **33,941 lb**, footnoted `CSM/LM separation`.

### Provenance value
This independently constrains the documented Apollo 13 LM separation mass state and differs by **68.7 lb** from the 17 March analysis-specific `33,872.3 lbm` value. It therefore confirms that the 17 March value must not be promoted as the current mission separation weight.

### Boundary
The Review Board table does not supply LM c.g., identify Amendment 79/Table 3.3-3 as its numerical source, explain the 68.7-lb difference, identify CONTROL's input, or represent the T+55 real-time mass state.

## NASA/Grumman LM-7 DPS weight characteristics — 17 March 1970

Primary mission-specific analysis source. Gives a `33,872.3 lbm` LM separation weight and component weights but explicitly directs users to Volume III for current official mass properties. Retain as an analysis-specific preflight source, not CONTROL's assumed input.

## NASA/MSC RTACF operational documentation / Apollo 11 support report

Primary contemporary sources establish the generic processor contract:

`configuration + consumables -> mass-properties / weight-c.g. product -> RTACF/RTCC trajectory processor -> pitch/yaw trim`

## NASA Apollo 13 voice / Mission Report

Voice establishes `5.86 / 6.75` as the ~59/61:29 commanded reference and the separate preburn checkout. Later `5.85 / 6.74` is a ground-issued PC+2 reference with no-action disposition. Mission Report execution/actuator products remain separate from ground trim-computation provenance.

## Current provenance chain

`1970-03-17 analysis-specific LM separation weight = 33,872.3 lbm -> not current-official authority`

`LM-7 official preflight sequential model -> SNA-8-D-027(III) Rev 2 + Amendment 79 + Table 3.3-3 (1970-03-30) -> CONTROL selection UNKNOWN`

`Table 3.3-8 cross-reference -> says LM sequential Table 3-3.2 -> inconsistent with recovered Table 3.3-3 heading; cause UNKNOWN`

`Apollo 13 Review Board mission summary -> CSM/LM separation weight = 33,941 lb -> relationship to Table 3.3-3/CONTROL/T+55 UNKNOWN`

`T-6 -> generated -> loaded in RTCC`

`T+25 -> RTCC mass-properties run -> P/Y comparison -> within 0.01° -> no update`

`T+55 -> RTCC LM-burn decks updated -> mission-specific run consumption unresolved`

`~59 Flight Dynamics PC+2 calculation -> 5.86 / 6.75 -> CONTROL challenge using premission mass properties -> reconciliation -> same pair commanded for 61:29`

## Next source target

Recover (1) Apollo 13 T+55 real-time weight/c.g. output plus explicit downstream RTCC/RTACF run/request/output, and (2) controller evidence identifying whether CONTROL selected Amendment 79/Table 3.3-3 or another premission source. Highest-value missing fields remain CONTROL's alternative values, ground-computation comparison/acceptance basis, job identity, and explicit T+55-deck-to-`5.86 / 6.75` lineage. Complete recovery of the opening/relevant Table 3.3-3 pages remains useful supporting work.