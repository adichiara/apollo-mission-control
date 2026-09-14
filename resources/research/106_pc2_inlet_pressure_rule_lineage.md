# Apollo 13 PC+2 — inlet-pressure rule lineage follow-up

Date: 2026-09-13  
Status: **REVIEWED-PARTIAL — historical lineage strongly narrows the 150-psi ground criterion toward fuel inlet pressure, but an Apollo 13-specific source tying the rule unambiguously to GQ3611P has not yet been recovered. Keep the executable rule NOT_EVALUABLE.**

## Purpose

Research note 057 established that LM-7 carried two distinct engine-interface pressure measurements:

- `GQ3611P` — engine interface fuel pressure;
- `GQ4111P` — engine interface oxidizer pressure.

It deliberately refused to guess how Apollo 13's singular ground rule, “engine inlet pressure = 150 psi,” selected or combined those measurements.

This follow-up asks whether the documented rule lineage resolves that ambiguity.

## 1. Apollo 13 PC+2 wording remains generic on the ground side

The Flight Control Division *Mission Operations Report — Apollo 13* records the PC+2 shutdown criterion as:

- engine inlet pressure = 150 psi on the ground or 160 psi onboard.

The Apollo 13 air-to-ground rule read-up at about 76:30 GET says the rules should be **similar to LOI Mode I abort with tight limits**. CAPCOM describes the onboard criterion as DPS propellant-tank pressure / inlet pressure, 160 psi or below.

The CONTROL post-mission material similarly describes “engine inlets” for the onboard 160-psia criterion and separately preserves the fuel-to-oxidizer delta-P criterion as a ground callout.

These Apollo 13 sources do not themselves name `GQ3611P` or state a fuel/oxidizer aggregation formula for the 150-psi ground value.

## 2. The LOI/DPS rule lineage names fuel inlet pressure

Apollo 10 Mission Rules, Section 3, item 3-77, states that a DPS maneuver will be inhibited for several LM problems, including:

- **fuel inlet pressure <120 psi for <65 percent throttle**;
- **fuel inlet pressure <150 psi for >65 percent throttle**.

This is materially more specific than the later Apollo 13 narrative shorthand “engine inlet pressure.” It does **not** say either inlet, minimum inlet, averaged inlet, or oxidizer inlet.

Apollo 13 PC+2 used a throttle profile of approximately 12.6 percent for 5 seconds, 40 percent for 21 seconds, then maximum thrust for roughly 235 seconds. The 150-psi value therefore aligns directly with the >65-percent/full-throttle portion of the earlier DPS rule lineage.

Apollo 11 Mission Rules also identify the corresponding DPS quantity as **fuel inlet pressure**, although the reviewed Apollo 11 summary carries a 120-psi limit rather than the Apollo 10 two-level throttle-dependent rule. That continuity supports the measurement identity (“fuel inlet”), while also showing that numeric rule details changed across mission-rule revisions and should not be imported casually.

## 3. LM-7 redline data keeps fuel and oxidizer measurements separate

March 9, 1970 LM-7-and-subsequent redline documentation lists `GQ3611P` and `GQ4111P` together as separate “Press Engine Interface Fuel” and “Press Engine Interface Ox” measurements. The table gives nominal operation values of Fuel: 150 and Ox: 150 at 70°F.

This confirms that both measurements existed and were separately identified on LM-7-family telemetry. It does **not** establish that both participated in the PC+2 150-psi shutdown rule.

## 4. What can now be said safely

The evidence now supports a stronger historical interpretation than note 057 could make:

1. Apollo 13 explicitly said its PC+2 rules followed the LOI Mode I abort philosophy with tighter limits.
2. A surviving Apollo DPS mission rule in that lineage names **fuel inlet pressure** and gives the same **150-psi** threshold when throttle is above 65 percent.
3. Apollo 13 PC+2 spent most of the burn at maximum thrust, so the throttle regime is compatible with that 150-psi branch.
4. LM-7 had a dedicated fuel engine-interface pressure measurement, `GQ3611P`.

Therefore, **fuel inlet pressure / GQ3611P is the leading source-backed candidate for the Apollo 13 ground criterion.**

## 5. What remains unsupported

The reviewed evidence still does not provide an Apollo 13-specific mission-rule/display page that explicitly says:

> PC+2 ground shutdown when GQ3611P ≤150 psi.

Nor does it establish:

- exact CONTROL display field/routing during PC+2;
- any automatic limit-sense logic tied to the criterion;
- whether the Apollo 13 FCD narrative intentionally generalized a fuel-only rule or reflected a revised two-inlet rule;
- exact inequality convention at the threshold (`<150` versus `≤150`) for the Apollo 13 ground product;
- update cadence/filtering/scaling used at CONTROL.

The Apollo 13 narrative sources and CONTROL post-mission wording are not overridden by inference from Apollo 10.

## 6. Implementation consequence

**No executable change is authorized by this note.**

Keep the ground 150-psi rule `NOT_EVALUABLE` until an Apollo 13-specific rule/display/routing source is recovered or the project deliberately adopts a labeled historical approximation.

Do not implement:

- minimum(fuel, oxidizer);
- either-side trigger;
- average(fuel, oxidizer);
- a synthetic combined `dps_inlet_pressure_psi`;
- automatic mapping of the 150-psi rule to `GQ3611P` as if directly proven for Apollo 13.

If a later first-playable revision needs a historically bounded approximation, the only currently defensible candidate is **fuel engine-interface pressure (`GQ3611P`)**, explicitly labeled as a lineage-based approximation rather than an Apollo 13-specific recovered mapping.

## 7. Research priority

This remains a bounded, nonblocking historical gap. Highest-value evidence would be:

1. Apollo 13 mission-rule pages for DPS/LOI Mode I or PC+2;
2. Apollo 13 CONTROL display/MSK material showing the 150-psi field;
3. MCC telemetry/display routing tying `GQ3611P` to the relevant CONTROL product during the maneuver.

Physical first-playable validation remains the project blocking boundary; this archival question should not displace it.

## Primary sources reviewed

- NASA Manned Spacecraft Center, *Apollo 10 Mission Rules*, Section 3, item 3-77, 23 Apr 1969 revision page: DPS maneuver inhibit criteria include fuel inlet pressure <120 psi below 65% throttle and <150 psi above 65% throttle.
- NASA Manned Spacecraft Center, *Apollo 11 Mission Rules*, Section 3, item 3-72: DPS maneuver inhibit criterion names fuel inlet pressure, with a 120-psi value in the reviewed summary.
- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 Apr 1970: PC+2 ground criterion “engine inlet pressure = 150 psi,” burn profile, and CONTROL post-mission appendix.
- Apollo 13 Technical Air-to-Ground Voice Transcription, ~76:30 GET: PC+2 rules described as similar to LOI Mode I abort with tight limits; onboard inlet/propellant pressure criterion read to crew.
- Grumman/NASA, LM Data Book Volume 2 Part 2, LM-6 and subsequent launch mission-rule redlines, Rev. 5, 9 Mar 1970, LED-540-57: `GQ3611P` and `GQ4111P` listed separately as engine-interface fuel/oxidizer pressure measurements; nominal 150 psia values at 70°F.

## Relationship to earlier work

This note **supplements but does not supersede** note 057. Note 057's prohibition on invented aggregation remains correct. The new finding changes the best historical hypothesis from “unknown selection/aggregation” to “fuel inlet is the leading lineage-supported interpretation,” while retaining `NOT_EVALUABLE` in the executable model.