# Research note 166 — MCC-3 nomenclature and GDA-state continuity

Date: 2026-09-15

## Question

Can primary mission records reconcile the CONTROL report's statement that the GDA settings "at the end of MCC-3" were expected to be optimum for PC+2, and sharpen what state was actually carried forward?

## Primary-source findings

Yes. The same Flight Control Division *Mission Operations Report — Apollo 13* (MSC-02680, 28 April 1970) uses two numbering conventions in different sections.

The trajectory/summary material identifies the originally planned pre-accident `MCC-3` as not required and identifies the contingency free-return DPS maneuver at GET 61:29:42.84 as `MCC-4`. However, the LM CONTROL narrative explicitly calls the contingency 61:29 maneuver **`MCC-3 - DPS 1`**, then labels the following period **`POST MCC-3 TLC (62:00 - 78:00 GET)`**. It records the burn as 5 seconds at low throttle followed by 27 seconds at 40 percent.

The primary PAO/air-to-ground transcript at about GET 61:10 adds a direct operational statement immediately before that free-return burn: after discussion of the DAP/ullage load, CAPCOM says, **"The GDA's are go as they are."**

Primary sources:
- NASA/MSC Flight Control Division, *Mission Operations Report — Apollo 13*, MSC-02680, 28 April 1970, summary/trajectory and LM CONTROL sections. NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- NASA Apollo 13 PAO/air-to-ground transcript, GET ~61:10. Searchable transcript copy: https://www.scribd.com/document/1006906908/AS13-PAO ; repository source catalog retains NASA transcript location.

## Reconciliation

The `MCC-3` in CONTROL's later statement about the GDA settings "at the end of MCC-3 with its 40 percent thrust compliance" refers to the **61:29 contingency free-return DPS burn**, not to the originally scheduled pre-accident MCC-3 that was omitted.

This is an internal nomenclature difference within the postflight report, not evidence for an additional maneuver. Other mission-level records commonly call the 61:29 maneuver MCC-4 / DPS-1; CONTROL's own section renumbered it MCC-3 in the contingency sequence.

## Consequence for the GDA chain

The operational continuity is now better constrained:

`pre-free-return GDA state accepted by ground -> CAPCOM: GDA's "go as they are" -> 61:29 free-return DPS burn -> 40% powered-flight compliance establishes post-burn GDA state -> that state retained through coast -> CONTROL expects it to be optimum for PC+2 -> no PC+2 N48 update -> PC+2 ignition response`.

This supports the interpretation of note 165 without silently translating an ambiguous maneuver label. It also shows that the retained PC+2 state was specifically the **post-powered-flight complied state from the 61:29 burn**, rather than merely an arbitrary earlier commanded pair.

## Evidence boundary

This does not recover the numerical post-61:29 GDA angles, the PC+2 candidate trim calculation, comparison tolerance, RTCC job identity, or a direct calculation-level T+55 deck link. Do not equate the pre-free-return transmitted `5.86° / 6.75°` pair with the post-compliance state unless a primary source explicitly supplies that equality.

## Next unresolved item

Continue upstream archival work for the PC+2 calculation/comparison itself: candidate trim, post-61:29 reference GDA state, delta/tolerance, calculation time/job identity, and direct T+55 mass-properties linkage.