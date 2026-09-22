# Roadmap continuation — Apollo 11 P66 manual-landing monitoring

Date: 2026-09-21
Parent: `docs/roadmap/2026-09-21_apollo11_descent_propellant_countdown.md`

## Bounded question

Once Apollo 11 entered P66/manual landing, what remained controller-visible and what decision authority changed?

## Primary-source result

NASA TM X-58038, *Development of Guidance-Monitoring Techniques and Guidance-Monitoring Experience During the Apollo 11 Lunar Descent* (1970), explicitly defines the descent guidance-monitoring job as evaluation of LM PGNS and AGS for descent-abort and guidance-switchover decisions. It describes three independent navigation references — PGNS, AGS, and a ground track based on MSFN data — and says the comparisons were generated in component form and displayed on analog recorders.

For terminal descent, the same report states that the approach phase was operationally considered complete at about 500 ft, where the pilot normally assumed manual control for final touchdown-point selection and landing. Its Apollo 11 plots mark **P66 initiation** as the point at which the pilot assumed manual control. The report continues to plot/compare the actual trajectory after that event; manual takeover therefore did not make ground monitoring disappear.

The Apollo 11 Mission Report independently records P66/manual takeover at about 102:43:22 GET and documents the subsequent landing-radar-data loss near 102:44:11. The contemporary descent record continues to carry altitude, altitude-rate, horizontal-velocity, PGNS/AGS, radar-validity, and propellant information through the landing phase.

The already-recovered Apollo 11 Flight Mission Rule 5-91 supplies the crucial decision boundary: after crew takeover, trajectory/guidance constraints are not themselves abort causes. Thus **observation continuity is not the same as decision-authority continuity**.

## Simulator implication

Preserve this transition explicitly:

`automatic P64 guidance + ground comparison/decision monitoring → P66/manual crew control + continued ground observation/comparison → advisory/controller assessment + independent systems/propellant abort criteria`

P66 must not be implemented as either:

- loss of ground visibility; or
- permission for ground trajectory-limit logic to command an abort automatically.

GUIDANCE/FLIGHT can continue to receive and assess sourced navigation/trajectory evidence after P66. But once manual takeover occurs, a trajectory departure by itself must not be promoted into an abort trigger contrary to rule 5-91. Other independently sourced abort causes remain separate.

## Player-visible boundary

A future Apollo 11 runtime should expose a discrete **crew manual-control/P66 state** to the decision layer. That state changes how trajectory-rule evaluations are interpreted without erasing the underlying observations. The exact Mission-G CRT field or internal signal by which the ground knew P66 entry is not established here and must not be invented.

The crew-facing transcript and Mission Report support the actual sequence around manual takeover, but they do not establish a unique GUIDANCE voice call announcing P66. Do not add one without loop evidence.

## Next

This bounded dependency is **SUFFICIENT** for current architecture. The next Apollo 11 powered-descent work should connect the manual-control state to the existing reusable descent decision-gate/model-lab proof, keeping observation state and decision authority separate. Historical display/keying detail remains optional unless it becomes player-decision critical.

## Sources

- NASA, H. G. de Vezin Jr. et al., *Development of Guidance-Monitoring Techniques and Guidance-Monitoring Experience During the Apollo 11 Lunar Descent*, NASA TM X-58038, 1970: https://ntrs.nasa.gov/citations/19700023940
- NASA, *Apollo 11 Mission Report*, MSC-00171, November 1969: https://ntrs.nasa.gov/citations/19700008096
- NASA, *Apollo 11 Technical Air-to-Ground Voice Transcription (GOSS NET 1)*, July 1969: https://ntrs.nasa.gov/citations/20160014392
- Apollo 11 Flight Mission Rules, rule 5-91, as bounded in `docs/roadmap/2026-09-21_apollo11_descent_trajectory_rules.md`.

## Evidence status

- **DOCUMENTED / PRIMARY:** ground descent monitoring compared PGNS, AGS, and MSFN-derived ground tracking for guidance/abort assessment.
- **DOCUMENTED / PRIMARY:** P66 marks crew assumption of manual landing control at roughly the 500-ft terminal-descent boundary; Apollo 11 entered it at about 102:43:22 GET.
- **DOCUMENTED / PRIMARY:** ground/crew-relevant observations continued after P66, including a later landing-radar-data loss.
- **DOCUMENTED / MISSION RULE:** after crew takeover, trajectory/guidance constraints are not themselves abort causes.
- **UNRESOLVED BUT NOT REQUIRED:** exact Mission-G ground indication/CRT field for P66 entry and any station-specific voice call announcing it.