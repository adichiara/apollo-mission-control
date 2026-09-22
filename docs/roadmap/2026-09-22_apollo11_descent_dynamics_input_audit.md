# Roadmap continuation — Apollo 11 descent dynamics input audit

Date: 2026-09-22
Parent: `docs/roadmap/2026-09-22_apollo11_descent_continuous_trajectory_boundary.md`

## Bounded question

Which inputs already accepted by the generic DPS/translational proofs can be tied to primary Apollo sources without pretending that design values are Apollo 11 delivered-flight values?

## Primary-source findings

NASA TN D-7143 establishes the DPS design envelope: pressure-fed hypergolic engine, 10:1 throttling ratio, 10,500 lbf maximum-rated thrust, ±6 degree gimbal capability, and a 305 lbf-sec/lbm end-of-duty-cycle specific-impulse design requirement. These are valid architecture/design-envelope evidence, not an LM-5 as-flown thrust/Isp time history.

The Apollo 11 final Flight Plan provides configuration bookkeeping but not PDI mass. SNA-8-D-027(III) Rev. 2 / NASA-TM-X-68968 is the correct mass-properties source family, but its surviving public binder contains later replacement pages and cannot be treated as a pristine Mission-G snapshot.

The **Apollo 11 Mission Report, Appendix A.6 / table A-I** provides primary postflight LM masses: **33,683.5 lb at separation, 33,669.6 lb at DOI ignition, 33,401.6 lb at DOI cutoff, and 16,153.2 lb at landing**. It contains no PDI row.

## Event-provenance hazard now demonstrated twice

NASA SP-4029, *Apollo by the Numbers*, shifts the Mission Report's DOI masses into different event labels and is therefore rejected for PDI closure.

A new audit found NASA technical paper **20080013635**, *Lunar Surface Virtual Simulation* (2008). Its simulated Apollo vehicle uses **33,683.5 lb at PDI**. That value is exactly the primary Mission Report's LM-separation mass. The paper explicitly describes an approximate simulation vehicle and supplies no contemporaneous LM-5 mass-ledger provenance for the PDI assignment. It is therefore a simulation input, not evidence that 33,683.5 lb was the historical PDI mass.

The two conflicts make the evidence gate stricter: **a candidate PDI number is not closable merely because it appears in NASA material or numerically matches an authentic Apollo 11 mass. The source must explicitly establish Mission-G/LM-5 event identity and provenance.**

## Existing model audit

| Model input | Apollo source status | Promotion decision |
| --- | --- | --- |
| `thrust_n` / `end_thrust_n` | D-7143 design envelope; Mission Report flight throttle/chamber-pressure history; exact delivered thrust unresolved | Keep caller supplied; do not infer exact thrust from throttle percentage alone |
| `specific_impulse_s` | D-7143 design requirement; no LM-5 flight-effective history recovered | Keep caller supplied; do not freeze 305 s as Apollo 11 truth |
| `mass_kg` | Primary Mission Report documents named event masses through DOI cutoff and landing; no PDI row | Keep PDI mass unresolved; reject later event-relabeling/simulation assignments |
| `dry_mass_kg` | Published stage/resource bookkeeping does not equal the model depletion floor convention | Do not equate without a scenario mass convention |
| thrust `direction` | DPS gimbal capability and attitude validation products documented | Exact command history unresolved |
| burn duration | 756.3 s documented | Historical checkpoint |
| continuous position/velocity history | Reconstruction method documented; Volume-II NAT listing unrecovered | Keep RECONSTRUCTED; do not fabricate exact samples |

## D-022 result

No D-022 closure is claimed for PDI mass. Adjacent primary checkpoints do not define a sufficiently sourced numerical range because propellant/RCS/consumable changes between DOI cutoff and PDI have not yet been reconciled from a Mission-G ledger. Later NASA event assignments cannot substitute for that missing accounting.

## Architecture consequence

Historical validation may use **DOCUMENTED primary named-event masses + DOCUMENTED as-flown throttle/pressure telemetry + RECONSTRUCTED trajectory methodology + MODELLED unresolved PDI mass/thrust/Isp inputs**. Any scenario fixture using a convenient PDI mass must be labeled MODELLED unless a contemporaneous Mission-G source closes it.

## Next

Continue the PDI-mass search only against an explicitly labeled Mission-G/LM-5 PDI or pre-PDI source with trustworthy event provenance. Prioritize superseded Mission-G ODB pages, contractor/postflight mass ledgers, or recovered Apollo 11 DPS Supplement 7. Reopen TRW Volume-II BET only on a concrete archive/digitization lead.

## Evidence status

**PARTIALLY DOCUMENTED.** Primary postflight LM mass checkpoints are documented. Exact LM-5 PDI mass remains unresolved. Two later NASA sources/products now demonstrate event-assignment drift, so value-only triangulation is explicitly disallowed. Exact delivered thrust/Isp also remain unresolved; Apollo 11 DPS Supplement 7 and TRW Volume II remain **BLOCKED ON NAMED SOURCE RECOVERY**.