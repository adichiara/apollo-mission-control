# 405 — Apollo 11 landing-radar beam transform

Date: 2026-09-19

## Question

What Apollo-11-effective transformation produced the landing-radar beam vectors used by the LUMINARY 99 velocity-reference/reasonableness path, and which mission-specific geometry inputs are controlled well enough to implement rather than synthesize?

## Primary evidence

### LUMINARY 099 final-program listing

The Apollo 11 `SERVICER` listing directly implements the antenna-to-navigation-base beam setup in `SETPOS`.

- `SETPOS1` selects the position-1 pair `LRALPHA1`, `LRBETA1`; `SETPOS2` selects the position-2 pair `LRALPHA2`, `LRBETA2`.
- The selected pair is placed into the transformation-angle workspace as rotations about X and Y, with the Z rotation set to zero.
- `TRG*SMNB` / `*SMNB*` then transforms antenna-frame basis vectors into navigation-base coordinates.
- The resulting velocity-beam basis is stored as `VYBEAMNB`, `VXBEAMNB`, and `VZBEAMNB = VXBEAMNB × VYBEAMNB`.
- The fixed antenna-frame altitude/range vector `HBEAMANT` is transformed through the same path into `HBEAMNB`.
- The high-gate job explicitly recomputes these beam vectors after the landing-radar antenna reaches position 2.

Source: MIT Instrumentation Laboratory, LUMINARY 099 assembly listing, `SERVICER.agc`, pp. 895–897, Apollo 11 final program transcription from the MIT Museum hardcopy.

### LUMINARY Memo #95 — Landing Radar Orientation

Memo #95, dated 9 July 1969, resolves the sign/order ambiguity that would otherwise make a numerical implementation unsafe. It states that the R-567 alpha/beta angles describe the navigation-base-to-antenna transformation, while the LGC `LRALPHA` / `LRBETA` values are their negatives because `SETPOS` uses them for the antenna-to-navigation-base transformation. The memo also states the LGC order as beta then alpha.

Source: MIT Instrumentation Laboratory, LUMINARY Memo #95, *Landing Radar Orientation*, 9 July 1969.

### Apollo 11 LM-5 prelaunch erasable load

`SNA-8-D-027(II) REV 1`, the LM-5 Mission G LUMINARY 99 prelaunch erasable-load document, supplies the actual mission values:

| Quantity | LGC value | Documented angle |
| --- | ---: | ---: |
| `LRALPHA1` | 0.0163371759 rev | 5°52.883′ |
| `LRBETA1` | 0.0665287037 rev | 23°57.02′ |
| `LRALPHA2` | 0.0161680555 rev | 5°49.23′ |
| `LRBETA2` | 0.0001361111 rev | 0°2.94′ |

The load identifies position 1 as the stow position and position 2 as the hover position.

Source: `SNA-8-D-027(II) REV 1`, Volume II LM Data Book, table LM5/4.5.1-1, G prelaunch erasable load (LUMINARY 99), NASA data source.

### Fixed altitude/range beam vector

The LUMINARY 99 controlled constants define `HBEAMANT`, explicitly described as the range beam in landing-radar antenna coordinates, as the three-component vector beginning `(-0.4687018041, 0, -0.1741224271)` in the program's documented scaling representation. This is fixed program data rather than a guessed LM-5 mounting angle.

Source: MIT Instrumentation Laboratory, LUMINARY 099 `CONTROLLED_CONSTANTS.agc`, `HBEAMANT` at bank 33.

### Programmed-equation cross-check

MSC `69-FS-4` independently describes the same `SETPOS1` / `SETPOS2` / `SETPOS` sequence: select the appropriate alpha/beta pair, construct the antenna-to-navigation-base transform, form X/Y/Z velocity-beam vectors, and transform `HBEAMANT` into `HBEAMNB`. `69-FS-4` is later LUMINARY 1B material and is used here only as a structural cross-check; Apollo 11 effectivity comes from the LUMINARY 099 listing and LM-5 load above.

## Result

The previously open "exact LM-5 antenna-position + vehicle/platform attitude transform that produces the selected beam vector" can be narrowed substantially.

The **antenna-position portion is now documented for Apollo 11**: LUMINARY 099 defines the transformation algorithm; Memo #95 controls polarity/order; and the LM-5 load supplies the position-1 and position-2 alpha/beta values. `HBEAMANT` is also a controlled program constant.

The implementation must not replace this with an arbitrary normalized beam vector or a hand-entered mounting approximation.

A separate dynamic step remains: the velocity-measurement path reads IMU CDUs near the midpoint of the five-sample landing-radar velocity read and uses those attitude data when converting the navigation-base beam into the reference frame used by the velocity comparison. That time-tagged attitude/frame path should be recovered/implemented as its own bounded dependency rather than folded into the static antenna geometry.

## Implementation consequence

The landing-radar model may now admit a source-backed **static antenna-position transform stage** parameterized by the four LM-5 pad-loaded angles and the fixed LUMINARY 099 antenna-frame beam definitions. The current generic caller-supplied beam-vector interface remains useful as a lower-level proof, but a historical Apollo 11 profile should derive its navigation-base beam from these controlled inputs.

Do not yet claim a complete historical measurement geometry pipeline until the dynamic IMU-CDU/navigation-base-to-reference-frame step is implemented and validated.

No controller-display cadence or station-visible product timing is established by this note.

## Next bounded item

Trace the LUMINARY 099 velocity-measurement attitude path from `RDGIMS` (`LRXCDU`, `LRYCDU`, `LRZCDU`) through the navigation-base/reference-frame transformation used in `VELUPDAT`, preserving the measurement midpoint/time-tag semantics. Then determine whether that path supplies enough controlled information to close the remaining beam/reference computation gate without importing later-program equations.

## Evidence status

- **DOCUMENTED:** LUMINARY 099 `SETPOS` transforms antenna-frame beam definitions into navigation-base beam vectors using the selected landing-radar position angles.
- **DOCUMENTED:** Apollo 11 LM-5 prelaunch values for `LRALPHA1`, `LRBETA1`, `LRALPHA2`, and `LRBETA2`.
- **DOCUMENTED:** Memo #95 polarity/order clarification for LGC landing-radar orientation angles.
- **DOCUMENTED:** LUMINARY 099 fixed `HBEAMANT` range-beam constant and high-gate recomputation on transition to position 2.
- **PARTIALLY DOCUMENTED:** complete time-tagged navigation-base-to-reference-frame velocity-beam transformation; `RDGIMS` attitude capture is directly visible, but the full downstream transform is not closed in this note.
- **UNRESOLVED:** controller-visible landing-radar/guidance product cadence and formatting; downstream estimator/filter implementation remains a separate dependency.