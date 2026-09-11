# Apollo 13 Flight Program 7 — AEA telemetry-list continuity bounds

Date: 2026-09-11  
Status: **STRONG CONTINUITY / PARTIAL MISSION-SPECIFIC RECONSTRUCTION — exact FP7 list is still not directly extracted.**

## Purpose

Research note 037 established the AGS telemetry architecture and identified the missing Apollo 13 link:

> the exact Flight Program 7 AEA telemetry word list.

The complete February 1970 LM-7 Table 2.1-7 has not yet been extracted. However, the surviving Flight Program 6 and Flight Program 8 assembly listings, combined with the mission-specific Apollo 13 G&N Dictionary, strongly constrain the FP7 telemetry region.

This note records those constraints without silently reconstructing missing FP7 code.

---

# 1. FP6 and FP8 use the same telemetry memory region

The transcribed original assembly listings for:

- **Flight Program 6** — Apollo 11/12 era;
- **Flight Program 8** — Apollo 15–17 era;

both explicitly mark:

```text
START OF TELEMETRY LIST
...
END OF TELEMETRY LIST
```

around the same contiguous AEA memory range:

**0325 through 0406 octal**

That range contains exactly 50 words.

Therefore the software architecture on both sides of FP7 uses a 50-word telemetry block occupying the same AEA memory addresses.

### What this establishes

It is strong evidence that FP7 retained the same basic telemetry-buffer architecture and address range.

### What this does not establish

It does **not** prove that every FP7 address had the same variable meaning as FP6 or FP8.

Software can preserve the block location while changing the contents or semantics of individual words.

---

# 2. Side-by-side FP6 / FP8 block structure

The two surviving source listings show a remarkably stable block.

Common address families include:

| Octal address | FP6 / FP8 role family |
|---|---|
| 0325 | readout-mode flag |
| 0326 | DEDA data |
| 0327 | clear-mode flag |
| 0330–0332 | telemetry direction-cosine row |
| 0333 | DEDA address |
| 0334–0336 | telemetry direction-cosine row |
| 0337 | altitude |
| 0340–0342 | LM position |
| 0343 | LM pericynthion / telemetry alias |
| 0344–0346 | CSM position |
| 0347 | predicted/burnout altitude |
| 0350–0352 | body delta-V |
| 0353 | absolute-time low/significant component |
| 0354–0356 | delta-alpha / body rotation increments |
| 0357 | time to burnout |
| 0360–0362 | LM velocity |
| 0363 | telemetry working/status quantity |
| 0364–0366 | CSM velocity |
| 0367 | altitude rate |
| 0370 | velocity to gain |
| 0371 | transfer / maneuver velocity quantity — semantics differ between FP6 and FP8 |
| 0372 | maneuver-relative time |
| 0373 | TIG |
| 0374–0376 | commanded body-pointing direction |
| 0377 | absolute-time major component |
| 0400 | AGS function selector |
| 0401 | discrete word |
| 0402 | guidance/orbit display quantity |
| 0403 | telemetry/display orbit quantity |
| 0404–0406 | 40-ms velocity accumulations |

The block's overall structure is nearly identical in FP6 and FP8.

---

# 3. A real change inside the stable block: address 0371

The surviving source listings are not completely identical.

## FP6

Address **0371** is labeled `VT`, with comments describing total velocity required for transfer / velocity-to-be-gained at CDH depending on use.

## FP8

Address **0371** is labeled `VF`, described as transfer braking velocity.

## Apollo 13 mission-specific dictionary

The Apollo 13 G&N Dictionary gives address **371** as:

- ΔV for CDH in CSI/coast;
- ΔV direct-transfer + braking in TPI;

with 0.1 ft/s display scaling.

This is mission-specific FP7 evidence and shows why copying either adjacent flight program's mnemonic/comments wholesale would be unsafe.

### Consequence

The correct reconstruction method is:

```text
stable telemetry address
      +
mission-specific FP7 variable meaning
      +
mission-era engineering scaling
      =
Apollo 13 telemetry definition
```

—not “FP7 probably equals FP6” or “FP7 probably equals FP8.”

---

# 4. Apollo 13 directly verifies many addresses inside the telemetry region

NASA-indexed text from the Apollo 13 G&N Dictionary directly defines numerous addresses that fall inside 0325–0406.

Examples:

- **337** — LM altitude;
- **340–342** — LM position components;
- **344–346** — CSM position components;
- **347** — predicted altitude at TIG / burnout, depending on mode;
- **357** — time to burnout;
- **360–362** — LM velocity components;
- **364–366** — CSM velocity components;
- **367** — LM altitude rate;
- **371** — maneuver delta-V family;
- **377** — AGS computer time;
- **400** — AGS function selector;
- **404 / 405 / 406** — delta-V accumulator/reset words, with 470/471/472 as readouts.

This is significant because the mission-specific dictionary independently overlaps the telemetry-memory region documented in the FP6/FP8 source code.

---

# 5. Operational Apollo 13 validation

The Apollo 13 G&N Dictionary's manual-thrust procedure explicitly uses:

- 400 +0 — attitude hold;
- 404 +0;
- 405 +0;
- 406 +0;
- 470R / 471R / 472R to monitor and trim delta-V by axis.

The actual Apollo 13 mission record also uses the same 404/405/406 → 470 monitoring sequence during contingency burns.

Therefore these variables are not merely static dictionary entries: they were operationally used during the mission.

---

# 6. What can now be considered high confidence

## High-confidence architecture

- AEA sends a 50-word telemetry block.
- FP6 and FP8 place that block at octal 0325–0406.
- Apollo 13's LM-7 handbook contains a Table 2.1-7 AEA telemetry word list.
- Apollo 13's G&N Dictionary defines many FP7 addresses inside that same range.
- Selected in-range variables were actually used in Apollo 13 procedures.

## High-confidence Apollo 13 variable meanings

For addresses directly exposed by the mission-specific dictionary, use the Apollo 13 definition rather than adjacent-program comments.

Examples include 337, 340–347, 357, 360–367, 371, 377, 400, 404–406.

## Still unresolved

The project should **not yet freeze**:

- the exact contents of all 50 FP7 telemetry words;
- ID-code-to-address mapping, although sequential block structure strongly suggests a straightforward relationship in adjacent programs;
- fields in the 0325–0406 region not defined by the G&N Dictionary;
- scaling for every telemetry word;
- the exact ground decoder / RTCC mapping to MSK 1123.

---

# 7. Implication for reconstruction strategy

The missing FP7 telemetry list can now be approached as a constrained comparison rather than a blank-source problem.

Recommended method:

1. use the 50 fixed telemetry addresses 0325–0406 as a **candidate framework**, not a frozen FP7 fact;
2. fill only addresses directly supported by Apollo 13 sources;
3. compare FP6 and FP8 at unresolved addresses;
4. classify unchanged-before-and-after entries as **strong continuity candidates**;
5. leave any differing/ambiguous entry unresolved until a mission-specific source is found;
6. map only verified FP7 variables onward to MSK 1123.

This retains provenance at every step.

---

# 8. Important caution about telemetry IDs

General AEA documentation states that each transmitted telemetry word carries a 6-bit ID representing its sequential position in the 50-word list.

Because the FP6/FP8 blocks are contiguous, it may be tempting to derive every ID arithmetically from the memory address.

Do **not** freeze that mapping for Apollo 13 until Table 2.1-7 or an equivalent FP7 telemetry-format source is directly inspected.

Architecture continuity is not the same as mission-specific certification.

---

# 9. Sources

## Primary / source-code transcriptions

- Flight Program 6 assembly listing, original Apollo AGS source transcribed from surviving assembly listing:
  https://www.ibiblio.org/apollo/listings/FP6/FP6.aea.html
- Flight Program 8 assembly listing:
  https://www.ibiblio.org/apollo/listings/FP8/FP8.aea.html

The telemetry ranges in both listings were directly compared in this research pass.

## Mission-specific Apollo 13

- *Apollo 13 G&N Dictionary*, 1970 — NASA indexed text.
- *Apollo Operations Handbook, Lunar Module LM 7 and Subsequent*, 1 February 1970 — Table 2.1-7 identified but full table not yet extracted.
- Apollo 13 Flight Journal / mission voice records — operational use of AGS delta-V monitoring.

---

# 10. Next work

1. Search archival copies/OCR for the exact LM-7 Table 2.1-7.
2. Build an explicit FP6-vs-FP8 diff for all 50 telemetry addresses.
3. Query Apollo 13 dictionary/indexed material for every address where FP6/FP8 differ.
4. Produce an FP7 reconstruction matrix with evidence status per word:
   - mission-specific verified;
   - same in FP6 and FP8 / continuity candidate;
   - conflicting;
   - unknown.
5. Only then begin mapping AEA telemetry IDs to MSK 1123 AGS fields.
