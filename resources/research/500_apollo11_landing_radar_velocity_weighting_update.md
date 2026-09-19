# Research note 500 — Apollo 11 landing-radar velocity weighting and correction

Date: 2026-09-19  
Research thread: `apollo11-landing-radar`

## Bounded question

After a landing-radar velocity component has been reconstructed, projected into the measurement-time reference frame, and accepted by the reasonableness test, what Apollo-11-effective weighting and vector correction are applied to the LM guidance velocity estimate?

## Implementation dependency

This closes the downstream weighting/correction stage needed by the Apollo 11 landing-radar causal chain. It does not by itself close the upstream PIPA/gravity propagation to measurement time or any Mission Control display/update cadence.

## Findings

The flown LUMINARY 099 `SERVICER.agc` path directly implements the following velocity-update behavior.

After reasonableness testing, `VUPDAT` first respects the LR-update inhibit. If updating is allowed, it selects a velocity-component weight from estimated vehicle speed and the selected velocity component:

- when estimated speed is at or below `LRVF`, use the corresponding constant `LRWVFZ/Y/X`;
- when estimated speed is at or above `LRVMAX`, the normal speed-dependent weight is zero;
- between those thresholds, use `LRWVZ/Y/X * (1 - V/LRVMAX)`;
- when the program mode is P65, P66, or P67, the effective weight is replaced by `LRWVFF`.

The equality behavior follows the AGC `BZMF` instruction used at the threshold branches; the YUL opcode guide defines `BZMF` as branch on zero or minus.

The update itself is a one-component vector correction. The flown code multiplies the accepted measured-minus-estimated scalar velocity difference by the selected weight and the measurement-time selected velocity-beam vector, adds that correction to the current velocity estimate, stores the result as `GNUV`, and then stores the new guidance velocity.

The LM-5 Mission G LUMINARY 99 prelaunch erasable load supplies Apollo-11-effective values:

| Parameter | LM-5 value | Model interpretation |
| --- | ---: | --- |
| `LRVMAX` | 2000 ft/s | maximum normal velocity-update weighting threshold |
| `LRVF` | 200 ft/s | low-speed constant-weight threshold |
| `LRWVZ` | 0.3 | normal Z-component linear weight coefficient |
| `LRWVY` | 0.3 | normal Y-component linear weight coefficient |
| `LRWVX` | 0.3 | normal X-component linear weight coefficient |
| `LRWVFZ` | 0.2 | low-speed Z-component constant weight |
| `LRWVFY` | 0.2 | low-speed Y-component constant weight |
| `LRWVFX` | 0.2 | low-speed X-component constant weight |
| `LRWVFF` | 0.1 | P65/P66/P67 override weight in flown LUMINARY 099 |

A later R-567 Luminary 1C description independently explains the same speed-dependent / low-speed weighting concept and a final-descent override, but it describes the override as P66. Because that document is later than Apollo 11, it is retained only as descriptive corroboration; the Apollo-11-effective program-mode behavior comes from the flown LUMINARY 099 listing.

## Implementation consequence

The reusable implementation can now preserve:

`accepted scalar residual + measurement-time beam + speed/program-dependent weight -> vector velocity correction`

without embedding Apollo constants in generic code.

The Apollo 11 profile supplies the thresholds, per-axis weights, and P65/P66/P67 override.

## Remaining boundary

Still not closed by this note:

- integration of PIPA increments and lunar-gravity propagation into a complete historical estimate at the LR measurement time;
- executable reproduction of the already source-controlled LM-5 antenna / IMU attitude transform;
- landing-radar measurement noise/error generation;
- controller-visible guidance/radar product cadence and formatting.

Those remain separate dependencies.

## Sources

- MIT/IL LUMINARY 099 final-program listing, `SERVICER.agc`, `VELUPDAT` / `VUPDAT` / `GNUV` path: https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
- MIT/IL LUMINARY 099 `ERASABLE_ASSIGNMENTS.agc`, definitions of `LRVMAX`, `LRVF`, `LRWV*`, and `LRWVFF`: https://www.ibiblio.org/apollo/listings/Luminary099/ERASABLE_ASSIGNMENTS.agc.html
- Grumman / NASA, `SNA-8-D-027(II) REV 1`, LM-5 Mission G prelaunch erasable load, Table LM5/4.5.1-1, 11 June 1969: https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- YUL opcode guide, `BZMF` definition: Virtual AGC repository, `YUL/GUIDE_TO_OP_CODES_RECOGNIZED_BY_YUL_SYSTEM_FOR_BLK2_AND_AGC.argus`
- MIT/IL R-567 Section 5 Rev. 8, Luminary 1C state-vector update discussion, used only as later descriptive corroboration: https://www.ibiblio.org/apollo/NARA-SW/R-567-sec5-rev8-5.3.pdf

## Evidence status

- **DOCUMENTED:** LUMINARY 099 uses `LRVF`, `LRVMAX`, component-specific `LRWV*` / `LRWVF*` values, and `LRWVFF` to select the velocity correction weight.
- **DOCUMENTED:** the flown code applies `LRWVFF` for P65/P66/P67 and adds the weighted residual along the selected measurement-time beam direction to the velocity estimate.
- **DOCUMENTED:** the LM-5 Mission G prelaunch load gives `LRVMAX = 2000 ft/s`, `LRVF = 200 ft/s`, `LRWVZ/Y/X = 0.3`, `LRWVFZ/Y/X = 0.2`, and `LRWVFF = 0.1`.
- **DOCUMENTED:** `BZMF` is branch-on-zero-or-minus, supporting inclusive threshold behavior at the branch points used by `VUPDAT`.
- **PARTIALLY DOCUMENTED:** a complete end-to-end historical estimator cycle; the weighting/correction stage is controlled, but upstream PIPA/gravity propagation and executable measurement-frame transformation are not yet integrated into one model path.
- **UNRESOLVED:** controller-visible radar/guidance product cadence and formatting.
