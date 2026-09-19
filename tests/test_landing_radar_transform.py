import math
import unittest

from apollo_mission_control.landing_radar_transform import (
    antenna_to_navigation_base,
    landing_radar_velocity_beams_navigation_base,
    navigation_base_to_stable_member,
    norm,
    stable_member_to_navigation_base,
)


def axisrot_source_oracle(v, axis, angle, inverse=False):
    """Literal floating-point form of Sunburst37 AXISROT's two branches."""
    c, s = math.cos(angle), math.sin(angle)
    x, y, z = v
    pairs = {"x": (1, 2), "y": (2, 0), "z": (0, 1)}
    a, b = pairs[axis]
    q = [x, y, z]
    old_a, old_b = q[a], q[b]
    if inverse:
        q[b] = c * old_b - s * old_a
        q[a] = s * old_b + c * old_a
    else:
        q[b] = s * old_a + c * old_b
        q[a] = c * old_a - s * old_b
    return tuple(q)


class LandingRadarTransformTests(unittest.TestCase):
    def assertVectorAlmostEqual(self, a, b, places=12):
        for av, bv in zip(a, b):
            self.assertAlmostEqual(av, bv, places=places)

    def test_zero_angle_identity(self):
        v = (0.2, -0.3, 0.4)
        self.assertEqual(stable_member_to_navigation_base(v, cdu_y_rad=0, cdu_z_rad=0, cdu_x_rad=0), v)
        self.assertEqual(navigation_base_to_stable_member(v, cdu_y_rad=0, cdu_z_rad=0, cdu_x_rad=0), v)

    def test_smnb_matches_literal_axisrot_sequence(self):
        v = (0.21, -0.17, 0.31)
        y, z, x = 0.23, -0.19, 0.11
        oracle = v
        for axis, angle in (("y", y), ("z", z), ("x", x)):
            oracle = axisrot_source_oracle(oracle, axis, angle)
        actual = stable_member_to_navigation_base(v, cdu_y_rad=y, cdu_z_rad=z, cdu_x_rad=x)
        self.assertVectorAlmostEqual(actual, oracle)

    def test_nbsm_matches_literal_inverse_axisrot_sequence(self):
        v = (0.21, -0.17, 0.31)
        y, z, x = 0.23, -0.19, 0.11
        oracle = v
        for axis, angle in (("x", x), ("z", z), ("y", y)):
            oracle = axisrot_source_oracle(oracle, axis, angle, inverse=True)
        actual = navigation_base_to_stable_member(v, cdu_y_rad=y, cdu_z_rad=z, cdu_x_rad=x)
        self.assertVectorAlmostEqual(actual, oracle)

    def test_round_trip_and_basis_norms(self):
        y, z, x = 0.31, -0.22, 0.09
        for v in ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0), (0.2, -0.3, 0.4)):
            nb = stable_member_to_navigation_base(v, cdu_y_rad=y, cdu_z_rad=z, cdu_x_rad=x)
            sm = navigation_base_to_stable_member(nb, cdu_y_rad=y, cdu_z_rad=z, cdu_x_rad=x)
            self.assertVectorAlmostEqual(sm, v)
            self.assertAlmostEqual(norm(nb), norm(v), places=12)

    def test_setpos_beta_then_alpha_and_orthonormal_beams(self):
        beta, alpha = 0.41, -0.13
        expected = axisrot_source_oracle((1.0, 0.0, 0.0), "y", beta)
        expected = axisrot_source_oracle(expected, "x", alpha)
        self.assertVectorAlmostEqual(
            antenna_to_navigation_base((1.0, 0.0, 0.0), beta_rad=beta, alpha_rad=alpha),
            expected,
        )
        beams = landing_radar_velocity_beams_navigation_base(beta_rad=beta, alpha_rad=alpha)
        for beam in beams:
            self.assertAlmostEqual(norm(beam), 1.0, places=12)
        for i in range(3):
            for j in range(i + 1, 3):
                self.assertAlmostEqual(sum(a*b for a, b in zip(beams[i], beams[j])), 0.0, places=12)


if __name__ == "__main__":
    unittest.main()
