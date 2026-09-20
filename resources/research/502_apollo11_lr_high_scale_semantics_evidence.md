# 502 — Apollo 11 landing-radar high-scale semantics evidence

Date: 2026-09-20

## Evidence

Flown LUMINARY 099 establishes:

- landing-radar altitude high/low scale state (`ALTSCBIT`);
- conditional application of `SKALSKAL` on the low-scale path;
- `SKALSKAL` described as `LR ALT SCALE FACTOR RATIO: .2 NOM`;
- low-scale LR altitude representation of 1.079 ft/count.

Primary MIT/MSC document MSC-69-FS-4, *Programmed Guidance Equations for Luminary 1B, Manned LM Earth Orbital and Lunar Program*, tabulates `DNLRALT` count values as 1.0790 ft low scale and 5.3950 ft high scale. The low/high ratio is 0.2.

This closes the semantic interpretation of `.2 NOM` to a well-supported boundary: it is the nominal low/high altitude count-scale ratio. Because MSC-69-FS-4 is for Luminary 1B, the high-scale 5.3950-ft/count figure is not promoted to an Apollo-11-effective fact without direct LM-5/Luminary 1A corroboration.

The Apollo 11 prelaunch erasable-load record separately lists `SKALSKAL = 00000`. The relationship between that recorded zero and run-time initialization remains unresolved.

## Primary sources

1. LUMINARY 099 `SERVICER.agc`, `ERASABLE_ASSIGNMENTS.agc`, `CONTROLLED_CONSTANTS.agc`, and assembly/operation information, MIT Instrumentation Laboratory Apollo 11 software listing.
2. MSC-69-FS-4, *Programmed Guidance Equations for Luminary 1B, Manned LM Earth Orbital and Lunar Program*, MIT Instrumentation Laboratory / MSC.
3. Apollo 11 LUMINARY 99 prelaunch erasable-load table LM5/4.5.1-1.

## Prohibited inference

Do not infer from this note alone:

- that LM-5 hardware definitely used 5.3950 ft/count on high scale;
- that `SKALSKAL = 00000` means a zero run-time multiplier;
- raw serial word framing, bias, rounding, or truncation;
- any stochastic measurement-error distribution;
- any MCC controller-visible scale indication or procedure.

## Evidence status

**PARTIAL / STRONGLY BOUNDED.** Nominal scale-ratio semantics are resolved; direct Apollo-11-effective high-scale hardware confirmation and zero-padload semantics remain open.
