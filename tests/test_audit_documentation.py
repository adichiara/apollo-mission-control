from pathlib import Path
import json
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.audit_documentation import (  # noqa: E402
    check_note_ids,
    check_withdrawn_claims,
    load_withdrawn_claims,
    repository_text_files,
)


class DocumentationAuditTests(unittest.TestCase):
    def test_duplicate_research_note_ids_are_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            research = root / "resources" / "research"
            research.mkdir(parents=True)
            (research / "123_first.md").write_text("a", encoding="utf-8")
            (research / "123_second.md").write_text("b", encoding="utf-8")
            self.assertEqual(
                check_note_ids(root),
                {"123": ["123_first.md", "123_second.md"]},
            )

    def test_withdrawn_claim_occurrence_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "resources" / "audits").mkdir(parents=True)
            (root / "resources" / "research").mkdir(parents=True)
            withdrawing = root / "resources" / "research" / "999_correction.md"
            withdrawing.write_text("correction", encoding="utf-8")
            config = {
                "schema_version": 1,
                "claims": [
                    {
                        "claim": "retired assertion",
                        "withdrawn_by": "resources/research/999_correction.md",
                        "replacement": "replacement",
                    }
                ],
            }
            (root / "resources" / "audits" / "withdrawn_claims.json").write_text(
                json.dumps(config),
                encoding="utf-8",
            )
            (root / "docs").mkdir()
            (root / "docs" / "derived.md").write_text(
                "This repeats the retired assertion.",
                encoding="utf-8",
            )

            claims = load_withdrawn_claims(root)
            hits = check_withdrawn_claims(
                root,
                repository_text_files(root),
                claims,
            )
            self.assertEqual(len(hits), 1)
            self.assertIn("docs/derived.md", hits[0])


    def test_withdrawn_claims_reject_malformed_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "resources" / "audits").mkdir(parents=True)
            (root / "resources" / "audits" / "withdrawn_claims.json").write_text(
                "{not-json",
                encoding="utf-8",
            )
            with self.assertRaises(json.JSONDecodeError):
                load_withdrawn_claims(root)

    def test_withdrawn_claims_reject_missing_withdrawn_by_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "resources" / "audits").mkdir(parents=True)
            config = {
                "schema_version": 1,
                "claims": [
                    {
                        "claim": "retired assertion",
                        "withdrawn_by": "resources/research/999_missing.md",
                    }
                ],
            }
            (root / "resources" / "audits" / "withdrawn_claims.json").write_text(
                json.dumps(config),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "does not exist"):
                load_withdrawn_claims(root)

    def test_withdrawn_claim_list_does_not_match_itself(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "resources" / "audits").mkdir(parents=True)
            (root / "resources" / "research").mkdir(parents=True)
            withdrawing = root / "resources" / "research" / "999_correction.md"
            withdrawing.write_text("correction", encoding="utf-8")
            config = {
                "schema_version": 1,
                "claims": [
                    {
                        "claim": "retired assertion",
                        "withdrawn_by": "resources/research/999_correction.md",
                    }
                ],
            }
            (root / "resources" / "audits" / "withdrawn_claims.json").write_text(
                json.dumps(config),
                encoding="utf-8",
            )
            claims = load_withdrawn_claims(root)
            self.assertEqual(
                check_withdrawn_claims(
                    root,
                    repository_text_files(root),
                    claims,
                ),
                [],
            )


if __name__ == "__main__":
    unittest.main()
