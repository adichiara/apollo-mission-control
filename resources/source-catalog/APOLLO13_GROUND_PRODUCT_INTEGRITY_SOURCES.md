# Apollo 13 Ground-Product Integrity Sources

Status: active source supplement for the Apollo Mission Control data-path model.

## 1. Apollo 13 Mission Operations Report

- **Title:** *Mission Operations Report — Apollo 13*
- **Organization:** NASA Manned Spacecraft Center / Flight Control Division
- **Date:** 28 April 1970
- **Source class:** PRIMARY, mission-specific
- **Use in project:** Documents the post-MCC-5 case in which the ground's AGS attitude readout disagreed with the desired attitude, the RTCC was found to be incorrectly processing AGS body angles, the improper readout was disregarded, and the independent FDAI reference showed PTC was properly established.
- **Implementation consequence:** Supports wrong-but-present ground-derived products and independent cross-checks; does not support an automatic controller-visible `INVALID` label.
- **Limitations:** The report does not provide the erroneous numerical body angles or the exact RTCC software defect/equations.
- **Repository cross-reference:** `resources/research/065_apollo13_ground_product_integrity_failure.md`

## 2. MSC Apollo 13 Investigation Team, Panel 3 — Flight Operations and Network Final Report

- **NASA NTRS ID:** 19710010485
- **Report:** NASA-TM-X-66933
- **Date:** May 1970
- **Source class:** PRIMARY, contemporary investigation/operations record
- **Use in project:** Supports the broader flight-operations/network chronology and contemporary handling of post-accident Mission Control operations.
- **NTRS record:** https://ntrs.nasa.gov/citations/19710010485
- **Limitations:** The currently indexed archive PDF endpoint returned HTTP 403 to the web screenshot reader during the 2026-09-12 pass; no new page-image inspection is claimed from this source in note 065.

## 3. Existing AGS/RTCC repository evidence

- `resources/research/037_apollo13_ags_telemetry_ground_processing.md`
- `resources/research/040_apollo13_ags_attitude_direction_cosine_path.md`
- `resources/research/052_pc2_controller_product_projection.md`

These notes already establish the architectural separation among AEA/AGS source data, RTCC transformation, and controller-facing products. Note 065 uses the post-MCC-5 event as the first explicit product-integrity validation case.

## Evidence rule

For implementation, do not equate:

- data present with data correct;
- `validity=valid` with simulator-known integrity;
- an independent confirming cue with a hidden diagnostic flag.

Product integrity is internal simulation/audit metadata unless a historical system explicitly exposed a validity/quality indication to the controller.

## Implementation follow-through — explicit controller decision layer

Research note `resources/research/066_controller_product_rejection_decision_event.md` records the implementation consequence of the same primary case: rejection is a controller decision/audit event, not an automatic result of hidden integrity metadata.

This does not add a new historical claim; it preserves the source-supported separation between a bad RTCC product, an independent FDAI reference, and Mission Control's decision to disregard the bad readout.
