from pathlib import Path
import json
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.decision_gate import (  # noqa: E402
    ControllerReadinessReport,
    CueEvidence,
    ReadinessCallState,
    assemble_decision_gate_snapshot,
)
from apollo_mission_control.decision_gate_profiles import (  # noqa: E402
    discover_decision_gate_profiles,
    get_decision_gate_profile,
    load_decision_gate_profile,
)


class DecisionGateContractTests(unittest.TestCase):
    def profile(self):
        return get_decision_gate_profile("apollo11_g_descent_landing_partial")

    def test_apollo11_profile_preserves_station_topology(self):
        profile = self.profile()
        self.assertEqual(profile.mission_profile_id, "apollo11_g")
        self.assertEqual(profile.decision_mode, "controller_judgment")
        self.assertEqual(profile.decision_authority, "FLIGHT")
        self.assertEqual(profile.relay_station, "CAPCOM")
        self.assertEqual(
            [item.historical_call_label for item in profile.poll_order],
            [
                "RETRO",
                "FIDO",
                "GUIDANCE",
                "CONTROL",
                "TELCOM",
                "GNC",
                "EECOM",
                "SURGEON",
            ],
        )
        self.assertEqual(
            profile.cue("control.lr_antenna_position").station_id,
            "CONTROL",
        )
        self.assertEqual(
            profile.cue("msk1137.pgns_altitude_ft").station_id,
            "GUIDO",
        )

    def test_snapshot_reports_completeness_without_issuing_decision(self):
        profile = self.profile()
        snapshot = assemble_decision_gate_snapshot(
            profile.to_contract(),
            cues={
                "msk1137.lr_range_status": CueEvidence(
                    value="GOOD",
                    provenance=("synthetic test observation",),
                ),
                "control.lr_antenna_position": CueEvidence(
                    value=2,
                    provenance=("synthetic test observation",),
                ),
            },
            readiness_reports=(
                ControllerReadinessReport(
                    "GUIDO",
                    ReadinessCallState.GO,
                    "synthetic guidance report",
                ),
                ControllerReadinessReport(
                    "CONTROL",
                    ReadinessCallState.GO,
                    "synthetic control report",
                ),
            ),
        )
        self.assertFalse(snapshot.cue_coverage_complete)
        self.assertFalse(snapshot.poll_complete)
        payload = snapshot.to_dict()
        self.assertTrue(payload["controller_decision_required"])
        self.assertNotIn("mission_decision", payload)
        self.assertNotIn("go_for_landing", payload)
        self.assertNotIn("abort", payload)

    def test_complete_poll_still_requires_explicit_controller_decision(self):
        profile = self.profile()
        contract = profile.to_contract()
        cues = {
            cue_id: CueEvidence(
                value="synthetic",
                provenance=("synthetic test observation",),
            )
            for cue_id in contract.cue_owners
        }
        reports = tuple(
            ControllerReadinessReport(
                station,
                ReadinessCallState.GO,
                "synthetic report",
            )
            for station in contract.poll_stations
        )
        snapshot = assemble_decision_gate_snapshot(
            contract,
            cues=cues,
            readiness_reports=reports,
        )
        self.assertTrue(snapshot.cue_coverage_complete)
        self.assertTrue(snapshot.poll_complete)
        payload = snapshot.to_dict()
        self.assertTrue(payload["controller_decision_required"])
        self.assertNotIn("mission_decision", payload)

    def test_unknown_or_duplicate_reports_are_rejected(self):
        contract = self.profile().to_contract()
        with self.assertRaisesRegex(ValueError, "not in gate poll order"):
            assemble_decision_gate_snapshot(
                contract,
                readiness_reports=(
                    ControllerReadinessReport(
                        "UNKNOWN",
                        ReadinessCallState.GO,
                    ),
                ),
            )
        with self.assertRaisesRegex(ValueError, "duplicate readiness report"):
            assemble_decision_gate_snapshot(
                contract,
                readiness_reports=(
                    ControllerReadinessReport("GUIDO", ReadinessCallState.GO),
                    ControllerReadinessReport("GUIDO", ReadinessCallState.GO),
                ),
            )

    def test_profile_loader_rejects_automatic_decision_mode(self):
        payload = {
            "profile_id": "bad",
            "mission_profile_id": "synthetic",
            "gate_id": "gate",
            "status": "test",
            "phase_context": "test",
            "decision_mode": "automatic",
            "decision_authority": "FLIGHT",
            "relay_station": "CAPCOM",
            "cues": [
                {
                    "cue_id": "cue",
                    "station_id": "GUIDO",
                    "historical_call_label": "GUIDANCE",
                    "evidence_kind": "display_field",
                    "source_reference": "synthetic",
                    "semantics": "synthetic",
                    "provenance": ["synthetic"],
                }
            ],
            "poll_order": [
                {
                    "station_id": "GUIDO",
                    "historical_call_label": "GUIDANCE",
                }
            ],
            "rule_references": [],
            "unresolved": [],
            "sources": ["synthetic"],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "controller_judgment"):
                load_decision_gate_profile(path)

    def test_profile_discovery_is_unique(self):
        records = discover_decision_gate_profiles()
        ids = [item.profile_id for item in records]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertIn("apollo11_g_descent_landing_partial", ids)


if __name__ == "__main__":
    unittest.main()
