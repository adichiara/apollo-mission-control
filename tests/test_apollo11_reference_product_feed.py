from pathlib import Path
import json
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.apollo11_reference_product_feed import (  # noqa: E402
    evaluate_reference_product_feed,
    get_reference_product_feed,
    load_reference_product_feed,
)


class Apollo11ReferenceProductFeedTests(unittest.TestCase):
    def setUp(self):
        self.feed = get_reference_product_feed(
            "apollo11_descent_reference_products_v1"
        )

    def test_before_first_reference_event_products_remain_unavailable(self):
        snapshot = evaluate_reference_product_feed(self.feed, get_s=369500.0)
        self.assertEqual(snapshot.applied_event_ids, ())
        self.assertFalse(
            snapshot.product_set.product("program.alarm_latest").available
        )
        self.assertFalse(snapshot.product_set.product("program.number").available)
        self.assertEqual(
            snapshot.next_event.event_id,
            "first_1202_reference",
        )
        self.assertFalse(snapshot.historical_ground_display_timing_claimed)

    def test_alarm_reference_updates_only_explicit_alarm_field(self):
        snapshot = evaluate_reference_product_feed(self.feed, get_s=369502.0)
        alarm = snapshot.product_set.product("program.alarm_latest")
        self.assertTrue(alarm.available)
        self.assertEqual(alarm.value, "1202")
        self.assertFalse(snapshot.product_set.product("program.number").available)
        self.assertIn(
            "project_reference_at_source_event_time_not_historical_display_time",
            " ".join(alarm.provenance),
        )

    def test_p64_reference_retains_latest_alarm_and_adds_program_number(self):
        snapshot = evaluate_reference_product_feed(self.feed, get_s=369692.0)
        self.assertEqual(
            snapshot.product_set.product("program.alarm_latest").value,
            "1202",
        )
        self.assertEqual(
            snapshot.product_set.product("program.number").value,
            64,
        )
        self.assertEqual(
            snapshot.latest_applied_event.event_id,
            "enter_p64_reference",
        )

    def test_later_alarm_and_p66_progression(self):
        alarm = evaluate_reference_product_feed(self.feed, get_s=369738.0)
        self.assertEqual(
            alarm.product_set.product("program.alarm_latest").value,
            "1201",
        )
        self.assertEqual(alarm.product_set.product("program.number").value, 64)

        p66 = evaluate_reference_product_feed(self.feed, get_s=369802.0)
        self.assertEqual(
            p66.product_set.product("program.alarm_latest").value,
            "1202",
        )
        self.assertEqual(p66.product_set.product("program.number").value, 66)
        self.assertIsNone(p66.next_event)

    def test_feed_metadata_states_timing_boundary(self):
        public = self.feed.to_public_dict()
        self.assertEqual(
            public["timing_policy"],
            "project_reference_at_source_event_time_not_historical_display_time",
        )
        self.assertTrue(
            any("display refresh cadence" in item for item in public["unresolved"])
        )

    def test_unknown_product_key_in_feed_is_rejected(self):
        payload = {
            "feed_id": "bad",
            "mission_profile_id": "apollo11_g",
            "status": "test",
            "applicability": "test",
            "timing_policy": "test",
            "events": [
                {
                    "event_id": "bad",
                    "source_get_s": 1,
                    "source_get_hms": "00:00:01",
                    "activation_get_s": 1,
                    "label": "bad",
                    "values": {"hidden.agc.truth": 1},
                    "field_provenance": {},
                }
            ],
            "sources": ["synthetic"],
            "unresolved": ["synthetic"],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(
                ValueError,
                "unknown Apollo 11 descent product key",
            ):
                load_reference_product_feed(path)

    def test_out_of_order_events_are_rejected(self):
        payload = {
            "feed_id": "bad-order",
            "mission_profile_id": "apollo11_g",
            "status": "test",
            "applicability": "test",
            "timing_policy": "test",
            "events": [
                {
                    "event_id": "late",
                    "source_get_s": 2,
                    "source_get_hms": "00:00:02",
                    "activation_get_s": 2,
                    "label": "late",
                    "values": {"program.number": 64},
                    "field_provenance": {},
                },
                {
                    "event_id": "early",
                    "source_get_s": 1,
                    "source_get_hms": "00:00:01",
                    "activation_get_s": 1,
                    "label": "early",
                    "values": {"program.number": 63},
                    "field_provenance": {},
                },
            ],
            "sources": ["synthetic"],
            "unresolved": ["synthetic"],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "ordered by activation_get_s"):
                load_reference_product_feed(path)


if __name__ == "__main__":
    unittest.main()
