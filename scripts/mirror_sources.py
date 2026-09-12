#!/usr/bin/env python3
"""Mirror and verify the project's primary sources.

Metadata lives in the source catalogs. This script handles retrieval and
integrity only: it downloads what the manifest says to mirror, records the
SHA-256 and byte size of each file, and re-checks those hashes later.

    python3 scripts/mirror_sources.py status
    python3 scripts/mirror_sources.py fetch [--id ID ...] [--force]
    python3 scripts/mirror_sources.py verify

See docs/SOURCE_MIRRORING.md for the tiering rule.

No third-party dependencies, matching the rest of the project's tooling.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = REPO_ROOT / "resources" / "primary-sources" / "manifest.json"
LOCK_PATH = REPO_ROOT / "resources" / "primary-sources" / "SOURCES.lock.json"

MIRRORED_TIERS = ("full", "pages")
VALID_TIERS = ("full", "pages", "link-only")
VALID_RIGHTS = (
    "us-gov",
    "nasa-contract",
    "third-party-scan-of-us-gov",
    "unclear",
)

# GitHub warns above 50 MB and refuses above 100 MB for a single file.
WARN_BYTES = 50 * 1024 * 1024
REFUSE_BYTES = 100 * 1024 * 1024

USER_AGENT = "apollo-mission-control source mirror (+https://github.com/adichiara/apollo-mission-control)"


def load_manifest(path: Path = MANIFEST_PATH) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_lock(path: Path = LOCK_PATH) -> dict:
    if not path.exists():
        return {"schema": 1, "files": {}}
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def write_lock(lock: dict, path: Path = LOCK_PATH) -> None:
    lock["files"] = dict(sorted(lock["files"].items()))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(lock, handle, indent=2, sort_keys=False)
        handle.write("\n")


def storage_dir(manifest: dict) -> Path:
    return REPO_ROOT / manifest.get("storage", "resources/primary-sources/files")


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def target_path(manifest: dict, doc: dict) -> Path:
    """Where a document's bytes belong on disk.

    `pages` entries are extracted by hand, so the expected filename carries a
    -pages suffix to make it obvious the file is not the whole document.
    """
    suffix = "-pages" if doc["tier"] == "pages" else ""
    return storage_dir(manifest) / f"{doc['id']}{suffix}.pdf"


def human(size: int) -> str:
    value = float(size)
    for unit in ("B", "KB", "MB", "GB"):
        if value < 1024 or unit == "GB":
            return f"{value:.0f} {unit}" if unit == "B" else f"{value:.1f} {unit}"
        value /= 1024
    return f"{value:.1f} GB"


def download(url: str, destination: Path) -> tuple[bool, str]:
    """Fetch one URL to destination. Returns (ok, message)."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    temporary = destination.with_suffix(destination.suffix + ".part")
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            declared = response.headers.get("Content-Length")
            if declared and int(declared) > REFUSE_BYTES:
                return False, (
                    f"{human(int(declared))} exceeds the {human(REFUSE_BYTES)} single-file "
                    "limit; reclassify this entry as tier 'pages'"
                )
            destination.parent.mkdir(parents=True, exist_ok=True)
            written = 0
            with temporary.open("wb") as handle:
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    written += len(chunk)
                    if written > REFUSE_BYTES:
                        handle.close()
                        temporary.unlink(missing_ok=True)
                        return False, (
                            f"exceeded {human(REFUSE_BYTES)} mid-transfer; reclassify as "
                            "tier 'pages'"
                        )
                    handle.write(chunk)
    except urllib.error.HTTPError as error:
        temporary.unlink(missing_ok=True)
        return False, f"HTTP {error.code}"
    except urllib.error.URLError as error:
        temporary.unlink(missing_ok=True)
        return False, f"unreachable ({error.reason}) - check the environment's network access level"
    except OSError as error:
        temporary.unlink(missing_ok=True)
        return False, str(error)

    temporary.replace(destination)
    return True, "ok"


def cmd_status(manifest: dict, lock: dict, _args) -> int:
    by_tier: dict[str, list[dict]] = {tier: [] for tier in VALID_TIERS}
    for doc in manifest["documents"]:
        by_tier[doc["tier"]].append(doc)

    mirrored_bytes = 0
    print(f"manifest: {len(manifest['documents'])} documents")
    for tier in VALID_TIERS:
        docs = by_tier[tier]
        if not docs:
            continue
        print(f"\n{tier} ({len(docs)})")
        for doc in sorted(docs, key=lambda d: d["id"]):
            if tier == "link-only":
                print(f"  -        {doc['id']}")
                continue
            path = target_path(manifest, doc)
            if path.exists():
                size = path.stat().st_size
                mirrored_bytes += size
                state = f"present  {human(size):>9}"
            else:
                state = "pending           "
            print(f"  {state}  {doc['id']}")

    pending = [
        doc
        for doc in manifest["documents"]
        if doc["tier"] in MIRRORED_TIERS and not target_path(manifest, doc).exists()
    ]
    print(f"\nmirrored: {human(mirrored_bytes)} across {len(lock['files'])} locked files")
    if pending:
        print(f"pending:  {len(pending)} documents - run 'fetch'")
    return 0


def cmd_fetch(manifest: dict, lock: dict, args) -> int:
    wanted = set(args.id or [])
    selected = [
        doc
        for doc in manifest["documents"]
        if doc["tier"] in MIRRORED_TIERS and (not wanted or doc["id"] in wanted)
    ]
    unknown = wanted - {doc["id"] for doc in manifest["documents"]}
    for identifier in sorted(unknown):
        print(f"unknown id: {identifier}", file=sys.stderr)
    if unknown:
        return 2

    failures = 0
    fetched = 0
    for doc in selected:
        path = target_path(manifest, doc)
        if path.exists() and not args.force:
            print(f"skip     {doc['id']} (present)")
            continue

        if doc["tier"] == "pages":
            print(
                f"manual   {doc['id']} - tier 'pages': extract "
                f"\"{doc.get('pages', 'the cited pages')}\" to {path.relative_to(REPO_ROOT)}"
            )
            continue

        last_error = "no urls listed"
        for url in doc["urls"]:
            ok, message = download(url, path)
            if ok:
                size = path.stat().st_size
                digest = sha256_of(path)
                lock["files"][doc["id"]] = {
                    "path": str(path.relative_to(REPO_ROOT)),
                    "sha256": digest,
                    "bytes": size,
                    "retrieved_from": url,
                }
                note = ""
                if size > WARN_BYTES:
                    note = f"  WARNING over {human(WARN_BYTES)}; consider tier 'pages'"
                print(f"fetched  {doc['id']}  {human(size)}  {digest[:12]}{note}")
                fetched += 1
                break
            last_error = message
            print(f"  .. {url}: {message}", file=sys.stderr)
        else:
            failures += 1
            print(f"FAILED   {doc['id']}: {last_error}", file=sys.stderr)

    if fetched:
        write_lock(lock)
    if failures:
        print(
            f"\n{failures} document(s) could not be fetched. If every entry failed as "
            "unreachable, the session's network access level does not allow these hosts "
            "(see docs/SOURCE_MIRRORING.md).",
            file=sys.stderr,
        )
    return 1 if failures else 0


def cmd_verify(manifest: dict, lock: dict, _args) -> int:
    if not lock["files"]:
        print("nothing locked yet - run 'fetch' first")
        return 0

    ids = {doc["id"] for doc in manifest["documents"]}
    problems = 0
    for identifier, entry in lock["files"].items():
        path = REPO_ROOT / entry["path"]
        if identifier not in ids:
            print(f"ORPHAN   {identifier} is locked but not in the manifest")
            problems += 1
            continue
        if not path.exists():
            print(f"MISSING  {identifier} at {entry['path']}")
            problems += 1
            continue
        actual = sha256_of(path)
        if actual != entry["sha256"]:
            print(f"MISMATCH {identifier}")
            print(f"         locked {entry['sha256']}")
            print(f"         actual {actual}")
            problems += 1
        else:
            print(f"ok       {identifier}")

    print(f"\n{len(lock['files']) - problems}/{len(lock['files'])} verified")
    return 1 if problems else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("status", help="what is mirrored, what is pending")

    fetch = subparsers.add_parser("fetch", help="download mirrored entries and write the lock")
    fetch.add_argument("--id", action="append", help="fetch only this id (repeatable)")
    fetch.add_argument("--force", action="store_true", help="re-download files already present")

    subparsers.add_parser("verify", help="re-hash local files against the lock")

    args = parser.parse_args(argv)
    manifest = load_manifest()
    lock = load_lock()

    commands = {"status": cmd_status, "fetch": cmd_fetch, "verify": cmd_verify}
    return commands[args.command](manifest, lock, args)


if __name__ == "__main__":
    sys.exit(main())
