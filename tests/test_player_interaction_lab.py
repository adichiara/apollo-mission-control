from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PlayerInteractionLabContractTests(unittest.TestCase):
    def setUp(self):
        self.html = (ROOT / "web" / "player_lab.html").read_text(encoding="utf-8")
        self.web_app = (
            ROOT / "src" / "apollo_mission_control" / "web_app.py"
        ).read_text(encoding="utf-8")
        self.admin = (ROOT / "web" / "admin.html").read_text(encoding="utf-8")

    def test_lab_is_exposed_as_non_final_static_route(self):
        self.assertIn('@app.get("/player-lab"', self.web_app)
        self.assertIn('WEB_ROOT / "player_lab.html"', self.web_app)
        self.assertIn("player interaction lab", self.html)
        self.assertIn("prototype surface", self.html)

    def test_facilitator_console_links_to_lab(self):
        self.assertIn("OPEN PLAYER INTERACTION LAB", self.admin)
        self.assertIn('href="/player-lab"', self.admin)

    def test_lab_is_deliberately_limited_to_flight_and_capcom(self):
        self.assertIn('<option value="FLIGHT">FLIGHT</option>', self.html)
        self.assertIn('<option value="CAPCOM">CAPCOM</option>', self.html)
        self.assertNotIn('<option value="CONTROL">', self.html)
        self.assertNotIn("LM_SYSTEMS", self.html)
        self.assertNotIn("FLIGHT_DYNAMICS", self.html)

    def test_lab_uses_existing_authoritative_session_actions(self):
        self.assertIn("/api/session/join", self.html)
        self.assertIn("/api/session/player/", self.html)
        self.assertIn("/readiness", self.html)
        self.assertIn("/api/session/flight/", self.html)
        self.assertIn("/decision", self.html)
        self.assertIn("/capcom", self.html)
        self.assertIn("/api/session/capcom/", self.html)
        self.assertIn("/transmit/", self.html)

    def test_lab_does_not_expose_delta_p_solution_or_evidence_assessor(self):
        self.assertNotIn("ΔP SHUTDOWN", self.html)
        self.assertNotIn("delta-p-callout", self.html)
        self.assertNotIn("shutdown-evidence", self.html)
        self.assertNotIn("ASSESS SHUTDOWN EVIDENCE", self.html)

    def test_lab_does_not_render_developer_model_metadata(self):
        self.assertNotIn("source_layer", self.html)
        self.assertNotIn("provenance", self.html)
        self.assertNotIn("f.validity", self.html)
        self.assertIn("deliberately omits model provenance", self.html)

    def test_flight_and_capcom_preserve_distinct_workflows(self):
        self.assertIn("FLIGHT DISPOSITION", self.html)
        self.assertIn("CREW-FACING APPROVAL", self.html)
        self.assertIn("APPROVED CREW-FACING ITEMS", self.html)
        self.assertIn("approval ≠ transmission", self.html)
        self.assertIn("TRANSMIT TO CREW", self.html)
        self.assertIn("Crew receipt/readback remains a separate event", self.html)

    def test_lab_keeps_station_identity_and_get_persistent(self):
        self.assertIn('id="callsign"', self.html)
        self.assertIn("GET ", self.html)
        self.assertIn("apollo_player_lab_identity_v1", self.html)
        self.assertIn("attemptRejoin", self.html)


if __name__ == "__main__":
    unittest.main()
