# Roadmap addendum — PC+2 inverter onboard/ground monitoring boundary

Date: 2026-09-14

## Closed in this pass

Research note 122 closes one operational ambiguity left after note 121: **PC+2 inverter verification was not exclusively a ground-display task.**

Mission-specific Apollo 13 transcript evidence shows that the activation read-up explicitly had the crew:

1. power the EPS display;
2. select the Power/Temp Monitor to AC BUS;
3. compare **inverter 2, then inverter 1**;
4. continue into the mission-specific inverter configuration.

Post-burn, caution-and-warning power was deliberately retained through the immediate transition to PTC, while later reduced-power operation retained telemetry even as local displays were reduced.

## Canonical first-playable boundary

```text
crew-local path:
selected inverter / AC bus
    → onboard Power/Temp Monitor / caution-and-warning
    → crew observation
    → crew report/action via CAPCOM

parallel ground path:
inverter bus
    → GC0071V + GC0155F
    → PCM/MSFN/MCC
    → TELMU electrical evidence
    [exact Apollo 13 presentation unresolved]
```

Do not collapse these paths into one omniscient product.

## Next unresolved archival target

The highest-value remaining target stays unchanged but is now more tightly scoped:

1. recover **Apollo 13 PHO-TR155 Revision C / Mission H-2 MCC Operational Configuration** or equivalent TELMU console-loading sheets;
2. identify whether `GC0071V` / `GC0155F` were physical operational indicators, CRT fields, strip-chart channels, or some combination during AS-508;
3. recover exact live normal-format cadence and display/indicator routing;
4. only then freeze Apollo 13 TELMU presentation details.

If the configuration document remains unavailable, search Apollo 13 TELMU console handbooks/logs, MOC loading sheets, and display-request inventories before using later-mission coordinates or sample rates.

## Unchanged validation priorities

- seven-seat physical nominal run;
- synthetic ΔP branch physical run;
- five-player compact physical run.

No physical PASS boundary is changed by this research-only refinement.
