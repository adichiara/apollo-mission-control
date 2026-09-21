# Progress — Apollo 11 landing-radar 15-bit word-length closure

Date: 2026-09-21

## Research target

Resolve the next open landing-radar interface question: Apollo-11-effective raw LR/LGC serial word length. Keep bit order, serial sign representation/bias, and rounding/truncation separate unless primary evidence actually resolves them.

## Primary evidence recovered

A mission-specific Apollo 11 engineering note explaining the LGC 520 alarm observed when the DSKY circuit breaker was closed describes the radar-read hardware sequence directly. It states that the sequence consists of an 80-ms gate, a 5-ms delay, **15 readout pulses at 3200 pps**, and then a radar interrupt pulse. The same note explains the relationship to the LGC radar-read routine and `SAMPLIN`.

Source: `https://www.ibiblio.org/apollo/Documents/apollo_11_520_alarm.pdf`.

This is the missing Apollo-11 applicability bridge for the 15-bit/raw-read boundary. It is mission-specific evidence rather than a later LM-6 back-projection.

AC Electronics ND-1021042 independently describes the generic LGC radar-control hardware: radar input arrives as `RRIN1/RRIN0` or `LRIN1/LRIN0` under sync, and after **15 pulses** have been received the radar control terminates sync generation and requests `RUPT9`. This is consistent with the Apollo 11 note and supplies the interface-mechanism context.

## Controlled conclusion

The Apollo 11 LR/LGC raw transfer may now be documented as a **15-pulse serial binary word/readout**. The repository no longer needs to label raw word length as adjacent-effectivity only.

This does **not** resolve:

- serial bit order;
- the representation/polarity of velocity sign in the 15-bit word;
- any integer bias applied to raw velocity data;
- rounding versus truncation in the Signal Data Converter;
- controller visibility of any of those details.

The earlier NASA TN D-6849 result remains important: velocity sign is determined upstream in the measurement pulse-train path. The present evidence only closes transfer length.

## Documentation updated

- `docs/roadmap/2026-09-19_apollo11_landing_radar_beam_transform.md`
- `docs/station-status/2026-09-20_apollo11_lr_scale_selection.md`
- `resources/APOLLO11_LR_SCALE_SELECTION_SOURCE_CATALOG_ADDENDUM.md`

## Next target

Seek LM-5/Apollo-11-effective Signal Data Converter or LGC interface evidence for **serial bit order and sign/bias representation**. Treat rounding/truncation as a separate unresolved conversion question.

## Evidence status

- **DOCUMENTED, APOLLO-11-SPECIFIC:** radar read sequence contains 15 readout pulses at 3200 pps followed by RADARUPT.
- **CORROBORATED, PRIMARY INTERFACE:** ND-1021042 terminates radar sync and requests RUPT9 after 15 received radar pulses.
- **RESOLVED:** Apollo 11 raw LR/LGC serial transfer length = 15 pulses/bits.
- **UNRESOLVED:** bit order, serial sign representation/bias, and rounding/truncation.
