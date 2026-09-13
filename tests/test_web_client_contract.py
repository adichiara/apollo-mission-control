from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class WebClientContractTests(unittest.TestCase):
    def test_browser_persists_identity_and_attempts_rejoin(self):
        html = (ROOT / "web" / "index.html").read_text(encoding="utf-8")
        self.assertIn("apollo_pc2_player_identity_v2", html)
        self.assertIn("apollo_pc2_player_identity_v1", html)  # legacy migration
        self.assertIn("localStorage.setItem", html)
        self.assertIn("attemptStoredRejoin", html)
        self.assertIn("/api/session/join", html)
        self.assertIn("/api/session/join-set", html)

    def test_compact_roles_preserve_original_station_navigation(self):
        html = (ROOT / "web" / "index.html").read_text(encoding="utf-8")
        self.assertIn("LM_SYSTEMS:['TELMU','CONTROL']", html)
        self.assertIn("FLIGHT_DYNAMICS:['GUIDO','FIDO_RETRO']", html)
        self.assertIn("switchStation", html)
        self.assertIn("activeStation", html)
        self.assertIn("station:activeStation", html)
        self.assertIn("simulator conveniences", html)

    def test_control_delta_p_action_is_player_facing_but_injection_is_not(self):
        html = (ROOT / "web" / "index.html").read_text(encoding="utf-8")
        self.assertIn("CALL OUT ΔP SHUTDOWN CRITERION", html)
        self.assertIn("/delta-p-callout", html)
        self.assertNotIn("/api/session/admin/injection", html)


if __name__ == "__main__":
    unittest.main()
