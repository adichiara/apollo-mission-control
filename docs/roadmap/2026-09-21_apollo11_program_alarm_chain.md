# Roadmap continuation — Apollo 11 1201/1202 program-alarm chain

Date: 2026-09-21
Parent: `docs/roadmap/2026-09-21_apollo11_landing_go_poll.md`

## Bounded question

What can be established about the Apollo 11 powered-descent 1201/1202 decision chain without importing later recollection as if it were contemporary procedure?

## Primary/contemporary result

The Apollo 11 air-to-ground record fixes the crew-facing end of the chain. After the first 1202, Armstrong asks Houston for a reading and CAPCOM answers that Eagle is GO on the alarm. Later, after the 1201, CAPCOM answers immediately that it is the same type and the crew is GO. These are operational GO calls, not merely acknowledgements of the alarm code.

The surviving controller-loop record fixes the front-room disposition: GUIDANCE/Steve Bales supplies the GO assessment to FLIGHT; FLIGHT accepts the disposition; CAPCOM relays it to Eagle. For the later 1201, the controller-loop sequence supports the compact `GUIDANCE: same type / GO → FLIGHT: GO → CAPCOM: same type / GO` chain.

NASA's archival account of Jack Garman identifies him as the back-room computer specialist supporting Bales and states that Bales called to Garman, who recognized 1202 as an overload warning compatible with continuing the landing. This establishes a support-room specialist role in the decision chain, but that later NASA historical account is not sufficient to manufacture exact 1969 back-room wording or a formalized message schema.

## Written-rule source recovery — 2026-09-21

The surviving NASA-hosted Apollo 11 *Flight Mission Rules* scan is dated **16 April 1969**. Purdue's Neil Armstrong collection catalogs a later *Final Flight Mission Rules* copy dated **16 May 1969**. Both predate the final descent simulation that prompted the program-alarm review described in later controller testimony. They therefore cannot, by themselves, establish the late preflight alarm criterion produced after that simulation.

Contemporary postflight engineering sources do establish the technical behavior without supplying the missing preflight decision sheet. MIT/IL memo AG#370-69 (4 August 1969) records five Mission-G executive-overflow alarms, their P63/P64 timing, and the overload mechanism. Grumman memo LAV-500-940 (31 July 1969) is specifically a powered-descent program-alarm investigation. These are valid primary engineering evidence for what the alarms meant and how the LGC behaved, but they are postflight analyses and must not be mislabeled as the rule used at the console on 20 July.

A targeted recovery pass for the named late-preflight artifact classes did **not** recover a contemporary post-simulation rule-change page/change notice, authenticated Bales/Garman alarm cue sheet, or dated Guidance/training procedure from the final-simulation-to-landing interval. NASA's later Garman institutional history confirms that Garman prepared an alarm list before the landing, but it does not reproduce the sheet or establish its exact decision wording. Secondary recollections describe an `if it doesn't recur/come up too much` concept, but those are not promoted to the missing contemporary rule.

Under D-024, the **exact late-preflight written criterion is now BLOCKED on named source recovery**, rather than remaining an open-ended search item. Reopen only if one of the named artifact classes becomes accessible.

## Implementation consequence

The reference descent may model program alarms as:

`crew reports alarm → GUIDANCE evaluates with computer-specialist support → GUIDANCE recommends GO/abort to FLIGHT → FLIGHT owns disposition → CAPCOM relays operational disposition to crew`

For repeated alarms of the established executive-overflow family, the recorded 1201 exchange supports a shortened `same type / GO` response. Do not model `1201` and `1202` as automatically harmless. Do not encode a numeric recurrence threshold. The source-backed behavior is an evaluated GO during the flown sequence, not a universal alarm-number rule.

## Evidence boundary

- The air-to-ground transcript is primary for CAPCOM/crew speech.
- Controller-loop audio is primary for GUIDANCE→FLIGHT disposition where audible.
- MIT/IL AG#370-69 and Grumman LAV-500-940 are primary contemporary postflight engineering evidence for alarm mechanism and occurrence.
- The available April/May Flight Mission Rules copies predate the late simulation-driven review and cannot prove the resulting criterion.
- NASA's Garman historical biography is authoritative institutional corroboration for Garman's support role and preflight alarm-list preparation but is retrospective, not the cue sheet itself or a verbatim controller-loop transcript.
- Exact Garman→Bales words, precise support-room loop topology, a Mission-G CRT field that drove the alarm judgment, and the exact late-preflight written GO/abort rule are not claimed here.

## Closure and next bounded target

This exact written-criterion subquestion is **BLOCKED** under D-024 on recovery of a post-simulation mission-rule change page/change notice, the Bales/Garman alarm cue sheet or authenticated contemporary copy, or a revised Apollo-11-effective Guidance/training procedure dated after the final descent simulation and before landing.

The broader Apollo 11 powered-descent reference remains **OPEN**. Continue with the next controller-product/interface or sourced decision-rule dependency; do not continue generic alarm-rule searching unless the named source condition changes.

## Sources

- NASA, *Apollo 11 Technical Air-to-Ground Voice Transcription (GOSS NET 1)*, July 1969: https://ntrs.nasa.gov/citations/20160014392
- Apollo 11 descent Flight Director/GUIDANCE controller audio preserved in the Apollo 11 mission audio archive.
- NASA-hosted *Flight Mission Rules, Apollo 11 (AS-506/107/LM-5)*, 16 April 1969: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11missionrules.pdf
- Purdue University Archives, Neil A. Armstrong papers, *Final Flight Mission Rules, Apollo 11*, 16 May 1969: https://archives.lib.purdue.edu/repositories/2/archival_objects/38088
- MIT Instrumentation Laboratory, George Cherry, AG#370-69, *Exegesis of the 1201 and 1202 Alarms Which Occurred During the Mission G Lunar Landing*, 4 August 1969: https://www.ibiblio.org/apollo/Documents/CherryApollo11Exegesis.pdf
- Grumman Aircraft Engineering Corporation, Clint Tillman, LAV-500-940, *Program Alarms in Powered Descent - Apollo 11*, 31 July 1969: https://www.ibiblio.org/apollo/Documents/Memo-Tillman690731_text.pdf
- NASA History, `Apollo Era Hero John "Jack" Garman Dies` (2016): https://www.nasa.gov/image-article/apollo-era-hero-john-jack-garman-dies/

## Evidence status

- **DOCUMENTED / PRIMARY TRANSCRIPT:** CAPCOM gives the crew GO on the first 1202 and later 1201.
- **DOCUMENTED / PRIMARY AUDIO:** GUIDANCE supplies the front-room GO assessment to FLIGHT; the later 1201 is treated as the same alarm type and GO.
- **DOCUMENTED / PRIMARY POSTFLIGHT ENGINEERING:** alarm occurrence, executive-overflow mechanism, and restart behavior.
- **DOCUMENTED / RETROSPECTIVE NASA:** Garman supported Bales from the back room and prepared a preflight alarm list.
- **BLOCKED / NAMED SOURCE RECOVERY:** exact late-preflight written GO/abort criterion and cue-sheet wording.
- **UNRESOLVED BUT NOT INFERRED:** verbatim support-room exchange and exact alarm-specific CRT basis.