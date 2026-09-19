from pathlib import Path
import unittest

from scripts.update_research_indexes import (
    PRIMARY_SOURCE_CATALOG,
    RESEARCH_BLOCK_ALLOCATION,
    RESEARCH_INDEX,
    render_primary_source_catalog,
    render_research_block_allocation,
    render_research_index,
)


class ResearchIndexGenerationTests(unittest.TestCase):
    def test_research_index_matches_generator(self):
        self.assertEqual(
            RESEARCH_INDEX.read_text(encoding="utf-8"),
            render_research_index(),
        )

    def test_research_block_allocation_matches_generator(self):
        self.assertEqual(
            RESEARCH_BLOCK_ALLOCATION.read_text(encoding="utf-8"),
            render_research_block_allocation(),
        )

    def test_primary_source_scoped_index_matches_generator(self):
        current = PRIMARY_SOURCE_CATALOG.read_text(encoding="utf-8")
        self.assertEqual(current, render_primary_source_catalog(current))


if __name__ == "__main__":
    unittest.main()
