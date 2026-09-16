# Research Note 191 — LM-7 Volume III Amendment 79 current-official set

Date: 2026-09-16

## Question

Can the Volume III current-official Apollo 13/LM-7 mass-properties target identified in Note 190 be recovered closely enough to establish its revision/amendment state before launch?

## Primary source

NASA/MSC, *CSM/LM Spacecraft Operational Data Book, Volume III — Mass Properties*, SNA-8-D-027(III) Rev. 2, with LM-7 Amendment 79 pages dated 30 March 1970.

## Findings

The recovered Volume III material contains mission-specific **LM-7** pages marked **Amendment 79, 3/30/70**, twelve days before Apollo 13 launch. This closes the source-family/revision target more tightly than Note 190.

Table 3.3-8, `LM-7 Consumables Change Summary`, explicitly says it is to be used with the `LM sequential mass properties Table 3-3.2`. It tracks mission-event consumable changes including Earth orbit -> CSM/LM separation, separation -> pre-PDI, pre-PDI -> touchdown, ascent, rendezvous, docking, and jettison. Among the printed LM-7 values are descent-stage oxygen/water, LM RCS, DPS, APS, and ascent-stage consumables.

The same amendment stream includes Table 3.3-18, `LM-7 Propellant Loading Uncertainties`, and identifies loading-related quantities that would become known after loading. Thus Volume III was not merely a generic H-mission book: by 30 March it carried an Apollo-13-specific LM-7 amendment stream tied to sequential mass properties and consumable loading.

Volume III's stated purpose is to provide per-mission mass-properties data for mission planning, trajectory documentation, mission simulations, and consumable loading, with updates based on actual spacecraft weight/balance and maintenance through actual consumables loading.

## Interpretation

This substantially closes Note 190's archival target: the applicable official operational-data-book family is **SNA-8-D-027(III) Rev. 2 + LM-7 Amendment 79 dated 30 March 1970**. It also demonstrates that a late-preflight LM-7 sequential mass-properties set existed and was coupled to mission-event consumable accounting.

It does **not** prove that CONTROL used this set at ~59 GET. The Flight Dynamics report says CONTROL used `premission mass properties` that were not the best data available; no recovered controller working paper identifies the exact premission revision/table selected. Nor does Amendment 79 prove that the real-time T+55 deck was derived directly from Table 3-3.2.

No values from the sequential table are assigned to CONTROL until the table itself and controller selection are recovered unambiguously.

## Modeling consequence

For preflight source state, add/retain:

- `document = SNA-8-D-027(III) Rev 2`;
- `amendment = 79`;
- `amendment_date = 1970-03-30`;
- `vehicle = LM-7`;
- `authority = operational mass-properties data book`;
- `controller_selected = unknown`.

Keep `official_available_preflight` distinct from `selected_by_controller` and from `realtime_updated`.

## Next target

Recover LM-7 Table 3-3.2 itself at Amendment 79/current state, especially separation/docked weight and c.g. values and amendment markings; then seek CONTROL working material identifying its selected premission set. Priority 1 remains the T+55 weight/c.g. product -> specific RTCC/RTACF run -> `5.86 / 6.75` mission-specific consumption edge.