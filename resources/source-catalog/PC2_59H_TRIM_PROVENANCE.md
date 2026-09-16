# Apollo 13 PC+2 ~59 GET trim-provenance sources

Date: 2026-09-16  
Related notes: `resources/research/170_pc2_59h_trim_provenance.md` through `resources/research/190_lm7_premission_mass_properties_source_boundary.md`

## NASA/MSC Flight Control Division Mission Operations Report — Apollo 13

- Date: 28 April 1970
- Source class: primary mission-specific controller report

### Supports
- T-6 mass properties generated and loaded in RTCC.
- T+25 RTCC mass properties run; P/Y trims within `0.01°` of T-6, so no update.
- RTCC LM-burn mass-property decks later updated to T+55 decks.
- ~59 GET PC+2 pad and LM CONTROL challenge using premission mass properties; CONTROL later agreed with Flight Dynamics' data.

### Boundary
The report does not print T+55 deck contents, CONTROL's alternative trim, comparison delta, PC+2 computational acceptance criterion, job identity, or direct T+55-to-`5.86 / 6.75` linkage.

## NASA/Grumman LM-7 DPS weight characteristics — 17 March 1970

- Document family: SNA-8-D-027(II) Rev. 2, Amendment 55
- Table: LM7/4.7.1-1, LM-7 Descent Propulsion System Weight Characteristics
- Source class: primary mission-specific preflight engineering data

### Supports
- Identifiable Apollo 13/LM-7 preflight mass-properties source family.
- DPS stage inert `4,523.0 lbm`.
- Loaded DPS propellant `18,434.8 lbm` (`11,351.1` oxidizer; `7,083.7` fuel).
- Loaded APS stage and crew `10,914.5 lbm`.
- LM weight at separation `33,872.3 lbm`.
- Source explicitly states these mass properties were used for that analysis and directs users to **Volume III, Spacecraft Operational Data Book, for current official mass-properties data**.

### Provenance significance
This proves that mission-specific preflight LM-7 mass-property datasets had explicit scope/currentness distinctions. It does **not** identify CONTROL's actual premission input set. Do not substitute these Volume II DPS-analysis values for CONTROL's ~59 GET computation.

### Next archival target
Recover the applicable Apollo 13/LM-7 Volume III *Spacecraft Operational Data Book — Mass Properties* tables and revision/amendment trail, then seek controller evidence identifying which set CONTROL selected.

## NASA/Grumman Spacecraft Operational Data Book Volume II Part 2 — Revision 5

- Date: 9 March 1970
- Scope: LM-6 and subsequent Launch Mission Rule Redlines; includes LM-7-specific amendments
- Source class: primary preflight operational engineering documentation

### Supports
Confirms an active mission-specific LM-7 operational-data-book revision stream immediately before Apollo 13 launch.

## NASA/MSC Operational Support Plan for the RTACF — Apollo 10 Flight Annex

- Source class: primary contemporary RTACF operations documentation; adjacent mission

### Supports
RTACF Systems programs updated CSM/LM mass properties for consumables and vehicle reconfiguration and computed mass properties for specified configurations.

## MSC Internal Note 70-FM-20 — The Apollo 11 Adventure

- Date: 5 February 1970
- Source class: primary contemporary adjacent-mission mission-support report

### Supports
Mass-properties computations produced weight-c.g. tables used by RTACF and RTCC trajectory processors to compute pitch/yaw trim.

### Generic processor contract
`configuration + consumables -> mass-properties / weight-c.g. product -> RTACF/RTCC trajectory processor -> pitch/yaw trim`

## NASA Apollo 13 air-to-ground / technical voice

At ~59 GET CAPCOM passes pitch `5.86°`, roll `6.75°` with the PC+2 DPS abort pad and says the angles `will be updated`. At 60:53–60:56 GET the 61:29 free-return P30 pad uses the same pair and the crew readback is accepted.

## Apollo 13 Flight Director loop — pre-61:29 checkout

CONTROL directs the gimbal-trim checkout, reports `Trim looks okay`, then `within about 0.3` and `plenty close` when FLIGHT asks how close. This is mission-specific spacecraft checkout acceptance, not the missing ground-computation comparison criterion.

## NASA/MSC Apollo 13 Mission Report

Postflight second-midcourse-correction mass properties: ignition `95,959.9 lb`, c.g. `378.8 / 4.9 / 0.7 in`; cutoff `95,647.1 lb`, c.g. `379.4 / 5.0 / 0.7 in`. These validate the executed configuration postflight but are not the real-time T+55 deck.

Table 6.4-I supplies actual 61:29 GDA actuator phase values in inches. Section 6.6 establishes the executed firing duration/throttle profile. Keep these execution products separate from the ground trim-computation provenance.

## Current provenance chain

`configuration + consumables -> [generic Apollo RTACF mass-properties processor contract] -> mass-properties / weight-c.g. product -> RTACF/RTCC trajectory processor -> pitch/yaw trim`

`premission LM-7 source family -> [Volume II analysis-specific values exist; Volume III identified as current-official authority] -> CONTROL selected premission set UNKNOWN -> competing trim UNKNOWN`

`T-6 -> generated -> loaded in RTCC`

`T+25 -> RTCC mass-properties run -> P/Y comparison -> within 0.01° -> no update`

`T+55 -> RTCC LM-burn decks updated -> mission-specific generation/load/run consumption unresolved`

`~59 Flight Dynamics PC+2 calculation -> 5.86 / 6.75 -> CONTROL challenge using premission mass properties -> reconciliation -> same pair commanded for 61:29 -> preburn checkout within ~0.3 judged plenty close -> nominal powered flight -> later PC+2 as-is reference 5.85 / 6.74`

## Next source target

Recover (1) Apollo 13 T+55 real-time weight/c.g. output and an explicit downstream RTCC/RTACF LM-burn run/request/output, and (2) the applicable Volume III current-official LM-7/Apollo 13 preflight mass-properties set plus evidence identifying CONTROL's selected source. Highest-value missing fields remain CONTROL's alternative values, ground-computation comparison/acceptance basis, job identity, and explicit T+55-deck-to-`5.86 / 6.75` lineage.