# Research Note 190 — LM-7 premission mass-properties source boundary

Date: 2026-09-16

## Question

Can the documented statement that LM CONTROL used `premission mass properties` be tied to a recoverable Apollo 13 / LM-7 preflight source, and does that recover CONTROL's actual trim inputs or competing numerical solution?

## Primary sources

1. NASA/Grumman, *CSM/LM Spacecraft Operational Data Book, Volume II, Part 2 — Launch Mission Rule Redlines*, Revision 5, 9 March 1970, including LM-7 amendments.
2. NASA/Grumman, LM-7 Descent Propulsion System weight-characteristics material, SNA-8-D-027(II) Rev. 2, Amendment 55, 17 March 1970, Table LM7/4.7.1-1.
3. NASA/MSC Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970.

## Findings

The LM-7 DPS preflight engineering material is mission-specific and contemporaneous. Table LM7/4.7.1-1 gives a preflight LM-7 weight model including:

- DPS stage inert: `4,523.0 lbm`;
- loaded DPS propellant: `18,434.8 lbm` (`11,351.1` oxidizer, `7,083.7` fuel);
- loaded APS stage and crew: `10,914.5 lbm`;
- LM weight at separation: `33,872.3 lbm`.

The same table explicitly warns that these mass properties were used **for the purpose of that analysis** and directs the reader to **Volume III, Spacecraft Operational Data Book, for current official mass-properties data**.

The March 9 Volume II revision is explicitly an LM-6-and-subsequent operational-data-book revision and lists LM-7-specific amendments. This establishes that mission-specific preflight LM-7 mass-property documentation existed in the operational-data-book family before launch.

The Apollo 13 Flight Dynamics postflight chronology separately says LM CONTROL challenged the ~59 GET DPS trim because CONTROL had used `premission mass properties`, which were `not the best data available`.

## Interpretation

This recovers an identifiable **premission LM-7 mass-properties source family** and an example mission-specific preflight weight model, but it does **not** identify the exact dataset CONTROL used. The source itself points away from treating its Table LM7/4.7.1-1 values as the official operational set by directing users to Volume III for current official mass properties.

Therefore the repository must not substitute the recovered `33,872.3 lbm` separation weight, its component weights, or any Volume II DPS-analysis values for CONTROL's actual ~59 GET computation. The needed artifact is now more sharply defined: the Apollo 13/LM-7 **Volume III current official mass-properties set or controller derivative actually used by CONTROL**, ideally with the applicable docked CSM/LM configuration and c.g. values.

This also strengthens the interpretation of the Flight Dynamics disagreement. `Premission mass properties` need not mean a single immutable launch-day number; there were mission-specific preflight engineering datasets with explicit currency/authority distinctions. The mission report's statement that CONTROL's set was not the best available is therefore consistent with the operational documentation hierarchy, but no exact CONTROL source or numerical delta is inferred.

## Modeling consequence

Add source-state metadata for mass-property inputs:

- `mission_specific`;
- `preflight_or_realtime`;
- `authority/currentness`;
- `configuration_scope`;
- `reference_epoch`;
- `controller_selected_source`.

Do not equate `premission` with `official current Volume III`, and do not populate CONTROL's input values from Table LM7/4.7.1-1.

## Next target

Seek Volume III *Spacecraft Operational Data Book — Mass Properties* material applicable to LM-7/Apollo 13, especially the current official preflight CSM/LM docked mass-properties tables and revision/amendment trail. Then seek controller working material showing which premission set CONTROL actually selected. In parallel, continue seeking the T+55 real-time weight/c.g. product or RTCC/RTACF request/output linking the updated LM-burn deck to `5.86 / 6.75`.