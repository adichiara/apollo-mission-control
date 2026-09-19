from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PlayerInteractionLabContractTests(unittest.TestCase):
    def setUp(self):
        self.html = (ROOT / "web" / "player_lab.html").read_text(encoding="utf-8")
        self.web_app = (
            ROOT / "src" / "apollo_mission_control" / "web_app.py"
        ).read_text(encoding="utf-8")
        self.validation = (ROOT / "web" / "index.html").read_text(encoding="utf-8")
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
        self.assertNotIn("f.provenance", self.html)
        self.assertNotIn("f.validity", self.html)
        self.assertIn("deliberately omits model provenance", self.html)

    def test_lab_hides_internal_gate_and_raw_phase_state(self):
        self.assertNotIn("s.pending_gate", self.html)
        self.assertNotIn("PENDING '+esc(s.pending_gate)", self.html)
        self.assertIn("phaseLabel(s.phase)", self.html)
        self.assertIn("phaseLabel(f.value)", self.html)

    def test_lab_does_not_present_ambiguous_flight_go_boolean(self):
        self.assertIn("f.key!=='flight.go_for_burn'", self.html)
        self.assertIn("FLIGHT DISPOSITION", self.html)

    def test_join_controls_collapse_after_position_is_established(self):
        self.assertIn("$('joinPanel').classList.add('hidden')", self.html)
        self.assertGreaterEqual(
            self.html.count("$('joinPanel').classList.add('hidden')"),
            2,
        )

    def test_flight_and_capcom_preserve_distinct_workflows(self):
        self.assertIn("FLIGHT DISPOSITION", self.html)
        self.assertIn("CREW-FACING APPROVAL", self.html)
        self.assertIn("APPROVED CREW-FACING ITEMS", self.html)
        self.assertIn("approval ≠ transmission", self.html)
        self.assertIn("TRANSMIT TO CREW", self.html)
        self.assertIn("Crew receipt/readback remains a separate event", self.html)

    def test_capcom_queue_keeps_transmission_and_receipt_visibly_distinct(self):
        self.assertIn("APPROVED / PENDING", self.html)
        self.assertIn("TRANSMITTED / AWAITING RECEIPT", self.html)
        self.assertIn("CREW RECEIVED", self.html)
        self.assertIn("RECEIPT GET", self.html)
        self.assertIn("ACKNOWLEDGEMENT:", self.html)

    def test_playability_instrumentation_is_present_on_both_client_surfaces(self):
        for html, surface in (
            (self.html, "player_lab"),
            (self.validation, "validation_client"),
        ):
            self.assertIn("/api/session/instrumentation", html)
            self.assertIn(f"surface:'{surface}'", html)
            self.assertIn("client_elapsed_ms", html)
            self.assertIn("join_attempt", html)
            self.assertIn("join_success", html)
            self.assertIn("auto_rejoin_attempt", html)
            self.assertIn("auto_rejoin_success", html)
            self.assertIn("action_attempt", html)
            self.assertIn("action_success", html)
            self.assertIn("action_error", html)

    def test_validation_client_instruments_compact_station_switching(self):
        self.assertIn("station_switch", self.validation)
        self.assertIn("instrument('station_switch'", self.validation)

    def test_facilitator_can_export_playability_stream(self):
        self.assertIn("COPY PLAYABILITY LOG", self.admin)
        self.assertIn("/api/session/admin/playability-events", self.admin)
        self.assertIn("copyPlayabilityLog", self.admin)

    def test_playability_stream_is_separate_from_mission_audit_route(self):
        self.assertIn('@app.post("/api/session/instrumentation")', self.web_app)
        self.assertIn('"/api/session/admin/playability-events"', self.web_app)
        self.assertIn('@app.get("/api/session/audit"', self.web_app)

    def test_lab_keeps_station_identity_and_get_persistent(self):
        self.assertIn('id="callsign"', self.html)
        self.assertIn("GET ", self.html)
        self.assertIn("apollo_player_lab_identity_v1", self.html)
        self.assertIn("attemptRejoin", self.html)


if __name__ == "__main__":
    unittest.main()
