# Research Note 192 — LM-7 preflight weight-state cross-check

Date: 2026-09-16

## Question

Can an independent primary Apollo 13 source constrain the late-preflight LM-7 mass state while Table 3-3.2 itself remains unrecovered, and does it clarify whether the 17 March analysis weight in Note 190 can be treated as the current operational value?

## Primary sources

1. NASA, *Report of Apollo 13 Review Board*, NASA-TM-X-65270, June 1970, NTRS 19700076776. Chapter 3, Table 3-I, `Apollo 13 Weight Summary`.
2. NASA/MSC, *CSM/LM Spacecraft Operational Data Book, Volume III — Mass Properties*, SNA-8-D-027(III) Rev. 2, LM-7 Amendment 79 pages dated 30 March 1970 (Note 191).
3. NASA/Grumman LM-7 DPS weight-characteristics analysis dated 17 March 1970 (Note 190).

## Findings

The Review Board's Apollo 13 weight summary gives the Lunar Module a final CSM/LM-separation weight of **33,941 lb**. The table identifies the value specifically with the footnote `CSM/LM separation`.

The 17 March Grumman/NASA DPS analysis recovered in Note 190 instead used an LM separation weight of **33,872.3 lbm**. The difference is **68.7 lb**.

This is direct evidence that the mission's documented LM separation-weight state was not numerically frozen at the 17 March analysis value. It reinforces that source's own instruction to use Volume III for current official mass properties and supports Note 191's separation between an analysis-specific model and the late-preflight operational-data-book authority.

The Review Board table does not print LM c.g. coordinates, does not identify Table 3-3.2 or Amendment 79 as its numerical source, and does not identify what CONTROL used at ~59 GET. Its 33,941-lb value therefore cannot be substituted for the still-missing Table 3-3.2 state or CONTROL input.

## Interpretation

This closes one ambiguity around Note 190: **33,872.3 lbm must not be promoted as the Apollo 13 current-official separation weight.** A separate primary Apollo 13 program-level summary reports 33,941 lb at CSM/LM separation, a 68.7-lb difference.

The discrepancy is useful provenance evidence, not a basis for reverse-engineering the missing trim. No claim is made that 68.7 lb explains CONTROL's disagreement, that either weight was used by CONTROL, or that the Review Board value is the T+55 real-time mass state.

## Modeling consequence

Keep at least these source states distinct:

- `1970-03-17 analysis_specific`: separation weight `33,872.3 lbm`;
- `1970-03-30 official_available_preflight`: Volume III Rev. 2 / Amendment 79, Table 3-3.2 values not yet directly recovered;
- `Apollo 13 Review Board mission_summary`: CSM/LM-separation weight `33,941 lb`;
- `controller_selected_source`: unknown;
- `realtime_T+55`: unknown.

Do not interpolate between these values or assign the 68.7-lb delta to consumables, loading, configuration, amendment effects, or bookkeeping without source evidence.

## Next target

Priority 1 remains the mission-specific `T+55 deck -> weight/c.g. -> RTCC/RTACF run -> 5.86 / 6.75` consumption edge. Parallel priority remains direct recovery of LM-7 Volume III Table 3-3.2 at the Amendment 79/current state, especially its separation/docked weight and c.g. fields, followed by controller working material identifying CONTROL's selected premission set.