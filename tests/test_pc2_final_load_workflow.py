from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from apollo_mission_control.controller_products import project_controller_products  # noqa: E402
from apollo_mission_control.pc2_nominal import (  # noqa: E402
    PC2State,
    SimEvent,
    apply_event,
    load_fixture,
    run_nominal,
)


class PC2FinalLoadWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.fixture = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")
        self.state = PC2State(get_s=float(self.fixture["start_get_s"]))

    def apply(self, get_s, name):
        apply_event(self.state, SimEvent(float(get_s), name), self.fixture)

    def test_staged_final_load_transitions(self):
        self.assertEqual(self.state.state_vector_load_status, "preliminary_loaded")
        self.assertEqual(self.state.target_load_status, "preliminary_loaded")
        self.assertEqual(self.state.pc2_solution_stage, "preliminary")

        self.apply(280800, "final_pc2_solution_ready")
        self.assertEqual(self.state.pc2_solution_stage, "final_ready")
        self.assertEqual(self.state.state_vector_load_status, "final_pending")
        self.assertEqual(self.state.target_load_status, "final_pending")

        self.apply(281820, "final_load_requested")
        self.assertTrue(self.state.final_load_requested)
        self.assertTrue(self.state.uplink_configuration_ready)

        self.apply(281820, "final_load_transmission_started")
        self.assertEqual(self.state.state_vector_load_status, "transmitting")
        self.assertEqual(self.state.target_load_status, "transmitting")

        self.apply(281?00 if False else 282185, "computer_returned_to_crew")
        self.assertTrue(self.state.final_load_complete)
        self.assertTrue(self.state.computer_with_crew)
        self.assertEqual(self.state.state_vector_load_status, "final_loaded")
        self.assertEqual(self.state.target_load_status, "final_loaded")
        self.assertEqual(self.state.pc2_solution_stage, "final_stable")

    def test_station_products_preserve_cross_station_workflow(self):
        self.apply(280800, "final_pc2_solution_ready")
        self.apply(281820, "final_load_requested")
        projections = project_controller_products(self.state, self.fixture)

        self.assertEqual(
            projections["GUIDO"].products["ground.pc2.solution_stage"].value,
            "final_ready",
        )
        self.assertTrue(
            projections["INCO"].products["comm.uplink_configuration_ready"].value
        )
        self.assertTrue(
            projections["CAPCOM"].products["ground.pc2.final_load_requested"].value
        )
        self.assertFalse(
            projections["FLIGHT"].products["ground.pc2.final_load_complete"].value
        )

    def test_nominal_finishes_with_final_load_complete(self):
        final_state = run_nominal(self.fixture)
        self.assertTrue(final_state.final_load_complete)
        self.assertEqual(final_state.pc2_solution_stage, "final_stable")
        self.assertEqual(final_state.state_vector_load_status, "final_loaded")
        self.assertEqual(final_state.target_load_status, "final_loaded")


if __name__ == "__main__":
    unittest.main()
