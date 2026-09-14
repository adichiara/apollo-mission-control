# Station-status addendum — PC+2 inverter TELMU indicator continuity

Date: 2026-09-14

## TELMU

**Maturity:** unchanged.

New primary continuity evidence strengthens the station assignment for inverter-bus electrical evidence:

- SA-204/LM-1 documentation already treats `GC0071V` and `GC0155F` as ground display/telemetry products.
- Apollo 15 PHO-TR155 identifies console 09 as LM TELMU and places `GC0071V * AC BUS V` and `GC0155F * AC BUS F` on TELMU module-05 operational indicators.

For Apollo 13 first playable, TELMU may therefore own the project-rendered inverter voltage/frequency product with stronger historical support than a generic TELMU/CONTROL assignment.

### Boundary

Do not reproduce Apollo 15 module-05 positions 07/16 as Apollo 13 facts. Exact AS-508 TELMU indicator loading, PC+2 CRT/MSK use, live sample cadence, display request, precision, refresh, and latency remain unresolved.

## CONTROL

**Maturity:** unchanged.

No reviewed source establishes a corresponding direct CONTROL operational indicator for `GC0071V` or `GC0155F`. CONTROL retains propulsion/guidance/control responsibilities already documented; inverter electrical evidence should not be duplicated there as a recovered historical product without additional primary evidence.

## Research record

- `resources/research/121_pc2_inverter_telmu_indicator_continuity_boundary.md`
- `resources/source-catalog/PC2_INVERTER_TELEMETRY_PRESENTATION_SOURCES.md`
