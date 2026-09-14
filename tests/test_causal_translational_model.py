from math import pi, sqrt
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.causal_dps_model import BurnSegment  # noqa: E402
from apollo_mission_control.causal_translational_model import (  # noqa: E402
    TranslationalConfig,
    TranslationalState,
    simulate_translational_maneuver,
)


class TranslationalModelTests(unittest.TestCase):
    def test_zero_gravity_coast_is_exact_straight_line(self):
        result = simulate_translational_maneuver(
            TranslationalState(
                time_s=10.0,
                position_m=(100.0, -50.0, 25.0),
                velocity_m_s=(2.0, 3.0, -1.0),
                mass_kg=1000.0,
            ),
            [BurnSegment(20.0, 0.0, (0.0, 0.0, 0.0), regime="coast")],
            TranslationalConfig(
                specific_impulse_s=300.0,
                dry_mass_kg=500.0,
                max_step_s=7.0,
            ),
        )

        for actual, expected in zip(
            result.final_state.position_m,
            (140.0, 10.0, 5.0),
        ):
            self.assertAlmostEqual(actual, expected, places=12)
        for actual, expected in zip(
            result.final_state.velocity_m_s,
            (2.0, 3.0, -1.0),
        ):
            self.assertAlmostEqual(actual, expected, places=12)
        self.assertEqual(result.final_state.mass_kg, 1000.0)
        self.assertEqual(result.propulsive_impulse_n_s, 0.0)

    def test_zero_gravity_thrust_changes_position_velocity_and_mass(self):
        result = simulate_translational_maneuver(
            TranslationalState(
                time_s=0.0,
                position_m=(0.0, 0.0, 0.0),
                velocity_m_s=(0.0, 0.0, 0.0),
                mass_kg=10_000.0,
            ),
            [BurnSegment(10.0, 10_000.0, (1.0, 0.0, 0.0))],
            TranslationalConfig(
                specific_impulse_s=300.0,
                dry_mass_kg=5_000.0,
                max_step_s=0.1,
            ),
        )

        self.assertGreater(result.final_state.position_m[0], 0.0)
        self.assertGreater(result.final_state.velocity_m_s[0], 0.0)
        self.assertEqual(result.final_state.position_m[1:], (0.0, 0.0))
        self.assertLess(result.final_state.mass_kg, 10_000.0)
        self.assertAlmostEqual(result.propulsive_impulse_n_s, 100_000.0, places=7)

    def test_linear_thrust_impulse_is_step_size_invariant(self):
        kwargs = dict(
            initial_state=TranslationalState(
                time_s=0.0,
                position_m=(0.0, 0.0, 0.0),
                velocity_m_s=(0.0, 0.0, 0.0),
                mass_kg=10_000.0,
            ),
            segments=[
                BurnSegment(
                    12.0,
                    0.0,
                    (1.0, 0.0, 0.0),
                    end_thrust_n=12_000.0,
                    regime="startup",
                )
            ],
        )
        coarse = simulate_translational_maneuver(
            **kwargs,
            config=TranslationalConfig(
                specific_impulse_s=300.0,
                dry_mass_kg=5_000.0,
                max_step_s=3.0,
            ),
        )
        fine = simulate_translational_maneuver(
            **kwargs,
            config=TranslationalConfig(
                specific_impulse_s=300.0,
                dry_mass_kg=5_000.0,
                max_step_s=0.1,
            ),
        )

        self.assertAlmostEqual(coarse.propulsive_impulse_n_s, 72_000.0, places=8)
        self.assertAlmostEqual(fine.propulsive_impulse_n_s, 72_000.0, places=8)
        self.assertAlmostEqual(
            coarse.final_state.mass_kg,
            fine.final_state.mass_kg,
            places=9,
        )

    def test_central_gravity_bends_a_tangential_coast(self):
        mu = 1.0e6
        radius = 1000.0
        circular_speed = sqrt(mu / radius)

        result = simulate_translational_maneuver(
            TranslationalState(
                time_s=0.0,
                position_m=(radius, 0.0, 0.0),
                velocity_m_s=(0.0, circular_speed, 0.0),
                mass_kg=1000.0,
            ),
            [BurnSegment(10.0, 0.0, (0.0, 0.0, 0.0), regime="coast")],
            TranslationalConfig(
                specific_impulse_s=300.0,
                dry_mass_kg=500.0,
                gravitational_parameter_m3_s2=mu,
                max_step_s=0.05,
            ),
        )

        self.assertLess(result.final_state.position_m[0], radius)
        self.assertGreater(result.final_state.position_m[1], 0.0)
        self.assertLess(result.final_state.velocity_m_s[0], 0.0)
        self.assertEqual(result.final_state.mass_kg, 1000.0)

    def test_circular_orbit_converges_over_one_period(self):
        mu = 1.0e6
        radius = 1000.0
        circular_speed = sqrt(mu / radius)
        period = 2.0 * pi * sqrt(radius ** 3 / mu)

        def run(step):
            return simulate_translational_maneuver(
                TranslationalState(
                    time_s=0.0,
                    position_m=(radius, 0.0, 0.0),
                    velocity_m_s=(0.0, circular_speed, 0.0),
                    mass_kg=1000.0,
                ),
                [BurnSegment(period, 0.0, (0.0, 0.0, 0.0), regime="coast")],
                TranslationalConfig(
                    specific_impulse_s=300.0,
                    dry_mass_kg=500.0,
                    gravitational_parameter_m3_s2=mu,
                    max_step_s=step,
                ),
            )

        coarse = run(1.0)
        fine = run(0.1)

        def position_error(result):
            x, y, z = result.final_state.position_m
            return sqrt((x - radius) ** 2 + y ** 2 + z ** 2)

        self.assertLess(position_error(fine), position_error(coarse))
        self.assertLess(position_error(fine), 2.0)

    def test_rejects_invalid_gravity_and_singularity(self):
        state = TranslationalState(
            time_s=0.0,
            position_m=(1.0, 0.0, 0.0),
            velocity_m_s=(0.0, 0.0, 0.0),
            mass_kg=1000.0,
        )
        coast = [BurnSegment(1.0, 0.0, (0.0, 0.0, 0.0), regime="coast")]

        with self.assertRaisesRegex(ValueError, "gravitational_parameter"):
            simulate_translational_maneuver(
                state,
                coast,
                TranslationalConfig(
                    specific_impulse_s=300.0,
                    dry_mass_kg=500.0,
                    gravitational_parameter_m3_s2=-1.0,
                ),
            )

        with self.assertRaisesRegex(ValueError, "gravity center"):
            simulate_translational_maneuver(
                TranslationalState(
                    time_s=0.0,
                    position_m=(0.0, 0.0, 0.0),
                    velocity_m_s=(0.0, 0.0, 0.0),
                    mass_kg=1000.0,
                ),
                coast,
                TranslationalConfig(
                    specific_impulse_s=300.0,
                    dry_mass_kg=500.0,
                    gravitational_parameter_m3_s2=1.0,
                ),
            )


if __name__ == "__main__":
    unittest.main()
