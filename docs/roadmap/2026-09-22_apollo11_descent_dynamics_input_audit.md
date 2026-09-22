# Roadmap continuation — Apollo 11 descent dynamics input audit

Date: 2026-09-22
Parent: `docs/roadmap/2026-09-22_apollo11_descent_continuous_trajectory_boundary.md`

## Bounded question

Which inputs already accepted by the generic DPS/translational proofs can be tied to primary Apollo sources without pretending that design values are Apollo 11 delivered-flight values?

## Primary-source findings

NASA TN D-7143 establishes the DPS design envelope: pressure-fed hypergolic engine, 10:1 throttling ratio, 10,500 lbf maximum-rated thrust, ±6 degree gimbal capability, and a 305 lbf-sec/lbm end-of-duty-cycle specific-impulse design requirement. These are valid architecture/design-envelope evidence, not an LM-5 as-flown thrust/Isp time history.

The Apollo 11 press kit gives LM-5 launch bookkeeping: 33,205 lb total, including 18,100 lb loaded DPS propellant, 5,214 lb APS propellant, 604 lb RCS propellant, 4,483 lb dry descent stage, and 4,804 lb dry ascent stage. Those values constrain vehicle/resource accounting but are not the mass at powered-descent initiation.

The Apollo 11 final Flight Plan adds a second, more useful bookkeeping state: its SPS budget assumptions use an unmanned LM weight of **33,278.3 lb** and separately specify **436.7 lb transferred from CSM to LM during lunar-orbit activity**. This confirms that launch/unmanned bookkeeping and descent configuration are distinct states; it still does not close PDI mass because crew mass, consumable losses, RCS use, DOI propellant expenditure, and the exact transfer/event accounting must be reconciled rather than guessed.

A targeted mass-properties search identified the exact primary document family used for this kind of mission-event state: **CSM/LM Spacecraft Operational Data Book, Volume III — Mass Properties, SNA-8-D-027(III) Rev. 2 / NASA-TM-X-68968**. NASA describes Volume III as mission-specific mass-properties/consumable-loading documentation maintained through actual consumable loading. The recovered 20 August 1969 revision explicitly covers G/H/J mission data. Existing repository work on Apollo 13 has already verified that later amendments of this same document contain `LM PRE P.D.I.` sequential-mass rows and consumables-change tables. That Apollo 13 value is not transferable to LM-5; it instead establishes the correct table class to recover for Mission G.

The Apollo 11 Mission Report closes more of the as-flown propulsion envelope. Section 9.8 reports the 756.3-second powered descent, approximately 6775 ft/s velocity change, 13% minimum-throttle start, throttle-up to full after about 26 seconds, and a roughly 45-second data dropout. Figure 9.8-1 records flight throttle position, chamber pressure, regulator outlet pressure, and fuel/oxidizer interface pressures against mission time. These are legitimate as-flown validation products, but they do not by themselves establish exact delivered thrust or effective Isp versus time.

A later primary NASA mission-report supplement table identifies **Apollo 11 Mission Report Supplement 7, _Descent Propulsion System Final Flight Evaluation_, published September 1970**. A targeted public recovery pass did not recover a copy. This remains a named-source recovery target.

### Postflight trajectory reconstruction recovered

TRW Note 70-FMT-819 / NASA CR-108349, *Apollo Mission 11, Trajectory Reconstruction and Postflight Analysis, Volume I* (16 March 1970), documents the DOI→touchdown reconstruction. The actual 45-day BET listing is assigned to unrecovered Volume II in NASA Apollo Trajectory format; broad online discovery is exhausted and recovery is archive-triggered.

### Primary validation envelope recovered

NASA TN D-6846 / MSC-S-295, Floyd V. Bennett's *Apollo Experience Report: Mission Planning for Lunar Module Descent and Ascent* (June 1972), preserves Apollo 11 planned and postflight descent products. Together with Mission Report §9.8/fig. 9.8-1, the validation contract includes commanded/planned relationships and as-flown propulsion telemetry relationships without fabricating an exact force history.

## Existing model audit

| Model input | Apollo source status | Promotion decision |
| --- | --- | --- |
| `thrust_n` / `end_thrust_n` | D-7143 design envelope; D-6846 command relationships; Mission Report flight throttle/chamber-pressure history; exact delivered thrust unresolved | Keep caller supplied; validate timing/shape against documented flight evidence; do not infer exact thrust from throttle percentage alone |
| `specific_impulse_s` | D-7143 design requirement; no LM-5 flight-effective history recovered | Keep caller supplied; do not freeze 305 s as Apollo 11 truth |
| `mass_kg` | Launch/unmanned and lunar-orbit transfer bookkeeping documented; exact Mission-G pre-PDI sequential row not yet extracted | Keep PDI mass unresolved until LM-5 sequential mass-properties/consumables row is recovered and its amendment provenance checked |
| `dry_mass_kg` | Published stage/resource bookkeeping does not equal the model depletion floor convention | Do not equate without a scenario mass convention |
| thrust `direction` | DPS gimbal capability and attitude validation products documented | Exact command history unresolved |
| burn duration | 756.3 s documented | Historical checkpoint |
| continuous position/velocity history | Reconstruction method documented; Volume-II NAT listing unrecovered | Keep RECONSTRUCTED; do not fabricate exact samples |

## D-022 result

No D-022 closure is claimed. The mass search has narrowed from a generic archival hunt to a specific primary document/table class, but a sourced LM-5 pre-PDI value has not yet been recovered.

## Architecture consequence

Historical validation can use **DOCUMENTED as-flown throttle/pressure telemetry + DOCUMENTED event/checkpoint and command relationships + RECONSTRUCTED trajectory methodology + MODELLED mass/thrust/Isp inputs**. The simulator must not derive PDI mass by arithmetic from launch mass and assumed consumable use while a mission-specific sequential mass-properties source remains recoverable.

## Next

Recover the **Mission-G / LM-5 sequential mass-properties pages and consumables-change pages** from SNA-8-D-027(III) Rev. 2, including amendment dates and the `LM PRE P.D.I.` row if present. Reconcile that row against the Flight Plan's 33,278.3-lb unmanned state and 436.7-lb CSM→LM transfer without assuming that either is the PDI state. In parallel, pursue Apollo 11 Mission Report Supplement 7 through archival/catalog routes. Reopen Volume-II BET only on a concrete archive/digitization lead.

## Evidence status

**PARTIALLY DOCUMENTED.** The correct primary mass-properties document family and table class are now identified, and additional Apollo 11 configuration bookkeeping is documented. Exact LM-5 PDI mass remains unresolved pending recovery of the Mission-G sequential row. Exact delivered thrust/Isp also remain unresolved; Apollo 11 DPS Supplement 7 and TRW Volume II are **BLOCKED ON NAMED SOURCE RECOVERY**.