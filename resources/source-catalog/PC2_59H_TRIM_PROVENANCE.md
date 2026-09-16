# Apollo 13 PC+2 ~59 GET trim-provenance sources

Date: 2026-09-16  
Related notes: `resources/research/170_pc2_59h_trim_provenance.md` through `resources/research/192_lm7_preflight_weight_state_crosscheck.md`

## NASA/MSC Flight Control Division Mission Operations Report — Apollo 13

Primary mission-specific controller report. Supports T-6 generation/load, T+25 RTCC mass-properties run and `0.01°` no-update result, later update of RTCC LM-burn decks to T+55, and CONTROL's ~59 GET challenge using premission mass properties. Does not print the T+55 deck, CONTROL alternative trim, comparison criterion, job identity, or direct T+55-to-`5.86 / 6.75` linkage.

## NASA/MSC CSM/LM Spacecraft Operational Data Book Volume III — LM-7 Amendment 79

- Document: SNA-8-D-027(III) Rev. 2
- Amendment: 79
- Date on recovered LM-7 pages: **30 March 1970**
- Source class: primary mission-specific preflight operational mass-properties documentation

### Supports
- Concrete late-preflight official LM-7 mass-properties source state twelve days before Apollo 13 launch.
- Table 3.3-8: `LM-7 Consumables Change Summary`, explicitly `to be used in conjunction with the LM sequential mass properties Table 3-3.2`.
- Mission-event consumable accounting across separation, pre-PDI, touchdown, ascent, rendezvous/docking, and jettison.
- Table 3.3-18: `LM-7 Propellant Loading Uncertainties`, including quantities whose uncertainty/values depend on actual loading.

### Boundary
This establishes **official data available preflight**, not **data selected by CONTROL**. Table 3-3.2 itself and its current LM-7 values still need direct recovery/verification. No Amendment 79 value is assigned to CONTROL's ~59 GET calculation without controller-selection evidence.

## NASA Apollo 13 Review Board — Table 3-I weight summary

- Report: *Report of Apollo 13 Review Board*, NASA-TM-X-65270, June 1970; NTRS 19700076776.
- Source class: primary postflight NASA mission/accident-review report.
- Table 3-I reports Lunar Module final separation weight **33,941 lb**, footnoted `CSM/LM separation`.

### Provenance value
This independently constrains the documented Apollo 13 LM separation mass state and differs by **68.7 lb** from the 17 March analysis-specific `33,872.3 lbm` value. It therefore confirms that the 17 March value must not be promoted as the current mission separation weight.

### Boundary
The Review Board table does not supply LM c.g., identify Amendment 79/Table 3-3.2 as its numerical source, explain the 68.7-lb difference, identify CONTROL's input, or represent the T+55 real-time mass state.

## NASA/Grumman LM-7 DPS weight characteristics — 17 March 1970

Primary mission-specific analysis source. Gives a `33,872.3 lbm` LM separation weight and component weights but explicitly directs users to Volume III for current official mass properties. Retain as an analysis-specific preflight source, not CONTROL's assumed input. Its separation weight is 68.7 lb below the later Apollo 13 Review Board mission-summary value; cause not established.

## NASA/MSC RTACF operational documentation / Apollo 11 support report

Primary contemporary sources establish the generic processor contract:

`configuration + consumables -> mass-properties / weight-c.g. product -> RTACF/RTCC trajectory processor -> pitch/yaw trim`

## NASA Apollo 13 voice / Mission Report

Voice establishes `5.86 / 6.75` as the ~59/61:29 commanded reference and the separate preburn checkout. Later `5.85 / 6.74` is a ground-issued PC+2 reference with no-action disposition. Mission Report execution/actuator products remain separate from ground trim-computation provenance.

## Current provenance chain

`1970-03-17 analysis-specific LM separation weight = 33,872.3 lbm -> not current-official authority`

`LM-7 official preflight source -> SNA-8-D-027(III) Rev 2 + Amendment 79 (1970-03-30) -> sequential Table 3-3.2 referenced -> values/CONTROL selection UNKNOWN`

`Apollo 13 Review Board mission summary -> CSM/LM separation weight = 33,941 lb -> relationship to Table 3-3.2/CONTROL/T+55 UNKNOWN`

`T-6 -> generated -> loaded in RTCC`

`T+25 -> RTCC mass-properties run -> P/Y comparison -> within 0.01° -> no update`

`T+55 -> RTCC LM-burn decks updated -> mission-specific run consumption unresolved`

`~59 Flight Dynamics PC+2 calculation -> 5.86 / 6.75 -> CONTROL challenge using premission mass properties -> reconciliation -> same pair commanded for 61:29`

## Next source target

Recover (1) Apollo 13 T+55 real-time weight/c.g. output plus explicit downstream RTCC/RTACF run/request/output, and (2) LM-7 Volume III Table 3-3.2 at Amendment 79/current state plus controller evidence identifying CONTROL's selected premission source. Highest-value missing fields remain CONTROL's alternative values, ground-computation comparison/acceptance basis, job identity, and explicit T+55-deck-to-`5.86 / 6.75` lineage.