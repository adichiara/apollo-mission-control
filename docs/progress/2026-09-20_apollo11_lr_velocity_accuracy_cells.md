# Progress — Apollo 11 landing-radar velocity accuracy cells

Date: 2026-09-20

## Work completed

The previous pass recovered the LSP-470-2D range limits but deliberately left the velocity table unencoded because OCR column alignment was uncertain. The NASA-hosted primary-source extraction for NTRS 19700004489 was rechecked against exact cell phrases and the altitude/component matrix can now be transcribed without inventing values.

The table labels velocity accuracy to the LGC as **3 sigma** and gives:

| Altitude | Vx | Vy | Vz |
| --- | --- | --- | --- |
| 25,000–2,000 ft | 1.5% or 1.5 ft/s | 2.0% or 2.0 ft/s | 2.0% or 2.0 ft/s |
| 2,000–200 ft | 1.5% or 1.5 ft/s | 3.5% or 3.5 ft/s | 3.0% or 3.0 ft/s |
| 200–5 ft | 1.5% or 1.5 ft/s | 2.0% or 1.5 ft/s | 2.0% or 1.5 ft/s |

The table footnotes state that the percentage is of vector velocity and to use the percentage or ft/s value, whichever is greater.

## Result

The quantitative landing-radar **performance envelope** is now closed at component/altitude-cell level. This is sufficient to implement source-controlled validation bounds if needed.

It does not resolve historical stochastic behavior. The 3-sigma terminology remains an acceptance/specification expression; NASA TN D-6849 separately warns that the Doppler-spectrum simulator's Gaussian assumption required correction because the approximation put more energy in the tails. No Gaussian or other probability distribution is inferred.

## Documentation synchronized

- focused landing-radar roadmap;
- landing-radar station research status;
- Apollo 11 / Luminary 1A source catalog;
- this progress record.

## Next discriminating evidence

Continue seeking LM-5 qualification/acceptance or Apollo 11 flight-data reduction evidence for actual bias, correlation, quantization, dropout, or distribution behavior. Separately, the higher-level MSK-1137 per-field D/L-versus-RTCC routing and GUIDO console-workflow gaps remain unresolved.

## Evidence status

**DOCUMENTED PERFORMANCE ENVELOPE; STOCHASTIC PROCESS UNRESOLVED/BLOCKED.** Exact altitude/component acceptance cells are now source-controlled. No unsupported historical random-error model has been introduced.
