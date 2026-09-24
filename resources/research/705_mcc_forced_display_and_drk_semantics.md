# 705 — MCC forced-display and DRK semantics

Date: 2026-09-24
Research thread: `apollo-mocr-controller-interface`

## Question

Can the open Apollo 11 console-display interaction be narrowed further without inventing Mission-G GUIDO key assignments?

## Primary-source result

Yes, at the generic MCC interaction level. The contemporary Saturn V Flight Manual for SA-507 (Apollo 12) describes two relevant console devices:

- the **forced display module (FDK)** monitors preprogrammed analog-parameter limits. When an out-of-tolerance condition occurs, the corresponding pushbutton indicator illuminates; acknowledging it produces a **four-digit code identifying the display format** on which the out-of-tolerance parameter appears;
- the **display request keyboard (DRK)** provides a fast way to request a specific RTCC display format by pressing the appropriately labeled pushbutton indicator. The manual explicitly says this is the same capability as the Manual Select Keyboard in display-request mode, but faster because thumbwheel selection is unnecessary.

This complements NASA TN D-7685: the latter establishes central request/channel-allocation behavior, while the flight manual establishes the controller-side distinction between general numeric format selection and fast pre-labeled DRK access, plus a separate alert-to-format-code path.

## Effectivity boundary

SA-507 is the Apollo 12 launch vehicle manual, not a Mission-G console-configuration record. These passages describe MCC console architecture immediately after Apollo 11 and are useful as **near-contemporary generic interaction evidence only**.

They do **not** establish:

- which DRK labels or format numbers were assigned to Apollo 11 GUIDO;
- whether GUIDO's Apollo 11 station had a particular FDK configuration;
- which display Bales selected during P63/P64/P66;
- whether a 1201/1202 alarm itself illuminated an FDK pushbutton;
- Apollo 11 request cadence or latency.

No such details are inferred.

## Simulator consequence

The generic console interaction can now distinguish three historically grounded actions:

1. **MSK display request** — select a format numerically and request it;
2. **DRK fast request** — request a preassigned format with one labeled key;
3. **FDK alert/lookup** — acknowledge an out-of-tolerance indication and obtain the identifying display-format code.

For the Apollo 11 GUIDO reference, the simulator should expose those mechanics only at the architecture level until Mission-G-effective configuration evidence identifies actual keys/formats. A modern alert that automatically opens a guessed GUIDO display would exceed the evidence.

## Sources

- NASA/MSFC, _Saturn V Flight Manual, SA-507_, mission-control section, console-keyboard discussion (Apollo 12 vehicle; 1969): https://www.nasa.gov/wp-content/uploads/static/history/afj/ap12fj/pdf/a12_sa507-flightmanual.pdf

## Evidence status

- **DOCUMENTED / PRIMARY / NEAR-CONTEMPORARY GENERIC:** DRK is a faster pre-labeled equivalent of MSK display-request mode.
- **DOCUMENTED / PRIMARY / NEAR-CONTEMPORARY GENERIC:** FDK out-of-tolerance acknowledgement exposes a four-digit identifying display-format code.
- **OPEN / MISSION-G-SPECIFIC:** GUIDO DRK labels/format assignments, FDK configuration, exact descent callups, and cadence/latency.
- **NO INFERENCE:** program alarms are not mapped to FDK behavior without Mission-G evidence.
