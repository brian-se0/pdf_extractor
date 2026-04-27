from pdf_pipeline.dedup import build_duplicate_flags, normalize_doi


def test_normalize_doi_rejects_incomplete_elsevier_prefix() -> None:
    assert normalize_doi("10.1016/j") is None


def test_build_duplicate_flags_ignores_incomplete_doi_prefix() -> None:
    records = [
        {
            "paper_id": "first",
            "source_file": "first.pdf",
            "status": "success",
            "word_count": 1000,
            "table_count": 1,
            "figure_count": 1,
            "metadata": {"title": "First title", "doi": "10.1016/j"},
        },
        {
            "paper_id": "second",
            "source_file": "second.pdf",
            "status": "success",
            "word_count": 1000,
            "table_count": 1,
            "figure_count": 1,
            "metadata": {"title": "Second unrelated title", "doi": "10.1016/j"},
        },
    ]

    flags = build_duplicate_flags(records)

    assert flags["first"]["is_duplicate"] is False
    assert flags["second"]["is_duplicate"] is False


def test_build_duplicate_flags_accepts_complete_doi_match() -> None:
    records = [
        {
            "paper_id": "canonical",
            "source_file": "canonical.pdf",
            "status": "success",
            "word_count": 2000,
            "table_count": 1,
            "figure_count": 1,
            "metadata": {"title": "A title", "doi": "10.1002/fut.22302"},
        },
        {
            "paper_id": "duplicate",
            "source_file": "duplicate.pdf",
            "status": "success",
            "word_count": 1000,
            "table_count": 1,
            "figure_count": 1,
            "metadata": {"title": "A title", "doi": "https://doi.org/10.1002/fut.22302"},
        },
    ]

    flags = build_duplicate_flags(records)

    assert flags["canonical"]["is_duplicate"] is False
    assert flags["duplicate"]["is_duplicate"] is True
    assert flags["duplicate"]["duplicate_of"] == "canonical"
