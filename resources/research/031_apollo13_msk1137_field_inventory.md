# Apollo 13 MSK 1137 — normalized field inventory

Status: research transcription, not a frozen renderer specification.
Date: 2026-09-11.

Source: [Apollo 13 Guidance & Navigation Summary](https://apollojournals.org/afj/ap13fj/pdf-hr/a13-ac-elect-g-n-summary.pdf), layout PDF 188 / ASPO-10; definitions PDF 189–190 / ASPO-11–12. All PDF page numbers are one-based.

This inventory covers the named definition groups on both definition pages. Descriptions are paraphrased; grouped axes/registers remain grouped. It does not supply exact field coordinates, every character mask, transport source, or update timing. Those require a subsequent field-by-field implementation pass. Asterisk-prefixed source entries refer to the LM software section for further definition.

## ASPO-11 / PDF 189

| Field or contextual group | Meaning / units or states |
|---|---|
| GET | Ground elapsed time; hours:minutes:seconds |
| LGC (header clock) | LM computer time; hours:minutes:seconds |
| GMT | Greenwich mean time; hours:minutes:seconds |
| SITE | Receiving station identifier |
| D/L | Downlist identifier |
| SELECT | Throttle switch state; AUTO/blank |
| DECA | Descent throttle command; percent |
| MAN THR | Manual throttle command; percent |
| AUTO THR | Automatic throttle command; percent |
| CMD THR | Sum of manual and automatic throttle commands; percent |
| VAR ACT | Variable actuator position; percent |
| GUID CMD | LGC thrust command; percent |
| TCP | Chamber pressure presented as percent |
| LGC error/rate selection | Attitude following error in degrees, or LGC-computed body rates; exact selector text/mask requires further review |
| AGS ERR | AGS positional error; degrees |
| OMEGA-D | Desired automatic-maneuver body rates; degrees/second |
| OFFSET | Engine-related computed angular acceleration about Y and Z body axes; degrees/second squared |
| GMBL DR | Engine-bell motion direction; roll/pitch signs |
| A/H | Attitude-hold state; code/blank |
| AUTO | Automatic-stabilization state; code/blank |
| +TORQ-U/V/P | Accumulated positive commanded control-axis torque indication; source displays seconds |
| -TORQ-U/V/P | Accumulated negative commanded control-axis torque indication; source displays seconds |
| WT | LM mass; pounds |
| RTCC | Ground-computed LM or combined LM+CSM mass; pounds |
| CSM | CSM mass; pounds |
| PIP-S | PIPA counts; decimal |
| RATE | Desired automatic-maneuver rate; degrees/second |
| RHC | Hand-controller scaling; NORM/FINE |
| X-TRANS | RCS system selection and number of X-translation jets; A/B and 2/4 |
| DAP (flagword) | DAPBOOLS; octal |
| CH 11–14 | LGC output channels; octal |
| CH 30–33 | LGC input channels; octal |
| RAD | RADMODES flagword; octal |
| LOCAL | Attitude relative to local horizontal; degrees |
| BIAS (attitude section) | Ground-computed PIPA free-fall bias, expressed as change in counts per change in time; cm/second squared |
| OCTAL | Computed octal loads for LGC PIPA-bias registers |
| RSVR-S | Resolver angles; degrees |
| RSVR-F | Resolver angles expressed in FDAI coordinates; degrees |
| ACT-F | LM attitude expressed in FDAI coordinates; degrees |
| IDES-F | Intermediate desired CDU angles in FDAI coordinates; degrees |
| FDES-F | Final desired CDU angles in FDAI coordinates; degrees |
| AGS-F | AGS Euler angles in FDAI coordinates; degrees |
| ΔERR-S | Difference between PGNS and AGS Euler angles; degrees |

## ASPO-12 / PDF 190

| Field or contextual group | Meaning / units or states |
|---|---|
| PGNS-B | DAP-computed body rates; degrees/second |
| RGA-B | AGS gyro rates in body coordinates; degrees/second |
| AGS-B | AGS linear velocity in body coordinates; feet/second |
| LGC-B | Accumulated PIPA quantity while SERVICER runs, in body coordinates; feet/second |
| ACT ΔV | Ground-computed gained delta velocity; feet/second |
| SM | Two-second accumulated PIPA quantity in stable-member coordinates; feet/second |
| DAP (status, left) | Guidance/control switch selection; AGS/PGNS |
| DAP (status, right) | DAP state; ON/OFF |
| TIG | Ignition time; hours:minutes:seconds |
| TGO | Time until cutoff; seconds |
| TEVT | Last/next significant event time; hours:minutes:seconds |
| T/P | Time until descent phase ends; seconds |
| LGC / ISS (warning section) | Respective warning-lamp states |
| PGNS / PROG (warning section) | Respective caution-lamp states |
| FREG0 / FREG1 / FREG2 | First, second, and most recent alarm codes; octal |
| REDO | Restart count; displayed in octal |
| PROG (DSKY section) | Computer program number |
| VERB / NOUN | DSKY verb and noun |
| FL | Verb/noun flash indication; FLSH/blank |
| R1 / R2 / R3 | DSKY register displays |
| LR RNG | Landing-radar range validity; GOOD/BAD |
| VEL | Landing-radar velocity validity; GOOD/BAD |
| VXS / VYS / VZS | Landing-radar velocities converted to stable-member coordinates; feet/second |
| RANGE (landing radar) | Radar slant range; feet |
| ΔH (middle column) | Landing radar minus LGC altitude; feet |
| ΔH (right column) | Landing radar minus AGS altitude; feet |
| PGNS comparison column | Landing-radar minus PGNS velocities, corrected for lunar gravity in stable-member coordinates; feet/second |
| ΔAGS comparison column | Landing-radar minus AGS velocities, corrected for lunar gravity in stable-member coordinates; feet/second |
| RR (state) | Rendezvous-radar state; ON/OFF |
| CNTRL | Rendezvous-radar control mode; AUTO/MAN |
| DATA | Rendezvous-radar validity; GOOD/BAD |
| MODE | Rendezvous-radar antenna mode; 1/2 |
| LGC (radar position) | Radar antenna position from CDU; degrees |
| RR (radar position) | Radar antenna position in FDAI coordinates; degrees |
| ERR (radar) | Computer-commanded radar antenna rate; degrees/second |
| RANGE (rendezvous radar) | Range; nautical miles |
| RNGRT | Range rate; feet/second |
| 800~ / 3200~ | Respective AC voltage indications; volts |
| 120V | PIPA DC supply indication; volts |
| BIAS (power section) | Bias-voltage indication; volts |
| LR / RR / PIP (temperature section) | Radar antenna and PIPA temperatures; Fahrenheit |

## Open interpretation issues

- The definition page's landing-radar labels do not reproduce every layout label literally. For example the layout uses RNG and comparison-column markings. Preserve both definition and layout evidence when building keys.
- The power BIAS description appears to read “28 BIAS VOLTAGE”; the exact historical abbreviation and nominal value need a clearer-source check. Only its identity as a voltage is accepted here.
- A repeated label (LGC, RR, DAP, PROG, BIAS, RANGE) denotes different fields according to section.
- The torque indications are specified in seconds; do not substitute physical torque units without researching their accumulation/scaling.
- The two-second SM accumulation interval does not establish CRT refresh cadence.
- Underlying downlist words, scaling equations, reference frames, gravity correction, quality flags, and missing-data behavior remain unresolved at implementation level.

See [cross-mission comparison](030_apollo11_apollo13_msk1137_comparison.md).
