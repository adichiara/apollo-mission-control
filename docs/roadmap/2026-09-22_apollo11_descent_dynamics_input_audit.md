# Roadmap continuation — Apollo 11 descent dynamics input audit

Date: 2026-09-22
Parent: `docs/roadmap/2026-09-22_apollo11_descent_continuous_trajectory_boundary.md`

## Bounded question

Which inputs already accepted by the generic DPS/translational proofs can be tied to primary Apollo sources without pretending that design values are Apollo 11 delivered-flight values?

## Primary-source findings

NASA TN D-7143 establishes the DPS design envelope: pressure-fed hypergolic engine, 10:1 throttling ratio, 10,500 lbf maximum-rated thrust, ±6 degree gimbal capability, and a 305 lbf-sec/lbm end-of-duty-cycle specific-impulse design requirement. These are valid architecture/design-envelope evidence, not an LM-5 as-flown thrust/Isp time history.

The Apollo 11 press kit gives LM-5 launch bookkeeping: 33,205 lb total, including 18,100 lb loaded DPS propellant, 5,214 lb APS propellant, 604 lb RCS propellant, 4,483 lb dry descent stage, and 4,804 lb dry ascent stage. Those values constrain vehicle/resource accounting but are not the mass at powered-descent initiation; intervening DOI/RCS use and consumables prevent using launch mass as PDI mass.

The Apollo 11 Mission Report documents a 756.3-second powered descent and reports that DPS propellant use exceeded prediction because of additional landing-site redesignation time. It supplies event/checkpoint validation, not a complete delivered thrust history.

### Postflight trajectory reconstruction recovered

TRW Note 70-FMT-819 / NASA CR-108349, *Apollo Mission 11, Trajectory Reconstruction and Postflight Analysis, Volume I* (16 March 1970), documents the postflight reconstruction. Section 7.2.3.1 states that the original powered-descent best-estimate trajectory was based on a fit to low-speed MSFN data and a landing-site constraint; a subsequent reconstruction combined onboard and high-speed MSFN data with pre-PDI relative tracking to produce a consistent continuous LM trajectory from DOI through touchdown.

Volume I also establishes that the actual 45-day BET listing is in **Volume II**, in NASA Apollo Trajectory (NAT) format, and was not generally distributed. A targeted 2026-09-22 recovery pass using the exact report number/title, contractor identifiers, NASA accession, NAT/BET terminology, NTRS, and archive-oriented searches recovered no public primary Volume-II copy or traceable derivative. The named source remains **BLOCKED ON NAMED SOURCE RECOVERY**; repeated broad web discovery is no longer a useful active task.

### Primary validation envelope recovered

NASA TN D-6846 / MSC-S-295, Floyd V. Bennett's *Apollo Experience Report: Mission Planning for Lunar Module Descent and Ascent* (June 1972), is a primary NASA synthesis of the Apollo 11 planning, real-time, and postflight work. It preserves both premission and postflight descent products: the event table and planned thrust/attitude history, guidance thrust command versus horizontal velocity, landing-radar updates, approach and landing trajectories, attitude, altitude-versus-altitude-rate, and landing-phase events. It explicitly distinguishes the nominal/planned descent from the actual landing-phase behavior after manual terrain avoidance.

This closes a useful validation seam without inventing missing physics. A model can be checked against source-backed event ordering, trajectory/checkpoint behavior, and thrust-command relationships even while exact PDI mass, delivered thrust, effective Isp, and Volume-II NAT states remain unavailable. Plotted or commanded values are not to be relabeled as an exact delivered engine history.

## Existing model audit

| Model input | Existing semantic fit | Apollo source status | Promotion decision |
| --- | --- | --- | --- |
| `thrust_n` / `end_thrust_n` | Yes | D-7143 supplies design envelope; D-6846 supplies planned/command validation relationships; no LM-5 delivered time history recovered | Keep caller supplied; validate behavior against source-backed envelope, not an invented as-flown profile |
| `specific_impulse_s` | Yes | D-7143 supplies design requirement; not LM-5 flight-effective history | Keep caller supplied; do not freeze 305 s as Apollo 11 truth |
| `mass_kg` | Yes | LM-5 launch mass/loading documented; PDI epoch mass not closed by those figures | PDI mass remains unresolved |
| `dry_mass_kg` | Numerical depletion floor, not spacecraft bookkeeping | Press kit separates dry stages and multiple propellant systems | Do not equate model floor with published descent-stage dry mass without a scenario mass convention |
| thrust `direction` | Yes | DPS gimbal capability documented; D-6846 supplies planned/actual attitude validation products | Exact inertial/body-frame command history remains unresolved |
| central gravity `mu` / center | Yes | Model accepts source-supplied lunar gravity parameter | Source and frame convention still must be frozen before historical validation |
| burn duration | Yes | 756.3 s total powered descent documented | Useful validation checkpoint; insufficient to derive segment throttle history |
| continuous position/velocity history | Yes | 70-FMT-819 documents reconstruction method; actual 45-day BET listing remains unrecovered Volume II | Keep RECONSTRUCTED; use D-6846 checkpoint products without fabricating exact state samples |

## D-022 result

No D-022 closure is claimed. The recovered material provides validation products, not two sourced endpoints of an Apollo-11-specific uncertain input whose irrelevance has been demonstrated at player-product resolution.

## Architecture consequence

The historical validation contract is now stronger and more explicit: **DOCUMENTED event/checkpoint and command/trajectory relationships + RECONSTRUCTED trajectory methodology/reference + MODELLED propulsion/mass inputs**. Exact continuous states remain optional refinement blocked on Volume-II recovery; they are no longer a reason to stall the model-validation path.

## Next

Move active research to the still decision-relevant **LM-5 PDI mass/state bookkeeping** target. Search mission mass-property/operational-data material and mission-specific postflight propulsion/performance records first. Keep the delivered DPS thrust/Isp history as a parallel target, but accept TN D-6846's source-backed validation envelope where exact engine history is unnecessary. Reopen Volume-II BET recovery only on a concrete archival/digitization lead.

## Evidence status

**PARTIALLY DOCUMENTED.** Reconstruction methods, comparison semantics, DPS design physics, mission checkpoints, and a primary NASA descent validation envelope are documented. The machine-usable 45-day BET state listing remains **BLOCKED ON NAMED SOURCE RECOVERY**; Apollo-11-specific PDI mass and delivered thrust/Isp history remain unresolved.