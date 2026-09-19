from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.landing_radar_reference import (  # noqa: E402
    LandingRadarVelocityReferenceInput,
    compute_landing_radar_velocity_reference,
)


class LandingRadarVelocityReferenceTests(unittest.TestCase):
    def test_projects_surface_relative_velocity_on_selected_beam(self):
        result = compute_landing_radar_velocity_reference(
            LandingRadarVelocityReferenceInput(
                estimated_velocity_m_s=(100.0, 20.0, -5.0),
                lunar_surface_velocity_m_s=(10.0, 2.0, -1.0),
                beam_unit_vector=(1.0, 0.0, 0.0),
                component="vx",
                provenance=("synthetic projection test",),
            )
        )

        self.assertEqual(result.relative_surface_velocity_m_s, (90.0, 18.0, -4.0))
        self.assertEqual(result.reference_velocity_m_s, 90.0)
        self.assertEqual(result.component, "vx")

    def test_projection_preserves_beam_sign(self):
        result = compute_landing_radar_velocity_reference(
            LandingRadarVelocityReferenceInput(
                estimated_velocity_m_s=(100.0, 0.0, 0.0),
                lunar_surface_velocity_m_s=(10.0, 0.0, 0.0),
                beam_unit_vector=(-1.0, 0.0, 0.0),
            )
        )
        self.assertEqual(result.reference_velocity_m_s, -90.0)

    def test_orthogonal_beam_produces_zero_reference(self):
        result = compute_landing_radar_velocity_reference(
            LandingRadarVelocityReferenceInput(
                estimated_velocity_m_s=(10.0, 0.0, 0.0),
                lunar_surface_velocity_m_s=(0.0, 0.0, 0.0),
                beam_unit_vector=(0.0, 1.0, 0.0),
            )
        )
        self.assertEqual(result.reference_velocity_m_s, 0.0)

    def test_equal_vehicle_and_surface_velocity_produces_zero(self):
        result = compute_landing_radar_velocity_reference(
            LandingRadarVelocityReferenceInput(
                estimated_velocity_m_s=(1.0, 2.0, 3.0),
                lunar_surface_velocity_m_s=(1.0, 2.0, 3.0),
                beam_unit_vector=(0.0, 0.0, 1.0),
            )
        )
        self.assertEqual(result.relative_surface_velocity_m_s, (0.0, 0.0, 0.0))
        self.assertEqual(result.reference_velocity_m_s, 0.0)

    def test_non_unit_beam_is_rejected_instead_of_silently_normalized(self):
        with self.assertRaisesRegex(ValueError, "unit length"):
            compute_landing_radar_velocity_reference(
                LandingRadarVelocityReferenceInput(
                    estimated_velocity_m_s=(1.0, 2.0, 3.0),
                    lunar_surface_velocity_m_s=(0.0, 0.0, 0.0),
                    beam_unit_vector=(2.0, 0.0, 0.0),
                )
            )

    def test_result_serializes_boundary_and_provenance(self):
        result = compute_landing_radar_velocity_reference(
            LandingRadarVelocityReferenceInput(
                estimated_velocity_m_s=(3.0, 4.0, 5.0),
                lunar_surface_velocity_m_s=(1.0, 1.0, 1.0),
                beam_unit_vector=(0.0, 0.0, 1.0),
                applicability="test boundary",
                provenance=("source-a", "source-b"),
            )
        ).to_dict()

        self.assertEqual(result["reference_velocity_m_s"], 4.0)
        self.assertEqual(result["relative_surface_velocity_m_s"], [2.0, 3.0, 4.0])
        self.assertEqual(result["provenance"], ["source-a", "source-b"])
        self.assertIn("historical antenna/vehicle/platform transformation", result["assumptions"][2])


if __name__ == "__main__":
    unittest.main()
