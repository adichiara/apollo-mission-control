"""Tests for the primary-source manifest and the mirror/verify logic.

The manifest is provenance infrastructure, so its integrity is worth testing:
a duplicate id or an unknown tier would silently drop a document from
mirroring. The hash-verification path is tested against synthetic files so the
logic is exercised without network access.
"""

from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import mirror_sources  # noqa: E402


class ManifestIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = mirror_sources.load_manifest()
        cls.documents = cls.manifest["documents"]

    def test_manifest_has_expected_shape(self):
        self.assertEqual(self.manifest["schema"], 1)
        self.assertIn("storage", self.manifest)
        self.assertGreater(len(self.documents), 0)

    def test_ids_are_unique(self):
        ids = [doc["id"] for doc in self.documents]
        duplicates = sorted({i for i in ids if ids.count(i) > 1})
        self.assertEqual(duplicates, [], f"duplicate manifest ids: {duplicates}")

    def test_ids_are_filesystem_safe(self):
        for doc in self.documents:
            with self.subTest(doc=doc["id"]):
                self.assertRegex(doc["id"], r"^[a-z0-9][a-z0-9-]*$")

    def test_required_fields_present(self):
        for doc in self.documents:
            with self.subTest(doc=doc["id"]):
                for field in ("id", "title", "tier", "rights", "urls"):
                    self.assertIn(field, doc)

    def test_tiers_are_known(self):
        for doc in self.documents:
            with self.subTest(doc=doc["id"]):
                self.assertIn(doc["tier"], mirror_sources.VALID_TIERS)

    def test_rights_are_known(self):
        for doc in self.documents:
            with self.subTest(doc=doc["id"]):
                self.assertIn(doc["rights"], mirror_sources.VALID_RIGHTS)

    def test_mirrored_entries_have_at_least_one_url(self):
        for doc in self.documents:
            if doc["tier"] in mirror_sources.MIRRORED_TIERS:
                with self.subTest(doc=doc["id"]):
                    self.assertGreaterEqual(len(doc["urls"]), 1)

    def test_pages_entries_declare_which_pages(self):
        """A 'pages' entry without a page description cannot be extracted."""
        for doc in self.documents:
            if doc["tier"] == "pages":
                with self.subTest(doc=doc["id"]):
                    self.assertTrue(doc.get("pages"), f"{doc['id']} needs a 'pages' field")

    def test_urls_are_https(self):
        for doc in self.documents:
            for url in doc["urls"]:
                with self.subTest(doc=doc["id"], url=url):
                    self.assertTrue(url.startswith("https://"))

    def test_unclear_rights_are_not_full_mirrors_without_a_note(self):
        """Anything whose rights basis is doubtful must carry its reasoning."""
        for doc in self.documents:
            if doc["rights"] == "unclear" and doc["tier"] != "link-only":
                with self.subTest(doc=doc["id"]):
                    self.assertTrue(
                        doc.get("note"),
                        f"{doc['id']} mirrors content with unclear rights and needs a note",
                    )


class TargetPathTests(unittest.TestCase):
    def test_pages_files_are_named_distinctly(self):
        manifest = {"storage": "resources/primary-sources/files"}
        whole = mirror_sources.target_path(manifest, {"id": "doc-a", "tier": "full"})
        partial = mirror_sources.target_path(manifest, {"id": "doc-a", "tier": "pages"})
        self.assertNotEqual(whole, partial)
        self.assertTrue(partial.name.endswith("-pages.pdf"))


class VerifyTests(unittest.TestCase):
    def setUp(self):
        self._tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self._tempdir.name)
        self._saved_root = mirror_sources.REPO_ROOT
        mirror_sources.REPO_ROOT = self.root
        self.addCleanup(self._restore)

    def _restore(self):
        mirror_sources.REPO_ROOT = self._saved_root
        self._tempdir.cleanup()

    def _run_verify(self, manifest, lock):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = mirror_sources.cmd_verify(manifest, lock, None)
        return code, buffer.getvalue()

    def _write(self, relative, content: bytes):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return path

    def test_matching_hash_verifies(self):
        path = self._write("files/doc-a.pdf", b"apollo")
        manifest = {"documents": [{"id": "doc-a", "tier": "full"}]}
        lock = {
            "files": {
                "doc-a": {
                    "path": "files/doc-a.pdf",
                    "sha256": mirror_sources.sha256_of(path),
                    "bytes": 6,
                }
            }
        }
        code, output = self._run_verify(manifest, lock)
        self.assertEqual(code, 0)
        self.assertIn("ok       doc-a", output)

    def test_changed_bytes_are_detected(self):
        path = self._write("files/doc-a.pdf", b"apollo")
        digest = mirror_sources.sha256_of(path)
        path.write_bytes(b"apollo-revised")
        manifest = {"documents": [{"id": "doc-a", "tier": "full"}]}
        lock = {"files": {"doc-a": {"path": "files/doc-a.pdf", "sha256": digest, "bytes": 6}}}
        code, output = self._run_verify(manifest, lock)
        self.assertEqual(code, 1)
        self.assertIn("MISMATCH", output)

    def test_missing_file_is_reported(self):
        manifest = {"documents": [{"id": "doc-a", "tier": "full"}]}
        lock = {"files": {"doc-a": {"path": "files/doc-a.pdf", "sha256": "0" * 64, "bytes": 1}}}
        code, output = self._run_verify(manifest, lock)
        self.assertEqual(code, 1)
        self.assertIn("MISSING", output)

    def test_locked_file_absent_from_manifest_is_flagged(self):
        self._write("files/doc-b.pdf", b"x")
        manifest = {"documents": [{"id": "doc-a", "tier": "full"}]}
        lock = {"files": {"doc-b": {"path": "files/doc-b.pdf", "sha256": "0" * 64, "bytes": 1}}}
        code, output = self._run_verify(manifest, lock)
        self.assertEqual(code, 1)
        self.assertIn("ORPHAN", output)

    def test_empty_lock_is_not_an_error(self):
        code, output = self._run_verify({"documents": []}, {"files": {}})
        self.assertEqual(code, 0)
        self.assertIn("nothing locked yet", output)


class LockRoundTripTests(unittest.TestCase):
    def test_lock_is_written_sorted_and_reloadable(self):
        with tempfile.TemporaryDirectory() as name:
            path = Path(name) / "SOURCES.lock.json"
            lock = {"schema": 1, "files": {"z-doc": {"sha256": "b"}, "a-doc": {"sha256": "a"}}}
            mirror_sources.write_lock(lock, path)
            reloaded = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(list(reloaded["files"]), ["a-doc", "z-doc"])

    def test_absent_lock_loads_as_empty(self):
        with tempfile.TemporaryDirectory() as name:
            lock = mirror_sources.load_lock(Path(name) / "does-not-exist.json")
            self.assertEqual(lock["files"], {})


if __name__ == "__main__":
    unittest.main()
