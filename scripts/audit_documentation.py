#!/usr/bin/env python3
"""Inventory documentation links and enforce reproducible evidence-audit issues."""

from __future__ import annotations

import argparse
import json
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
TEXT_SUFFIXES = {
    ".md", ".json", ".py", ".txt", ".toml", ".yml", ".yaml",
    ".html", ".js", ".css", ".ini", ".cfg",
}
WITHDRAWN_CLAIMS_PATH = Path("resources/audits/withdrawn_claims.json")


def markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)


def repository_text_files(root: Path) -> list[Path]:
    return sorted(
        p for p in root.rglob("*")
        if p.is_file()
        and ".git" not in p.parts
        and p.suffix.lower() in TEXT_SUFFIXES
        and p.relative_to(root) != WITHDRAWN_CLAIMS_PATH
    )


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


def load_withdrawn_claims(root: Path) -> list[dict[str, str]]:
    path = root / WITHDRAWN_CLAIMS_PATH
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("claims"), list):
        raise ValueError("withdrawn claims file must contain a 'claims' list")

    claims: list[dict[str, str]] = []
    seen: set[str] = set()
    for item in data["claims"]:
        if not isinstance(item, dict):
            raise ValueError("withdrawn claim entries must be objects")
        claim = item.get("claim")
        withdrawn_by = item.get("withdrawn_by")
        replacement = item.get("replacement", "")
        if not isinstance(claim, str) or not claim:
            raise ValueError("withdrawn claim text must be a non-empty string")
        if not isinstance(withdrawn_by, str) or not withdrawn_by:
            raise ValueError("withdrawn_by must be a non-empty path string")
        if claim in seen:
            raise ValueError(f"duplicate withdrawn claim string: {claim}")
        seen.add(claim)
        if not (root / withdrawn_by).exists():
            raise ValueError(f"withdrawn_by path does not exist: {withdrawn_by}")
        claims.append(
            {
                "claim": claim,
                "withdrawn_by": withdrawn_by,
                "replacement": replacement if isinstance(replacement, str) else "",
            }
        )
    return claims


def check_withdrawn_claims(
    root: Path,
    files: list[Path],
    claims: list[dict[str, str]],
) -> list[str]:
    failures: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for item in claims:
            claim = item["claim"]
            if claim in text:
                failures.append(
                    f"{path.relative_to(root)} contains withdrawn claim {claim!r} "
                    f"(withdrawn by {item['withdrawn_by']})"
                )
    return failures


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
    except Exception as exc:
        return f"ERROR:{type(exc).__name__}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-http", action="store_true", help="request every unique external URL")
    parser.add_argument("--timeout", type=int, default=20)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    markdown = markdown_files(root)
    text_files = repository_text_files(root)
    urls, counts = external_urls(markdown)
    broken_internal = check_internal_links(root, markdown)
    duplicate_notes = check_note_ids(root)

    withdrawn_config_error: str | None = None
    withdrawn_hits: list[str] = []
    try:
        withdrawn_claims = load_withdrawn_claims(root)
        withdrawn_hits = check_withdrawn_claims(root, text_files, withdrawn_claims)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        withdrawn_config_error = str(exc)

    print(f"Markdown files: {len(markdown)}")
    print(f"External URL references: {sum(counts.values())}")
    print(f"Unique external URLs: {len(urls)}")
    print(f"Broken internal links: {len(broken_internal)}")
    for failure in broken_internal:
        print(f"  {failure}")
    print(f"Duplicate research-note IDs: {len(duplicate_notes)}")
    for note_id, names in duplicate_notes.items():
        print(f"  {note_id}: {', '.join(names)}")
    if withdrawn_config_error:
        print(f"Withdrawn-claims configuration error: {withdrawn_config_error}")
    print(f"Withdrawn-claim occurrences: {len(withdrawn_hits)}")
    for failure in withdrawn_hits:
        print(f"  {failure}")

    http_failures = 0
    if args.check_http:
        print("HTTP results:")
        for url in urls:
            status = http_status(url, args.timeout)
            print(f"  {status} {url}")
            if status != "200":
                http_failures += 1

    return 1 if (
        broken_internal
        or duplicate_notes
        or withdrawn_config_error
        or withdrawn_hits
        or http_failures
    ) else 0


if __name__ == "__main__":
    sys.exit(main())
