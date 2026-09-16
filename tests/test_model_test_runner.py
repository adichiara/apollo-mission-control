from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from fastapi.testclient import TestClient
from apollo_mission_control.live_app import app


class ModelTestRunnerTests(unittest.TestCase):
    def test_route_and_report_contract(self):
        response = TestClient(app).get("/model-tests")
        self.assertEqual(response.status_code, 200)
        for required in ("Download report", "Copy report", "schema_version",
                         "build_before", "build_after", "rocket equation",
                         "step refinement", "INCOMPLETE", "AbortController",
                         "Causal Model Lab", "PC+2 correct / late / omitted / wrong action matrix", "PC+2 inverter action / observation consequence matrix", "Trajectory → tracking observation",
                         "Exercise malfunction → explicit causal insertions",
                         "Resource → power → observation",
                         "/api/admin/model-proof/pc2-action-consequences",
                         "/api/admin/model-proof/pc2-inverter-consequences",
                         "/api/admin/model-proof/trajectory-tracking",
                         "/api/admin/model-proof/malfunction-plan",
                         "/api/admin/model-proof/resource-power-observation",
                         "/api/admin/model-proof/guidance-alarm",
                         "/api/admin/model-proof/guidance-crosscheck",
                         "/api/admin/model-proof/guidance-consensus",
                         "/api/admin/model-proof/landing-radar-quality-update",
                         "Guidance-computer alarm → restart recovery",
                         "Guidance comparison / multi-source consensus",
                         "Landing-radar quality → update eligibility",
                         "Authoritative trajectory", "Controller-visible observation",
                         "causal_runs"):
            self.assertIn(required, response.text)
        self.assertNotIn("/api/session/create", response.text)
        self.assertNotIn("/api/session/advance", response.text)
        self.assertIn("/api/admin/model-proof/dps-burn", response.text)
        self.assertIn("notes:$('notes').value", response.text)
        self.assertNotIn("token:", response.text)
