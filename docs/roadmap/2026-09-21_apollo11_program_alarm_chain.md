# Roadmap continuation — Apollo 11 1201/1202 program-alarm chain

Date: 2026-09-21
Parent: `docs/roadmap/2026-09-21_apollo11_landing_go_poll.md`

## Bounded question

What can be established about the Apollo 11 powered-descent 1201/1202 decision chain without importing later recollection as if it were contemporary procedure?

## Primary/contemporary result

The Apollo 11 air-to-ground record fixes the crew-facing end of the chain. After the first 1202, Armstrong asks Houston for a reading and CAPCOM answers that Eagle is GO on the alarm. Later, after the 1201, CAPCOM answers immediately that it is the same type and the crew is GO. These are operational GO calls, not merely acknowledgements of the alarm code.

The surviving controller-loop record fixes the front-room disposition: GUIDANCE/Steve Bales supplies the GO assessment to FLIGHT; FLIGHT accepts the disposition; CAPCOM relays it to Eagle. For the later 1201, the controller-loop sequence supports the compact `GUIDANCE: same type / GO → FLIGHT: GO → CAPCOM: same type / GO` chain.

NASA's archival account of Jack Garman identifies him as the back-room computer specialist supporting Bales and states that Bales called to Garman, who recognized 1202 as an overload warning compatible with continuing the landing. This establishes a support-room specialist role in the decision chain, but that later NASA historical account is not sufficient to manufacture exact 1969 back-room wording or a formalized message schema.

## Implementation consequence

The reference descent may model program alarms as:

`crew reports alarm → GUIDANCE evaluates with computer-specialist support → GUIDANCE recommends GO/abort to FLIGHT → FLIGHT owns disposition → CAPCOM relays operational disposition to crew`

For repeated alarms of the established executive-overflow family, the recorded 1201 exchange supports a shortened `same type / GO` response. Do not model `1201` and `1202` as automatically harmless: the documented operational judgment depended on the computer continuing to perform required guidance functions and on the alarm behavior, not merely the numeric code.

## Evidence boundary

- The air-to-ground transcript is primary for CAPCOM/crew speech.
- Controller-loop audio is primary for GUIDANCE→FLIGHT disposition where audible.
- NASA's Garman historical biography is authoritative institutional corroboration for Garman's support role but is retrospective, not a verbatim controller-loop transcript.
- Exact Garman→Bales words, the precise support-room loop topology used at each alarm, and a Mission-G CRT field that drove the alarm judgment are not claimed here.

## Next bounded target

Research the Apollo-11-effective **program-alarm GO/abort criterion itself**: recover contemporary mission-rule, guidance procedure, computer-alarm, or training documentation that states what conditions made an executive-overflow alarm acceptable versus abort-worthy. Keep this separate from later memoir descriptions.

## Sources

- NASA, *Apollo 11 Technical Air-to-Ground Voice Transcription (GOSS NET 1)*, July 1969: https://ntrs.nasa.gov/citations/20160014392
- Apollo 11 descent Flight Director/GUIDANCE controller audio preserved in the Apollo 11 mission audio archive.
- NASA History, `Apollo Era Hero John "Jack" Garman Dies` (2016), institutional retrospective identifying Garman's back-room support to Bales: https://www.nasa.gov/image-article/apollo-era-hero-john-jack-garman-dies/

## Evidence status

- **DOCUMENTED / PRIMARY TRANSCRIPT:** CAPCOM gives the crew GO on the first 1202 and later 1201.
- **DOCUMENTED / PRIMARY AUDIO:** GUIDANCE supplies the front-room GO assessment to FLIGHT; the later 1201 is treated as the same alarm type and GO.
- **DOCUMENTED / RETROSPECTIVE NASA:** Garman supported Bales from the back room and recognized the 1202 overload condition.
- **UNRESOLVED:** exact contemporary written GO/abort criterion and verbatim support-room exchange.