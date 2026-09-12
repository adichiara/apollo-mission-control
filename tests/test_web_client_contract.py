from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class WebClientContractTests(unittest.TestCase):
    def test_browser_persists_identity_and_attempts_rejoin(self):
        html = (ROOT / "web" / "index.html").read_text(encoding="utf-8")
        self.assertIn("apollo_pc2_player_identity_v1", html)
        self.assertIn("localStorage.setItem", html)
        self.assertIn("attemptStoredRejoin", html)
        self.assertIn("/api/session/join", html)

    def test_control_delta_p_action_is_player_facing_but_injection_is_not(self):
        html = (ROOT / "web" / "index.html").read_text(encoding="utf-8")
        self.assertIn("CALL OUT ΔP SHUTDOWN CRITERION", html)
        self.assertIn("/delta-p-callout", html)
        self.assertNotIn("/api/session/admin/injection", html)


if __name__ == "__main__":
    unittest.main()
