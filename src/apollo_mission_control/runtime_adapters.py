"""Runtime-adapter registry for scenario-specific session implementations.

A scenario fixture names an adapter. The registry maps that name to a builder
without making the web transport depend directly on a specific scenario class.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from .generic_runtime import GenericScenarioSession
from .pc2_session import PC2Session
from .scenario_catalog import ScenarioRecord, load_scenario_fixture
from .session_runtime import SessionRuntime


RuntimeBuilder = Callable[[ScenarioRecord], SessionRuntime]


@dataclass(frozen=True)
class RuntimeAdapter:
    adapter_id: str
    builder: RuntimeBuilder
    capabilities: frozenset[str]


def _build_pc2(record: ScenarioRecord) -> SessionRuntime:
    return PC2Session.create(load_scenario_fixture(record))


def _build_generic(record: ScenarioRecord) -> SessionRuntime:
    return GenericScenarioSession.create(load_scenario_fixture(record))


_ADAPTERS: dict[str, RuntimeAdapter] = {
    "generic_v1": RuntimeAdapter(
        adapter_id="generic_v1",
        builder=_build_generic,
        capabilities=frozenset(
            {
                "mission_control_core",
                "state_injection",
                "generic_timed_events",
            }
        ),
    ),
    "pc2_v1": RuntimeAdapter(
        adapter_id="pc2_v1",
        builder=_build_pc2,
        capabilities=frozenset(
            {
                "mission_control_core",
                "state_injection",
                "pc2_delta_p",
                "pc2_dps_shutdown",
                "pc2_inverter_transfer",
            }
        ),
    ),
}


def supported_runtime_adapters() -> frozenset[str]:
    return frozenset(_ADAPTERS)


def has_runtime_adapter(adapter_id: str) -> bool:
    return adapter_id in _ADAPTERS


def create_runtime(record: ScenarioRecord) -> SessionRuntime:
    adapter = _ADAPTERS.get(record.runtime_adapter)
    if adapter is None:
        raise ValueError(
            f"scenario {record.scenario_id} uses unsupported runtime adapter "
            f"{record.runtime_adapter!r}"
        )
    return adapter.builder(record)


def runtime_capabilities(adapter_id: str) -> frozenset[str]:
    adapter = _ADAPTERS.get(adapter_id)
    if adapter is None:
        return frozenset()
    return adapter.capabilities
