from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.compact_roles import COMPACT_FIVE_PLAYER_ROLES  # noqa: E402
from apollo_mission_control.pc2_nominal import load_fixture  # noqa: E402
from apollo_mission_control.pc2_session import PC2Session  # noqa: E402


class CompactStationSetTests(unittest.TestCase):
    def _session(self):
        fixture = load_fixture(ROOT / "data" / "scenarios" / "apollo13_pc2_nominal.json")
        return PC2Session.create(fixture)

    def test_approved_compact_role_sets_cover_each_original_station_once(self):
        flattened = [
            station
            for stations in COMPACT_FIVE_PLAYER_ROLES.values()
            for station in stations
        ]
        self.assertEqual(len(flattened), len(set(flattened)))
        self.assertEqual(
            set(flattened),
            {"FLIGHT", "CAPCOM", "TELMU", "CONTROL", "GUIDO", "FIDO_RETRO", "INCO"},
        )

    def test_one_player_can_own_multiple_original_stations_without_synthetic_station(self):
        session = self._session()
        session.assign_stations("lm-systems-player", ("TELMU", "CONTROL"))

        self.assertEqual(
            session.stations_for("lm-systems-player"),
            ("TELMU", "CONTROL"),
        )
        self.assertTrue(session.owns_station("lm-systems-player", "TELMU"))
        self.assertTrue(session.owns_station("lm-systems-player", "CONTROL"))
        self.assertNotIn("LM_SYSTEMS", session.available_stations)
        with self.assertRaises(ValueError):
            session.station_for("lm-systems-player")

    def test_original_station_cannot_be_owned_by_two_players(self):
        session = self._session()
        session.assign_stations("lm-systems-player", ("TELMU", "CONTROL"))
        with self.assertRaises(ValueError):
            session.assign_station("other-player", "CONTROL")

    def test_bundled_snapshot_keeps_station_presentations_separate(self):
        session = self._session()
        session.assign_stations("fd-player", ("GUIDO", "FIDO_RETRO"))

        payload = session.bundled_player_snapshot("fd-player").to_dict()

        self.assertEqual(payload["stations"], ("GUIDO", "FIDO_RETRO"))
        self.assertEqual(set(payload["presentations"]), {"GUIDO", "FIDO_RETRO"})
        self.assertNotIn("FLIGHT", payload["presentations"])
        self.assertNotIn("CONTROL", payload["presentations"])

    def test_readiness_remains_station_specific_for_bundled_player(self):
        session = self._session()
        session.assign_stations("lm-systems-player", ("TELMU", "CONTROL"))

        with self.assertRaises(ValueError):
            session.submit_readiness("lm-systems-player", ready=True)

        telmu = session.submit_readiness(
            "lm-systems-player",
            station="TELMU",
            ready=True,
            note="electrical/environmental ready",
        )
        control = session.submit_readiness(
            "lm-systems-player",
            station="CONTROL",
            ready=False,
            note="propulsion review open",
        )

        self.assertEqual(telmu.station, "TELMU")
        self.assertEqual(control.station, "CONTROL")
        latest = session.latest_readiness_by_station()
        self.assertTrue(latest["TELMU"].ready)
        self.assertFalse(latest["CONTROL"].ready)

    def test_actions_keep_original_station_authority_and_audit_actor(self):
        session = self._session()
        session.assign_stations("lm-systems-player", ("TELMU", "CONTROL"))
        session.assign_station("capcom-player", "CAPCOM")
        session.start()

        # CONTROL authorization must recognize ownership of the original station,
        # not the compact-mode label. The criterion itself is not triggered in the
        # nominal start state, so authorization passes and rule state blocks it.
        with self.assertRaisesRegex(ValueError, "criterion is not currently triggered"):
            session.record_control_delta_p_callout(
                "lm-systems-player",
                basis="compact-mode authorization test",
            )

        with self.assertRaisesRegex(ValueError, "Only CAPCOM"):
            session.transmit_capcom_item("lm-systems-player", 1)


if __name__ == "__main__":
    unittest.main()
