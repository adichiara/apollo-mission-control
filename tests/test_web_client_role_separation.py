from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fastapi.testclient import TestClient  # noqa: E402
from apollo_mission_control.web_app import app  # noqa: E402


class WebClientRoleSeparationTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_player_root_omits_validation_controls(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertIn("player station client", page.text)
        self.assertNotIn("PROTOTYPE TIME CONTROL", page.text)
        self.assertNotIn("CREATE / RESET", page.text)
        self.assertNotIn("APPLY INJECTION", page.text)
        self.assertNotIn("APPLY ENGINE-OFF RESPONSE", page.text)
        self.assertNotIn("REFRESH AUDIT", page.text)

    def test_admin_console_contains_validation_controls(self):
        page = self.client.get("/admin")
        self.assertEqual(page.status_code, 200)
        self.assertIn("VALIDATION ADMIN", page.text)
        self.assertIn("CREATE / RESET", page.text)
        self.assertIn("APPLY INJECTION", page.text)
        self.assertIn("APPLY ENGINE-OFF RESPONSE", page.text)
        self.assertIn("REFRESH AUDIT", page.text)
        self.assertIn("not an authentication boundary", page.text)


if __name__ == "__main__":
    unittest.main()
