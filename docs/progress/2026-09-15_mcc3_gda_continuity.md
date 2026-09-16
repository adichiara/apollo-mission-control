# MCC-3 nomenclature and GDA continuity

Date: 2026-09-16  
Latest research note: `resources/research/192_lm7_preflight_weight_state_crosscheck.md`

## Completed

- Reconciled the `MCC-3` nomenclature split and established the `5.86 / 6.75` commanded pair, preburn checkout disposition, and later `5.85 / 6.74` no-action reference.
- Joined the ~59 GET pair to the Flight Dynamics chronology: CONTROL challenged it using **premission mass properties** and later agreed with Flight Dynamics' better data.
- Established T-6 generation/load, T+25 RTCC run and `0.01°` no-update result, and later RTCC LM-burn deck update to T+55; downstream T+55 run consumption remains unproved.
- Established the generic RTACF/RTCC processor contract from configuration/consumables through weight-c.g. products to pitch/yaw trim.
- Note 190 separated an analysis-specific LM-7 preflight weight model from the Volume III current-official authority.
- Note 191 recovered the late-preflight official source state: SNA-8-D-027(III) Rev. 2, **LM-7 Amendment 79 dated 30 March 1970**, with Table 3.3-8 explicitly coupled to `LM sequential mass properties Table 3-3.2`.
- **Note 192 independently cross-checks the LM-7 separation-weight state.** NASA's Apollo 13 Review Board Table 3-I reports **33,941 lb at CSM/LM separation**, versus **33,872.3 lbm** in the 17 March analysis-specific source, a **68.7-lb difference**. This confirms that the 17 March value is not safe to promote as the current mission separation weight.
- Kept the boundary explicit: the Review Board table does not identify the cause of the 68.7-lb difference, Table 3-3.2/Amendment 79 as its numerical source, CONTROL's selected input, or the T+55 state.

## Next

Priority remains an Apollo 13 T+55 weight/c.g. product or RTCC/RTACF request/run/output explicitly bridging the real-time deck to `5.86 / 6.75`. Parallel target: recover LM-7 Table 3-3.2 at Amendment 79/current state and then controller material identifying CONTROL's selected premission source and competing trim.

Do not reuse the preburn `~0.3°` checkout, T+25 `0.01°` result, later reference-pair difference, either recovered preflight weight, or the 68.7-lb cross-source difference as the missing ground-computation criterion without direct evidence.