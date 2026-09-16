# Apollo 13 PC+2 GDA trim source catalog

Date: 2026-09-15

## Apollo 13 Luminary 1C / Luminary 131 source listing — Verb 48 DAP-load routine

- File: `EXTENDED_VERBS.agc`
- Listing: https://www.ibiblio.org/apollo/listings/Luminary131/EXTENDED_VERBS.agc.html
- Relevant printed pages: 297–298
- Relevant labels: `DAPDATA2`, `ENDR03`, `DAPDAT2`, `DAPDATA3`, `DPDAT3`, `TRIMGIMB`
- Source class: Apollo 13 mission flight-software source listing, transcribed from MIT Museum program-listing material

### Supports

- R03 explicitly reaches Noun 47 as the mass-load step.
- At the Noun 47 response dispatch, `V34E` branches to `ENDR03` and then `ENDEXT`.
- The `V33E` proceed branch instead performs mass/moment processing and reaches `DAPDATA3`.
- `DAPDATA3` explicitly displays Noun 48 and requests a response; a later proceed response invokes `TRIMGIMB`.
- The PC+2 instruction to enter V34 after N47 therefore selected a real software termination path before N48.

### Boundary

This proves the computer/procedural branch, not CONTROL's reason for selecting it. It does not recover the candidate trim, tolerance, retained two-axis state, or mass-properties job behind the no-update decision.

## NASA Apollo 13 air-to-ground transcript — 61:29 free-return DPS burn

- Relevant GET: approximately `061:10`
- NASA PAO/air-to-ground transcript; searchable transcript derivative used for navigation
- Source class: primary mission voice transcription

### Supports

- Immediately before the 61:29 contingency free-return DPS burn, CAPCOM explicitly says the GDA settings are **"go as they are."**
- This provides a direct operational bridge from the pre-burn accepted GDA state into the powered maneuver.

### Boundary

It does not prove that the post-burn complied GDA angles equal the earlier commanded `5.86° / 6.75°` pair. CONTROL later describes the 40%-thrust compliance as the state-setting event relevant to PC+2.

## NASA Apollo 13 mission commentary — post-61:29 revised PC+2 pad readback

- Relevant transcript page header: approximately `GET 63:10:00`
- NASA Apollo 13 mission commentary / air-to-ground transcript
- Searchable NASA result text: `GDA should be okay as is, which hopefully is Pitch, 5.85 Yaw 6.74.`
- Source class: primary mission voice/PAO transcription

### Supports

- After the 61:29 free-return maneuver, the crew reads back a revised PC+2 pad with the disposition that the **GDA should be okay as is**.
- The same readback associates that intended retained reference with pitch `5.85` and a second GDA-axis value `6.74`.
- The transcript renders the second axis as `Yaw`; preserve that transcription as a source caveat rather than silently normalizing it.
- The pair is numerically `0.01°` below the earlier `5.86 / 6.75` interim pair.

### Boundary

The crew qualifies the numerical identification with **"hopefully"**. This is therefore evidence for an intended/retained PC+2 reference, not a measurement of post-compliance actuator position. The `0.01°` difference from the earlier pair must not be treated as a recovered PC+2 comparison tolerance, and the T+25 `0.01°` no-update precedent must not be imported into this event.

## NASA Apollo 13 air-to-ground transcript — PC+2 two-hour activation

- Relevant GET: `075:07:43`–`075:08:35`
- Transcript navigation: https://apollo13.spacelog.org/03%3A03%3A07%3A13/
- Corrected transcript/context: https://www.apollojournals.org/afj/ap13fj/12day4-approach-moon.html
- Source class: primary mission voice transcription; modern transcript interfaces used for navigation

### Supports

- CAPCOM instructs `VERB 34 ENTER` immediately after Noun 47 during the PC+2 DAP-loading procedure.
- Haise explicitly asks whether the instruction means the gimbals already look all right.
- Duke answers affirmatively and says there is nothing else on page 14.
- Combined with the Luminary 131 source above, the instruction is software-confirmed to terminate the routine before Noun 48.

### Boundary

This establishes **no new crew-entered Noun 48 trim during this PC+2 activation sequence**. It does not prove that the `5.85 / 6.74` pad/reference pair was the instantaneous actuator state or identify the ground-computed candidate trim.

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

The phrasing is not sufficient by itself to reconstruct the controller-side rationale or exact pre-ignition gimbal angles. It is strongest when combined with the explicit `VERB 34`-before-Noun-48 procedure and the Luminary branch evidence above.

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
- NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- Alternate searchable scan: https://www.ccas.us/CCAS_NASA_PressKits/Apollo_Missions/Apollo13_MissionOperationsReport.pdf
- Source class: primary mission-specific postflight report

### Supports

- RTCC **LM-burn mass-property decks were updated to T+55 decks**;
- ~59-hour CONTROL/Flight Dynamics trim disagreement and reconciliation;
- CONTROL's disputed trim basis used **premission mass properties**, explicitly described as not the best data available;
- a separate mission-specific **T+25 RTCC mass-properties run** where Flight Dynamics explicitly decided that no trim update was needed because pitch/yaw trims were within `0.01°` of the T+6 values;
- Flight Director final-preparation ground rules after the ~74:00 GET White Team handover explicitly include **“No PC+2 maneuver trims were required”**;
- PC+2 execution-state GDA observations;
- CONTROL reports that the roll GDA moved to approximately `-2°` at PC+2 ignition, a change of `-1.2°`; these approximate reported quantities imply an immediately pre-ignition roll position of about `-0.8°` by arithmetic;
- CONTROL says that ignition roll-GDA motion was unexpected because the ground expected the GDA settings at the end of `MCC-3`, with its 40% thrust compliance, to provide optimum PC+2 alignment;
- the report's LM CONTROL section itself labels the **61:29 contingency free-return DPS burn** `MCC-3 - DPS 1` and the following coast `POST MCC-3 TLC`, reconciling that wording with the same report's mission-summary convention that calls the 61:29 maneuver MCC-4 and the originally planned pre-accident MCC-3 not required.

### Boundary

`T+55` is supported as a deck/reference-epoch family. The report does **not** identify a PC+2 numbered job, calculation timestamp, printed T+55 deck contents, candidate comparison values, or a direct calculation-level link from T+55 to the operational GDA reference. The T+25 case establishes a `run -> compare -> update/no-update` workflow, but its `0.01°` criterion must not be transferred to PC+2. The nomenclature reconciliation identifies CONTROL's state-setting maneuver but does not recover its exact post-compliance two-axis actuator state. The `~-0.8°` roll figure is a derived approximate pre-PC+2 execution value; the separate `5.85 / 6.74` evidence is a crew pad/reference readback. Neither should be silently substituted for the missing RTCC candidate/reference comparison.

## Current synthesis

Do not search for or invent a “final PC+2 Noun 48 pair” as though one must have existed. Current primary operational, controller, and software evidence supports:

`mass-properties deck/reference state -> calculation/comparison [details unresolved] -> pre-61:29 GDA state accepted ("go as they are") -> 61:29 free-return DPS maneuver -> 40%-thrust compliance -> post-MCC-3 PC+2 reference read back as "okay as is" [5.85 / 6.74, qualified by "hopefully"] -> retained/reference state carried through coast -> ground judges no new PC+2 trim required -> Noun 46 configuration -> Noun 47 display -> VERB 34 termination -> software exits R03 before Noun 48 -> no new Noun 48 crew entry -> powered-flight GDA response [roll pre-ignition ≈ -0.8° derived from CONTROL motion report]`.

The next archival target is a controller-side artifact **upstream of the documented no-update judgment**: PC+2 candidate trim, reference values actually used for comparison, comparison delta/tolerance, calculation time/job identity, and direct T+55 deck linkage. A telemetry/working-sheet bridge between the pad/reference pair and actual actuator state would also resolve the remaining state-reconciliation ambiguity.