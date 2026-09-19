from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.landing_radar_velocity_update import (  # noqa: E402
    LandingRadarVelocityUpdateInput,
    LandingRadarVelocityWeightConfig,
    apply_landing_radar_velocity_update,
)


class LandingRadarVelocityUpdateTests(unittest.TestCase):
    def config(self):
        return LandingRadarVelocityWeightConfig(
            maximum_speed_m_s=600.0,
            low_speed_threshold_m_s=60.0,
            linear_component_weights={"x": 0.3, "y": 0.4, "z": 0.5},
            low_speed_component_weights={"x": 0.2, "y": 0.25, "z": 0.3},
            override_programs=("P65", "P66", "P67"),
            override_weight=0.1,
            provenance=("synthetic",),
        )

    def evaluate(self, *, speed, component="x", program=None, residual=10.0,
            reasonableness=True, permitted=True, beam=(1.0, 0.0, 0.0)):
        return apply_landing_radar_velocity_update(
            LandingRadarVelocityUpdateInput(
                prior_velocity_m_s=(100.0, 20.0, -5.0),
                estimated_speed_m_s=speed,
                measured_minus_reference_m_s=residual,
                beam_unit_vector=beam,
                component=component,
                program=program,
                reasonableness_passed=reasonableness,
                updates_permitted=permitted,
            ),
            self.config(),
        )

    def test_low_speed_uses_component_constant(self):
        result = self.evaluate(speed=50.0, component="x")
        self.assertEqual(result.selected_weight, 0.2)
        self.assertEqual(result.weight_regime, "low_speed_constant")
        self.assertEqual(result.delta_velocity_m_s, (2.0, 0.0, 0.0))
        self.assertEqual(result.updated_velocity_m_s, (102.0, 20.0, -5.0))

    def test_low_speed_boundary_uses_constant(self):
        result = self.evaluate(speed=60.0, component="y", beam=(0.0, 1.0, 0.0))
        self.assertEqual(result.selected_weight, 0.25)
        self.assertEqual(result.weight_regime, "low_speed_constant")

    def test_mid_speed_uses_linear_weight(self):
        result = self.evaluate(speed=300.0, component="x")
        self.assertAlmostEqual(result.selected_weight, 0.15)
        self.assertEqual(result.weight_regime, "linear_with_speed")
        self.assertAlmostEqual(result.updated_velocity_m_s[0], 101.5)

    def test_maximum_speed_and_above_have_zero_weight(self):
        for speed in (600.0, 700.0):
            result = self.evaluate(speed=speed)
            self.assertEqual(result.selected_weight, 0.0)
            self.assertFalse(result.update_applied)
            self.assertEqual(result.weight_regime, "at_or_above_maximum_speed")
            self.assertIn("weight_zero_at_or_above_maximum_speed", result.reasons)

    def test_program_override_replaces_speed_dependent_weight(self):
        for program in ("P65", "P66", "P67", "p66"):
            result = self.evaluate(speed=300.0, program=program)
            self.assertEqual(result.selected_weight, 0.1)
            self.assertEqual(result.weight_regime, "program_override")
            self.assertAlmostEqual(result.updated_velocity_m_s[0], 101.0)

    def test_program_override_also_replaces_zero_above_maximum(self):
        result = self.evaluate(speed=700.0, program="P66")
        self.assertEqual(result.selected_weight, 0.1)
        self.assertTrue(result.update_applied)

    def test_failed_reasonableness_bypasses_update(self):
        result = self.evaluate(speed=50.0, reasonableness=False)
        self.assertFalse(result.update_applied)
        self.assertEqual(result.selected_weight, 0.0)
        self.assertEqual(result.updated_velocity_m_s, result.prior_velocity_m_s)
        self.assertIn("reasonableness_test_failed", result.reasons)

    def test_update_inhibit_bypasses_update(self):
        result = self.evaluate(speed=50.0, permitted=False)
        self.assertFalse(result.update_applied)
        self.assertIn("landing_radar_updates_inhibited", result.reasons)

    def test_signed_residual_and_beam_direction_are_preserved(self):
        result = self.evaluate(
            speed=50.0,
            residual=-10.0,
            beam=(0.0, -1.0, 0.0),
        )
        self.assertEqual(result.delta_velocity_m_s, (-0.0, 2.0, -0.0))
        self.assertEqual(result.updated_velocity_m_s, (100.0, 22.0, -5.0))

    def test_non_unit_beam_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unit length"):
            self.evaluate(speed=50.0, beam=(2.0, 0.0, 0.0))

    def test_unknown_component_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown velocity component"):
            self.evaluate(speed=50.0, component="q")

    def test_invalid_config_threshold_order_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "below maximum"):
            LandingRadarVelocityWeightConfig(
                maximum_speed_m_s=100.0,
                low_speed_threshold_m_s=100.0,
                linear_component_weights={"x": 0.3},
                low_speed_component_weights={"x": 0.2},
            ).validated()


if __name__ == "__main__":
    unittest.main()
