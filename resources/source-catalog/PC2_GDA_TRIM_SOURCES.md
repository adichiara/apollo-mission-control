# Apollo 13 PC+2 GDA trim source catalog

Date: 2026-09-15

## NASA Apollo 13 air-to-ground transcript — PC+2 two-hour activation

- Relevant GET: `075:07:43`–`075:08:35`
- Transcript navigation: https://apollo13.spacelog.org/03%3A03%3A07%3A13/
- Corrected transcript/context: https://www.apollojournals.org/afj/ap13fj/12day4-approach-moon.html
- Source class: primary mission voice transcription; modern transcript interfaces used for navigation

### Supports

- CAPCOM instructs `VERB 34 ENTER` immediately after Noun 47 during the PC+2 DAP-loading procedure.
- Haise explicitly asks whether the instruction means the gimbals already look all right.
- Duke answers affirmatively and says there is nothing else on page 14.
- The procedure therefore terminates before the normal Noun 48 engine-gimbal trim entry.

### Boundary

This establishes **no new crew-entered Noun 48 trim during this PC+2 activation sequence**. It does not identify the exact retained gimbal state, prove reuse of the earlier `5.86° / 6.75°` pair, or prove that no ground-computed candidate trim existed.

## NASA Apollo 13 PAO/air-to-ground transcript — PC+2 burn rules

- Relevant GET: `076:35`–`076:39`
- NASA transcript PDF: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
- Corrected transcript navigation: https://www.apollojournals.org/afj/ap13fj/12day4-approach-moon.html
- Source class: primary mission voice/PAO transcription

### Supports

- Brand states that after PC+2 there are no trim requirements.
- Haise reads back, “there's no trim requirements on this burn.”
- CAPCOM corrects a different readback error (`178` to `78` hours) but does not correct the trim statement.

### Boundary

The phrasing is not sufficient by itself to reconstruct the controller-side rationale or exact pre-ignition gimbal angles. It is strongest when combined with the explicit `VERB 34`-before-Noun-48 procedure above.

## NASA Apollo 13 final P30 read-up

- Relevant GET: `077:55:24`
- NASA transcript PDF: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
- Source class: primary mission voice transcription

### Supports

- Final PC+2 P30 targeting read-up omits a GDA trim pair; CAPCOM states the remaining fields are N/A except comments.

### Boundary

This omission is now consistent with, but is not the sole evidence for, the no-new-Noun-48 workflow.

## NASA Flight Control Division Mission Operations Report — Apollo 13

- Report: MSC-02680
- Date: 1970-04-28
- Scan: https://apollojournals.org/alsj/a13/A13_MissionOpReport.pdf
- Source class: primary mission-specific postflight report

### Supports

- `T+55` LM-burn mass-property-deck lineage;
- ~59-hour CONTROL/Flight Dynamics trim disagreement and reconciliation;
- PC+2 execution-state GDA observations.

### Boundary

No recovered passage yet identifies the mass-properties job/comparison that supported the later PC+2 **no-update** decision.

## Current synthesis

Do not search for or invent a “final PC+2 Noun 48 pair” as though one must have existed. Current primary operational evidence supports:

`computed/available trim information -> controller acceptance/no-update decision -> Noun 46 configuration -> Noun 47 weights -> VERB 34 termination -> no new Noun 48 crew entry -> retained gimbal state -> powered-flight GDA response`.

The next archival target is the controller-side basis for the no-update decision, not a presumed missing crew-entered trim pair.