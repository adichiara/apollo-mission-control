from math import cos, radians, sin
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.propulsion_dynamics import (  # noqa: E402
    BurnSegment,
    PropulsionModel,
    PropulsionState,
    UNIT_X,
    Vector3,
    command_propulsion,
    delta_v_vector,
    lbf_to_newtons,
    meters_per_second_to_feet_per_second,
    pounds_mass_to_kg,
    run_burn_segments,
    step_propulsion,
)


class PropulsionDynamicsTests(unittest.TestCase):
    def setUp(self):
        self.model = PropulsionModel(
            full_thrust_n=lbf_to_newtons(10_000.0),
            specific_impulse_s=300.0,
        )
        self.initial = PropulsionState(
            elapsed_s=0.0,
            mass_kg=pounds_mass_to_kg(100_000.0),
        )

    def test_command_changes_configuration_without_advancing_physics(self):
        commanded = command_propulsion(
            self.initial,
            engine_running=True,
            throttle_fraction=0.4,
        )
        self.assertEqual(commanded.elapsed_s, 0.0)
        self.assertEqual(commanded.mass_kg, self.initial.mass_kg)
        self.assertEqual(commanded.velocity_m_s, self.initial.velocity_m_s)
        self.assertTrue(commanded.engine_running)
        self.assertEqual(commanded.throttle_fraction, 0.4)

    def test_engine_off_elapsed_time_does_not_create_impulse(self):
        final = step_propulsion(self.initial, self.model, 30.0)
        self.assertEqual(final.elapsed_s, 30.0)
        self.assertEqual(final.mass_kg, self.initial.mass_kg)
        self.assertEqual(final.velocity_m_s, self.initial.velocity_m_s)
        self.assertEqual(final.accumulated_impulse_n_s, 0.0)

    def test_early_and_late_cutoff_emerge_from_same_model(self):
        early = run_burn_segments(
            self.initial,
            self.model,
            [BurnSegment(duration_s=100.0, throttle_fraction=1.0)],
        )
        nominal = run_burn_segments(
            self.initial,
            self.model,
            [BurnSegment(duration_s=200.0, throttle_fraction=1.0)],
        )
        late = run_burn_segments(
            self.initial,
            self.model,
            [BurnSegment(duration_s=250.0, throttle_fraction=1.0)],
        )

        self.assertLess(
            delta_v_vector(self.initial.velocity_m_s, early).magnitude(),
            delta_v_vector(self.initial.velocity_m_s, nominal).magnitude(),
        )
        self.assertLess(
            delta_v_vector(self.initial.velocity_m_s, nominal).magnitude(),
            delta_v_vector(self.initial.velocity_m_s, late).magnitude(),
        )
        self.assertLess(early.propellant_used_kg, nominal.propellant_used_kg)
        self.assertLess(nominal.propellant_used_kg, late.propellant_used_kg)
        self.assertGreater(early.mass_kg, nominal.mass_kg)
        self.assertGreater(nominal.mass_kg, late.mass_kg)

    def test_wrong_throttle_changes_consequence_without_branching(self):
        low = run_burn_segments(
            self.initial,
            self.model,
            [BurnSegment(duration_s=120.0, throttle_fraction=0.4)],
        )
        full = run_burn_segments(
            self.initial,
            self.model,
            [BurnSegment(duration_s=120.0, throttle_fraction=1.0)],
        )

        self.assertLess(
            delta_v_vector(self.initial.velocity_m_s, low).magnitude(),
            delta_v_vector(self.initial.velocity_m_s, full).magnitude(),
        )
        self.assertLess(low.propellant_used_kg, full.propellant_used_kg)

    def test_wrong_attitude_rotates_vector_delta_v(self):
        angle = radians(10.0)
        nominal_direction = UNIT_X
        wrong_direction = Vector3(cos(angle), sin(angle), 0.0)

        nominal = run_burn_segments(
            self.initial,
            self.model,
            [
                BurnSegment(
                    duration_s=120.0,
                    throttle_fraction=1.0,
                    thrust_direction=nominal_direction,
                )
            ],
        )
        wrong = run_burn_segments(
            self.initial,
            self.model,
            [
                BurnSegment(
                    duration_s=120.0,
                    throttle_fraction=1.0,
                    thrust_direction=wrong_direction,
                )
            ],
        )

        nominal_dv = delta_v_vector(self.initial.velocity_m_s, nominal)
        wrong_dv = delta_v_vector(self.initial.velocity_m_s, wrong)

        self.assertAlmostEqual(nominal_dv.magnitude(), wrong_dv.magnitude(), places=9)
        self.assertAlmostEqual(nominal_dv.y, 0.0, places=12)
        self.assertGreater(wrong_dv.y, 0.0)
        self.assertLess(wrong_dv.x, nominal_dv.x)

    def test_combined_error_uses_same_segment_interface(self):
        angle = radians(-7.0)
        final = run_burn_segments(
            self.initial,
            self.model,
            [
                BurnSegment(
                    duration_s=5.0,
                    throttle_fraction=0.126,
                    thrust_direction=Vector3(cos(angle), sin(angle), 0.0),
                ),
                BurnSegment(
                    duration_s=26.0,
                    throttle_fraction=0.4,
                    thrust_direction=Vector3(cos(angle), sin(angle), 0.0),
                ),
                BurnSegment(
                    duration_s=180.0,
                    throttle_fraction=0.85,
                    thrust_direction=Vector3(cos(angle), sin(angle), 0.0),
                ),
            ],
            step_s=0.25,
        )
        dv = delta_v_vector(self.initial.velocity_m_s, final)
        self.assertGreater(dv.magnitude(), 0.0)
        self.assertLess(dv.y, 0.0)
        self.assertGreater(final.propellant_used_kg, 0.0)

    def test_step_refinement_is_numerically_stable_for_level_one(self):
        segments = [
            BurnSegment(duration_s=5.0, throttle_fraction=0.126),
            BurnSegment(duration_s=21.0, throttle_fraction=0.4),
            BurnSegment(duration_s=120.0, throttle_fraction=1.0),
        ]
        coarse = run_burn_segments(
            self.initial,
            self.model,
            segments,
            step_s=1.0,
        )
        fine = run_burn_segments(
            self.initial,
            self.model,
            segments,
            step_s=0.05,
        )
        self.assertAlmostEqual(coarse.mass_kg, fine.mass_kg, places=7)
        self.assertAlmostEqual(
            coarse.velocity_m_s.x,
            fine.velocity_m_s.x,
            places=7,
        )
        self.assertAlmostEqual(
            coarse.accumulated_impulse_n_s,
            fine.accumulated_impulse_n_s,
            places=5,
        )

    def test_units_round_trip(self):
        dv_m_s = 100.0
        self.assertAlmostEqual(
            meters_per_second_to_feet_per_second(dv_m_s),
            328.0839895013123,
        )


if __name__ == "__main__":
    unittest.main()
