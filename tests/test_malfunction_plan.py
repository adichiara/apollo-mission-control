from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.malfunction_plan import (  # noqa: E402
    CausalInsertion,
    InsertionLayer,
    InsertionMode,
    MalfunctionPlan,
    MalfunctionScheduler,
    activation_to_dict,
)


def insertion(name, layer=InsertionLayer.VEHICLE_SYSTEM):
    return CausalInsertion(
        insertion_id=name,
        layer=layer,
        target=f"target.{name}",
        value=True,
        provenance="synthetic test insertion",
    )


class MalfunctionPlanTests(unittest.TestCase):
    def test_one_exercise_malfunction_can_expand_to_multiple_causal_insertions(self):
        scheduler = MalfunctionScheduler(
            (
                MalfunctionPlan(
                    malfunction_id="dual-layer",
                    description="synthetic multi-insertion failure",
                    mode=InsertionMode.MANUAL,
                    insertions=(
                        insertion("source"),
                        insertion("telemetry", InsertionLayer.TELEMETRY),
                    ),
                    provenance="synthetic test",
                ),
            )
        )
        activation = scheduler.activate(
            "dual-layer",
            current_time_s=10.0,
            trigger_mode=InsertionMode.MANUAL,
        )
        self.assertEqual(len(activation.insertions), 2)
        self.assertEqual(
            [item.layer for item in activation.insertions],
            [InsertionLayer.VEHICLE_SYSTEM, InsertionLayer.TELEMETRY],
        )
        self.assertFalse(activation_to_dict(activation)["applies_downstream_effects"])

    def test_time_dependent_plan_cannot_activate_early_and_activates_once_due(self):
        scheduler = MalfunctionScheduler(
            (
                MalfunctionPlan(
                    malfunction_id="timed",
                    description="synthetic timed failure",
                    mode=InsertionMode.TIME_DEPENDENT,
                    activation_time_s=20.0,
                    insertions=(insertion("timed"),),
                    provenance="synthetic test",
                ),
            )
        )
        with self.assertRaisesRegex(ValueError, "not due"):
            scheduler.activate("timed", current_time_s=19.9)
        self.assertEqual(scheduler.activate_due(current_time_s=19.9), ())
        due = scheduler.activate_due(current_time_s=20.0)
        self.assertEqual(len(due), 1)
        self.assertEqual(scheduler.activate_due(current_time_s=21.0), ())

    def test_manual_and_preprogrammed_modes_require_matching_explicit_trigger(self):
        for mode in (InsertionMode.MANUAL, InsertionMode.PREPROGRAMMED):
            scheduler = MalfunctionScheduler(
                (
                    MalfunctionPlan(
                        malfunction_id=mode.value,
                        description="synthetic",
                        mode=mode,
                        insertions=(insertion(mode.value),),
                        provenance="synthetic",
                    ),
                )
            )
            with self.assertRaisesRegex(ValueError, "requires trigger_mode"):
                scheduler.activate(mode.value, current_time_s=1.0)
            with self.assertRaisesRegex(ValueError, "does not match"):
                scheduler.activate(
                    mode.value,
                    current_time_s=1.0,
                    trigger_mode=(
                        InsertionMode.PREPROGRAMMED
                        if mode == InsertionMode.MANUAL
                        else InsertionMode.MANUAL
                    ),
                )
            self.assertEqual(
                scheduler.activate(
                    mode.value,
                    current_time_s=1.0,
                    trigger_mode=mode,
                ).mode,
                mode,
            )

    def test_plan_validation_rejects_duplicate_insertions_and_bad_time_semantics(self):
        with self.assertRaisesRegex(ValueError, "duplicate insertion_id"):
            MalfunctionScheduler(
                (
                    MalfunctionPlan(
                        malfunction_id="duplicate",
                        description="synthetic",
                        mode=InsertionMode.MANUAL,
                        insertions=(insertion("same"), insertion("same")),
                        provenance="synthetic",
                    ),
                )
            )
        with self.assertRaisesRegex(ValueError, "requires activation_time_s"):
            MalfunctionScheduler(
                (
                    MalfunctionPlan(
                        malfunction_id="bad-timed",
                        description="synthetic",
                        mode=InsertionMode.TIME_DEPENDENT,
                        insertions=(insertion("x"),),
                        provenance="synthetic",
                    ),
                )
            )
        with self.assertRaisesRegex(ValueError, "only valid"):
            MalfunctionScheduler(
                (
                    MalfunctionPlan(
                        malfunction_id="bad-manual",
                        description="synthetic",
                        mode=InsertionMode.MANUAL,
                        activation_time_s=1.0,
                        insertions=(insertion("x"),),
                        provenance="synthetic",
                    ),
                )
            )

    def test_duplicate_activation_is_rejected(self):
        scheduler = MalfunctionScheduler(
            (
                MalfunctionPlan(
                    malfunction_id="once",
                    description="synthetic",
                    mode=InsertionMode.MANUAL,
                    insertions=(insertion("once"),),
                    provenance="synthetic",
                ),
            )
        )
        scheduler.activate(
            "once",
            current_time_s=1.0,
            trigger_mode=InsertionMode.MANUAL,
        )
        with self.assertRaisesRegex(ValueError, "already activated"):
            scheduler.activate(
                "once",
                current_time_s=2.0,
                trigger_mode=InsertionMode.MANUAL,
            )


if __name__ == "__main__":
    unittest.main()
