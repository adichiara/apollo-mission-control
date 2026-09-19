#!/usr/bin/env python3
"""Query research notes without inferring evidence status from prose."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_DIR = ROOT / "resources" / "research"
LEGACY_SOURCE_HEADINGS = {
    "Primary source",
    "Primary sources",
    "Primary evidence",
    "Primary-source findings",
    "Source",
}
EVIDENCE_CHOICES = ("DOCUMENTED", "PARTIALLY DOCUMENTED", "UNRESOLVED", "UNLABELED")


def formal_labels(text: str) -> list[str]:
    labels: list[str] = []
    if re.search(r"(?<!PARTIALLY )\bDOCUMENTED\b", text):
        labels.append("DOCUMENTED")
    if "PARTIALLY DOCUMENTED" in text:
        labels.append("PARTIALLY DOCUMENTED")
    if re.search(r"\bUNRESOLVED\b", text):
        labels.append("UNRESOLVED")
    return labels


def source_heading_kind(text: str) -> str:
    headings = set(re.findall(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE))
    canonical = "Sources" in headings
    legacy = bool(headings & LEGACY_SOURCE_HEADINGS)
    if canonical and legacy:
        return "mixed"
    if canonical:
        return "canonical"
    if legacy:
        return "legacy"
    return "none"


def note_title(path: Path, text: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else path.stem


def records() -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for path in sorted(RESEARCH_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        labels = formal_labels(text)
        out.append(
            {
                "id": path.name[:3] if re.match(r"^\d{3}_", path.name) else "",
                "path": str(path.relative_to(ROOT)),
                "title": note_title(path, text),
                "evidence_labels": labels or ["UNLABELED"],
                "source_heading": source_heading_kind(text),
                "_text": text,
            }
        )
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", help="case-insensitive full-text filter")
    parser.add_argument("--evidence", choices=EVIDENCE_CHOICES)
    parser.add_argument(
        "--source-heading",
        choices=("canonical", "legacy", "mixed", "none"),
        help="filter by normalized source-heading state",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON instead of a Markdown table")
    args = parser.parse_args()

    matches = records()
    if args.text:
        needle = args.text.casefold()
        matches = [item for item in matches if needle in str(item["_text"]).casefold()]
    if args.evidence:
        matches = [
            item for item in matches
            if args.evidence in item["evidence_labels"]
        ]
    if args.source_heading:
        matches = [
            item for item in matches
            if item["source_heading"] == args.source_heading
        ]

    for item in matches:
        item.pop("_text", None)

    if args.json:
        print(json.dumps(matches, indent=2))
        return 0

    print(f"Matches: {len(matches)}")
    print()
    print("| ID | Evidence metadata | Source heading | Research note |")
    print("| --- | --- | --- | --- |")
    for item in matches:
        labels = ", ".join(item["evidence_labels"])
        title = str(item["title"]).replace("|", "\\|")
        print(
            f"| {item['id']} | {labels} | {item['source_heading']} | "
            f"[{title}](../{item['path']}) |"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
