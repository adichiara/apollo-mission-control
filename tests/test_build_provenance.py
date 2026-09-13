from pathlib import Path
import os
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from apollo_mission_control.build_provenance import build_provenance  # noqa: E402


class BuildProvenanceTests(unittest.TestCase):
    def test_render_commit_takes_precedence(self):
        with patch.dict(
            os.environ,
            {
                "RENDER": "true",
                "RENDER_GIT_COMMIT": "render-sha",
                "APOLLO_BUILD_COMMIT": "fallback-sha",
                "RENDER_SERVICE_ID": "srv-test",
                "RENDER_SERVICE_NAME": "apollo-test",
            },
            clear=True,
        ):
            info = build_provenance()
        self.assertEqual(info["commit"], "render-sha")
        self.assertEqual(info["environment"], "render")
        self.assertEqual(info["service_id"], "srv-test")
        self.assertEqual(info["service_name"], "apollo-test")

    def test_ci_or_local_override_is_available(self):
        with patch.dict(os.environ, {"APOLLO_BUILD_COMMIT": "ci-sha"}, clear=True):
            info = build_provenance()
        self.assertEqual(info["commit"], "ci-sha")
        self.assertEqual(info["environment"], "local")
        self.assertIsNone(info["service_id"])

    def test_unknown_is_explicit_not_fabricated(self):
        with patch.dict(os.environ, {}, clear=True):
            info = build_provenance()
        self.assertEqual(info["commit"], "unknown")
        self.assertEqual(info["environment"], "local")


if __name__ == "__main__":
    unittest.main()
