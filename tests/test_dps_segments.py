import unittest
import sys
from pathlib import Path
from math import log
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from apollo_mission_control.causal_dps_model import (
    BurnSegment, DPSModelConfig, ManeuverState, simulate_dps_maneuver)


class SegmentTests(unittest.TestCase):
    def test_staged_vector_against_independent_analytic_solution(self):
        initial = ManeuverState(0, 10000, (0, 0, 0))
        segments = [BurnSegment(20, 4000, (1, 0, 0)),
                    BurnSegment(10, 0, (0, 0, 0)),
                    BurnSegment(30, 8000, (0, 1, 0))]
        result = simulate_dps_maneuver(initial, segments, DPSModelConfig(300, 5000))
        e = 300 * 9.80665
        m1 = 10000 - 80000 / e
        m2 = m1 - 240000 / e
        for actual, expected in zip(result.delta_v_m_s,
                                    (e*log(10000/m1), e*log(m1/m2), 0)):
            self.assertAlmostEqual(actual, expected, delta=1e-6)
        self.assertAlmostEqual(result.final_state.mass_kg, m2, delta=1e-6)
        self.assertEqual(result.elapsed_s, 60)

    def test_cutoff_coast_and_resumed_state(self):
        initial = ManeuverState(0, 10000, (0, 0, 0))
        config = DPSModelConfig(300, 5000)
        burn = BurnSegment(80, 10000, (1, 0, 0))
        coast = BurnSegment(20, 0, (0, 0, 0))
        first = simulate_dps_maneuver(initial, [burn], config)
        resumed = simulate_dps_maneuver(first.final_state, [coast], config)
        whole = simulate_dps_maneuver(initial, [burn, coast], config)
        self.assertEqual(resumed.final_state, whole.final_state)
        self.assertEqual(first.delta_v_m_s, whole.delta_v_m_s)

    def test_propellant_limit_rejection_does_not_mutate_input(self):
        initial = ManeuverState(0, 10000, (0, 0, 0))
        with self.assertRaisesRegex(ValueError, "dry_mass_kg"):
            simulate_dps_maneuver(initial, [BurnSegment(100, 10000, (1, 0, 0))],
                                  DPSModelConfig(300, 9999))
        self.assertEqual(initial.mass_kg, 10000)
