import json
import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from apollo_mission_control.causal_dps_model import DPSModelConfig, ManeuverState
from apollo_mission_control.dps_test_session import DPSTestSession


class StatefulTests(unittest.TestCase):
    def make(self):
        return DPSTestSession(ManeuverState(0, 10000, (0, 0, 0)),
                              DPSModelConfig(300, 5000))

    def test_commands_affect_only_subsequent_time(self):
        s = self.make()
        s.set_command(10000, (1, 0, 0), expected_revision=0)
        self.assertEqual(s.state.velocity_m_s, (0, 0, 0))
        s.advance(20, expected_revision=1)
        before = s.state
        s.set_command(8000, (0, 1, 0), expected_revision=2)
        self.assertEqual(s.state, before)
        s.advance(30, expected_revision=3)
        self.assertEqual(s.state.velocity_m_s[0], before.velocity_m_s[0])
        self.assertGreater(s.state.velocity_m_s[1], 0)
        s.set_command(0, (0, 0, 0), expected_revision=4)
        velocity = s.state.velocity_m_s
        s.advance(10, expected_revision=5)
        self.assertEqual(s.state.velocity_m_s, velocity)
        report = json.loads(json.dumps(s.export()))
        replay = DPSTestSession.replay(report)
        self.assertEqual(replay.snapshot(), s.snapshot())

    def test_rejection_is_atomic_and_revision_protected(self):
        s = self.make()
        before = s.export()
        with self.assertRaisesRegex(ValueError, "stale"):
            s.advance(10, expected_revision=1)
        self.assertEqual(s.export(), before)
        s.set_command(1000000, (1, 0, 0), expected_revision=0)
        before = s.export()
        with self.assertRaisesRegex(ValueError, "dry_mass"):
            s.advance(100, expected_revision=1)
        self.assertEqual(s.export(), before)

    def test_export_is_detached_and_work_is_bounded(self):
        s = self.make()
        report = s.export()
        report["events"].append({"kind": "fake"})
        self.assertEqual(s.events, [])
        for duration in (0, -1, float("nan"), float("inf"), 3601):
            with self.assertRaises(ValueError):
                s.advance(duration, expected_revision=0)
        self.assertEqual(s.events, [])
