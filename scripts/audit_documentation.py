#!/usr/bin/env python3
"""Inventory documentation links and report reproducible evidence-audit issues."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path
from urllib.parse import urldefrag


URL_RE = re.compile(r"https?://[^\s)>\]}]+")
MARKDOWN_LINK_RE = re.compile(r"!?\[[^]]*\]\(([^)]+)\)")
NOTE_RE = re.compile(r"^(\d{3})_.*\.md$")


def markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)


def clean_url(raw: str) -> str:
    return raw.rstrip(".,;:`'")


def check_internal_links(root: Path, files: list[Path]) -> list[str]:
    failures: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1).strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_path, _ = urldefrag(target)
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            if not resolved.exists():
                failures.append(f"{path.relative_to(root)} -> {target}")
    return failures


def check_note_ids(root: Path) -> dict[str, list[str]]:
    by_id: dict[str, list[str]] = {}
    research = root / "resources" / "research"
    for path in sorted(research.glob("*.md")):
        match = NOTE_RE.match(path.name)
        if match:
            by_id.setdefault(match.group(1), []).append(path.name)
    return {key: value for key, value in by_id.items() if len(value) > 1}


def external_urls(files: list[Path]) -> tuple[list[str], Counter[str]]:
    references: list[str] = []
    for path in files:
        references.extend(clean_url(url) for url in URL_RE.findall(path.read_text(encoding="utf-8")))
    return sorted(set(references)), Counter(references)


def http_status(url: str, timeout: int) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "apollo-mission-control-evidence-audit/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return str(response.status)
    except urllib.error.HTTPError as exc:
        return str(exc.code)
    except Exception as exc:  # Network/TLS failures must remain distinguishable from HTTP failures.
        return f"ERROR:{type(exc).__name__}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-http", action="store_true", help="request every unique external URL")
    parser.add_argument("--timeout", type=int, default=20)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    files = markdown_files(root)
    urls, counts = external_urls(files)
    broken_internal = check_internal_links(root, files)
    duplicate_notes = check_note_ids(root)

    print(f"Markdown files: {len(files)}")
    print(f"External URL references: {sum(counts.values())}")
    print(f"Unique external URLs: {len(urls)}")
    print(f"Broken internal links: {len(broken_internal)}")
    for failure in broken_internal:
        print(f"  {failure}")
    print(f"Duplicate research-note IDs: {len(duplicate_notes)}")
    for note_id, names in duplicate_notes.items():
        print(f"  {note_id}: {', '.join(names)}")

    http_failures = 0
    if args.check_http:
        print("HTTP results:")
        for url in urls:
            status = http_status(url, args.timeout)
            print(f"  {status} {url}")
            if status != "200":
                http_failures += 1

    return 1 if broken_internal or http_failures else 0


if __name__ == "__main__":
    sys.exit(main())
