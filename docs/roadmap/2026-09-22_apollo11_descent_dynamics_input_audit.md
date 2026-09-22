# Roadmap continuation — Apollo 11 descent dynamics input audit

Date: 2026-09-22
Parent: `docs/roadmap/2026-09-22_apollo11_descent_continuous_trajectory_boundary.md`

## Bounded question

Which inputs already accepted by the generic DPS/translational proofs can be tied to primary Apollo sources without pretending that design values are Apollo 11 delivered-flight values?

## Primary-source findings

NASA TN D-7143 establishes the DPS design envelope: pressure-fed hypergolic engine, 10:1 throttling ratio, 10,500 lbf maximum-rated thrust, ±6 degree gimbal capability, and a 305 lbf-sec/lbm end-of-duty-cycle specific-impulse design requirement. These are valid architecture/design-envelope evidence, not an LM-5 as-flown thrust/Isp time history.

The Apollo 11 press kit gives LM-5 launch bookkeeping: 33,205 lb total, including 18,100 lb loaded DPS propellant, 5,214 lb APS propellant, 604 lb RCS propellant, 4,483 lb dry descent stage, and 4,804 lb dry ascent stage. Those values constrain vehicle/resource accounting but are not the mass at powered-descent initiation; intervening DOI/RCS use and consumables prevent using launch mass as PDI mass.

The Apollo 11 Mission Report closes more of the as-flown propulsion envelope than the earlier audit recorded. Section 9.8 reports the 756.3-second powered descent, approximately 6775 ft/s velocity change, 13% minimum-throttle start, throttle-up to full after about 26 seconds, and a roughly 45-second data dropout during that early interval. Figure 9.8-1 records flight throttle position, chamber pressure, regulator outlet pressure, and fuel/oxidizer interface pressures against mission time. These are legitimate as-flown telemetry/performance validation products, but they do not by themselves establish exact delivered thrust or effective Isp versus time.

A later primary NASA mission-report supplement table identifies **Apollo 11 Mission Report Supplement 7, _Descent Propulsion System Final Flight Evaluation_, published September 1970**. A targeted exact-title/report-identifier/NTRS search did not recover a public copy. This is now a named-source recovery target rather than a reason to extrapolate from neighboring missions.

### Postflight trajectory reconstruction recovered

TRW Note 70-FMT-819 / NASA CR-108349, *Apollo Mission 11, Trajectory Reconstruction and Postflight Analysis, Volume I* (16 March 1970), documents the postflight reconstruction. The report establishes a consistent continuous LM trajectory reconstruction from DOI through touchdown using MSFN, onboard, and relative-tracking evidence. It also establishes that the actual 45-day BET listing is in **Volume II**, in NASA Apollo Trajectory format, and was not generally distributed. Broad online discovery for Volume II is exhausted; recovery is archive-triggered.

### Primary validation envelope recovered

NASA TN D-6846 / MSC-S-295, Floyd V. Bennett's *Apollo Experience Report: Mission Planning for Lunar Module Descent and Ascent* (June 1972), preserves Apollo 11 planned and postflight descent products: event/thrust/attitude behavior, guidance thrust command versus horizontal velocity, landing-radar updates, approach/landing trajectory and attitude, altitude-versus-altitude-rate, and landing-phase events. Together with Mission Report §9.8/fig. 9.8-1, the validation contract now includes both commanded/planned relationships and as-flown propulsion telemetry relationships without fabricating an exact force history.

## Existing model audit

| Model input | Apollo source status | Promotion decision |
| --- | --- | --- |
| `thrust_n` / `end_thrust_n` | D-7143 design envelope; D-6846 command relationships; Mission Report flight throttle/chamber-pressure history; exact delivered thrust unresolved | Keep caller supplied; validate timing/shape against documented flight evidence; do not infer exact thrust from throttle percentage alone |
| `specific_impulse_s` | D-7143 design requirement; no LM-5 flight-effective history recovered | Keep caller supplied; do not freeze 305 s as Apollo 11 truth |
| `mass_kg` | Launch loading documented; PDI epoch mass not closed | PDI mass remains unresolved |
| `dry_mass_kg` | Published stage/resource bookkeeping does not equal the model depletion floor convention | Do not equate without a scenario mass convention |
| thrust `direction` | DPS gimbal capability and attitude validation products documented | Exact command history unresolved |
| burn duration | 756.3 s documented | Historical checkpoint |
| continuous position/velocity history | Reconstruction method documented; Volume-II NAT listing unrecovered | Keep RECONSTRUCTED; do not fabricate exact samples |

## D-022 result

No D-022 closure is claimed. The newly recovered propulsion evidence improves validation but does not supply sourced endpoints plus a demonstrated player-resolution irrelevance result for the unresolved PDI mass or exact thrust/Isp inputs.

## Architecture consequence

Historical validation can now use **DOCUMENTED as-flown throttle/pressure telemetry + DOCUMENTED event/checkpoint and command relationships + RECONSTRUCTED trajectory methodology + MODELLED mass/thrust/Isp inputs**. The simulator still must not present an inferred exact thrust curve, exact PDI mass, or reconstructed state history as raw historical truth.

## Next

Keep **LM-5 PDI mass/state bookkeeping** as the active unresolved input. In parallel, recover the named September-1970 Apollo 11 Mission Report Supplement 7, *Descent Propulsion System Final Flight Evaluation*, through archival/catalog routes; it is the strongest identified candidate for closing mission-specific DPS performance. Do not substitute Apollo 10/12/14/15 supplement values. Reopen Volume-II BET only on a concrete archive/digitization lead.

## Evidence status

**PARTIALLY DOCUMENTED.** Apollo 11 as-flown throttle/pressure telemetry and the propulsion/trajectory validation envelope are now bounded. PDI mass and exact delivered thrust/Isp remain unresolved. Apollo 11 DPS Supplement 7 and TRW Volume II are **BLOCKED ON NAMED SOURCE RECOVERY**.