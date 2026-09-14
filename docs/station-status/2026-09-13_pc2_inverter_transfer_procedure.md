# Station Research Status — PC+2 inverter transfer procedure

Date: 2026-09-13

## CAPCOM / crew boundary

**Status:** source-sufficient for first-playable transfer action.

After an INVERTER caution while PC+2 is operating on inverter 2, the Apollo 13 LM Malfunction Procedures support an ordered crew transfer to inverter 1: close `CB(11) EPS: INV 1`, set `INVERTER` to `1`, then open `CB(16) EPS: INV 2`, followed by re-observation of the caution state.

CAPCOM remains the ground-to-crew communication boundary. Exact spoken wording and crew-member assignment are not recovered.

## TELMU / CONTROL

**Status:** rule/action semantics source-sufficient; exact display routing remains partial.

TELMU/CONTROL may reason from the inverter caution and subsequent fresh evidence, but the project still does not claim independent ground visibility of the cockpit selector position or a recovered exact telemetry/CRT field for it.

## First-playable consequence

The transfer procedure is no longer an unnamed generic action. It may be represented as the sourced three-control crew sequence. No numeric post-switch dwell or automatic shutdown is authorized.
