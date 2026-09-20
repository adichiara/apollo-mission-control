"""Historical landing-radar profile catalog."""
from __future__ import annotations
from dataclasses import dataclass
import json
from math import tau
from pathlib import Path
from typing import Any
from .landing_radar_data_good import LandingRadarDataGoodTransition
from .landing_radar_velocity_chain import LandingRadarBeamGeometryInput
from .landing_radar_velocity_update import LandingRadarVelocityWeightConfig

ROOT = Path(__file__).resolve().parents[2]
LANDING_RADAR_PROFILE_ROOT = ROOT / "data" / "landing_radar_profiles"
FT_TO_M = 0.3048

def _text(data: dict[str, Any], key: str) -> str:
    value=data.get(key)
    if not isinstance(value,str) or not value.strip(): raise ValueError(f"landing-radar profile {key!r} must be a non-empty string")
    return value.strip()

def _number(data: dict[str, Any], key: str, *, nonnegative: bool=True) -> float:
    value=data.get(key)
    if isinstance(value,bool) or not isinstance(value,(int,float)): raise ValueError(f"landing-radar profile {key!r} must be numeric")
    number=float(value)
    if nonnegative and number<0: raise ValueError(f"landing-radar profile {key!r} must be non-negative")
    return number

def _weight_map(data: Any,key:str)->dict[str,float]:
    if not isinstance(data,dict) or not data: raise ValueError(f"landing-radar profile {key!r} must be a non-empty object")
    result={}
    for name,value in data.items():
        if not isinstance(name,str) or not name.strip() or isinstance(value,bool) or not isinstance(value,(int,float)): raise ValueError(f"invalid {key} entry")
        if float(value)<0: raise ValueError(f"landing-radar profile {key!r} weights must be non-negative")
        result[name.strip().lower()]=float(value)
    return result

@dataclass(frozen=True)
class LandingRadarVelocityWeightingProfile:
    maximum_speed_fps: float; low_speed_threshold_fps: float; linear_component_weights: dict[str,float]; low_speed_component_weights: dict[str,float]; override_programs: tuple[str,...]; override_weight: float; evidence_note: str
    def to_config(self,provenance:tuple[str,...])->LandingRadarVelocityWeightConfig:
        return LandingRadarVelocityWeightConfig(maximum_speed_m_s=self.maximum_speed_fps*FT_TO_M,low_speed_threshold_m_s=self.low_speed_threshold_fps*FT_TO_M,linear_component_weights=self.linear_component_weights,low_speed_component_weights=self.low_speed_component_weights,override_programs=self.override_programs,override_weight=self.override_weight,applicability="Apollo 11 LM-5 landing-radar velocity weighting",provenance=provenance,assumptions=("thresholds and weights are from the LM-5 Mission G LUMINARY 99 erasable load","piecewise selection and P65/P66/P67 override follow flown LUMINARY 099 SERVICER logic","input residual and beam vector are supplied by upstream Apollo landing-radar stages"))
    def to_public_dict(self)->dict[str,object]: return {"maximum_speed_fps":self.maximum_speed_fps,"low_speed_threshold_fps":self.low_speed_threshold_fps,"linear_component_weights":dict(self.linear_component_weights),"low_speed_component_weights":dict(self.low_speed_component_weights),"override_programs":list(self.override_programs),"override_weight":self.override_weight,"evidence_note":self.evidence_note}

@dataclass(frozen=True)
class LandingRadarGeometryPositionProfile:
    position:int; name:str; alpha_rev:float; beta_rev:float
    def beam_geometry(self,*,cdu_y_rad:float,cdu_z_rad:float,cdu_x_rad:float)->LandingRadarBeamGeometryInput:
        return LandingRadarBeamGeometryInput(alpha_rad=self.alpha_rev*tau,beta_rad=self.beta_rev*tau,cdu_y_rad=cdu_y_rad,cdu_z_rad=cdu_z_rad,cdu_x_rad=cdu_x_rad)
    def to_public_dict(self)->dict[str,object]: return {"position":self.position,"name":self.name,"alpha_rev":self.alpha_rev,"beta_rev":self.beta_rev}

@dataclass(frozen=True)
class LandingRadarProfileRecord:
    profile_id:str; mission_profile_id:str; status:str; velocity_weighting:LandingRadarVelocityWeightingProfile|None; geometry_positions:dict[int,LandingRadarGeometryPositionProfile]; geometry_evidence_note:str|None; data_good_min_duration_s:float; historical_data_good_transitions:tuple[LandingRadarDataGoodTransition,...]; unresolved:tuple[str,...]; sources:tuple[str,...]; profile_path:Path
    def velocity_update_config(self)->LandingRadarVelocityWeightConfig:
        if self.velocity_weighting is None: raise ValueError(f"landing-radar profile {self.profile_id!r} has no velocity weighting")
        return self.velocity_weighting.to_config(self.sources)
    def beam_geometry(self,position:int,*,cdu_y_rad:float,cdu_z_rad:float,cdu_x_rad:float)->LandingRadarBeamGeometryInput:
        try: item=self.geometry_positions[int(position)]
        except (KeyError,ValueError) as exc: raise ValueError(f"landing-radar profile {self.profile_id!r} has no geometry for position {position!r}") from exc
        return item.beam_geometry(cdu_y_rad=cdu_y_rad,cdu_z_rad=cdu_z_rad,cdu_x_rad=cdu_x_rad)
    def to_public_dict(self)->dict[str,object]:
        return {"profile_id":self.profile_id,"mission_profile_id":self.mission_profile_id,"status":self.status,"velocity_update_weighting":None if self.velocity_weighting is None else self.velocity_weighting.to_public_dict(),"landing_radar_geometry":{"positions":{str(k):v.to_public_dict() for k,v in sorted(self.geometry_positions.items())},"evidence_note":self.geometry_evidence_note} if self.geometry_positions else None,"data_good_min_duration_s":self.data_good_min_duration_s,"historical_data_good_transitions":[item.to_dict() for item in self.historical_data_good_transitions],"unresolved":list(self.unresolved),"sources":list(self.sources)}

def _velocity_weighting(payload:Any)->LandingRadarVelocityWeightingProfile|None:
    if payload is None:return None
    if not isinstance(payload,dict):raise ValueError("velocity_update_weighting must be an object or null")
    programs=payload.get("override_programs",[])
    if not isinstance(programs,list) or not all(isinstance(x,str) and x.strip() for x in programs):raise ValueError("override_programs must be a list of non-empty strings")
    return LandingRadarVelocityWeightingProfile(_number(payload,"maximum_speed_fps"),_number(payload,"low_speed_threshold_fps"),_weight_map(payload.get("linear_component_weights"),"linear_component_weights"),_weight_map(payload.get("low_speed_component_weights"),"low_speed_component_weights"),tuple(x.strip().upper() for x in programs),_number(payload,"override_weight"),_text(payload,"evidence_note"))

def _geometry(payload:Any)->tuple[dict[int,LandingRadarGeometryPositionProfile],str|None]:
    if payload is None:return {},None
    if not isinstance(payload,dict) or payload.get("angle_unit")!="revolution":raise ValueError("landing_radar_geometry must use source angle_unit 'revolution'")
    positions=payload.get("positions")
    if not isinstance(positions,dict) or not positions:raise ValueError("landing_radar_geometry positions must be a non-empty object")
    result={}
    for key,item in positions.items():
        if not isinstance(item,dict):raise ValueError("landing_radar_geometry position must be an object")
        pos=int(key); result[pos]=LandingRadarGeometryPositionProfile(pos,_text(item,"name"),_number(item,"alpha_rev"),_number(item,"beta_rev"))
    return result,_text(payload,"evidence_note")

def _data_good_transitions(payload:Any)->tuple[LandingRadarDataGoodTransition,...]:
    if payload is None:return ()
    if not isinstance(payload,list):raise ValueError("historical_data_good_transitions must be a list")
    result=[]
    for item in payload:
        if not isinstance(item,dict):raise ValueError("historical DATA GOOD transition must be an object")
        data_good=item.get("data_good")
        if not isinstance(data_good,bool):raise ValueError("historical DATA GOOD transition data_good must be boolean")
        resolution=item.get("source_resolution_s")
        if resolution is not None and (isinstance(resolution,bool) or not isinstance(resolution,(int,float))):raise ValueError("source_resolution_s must be numeric or null")
        provenance=item.get("provenance",[])
        if not isinstance(provenance,list) or not all(isinstance(x,str) and x.strip() for x in provenance):raise ValueError("historical DATA GOOD transition provenance must be strings")
        result.append(LandingRadarDataGoodTransition(time_s=_number(item,"time_s"),data_good=data_good,label=_text(item,"label"),source_resolution_s=None if resolution is None else float(resolution),provenance=tuple(x.strip() for x in provenance)).validated())
    times=[item.time_s for item in result]
    if times!=sorted(times) or len(times)!=len(set(times)):raise ValueError("historical DATA GOOD transitions must have unique ascending times")
    return tuple(result)

def load_landing_radar_profile(path:str|Path)->LandingRadarProfileRecord:
    profile_path=Path(path)
    try:data=json.loads(profile_path.read_text(encoding="utf-8"))
    except (OSError,json.JSONDecodeError) as exc:raise ValueError(f"cannot load landing-radar profile {profile_path}: {exc}") from exc
    if not isinstance(data,dict):raise ValueError("landing-radar profile must contain a JSON object")
    unresolved=data.get("unresolved",[]); sources=data.get("sources",[])
    if not isinstance(unresolved,list) or not all(isinstance(x,str) and x.strip() for x in unresolved):raise ValueError("landing-radar profile unresolved must be strings")
    if not isinstance(sources,list) or not all(isinstance(x,str) and x.strip() for x in sources):raise ValueError("landing-radar profile sources must be strings")
    geometry,note=_geometry(data.get("landing_radar_geometry"))
    record=LandingRadarProfileRecord(_text(data,"profile_id"),_text(data,"mission_profile_id"),_text(data,"status"),_velocity_weighting(data.get("velocity_update_weighting")),geometry,note,_number(data,"data_good_min_duration_s"),_data_good_transitions(data.get("historical_data_good_transitions")),tuple(x.strip() for x in unresolved),tuple(x.strip() for x in sources),profile_path)
    if record.velocity_weighting is not None:record.velocity_update_config().validated()
    return record

def discover_landing_radar_profiles(root:str|Path=LANDING_RADAR_PROFILE_ROOT)->tuple[LandingRadarProfileRecord,...]:
    records=tuple(load_landing_radar_profile(p) for p in sorted(Path(root).glob("*.json"))); ids=[r.profile_id for r in records]
    if len(ids)!=len(set(ids)):raise ValueError("duplicate landing-radar profile_id")
    return records

def get_landing_radar_profile(profile_id:str,root:str|Path=LANDING_RADAR_PROFILE_ROOT)->LandingRadarProfileRecord:
    requested=str(profile_id).strip()
    if not requested:raise ValueError("profile_id must not be empty")
    for record in discover_landing_radar_profiles(root):
        if record.profile_id==requested:return record
    raise ValueError(f"unknown landing-radar profile_id: {requested}")
