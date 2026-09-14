# Apollo 13 PC+2 — inverter onboard/ground monitoring boundary

Date: 2026-09-14  
Status: **REVIEWED / PARTIALLY RESOLVED — mission-specific Apollo 13 transcript evidence establishes explicit onboard inverter comparison before PC+2 and continued telemetry-dependent monitoring after the burn; exact TELMU indicator/CRT loading remains unresolved.**

## Question

Research note 121 strengthened TELMU as the station-family owner for inverter-bus electrical telemetry but left actual PC+2 use unresolved. The next question is:

> During the flown PC+2 sequence, what inverter evidence was explicitly crew-local versus available to Mission Control, and can that boundary be established without inventing an Apollo 13 TELMU display layout?

## Primary mission-specific evidence

### Apollo 13 Mission Commentary / air-to-ground transcript

The surviving Apollo 13 mission transcript records the PC+2 activation read-up at approximately 74:55 GET. CAPCOM directs the crew to:

- close the EPS display circuit breaker;
- use **POWER/TEMP MONITOR — AC BUS**;
- check **INVERTER 2, then INVERTER 1**;
- continue with the mission-specific inverter configuration changes.

This is direct operational evidence that the crew's pre-PC+2 electrical verification included a local spacecraft display/meter comparison of the two inverter selections. It is not merely an inferred ground-telemetry task.

The same mission transcript records the immediate post-PC+2 powerdown. At about 79:51–79:56 GET the crew removes the bus-tie inverters from the line, pulls inverter 1, and asks whether caution-and-warning power can also be shut down. CAPCOM directs that caution and warning remain powered until PTC is established.

Later, during the deeper powerdown, CAPCOM describes the remaining spacecraft functions as including **low-bit-rate telemetry** while multiple local display functions are being powered down. Elsewhere in the mission transcript, Mission Control explicitly requests high-bit-rate telemetry when it needs additional LM diagnostic data and then returns the spacecraft to low bit rate after the check. This confirms that telemetry availability and local display availability were separable operational resources.

## Sources inspected

### Primary

- NASA / Manned Spacecraft Center, *Apollo 13 Mission Commentary*, April 1970.
- Apollo Flight Journal high-resolution archival scan:
  https://apollojournals.org/afj/ap13fj/pdf-hr/a13-pao-transcript.pdf
- Relevant transcript locations:
  - PDF p. 379: PC+2 activation; EPS display close; POWER/TEMP MONITOR AC BUS, inverter 2 then inverter 1.
  - PDF p. 430: post-burn caution-and-warning retention discussion.
  - PDF p. 457: low-bit-rate telemetry retained in the later powerdown configuration.

### Corroborating mission transcript index

- Apollo 13 Flight Journal, mission documents:
  https://apollojournals.org/afj/ap13fj/a13-documents.html

## Interpretation

The PC+2 inverter information path was operationally redundant in a useful way:

```text
crew-local path
selected inverter / AC bus
    → onboard Power/Temp Monitor / caution-and-warning
    → crew observation
    → crew report / action

and

ground path
selected inverter bus electrical condition
    → GC0071V / GC0155F instrumentation
    → PCM / MSFN telemetry
    → MCC processing
    → TELMU electrical evidence
    [exact Apollo 13 presentation unresolved]
```

The primary transcript therefore rules out a first-playable design in which inverter verification is exclusively a TELMU-ground-display event. The crew had an explicit onboard electrical comparison task during activation.

Conversely, the transcript does **not** identify an Apollo 13 TELMU module, operational-indicator coordinate, MSK, display-request number, refresh rate, or latency for `GC0071V` / `GC0155F`.

## First-playable consequence

Preserve two distinct evidence channels:

1. **crew-local electrical/caution evidence**
   - represented through crew action/report state at the CAPCOM boundary;
   - may include the sourced preburn inverter-2/inverter-1 Power/Temp Monitor comparison;
   - does not become a hidden automatic TELMU diagnosis.

2. **ground telemetry evidence**
   - `GC0071V` inverter-bus voltage and `GC0155F` inverter-bus frequency remain source-backed TELMU electrical evidence;
   - exact Apollo 13 presentation remains project-rendered and must be labeled accordingly.

For an injected inverter anomaly, a controller should be able to encounter disagreement or timing differences between crew-local indication/report and ground electrical telemetry if the authored observation fault explicitly produces that condition. Do not synthesize such disagreement randomly.

## What this resolves

- PC+2 activation included an explicit onboard AC-bus/inverter comparison: **inverter 2 then inverter 1**.
- Caution-and-warning availability was deliberately retained through the immediate post-burn/P​​TC transition rather than assumed continuously powered or immediately removed.
- Telemetry remained an operational monitoring resource during later reduced-power configurations even as local display functions were reduced.
- The first playable should model onboard crew evidence and ground TELMU evidence as separate information paths.

## What remains unresolved

- exact Apollo 13 TELMU operational-indicator loading for `GC0071V` / `GC0155F`;
- exact Apollo 13 CRT/MSK or display-request use for those measurements;
- live normal-format sample cadence, field precision, refresh, and latency;
- whether TELMU used a physical indicator, CRT product, strip chart, or a combination during the PC+2 interval;
- whether CONTROL had any direct equivalent presentation;
- exact crew meter reading values during the preburn inverter comparison;
- any direct telemetered caution/selector discrete beyond the voltage/frequency paths already documented.

## Next archival target

Continue prioritizing the missing Apollo 13 **PHO-TR155 Revision C / Mission H-2 MCC Operational Configuration** or equivalent console-loading sheets. Research note 012 already establishes that this mission-specific configuration document was issued on 1970-03-06. A surviving TELMU console-09 sheet is the most direct route to closing the remaining presentation question.

If that document remains unavailable, next-best evidence is an Apollo 13 TELMU console handbook/log, MOC loading sheet, or display-request inventory that names `GC0071V` / `GC0155F`.

## Project consequence

No station maturity grade or physical-validation PASS state changes. This note refines the information architecture: **PC+2 inverter verification is not a single ground-only product.** Crew-local Power/Temp Monitor and caution/warning evidence must remain distinct from TELMU telemetry evidence, while the exact AS-508 TELMU presentation remains intentionally unfrozen.
