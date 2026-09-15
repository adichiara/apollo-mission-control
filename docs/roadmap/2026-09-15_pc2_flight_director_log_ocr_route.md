# PC+2 controller-record roadmap — searchable Flight Director Log

Date: 2026-09-15  
Research note: `resources/research/164_pc2_flight_director_log_ocr_route.md`

## Roadmap refinement

The Flight Director Log target identified in note 163 now has a searchable OCR derivative. This changes the immediate archival task from blind/manual inspection of a 378 MB handwritten scan to a two-stage process: OCR discovery followed by high-resolution handwriting verification.

## Priority sequence

1. Search the OCR Flight Director Log across the ~59–74 GET decision interval.
2. Verify candidate pages against the high-resolution handwritten log.
3. Extract only verified references to PC+2 mass properties, trim/GDA state, CONTROL/Flight Dynamics comparison, RTCC/RTACF run/job, or the no-update decision.
4. If no upstream calculation survives in the Flight Director Log, target CONTROL/Flight Dynamics working sheets and RTCC/RTACF output records.

## Numerical-model gate

Do not add a final PC+2 N48 trim load. Existing evidence says the crew was intentionally branched out before N48 and that no PC+2 maneuver trims were required. Do not introduce a comparison tolerance or candidate trim until a primary record supplies it.