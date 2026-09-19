from pathlib import Path
import json
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.audit_documentation import (  # noqa: E402
    check_catalog_index_coverage,
    check_note_ids,
    check_research_metadata,
    check_withdrawn_claims,
    load_research_metadata_legacy,
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

    def test_new_research_note_requires_canonical_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            research = root / "resources" / "research"
            research.mkdir(parents=True)
            note = research / "400_new_thread.md"
            note.write_text(
                "# Test\n\n## Primary sources\n\nsource\n",
                encoding="utf-8",
            )
            failures = check_research_metadata(root, set())
            self.assertTrue(any("missing canonical '## Sources'" in item for item in failures))
            self.assertTrue(any("legacy source heading" in item for item in failures))
            self.assertTrue(any("missing '## Evidence status'" in item for item in failures))

    def test_new_research_note_accepts_claim_scoped_status(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            research = root / "resources" / "research"
            research.mkdir(parents=True)
            note = research / "400_new_thread.md"
            note.write_text(
                "# Test\n\n## Sources\n\n- source\n\n"
                "## Evidence status\n\n- **DOCUMENTED** — source directly supports this claim.\n",
                encoding="utf-8",
            )
            self.assertEqual(check_research_metadata(root, set()), [])

    def test_legacy_research_note_is_format_exempt(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            research = root / "resources" / "research"
            research.mkdir(parents=True)
            note = research / "123_old.md"
            note.write_text("# Old\n\n## Primary evidence\n", encoding="utf-8")
            self.assertEqual(check_research_metadata(root, {"123_old.md"}), [])

    def test_legacy_baseline_loader_rejects_duplicates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            audits = root / "resources" / "audits"
            audits.mkdir(parents=True)
            (audits / "research_metadata_legacy.json").write_text(
                json.dumps({"schema_version": 1, "notes": ["123_old.md", "123_old.md"]}),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "duplicate"):
                load_research_metadata_legacy(root)

    def test_catalog_indexes_must_cover_tree(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            resources = root / "resources"
            research = resources / "research"
            source_catalog = resources / "source-catalog"
            research.mkdir(parents=True)
            source_catalog.mkdir(parents=True)
            (research / "400_note.md").write_text("# Note", encoding="utf-8")
            (source_catalog / "TEST_SOURCES.md").write_text("# Sources", encoding="utf-8")
            (resources / "RESEARCH_INDEX.md").write_text("# index\n", encoding="utf-8")
            (resources / "PRIMARY_SOURCE_CATALOG.md").write_text("# catalog\n", encoding="utf-8")

            failures = check_catalog_index_coverage(root)
            self.assertEqual(len(failures), 2)
            self.assertTrue(any("research/400_note.md" in item for item in failures))
            self.assertTrue(any("source-catalog/TEST_SOURCES.md" in item for item in failures))


if __name__ == "__main__":
    unittest.main()
