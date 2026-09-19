from scripts.query_research import formal_labels, source_heading_kind


def test_formal_labels_do_not_promote_partial_to_documented():
    assert formal_labels("**PARTIALLY DOCUMENTED** — some details remain open") == [
        "PARTIALLY DOCUMENTED"
    ]


def test_formal_labels_can_report_mixed_claim_states():
    text = "**DOCUMENTED** — first claim\n**UNRESOLVED** — second claim"
    assert formal_labels(text) == ["DOCUMENTED", "UNRESOLVED"]


def test_source_heading_aliases_are_normalized_for_query():
    assert source_heading_kind("## Primary sources\n") == "legacy"
    assert source_heading_kind("## Sources\n") == "canonical"
    assert source_heading_kind("## Sources\n\n## Source\n") == "mixed"
