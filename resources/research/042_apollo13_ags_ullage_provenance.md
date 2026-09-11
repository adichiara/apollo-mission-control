# Apollo 13 AGS ullage — measurement, counter, and state are separate

Date: 2026-09-11  
Status: **STRONG CONTINUITY / SYSTEM-SPECIFICATION SUPPORTED — ullage logic is documented; exact MSK 1123 AGS ULL field source remains unresolved.**

## Purpose

MSK 1123 includes an **AGS ULL** field described in the display-document family as:

> Abort Guidance ullage measurement

with velocity units.

Apollo AGS documentation also exposes:

- an ullage counter;
- an ullage-completion threshold;
- an engine-on condition.

These are not the same quantity.

This note separates them so the eventual simulator does not reduce ullage to one Boolean or one number.

---

# 1. Physical / sensed ullage measurement

The AGS system specification describes ullage detection in terms of sensed velocity increments along the LM X axis.

The specification requires ullage when:

- accumulated X-axis velocity increment exceeds approximately **0.2 ft/s in each 2-second computer cycle**;
- this occurs for **three consecutive cycles**.

Loss of ullage is detected when a cycle falls below the required X-axis increment.

This is equivalent to testing an average X-axis acceleration of approximately **0.1 ft/s²** over each 2-second cycle.

The LM Operations Handbook family describes the same logic in acceleration terms.

---

# 2. Programmed thrust-acceleration quantity: AT

Surviving FP6/FP8 source listings show the navigation logic computing:

```text
AT = 1/2 (VD1X - VDX)
```

in the program's internal scaling.

The source comments identify **AT** as thrust acceleration.

The computed AT value is compared against constant **4K35**, whose source comment identifies it as the:

> ULLAGE THRESHOLD

with value corresponding to **0.1** in the programmed acceleration scale.

This is consistent with the system specification's 0.2-ft/s-over-2-sec criterion.

### Important distinction

AT is a measurement/computed acceleration quantity used to decide whether the current cycle qualifies for ullage.

It is not the ullage counter itself.

---

# 3. Ullage counter: MU8

The AEA uses:

- **MU8** — ullage counter
- **1K9** — ullage-counter limit

The adjacent-program source identifies:

- MU8 at address 0614;
- 1K9 at 0616;
- 1K9 initialized to **3**.

When AT exceeds the ullage threshold, the program increments MU8.

When the threshold is not met, the counter is reset.

This implements the “three consecutive cycles” requirement.

---

# 4. Telemetry status: MU8S12

The telemetry block does not simply expose MU8 as a standalone display value.

It includes:

- **MU8S12** at telemetry-block address **0363**

The source code constructs MU8S12 from the ullage counter and S12 status for telemetry.

This is important because Mission Control can receive ullage progression/status information separately from any velocity-unit measurement used on the CRT.

---

# 5. DEDA counter access

The Apollo LM Operations Handbook DEDA output tables identify:

- **614** — ullage counter;
- **616** — ullage-counter value for completion.

These are count values.

The Apollo 13 G&N Dictionary independently confirms the same address family.

Thus the crew can inspect the counter logic directly through DEDA.

Again, this is different from MSK 1123's velocity-unit **AGS ULL** measurement.

---

# 6. MSK 1123 AGS ULL is not the counter

The display-document family defines:

- **AGS ULL** — Abort Guidance ullage measurement
- units: ft/s

The counter is dimensionless/count-based.

Therefore:

```text
MSK 1123 AGS ULL ≠ MU8 counter
```

and:

```text
MSK 1123 AGS ULL ≠ “ullage yes/no” Boolean
```

The display field must represent a velocity-related measurement or ground-scaled derivative of the AEA's sensed-ullage data.

Exactly which AEA variable/ground calculation feeds it is still under research.

---

# 7. Likely source family, but not yet certified

The AGS logic uses the difference between:

- current high-frequency velocity accumulation (VD1X);
- the prior/navigation-update accumulation (VDX);

to compute the thrust-acceleration quantity AT.

The system specification expresses the same test as velocity accumulated during the 2-second cycle.

Therefore the source family behind AGS ULL is strongly constrained to the X-axis sensed-velocity / thrust-acceleration chain.

However, without the MCC display-routing/calculation source, the project must not choose among:

- raw 2-second X-axis velocity increment;
- a scaled/reconstructed derivative from VD1X/VDX;
- another telemetry engineering value derived from AT.

---

# 8. State model required by the simulator

The eventual AGS subsystem should distinguish at least:

```text
sensed_x_delta_v
computed_thrust_acceleration
ullage_cycle_qualifies
ullage_counter
ullage_counter_limit
ullage_acquired
engine_on_permission/status
ground_display_ullage_measurement
```

These states can diverge during:

- sensor bias;
- telemetry failure;
- ground conversion error;
- interrupted qualifying cycles;
- incorrect counter state;
- display-processing problems.

A single variable such as `ags.ullage = true/false` is not sufficient for Apollo fidelity.

---

# 9. Timing

The documented chain includes:

- sensed velocity accumulation at high frequency;
- evaluation on the 2-second AGS navigation/computation cycle;
- counter progression across consecutive 2-second cycles;
- 1-Hz AEA telemetry blocks;
- unresolved MCC CRT refresh cadence.

This means controllers may observe progression through the ullage logic rather than only a final state.

---

# 10. Evidence status

## DOCUMENTED / STRONG CONTINUITY

- AGS ullage criterion is based on X-axis sensed velocity/acceleration.
- approximately 0.2 ft/s per 2-sec cycle / 0.1 ft/s² is the relevant criterion in system/program documentation.
- three consecutive qualifying cycles are required.
- AT is the programmed thrust-acceleration quantity compared to the ullage threshold.
- MU8 is the ullage counter.
- 1K9 is the counter limit and is 3 in adjacent programs.
- MU8/S12 information is packaged for telemetry.
- DEDA 614/616 exposes counter/count-limit information.
- MSK 1123 AGS ULL is a velocity-unit measurement and therefore cannot simply be MU8.

## NOT YET ESTABLISHED

- exact Flight Program 7 internal instruction sequence for ullage logic;
- exact AEA variable used for the MSK 1123 AGS ULL engineering field;
- exact ground scaling/conversion;
- exact CRT update behavior.

---

# 11. Sources

- Grumman Abort Guidance Section specification — ullage detection requirement.
- FP6 programmed equations — AT, MU8, velocity accumulation, counter behavior.
- FP6/FP8 source listings — ullage threshold/counter logic and MU8S12 telemetry packing.
- Apollo LM Operations Handbook — DEDA 614/616 and AGS ullage operational description.
- Apollo 13 G&N Dictionary — mission-specific counter-address continuity.
- AC Electronics Guidance & Navigation Summary family — MSK 1123 AGS ULL field definition.

---

# 12. Next work

1. Search MCC/RTCC display calculation sources for the velocity-unit AGS ULL field.
2. Determine whether the display uses a 2-second X-axis delta-V or a ground reconstruction of AT.
3. Recover the FP7 Table 2.1-7 row corresponding to MU8S12 and any ullage-related engineering output.
4. Map ullage measurement, counter progression, and acquired state separately in the future parameter dictionary.
