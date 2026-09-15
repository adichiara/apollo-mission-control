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

    def test_admin_readiness_controls_are_explicit_reports(self):
        html = (ROOT / "web" / "admin.html").read_text(encoding="utf-8")
        self.assertIn("REPORT READY", html)
        self.assertIn("REPORT NOT READY", html)
        self.assertIn("controller_readiness_report", html)

    def test_admin_exposes_assumption_visible_model_proof(self):
        html = (ROOT / "web" / "admin.html").read_text(encoding="utf-8")
        self.assertIn("CAUSAL MODEL PROOF", html)
        self.assertIn("NOT HISTORICALLY VALIDATED", html)
        self.assertIn("/api/admin/model-proof/dps-burn", html)
        self.assertIn("manual facilitator-console inputs; not historical evidence", html)

    def test_admin_links_to_causal_model_lab(self):
        html = (ROOT / "web" / "admin.html").read_text(encoding="utf-8")
        self.assertIn("OPEN CAUSAL MODEL LAB", html)
        self.assertIn("/model-tests", html)
        self.assertIn("trajectory→tracking", html)
        self.assertIn("resource→power→observation", html)

    def test_contingency_page_exposes_inverter_crew_reobservation_chain(self):
        html = (ROOT / "web" / "contingency.html").read_text(encoding="utf-8")
        self.assertIn("PC+2 Contingency Tests", html)
        self.assertIn("Inverter transfer / fresh re-observation chain", html)
        self.assertIn("/api/session/flight/test-flight/inverter-transfer", html)
        self.assertIn("/api/session/crew/inverter-transfer/", html)
        self.assertIn("/api/session/crew/inverter-transfer-report/", html)
        self.assertIn("/api/session/admin/inverter-rule", html)
        self.assertIn("CB(11) EPS: INV 1", html)
        self.assertIn("0.1 s ordering increment is test infrastructure", html)

    def test_admin_engine_off_override_has_no_dead_item_id_input(self):
        html = (ROOT / "web" / "admin.html").read_text(encoding="utf-8")
        self.assertIn("APPLY ENGINE-OFF RESPONSE", html)
        self.assertIn("No CAPCOM item ID is consumed by this action", html)
        self.assertNotIn('id="shutdownItem"', html)
        self.assertNotIn("SHUTDOWN ITEM ID", html)


if __name__ == "__main__":
    unittest.main()
