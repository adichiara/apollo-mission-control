from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.measurement_output_model import (  # noqa: E402
    MeasurementDefinition,
    MeasurementFault,
    MeasurementKind,
    MeasurementSourceKind,
    evaluate_measurement_outputs,
)


class MeasurementOutputModelTests(unittest.TestCase):
    def test_variable_and_fixed_sources_are_explicit_and_inspectable(self):
        result = evaluate_measurement_outputs(
            {"tank_pressure": 123.5},
            [
                MeasurementDefinition(
                    measurement_id="M_ANALOG",
                    description="synthetic analog measurement",
                    kind=MeasurementKind.ANALOG,
                    source_kind=MeasurementSourceKind.VARIABLE,
                    source_key="tank_pressure",
                    unit="psi",
                    provenance=("synthetic test",),
                ),
                MeasurementDefinition(
                    measurement_id="M_EVENT",
                    description="synthetic fixed event",
                    kind=MeasurementKind.EVENT,
                    source_kind=MeasurementSourceKind.FIXED,
                    fixed_value=True,
                    provenance=("synthetic test",),
                ),
            ],
            active_profile="PROFILE_A",
        )

        analog = result.measurement("M_ANALOG")
        event = result.measurement("M_EVENT")
        self.assertEqual(analog.value, 123.5)
        self.assertEqual(analog.source_key, "tank_pressure")
        self.assertEqual(analog.unit, "psi")
        self.assertIs(event.value, True)
        self.assertEqual(event.source_kind, MeasurementSourceKind.FIXED)

        payload = result.to_dict()
        self.assertFalse(payload["mutates_source_state"])
        self.assertFalse(payload["redundant_channel_combining_implemented"])

    def test_profile_effectivity_withholds_inapplicable_measurement(self):
        result = evaluate_measurement_outputs(
            {"signal": 12.0},
            [
                MeasurementDefinition(
                    measurement_id="M1",
                    description="profile-specific measurement",
                    kind=MeasurementKind.ANALOG,
                    source_kind=MeasurementSourceKind.VARIABLE,
                    source_key="signal",
                    unit="unit",
                    applicable_profiles=("PROFILE_A",),
                )
            ],
            active_profile="PROFILE_B",
        )
        output = result.measurement("M1")
        self.assertFalse(output.applicable)
        self.assertFalse(output.available)
        self.assertFalse(output.valid)
        self.assertIsNone(output.value)
        self.assertEqual(output.reasons, ("profile_not_applicable",))

    def test_output_fault_changes_measurement_without_mutating_source(self):
        source = {"signal": 10.0}
        result = evaluate_measurement_outputs(
            source,
            [
                MeasurementDefinition(
                    measurement_id="M1",
                    description="faultable measurement",
                    kind=MeasurementKind.ANALOG,
                    source_kind=MeasurementSourceKind.VARIABLE,
                    source_key="signal",
                    unit="unit",
                )
            ],
            faults=[
                MeasurementFault(
                    measurement_id="M1",
                    valid=False,
                    replacement_value=99.0,
                    provenance="synthetic telemetry fault",
                )
            ],
        )
        output = result.measurement("M1")
        self.assertEqual(source["signal"], 10.0)
        self.assertEqual(output.value, 99.0)
        self.assertTrue(output.available)
        self.assertFalse(output.valid)
        self.assertTrue(output.fault_applied)
        self.assertIn("fault_replacement_value", output.reasons)
        self.assertIn("fault_validity_override", output.reasons)

    def test_unavailable_fault_withholds_value_and_forces_invalid(self):
        result = evaluate_measurement_outputs(
            {"event_source": True},
            [
                MeasurementDefinition(
                    measurement_id="E1",
                    description="event measurement",
                    kind=MeasurementKind.EVENT,
                    source_kind=MeasurementSourceKind.VARIABLE,
                    source_key="event_source",
                )
            ],
            faults=[
                MeasurementFault(
                    measurement_id="E1",
                    available=False,
                    provenance="synthetic channel loss",
                )
            ],
        )
        output = result.measurement("E1")
        self.assertFalse(output.available)
        self.assertFalse(output.valid)
        self.assertIsNone(output.value)
        self.assertIn("measurement_unavailable", output.reasons)

    def test_missing_source_and_unknown_fault_are_rejected(self):
        definition = MeasurementDefinition(
            measurement_id="M1",
            description="missing source",
            kind=MeasurementKind.ANALOG,
            source_kind=MeasurementSourceKind.VARIABLE,
            source_key="missing",
            unit="unit",
        )
        with self.assertRaisesRegex(ValueError, "missing source variable"):
            evaluate_measurement_outputs({}, [definition])

        fixed = MeasurementDefinition(
            measurement_id="M1",
            description="fixed source",
            kind=MeasurementKind.EVENT,
            source_kind=MeasurementSourceKind.FIXED,
            fixed_value=True,
        )
        with self.assertRaisesRegex(ValueError, "unknown measurement"):
            evaluate_measurement_outputs(
                {},
                [fixed],
                faults=[MeasurementFault(measurement_id="OTHER", valid=False)],
            )

    def test_ambiguous_source_and_kind_shapes_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "must not set fixed_value"):
            evaluate_measurement_outputs(
                {"x": 1.0},
                [
                    MeasurementDefinition(
                        measurement_id="M1",
                        description="ambiguous",
                        kind=MeasurementKind.ANALOG,
                        source_kind=MeasurementSourceKind.VARIABLE,
                        source_key="x",
                        fixed_value=1.0,
                        unit="unit",
                    )
                ],
            )

        with self.assertRaisesRegex(ValueError, "requires fixed_value"):
            evaluate_measurement_outputs(
                {},
                [
                    MeasurementDefinition(
                        measurement_id="M2",
                        description="missing fixed",
                        kind=MeasurementKind.EVENT,
                        source_kind=MeasurementSourceKind.FIXED,
                    )
                ],
            )

        with self.assertRaisesRegex(ValueError, "analog output requires unit"):
            evaluate_measurement_outputs(
                {},
                [
                    MeasurementDefinition(
                        measurement_id="M3",
                        description="analog no unit",
                        kind=MeasurementKind.ANALOG,
                        source_kind=MeasurementSourceKind.FIXED,
                        fixed_value=1.0,
                    )
                ],
            )

        with self.assertRaisesRegex(ValueError, "event output must not set unit"):
            evaluate_measurement_outputs(
                {},
                [
                    MeasurementDefinition(
                        measurement_id="M4",
                        description="event with unit",
                        kind=MeasurementKind.EVENT,
                        source_kind=MeasurementSourceKind.FIXED,
                        fixed_value=True,
                        unit="flag",
                    )
                ],
            )

    def test_duplicate_measurements_faults_and_profiles_are_rejected(self):
        definition = MeasurementDefinition(
            measurement_id="M1",
            description="fixed",
            kind=MeasurementKind.EVENT,
            source_kind=MeasurementSourceKind.FIXED,
            fixed_value=True,
        )
        with self.assertRaisesRegex(ValueError, "duplicate measurement_id"):
            evaluate_measurement_outputs({}, [definition, definition])

        with self.assertRaisesRegex(ValueError, "duplicate measurement fault"):
            evaluate_measurement_outputs(
                {},
                [definition],
                faults=[
                    MeasurementFault(measurement_id="M1", valid=False),
                    MeasurementFault(measurement_id="M1", available=False),
                ],
            )

        with self.assertRaisesRegex(ValueError, "duplicate applicable profiles"):
            evaluate_measurement_outputs(
                {},
                [
                    MeasurementDefinition(
                        measurement_id="M2",
                        description="duplicate profiles",
                        kind=MeasurementKind.EVENT,
                        source_kind=MeasurementSourceKind.FIXED,
                        fixed_value=True,
                        applicable_profiles=("A", "A"),
                    )
                ],
                active_profile="A",
            )

    def test_event_and_analog_types_are_not_silently_coerced(self):
        with self.assertRaisesRegex(ValueError, "event value must be bool"):
            evaluate_measurement_outputs(
                {"event": 1},
                [
                    MeasurementDefinition(
                        measurement_id="E1",
                        description="event",
                        kind=MeasurementKind.EVENT,
                        source_kind=MeasurementSourceKind.VARIABLE,
                        source_key="event",
                    )
                ],
            )

        with self.assertRaisesRegex(ValueError, "numeric, not bool"):
            evaluate_measurement_outputs(
                {"analog": True},
                [
                    MeasurementDefinition(
                        measurement_id="A1",
                        description="analog",
                        kind=MeasurementKind.ANALOG,
                        source_kind=MeasurementSourceKind.VARIABLE,
                        source_key="analog",
                        unit="unit",
                    )
                ],
            )


if __name__ == "__main__":
    unittest.main()
