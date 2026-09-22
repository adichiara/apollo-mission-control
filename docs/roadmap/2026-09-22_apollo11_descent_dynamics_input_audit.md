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
| continuous position/velocity history | Yes | 70-FMT-819 documents a postflight BET/reconstruction from MSFN, onboard, and relative-tracking data | Admit only as RECONSTRUCTED mission evidence, not raw documented truth |

## D-022 result

No D-022 closure is claimed in this pass. The recovered design values are not two sourced endpoints of an Apollo-11-specific uncertain input whose irrelevance has been demonstrated at a player-product resolution.

## Architecture consequence

The generic models already have the correct parameter seams. The project may now use the 70-FMT-819 postflight trajectory as a historical **validation/reference trajectory** if its tabulated/graphical states are extracted with provenance. It must not silently become authoritative physical truth or be reverse-engineered into an unsupported delivered thrust profile.

The next work should separate three classes explicitly: DOCUMENTED event/checkpoint facts, RECONSTRUCTED continuous trajectory states from the postflight BET, and MODELLED propulsion/mass inputs needed to reproduce or approximate those states.

## Next

Extract the usable DOI→touchdown state/checkpoint products from 70-FMT-819 and map their frame/epoch definitions before feeding them to the model lab. Continue a bounded search for LM-5 PDI mass/state bookkeeping and DPS final-flight/performance material; if those remain unavailable, implement the documented/reconstructed/modelled provenance contract rather than inventing them.

## Evidence status

**PARTIALLY DOCUMENTED.** Model semantics align with documented DPS physics, and a mission-specific postflight continuous trajectory reconstruction is now identified. Apollo-11-specific PDI mass and delivered thrust/Isp history remain unresolved; the continuous trajectory is explicitly RECONSTRUCTED.