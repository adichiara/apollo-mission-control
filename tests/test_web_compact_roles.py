from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fastapi.testclient import TestClient  # noqa: E402
from apollo_mission_control.web_app import app  # noqa: E402


class WebCompactRoleTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.assertEqual(self.client.post("/api/session/create").status_code, 200)

    def test_join_set_returns_separate_original_station_presentations(self):
        joined = self.client.post(
            "/api/session/join-set",
            json={"player_id": "lm-systems", "stations": ["TELMU", "CONTROL"]},
        )
        self.assertEqual(joined.status_code, 200)
        body = joined.json()
        self.assertEqual(body["stations"], ["TELMU", "CONTROL"])
        self.assertEqual(set(body["presentations"]), {"TELMU", "CONTROL"})
        self.assertNotIn("station", body)
        self.assertNotIn("presentation", body)

        snapshot = self.client.get("/api/session/player/lm-systems")
        self.assertEqual(snapshot.status_code, 200)
        self.assertEqual(snapshot.json()["stations"], ["TELMU", "CONTROL"])

    def test_rejoin_requires_exact_station_set_and_preserves_order(self):
        payload = {"player_id": "fd", "stations": ["GUIDO", "FIDO_RETRO"]}
        self.assertEqual(self.client.post("/api/session/join-set", json=payload).status_code, 200)
        self.assertEqual(self.client.post("/api/session/join-set", json=payload).status_code, 200)

        reversed_set = self.client.post(
            "/api/session/join-set",
            json={"player_id": "fd", "stations": ["FIDO_RETRO", "GUIDO"]},
        )
        self.assertEqual(reversed_set.status_code, 400)

        audit = self.client.get("/api/session/audit").json()
        rejoins = [e for e in audit if e["kind"] == "player_rejoined"]
        self.assertEqual(rejoins[-1]["details"]["stations"], ["GUIDO", "FIDO_RETRO"])

    def test_readiness_is_station_qualified_for_bundled_player(self):
        self.client.post(
            "/api/session/join-set",
            json={"player_id": "lm-systems", "stations": ["TELMU", "CONTROL"]},
        )

        ambiguous = self.client.post(
            "/api/session/player/lm-systems/readiness",
            json={"ready": True, "note": "ready"},
        )
        self.assertEqual(ambiguous.status_code, 400)

        control = self.client.post(
            "/api/session/player/lm-systems/readiness",
            json={"ready": True, "note": "CONTROL ready", "station": "CONTROL"},
        )
        self.assertEqual(control.status_code, 200)
        self.assertEqual(control.json()["station"], "CONTROL")

        not_owned = self.client.post(
            "/api/session/player/lm-systems/readiness",
            json={"ready": True, "station": "GUIDO"},
        )
        self.assertEqual(not_owned.status_code, 400)

    def test_original_station_conflict_is_enforced_across_bundles(self):
        first = self.client.post(
            "/api/session/join-set",
            json={"player_id": "lm-systems", "stations": ["TELMU", "CONTROL"]},
        )
        self.assertEqual(first.status_code, 200)
        second = self.client.post(
            "/api/session/join",
            json={"player_id": "other", "station": "CONTROL"},
        )
        self.assertEqual(second.status_code, 400)

    def test_control_authority_survives_compact_ownership(self):
        self.client.post(
            "/api/session/join-set",
            json={"player_id": "lm-systems", "stations": ["TELMU", "CONTROL"]},
        )
        response = self.client.get(
            "/api/session/control/lm-systems/shutdown-evidence"
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
