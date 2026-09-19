#!/usr/bin/env python3
"""Regenerate research/source navigation indexes from the repository tree."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_INDEX = ROOT / "resources" / "RESEARCH_INDEX.md"
PRIMARY_SOURCE_CATALOG = ROOT / "resources" / "PRIMARY_SOURCE_CATALOG.md"
RESEARCH_DIR = ROOT / "resources" / "research"
SOURCE_CATALOG_DIR = ROOT / "resources" / "source-catalog"
SOURCE_INDEX_START = "<!-- SOURCE-CATALOG-INDEX:START -->"
SOURCE_INDEX_END = "<!-- SOURCE-CATALOG-INDEX:END -->"


def display_name(filename: str) -> str:
    text = re.sub(r"\.md$", "", filename)
    text = text.replace("_", " ")
    replacements = (
        (r"\bpc2\b", "PC+2"),
        (r"\blms\b", "LMS"),
        (r"\bgda\b", "GDA"),
        (r"\bapollo13\b", "Apollo 13"),
        (r"\bapollo\b", "Apollo"),
    )
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text


def research_files() -> list[Path]:
    return sorted(RESEARCH_DIR.glob("*.md"))


def source_catalog_files() -> list[Path]:
    return sorted(SOURCE_CATALOG_DIR.glob("*.md"))


def render_research_index() -> str:
    files = research_files()
    out = [
        "# Research Note Index",
        "",
        "This is the master navigation index for `resources/research/`.",
        "",
        "It is an index, not an evidence upgrade. The presence of a note here says only that the note exists. Historical claim status remains governed by `docs/PROJECT_PRINCIPLES.md` and the note itself.",
        "",
        "## Retrieval conventions",
        "",
        "New research notes use:",
        "",
        "- `## Sources` for source references;",
        "- `## Evidence status` for explicit claim-scoped use of `DOCUMENTED`, `PARTIALLY DOCUMENTED`, and/or `UNRESOLVED`;",
        "- `## Findings` for source-derived findings when useful;",
        "- `## Unresolved` for open gaps when useful.",
        "",
        "Legacy notes predate this convention. They remain indexed without silent relabeling; `UNLABELED` in retrieval tooling means only that canonical evidence metadata has not yet been normalized, not that the historical question is unresolved.",
        "",
        "For corpus retrieval, use `python3 scripts/query_research.py`. Examples: `--text DDP-224`, `--evidence UNRESOLVED`, `--evidence UNLABELED`, and `--source-heading legacy`. The query tool reports only labels that literally occur in a note; it does not infer evidence status from prose.",
        "",
        "Run `python3 scripts/update_research_indexes.py` after adding or renaming research notes or source-catalog supplements.",
        "",
    ]
    for block_start in (0, 100, 200, 300):
        block = []
        for path in files:
            match = re.match(r"^(\d{3})_", path.name)
            if match and block_start <= int(match.group(1)) < block_start + 100:
                block.append(path)
        if not block:
            continue
        out.extend([
            f"## {block_start:03d}–{block_start + 99:03d}",
            "",
        ])
        for path in block:
            note_id = path.name[:3]
            out.append(
                f"- **{note_id}** — [{display_name(path.name[4:])}](research/{path.name})"
            )
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def source_group(filename: str) -> str:
    if filename.startswith("PC2_"):
        return "Apollo 13 PC+2"
    if filename.startswith("LMS_"):
        return "Lunar Module Simulator"
    if filename.startswith(("GDA_", "AGS_")):
        return "Guidance / GDA / AGS"
    return "General simulation, validation, and platform"


def render_source_catalog_index() -> str:
    groups = (
        "General simulation, validation, and platform",
        "Guidance / GDA / AGS",
        "Lunar Module Simulator",
        "Apollo 13 PC+2",
    )
    files = source_catalog_files()
    out = [
        SOURCE_INDEX_START,
        "## Scoped source-catalog index",
        "",
        "The detailed files under `source-catalog/` remain the scoped source ledgers for implementation and research threads. This master catalog indexes every supplement so the source corpus cannot become invisible merely because detail lives in a scoped file. Duplicate source detail is not copied here unless a canonical source-identity record belongs in the master catalog.",
        "",
    ]
    for group in groups:
        out.extend([f"### {group}", ""])
        for path in files:
            if source_group(path.name) == group:
                out.append(
                    f"- [{display_name(path.name)}](source-catalog/{path.name})"
                )
        out.append("")
    out.append(SOURCE_INDEX_END)
    return "\n".join(out)


def render_primary_source_catalog(current: str) -> str:
    block = render_source_catalog_index()
    if SOURCE_INDEX_START in current and SOURCE_INDEX_END in current:
        start = current.index(SOURCE_INDEX_START)
        end = current.index(SOURCE_INDEX_END) + len(SOURCE_INDEX_END)
        return current[:start] + block + current[end:]
    marker = "\n---\n"
    pos = current.find(marker)
    if pos < 0:
        raise ValueError("PRIMARY_SOURCE_CATALOG.md has no insertion marker")
    return current[:pos] + "\n\n" + block + "\n" + current[pos:]


def update_file(path: Path, expected: str, check: bool) -> bool:
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    if current == expected:
        return True
    if check:
        print(f"stale index: {path.relative_to(ROOT)}")
        return False
    path.write_text(expected, encoding="utf-8")
    print(f"updated {path.relative_to(ROOT)}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail instead of writing when generated indexes are stale",
    )
    args = parser.parse_args()

    research_ok = update_file(RESEARCH_INDEX, render_research_index(), args.check)
    current_primary = PRIMARY_SOURCE_CATALOG.read_text(encoding="utf-8")
    source_ok = update_file(
        PRIMARY_SOURCE_CATALOG,
        render_primary_source_catalog(current_primary),
        args.check,
    )
    return 0 if research_ok and source_ok else 1


if __name__ == "__main__":
    sys.exit(main())
