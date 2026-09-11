# Apollo 13 AGS delta-V interfaces — telemetry accumulation versus DEDA readout

Date: 2026-09-11  
Status: **STRONG CONTINUITY / APOLLO-13 PROCEDURE VALIDATED — internal variable relationships are documented in adjacent AGS programs and Apollo 13 DEDA use is mission-specific; exact MSK 1123 field mapping remains unresolved.**

## Purpose

MSK 1123 contains an **AGS DEL VEL** family.

Apollo 13 contingency procedures also use DEDA addresses **470/471/472** to monitor measured delta velocity.

It would be easy—but incorrect—to assume that the ground CRT simply mirrors the DEDA 470–472 values.

The surviving AGS program documentation shows two distinct delta-V representations.

---

# 1. Telemetry variables: VD1X / VD1Y / VD1Z

In the FP6 and FP8 telemetry blocks:

- 0404 — VD1X
- 0405 — VD1Y
- 0406 — VD1Z

The source listings label these:

> 40MS VEL ACCUMULATION

The FP6 programmed-equations document defines them as components along the **LM body X/Y/Z axes** of accumulated sensed velocity increments, updated every **40 ms**.

They are included directly in the 50-word AEA telemetry block.

Therefore Mission Control receives a delta-velocity-related AEA quantity independently of the crew's current DEDA selection.

---

# 2. DEDA variables: VDX / VDY / VDZ

Separate AEA memory locations are:

- 0470 — VDX
- 0471 — VDY
- 0472 — VDZ

The FP6 programmed-equations document describes these as body-axis accumulated sensed velocity increments that are updated at the **2-second navigation-update** interval.

The Apollo 13 G&N Dictionary directly identifies these addresses as crew readouts:

- 470 — measured ΔVX, +up, 0.1 ft/s
- 471 — measured ΔVY, +right, 0.1 ft/s
- 472 — measured ΔVZ, +forward, 0.1 ft/s

and links zeroing to 404/405/406.

### Important interface distinction

```text
VD1X/Y/Z
  = telemetry-region 40-ms accumulators

VDX/Y/Z
  = navigation-update / DEDA readout values
```

They are related, but they are not the same memory locations or update process.

---

# 3. Source-code relationship between the two representations

The surviving FP6/FP8 source shows the navigation-update logic copying the telemetry accumulation into the DEDA/navigation quantity:

```text
VD1X → VDX
VD1Y → VDY
VD1Z → VDZ
```

at the appropriate navigation-update point.

The code also compares the current VD1 accumulation against the stored VDX value when computing thrust acceleration.

This establishes a real internal pipeline:

```text
accelerometer / sensed velocity increments
        ↓
VD1X/Y/Z  (updated at high frequency)
        ↓
AEA telemetry block
        |
        +----> ground
        |
        ↓
navigation update
        ↓
VDX/Y/Z  (2-sec update)
        ↓
DEDA 470/471/472
        ↓
crew
```

The exact Flight Program 7 code is missing, so this is **strong adjacent-program continuity**, not a claim that every FP7 instruction is identical.

Apollo 13 mission-specific DEDA semantics independently confirm the VDX/Y/Z side of the architecture.

---

# 4. Apollo 13 operational validation

Before the final course-correction burn, Mission Control instructed the crew to:

- zero 404/405/406;
- select address 470;
- inspect the pre-burn delta-V bias.

Haise reported approximately -0.2 ft/s bias at 470.

That confirms that the crew-side DEDA interface was operationally used as an independent burn monitor.

It does **not** imply that the ground CRT depended on the crew leaving 470 selected.

---

# 5. Consequence for MSK 1123 AGS DEL VEL

The Apollo display definition family describes **AGS DEL VEL** as an Abort Guidance System measured-velocity quantity.

There are now at least three possible layers that must be distinguished:

1. AEA high-frequency body-axis accumulation — VD1X/Y/Z;
2. AEA 2-second navigation/DEDA values — VDX/Y/Z;
3. controller-facing engineering values on MSK 1123.

The exact field source is not yet certified.

### What should not be implemented

Do not use:

```text
MSK1123.ags_delta_v = DEDA.current_display
```

because the ground had its own AEA telemetry stream.

Do not automatically use:

```text
MSK1123.ags_delta_v = VD1
```

either, until the MCC conversion/routing documentation is found.

---

# 6. Scaling / frame caution

Adjacent-program technical documentation describes VD1 and VDX as **body-axis** components.

The Apollo 13 G&N Dictionary presents the DEDA 470–472 readout with operational axis labels:

- +up
- +right
- +forward

after the relevant body-axis alignment.

These labels reflect the operational attitude/alignment context.

Do not generalize them into a universal inertial or local-vertical frame definition for all mission phases.

---

# 7. Timing model consequence

There are now several independently documented cadences:

- sensed-velocity accumulation: 40 ms;
- navigation/VDX update: 2 sec;
- AEA telemetry block: 1 sec;
- DEDA presentation: interface-specific;
- MCC CRT refresh: unresolved.

The simulator should preserve these as separate timing concepts.

A failure or stale-data condition can therefore affect one layer without forcing all layers to change simultaneously.

---

# 8. Evidence status

## DOCUMENTED / STRONG CONTINUITY

- FP6 and FP8 telemetry blocks contain VD1X/Y/Z at 0404–0406.
- Programmed equations define VD1 as body-axis accumulated sensed velocity updated every 40 ms.
- VDX/Y/Z at 0470–0472 are separate navigation-update values.
- Source code copies VD1 into VDX at the navigation update.
- Apollo 13 mission-specific G&N Dictionary defines 470–472 and 404–406 operationally.

## APOLLO 13 OPERATIONAL FACT

- Apollo 13 used 404/405/406 zeroing and 470 monitoring for contingency burns.

## NOT YET ESTABLISHED

- exact FP7 instruction sequence relating VD1 and VDX;
- which representation feeds the MSK 1123 AGS DEL VEL field;
- engineering conversion/precision on the CRT;
- whether RTCC applies frame transformations before display.

---

# 9. Sources

- FP6 programmed equations — definitions of VD1X/Y/Z and VDX/Y/Z.
- FP6 and FP8 source listings — memory locations and navigation-copy logic.
- Apollo 13 G&N Dictionary — mission-specific DEDA 404–406 / 470–472 semantics.
- Apollo 13 Flight Journal / voice record — actual burn-monitor procedure.
- Apollo 13 AC Electronics Guidance & Navigation Summary — MSK 1123 display family.

---

# 10. Next work

1. Search MCC/RTCC material for the source of MSK 1123 **AGS DEL VEL**.
2. Determine whether ground converts VD1 or VDX into the displayed engineering quantity.
3. Investigate **AGS ULL** similarly; the DEDA ullage counter (614/616) is not itself the velocity-unit display field.
4. Build a field-by-field AGS portion of MSK 1123 with provenance confidence rather than a one-source display model.
