from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.controller_products import project_controller_products  # noqa: E402
from apollo_mission_control.pc2_nominal import Validity, hms_to_seconds, load_fixture  # noqa: E402
from apollo_mission_control.scenario_injection import (  # noqa: E402
    EvidenceClass,
    StateInjection,
    run_with_injections,
)
from apollo_mission_control.shutdown_rules import (  # noqa: E402
    RuleState,
    evaluate_pc2_shutdown_rules,
)


class ObservationFreshnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = load_fixture(
            ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json"
        )

    def test_carried_forward_analog_value_keeps_original_observation_time(self):
        injection_get = hms_to_seconds("79:29:00")
        projection_get = hms_to_seconds("79:30:00")
        state = run_with_injections(
            self.fixture,
            [
                StateInjection(
                    injection_id="age-test-chamber-pressure",
                    get_s=injection_get,
                    target="dps_chamber_pressure_psi",
                    value=80.0,
                    evidence_class=EvidenceClass.SOURCE_BOUNDED_TEST,
                    provenance="Synthetic timestamp/age test; not historical telemetry.",
                )
            ],
            stop_get_s=projection_get,
        )

        product = project_controller_products(state, self.fixture)["CONTROL"].products[
            "dps.chamber_pressure_psi"
        ]
        self.assertEqual(product.source_time_get, injection_get)
        self.assertEqual(product.sample_time_get, injection_get)
        self.assertEqual(product.display_time_get, projection_get)
        self.assertEqual(product.age_at(projection_get), 60.0)

    def test_nonzero_age_does_not_invent_stale_threshold(self):
        injection_get = hms_to_seconds("79:29:00")
        projection_get = hms_to_seconds("79:30:00")
        state = run_with_injections(
            self.fixture,
            [
                StateInjection(
                    injection_id="no-stale-policy-test",
                    get_s=injection_get,
                    target="dps_chamber_pressure_psi",
                    value=80.0,
                    evidence_class=EvidenceClass.SOURCE_BOUNDED_TEST,
                    provenance="Synthetic timestamp/age test; not historical telemetry.",
                )
            ],
            stop_get_s=projection_get,
        )
        projections = project_controller_products(state, self.fixture)
        product = projections["CONTROL"].products["dps.chamber_pressure_psi"]
        evaluation = evaluate_pc2_shutdown_rules(projections, self.fixture)[
            "ground_chamber_pressure"
        ]

        self.assertEqual(product.validity, Validity.VALID)
        self.assertEqual(evaluation.state, RuleState.TRIGGERED)
        self.assertEqual(evaluation.observation["observation_age_s"], 60.0)

    def test_delta_p_age_is_exposed_to_rule_audit(self):
        injection_get = hms_to_seconds("79:29:10")
        projection_get = hms_to_seconds("79:29:40")
        state = run_with_injections(
            self.fixture,
            [
                StateInjection(
                    injection_id="age-test-delta-p",
                    get_s=injection_get,
                    target="dps_fuel_oxidizer_delta_p_psi",
                    value=26.0,
                    evidence_class=EvidenceClass.SOURCE_BOUNDED_TEST,
                    provenance="Synthetic timestamp/age test; not historical telemetry.",
                )
            ],
            stop_get_s=projection_get,
        )
        projections = project_controller_products(state, self.fixture)
        evaluation = evaluate_pc2_shutdown_rules(projections, self.fixture)[
            "fuel_oxidizer_delta_p"
        ]

        self.assertEqual(evaluation.state, RuleState.TRIGGERED)
        self.assertEqual(evaluation.observation["observation_age_s"], 30.0)


if __name__ == "__main__":
    unittest.main()
