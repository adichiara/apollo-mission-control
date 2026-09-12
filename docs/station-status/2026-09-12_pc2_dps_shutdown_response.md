# Station research-status addendum — DPS shutdown command / physical response

Date: 2026-09-12

## CONTROL

**Maturity remains B.**

Improved:

- the crew shutdown command is no longer collapsed into physical engine state;
- a separate source-backed engine-off vehicle response now exists;
- later CONTROL confirmation can therefore depend on telemetry/product updates rather than hidden command state.

Still unresolved:

- exact controller-visible shutdown confirmation field/route;
- exact LM-7 shutdown transient timing;
- exact GQ6510P pressure decay after STOP command.

## CAPCOM / crew boundary

**Maturity remains B.**

Improved:

- contemporary LM control documentation supports refining the crew shutdown action to the descent-engine STOP pushbutton;
- either crew STOP pushbutton could initiate the engine-off command in the documented LM control architecture.

Still unresolved:

- which crew member would press STOP in the hypothetical PC+2 ΔP contingency;
- any exact spoken confirmation after the action.

## FLIGHT

**Maturity remains B.**

The architecture can now distinguish a crew command from confirmed physical shutdown. FLIGHT therefore need not treat a transmitted shutdown instruction or crew action as proof that the engine has actually stopped.

## Research stop

Do not pursue exact valve timing or pressure-tailoff behavior unless the next controller-confirmation implementation requires it.
