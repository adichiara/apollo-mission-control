# Apollo 13 PC+2 GDA trim source catalog

Date: 2026-09-16

## Apollo 13 Luminary 1C / Luminary 131 source listing — Verb 48 DAP-load routine

- File: `EXTENDED_VERBS.agc`
- Listing: https://www.ibiblio.org/apollo/listings/Luminary131/EXTENDED_VERBS.agc.html
- Relevant printed pages: 297–298
- Source class: Apollo 13 mission flight-software source listing

### Supports

R03 reaches Noun 47 as the mass-load step. `V34E` branches to termination before Noun 48, while the proceed path reaches Noun 48 and later `TRIMGIMB`. The PC+2 instruction to enter V34 after N47 therefore selected a real software termination path before N48.

### Boundary

This proves the computer/procedural branch, not CONTROL's reason for selecting it.

## NASA Apollo 13 air-to-ground transcript — ~59 GET provisional PC+2 pad

- Relevant GET: approximately 59:03–59:05
- Source class: primary mission voice transcription

### Supports

CAPCOM passes PC+2 DPS trim/GDA pitch `5.86°`, roll `6.75°`, while explicitly saying the angles "will be updated" and should be used for the moment. Crew reads the pair back and CAPCOM accepts it.

### Boundary

At this point the pair is explicitly provisional for PC+2; the statement does not identify the generating mass-properties job.

## NASA Apollo 13 Technical Air-to-Ground Voice Transmission — 61:29 free-return DPS burn

- NASA PDF: https://www.nasa.gov/wp-content/uploads/2026/01/as13-tec.pdf
- Relevant GET: `060:53:09`–`060:56:21`
- Tape/pages: 41/9–41/10, 217–218
- Source class: primary mission voice transcription

### Supports

- CAPCOM's P30 pad for the 61:29:42.84 free-return midcourse correction explicitly gives LM GDA pitch `5.86°`, roll `6.75°`.
- Haise reads back the same GDA pair with the free-return pad and CAPCOM accepts the readback.
- This is the exact numerical pair previously passed with the provisional ~59 GET PC+2 pad.

### Consequence

The primary voice record now establishes commanded-value continuity:

`~59 provisional PC+2 5.86 / 6.75 -> 61:29 free-return burn commanded 5.86 / 6.75 -> powered-flight compliance -> resulting GDA state`.

This is significant because CONTROL later identifies the 61:29 maneuver's 40% powered-flight compliance as the state-setting event expected to provide optimum PC+2 alignment.

### Boundary

Do not infer that post-compliance actuator angles remained exactly `5.86 / 6.75`. Commanded initial trim and resulting complied state are distinct.

## NASA Apollo 13 mission commentary — post-61:29 revised PC+2 pad readback

- Relevant transcript header: approximately `GET 63:10:00`
- Source class: primary mission voice/PAO transcription

### Supports

After the free-return maneuver, the revised PC+2 pad says GDA should be "okay as is" and associates the retained reference with pitch `5.85`, second-axis value `6.74`. The crew qualifies the identification with "hopefully."

### Boundary

This is evidence for an intended/reference value, not measured actuator telemetry. The `0.01°` difference from `5.86 / 6.75` is not a recovered PC+2 tolerance.

## NASA Apollo 13 air-to-ground transcript — PC+2 two-hour activation

- Relevant GET: `075:07:43`–`075:08:35`
- Source class: primary mission voice transcription

### Supports

CAPCOM instructs `VERB 34 ENTER` immediately after Noun 47. Haise asks whether that means the gimbals already look all right; Duke answers affirmatively. Combined with Luminary 131, this establishes no new crew-entered Noun 48 trim in this activation sequence.

## NASA Apollo 13 PAO/air-to-ground transcript — PC+2 burn rules

- Relevant GET: `076:35`–`076:39`
- Source class: primary mission voice/PAO transcription

### Supports

Brand states that after PC+2 there are no trim requirements; Haise reads back that there are no trim requirements on the burn.

## NASA Apollo 13 final P30 read-up

- Relevant GET: `077:55:24`
- Source class: primary mission voice transcription

### Supports

Final PC+2 P30 targeting read-up omits a GDA trim pair, consistent with the no-new-Noun-48 workflow.

## NASA Flight Control Division Mission Operations Report — Apollo 13

- Date: 28 April 1970
- NASA scan: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a13/A13_MissionOpReport.pdf
- Source class: primary mission-specific controller report

### Supports

- RTCC LM-burn mass-property decks were updated to T+55 decks.
- ~59 GET CONTROL/Flight Dynamics trim disagreement and reconciliation; CONTROL's challenged basis used premission mass properties.
- Earlier T+25 RTCC mass-properties run where no update was needed because pitch/yaw trims were within `0.01°` of T+6.
- Final-preparation ground rules explicitly include no PC+2 maneuver trims required.
- CONTROL reports roll GDA moved to approximately `-2°` at PC+2 ignition by `-1.2°`, implying approximate pre-ignition roll `~-0.8°` by arithmetic.
- CONTROL says ignition motion was unexpected because the GDA settings at the end of the 61:29 maneuver, with 40% thrust compliance, were expected to provide optimum PC+2 alignment.

### Boundary

The report does not identify a PC+2 numbered job, calculation timestamp, printed T+55 deck contents, candidate comparison values, exact post-61:29 two-axis complied state, or direct T+55-to-trim calculation link.

## Current synthesis

Do not search for or invent a "final PC+2 Noun 48 pair" as though one must have existed. Current evidence supports:

`mass-properties deck/reference state -> calculation/comparison [details unresolved] -> ~59 provisional PC+2 trim 5.86 / 6.75 -> same 5.86 / 6.75 commanded for 61:29 free-return DPS burn -> 40%-thrust compliance -> exact post-compliance GDA state unrecovered -> later PC+2 reference "okay as is" [5.85 / 6.74, qualified by "hopefully"] -> no new PC+2 trim required -> Noun 47 -> VERB 34 termination -> software exits before Noun 48 -> no new Noun 48 crew entry -> PC+2 powered-flight GDA response [roll pre-ignition ≈ -0.8° derived from CONTROL motion report]`.

The next archival target remains the upstream controller artifact: PC+2/LM-burn candidate trim calculation, real-time weight/c.g. inputs, comparison values and criterion, calculation/job identity, CONTROL's competing trim, and direct T+55 deck linkage. A telemetry or working-sheet record of the post-61:29 complied state remains the highest-value downstream target.