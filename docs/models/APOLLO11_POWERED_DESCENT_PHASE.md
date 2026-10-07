# Apollo 11 Powered-Descent Phase Skeleton

Status: **implemented nominal phase/event contract; not a continuous flown trajectory**

## Purpose

Provide a deterministic Apollo 11 powered-descent phase state for architecture/runtime work without inventing unsupported continuous thrust or trajectory history.

Implementation:

- `src/apollo_mission_control/powered_descent_phase.py`
- `src/apollo_mission_control/powered_descent_profiles.py`
- `data/powered_descent_profiles/apollo11_g_powered_descent_phase_skeleton.json`

## Source boundary

The phase state is driven only by nominal mission-plan anchors:

- PDI / start of braking: TFI 0 s;
- high gate / approach: nominal TFI 8:24 = 504 s, approximately 7,600 ft;
- low gate / landing: nominal TFI 10:08 = 608 s, approximately 500 ft;
- planned touchdown: nominal TFI 11:58 = 718 s.

The Flight Plan also marks fixed-throttle operation, landing-radar updates, throttle recovery, and radar velocity update. Where this repository does not carry a controlled numerical time for those events, the profile preserves them as **untimed nominal events** rather than assigning a guessed timestamp.

## Flown observations remain separate

The Apollo 11 Mission Report supplies flown/postflight propulsion observations:

- powered descent firing duration: 756.3 s;
- delta-V: approximately 6,775 ft/s;
- initial DPS throttle: 13 percent;
- advance to full throttle: approximately PDI +26 s;
- approximately 45 s of early propulsion data were lost.

These observations are returned with the phase snapshot but **never drive phase selection**.

That distinction is intentional. For example, TFI 730 s is after the Flight Plan's nominal touchdown anchor while still earlier than the reported 756.3 s flown firing duration. The model preserves both facts instead of reconciling them into an invented history.

## Phase semantics

The generic phases are:

`PRE_PDI -> BRAKING -> APPROACH -> LANDING -> POST_PLANNED_TOUCHDOWN`

This is an architecture/runtime skeleton. `POST_PLANNED_TOUCHDOWN` means only "after the nominal planned touchdown anchor." It does not assert that the spacecraft had actually landed at that elapsed time.

## Site-facing proof

The Causal Model Lab exposes:

`/api/admin/model-proof/powered-descent-phase`

The proof displays the selected nominal phase, most-recent/next nominal anchor, and the separate flown propulsion observations.

## Deliberately not implemented here

- continuous six-degree-of-freedom descent trajectory;
- continuous historical DPS thrust reconstruction;
- interpolation through the documented early propulsion-data gap;
- automatic P66/manual-takeover timing;
- controller-visible phase products not separately sourced;
- automatic GO/NO-GO or abort decisions.

The descent decision gate, controller-product schema, landing-radar estimator, and program-alarm model remain separate domains and should be composed explicitly when the bounded Apollo 11 runtime is assembled.

## Sources

- NASA, *Apollo 11 Flight Plan, AS-506, CSM-107/LM-5*, final, 1 July 1969.
- NASA, *Apollo 11 Mission Report*, MSC-00171, November 1969, section 9.8.
- NASA, *Apollo 11 AS-506 Mission Operation Report*, M-932-69-11, 24 June 1969.
