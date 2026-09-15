# Research note 156 — PC+2 final P30 pad trim-omission boundary

Date: 2026-09-15

## Question

Did the final ~78-hour PC+2 P30 LM maneuver PAD contain a superseding commanded GDA trim pair, as the current roadmap target assumed?

## Primary evidence

### Apollo 13 technical air-to-ground transcription — GET 077:55:24

NASA mission transcription preserves Vance Brand's final PC+2 P30 LM maneuver PAD read-up. The transmitted fields were:

- Noun 33 / TIG: `079:27:38.30`;
- Noun 81: `+0833.0, -0050.9, -0213.9` ft/s;
- HA: N/A;
- HP: `+0020.5` nmi;
- resultant delta-V: `0861.5` ft/s;
- burn time: `4:24`;
- attitude: `272, 081`;
- Brand then states **"the rest is N/A except for comments"**;
- comments: two-jet 10-second ullage, CSM weight `62480`, LM weight `33452`, and the DPS throttle profile.

Haise's readback likewise gives the numerical fields and says the rest is N/A. Brand confirms the readback after the weak-link repetition.

Source: NASA Apollo 13 technical/PAO air-to-ground transcription, preserved through the Apollo Flight Journal document collection and corrected transcript.

Navigation: https://www.apollojournals.org/afj/ap13fj/13day4-leaving-moon.html
NASA transcript PDF: https://www.nasa.gov/wp-content/uploads/static/history/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf

## Finding

The final transmitted P30 LM maneuver PAD at GET 077:55:24 **did not transmit a GDA trim pair**. Therefore the previous roadmap formulation — "recover the final ~78-hour PC+2 P30/GDA pad" — incorrectly implied that the final P30 pad itself should contain the missing superseding trim.

This is a negative but useful primary-source result. It narrows the missing artifact class.

## What this does not prove

Do **not** infer that:

- no final/superseding commanded trim existed;
- the ~59-hour `5.86° / 6.75°` interim pair remained active;
- the final trim was generated onboard rather than on the ground;
- the observed pre-ignition GDA state was itself the commanded trim;
- the P30 form could never carry GDA data in other circumstances;
- the final trim had any particular mass-properties job or `T+55` provenance.

The earlier ~59-hour pair was explicitly update-expected and later execution evidence proves supersession of at least the roll value. The absence of GDA fields from the final 077:55 P30 read-up therefore shifts the search away from that pad and toward CONTROL/Flight Dynamics working products, GDA setup/checklist traffic, telemetry/strip-chart records, Flight Director logs, and mass-properties job output.

## Simulation implication

Treat the final maneuver targeting PAD and the engine-trim product as **separate operational products**. A PC+2 scenario should not require a final P30 PAD object to carry GDA trim merely because the earlier contingency read-up included GDA angles.

For provenance, preserve:

`mass-properties state/job -> derived trim product -> GDA setup/verification -> observed execution state`

separately from:

`trajectory solution -> P30 maneuver PAD -> crew P30 load/readback`.

## Next archival target

Search H-2 CONTROL/Flight Dynamics working sheets, Flight Director logs, GDA setup/checklist records, and mass-properties job output between approximately GET 59 and ignition for the superseding commanded angular trim and its provenance. The final 077:55 P30 PAD itself is no longer an expected source for that value.