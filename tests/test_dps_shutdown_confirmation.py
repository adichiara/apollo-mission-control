from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.pc2_nominal import Product, Validity  # noqa: E402
from apollo_mission_control.shutdown_confirmation import (  # noqa: E402
    ShutdownEvidenceState,
    assess_dps_shutdown_evidence,
)


class DPSShutdownConfirmationTests(unittest.TestCase):
    def test_no_post_command_evidence(self):
        result = assess_dps_shutdown_evidence(command_get_s=100.0)
        self.assertEqual(result.state, ShutdownEvidenceState.NONE)

    def test_crew_report_is_independent_evidence(self):
        result = assess_dps_shutdown_evidence(
            command_get_s=100.0,
            crew_report_get_s=101.0,
        )
        self.assertEqual(result.state, ShutdownEvidenceState.CREW_REPORTED)
        self.assertIsNone(result.chamber_pressure_psi)

    def test_precommand_pressure_does_not_confirm_response(self):
        pressure = Product(
            value=100.0,
            units="psi",
            source_time_get=99.0,
            sample_time_get=99.0,
            display_time_get=101.0,
            validity=Validity.VALID,
            source_layer="measurement/telemetry",
            provenance="GQ6510P architecture test",
        )
        result = assess_dps_shutdown_evidence(
            command_get_s=100.0,
            chamber_pressure_product=pressure,
        )
        self.assertEqual(result.state, ShutdownEvidenceState.NONE)

    def test_fresh_postcommand_pressure_is_ground_evidence_without_threshold(self):
        pressure = Product(
            value=72.0,
            units="psi",
            source_time_get=101.0,
            sample_time_get=101.0,
            display_time_get=102.0,
            validity=Validity.VALID,
            source_layer="measurement/telemetry",
            provenance="synthetic GQ6510P response value; not historical Apollo 13 pressure",
        )
        result = assess_dps_shutdown_evidence(
            command_get_s=100.0,
            chamber_pressure_product=pressure,
        )
        self.assertEqual(result.state, ShutdownEvidenceState.GROUND_PRESSURE_OBSERVED)
        self.assertEqual(result.chamber_pressure_psi, 72.0)
        self.assertIn("no historical chamber-pressure threshold", result.note)

    def test_voice_and_ground_observation_are_corroborated_channels(self):
        pressure = Product(
            value=50.0,
            units="psi",
            source_time_get=101.5,
            sample_time_get=101.5,
            display_time_get=102.0,
            validity=Validity.VALID,
            source_layer="measurement/telemetry",
        )
        result = assess_dps_shutdown_evidence(
            command_get_s=100.0,
            crew_report_get_s=101.0,
            chamber_pressure_product=pressure,
        )
        self.assertEqual(result.state, ShutdownEvidenceState.CORROBORATED)


if __name__ == "__main__":
    unittest.main()
