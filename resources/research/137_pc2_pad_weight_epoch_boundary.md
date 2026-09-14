# 137 — PC+2 maneuver-pad weight epoch boundary

## Question

What can the documented Apollo 13 PC+2 CSM/LM weights safely mean in the causal numerical model?

## Primary-source finding

NASA's Apollo 13 Technical Air-to-Ground Voice Transcription records the final PC+2 P30 LM maneuver PAD at GET 077:55:24. CAPCOM transmitted:

- TIG / Noun 33: `079:27:38.30`
- resultant ΔV: `0861.5` ft/s
- burn duration: `4:24`
- CSM weight: `62480` lb
- LM weight: `33452` lb
- DPS profile: 5 seconds minimum, 21 seconds at 40 percent, remainder MAX

At GET 077:59:23 Haise repeated the CSM and LM weights with the rest of the maneuver data after improving the radio link. At 077:59:50 CAPCOM confirmed that, apart from clarifying the 40-percent wording, the readback was correct.

Primary archive identity: NASA NTRS, *Apollo 13 Technical Air-To-Ground Voice Transcription*, publication date 1970-04-01, NTRS 20160014370. NASA's currently indexed transcript PDF (`as13-tec.pdf`) exposes the quoted passage on transcript page 329.

Sources:

- NASA NTRS: https://ntrs.nasa.gov/citations/20160014370
- NASA indexed technical transcript PDF: https://www.nasa.gov/wp-content/uploads/2026/01/as13-tec.pdf
- Cross-check only: Apollo Flight Journal, Day 4 part 2, https://www.apollojournals.org/afj/ap13fj/13day4-leaving-moon.html

## Evidence boundary

### DOCUMENTED

The pair `62480 lb CSM / 33452 lb LM` was part of the final operational PC+2 maneuver PAD transmitted shortly before the burn and accepted by crew/ground readback.

### NOT DOCUMENTED BY THIS SOURCE

The transcript does **not** define those numbers as:

- an instantaneous scale-equivalent physical mass at ignition;
- an RTCC propagated mass state at the exact TIG;
- a mass after accounting for the 10-second ullage expenditure;
- a mass after accounting for the early DPS minimum/40-percent segments;
- a universal Apollo 13 stack-mass constant; or
- the exact mass convention used internally by the RTCC targeting computation.

Therefore the project must not silently relabel the numbers as `true ignition mass` or tune a physical model under that assumption.

## Model consequence

For regression against the historical PC+2 PAD, the values may be used as **final maneuver-pad / targeting weight inputs**:

`62480 + 33452 = 95932 lb`

The model should preserve the semantic label `pad_weight` or `targeting_weight_reference` until a mission-specific computation/weight-accounting source establishes the physical epoch and convention.

This is especially important when comparing a numerical DPS integration against the documented `861.5 ft/s` target: a mismatch must not automatically be corrected by treating the PAD weights as exact physical ignition masses.

## Status of research-note-130 target 5

Target 5 is **partially closed**:

- exact primary transcript provenance: resolved;
- operational communication epoch: resolved (final PAD at 077:55:24, confirmed by 077:59:50);
- exact physical/RTCC mass-reference epoch: unresolved.

## Next archival target

Seek a mission-specific RTCC/Flight Dynamics targeting, maneuver-computation, consumables/weight-accounting, or PC+2 computation record that defines the weight convention used for a docked CSM/LM P30 solution. Do not substitute adjacent-mission terminology without an applicability bridge.