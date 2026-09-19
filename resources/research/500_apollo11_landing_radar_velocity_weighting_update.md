# Research note 500 — Apollo 11 landing-radar velocity estimator chain

Date: 2026-09-19  
Research thread: `apollo11-landing-radar`

## Bounded question

How does flown LUMINARY 099 construct the guidance velocity estimate at the landing-radar velocity-measurement epoch, and what Apollo-11-effective weighting/correction is then applied after the residual passes its reasonableness test?

## Implementation dependency

This closes the source logic for the previously open PIPA/gravity propagation to landing-radar measurement time and the downstream weighting/correction stage. It does not by itself implement the complete composed estimator or establish any Mission Control display/update cadence.

## Findings

### Measurement-time snapshot and propagation

The flown LUMINARY 099 `LRVJOB` schedules `RDGIMS` 170 ms after initiating the five-sample velocity read. The listing states that `RDGIMS` is intended to run about midway through that read. `RDGIMS` saves `TIME2,TIME1` as `LRVTIME`, the three IMU CDU angles, and the instantaneous PIPA values as `PIPTEM`.

When `VELUPDAT` later processes the accepted velocity sample, it restores the saved CDUs, transforms the selected navigation-base velocity beam into stable-member coordinates, and converts the saved `PIPTEM` vector into a velocity increment. The interpretive sequence then explicitly forms:

`VU = V(N-1) + DELVU + G(N-1) * (TU - T(N-1))`

where the code comments identify `TU` with `LRVTIME`; it then subtracts the lunar-rotation velocity term (`DELVS`) before projecting the resulting estimate onto the measurement-time beam. The time interval is formed from `LRVTIME - PIPTIME`; the code uses the stored previous gravity term `GDT/2` with the corresponding scaling.

This is stronger than a generic assumption that the current guidance velocity can simply be compared with the radar sample. The flown program advances the prior guidance estimate to the radar measurement epoch using the intervening PIPA increment plus the stored gravity contribution, then applies the lunar-rotation correction before the scalar residual test.

This finding does not authorize a free-standing gravity model invented outside the AGC state-vector/servicer chain. A reusable implementation must accept or derive the prior guidance velocity, PIPA-derived increment, previous gravity term, epoch difference, and lunar-rotation correction from source-controlled upstream state.

### Downstream weighting/correction

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

The reusable historical chain can now preserve:

`prior guidance velocity + PIPA increment + stored gravity contribution to LR epoch - lunar-rotation correction -> measurement-time estimated velocity -> beam projection -> accepted residual -> speed/program-dependent weight -> vector velocity correction`

without embedding Apollo constants in generic code.

The next implementation task is composition: add a mission-neutral measurement-time propagation stage whose inputs remain explicit, then connect it to the already source-controlled beam transform and historical weighting/update model. Do not invent an independent lunar gravity field or PIPA error/noise model merely to make the chain executable.

## Remaining boundary

Still not closed by this note:

- executable composition of the source-controlled propagation and LM-5 antenna/CDU transform into one historical model path;
- landing-radar measurement noise/error generation;
- controller-visible guidance/radar product cadence and formatting.

## Sources

- MIT/IL LUMINARY 099 final-program listing, `SERVICER.agc`, `LRVJOB` / `RDGIMS` / `VELUPDAT` / `VUPDAT` / `GNUV` path: https://www.ibiblio.org/apollo/listings/Luminary099/SERVICER.agc.html
- MIT/IL LUMINARY 099 `ERASABLE_ASSIGNMENTS.agc`, definitions of `LRVMAX`, `LRVF`, `LRWV*`, and `LRWVFF`: https://www.ibiblio.org/apollo/listings/Luminary099/ERASABLE_ASSIGNMENTS.agc.html
- Grumman / NASA, `SNA-8-D-027(II) REV 1`, LM-5 Mission G prelaunch erasable load, Table LM5/4.5.1-1, 11 June 1969: https://ibiblio.org/apollo/Documents/Luminary99PadLoads.pdf
- YUL opcode guide, `BZMF` definition: Virtual AGC repository, `YUL/GUIDE_TO_OP_CODES_RECOGNIZED_BY_YUL_SYSTEM_FOR_BLK2_AND_AGC.argus`
- MIT/IL R-567 Section 5 Rev. 8, Luminary 1C state-vector update discussion, used only as later descriptive corroboration: https://www.ibiblio.org/apollo/NARA-SW/R-567-sec5-rev8-5.3.pdf

## Evidence status

- **DOCUMENTED:** `RDGIMS` captures the landing-radar velocity measurement epoch, IMU CDUs, and PIPA snapshot during the five-sample read.
- **DOCUMENTED:** flown `VELUPDAT` advances the prior guidance velocity to `LRVTIME` using the saved PIPA increment and previous gravity contribution, then subtracts the lunar-rotation velocity correction before beam projection/residual testing.
- **DOCUMENTED:** LUMINARY 099 uses `LRVF`, `LRVMAX`, component-specific `LRWV*` / `LRWVF*` values, and `LRWVFF` to select the velocity correction weight.
- **DOCUMENTED:** the flown code applies `LRWVFF` for P65/P66/P67 and adds the weighted residual along the selected measurement-time beam direction to the velocity estimate.
- **DOCUMENTED:** the LM-5 Mission G prelaunch load gives `LRVMAX = 2000 ft/s`, `LRVF = 200 ft/s`, `LRWVZ/Y/X = 0.3`, `LRWVFZ/Y/X = 0.2`, and `LRWVFF = 0.1`.
- **PARTIALLY DOCUMENTED:** complete end-to-end executable historical estimator composition; the constituent propagation, frame transform, qualification, and weighting logic are controlled, but are not yet integrated into one model path.
- **UNRESOLVED:** landing-radar measurement error/noise generation and controller-visible radar/guidance product cadence/formatting.
