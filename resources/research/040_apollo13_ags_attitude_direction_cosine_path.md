# Apollo 13 AGS attitude telemetry — direction-cosine path to ground body angles

Date: 2026-09-11  
Status: **STRONG CONTINUITY / MISSION-OPERATION VALIDATED — telemetry representation is documented; exact Apollo 13 RTCC angle-conversion algorithm remains unresolved.**

## Purpose

Apollo 13's Mission Operations Report records an important post-MCC-5 anomaly:

> RTCC was incorrectly processing AGS body angles.

The question for the simulator is therefore:

**What did the AGS actually transmit, and what did the ground have to compute before controllers saw “body angles”?**

The surviving AGS source listings and telemetry documentation answer the first half clearly.

---

# 1. AGS telemetry does not transmit ready-made body Euler angles

General AGS telemetry documentation for Flight Program 6 states that, at the end of each one-second telemetry block, the software stores the **current values of six direction cosines** for later telemetry output.

The transmitted six quantities are:

- A11T
- A12T
- A13T
- A31T
- A32T
- A33T

The FP6 and FP8 source listings identify them explicitly as:

> TM DIR COSINES

and place them at telemetry-block addresses:

- 0330–0332 — A11T/A12T/A13T
- 0334–0336 — A31T/A32T/A33T

Both adjacent programs use the same arrangement.

---

# 2. What those six values represent

The AGS source code identifies the underlying internal quantities as:

- A11/A12/A13 — **X-body direction cosines**
- A31/A32/A33 — **Z-body direction cosines**

The telemetry-initialize routine copies the current A11–A13 and A31–A33 values into A11T–A13T and A31T–A33T.

The FP6 listing shows this directly:

```text
A11,1  → A11T,1
A31,1  → A31T,1
```

within indexed loops that copy three elements from each body-axis row.

Thus the telemetry representation is an orientation matrix subset, not a roll/pitch/yaw tuple.

---

# 3. Why only six direction cosines are sufficient

A valid attitude direction-cosine matrix is orthonormal.

If the X-body and Z-body axes are known, the Y-body axis is mathematically constrained by the orthogonality/right-handed-frame relationship.

Therefore six direction cosines are sufficient to reconstruct the full body orientation, subject to:

- quantization;
- telemetry error;
- numerical normalization/orthogonality handling;
- correct coordinate-frame interpretation.

The exact Apollo RTCC implementation used for that reconstruction is still under research.

Do not code a specific cross-product/order/sign convention until the contemporary ground algorithm is located.

---

# 4. Apollo 13 controller display wants body angles, not raw direction cosines

The ASPO 45 MSK 1123 display definition contains an **AGS ATT** family described in the earlier directly searchable display manual family as **Abort Guidance System body angles**.

The mission-specific Apollo 13 MSK 1123 retains the AGS attitude section, but field-level cross-mission equality must still be checked before freezing every label/mask.

The important source-layer distinction is already clear:

```text
AEA attitude state
     ↓
six telemetered direction cosines
     ↓
ground decoding
     ↓
coordinate / angle conversion
     ↓
controller-facing AGS body-angle product
```

That conversion layer is exactly where a ground-side processing error can occur.

---

# 5. Apollo 13 post-MCC-5 anomaly fits this architecture

After MCC-5:

- crew used AGS to establish passive thermal control;
- rates were nulled;
- yaw pulses were applied;
- crew switched to low-bit-rate telemetry;
- Mission Control's last high-bit-rate attitude indication did not match the expected attitude;
- high bit rate was restored;
- the Mission Operations Report says the **RTCC was incorrectly processing AGS body angles**;
- the ground discarded the bad readout;
- FDAI reference showed PTC was actually correct.

The wording is significant.

It does not say:
- AGS attitude was wrong;
- AEA telemetry was bad;
- the crew maneuver was wrong.

It identifies the problem specifically as **RTCC processing**.

Given the documented six-direction-cosine telemetry representation, the historically supported architecture is:

```text
correct physical attitude
      ↓
AEA orientation state
      ↓
six direction cosines in telemetry
      ↓
RTCC processing  ← documented Apollo 13 failure point
      ↓
incorrect ground body-angle display/product
```

The exact failed equation/configuration remains unknown.

---

# 6. Simulation requirement

The AGS attitude path should eventually be represented with independent state for:

1. **true spacecraft orientation**
2. **AEA internal orientation representation**
3. **telemetered direction cosines**
4. **ground-decoded direction cosines**
5. **ground-derived body angles**
6. **controller-visible CRT field**

This allows historically real discrepancies such as:

- true attitude correct, telemetry valid, RTCC transform wrong;
- one direction-cosine word stale/corrupt;
- wrong reference frame selected on ground;
- body-angle product invalid while raw telemetry remains usable.

A direct alias such as:

```text
MSK1123.ags_att = spacecraft.euler_angles
```

would erase the actual Apollo architecture.

---

# 7. Timing consequence

FP6 telemetry documentation says:

- the 50-word block repeats once per second;
- one word normally outputs every 20 ms;
- AGS major computation cycle is 2 seconds;
- six direction cosines are snapshotted at the one-second telemetry-block boundary.

That creates a coherent attitude snapshot for the transmitted orientation subset.

Again:

**1-Hz telemetry snapshot ≠ proven 1-Hz MSK 1123 CRT refresh.**

The display cadence remains unresolved.

---

# 8. Evidence status

## DOCUMENTED / STRONG CONTINUITY

- FP6 and FP8 both reserve telemetry addresses 0330–0332 and 0334–0336 for A11T–A13T and A31T–A33T.
- Both identify them as telemetry direction cosines.
- The source code copies internal X-body and Z-body direction cosines into those telemetry words.
- AGS telemetry documentation says six direction cosines are snapshotted for output once per second.
- Apollo 13's telemetry block is strongly bounded to the same 0325–0406 architecture by adjacent-program continuity and the LM-7 handbook's known telemetry-table structure.

## MISSION-SPECIFIC OPERATIONAL FACT

- Apollo 13 encountered an RTCC error processing AGS body angles after MCC-5.

## NOT YET ESTABLISHED

- exact FP7 Table 2.1-7 confirmation of all six direction-cosine word IDs;
- exact RTCC equation / reference frame used to convert them to body angles;
- exact MSK 1123 angle mask/precision for Apollo 13;
- whether the MCC displayed any raw direction-cosine diagnostic product alongside derived angles.

---

# 9. Sources

### AGS telemetry architecture / equations

- Flight Program 6 programmed equations, telemetry section — 50-word block, six direction cosines snapshotted each second.
- FP6 source listing — A11/A31 internal direction cosines and telemetry-copy routine.
- FP8 source listing — same telemetry structure and copy routine, strengthening continuity.

### Apollo 13 mission-specific

- *Mission Operations Report — Apollo 13*, LM Control Officer report — documented RTCC body-angle processing error after MCC-5.
- Apollo 13 AC Electronics Guidance & Navigation Summary — MSK 1123 mission-specific layout/definition family.
- Apollo Operations Handbook, LM-7 and Subsequent — exact Table 2.1-7 remains the outstanding telemetry-list authority.

---

# 10. Next work

1. Find the RTCC/AGS body-angle conversion documentation or flight-dynamics/guidance equations used by MCC.
2. Recover LM-7 Table 2.1-7 to certify A11T–A33T positions/IDs for FP7.
3. Determine the reference frame represented by the telemetered A matrix during the relevant Apollo 13 modes.
4. Map the resulting ground-computed angles to the exact MSK 1123 AGS ATT fields.
5. Use the MCC-5 anomaly as a future validation case: inject a ground-transform fault without altering spacecraft attitude or raw AGS telemetry.
