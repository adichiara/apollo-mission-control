"""Mission-neutral deterministic simulated flight-crew actor.

The actor separates:
1. transmitted CAPCOM instruction;
2. crew receipt/acknowledgement;
3. supported crew operational action;
4. source-backed procedures briefed before the active runtime interval;
5. downstream physical/subsystem response.

Rules are supplied by the scenario/runtime. No response delay, physical effect,
mission decision, or unrecorded live transmission is invented by this module.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from math import isfinite
from typing import Any, Mapping, Protocol, runtime_checkable


def _text(value: Any, name: str) -> str:
    result = str(value).strip()
    if not result:
        raise ValueError(f"{name} must not be empty")
    return result


def _finite(value: float, name: str) -> float:
    number = float(value)
    if not isfinite(number):
        raise ValueError(f"{name} must be finite")
    return number


@runtime_checkable
class CapcomInstructionLike(Protocol):
    item_id: int
    action: str
    parameters: dict[str, Any]
    basis: str
    transmitted: bool
    transmitted_get_s: float | None


@dataclass(frozen=True)
class CrewInstructionRule:
    """Scenario-supplied mapping from one CAPCOM action to one crew action."""

    capcom_action: str
    acknowledgement: str
    crew_action: str
    forwarded_parameters: tuple[str, ...] = ()
    provenance: str = "project-configured simulated crew rule"

    def validated(self) -> "CrewInstructionRule":
        forwarded: list[str] = []
        for raw in self.forwarded_parameters:
            name = _text(raw, "forwarded parameter")
            if name not in forwarded:
                forwarded.append(name)
        return CrewInstructionRule(
            capcom_action=_text(self.capcom_action, "capcom_action"),
            acknowledgement=_text(self.acknowledgement, "acknowledgement"),
            crew_action=_text(self.crew_action, "crew_action"),
            forwarded_parameters=tuple(forwarded),
            provenance=_text(self.provenance, "provenance"),
        )


@dataclass(frozen=True)
class CrewProcedureRule:
    """Scenario-supplied procedure already briefed before active runtime."""

    procedure_id: str
    crew_action: str
    parameters: Mapping[str, Any] = field(default_factory=dict)
    repeatable: bool = False
    provenance: str = "project-configured prebriefed crew procedure"

    def validated(self) -> "CrewProcedureRule":
        return CrewProcedureRule(
            procedure_id=_text(self.procedure_id, "procedure_id"),
            crew_action=_text(self.crew_action, "crew_action"),
            parameters=dict(self.parameters),
            repeatable=bool(self.repeatable),
            provenance=_text(self.provenance, "provenance"),
        )


@dataclass(frozen=True)
class CrewProcedureAction:
    action_id: str
    procedure_id: str
    crew_id: str
    get_s: float
    action: str
    parameters: dict[str, Any]
    provenance: str


@dataclass(frozen=True)
class CrewReceipt:
    capcom_item_id: int
    crew_id: str
    received_get_s: float
    capcom_action: str
    acknowledgement: str
    provenance: str


@dataclass(frozen=True)
class CrewOperationalAction:
    action_id: str
    capcom_item_id: int
    crew_id: str
    get_s: float
    action: str
    parameters: dict[str, Any]
    provenance: str


@dataclass
class SimulatedCrew:
    """Deterministic crew state for one exercise/runtime."""

    crew_id: str
    rules: Mapping[str, CrewInstructionRule]
    procedures: Mapping[str, CrewProcedureRule] = field(default_factory=dict)
    receipts: dict[int, CrewReceipt] = field(default_factory=dict)
    actions: dict[int, CrewOperationalAction] = field(default_factory=dict)
    procedure_actions: list[CrewProcedureAction] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.crew_id = _text(self.crew_id, "crew_id")

        normalized: dict[str, CrewInstructionRule] = {}
        for raw_key, raw_rule in self.rules.items():
            key = _text(raw_key, "crew rule key")
            rule = raw_rule.validated()
            if key != rule.capcom_action:
                raise ValueError(
                    f"crew rule key {key!r} does not match capcom_action "
                    f"{rule.capcom_action!r}"
                )
            normalized[key] = rule
        if not normalized:
            raise ValueError("at least one simulated crew rule is required")
        self.rules = normalized

        procedures: dict[str, CrewProcedureRule] = {}
        for raw_key, raw_rule in self.procedures.items():
            key = _text(raw_key, "crew procedure key")
            rule = raw_rule.validated()
            if key != rule.procedure_id:
                raise ValueError(
                    f"crew procedure key {key!r} does not match procedure_id "
                    f"{rule.procedure_id!r}"
                )
            procedures[key] = rule
        self.procedures = procedures

    def rule_for(self, item: CapcomInstructionLike) -> CrewInstructionRule:
        if not isinstance(item, CapcomInstructionLike):
            raise ValueError("CAPCOM item does not satisfy the instruction contract")
        rule = self.rules.get(str(item.action))
        if rule is None:
            raise ValueError(f"unsupported crew CAPCOM action: {item.action}")
        return rule

    def receive_instruction(
        self,
        item: CapcomInstructionLike,
        *,
        get_s: float,
    ) -> CrewReceipt:
        """Record bounded crew receipt; never performs the associated action."""

        rule = self.rule_for(item)
        if not item.transmitted:
            raise ValueError("crew cannot receive an untransmitted CAPCOM item")
        if item.transmitted_get_s is None:
            raise ValueError("transmitted CAPCOM item is missing transmitted_get_s")

        received_get_s = _finite(get_s, "received get_s")
        if received_get_s < float(item.transmitted_get_s):
            raise ValueError("crew receipt cannot precede CAPCOM transmission")
        if item.item_id in self.receipts:
            raise ValueError(f"crew receipt already recorded for item {item.item_id}")

        receipt = CrewReceipt(
            capcom_item_id=int(item.item_id),
            crew_id=self.crew_id,
            received_get_s=received_get_s,
            capcom_action=rule.capcom_action,
            acknowledgement=rule.acknowledgement,
            provenance=rule.provenance,
        )
        self.receipts[item.item_id] = receipt
        return receipt

    def perform_prebriefed_procedure(
        self,
        procedure_id: str,
        *,
        get_s: float,
    ) -> CrewProcedureAction:
        """Create a crew action from an explicitly configured prior briefing.

        This path deliberately has no live CAPCOM receipt stage. It is for
        procedures whose source record establishes that the crew had already
        received the instruction before the active runtime interval.
        """

        key = _text(procedure_id, "procedure_id")
        rule = self.procedures.get(key)
        if rule is None:
            raise ValueError(f"unsupported prebriefed crew procedure: {key}")

        prior = [
            action
            for action in self.procedure_actions
            if action.procedure_id == key
        ]
        if prior and not rule.repeatable:
            raise ValueError(f"prebriefed crew procedure already performed: {key}")

        action_get_s = _finite(get_s, "crew procedure get_s")
        action = CrewProcedureAction(
            action_id=f"crew-procedure-{key}-{len(prior) + 1}",
            procedure_id=key,
            crew_id=self.crew_id,
            get_s=action_get_s,
            action=rule.crew_action,
            parameters=dict(rule.parameters),
            provenance=rule.provenance,
        )
        self.procedure_actions.append(action)
        return action

    def perform_supported_action(
        self,
        item: CapcomInstructionLike,
        *,
        get_s: float,
    ) -> CrewOperationalAction:
        """Create a crew action after receipt, without applying physical effects."""

        rule = self.rule_for(item)
        receipt = self.receipts.get(item.item_id)
        if receipt is None:
            raise ValueError("crew receipt must be recorded before crew action")
        if item.item_id in self.actions:
            raise ValueError(f"crew action already recorded for item {item.item_id}")

        action_get_s = _finite(get_s, "crew action get_s")
        if action_get_s < receipt.received_get_s:
            raise ValueError("crew action cannot precede crew receipt")

        parameters: dict[str, Any] = {}
        for name in rule.forwarded_parameters:
            if name not in item.parameters:
                raise ValueError(
                    f"CAPCOM item {item.item_id} is missing required parameter {name!r}"
                )
            parameters[name] = item.parameters[name]

        action = CrewOperationalAction(
            action_id=f"crew-{rule.crew_action}-{item.item_id}",
            capcom_item_id=int(item.item_id),
            crew_id=self.crew_id,
            get_s=action_get_s,
            action=rule.crew_action,
            parameters=parameters,
            provenance=rule.provenance,
        )
        self.actions[item.item_id] = action
        return action
