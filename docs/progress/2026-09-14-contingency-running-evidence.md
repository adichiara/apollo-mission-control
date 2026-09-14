# PC+2 contingency validation follow-up — 2026-09-14

## Live result

A guided live contingency run progressed successfully through the core response chain:

1. synthetic 26 psi DPS fuel/oxidizer ΔP injected,
2. CONTROL shutdown callout recorded,
3. CAPCOM item queued and transmitted,
4. crew receipt recorded,
5. crew DPS shutdown commanded,
6. physical DPS engine-off response recorded,
7. crew shutdown report recorded.

The nominal guided-cutoff event was then correctly marked MISSED because the DPS engine was already off.

## Two test-harness defects found

### Paused setup was incompatible with controller/crew actions

The guided page intentionally paused at GET 79:29, but the session API requires RUNNING state for the command chain. The tester therefore had to resume manually. The guided setup now leaves the session RUNNING and positions the test slightly earlier, at GET 79:28:15, providing about 3m47s before nominal cutoff.

### Final corroboration lacked a fresh ground observation

The shutdown-evidence model requires both a post-command crew report and a fresh post-command ground chamber-pressure observation for `corroborated` state. The network smoke test already supplies a synthetic fresh 100 psi chamber-pressure sample specifically to prove that no engine-off pressure threshold is being inferred. The guided page did not include that required observation.

Step 7 now records both the crew shutdown report and the same kind of explicitly synthetic fresh chamber-pressure observation. The 100 psi value remains deliberately high and is used only to establish observation freshness, not as a binary engine-off criterion.

## Scope

Validation UI only. No scenario timing, controller authority, historical claims, or simulation rules changed.