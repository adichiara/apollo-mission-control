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
RESEARCH_METADATA_LEGACY_PATH = Path("resources/audits/research_metadata_legacy.json")
RESEARCH_INDEX_PATH = Path("resources/RESEARCH_INDEX.md")
PRIMARY_SOURCE_CATALOG_PATH = Path("resources/PRIMARY_SOURCE_CATALOG.md")
EVIDENCE_LABELS = ("DOCUMENTED", "PARTIALLY DOCUMENTED", "UNRESOLVED")
RESEARCH_THREAD_RE = re.compile(r"^Research thread:\s*`([^`]+)`\s*$", re.MULTILINE)
CLOSED_LEGACY_LAST_ID = 328
FIRST_ALLOCATED_BLOCK_START = 400
LEGACY_SOURCE_HEADINGS = (
    "Primary source",
    "Primary sources",
    "Primary evidence",
    "Primary-source findings",
    "Source",
)


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


def check_research_block_allocation(root: Path) -> list[str]:
    """Enforce machine-allocated post-legacy research-number blocks.

    IDs through 328 are grandfathered. 329-399 are permanently closed. New
    research starts at a hundred-block boundary (400, 500, ...) and every note
    in that block declares the same stable Research thread slug.
    """
    failures: list[str] = []
    research = root / "resources" / "research"
    blocks: dict[int, list[tuple[int, Path]]] = {}

    for path in sorted(research.glob("*.md")):
        match = NOTE_RE.match(path.name)
        if not match:
            continue
        identifier = int(match.group(1))

        if CLOSED_LEGACY_LAST_ID < identifier < FIRST_ALLOCATED_BLOCK_START:
            failures.append(
                f"{path.relative_to(root)} uses closed legacy research ID "
                f"{identifier:03d}; new threads must start at 400 or above"
            )
            continue

        if identifier < FIRST_ALLOCATED_BLOCK_START:
            continue

        block_start = (identifier // 100) * 100
        blocks.setdefault(block_start, []).append((identifier, path))

    for block_start, entries in sorted(blocks.items()):
        ids = {identifier for identifier, _ in entries}
        if block_start not in ids:
            failures.append(
                f"research block {block_start:03d}-{block_start + 99:03d} "
                f"is unclaimed: first note must be {block_start:03d}_*.md"
            )

        threads: dict[str, list[str]] = {}
        for _identifier, path in entries:
            text = path.read_text(encoding="utf-8")
            match = RESEARCH_THREAD_RE.search(text)
            if match is None:
                failures.append(
                    f"{path.relative_to(root)} missing canonical "
                    f"'Research thread: `<slug>`' metadata"
                )
                continue
            thread = match.group(1).strip()
            if not thread:
                failures.append(
                    f"{path.relative_to(root)} has empty Research thread metadata"
                )
                continue
            threads.setdefault(thread, []).append(path.name)

        if len(threads) > 1:
            detail = "; ".join(
                f"{thread}: {', '.join(names)}"
                for thread, names in sorted(threads.items())
            )
            failures.append(
                f"research block {block_start:03d}-{block_start + 99:03d} "
                f"contains multiple Research thread values: {detail}"
            )

    return failures


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


def load_research_metadata_legacy(root: Path) -> set[str]:
    path = root / RESEARCH_METADATA_LEGACY_PATH
    data = json.loads(path.read_text(encoding="utf-8"))
    notes = data.get("notes") if isinstance(data, dict) else None
    if not isinstance(notes, list) or not all(isinstance(name, str) and name for name in notes):
        raise ValueError("research metadata legacy file must contain a string 'notes' list")
    if len(notes) != len(set(notes)):
        raise ValueError("research metadata legacy file contains duplicate note names")
    return set(notes)


def _section(text: str, heading: str) -> str | None:
    match = re.search(rf"^## {re.escape(heading)}\s*$", text, flags=re.MULTILINE)
    if not match:
        return None
    remainder = text[match.end():]
    next_heading = re.search(r"^##\s+", remainder, flags=re.MULTILINE)
    return remainder[:next_heading.start()] if next_heading else remainder


def check_research_metadata(root: Path, legacy: set[str]) -> list[str]:
    failures: list[str] = []
    research = root / "resources" / "research"
    current = {path.name for path in research.glob("*.md")}

    for stale in sorted(legacy - current):
        failures.append(f"legacy metadata baseline references missing note: {stale}")

    for path in sorted(research.glob("*.md")):
        if path.name in legacy:
            continue
        text = path.read_text(encoding="utf-8")
        if not re.search(r"^## Sources\s*$", text, flags=re.MULTILINE):
            failures.append(f"{path.relative_to(root)} missing canonical '## Sources' heading")
        for heading in LEGACY_SOURCE_HEADINGS:
            if re.search(rf"^## {re.escape(heading)}\s*$", text, flags=re.MULTILINE):
                failures.append(
                    f"{path.relative_to(root)} uses legacy source heading '## {heading}'"
                )
        status = _section(text, "Evidence status")
        if status is None:
            failures.append(f"{path.relative_to(root)} missing '## Evidence status' section")
        elif not any(label in status for label in EVIDENCE_LABELS):
            failures.append(
                f"{path.relative_to(root)} evidence-status section contains no canonical label"
            )
    return failures


def check_catalog_index_coverage(root: Path) -> list[str]:
    failures: list[str] = []
    research_index = (root / RESEARCH_INDEX_PATH).read_text(encoding="utf-8")
    primary_catalog = (root / PRIMARY_SOURCE_CATALOG_PATH).read_text(encoding="utf-8")

    for path in sorted((root / "resources" / "research").glob("*.md")):
        target = f"research/{path.name}"
        if target not in research_index:
            failures.append(f"research index missing {target}")

    for path in sorted((root / "resources" / "source-catalog").glob("*.md")):
        target = f"source-catalog/{path.name}"
        if target not in primary_catalog:
            failures.append(f"primary source catalog missing {target}")

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
        # Network/TLS failures must remain distinguishable from HTTP failures.
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
    block_failures = check_research_block_allocation(root)
    index_failures = check_catalog_index_coverage(root)

    withdrawn_config_error: str | None = None
    withdrawn_hits: list[str] = []
    try:
        withdrawn_claims = load_withdrawn_claims(root)
        withdrawn_hits = check_withdrawn_claims(root, text_files, withdrawn_claims)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        withdrawn_config_error = str(exc)

    metadata_config_error: str | None = None
    metadata_failures: list[str] = []
    legacy_count = 0
    try:
        legacy = load_research_metadata_legacy(root)
        legacy_count = len(legacy)
        metadata_failures = check_research_metadata(root, legacy)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        metadata_config_error = str(exc)

    print(f"Markdown files: {len(markdown)}")
    print(f"External URL references: {sum(counts.values())}")
    print(f"Unique external URLs: {len(urls)}")
    print(f"Broken internal links: {len(broken_internal)}")
    for failure in broken_internal:
        print(f"  {failure}")
    print(f"Duplicate research-note IDs: {len(duplicate_notes)}")
    for note_id, names in duplicate_notes.items():
        print(f"  {note_id}: {', '.join(names)}")
    print(f"Research block-allocation failures: {len(block_failures)}")
    for failure in block_failures:
        print(f"  {failure}")
    print(f"Catalog/index coverage failures: {len(index_failures)}")
    for failure in index_failures:
        print(f"  {failure}")
    if withdrawn_config_error:
        print(f"Withdrawn-claims configuration error: {withdrawn_config_error}")
    print(f"Withdrawn-claim occurrences: {len(withdrawn_hits)}")
    for failure in withdrawn_hits:
        print(f"  {failure}")
    if metadata_config_error:
        print(f"Research-metadata configuration error: {metadata_config_error}")
    print(f"Legacy research-metadata exemptions: {legacy_count}")
    print(f"Research-metadata failures: {len(metadata_failures)}")
    for failure in metadata_failures:
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
        or block_failures
        or index_failures
        or withdrawn_config_error
        or withdrawn_hits
        or metadata_config_error
        or metadata_failures
        or http_failures
    ) else 0


if __name__ == "__main__":
    sys.exit(main())
