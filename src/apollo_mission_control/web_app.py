"""Thin FastAPI transport for the Apollo Mission Control simulator.

The simulation/domain layer remains framework-neutral. Scenario-specific
sessions are constructed through the runtime-adapter registry. This module owns only
HTTP request/response adaptation, an in-memory single-session registry, realtime
wall-clock pacing, facilitator authorization, and static prototype delivery.
"""

from __future__ import annotations

import hmac
import os
from pathlib import Path
from threading import RLock
from typing import Any, Callable

from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from .causal_dps_model import (
    BurnSegment,
    DPSModelConfig,
    ManeuverState,
    simulate_dps_maneuver,
)
from .causal_translational_model import (
    TranslationalConfig,
    TranslationalState,
    simulate_translational_maneuver,
)
from .controller_products import project_controller_products
from .crew_response import (
    apply_session_engine_off_response,
    apply_session_restart_response,
    command_dps_shutdown_from_callout,
    perform_inverter_transfer_from_callout,
    perform_prebriefed_pc2_restart_procedure,
    record_crew_receipt,
    record_inverter_transfer_completion_report,
    record_premature_dps_stop,
)
from .electrical_power_model import (
    ElectricalBusConfig,
    ElectricalBusState,
    ElectricalLoadSpec,
    ElectricalSourceSpec,
    evaluate_electrical_bus,
)
from .guidance_computer_model import (
    GuidanceComputerConfig,
    GuidanceComputerState,
    ProgramAlarmEvent,
    ProgramAlarmRule,
    apply_program_alarm,
)
from .guidance_crosscheck import (
    GuidanceCrosscheckConfig,
    GuidanceObservation,
    compare_guidance_observations,
)
from .guidance_monitoring_profiles import get_guidance_monitoring_profile
from .guidance_voting import (
    GuidanceVotingConfig,
    assess_guidance_consensus,
)
from .landing_radar_model import (
    LandingRadarGuidanceContext,
    LandingRadarMeasurement,
    LandingRadarUpdateConfig,
    assess_landing_radar_update,
)
from .landing_radar_quality import (
    AffineResidualRule,
    LandingRadarQualityConfig,
    LandingRadarQualityInput,
    RadarScalarChannel,
    qualify_landing_radar_measurements,
)
from .landing_radar_reference import (
    LandingRadarVelocityReferenceInput,
    compute_landing_radar_velocity_reference,
)
from .landing_radar_profiles import get_landing_radar_profile
from .landing_radar_velocity_update import (
    LandingRadarVelocityUpdateInput,
    apply_landing_radar_velocity_update,
)
from .malfunction_plan import (
    CausalInsertion,
    InsertionLayer,
    InsertionMode,
    MalfunctionPlan,
    MalfunctionScheduler,
    activation_to_dict,
)
from .measurement_profiles import get_measurement_profile
from .mission_profiles import (
    MissionProfileRecord,
    discover_mission_profiles,
    get_mission_profile,
)
from .pc2_action_consequence_probe import run_pc2_action_consequence_matrix
from .pc2_inverter_consequence_probe import run_pc2_inverter_consequence_matrix
from .pc2_nominal import load_fixture
from .model_profiles import (
    ModelProfileRecord,
    assess_model_readiness,
    discover_model_profiles,
    get_model_profile,
)
from .realtime_clock import RealtimeSessionClock
from .resource_inventory_model import (
    ResourceFlowSegment,
    ResourceInventoryConfig,
    ResourceInventoryState,
    ResourceSpec,
    simulate_resource_inventory,
)
from .resource_power_coupling import (
    ResourceElectricalSourceRule,
    derive_electrical_source_availability,
)
from .runtime_adapters import (
    create_runtime,
    has_runtime_adapter,
    runtime_capabilities,
)
from .session_runtime import SessionRuntime
from .scenario_catalog import (
    DEFAULT_SCENARIO_ID,
    ScenarioRecord,
    discover_scenarios,
    get_scenario_record,
)
from .scenario_injection import EvidenceClass, StateInjection
from .session_shutdown_evidence import (
    assess_session_shutdown_evidence,
    record_crew_shutdown_report,
)
from .shutdown_rules import evaluate_pc2_shutdown_rules
from .tracking_observation import (
    TrackingObservationConfig,
    TrackingStationState,
    compute_geometric_tracking_truth,
    produce_tracking_observation,
)

ROOT = Path(__file__).resolve().parents[2]
WEB_ROOT = ROOT / "web"
FACILITATOR_TOKEN_ENV = "APOLLO_FACILITATOR_TOKEN"

app = FastAPI(
    title="Apollo Mission Control",
    description="Reusable Apollo Mission Control simulation API",
    version="0.1.0",
)

_lock = RLock()
_session: SessionRuntime | None = None
_clock: RealtimeSessionClock | None = None
_active_scenario: ScenarioRecord | None = None
_active_mission_profile: MissionProfileRecord | None = None
_active_model_profile: ModelProfileRecord | None = None
_active_runtime_adapter_id: str | None = None
_playability_events: list[dict[str, Any]] = []
_playability_sequence = 0

PLAYABILITY_SURFACES = {"validation_client", "player_lab"}
PLAYABILITY_EVENT_KINDS = {
    "page_load",
    "join_attempt",
    "join_success",
    "auto_rejoin_attempt",
    "auto_rejoin_success",
    "auto_rejoin_failure",
    "workspace_ready",
    "station_switch",
    "action_attempt",
    "action_success",
    "action_error",
}


class JoinRequest(BaseModel):
    player_id: str = Field(min_length=1, max_length=64)
    station: str = Field(min_length=1, max_length=32)


class JoinSetRequest(BaseModel):
    player_id: str = Field(min_length=1, max_length=64)
    stations: list[str] = Field(min_length=1, max_length=7)


class PlayabilityEventRequest(BaseModel):
    surface: str = Field(min_length=1, max_length=32)
    event: str = Field(min_length=1, max_length=64)
    player_id: str | None = Field(default=None, min_length=1, max_length=64)
    station: str | None = Field(default=None, min_length=1, max_length=32)
    target: str | None = Field(default=None, min_length=1, max_length=128)
    client_elapsed_ms: float | None = Field(default=None, ge=0.0, le=86_400_000.0)


class AdvanceRequest(BaseModel):
    target_get_s: float


class ReadinessRequest(BaseModel):
    ready: bool
    note: str = Field(default="", max_length=500)
    station: str | None = Field(default=None, min_length=1, max_length=32)


class FlightDecisionRequest(BaseModel):
    go: bool
    basis: str = Field(min_length=1, max_length=1000)


class CapcomQueueRequest(BaseModel):
    action: str = Field(min_length=1, max_length=128)
    parameters: dict[str, Any] = Field(default_factory=dict)
    basis: str = Field(min_length=1, max_length=1000)


class StateInjectionRequest(BaseModel):
    injection_id: str = Field(min_length=1, max_length=128)
    target: str = Field(min_length=1, max_length=128)
    value: Any
    evidence_class: EvidenceClass
    provenance: str = Field(min_length=1, max_length=2000)


class ControlDeltaPCalloutRequest(BaseModel):
    basis: str = Field(min_length=1, max_length=1000)


class CrewReceiptRequest(BaseModel):
    crew_id: str = Field(default="CREW", min_length=1, max_length=64)
    response: str = Field(default="received", min_length=1, max_length=500)


class InverterTransferQueueRequest(BaseModel):
    basis: str = Field(min_length=1, max_length=1000)


class CrewInverterTransferRequest(BaseModel):
    crew_id: str = Field(default="CREW", min_length=1, max_length=64)
    provenance: str = Field(
        default=(
            "Apollo 13 LM Malfunction Procedures INVERTER caution flowchart; "
            "inverter 2 to inverter 1 transfer"
        ),
        min_length=1,
        max_length=2000,
    )


class CrewInverterTransferReportRequest(BaseModel):
    crew_id: str = Field(default="CREW", min_length=1, max_length=64)


class CrewShutdownRequest(BaseModel):
    crew_id: str = Field(default="CREW", min_length=1, max_length=64)
    provenance: str = Field(
        default=(
            "Apollo 13 PC+2 ground-call shutdown rule; "
            "exact cockpit choreography unresolved"
        ),
        min_length=1,
        max_length=2000,
    )


class CrewShutdownReportRequest(BaseModel):
    crew_id: str = Field(default="CREW", min_length=1, max_length=64)


class PrematureDPSStopRequest(BaseModel):
    shutdown_cause_known_non_rule: bool = False
    noun97_flashing: bool | None = None
    cause: str = Field(
        default="premature_stop_mechanism_unspecified",
        min_length=1,
        max_length=256,
    )


class CrewRestartProcedureRequest(BaseModel):
    crew_id: str = Field(default="CREW", min_length=1, max_length=64)


class DPSRestartResponseRequest(BaseModel):
    cause: str = Field(
        default="pc2_manual_restart_sequence",
        min_length=1,
        max_length=256,
    )


class EngineOffResponseRequest(BaseModel):
    cause: str = Field(default="crew_stop_pushbutton", min_length=1, max_length=128)


class BurnSegmentRequest(BaseModel):
    duration_s: float = Field(ge=0.0, le=7200.0)
    thrust_n: float = Field(ge=0.0, le=1_000_000.0)
    direction: list[float] = Field(min_length=3, max_length=3)
    end_thrust_n: float | None = Field(default=None, ge=0.0, le=1_000_000.0)
    specific_impulse_s: float | None = Field(default=None, gt=0.0, le=10_000.0)
    regime: str = Field(default="regulated", min_length=1, max_length=64)


class DPSModelProofRequest(BaseModel):
    initial_time_s: float = 0.0
    initial_mass_kg: float = Field(gt=0.0, le=1_000_000.0)
    dry_mass_kg: float = Field(ge=0.0, le=1_000_000.0)
    initial_velocity_m_s: list[float] = Field(
        default_factory=lambda: [0.0, 0.0, 0.0],
        min_length=3,
        max_length=3,
    )
    specific_impulse_s: float = Field(gt=0.0, le=10_000.0)
    max_step_s: float = Field(default=0.25, gt=0.0, le=60.0)
    applicability: str = Field(
        default="generic model proof; not mission validated",
        min_length=1,
        max_length=500,
    )
    provenance: list[str] = Field(default_factory=list, max_length=20)
    segments: list[BurnSegmentRequest] = Field(min_length=1, max_length=50)


class TrackingObservationRequest(BaseModel):
    receive_delay_s: float = Field(default=0.0, ge=0.0, le=86_400.0)
    range_bias_m: float = Field(default=0.0, ge=-1.0e9, le=1.0e9)
    range_rate_bias_m_s: float = Field(default=0.0, ge=-1.0e6, le=1.0e6)
    available: bool = True
    valid: bool = True
    source: str = Field(
        default="generic trajectory-tracking API proof",
        min_length=1,
        max_length=500,
    )
    provenance: list[str] = Field(default_factory=list, max_length=20)


class TrajectoryTrackingModelProofRequest(BaseModel):
    initial_time_s: float = 0.0
    initial_position_m: list[float] = Field(min_length=3, max_length=3)
    initial_velocity_m_s: list[float] = Field(min_length=3, max_length=3)
    initial_mass_kg: float = Field(gt=0.0, le=1_000_000.0)
    dry_mass_kg: float = Field(ge=0.0, le=1_000_000.0)
    specific_impulse_s: float = Field(gt=0.0, le=10_000.0)
    gravitational_parameter_m3_s2: float = Field(default=0.0, ge=0.0)
    gravity_center_m: list[float] = Field(
        default_factory=lambda: [0.0, 0.0, 0.0],
        min_length=3,
        max_length=3,
    )
    max_step_s: float = Field(default=0.25, gt=0.0, le=60.0)
    applicability: str = Field(
        default="generic trajectory-tracking model proof; not mission validated",
        min_length=1,
        max_length=500,
    )
    provenance: list[str] = Field(default_factory=list, max_length=20)
    segments: list[BurnSegmentRequest] = Field(min_length=1, max_length=50)
    station_position_m: list[float] = Field(min_length=3, max_length=3)
    station_velocity_m_s: list[float] = Field(
        default_factory=lambda: [0.0, 0.0, 0.0],
        min_length=3,
        max_length=3,
    )
    observation: TrackingObservationRequest = Field(
        default_factory=TrackingObservationRequest
    )


class HistoricalMeasurementProfileProofRequest(BaseModel):
    profile_id: str = Field(min_length=1, max_length=128)
    source_state: dict[str, Any] = Field(default_factory=dict)


class GuidanceAlarmModelProofRequest(BaseModel):
    state_time_s: float = 0.0
    active_program: str = Field(min_length=1, max_length=128)
    alarm_code: str = Field(min_length=1, max_length=64)
    alarm_meaning: str = Field(min_length=1, max_length=500)
    software_restart: bool = True
    restart_protected_programs: list[str] = Field(default_factory=list, max_length=50)
    event_time_s: float
    source: str = Field(default="synthetic_program_detected", min_length=1, max_length=128)
    applicability: str = Field(
        default="generic guidance-computer alarm API proof; not mission validated",
        min_length=1,
        max_length=500,
    )
    provenance: list[str] = Field(default_factory=list, max_length=20)


class GuidanceObservationRequest(BaseModel):
    source: str = Field(min_length=1, max_length=128)
    time_s: float
    valid: bool = True
    values: dict[str, float]
    provenance: list[str] = Field(default_factory=list, max_length=20)


class GuidanceCrosscheckModelProofRequest(BaseModel):
    first: GuidanceObservationRequest
    second: GuidanceObservationRequest
    tolerances: dict[str, float]
    max_time_separation_s: float = Field(ge=0.0, le=86_400.0)
    applicability: str = Field(
        default="generic guidance cross-check API proof; not mission validated",
        min_length=1,
        max_length=500,
    )
    provenance: list[str] = Field(default_factory=list, max_length=20)


class GuidanceConsensusModelProofRequest(BaseModel):
    observations: list[GuidanceObservationRequest] = Field(min_length=2, max_length=20)
    tolerances: dict[str, float]
    max_time_separation_s: float = Field(ge=0.0, le=86_400.0)
    minimum_agreeing_sources: int = Field(default=2, ge=2, le=20)
    applicability: str = Field(
        default="generic guidance consensus API proof; not mission validated",
        min_length=1,
        max_length=500,
    )
    provenance: list[str] = Field(default_factory=list, max_length=20)


class RadarScalarChannelRequest(BaseModel):
    measured_value: float
    reference_value: float
    unit: str = Field(min_length=1, max_length=32)
    valid: bool = True


class AffineResidualRuleRequest(BaseModel):
    fixed_tolerance: float = Field(ge=0.0)
    proportional_tolerance: float = Field(default=0.0, ge=0.0)


class LandingRadarQualityUpdateChainRequest(BaseModel):
    time_s: float
    guidance_time_s: float
    data_good: bool = True
    data_good_since_s: float | None = None
    range_scale_last_changed_s: float | None = None
    source: str = Field(
        default="generic landing-radar chain API proof",
        min_length=1,
        max_length=500,
    )
    channels: dict[str, RadarScalarChannelRequest]
    min_data_good_duration_s: float = Field(default=0.0, ge=0.0)
    min_range_scale_stable_s: float | None = Field(default=None, ge=0.0)
    scale_stability_channels: list[str] = Field(default_factory=list, max_length=20)
    residual_rules: dict[str, AffineResidualRuleRequest]
    updates_enabled: bool = True
    estimated_velocity_m_s: list[float] = Field(min_length=3, max_length=3)
    velocity_update_speed_threshold_m_s: float | None = Field(default=None, ge=0.0)
    altitude_channel: str = Field(default="altitude", min_length=1, max_length=128)
    velocity_channel: str = Field(default="velocity_axis", min_length=1, max_length=128)
    applicability: str = Field(
        default="generic landing-radar quality/update API proof; not mission validated",
        min_length=1,
        max_length=500,
    )
    provenance: list[str] = Field(default_factory=list, max_length=20)


class LandingRadarVelocityReferenceRequest(BaseModel):
    estimated_velocity_m_s: list[float] = Field(min_length=3, max_length=3)
    lunar_surface_velocity_m_s: list[float] = Field(min_length=3, max_length=3)
    beam_unit_vector: list[float] = Field(min_length=3, max_length=3)
    component: str = Field(default="velocity_axis", min_length=1, max_length=128)
    unit_vector_tolerance: float = Field(default=1.0e-6, ge=0.0)
    applicability: str = Field(
        default=(
            "landing-radar velocity-reference projection; "
            "historical beam/attitude transform supplied upstream"
        ),
        min_length=1,
        max_length=500,
    )
    provenance: list[str] = Field(default_factory=list, max_length=20)


class LandingRadarHistoricalVelocityUpdateRequest(BaseModel):
    profile_id: str = Field(
        default="apollo11_lm5_landing_radar_partial",
        min_length=1,
        max_length=128,
    )
    prior_velocity_m_s: list[float] = Field(min_length=3, max_length=3)
    estimated_speed_m_s: float = Field(ge=0.0)
    measured_minus_reference_m_s: float
    beam_unit_vector: list[float] = Field(min_length=3, max_length=3)
    component: str = Field(min_length=1, max_length=32)
    program: str | None = Field(default=None, min_length=1, max_length=32)
    reasonableness_passed: bool = True
    updates_permitted: bool = True


class CausalInsertionRequest(BaseModel):
    insertion_id: str = Field(min_length=1, max_length=128)
    layer: InsertionLayer
    target: str = Field(min_length=1, max_length=256)
    value: Any
    provenance: str = Field(min_length=1, max_length=1000)


class MalfunctionPlanProofRequest(BaseModel):
    malfunction_id: str = Field(min_length=1, max_length=128)
    description: str = Field(min_length=1, max_length=500)
    mode: InsertionMode
    activation_time_s: float | None = None
    current_time_s: float
    trigger_mode: InsertionMode | None = None
    insertions: list[CausalInsertionRequest] = Field(min_length=1, max_length=50)
    provenance: str = Field(min_length=1, max_length=1000)


class ResourceSpecRequest(BaseModel):
    resource_id: str = Field(min_length=1, max_length=128)
    unit: str = Field(min_length=1, max_length=32)
    minimum_quantity: float = 0.0
    maximum_quantity: float | None = None


class ResourceFlowSegmentRequest(BaseModel):
    duration_s: float = Field(ge=0.0, le=10_000_000.0)
    rates_per_s: dict[str, float] = Field(default_factory=dict)
    label: str = Field(default="flow", min_length=1, max_length=128)


class ResourceInventoryModelProofRequest(BaseModel):
    initial_time_s: float = 0.0
    initial_quantities: dict[str, float]
    resources: list[ResourceSpecRequest] = Field(min_length=1, max_length=100)
    segments: list[ResourceFlowSegmentRequest] = Field(min_length=1, max_length=500)
    applicability: str = Field(
        default="generic resource inventory API proof; not mission validated",
        min_length=1,
        max_length=500,
    )
    provenance: list[str] = Field(default_factory=list, max_length=20)


class ElectricalSourceRequest(BaseModel):
    source_id: str = Field(min_length=1, max_length=128)
    max_power_w: float = Field(ge=0.0, le=1.0e12)


class ElectricalLoadRequest(BaseModel):
    load_id: str = Field(min_length=1, max_length=128)
    power_w: float = Field(ge=0.0, le=1.0e12)
    priority: int = Field(default=0, ge=-1_000_000, le=1_000_000)


class ElectricalBusModelProofRequest(BaseModel):
    bus_id: str = Field(min_length=1, max_length=128)
    sources: list[ElectricalSourceRequest] = Field(min_length=1, max_length=100)
    loads: list[ElectricalLoadRequest] = Field(default_factory=list, max_length=500)
    source_available: dict[str, bool] = Field(default_factory=dict)
    load_commanded_on: dict[str, bool] = Field(default_factory=dict)
    bus_enabled: bool = True
    applicability: str = Field(
        default="generic electrical bus API proof; not mission validated",
        min_length=1,
        max_length=500,
    )
    provenance: list[str] = Field(default_factory=list, max_length=20)


class ResourceElectricalSourceRuleRequest(BaseModel):
    source_id: str = Field(min_length=1, max_length=128)
    resource_id: str = Field(min_length=1, max_length=128)
    minimum_operating_quantity: float = 0.0
    available_at_threshold: bool = False
    provenance: str = Field(
        default="caller-supplied resource/power coupling",
        min_length=1,
        max_length=1000,
    )


class PoweredTrackingObservationRequest(BaseModel):
    receive_delay_s: float = Field(default=0.0, ge=0.0, le=86_400.0)
    range_bias_m: float = Field(default=0.0, ge=-1.0e9, le=1.0e9)
    range_rate_bias_m_s: float = Field(default=0.0, ge=-1.0e6, le=1.0e6)
    upstream_valid: bool = True
    source: str = Field(
        default="generic resource-power tracking proof",
        min_length=1,
        max_length=500,
    )
    provenance: list[str] = Field(default_factory=list, max_length=20)


class ResourcePowerObservationChainRequest(BaseModel):
    resource_inventory: ResourceInventoryModelProofRequest
    source_rules: list[ResourceElectricalSourceRuleRequest] = Field(
        min_length=1,
        max_length=100,
    )
    source_hardware_available: dict[str, bool] = Field(default_factory=dict)
    electrical_bus: ElectricalBusModelProofRequest
    observation_load_id: str = Field(min_length=1, max_length=128)
    vehicle_time_s: float
    vehicle_position_m: list[float] = Field(min_length=3, max_length=3)
    vehicle_velocity_m_s: list[float] = Field(min_length=3, max_length=3)
    vehicle_mass_kg: float = Field(gt=0.0, le=1.0e9)
    station_position_m: list[float] = Field(min_length=3, max_length=3)
    station_velocity_m_s: list[float] = Field(
        default_factory=lambda: [0.0, 0.0, 0.0],
        min_length=3,
        max_length=3,
    )
    observation: PoweredTrackingObservationRequest = Field(
        default_factory=PoweredTrackingObservationRequest
    )


def _require_session() -> SessionRuntime:
    if _session is None:
        raise HTTPException(status_code=409, detail="No simulation session has been created")
    return _session


def _require_clock() -> RealtimeSessionClock:
    if _clock is None:
        raise HTTPException(status_code=409, detail="No simulation session clock has been created")
    return _clock


def _sync_session() -> SessionRuntime:
    session = _require_session()
    _require_clock().sync()
    return session


def _domain_call(call: Callable[[], Any]) -> Any:
    try:
        return call()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


def _require_runtime_capability(capability: str) -> None:
    adapter_id = _active_runtime_adapter_id
    if adapter_id is None:
        raise HTTPException(status_code=409, detail="No simulation session has been created")
    if capability not in runtime_capabilities(adapter_id):
        raise HTTPException(
            status_code=400,
            detail=(
                f"runtime adapter {adapter_id!r} does not support "
                f"capability {capability!r}"
            ),
        )


def _facilitator_guard(
    x_apollo_facilitator: str | None = Header(default=None),
) -> None:
    """Protect facilitator/SimSup operations without conflating them with stations."""
    expected = os.getenv(FACILITATOR_TOKEN_ENV)
    if not expected:
        if os.getenv("RENDER", "").lower() == "true":
            raise HTTPException(
                status_code=503,
                detail="Facilitator authorization is not configured",
            )
        return
    if not x_apollo_facilitator or not hmac.compare_digest(
        x_apollo_facilitator, expected
    ):
        raise HTTPException(status_code=401, detail="Facilitator authorization required")


def _status_payload(session: SessionRuntime) -> dict[str, Any]:
    readiness = (
        assess_model_readiness(
            _active_model_profile,
            _active_scenario.required_model_domains,
        )
        if _active_model_profile is not None and _active_scenario is not None
        else None
    )
    return {
        "status": session.status.value,
        "get_s": session.state.get_s,
        "phase": session.state.phase,
        "pending_gate": session.pending_gate,
        "pause_reason": session.pause_reason,
        "assigned_stations": sorted(session.assigned_stations),
        "available_stations": list(session.available_stations),
        "scenario_id": (
            _active_scenario.scenario_id if _active_scenario is not None else None
        ),
        "mission": (
            _active_scenario.mission if _active_scenario is not None else None
        ),
        "scenario_title": (
            _active_scenario.title if _active_scenario is not None else None
        ),
        "mission_profile_id": (
            _active_mission_profile.mission_profile_id
            if _active_mission_profile is not None
            else None
        ),
        "model_profile_id": (
            _active_model_profile.model_profile_id
            if _active_model_profile is not None
            else None
        ),
        "model_validation_state": (
            _active_model_profile.validation_state
            if _active_model_profile is not None
            else None
        ),
        "model_readiness": (
            readiness.to_public_dict() if readiness is not None else None
        ),
        "runtime_adapter": _active_runtime_adapter_id,
        "runtime_capabilities": sorted(
            runtime_capabilities(_active_runtime_adapter_id)
            if _active_runtime_adapter_id is not None
            else ()
        ),
    }


def _snapshot_payload(session: SessionRuntime, player_id: str) -> dict[str, Any]:
    stations = session.stations_for(player_id)
    if len(stations) == 1:
        return session.player_snapshot(player_id).to_dict()
    return session.bundled_player_snapshot(player_id).to_dict()


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/scenarios")
def list_scenarios() -> list[dict[str, object]]:
    records = _domain_call(discover_scenarios)
    result: list[dict[str, object]] = []
    for record in records:
        profile = _domain_call(
            lambda record=record: get_model_profile(record.model_profile_id)
        )
        readiness = _domain_call(
            lambda record=record, profile=profile: assess_model_readiness(
                profile,
                record.required_model_domains,
            )
        )
        result.append(
            {
                **record.to_public_dict(),
                "default": record.scenario_id == DEFAULT_SCENARIO_ID,
                "executable": has_runtime_adapter(record.runtime_adapter),
                "model_readiness": readiness.to_public_dict(),
            }
        )
    return result


@app.get("/api/mission-profiles")
def list_mission_profiles() -> list[dict[str, object]]:
    return [
        record.to_public_dict()
        for record in _domain_call(discover_mission_profiles)
    ]


@app.get("/api/model-profiles")
def list_model_profiles() -> list[dict[str, object]]:
    return [
        record.to_public_dict()
        for record in _domain_call(discover_model_profiles)
    ]


@app.post("/api/session/create", dependencies=[Depends(_facilitator_guard)])
def create_session(
    scenario_id: str = DEFAULT_SCENARIO_ID,
) -> dict[str, Any]:
    global _session, _clock, _active_scenario, _active_mission_profile
    global _active_model_profile, _active_runtime_adapter_id
    global _playability_events, _playability_sequence
    with _lock:
        record = _domain_call(lambda: get_scenario_record(scenario_id))
        profile = _domain_call(
            lambda: get_mission_profile(record.mission_profile_id)
        )
        model_profile = _domain_call(
            lambda: get_model_profile(record.model_profile_id)
        )
        if profile.mission != record.mission:
            raise HTTPException(
                status_code=400,
                detail=(
                    f"scenario {record.scenario_id} mission {record.mission!r} "
                    f"does not match mission profile {profile.mission_profile_id} "
                    f"mission {profile.mission!r}"
                ),
            )
        if model_profile.mission_profile_id != profile.mission_profile_id:
            raise HTTPException(
                status_code=400,
                detail=(
                    f"scenario {record.scenario_id} model profile "
                    f"{model_profile.model_profile_id!r} belongs to mission profile "
                    f"{model_profile.mission_profile_id!r}, not "
                    f"{profile.mission_profile_id!r}"
                ),
            )
        session = _domain_call(lambda: create_runtime(record))
        _session = session
        _clock = RealtimeSessionClock(session)
        _active_scenario = record
        _active_mission_profile = profile
        _active_model_profile = model_profile
        _active_runtime_adapter_id = record.runtime_adapter
        _playability_events = []
        _playability_sequence = 0
        return _status_payload(session)


@app.post("/api/session/instrumentation")
def record_playability_event(request: PlayabilityEventRequest) -> dict[str, Any]:
    """Record non-authoritative usability/playability telemetry for prototype clients."""
    global _playability_sequence
    with _lock:
        session = _sync_session()
        if request.surface not in PLAYABILITY_SURFACES:
            raise HTTPException(status_code=400, detail="Unsupported playability surface")
        if request.event not in PLAYABILITY_EVENT_KINDS:
            raise HTTPException(status_code=400, detail="Unsupported playability event")
        _playability_sequence += 1
        event = {
            "sequence": _playability_sequence,
            "get_s": float(session.state.get_s),
            "surface": request.surface,
            "event": request.event,
            "player_id": request.player_id,
            "station": request.station,
            "target": request.target,
            "client_elapsed_ms": request.client_elapsed_ms,
        }
        _playability_events.append(event)
        return dict(event)


@app.get(
    "/api/session/admin/playability-events",
    dependencies=[Depends(_facilitator_guard)],
)
def playability_events() -> list[dict[str, Any]]:
    """Return prototype usability telemetry separately from the mission audit log."""
    with _lock:
        _sync_session()
        return [dict(event) for event in _playability_events]


@app.get("/api/session/status")
def session_status() -> dict[str, Any]:
    with _lock:
        return _status_payload(_sync_session())


@app.post("/api/session/join")
def join_session(request: JoinRequest) -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        _domain_call(
            lambda: session.join_or_rejoin_stations(
                request.player_id,
                (request.station,),
            )
        )
        return _snapshot_payload(session, request.player_id)


@app.post("/api/session/join-set")
def join_session_set(request: JoinSetRequest) -> dict[str, Any]:
    """Join/rejoin multiple original stations without creating a synthetic station."""
    with _lock:
        session = _sync_session()
        _domain_call(
            lambda: session.join_or_rejoin_stations(
                request.player_id,
                request.stations,
            )
        )
        return _snapshot_payload(session, request.player_id)


@app.post("/api/session/start", dependencies=[Depends(_facilitator_guard)])
def start_session() -> dict[str, Any]:
    with _lock:
        session = _require_session()
        _domain_call(session.start)
        _require_clock().reanchor()
        return _status_payload(session)


@app.post("/api/session/pause", dependencies=[Depends(_facilitator_guard)])
def pause_session() -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        _domain_call(session.pause)
        _require_clock().reanchor()
        return _status_payload(session)


@app.post("/api/session/resume", dependencies=[Depends(_facilitator_guard)])
def resume_session() -> dict[str, Any]:
    with _lock:
        session = _require_session()
        _domain_call(session.resume)
        _require_clock().reanchor()
        return _status_payload(session)


@app.post("/api/session/advance", dependencies=[Depends(_facilitator_guard)])
def advance_session(request: AdvanceRequest) -> dict[str, Any]:
    """Manual validation control retained alongside realtime pacing."""
    with _lock:
        session = _sync_session()
        reached = _domain_call(lambda: session.advance_to(request.target_get_s))
        _require_clock().reanchor()
        payload = _status_payload(session)
        payload["reached_get_s"] = reached
        return payload


@app.post(
    "/api/session/admin/injection",
    dependencies=[Depends(_facilitator_guard)],
)
def apply_injection(request: StateInjectionRequest) -> dict[str, Any]:
    """Prototype scenario-authoring/validation endpoint, not a player control."""
    with _lock:
        _require_runtime_capability("state_injection")
        session = _sync_session()
        injection = StateInjection(
            injection_id=request.injection_id,
            get_s=float(session.state.get_s),
            target=request.target,
            value=request.value,
            evidence_class=request.evidence_class,
            provenance=request.provenance,
        )
        _domain_call(lambda: session.apply_session_injection(injection))
        return _status_payload(session)


@app.get("/api/session/player/{player_id}")
def player_snapshot(player_id: str) -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        return _domain_call(lambda: _snapshot_payload(session, player_id))


@app.post("/api/session/player/{player_id}/readiness")
def submit_readiness(player_id: str, request: ReadinessRequest) -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        report = _domain_call(
            lambda: session.submit_readiness(
                player_id,
                ready=request.ready,
                note=request.note,
                station=request.station,
            )
        )
        return {
            "get_s": report.get_s,
            "station": report.station,
            "ready": report.ready,
            "note": report.note,
        }


@app.post("/api/session/flight/{player_id}/decision")
def flight_decision(player_id: str, request: FlightDecisionRequest) -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        _domain_call(lambda: session.record_flight_go(player_id, go=request.go, basis=request.basis))
        return _snapshot_payload(session, player_id)


@app.post("/api/session/flight/{player_id}/capcom")
def queue_capcom(player_id: str, request: CapcomQueueRequest) -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        item = _domain_call(
            lambda: session.queue_capcom_instruction(
                player_id,
                action=request.action,
                parameters=request.parameters,
                basis=request.basis,
            )
        )
        return {
            "item_id": item.item_id,
            "get_s": item.get_s,
            "requested_by": item.requested_by,
            "action": item.action,
            "parameters": item.parameters,
            "basis": item.basis,
            "transmitted": item.transmitted,
        }


@app.post(
    "/api/session/flight/{player_id}/inverter-transfer",
)
def queue_inverter_transfer(
    player_id: str,
    request: InverterTransferQueueRequest,
) -> dict[str, Any]:
    with _lock:
        _require_runtime_capability("pc2_inverter_transfer")
        session = _sync_session()
        item = _domain_call(
            lambda: session.queue_inverter_transfer_instruction(
                player_id,
                basis=request.basis,
            )
        )
        return {
            "item_id": item.item_id,
            "get_s": item.get_s,
            "requested_by": item.requested_by,
            "action": item.action,
            "parameters": item.parameters,
            "basis": item.basis,
            "transmitted": item.transmitted,
        }


@app.post("/api/session/control/{player_id}/delta-p-callout")
def control_delta_p_callout(player_id: str, request: ControlDeltaPCalloutRequest) -> dict[str, Any]:
    with _lock:
        _require_runtime_capability("pc2_delta_p")
        session = _sync_session()
        item = _domain_call(
            lambda: session.record_control_delta_p_callout(player_id, basis=request.basis)
        )
        return {
            "item_id": item.item_id,
            "get_s": item.get_s,
            "requested_by": item.requested_by,
            "action": item.action,
            "parameters": item.parameters,
            "basis": item.basis,
            "transmitted": item.transmitted,
        }


@app.get("/api/session/control/{player_id}/shutdown-evidence")
def control_shutdown_evidence(player_id: str) -> dict[str, Any]:
    """Return controller-observable evidence availability, never hidden truth."""
    with _lock:
        _require_runtime_capability("pc2_delta_p")
        session = _sync_session()
        if not _domain_call(lambda: session.owns_station(player_id, "CONTROL")):
            raise HTTPException(status_code=400, detail="Only a CONTROL owner can request shutdown evidence")
        return _domain_call(lambda: assess_session_shutdown_evidence(session))


@app.post("/api/session/capcom/{player_id}/transmit/{item_id}")
def transmit_capcom(player_id: str, item_id: int) -> dict[str, Any]:
    with _lock:
        session = _sync_session()
        item = _domain_call(lambda: session.transmit_capcom_item(player_id, item_id))
        return {
            "item_id": item.item_id,
            "requested_by": item.requested_by,
            "action": item.action,
            "transmitted": item.transmitted,
            "transmitted_get_s": item.transmitted_get_s,
        }


@app.post(
    "/api/session/crew/receipt/{item_id}",
    dependencies=[Depends(_facilitator_guard)],
)
def crew_receipt(item_id: int, request: CrewReceiptRequest) -> dict[str, Any]:
    with _lock:
        _require_runtime_capability("pc2_simulated_crew")
        session = _sync_session()
        return _domain_call(
            lambda: record_crew_receipt(
                session,
                item_id,
                crew_id=request.crew_id,
                response=request.response,
            )
        )


@app.get(
    "/api/session/admin/inverter-rule",
    dependencies=[Depends(_facilitator_guard)],
)
def inverter_rule_validation() -> dict[str, Any]:
    """Expose the derived inverter rule state for facilitator validation only."""
    with _lock:
        _require_runtime_capability("pc2_inverter_transfer")
        session = _sync_session()
        evaluations = _domain_call(
            lambda: evaluate_pc2_shutdown_rules(
                project_controller_products(session.state, session.fixture),
                session.fixture,
            )
        )
        rule = evaluations["persistent_inverter_warning"]
        return {
            "rule_id": rule.rule_id,
            "state": rule.state.value,
            "owner": rule.owner,
            "basis": rule.basis,
            "observation": rule.observation,
            "validation_only": True,
        }


@app.post(
    "/api/session/crew/inverter-transfer/{item_id}",
    dependencies=[Depends(_facilitator_guard)],
)
def crew_inverter_transfer(
    item_id: int,
    request: CrewInverterTransferRequest,
) -> dict[str, Any]:
    with _lock:
        _require_runtime_capability("pc2_inverter_transfer")
        session = _sync_session()
        action = _domain_call(
            lambda: perform_inverter_transfer_from_callout(
                session,
                item_id,
                crew_id=request.crew_id,
                provenance=request.provenance,
            )
        )
        return {
            "action_id": action.action_id,
            "get_s": action.get_s,
            "actor": action.actor,
            "action": action.action,
            "parameters": action.parameters,
            "provenance": action.provenance,
        }


@app.post(
    "/api/session/crew/inverter-transfer-report/{item_id}",
    dependencies=[Depends(_facilitator_guard)],
)
def crew_inverter_transfer_report(
    item_id: int,
    request: CrewInverterTransferReportRequest,
) -> dict[str, Any]:
    with _lock:
        _require_runtime_capability("pc2_inverter_transfer")
        session = _sync_session()
        return _domain_call(
            lambda: record_inverter_transfer_completion_report(
                session,
                item_id,
                crew_id=request.crew_id,
            )
        )


@app.post(
    "/api/session/crew/shutdown/{item_id}",
    dependencies=[Depends(_facilitator_guard)],
)
def crew_shutdown(item_id: int, request: CrewShutdownRequest) -> dict[str, Any]:
    with _lock:
        _require_runtime_capability("pc2_dps_shutdown")
        session = _sync_session()
        action = _domain_call(
            lambda: command_dps_shutdown_from_callout(
                session,
                item_id,
                crew_id=request.crew_id,
                provenance=request.provenance,
            )
        )
        return {
            "action_id": action.action_id,
            "get_s": action.get_s,
            "actor": action.actor,
            "action": action.action,
            "parameters": action.parameters,
            "provenance": action.provenance,
        }


@app.post(
    "/api/session/crew/shutdown-report",
    dependencies=[Depends(_facilitator_guard)],
)
def crew_shutdown_report(request: CrewShutdownReportRequest) -> dict[str, Any]:
    with _lock:
        _require_runtime_capability("pc2_dps_shutdown")
        session = _sync_session()
        return _domain_call(lambda: record_crew_shutdown_report(session, crew_id=request.crew_id))


@app.post(
    "/api/session/admin/vehicle/dps-premature-stop",
    dependencies=[Depends(_facilitator_guard)],
)
def dps_premature_stop(request: PrematureDPSStopRequest) -> dict[str, Any]:
    with _lock:
        _require_runtime_capability("pc2_dps_restart")
        session = _sync_session()
        return _domain_call(
            lambda: record_premature_dps_stop(
                session,
                shutdown_cause_known_non_rule=request.shutdown_cause_known_non_rule,
                noun97_flashing=request.noun97_flashing,
                cause=request.cause,
            )
        )


@app.post(
    "/api/session/crew/restart-procedure",
    dependencies=[Depends(_facilitator_guard)],
)
def crew_restart_procedure(request: CrewRestartProcedureRequest) -> dict[str, Any]:
    with _lock:
        _require_runtime_capability("pc2_dps_restart")
        session = _sync_session()
        events = _domain_call(
            lambda: perform_prebriefed_pc2_restart_procedure(
                session,
                crew_id=request.crew_id,
            )
        )
        return {"events": events}


@app.post(
    "/api/session/admin/vehicle/dps-restart",
    dependencies=[Depends(_facilitator_guard)],
)
def dps_restart_response(request: DPSRestartResponseRequest) -> dict[str, Any]:
    with _lock:
        _require_runtime_capability("pc2_dps_restart")
        session = _sync_session()
        return _domain_call(
            lambda: apply_session_restart_response(
                session,
                cause=request.cause,
            )
        )


@app.post(
    "/api/session/admin/vehicle/dps-engine-off",
    dependencies=[Depends(_facilitator_guard)],
)
def dps_engine_off_response(request: EngineOffResponseRequest) -> dict[str, Any]:
    with _lock:
        _require_runtime_capability("pc2_dps_shutdown")
        session = _sync_session()
        return _domain_call(
            lambda: apply_session_engine_off_response(
                session,
                get_s=float(session.state.get_s),
                cause=request.cause,
            )
        )


@app.post(
    "/api/admin/model-proof/pc2-action-consequences",
    dependencies=[Depends(_facilitator_guard)],
)
def pc2_action_consequence_model_proof() -> dict[str, Any]:
    fixture = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")
    return _domain_call(lambda: run_pc2_action_consequence_matrix(fixture))


@app.post(
    "/api/admin/model-proof/pc2-inverter-consequences",
    dependencies=[Depends(_facilitator_guard)],
)
def pc2_inverter_consequence_model_proof() -> dict[str, Any]:
    fixture = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")
    return _domain_call(lambda: run_pc2_inverter_consequence_matrix(fixture))


@app.post(
    "/api/admin/model-proof/dps-burn",
    dependencies=[Depends(_facilitator_guard)],
)
def dps_burn_model_proof(request: DPSModelProofRequest) -> dict[str, object]:
    """Run the mission-neutral Level-1 burn model from explicit caller inputs."""

    result = _domain_call(
        lambda: simulate_dps_maneuver(
            ManeuverState(
                time_s=request.initial_time_s,
                mass_kg=request.initial_mass_kg,
                velocity_m_s=tuple(request.initial_velocity_m_s),
            ),
            [
                BurnSegment(
                    duration_s=segment.duration_s,
                    thrust_n=segment.thrust_n,
                    direction=tuple(segment.direction),
                    end_thrust_n=segment.end_thrust_n,
                    specific_impulse_s=segment.specific_impulse_s,
                    regime=segment.regime,
                )
                for segment in request.segments
            ],
            DPSModelConfig(
                specific_impulse_s=request.specific_impulse_s,
                dry_mass_kg=request.dry_mass_kg,
                max_step_s=request.max_step_s,
                applicability=request.applicability,
                provenance=tuple(request.provenance),
            ),
        )
    )
    return result.to_dict()


@app.post(
    "/api/admin/model-proof/trajectory-tracking",
    dependencies=[Depends(_facilitator_guard)],
)
def trajectory_tracking_model_proof(
    request: TrajectoryTrackingModelProofRequest,
) -> dict[str, object]:
    """Run a mission-neutral trajectory -> tracking-observation proof chain."""

    segments = [
        BurnSegment(
            duration_s=segment.duration_s,
            thrust_n=segment.thrust_n,
            direction=tuple(segment.direction),
            end_thrust_n=segment.end_thrust_n,
            specific_impulse_s=segment.specific_impulse_s,
            regime=segment.regime,
        )
        for segment in request.segments
    ]

    trajectory = _domain_call(
        lambda: simulate_translational_maneuver(
            TranslationalState(
                time_s=request.initial_time_s,
                position_m=tuple(request.initial_position_m),
                velocity_m_s=tuple(request.initial_velocity_m_s),
                mass_kg=request.initial_mass_kg,
            ),
            segments,
            TranslationalConfig(
                specific_impulse_s=request.specific_impulse_s,
                dry_mass_kg=request.dry_mass_kg,
                gravitational_parameter_m3_s2=request.gravitational_parameter_m3_s2,
                gravity_center_m=tuple(request.gravity_center_m),
                max_step_s=request.max_step_s,
                applicability=request.applicability,
                provenance=tuple(request.provenance),
            ),
        )
    )

    truth = _domain_call(
        lambda: compute_geometric_tracking_truth(
            trajectory.final_state,
            TrackingStationState(
                position_m=tuple(request.station_position_m),
                velocity_m_s=tuple(request.station_velocity_m_s),
            ),
        )
    )
    observation = _domain_call(
        lambda: produce_tracking_observation(
            truth,
            TrackingObservationConfig(
                receive_delay_s=request.observation.receive_delay_s,
                range_bias_m=request.observation.range_bias_m,
                range_rate_bias_m_s=request.observation.range_rate_bias_m_s,
                available=request.observation.available,
                valid=request.observation.valid,
                source=request.observation.source,
                provenance=tuple(request.observation.provenance),
            ),
        )
    )

    return {
        "model_status": "trajectory_tracking_chain_not_historically_validated",
        "trajectory": trajectory.to_dict(),
        "tracking_observation": observation.to_dict(),
    }




def _resource_inventory_from_request(
    request: ResourceInventoryModelProofRequest,
):
    return simulate_resource_inventory(
        ResourceInventoryState(
            time_s=request.initial_time_s,
            quantities=request.initial_quantities,
        ),
        [
            ResourceFlowSegment(
                duration_s=segment.duration_s,
                rates_per_s=segment.rates_per_s,
                label=segment.label,
            )
            for segment in request.segments
        ],
        ResourceInventoryConfig(
            resources=tuple(
                ResourceSpec(
                    resource_id=resource.resource_id,
                    unit=resource.unit,
                    minimum_quantity=resource.minimum_quantity,
                    maximum_quantity=resource.maximum_quantity,
                )
                for resource in request.resources
            ),
            applicability=request.applicability,
            provenance=tuple(request.provenance),
        ),
    )


def _electrical_bus_from_request(
    request: ElectricalBusModelProofRequest,
    *,
    source_available: dict[str, bool] | None = None,
):
    return evaluate_electrical_bus(
        ElectricalBusConfig(
            bus_id=request.bus_id,
            sources=tuple(
                ElectricalSourceSpec(
                    source_id=source.source_id,
                    max_power_w=source.max_power_w,
                )
                for source in request.sources
            ),
            loads=tuple(
                ElectricalLoadSpec(
                    load_id=load.load_id,
                    power_w=load.power_w,
                    priority=load.priority,
                )
                for load in request.loads
            ),
            applicability=request.applicability,
            provenance=tuple(request.provenance),
        ),
        ElectricalBusState(
            source_available=(
                request.source_available
                if source_available is None
                else source_available
            ),
            load_commanded_on=request.load_commanded_on,
            bus_enabled=request.bus_enabled,
        ),
    )


@app.post(
    "/api/admin/model-proof/historical-measurement-profile",
    dependencies=[Depends(_facilitator_guard)],
)
def historical_measurement_profile_model_proof(
    request: HistoricalMeasurementProfileProofRequest,
) -> dict[str, Any]:
    profile = _domain_call(lambda: get_measurement_profile(request.profile_id))
    outputs = _domain_call(lambda: profile.evaluate_source_state(request.source_state))

    ground_gate = "open"
    ground_gate_reason = None
    try:
        profile.require_historical_ground_product()
    except ValueError as exc:
        ground_gate = "blocked"
        ground_gate_reason = str(exc)

    return {
        "model_status": "historical_measurement_profile_vehicle_boundary",
        "profile": profile.to_public_dict(),
        "vehicle_measurement_output": outputs.to_dict(),
        "historical_ground_product_gate": ground_gate,
        "historical_ground_product_gate_reason": ground_gate_reason,
        "note": (
            "Vehicle measurement execution does not imply live mission PCM loading, "
            "MCC routing, or controller-display availability."
        ),
    }


@app.post(
    "/api/admin/model-proof/guidance-alarm",
    dependencies=[Depends(_facilitator_guard)],
)
def guidance_alarm_model_proof(
    request: GuidanceAlarmModelProofRequest,
) -> dict[str, object]:
    result = _domain_call(
        lambda: apply_program_alarm(
            GuidanceComputerState(
                time_s=request.state_time_s,
                active_program=request.active_program,
            ),
            ProgramAlarmEvent(
                time_s=request.event_time_s,
                code=request.alarm_code,
                source=request.source,
            ),
            GuidanceComputerConfig(
                alarm_rules={
                    request.alarm_code: ProgramAlarmRule(
                        code=request.alarm_code,
                        meaning=request.alarm_meaning,
                        software_restart=request.software_restart,
                    )
                },
                restart_protected_programs=tuple(
                    request.restart_protected_programs
                ),
                applicability=request.applicability,
                provenance=tuple(request.provenance),
            ),
        )
    )
    return result.to_dict()


def _guidance_observation_from_request(
    request: GuidanceObservationRequest,
) -> GuidanceObservation:
    return GuidanceObservation(
        source=request.source,
        time_s=request.time_s,
        valid=request.valid,
        values=request.values,
        provenance=tuple(request.provenance),
    )


@app.get(
    "/api/admin/model-proof/guidance-monitoring-profile/{profile_id}",
    dependencies=[Depends(_facilitator_guard)],
)
def guidance_monitoring_profile_model_proof(profile_id: str) -> dict[str, Any]:
    """Expose historical monitoring evidence without inventing executable freshness."""
    profile = _domain_call(lambda: get_guidance_monitoring_profile(profile_id))
    payload = profile.to_public_dict()
    payload["historically_executable"] = all(
        comparison.historically_executable for comparison in profile.comparisons
    )
    payload["execution_gate"] = (
        "open" if payload["historically_executable"] else "blocked"
    )
    payload["gate_note"] = (
        "Processor/input cadence evidence is not an inter-source comparison "
        "freshness rule. Comparisons remain non-executable while "
        "max_time_separation_s is unresolved."
    )
    return payload


@app.post(
    "/api/admin/model-proof/guidance-crosscheck",
    dependencies=[Depends(_facilitator_guard)],
)
def guidance_crosscheck_model_proof(
    request: GuidanceCrosscheckModelProofRequest,
) -> dict[str, object]:
    result = _domain_call(
        lambda: compare_guidance_observations(
            _guidance_observation_from_request(request.first),
            _guidance_observation_from_request(request.second),
            GuidanceCrosscheckConfig(
                tolerances=request.tolerances,
                max_time_separation_s=request.max_time_separation_s,
                applicability=request.applicability,
                provenance=tuple(request.provenance),
            ),
        )
    )
    return result.to_dict()


@app.post(
    "/api/admin/model-proof/guidance-consensus",
    dependencies=[Depends(_facilitator_guard)],
)
def guidance_consensus_model_proof(
    request: GuidanceConsensusModelProofRequest,
) -> dict[str, object]:
    result = _domain_call(
        lambda: assess_guidance_consensus(
            [
                _guidance_observation_from_request(observation)
                for observation in request.observations
            ],
            GuidanceVotingConfig(
                tolerances=request.tolerances,
                max_time_separation_s=request.max_time_separation_s,
                minimum_agreeing_sources=request.minimum_agreeing_sources,
                applicability=request.applicability,
                provenance=tuple(request.provenance),
            ),
        )
    )
    return result.to_dict()


@app.post(
    "/api/admin/model-proof/landing-radar-velocity-reference",
    dependencies=[Depends(_facilitator_guard)],
)
def landing_radar_velocity_reference_model_proof(
    request: LandingRadarVelocityReferenceRequest,
) -> dict[str, object]:
    """Expose the source-backed velocity-reference projection without beam synthesis."""

    result = _domain_call(
        lambda: compute_landing_radar_velocity_reference(
            LandingRadarVelocityReferenceInput(
                estimated_velocity_m_s=tuple(request.estimated_velocity_m_s),
                lunar_surface_velocity_m_s=tuple(
                    request.lunar_surface_velocity_m_s
                ),
                beam_unit_vector=tuple(request.beam_unit_vector),
                component=request.component,
                unit_vector_tolerance=request.unit_vector_tolerance,
                applicability=request.applicability,
                provenance=tuple(request.provenance),
            )
        )
    )
    return result.to_dict()


@app.get(
    "/api/admin/model-proof/landing-radar-profile/{profile_id}",
    dependencies=[Depends(_facilitator_guard)],
)
def landing_radar_profile_model_proof(profile_id: str) -> dict[str, object]:
    profile = _domain_call(lambda: get_landing_radar_profile(profile_id))
    return profile.to_public_dict()


@app.post(
    "/api/admin/model-proof/landing-radar-historical-velocity-update",
    dependencies=[Depends(_facilitator_guard)],
)
def landing_radar_historical_velocity_update_model_proof(
    request: LandingRadarHistoricalVelocityUpdateRequest,
) -> dict[str, object]:
    profile = _domain_call(lambda: get_landing_radar_profile(request.profile_id))
    config = _domain_call(profile.velocity_update_config)
    result = _domain_call(
        lambda: apply_landing_radar_velocity_update(
            LandingRadarVelocityUpdateInput(
                prior_velocity_m_s=tuple(request.prior_velocity_m_s),
                estimated_speed_m_s=request.estimated_speed_m_s,
                measured_minus_reference_m_s=request.measured_minus_reference_m_s,
                beam_unit_vector=tuple(request.beam_unit_vector),
                component=request.component,
                program=request.program,
                reasonableness_passed=request.reasonableness_passed,
                updates_permitted=request.updates_permitted,
            ),
            config,
        )
    )
    return {
        "profile": profile.to_public_dict(),
        "velocity_update": result.to_dict(),
    }


@app.post(
    "/api/admin/model-proof/landing-radar-quality-update",
    dependencies=[Depends(_facilitator_guard)],
)
def landing_radar_quality_update_model_proof(
    request: LandingRadarQualityUpdateChainRequest,
) -> dict[str, object]:
    quality = _domain_call(
        lambda: qualify_landing_radar_measurements(
            LandingRadarQualityInput(
                time_s=request.time_s,
                data_good=request.data_good,
                data_good_since_s=request.data_good_since_s,
                range_scale_last_changed_s=request.range_scale_last_changed_s,
                source=request.source,
                channels={
                    name: RadarScalarChannel(
                        measured_value=channel.measured_value,
                        reference_value=channel.reference_value,
                        unit=channel.unit,
                        valid=channel.valid,
                    )
                    for name, channel in request.channels.items()
                },
            ),
            LandingRadarQualityConfig(
                min_data_good_duration_s=request.min_data_good_duration_s,
                min_range_scale_stable_s=request.min_range_scale_stable_s,
                scale_stability_channels=tuple(request.scale_stability_channels),
                residual_rules={
                    name: AffineResidualRule(
                        fixed_tolerance=rule.fixed_tolerance,
                        proportional_tolerance=rule.proportional_tolerance,
                    )
                    for name, rule in request.residual_rules.items()
                },
                applicability=request.applicability,
                provenance=tuple(request.provenance),
            ),
        )
    )

    try:
        altitude_quality = quality.channel(request.altitude_channel)
    except ValueError:
        altitude_quality = None
    try:
        velocity_quality = quality.channel(request.velocity_channel)
    except ValueError:
        velocity_quality = None

    altitude_request = request.channels.get(request.altitude_channel)
    velocity_request = request.channels.get(request.velocity_channel)

    if altitude_request is not None and altitude_request.unit != "m":
        raise HTTPException(
            status_code=400,
            detail="altitude_channel must use unit 'm'; no implicit conversion is performed",
        )
    if velocity_request is not None and velocity_request.unit != "m/s":
        raise HTTPException(
            status_code=400,
            detail="velocity_channel must use unit 'm/s'; no implicit conversion is performed",
        )

    altitude_m = (
        altitude_request.measured_value
        if altitude_request is not None
        and altitude_quality is not None
        and altitude_quality.accepted
        else None
    )
    velocity_m_s = (
        (velocity_request.measured_value, 0.0, 0.0)
        if velocity_request is not None
        and velocity_quality is not None
        and velocity_quality.accepted
        else None
    )

    update = _domain_call(
        lambda: assess_landing_radar_update(
            LandingRadarMeasurement(
                time_s=request.time_s,
                data_good=quality.data_good_qualified,
                altitude_m=altitude_m,
                velocity_m_s=velocity_m_s,
                source=request.source,
            ),
            LandingRadarGuidanceContext(
                time_s=request.guidance_time_s,
                updates_enabled=request.updates_enabled,
                estimated_velocity_m_s=tuple(request.estimated_velocity_m_s),
            ),
            LandingRadarUpdateConfig(
                velocity_update_speed_threshold_m_s=(
                    request.velocity_update_speed_threshold_m_s
                ),
                applicability=request.applicability,
                provenance=tuple(request.provenance),
            ),
        )
    )

    return {
        "model_status": (
            "landing_radar_quality_update_chain_not_historically_validated"
        ),
        "quality": quality.to_dict(),
        "qualified_measurement": {
            "time_s": request.time_s,
            "data_good": quality.data_good_qualified,
            "altitude_m": altitude_m,
            "velocity_m_s": list(velocity_m_s) if velocity_m_s is not None else None,
            "source": request.source,
        },
        "update_assessment": update.to_dict(),
    }


@app.post(
    "/api/admin/model-proof/malfunction-plan",
    dependencies=[Depends(_facilitator_guard)],
)
def malfunction_plan_model_proof(
    request: MalfunctionPlanProofRequest,
) -> dict[str, Any]:
    plan = MalfunctionPlan(
        malfunction_id=request.malfunction_id,
        description=request.description,
        mode=request.mode,
        activation_time_s=request.activation_time_s,
        insertions=tuple(
            CausalInsertion(
                insertion_id=item.insertion_id,
                layer=item.layer,
                target=item.target,
                value=item.value,
                provenance=item.provenance,
            )
            for item in request.insertions
        ),
        provenance=request.provenance,
    )
    scheduler = _domain_call(lambda: MalfunctionScheduler((plan,)))
    activation = _domain_call(
        lambda: scheduler.activate(
            request.malfunction_id,
            current_time_s=request.current_time_s,
            trigger_mode=request.trigger_mode,
        )
    )
    return {
        "model_status": "malfunction_plan_scheduler_proof_not_historically_validated",
        "activation": activation_to_dict(activation),
        "note": (
            "Activation emits explicit causal insertions only; downstream model "
            "effects are not applied by this endpoint."
        ),
    }


@app.post(
    "/api/admin/model-proof/resource-inventory",
    dependencies=[Depends(_facilitator_guard)],
)
def resource_inventory_model_proof(
    request: ResourceInventoryModelProofRequest,
) -> dict[str, object]:
    result = _domain_call(lambda: _resource_inventory_from_request(request))
    return result.to_dict()


@app.post(
    "/api/admin/model-proof/electrical-bus",
    dependencies=[Depends(_facilitator_guard)],
)
def electrical_bus_model_proof(
    request: ElectricalBusModelProofRequest,
) -> dict[str, object]:
    result = _domain_call(lambda: _electrical_bus_from_request(request))
    return result.to_dict()


@app.post(
    "/api/admin/model-proof/resource-power-observation",
    dependencies=[Depends(_facilitator_guard)],
)
def resource_power_observation_model_proof(
    request: ResourcePowerObservationChainRequest,
) -> dict[str, object]:
    """Run resource -> source -> bus/load -> tracking observation causality."""

    if request.electrical_bus.source_available:
        raise HTTPException(
            status_code=400,
            detail=(
                "resource-power-observation derives source availability from "
                "source_rules; electrical_bus.source_available must be empty"
            ),
        )

    resource = _domain_call(
        lambda: _resource_inventory_from_request(request.resource_inventory)
    )
    source_coupling = _domain_call(
        lambda: derive_electrical_source_availability(
            resource.final_state,
            [
                ResourceElectricalSourceRule(
                    source_id=rule.source_id,
                    resource_id=rule.resource_id,
                    minimum_operating_quantity=rule.minimum_operating_quantity,
                    available_at_threshold=rule.available_at_threshold,
                    provenance=rule.provenance,
                )
                for rule in request.source_rules
            ],
            upstream_availability=request.source_hardware_available,
        )
    )
    derived_source_available = {
        result.source_id: result.available for result in source_coupling
    }
    electrical = _domain_call(
        lambda: _electrical_bus_from_request(
            request.electrical_bus,
            source_available=derived_source_available,
        )
    )
    load_result = _domain_call(
        lambda: electrical.load(request.observation_load_id)
    )

    truth = _domain_call(
        lambda: compute_geometric_tracking_truth(
            TranslationalState(
                time_s=request.vehicle_time_s,
                position_m=tuple(request.vehicle_position_m),
                velocity_m_s=tuple(request.vehicle_velocity_m_s),
                mass_kg=request.vehicle_mass_kg,
            ),
            TrackingStationState(
                position_m=tuple(request.station_position_m),
                velocity_m_s=tuple(request.station_velocity_m_s),
            ),
        )
    )
    observation = _domain_call(
        lambda: produce_tracking_observation(
            truth,
            TrackingObservationConfig(
                receive_delay_s=request.observation.receive_delay_s,
                range_bias_m=request.observation.range_bias_m,
                range_rate_bias_m_s=request.observation.range_rate_bias_m_s,
                available=load_result.supplied,
                valid=load_result.supplied and request.observation.upstream_valid,
                source=request.observation.source,
                provenance=tuple(request.observation.provenance),
            ),
        )
    )

    return {
        "model_status": "resource_power_observation_chain_not_historically_validated",
        "resource_inventory": resource.to_dict(),
        "source_coupling": [result.to_dict() for result in source_coupling],
        "electrical_bus": electrical.to_dict(),
        "observation_load_id": request.observation_load_id,
        "tracking_observation": observation.to_dict(),
    }


@app.get("/api/session/audit", dependencies=[Depends(_facilitator_guard)])
def audit_log() -> list[dict[str, Any]]:
    with _lock:
        session = _sync_session()
        return [
            {
                "sequence": event.sequence,
                "get_s": event.get_s,
                "kind": event.kind,
                "actor": event.actor,
                "details": event.details,
            }
            for event in session.audit_log
        ]


@app.get("/", include_in_schema=False)
def index() -> FileResponse:
    return FileResponse(WEB_ROOT / "index.html")


@app.get("/player-lab", include_in_schema=False)
def player_interaction_lab() -> FileResponse:
    """Non-final FLIGHT/CAPCOM player-interaction prototype."""
    return FileResponse(WEB_ROOT / "player_lab.html")


@app.get("/admin", include_in_schema=False)
def admin_console() -> FileResponse:
    """Facilitator/SimSup validation console; API operations require authority."""
    return FileResponse(WEB_ROOT / "admin.html")
