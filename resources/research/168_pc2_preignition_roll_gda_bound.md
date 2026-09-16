# Research note 168 — PC+2 pre-ignition roll-GDA bound

Date: 2026-09-15

## Question

Can the primary CONTROL record recover any numerical component of the retained GDA state immediately before PC+2, without inventing the missing RTCC comparison?

## Primary-source finding

Yes, for the roll axis only and only approximately.

The LM CONTROL section of the NASA Manned Spacecraft Center Flight Control Division *Mission Operations Report — Apollo 13* (MSC-02680, 28 April 1970) reports that at PC+2 ignition the roll GDA moved to approximately `-2°`, a change of `-1.2°` from its pre-ignition position. The same passage says this motion was unexpected because the ground believed the GDA settings left at the end of the preceding `MCC-3` DPS maneuver, including its 40-percent-thrust compliance, would provide optimum GDA alignment for PC+2.

Primary report:
- NASA/MSC Flight Control Division, *Mission Operations Report — Apollo 13*, MSC-02680, 28 April 1970, LM CONTROL section H-4/H-5.
- NASA scan/cataloged project copy: see `resources/PRIMARY_SOURCE_CATALOG.md` and `resources/source-catalog/PC2_GDA_TRIM_SOURCES.md`.

## Derived numerical bound

The report supplies both the approximate post-motion roll position and the signed change. Simple subtraction therefore gives an approximate immediately pre-ignition roll-GDA position:

`pre-ignition roll GDA ≈ (-2.0°) - (-1.2°) = -0.8°`

This `~-0.8°` value is a transparent arithmetic derivation from two primary-source quantities, not a separately printed controller value. It should therefore be labeled **derived/approximate**, not DOCUMENTED as an independently reported number.

## What this resolves

The previously unresolved "post-61:29 reference GDA angles" target can now be narrowed:

- roll axis: the retained state immediately before PC+2 is constrained to approximately `-0.8°` by the CONTROL execution narrative;
- pitch axis: still unrecovered;
- exact post-61:29 value at maneuver cutoff: still unrecovered, because the source establishes the state immediately before PC+2, not that no intervening adjustment occurred during the long coast;
- candidate PC+2 trim and controller comparison: still unrecovered.

The result also demonstrates why the earlier interim `5.86° / 6.75°` pair must not be carried forward numerically as the final retained state. Whatever those communicated values represented at ~59:03, the later CONTROL execution record constrains the actual pre-PC+2 roll GDA to a very different neighborhood after the 61:29 powered-flight compliance and subsequent coast.

## Evidence boundary

Do not infer:

- an exact `-0.8°` value; both source inputs are approximate;
- the pitch GDA from symmetry or from the earlier interim pair;
- that `-0.8°` was exactly the value at 61:29 cutoff;
- a PC+2 trim-update tolerance;
- that the missing RTCC candidate trim equaled `-0.8°`;
- a direct numerical link from the T+55 deck to this value.

## Simulator implication

If a later PC+2 model requires an approximate observed pre-ignition roll-GDA state, `~-0.8°` now has a primary-source-derived basis. It should carry provenance such as `derived_from_reported_motion`, with uncertainty/approximation explicit. The simulator should still keep commanded trim, complied GDA state, retained pre-ignition state, and candidate mass-properties trim as distinct concepts.

## Next unresolved item

Continue archival search for the **pitch-axis retained state** and, more importantly, the controller-side comparison that justified no PC+2 update: candidate trim, reference values, delta/criterion, calculation time/job identity, and direct T+55 mass-property-deck provenance.