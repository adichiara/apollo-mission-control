# Roadmap continuation — Apollo 11 descent dynamics input audit

Date: 2026-09-22
Parent: `docs/roadmap/2026-09-22_apollo11_descent_continuous_trajectory_boundary.md`

## Bounded question

Which inputs already accepted by the generic DPS/translational proofs can be tied to primary Apollo sources without pretending that design values are Apollo 11 delivered-flight values?

## Primary-source findings

NASA TN D-7143 establishes the DPS design envelope: pressure-fed hypergolic engine, 10:1 throttling ratio, 10,500 lbf maximum-rated thrust, ±6 degree gimbal capability, and a 305 lbf-sec/lbm end-of-duty-cycle specific-impulse design requirement. These are valid architecture/design-envelope evidence, not an LM-5 as-flown thrust/Isp time history.

The Apollo 11 press kit gives LM-5 launch bookkeeping: 33,205 lb total, including 18,100 lb loaded DPS propellant, 5,214 lb APS propellant, 604 lb RCS propellant, 4,483 lb dry descent stage, and 4,804 lb dry ascent stage. Those values constrain vehicle/resource accounting but are not the mass at powered-descent initiation.

The Apollo 11 final Flight Plan adds a second bookkeeping state: its SPS budget assumptions use an unmanned LM weight of **33,278.3 lb** and separately specify **436.7 lb transferred from CSM to LM during lunar-orbit activity**. This confirms that launch/unmanned bookkeeping and descent configuration are distinct states; it still does not close PDI mass because crew mass, consumable losses, RCS use, DOI propellant expenditure, and exact event accounting must be reconciled rather than guessed.

A targeted mass-properties search identified the primary document family used for mission-event states: **CSM/LM Spacecraft Operational Data Book, Volume III — Mass Properties, SNA-8-D-027(III) Rev. 2 / NASA-TM-X-68968**. NASA describes Volume III as mission-specific mass-properties/consumable-loading documentation maintained through actual consumable loading. The base Rev. 2 is dated 20 August 1969 and covers G/H/J mission data.

### Amendment-provenance trap identified

The publicly digitized Rev. 2 binder is not a pristine 20 August 1969 snapshot. Its indexed text contains later replacement pages: the section 3 introduction is marked **Amendment 86, 9/10/70**, while an indexed table 3.1-8 page is marked **Amendment 110, 7/19/71** and describes **LM-10**, not LM-5. Therefore section/table numbers in the surviving scan cannot be assumed to preserve the original Mission-G contents merely because the title page says Rev. 2.

This changes the recovery requirement: an LM-5 `PRE P.D.I.` number is acceptable only from a page whose mission identity and amendment/effective date establish Mission-G applicability. A later overwritten table, a neighboring LM, or an unlabeled extracted value is insufficient. Existing Apollo 13 work still demonstrates that this document family used sequential mass-properties and consumables-change tables with explicit pre-PDI states, but those LM-7 values remain non-transferable.

### Mission-specific postflight mass-properties cross-check

The **Apollo 11 Mission Report, Appendix A.6 / table A-I** is itself a primary mission-specific postflight mass-properties source. NASA states that the table reflects postflight analysis of expendable loadings and usage, with measured module/stage weights updated for changes after weighing. Its LM rows give **33,683.5 lb at LM separation**, **33,669.6 lb at DOI ignition**, **33,401.6 lb at DOI cutoff**, and **16,153.2 lb at lunar landing**.

This is stronger provenance than the amended operational-data-book scan for those named events, but table A-I does **not** include a PDI row. It therefore narrows and validates the event accounting without closing PDI mass.

A secondary NASA compilation, *Apollo by the Numbers* (SP-4029), was checked because its cross-mission table labels an Apollo 11 value under `LM at Powered Descent Initiation`. That row shows **33,669.6 lb**, while the same compilation's `LM at Descent Orbit Insertion Ignition` row shows **33,401.6 lb**. Those numbers conflict with the primary Apollo 11 Mission Report, which explicitly assigns 33,669.6 lb to DOI ignition and 33,401.6 lb to DOI cutoff. The secondary compilation is therefore **not accepted as evidence for Apollo 11 PDI mass**; its apparent event-label shift must not be propagated into the simulator.

The Apollo 11 Mission Report closes more of the as-flown propulsion envelope. Section 9.8 reports the 756.3-second powered descent, approximately 6775 ft/s velocity change, 13% minimum-throttle start, throttle-up to full after about 26 seconds, and a roughly 45-second data dropout. Figure 9.8-1 records flight throttle position, chamber pressure, regulator outlet pressure, and fuel/oxidizer interface pressures against mission time. These are legitimate as-flown validation products, but they do not by themselves establish exact delivered thrust or effective Isp versus time.

A later primary NASA mission-report supplement table identifies **Apollo 11 Mission Report Supplement 7, _Descent Propulsion System Final Flight Evaluation_, published September 1970**. A targeted public recovery pass did not recover a copy. This remains a named-source recovery target.

TRW Note 70-FMT-819 / NASA CR-108349, *Apollo Mission 11, Trajectory Reconstruction and Postflight Analysis, Volume I* (16 March 1970), documents the DOI→touchdown reconstruction. The actual 45-day BET listing is assigned to unrecovered Volume II in NASA Apollo Trajectory format; broad online discovery is exhausted and recovery is archive-triggered.

NASA TN D-6846 / MSC-S-295, Floyd V. Bennett's *Apollo Experience Report: Mission Planning for Lunar Module Descent and Ascent* (June 1972), preserves Apollo 11 planned and postflight descent products. Together with Mission Report §9.8/fig. 9.8-1, the validation contract includes commanded/planned relationships and as-flown propulsion telemetry relationships without fabricating an exact force history.

## Existing model audit

| Model input | Apollo source status | Promotion decision |
| --- | --- | --- |
| `thrust_n` / `end_thrust_n` | D-7143 design envelope; D-6846 command relationships; Mission Report flight throttle/chamber-pressure history; exact delivered thrust unresolved | Keep caller supplied; validate timing/shape against documented flight evidence; do not infer exact thrust from throttle percentage alone |
| `specific_impulse_s` | D-7143 design requirement; no LM-5 flight-effective history recovered | Keep caller supplied; do not freeze 305 s as Apollo 11 truth |
| `mass_kg` | Mission Report table A-I documents postflight LM event masses through DOI cutoff and landing, but no PDI row; amended ODB scan cannot safely supply the missing row | Keep PDI mass unresolved; use table A-I named-event masses as primary validation checkpoints |
| `dry_mass_kg` | Published stage/resource bookkeeping does not equal the model depletion floor convention | Do not equate without a scenario mass convention |
| thrust `direction` | DPS gimbal capability and attitude validation products documented | Exact command history unresolved |
| burn duration | 756.3 s documented | Historical checkpoint |
| continuous position/velocity history | Reconstruction method documented; Volume-II NAT listing unrecovered | Keep RECONSTRUCTED; do not fabricate exact samples |

## D-022 result

No D-022 closure is claimed for PDI mass. The primary Mission Report now supplies high-confidence adjacent event checkpoints, but the exact PDI state is still absent. A secondary NASA compilation that appears to provide the missing value is contradicted by the primary event assignments and is rejected for this purpose.

## Architecture consequence

Historical validation can use **DOCUMENTED postflight LM event masses + DOCUMENTED as-flown throttle/pressure telemetry + DOCUMENTED event/checkpoint and command relationships + RECONSTRUCTED trajectory methodology + MODELLED unresolved PDI mass/thrust/Isp inputs**. The simulator must not derive PDI mass by arithmetic from launch mass or silently relabel the Mission Report's DOI ignition/cutoff masses as PDI.

## Next

Continue the PDI-mass search only against a source that explicitly labels a Mission-G/LM-5 PDI or pre-PDI state with trustworthy provenance. Prioritize superseded Mission-G operational-data-book pages, mission-specific contractor/postflight mass ledgers, or a recovered Apollo 11 DPS Supplement 7. Treat *Apollo by the Numbers* as a warning source for this field, not as closure. Reopen Volume-II BET only on a concrete archive/digitization lead.

## Evidence status

**PARTIALLY DOCUMENTED.** Primary postflight LM mass checkpoints are now documented at separation, DOI ignition, DOI cutoff, and landing. Exact LM-5 PDI mass remains unresolved, and a tempting secondary NASA PDI value has been rejected because its event assignments conflict with the primary Mission Report. Exact delivered thrust/Isp also remain unresolved; Apollo 11 DPS Supplement 7 and TRW Volume II are **BLOCKED ON NAMED SOURCE RECOVERY**.