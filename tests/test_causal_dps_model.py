from math import log
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.causal_dps_model import (  # noqa: E402
    STANDARD_GRAVITY_M_S2,
    BurnSegment,
    DPSModelConfig,
    ManeuverState,
    simulate_dps_maneuver,
)


class CausalDPSModelTests(unittest.TestCase):
    def run_profile(self, segments, *, step=0.25):
        return simulate_dps_maneuver(
            ManeuverState(time_s=100.0, mass_kg=10_000.0, velocity_m_s=(0.0, 0.0, 0.0)),
            segments,
            DPSModelConfig(
                specific_impulse_s=300.0,
                dry_mass_kg=5_000.0,
                max_step_s=step,
                applicability="unit-test generic vehicle",
                provenance=("test fixture; not historical evidence",),
            ),
        )

    def test_constant_thrust_matches_mass_and_converges_to_rocket_equation(self):
        coarse = self.run_profile([BurnSegment(100.0, 10_000.0, (1.0, 0.0, 0.0))], step=5.0)
        fine = self.run_profile([BurnSegment(100.0, 10_000.0, (1.0, 0.0, 0.0))], step=0.1)
        expected_mass = 10_000.0 - 10_000.0 / (300.0 * STANDARD_GRAVITY_M_S2) * 100.0
        expected_dv = 300.0 * STANDARD_GRAVITY_M_S2 * log(10_000.0 / expected_mass)

        self.assertAlmostEqual(fine.final_state.mass_kg, expected_mass, places=9)
        self.assertAlmostEqual(fine.impulse_n_s, 1_000_000.0, places=6)
        self.assertLess(abs(fine.delta_v_m_s[0] - expected_dv), abs(coarse.delta_v_m_s[0] - expected_dv))
        self.assertAlmostEqual(fine.delta_v_m_s[0], expected_dv, places=6)

    def test_correct_early_late_and_wrong_throttle_share_one_model(self):
        correct = self.run_profile([BurnSegment(100.0, 10_000.0, (1.0, 0.0, 0.0))])
        early = self.run_profile([BurnSegment(80.0, 10_000.0, (1.0, 0.0, 0.0))])
        late = self.run_profile([BurnSegment(120.0, 10_000.0, (1.0, 0.0, 0.0))])
        low_throttle = self.run_profile([BurnSegment(100.0, 7_000.0, (1.0, 0.0, 0.0))])

        self.assertLess(early.delta_v_magnitude_m_s, correct.delta_v_magnitude_m_s)
        self.assertLess(correct.delta_v_magnitude_m_s, late.delta_v_magnitude_m_s)
        self.assertLess(low_throttle.delta_v_magnitude_m_s, correct.delta_v_magnitude_m_s)
        self.assertGreater(early.final_state.mass_kg, correct.final_state.mass_kg)
        self.assertGreater(correct.final_state.mass_kg, late.final_state.mass_kg)

    def test_direction_is_normalized_and_changes_vector_not_scalar_result(self):
        axial = self.run_profile([BurnSegment(60.0, 10_000.0, (1.0, 0.0, 0.0))])
        offset = self.run_profile([BurnSegment(60.0, 10_000.0, (1.0, 1.0, 0.0))])

        self.assertAlmostEqual(axial.delta_v_magnitude_m_s, offset.delta_v_magnitude_m_s, places=10)
        self.assertGreater(offset.delta_v_m_s[1], 0.0)
        self.assertLess(offset.delta_v_m_s[0], axial.delta_v_m_s[0])

    def test_combined_error_needs_no_special_branch(self):
        result = self.run_profile([
            BurnSegment(20.0, 4_000.0, (1.0, 0.0, 0.0)),
            BurnSegment(65.0, 8_000.0, (0.98, 0.2, 0.0)),
        ])
        self.assertEqual(result.elapsed_s, 85.0)
        self.assertGreater(result.delta_v_m_s[0], 0.0)
        self.assertGreater(result.delta_v_m_s[1], 0.0)
        self.assertEqual(result.to_dict()["model_status"], "level_1_model_proof_not_historically_validated")

    def test_zero_thrust_coasts_without_mass_or_velocity_change(self):
        result = self.run_profile([BurnSegment(10.0, 0.0, (0.0, 0.0, 0.0))])
        self.assertEqual(result.final_state.mass_kg, 10_000.0)
        self.assertEqual(result.delta_v_m_s, (0.0, 0.0, 0.0))
        self.assertEqual(result.impulse_n_s, 0.0)

    def test_run_is_deterministic(self):
        profile = [BurnSegment(7.25, 9_000.0, (0.2, -0.4, 0.8))]
        first = self.run_profile(profile)
        second = self.run_profile(profile)
        self.assertEqual(first, second)


    def test_linear_thrust_profile_has_expected_impulse_and_propellant_use(self):
        result = self.run_profile([
            BurnSegment(
                10.0,
                0.0,
                (1.0, 0.0, 0.0),
                end_thrust_n=10_000.0,
                regime="startup",
            )
        ])
        expected_impulse = 50_000.0
        expected_propellant = expected_impulse / (300.0 * STANDARD_GRAVITY_M_S2)

        self.assertAlmostEqual(result.impulse_n_s, expected_impulse, places=9)
        self.assertAlmostEqual(result.propellant_used_kg, expected_propellant, places=9)
        self.assertGreater(result.delta_v_m_s[0], 0.0)

    def test_split_linear_profile_is_invariant_at_same_step_grid(self):
        whole = self.run_profile([
            BurnSegment(
                10.0,
                0.0,
                (1.0, 0.0, 0.0),
                end_thrust_n=10_000.0,
                regime="startup",
            )
        ])
        split = self.run_profile([
            BurnSegment(
                5.0,
                0.0,
                (1.0, 0.0, 0.0),
                end_thrust_n=5_000.0,
                regime="startup",
            ),
            BurnSegment(
                5.0,
                5_000.0,
                (1.0, 0.0, 0.0),
                end_thrust_n=10_000.0,
                regime="startup",
            ),
        ])

        self.assertAlmostEqual(whole.impulse_n_s, split.impulse_n_s, places=9)
        self.assertAlmostEqual(
            whole.final_state.mass_kg,
            split.final_state.mass_kg,
            places=9,
        )
        self.assertAlmostEqual(
            whole.delta_v_m_s[0],
            split.delta_v_m_s[0],
            places=12,
        )

    def test_segment_specific_isp_changes_mass_not_impulse(self):
        baseline = self.run_profile([
            BurnSegment(10.0, 10_000.0, (1.0, 0.0, 0.0))
        ])
        lower_isp = self.run_profile([
            BurnSegment(
                10.0,
                10_000.0,
                (1.0, 0.0, 0.0),
                specific_impulse_s=250.0,
                regime="alternate-performance",
            )
        ])

        self.assertAlmostEqual(baseline.impulse_n_s, lower_isp.impulse_n_s, places=9)
        self.assertLess(lower_isp.final_state.mass_kg, baseline.final_state.mass_kg)
        self.assertGreater(
            lower_isp.delta_v_magnitude_m_s,
            baseline.delta_v_magnitude_m_s,
        )

    def test_rejects_invalid_inputs_and_dry_mass_violation(self):
        with self.assertRaisesRegex(ValueError, "non-zero"):
            self.run_profile([BurnSegment(1.0, 1.0, (0.0, 0.0, 0.0))])
        with self.assertRaisesRegex(ValueError, "dry_mass"):
            simulate_dps_maneuver(
                ManeuverState(0.0, 10.0, (0.0, 0.0, 0.0)),
                [BurnSegment(10.0, 10_000.0, (1.0, 0.0, 0.0))],
                DPSModelConfig(specific_impulse_s=1.0, dry_mass_kg=9.0),
            )
        with self.assertRaisesRegex(ValueError, "end_thrust_n"):
            self.run_profile([
                BurnSegment(
                    1.0,
                    0.0,
                    (1.0, 0.0, 0.0),
                    end_thrust_n=-1.0,
                )
            ])
        with self.assertRaisesRegex(ValueError, "direction must be non-zero"):
            self.run_profile([
                BurnSegment(
                    1.0,
                    0.0,
                    (0.0, 0.0, 0.0),
                    end_thrust_n=1.0,
                )
            ])
        with self.assertRaisesRegex(ValueError, "specific_impulse_s"):
            self.run_profile([
                BurnSegment(
                    1.0,
                    1.0,
                    (1.0, 0.0, 0.0),
                    specific_impulse_s=0.0,
                )
            ])


if __name__ == "__main__":
    unittest.main()
