# Station research status — PC+2 inlet-pressure rule lineage

Date: 2026-09-13

## CONTROL

Status remains **B / first-playable sufficient with bounded historical gaps**.

New evidence:

- Apollo 13 PC+2 rule read-up explicitly traces the shutdown philosophy to LOI Mode I abort with tight limits.
- Apollo 10 DPS mission rules identify the relevant high-throttle criterion as **fuel inlet pressure <150 psi**.
- LM-7-family telemetry identifies `GQ3611P` as engine-interface fuel pressure and `GQ4111P` as engine-interface oxidizer pressure.

Interpretation:

- `GQ3611P` is now the leading source-backed candidate for the ground 150-psi criterion.
- Apollo 13-specific CONTROL display/routing or mission-rule evidence has not yet been recovered to make that mapping definitive.
- The 150-psi criterion therefore remains `NOT_EVALUABLE` in the executable model.
- No combined inlet-pressure telemetry product may be invented.

No change to CONTROL player authority, presentation, or current first-playable PASS status is warranted from this research alone.

## Other stations

No station-maturity change. The crew-side 160-psi criterion remains distinct from the unresolved ground mapping; CAPCOM's sourced rule read-up is unchanged.
