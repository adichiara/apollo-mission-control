# Apollo 13 ground-product integrity failure — AGS body-angle processing after MCC-5

Date: 2026-09-12  
Status: **REVIEWED — source-backed architecture case; not part of the PC+2 historical interval**

## Question

Can the simulator represent a controller-visible ground product that is present and apparently usable, even though the underlying spacecraft state and received telemetry are satisfactory and the ground transformation itself is wrong?

## Primary-source case

The Apollo 13 Mission Operations Report records exactly such a case after MCC-5.

After the crew established passive thermal control using AGS, the ground's last high-bit-rate attitude readout did not agree with the desired attitude. The crew was asked to return to high-bit-rate telemetry. Mission Control then determined that the **RTCC was incorrectly processing AGS body angles**.

The ground discarded the improper processed readout and used the independent FDAI reference, which showed that passive thermal control had in fact been established correctly.

The same event is preserved in NASA's Apollo 13 Flight Control Division / mission-operations material and is also indexed in the project research already completed for AGS direction-cosine ground processing.

## Evidence boundary

This source establishes:

1. spacecraft attitude can be satisfactory;
2. received spacecraft/AGS data can exist;
3. a ground-processing transformation can nevertheless produce a wrong controller-facing product;
4. the wrong product need not automatically identify itself as invalid;
5. an independent reference can allow controllers to reject the bad product.

It does **not** establish:

- the exact numerical erroneous body angles;
- the exact RTCC software defect or equation error;
- a controller-visible `INVALID` flag attached to the bad value;
- exact timing beyond the post-MCC-5 / PTC sequence;
- that the same failure occurred during PC+2.

Therefore no synthetic angle value is promoted as historical truth, and the case is used as an architectural validation case rather than inserted into the nominal PC+2 scenario.

## Implementation consequence

The existing `Product.validity` field is not sufficient by itself to represent this event if `validity` is interpreted as what the controller-facing product claims or whether it is available.

A wrong ground computation may still be:

- present;
- current;
- formatted normally;
- available to the controller;
- not automatically flagged by the system.

The project therefore needs a second, internal semantic dimension: **product integrity**.

Recommended distinction:

- `validity`: availability/status presented or operationally associated with the product (`valid`, `stale`, `invalid`, `unavailable` where historically justified);
- `integrity`: simulator truth about whether the product correctly represents its source state (`correct`, `incorrect`, `unknown`).

For the Apollo 13 AGS/RTCC case:

```text
spacecraft attitude       satisfactory
AGS source information    available
RTCC body-angle product   available/present
product validity          not known to be system-flagged invalid
product integrity         INCORRECT
independent FDAI cue       CORRECT
controller conclusion      reject RTCC readout; trust independent cue
```

The integrity field is simulation/audit metadata. It must **not** automatically appear on a player's display or become an unsolicited diagnostic hint.

## Architectural rule

A scenario fault should be able to affect the ground-processing layer without mutating the underlying physical state or raw source data.

Conceptually:

```text
physical attitude (correct)
        ↓
AGS/source data (correct)
        ↓
RTCC transformation (faulted)
        ↓
body-angle product (incorrect but present)

independent FDAI reference (correct)
        ↓
controller cross-check
```

This is materially different from:

- telemetry loss;
- stale telemetry;
- sensor failure;
- spacecraft attitude failure.

## PC+2 relevance

The event itself is later than PC+2 and must not be inserted into the first vertical slice as though it occurred there.

Its value is architectural: PC+2 controller products already distinguish source, telemetry, ground processing, and display layers. This historical case validates implementing ground-product corruption as an independent failure class before broader nonnominal scenarios are authored.

## Sources

Primary:

- NASA Flight Control Division, *Mission Operations Report — Apollo 13*, 28 April 1970, LM CONTROL narrative, post-MCC-5 passive-thermal-control discussion.
- NASA NTRS 19710010485, *MSC Apollo 13 Investigation Team, Panel 3 — Flight Operations and Network Final Report*, May 1970, for contemporary flight-operations/network context.

Existing repository cross-checks:

- `resources/research/037_apollo13_ags_telemetry_ground_processing.md`
- `resources/research/040_apollo13_ags_attitude_direction_cosine_path.md`
- `resources/research/052_pc2_controller_product_projection.md`

## Access note

During this pass, the currently indexed NASA/NTRS PDF endpoints could not be rendered through the web PDF screenshot path (NASA URL returned 404; NTRS archive PDF returned 403). The historical wording was recoverable through indexed NASA/search text and previously cataloged mission documentation, but this pass does not claim a new page-image inspection.

## Next implementation step

Add internal product-integrity metadata and a ground-processing corruption helper, then test the Apollo 13 architecture case with:

- correct source/spacecraft state;
- incorrect ground-derived attitude product;
- no automatic controller-visible invalid flag;
- correct independent reference;
- no automatic diagnosis or corrective action.
