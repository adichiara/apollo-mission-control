import unittest

from scripts.query_research import formal_labels, source_heading_kind


class ResearchQueryTests(unittest.TestCase):
    def test_formal_labels_do_not_promote_partial_to_documented(self):
        self.assertEqual(
            formal_labels("**PARTIALLY DOCUMENTED** — some details remain open"),
            ["PARTIALLY DOCUMENTED"],
        )

    def test_formal_labels_can_report_mixed_claim_states(self):
        text = "**DOCUMENTED** — first claim\n**UNRESOLVED** — second claim"
        self.assertEqual(formal_labels(text), ["DOCUMENTED", "UNRESOLVED"])

    def test_source_heading_aliases_are_normalized_for_query(self):
        self.assertEqual(source_heading_kind("## Primary sources\n"), "legacy")
        self.assertEqual(source_heading_kind("## Sources\n"), "canonical")
        self.assertEqual(
            source_heading_kind("## Sources\n\n## Source\n"),
            "mixed",
        )


if __name__ == "__main__":
    unittest.main()
