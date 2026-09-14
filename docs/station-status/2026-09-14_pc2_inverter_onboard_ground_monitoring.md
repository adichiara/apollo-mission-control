# Station-status addendum — PC+2 inverter onboard/ground monitoring boundary

Date: 2026-09-14

## TELMU

**Maturity:** unchanged.

Research note 122 adds Apollo-13-specific operational context to the inverter telemetry work:

- the crew performed an explicit onboard AC-bus comparison on inverter 2 and inverter 1 during PC+2 activation;
- this local verification path was distinct from MCC telemetry;
- later reduced-power operation retained telemetry while some onboard displays were removed.

TELMU remains the strongest source-backed station-family owner for project-rendered `GC0071V` / `GC0155F` electrical evidence. Exact AS-508 physical indicator/CRT loading remains unresolved.

### Boundary

Do not turn the crew's Power/Temp Monitor reading or onboard INVERTER caution into direct TELMU telemetry. Ground evidence remains the documented inverter-bus voltage/frequency path unless a mission-specific routing source proves more.

## CAPCOM / crew boundary

**Maturity:** unchanged; evidence path clarified.

The PC+2 activation transcript establishes a concrete crew-local inverter-verification action. In first playable, crew observation/report is therefore a legitimate separate information channel at the CAPCOM boundary rather than an inferred duplicate of TELMU telemetry.

This remains consistent with D-021: CAPCOM transmission, crew receipt/action, physical response, telemetry, and crew report stay separate.

## CONTROL

**Maturity:** unchanged.

No new evidence establishes a direct CONTROL presentation of `GC0071V`, `GC0155F`, the onboard caution, or inverter selector position.

## Research record

- `resources/research/122_pc2_inverter_onboard_ground_monitoring_boundary.md`
- `resources/source-catalog/PC2_INVERTER_TELEMETRY_PRESENTATION_SOURCES.md`
