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

TRW Note 70-FMT-819 / NASA CR-108349, *Apollo Mission 11, Trajectory Reconstruction and Postflight Analysis, Volume 1* (16 March 1970), closes a different part of the problem. Section 7.2.3.1 states that the original powered-descent best-estimate trajectory was based on a fit to low-speed MSFN data from revolution-14 acquisition through touchdown and was modified to force the landing point to the then-current best landing-site estimate. The report then describes a subsequent reconstruction using onboard plus high-speed MSFN data; combined with relative tracking before PDI, this produced a consistent, continuous LM trajectory from DOI through touchdown.

This is strong mission-specific postflight evidence for a **reconstructed continuous trajectory**, but it is not a raw as-flown truth stream and it does not establish an LM-5 PDI mass or delivered DPS thrust/Isp time history. The report itself documents estimation/fitting and landing-site constraints, so simulator provenance must preserve that distinction.

### Extraction audit

The follow-on extraction pass establishes an important source boundary. Volume I describes the reconstruction and comparison products, but its foreword says the actual 45-day BET listing is in **Volume II**, in NASA Apollo Trajectory (NAT) format. Volume II was not generally distributed; the report directs requests to the MSC Computations and Analysis Division Central Metric Data File. The publicly recovered Volume I therefore cannot honestly be treated as a tabulated DOI→touchdown state history.

Volume I does provide useful reconstruction semantics. The descent was divided into undocking→DOI, DOI→PDI, and PDI→touchdown segments. Section 7.4.1 compares six descent solutions: real-time RTCC, low-speed MSFN, onboard relative tracking, landing-site-constrained BET #3, a Lear high-speed MSFN solution, and an onboard/MSFN high-speed HOPE solution. The Lear solution used 10-sample/s high-speed MSFN data over a 232-second arc just before PDI. The combined onboard/MSFN solution used high-speed Doppler compacted to 30 observations/minute plus CSM sextant and VHF ranging data, and modeled the descent burn in HOPE with telemetered acceleration through its IGS burn option.

Volume I also defines a UVW-type **CSM-centered relative coordinate system** for its relative-trajectory comparison figures: RZ is negative U/radial, RX is V/downrange, and RY is negative W/crossrange, with corresponding velocity components. That definition is valid for those comparison products; it must not be generalized to the unrecovered NAT Volume-II state listing without the NAT format/frame definition.

## Existing model audit

| Model input | Existing semantic fit | Apollo source status | Promotion decision |
| --- | --- | --- | --- |
| `thrust_n` / `end_thrust_n` | Yes | D-7143 supplies design envelope; no LM-5 delivered time history recovered here | Keep caller supplied; design values may bound tests, not label an as-flown profile |
| `specific_impulse_s` | Yes | D-7143 supplies design requirement; not LM-5 flight-effective history | Keep caller supplied; do not freeze 305 s as Apollo 11 truth |
| `mass_kg` | Yes | LM-5 launch mass/loading documented; PDI epoch mass not closed by those figures | PDI mass remains unresolved |
| `dry_mass_kg` | Numerical depletion floor, not spacecraft bookkeeping | Press kit separates dry stages and multiple propellant systems | Do not equate model floor with published descent-stage dry mass without a scenario mass convention |
| thrust `direction` | Yes | DPS gimbal capability documented; guidance-mode semantics documented elsewhere | Exact inertial/body-frame command history remains unresolved |
| central gravity `mu` / center | Yes | Model accepts source-supplied lunar gravity parameter | Source and frame convention still must be frozen before historical validation |
| burn duration | Yes | 756.3 s total powered descent documented | Useful validation checkpoint; insufficient to derive segment throttle history |
| continuous position/velocity history | Yes | 70-FMT-819 documents the reconstruction method, but the actual 45-day BET state listing is assigned to unrecovered Volume II | Keep RECONSTRUCTED; do not fabricate state samples from Volume-I plots |

## D-022 result

No D-022 closure is claimed in this pass. The recovered design values are not two sourced endpoints of an Apollo-11-specific uncertain input whose irrelevance has been demonstrated at a player-product resolution.

## Architecture consequence

The generic models already have the correct parameter seams. Volume I is now sufficient to define the **provenance and reconstruction-method contract**, but not to populate an authoritative state-series fixture. Graph digitization may be used only as an explicitly approximate derived dataset if a future product needs it; it must not masquerade as the Volume-II NAT listing.

The historical validation contract is therefore: DOCUMENTED event/checkpoint facts + RECONSTRUCTED trajectory methodology/reference + MODELLED propulsion/mass inputs. A tabulated RECONSTRUCTED state history remains blocked on recovery of Volume II (or an independently archived derivative that preserves NAT epochs, frames, units, and provenance).

## Next

Search specifically for TRW 70-FMT-819 Volume II / the 45-day Apollo 11 BET NAT listing or a traceable archival derivative. In parallel, continue the narrower LM-5 PDI mass and DPS delivered-performance search. Do not infer NAT frame/epoch semantics from the CSM-centered UVW comparison plots.

## Evidence status

**PARTIALLY DOCUMENTED.** Reconstruction methods, data sources, comparison-frame semantics, DPS physics, and mission checkpoints are documented. The machine-usable 45-day BET state listing is **BLOCKED ON NAMED SOURCE RECOVERY** (Volume II); Apollo-11-specific PDI mass and delivered thrust/Isp history remain unresolved.