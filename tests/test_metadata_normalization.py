from pdf_pipeline.metadata import normalize_metadata


def test_hhaa041_prefers_volume_issue_year() -> None:
    metadata = {
        "title": "OP-REVF200042",
        "authors": ["Author A"],
        "doi": "10.1093/rfs/hhaa041",
        "raw_pdf_metadata": {
            "creationDate": "D:20201215162743Z",
            "modDate": "D:20260208020050+00'00'",
        },
    }
    text = "\n".join(
        [
            "Received April 22, 2019; editorial decision January 20, 2020.",
            "The Review of Financial Studies 34 (2021) 394-450",
            "The Author(s) 2020. Published by Oxford University Press.",
            "doi:10.1093/rfs/hhaa041",
            "Advance Access publication March 30, 2020",
        ]
    )

    normalized = normalize_metadata(metadata, text_hint=text)

    assert normalized["publication_year"] == 2021
    assert normalized["year"] == 2021
    assert normalized["year_resolution_reason"].startswith("volume_issue_year")
    assert normalized["raw_pdf_year"] == 2020


def test_rfaf016_prefers_journal_or_doi_year() -> None:
    metadata = {
        "title": "Pricing event risk: evidence from concave implied volatility curves",
        "authors": [],
        "doi": "10.1093/rof/rfaf016",
        "raw_pdf_metadata": {
            "creationDate": "D:20250628183807+05'30'",
        },
    }
    text = "\n".join(
        [
            "Review of Finance, 2025, 29, 963-1007",
            "https://doi.org/10.1093/rof/rfaf016",
            "Advance Access Publication Date: 14 March 2025",
            "Ball and Brown (1968)",
        ]
    )

    normalized = normalize_metadata(metadata, text_hint=text)

    assert normalized["publication_year"] == 2025
    assert normalized["year"] == 2025
    assert normalized["year_resolution_reason"].split(":")[0] in {
        "doi_journal_citation_line",
        "volume_issue_year",
    }


def test_raw_pdf_year_is_not_canonical_when_no_text_year() -> None:
    metadata = {
        "title": "Unknown",
        "authors": [],
        "doi": None,
        "raw_pdf_metadata": {
            "creationDate": "D:20140101120000Z",
        },
    }
    normalized = normalize_metadata(metadata, text_hint="No publication metadata found.")

    assert normalized["publication_year"] is None
    assert normalized["year"] is None
    assert normalized["raw_pdf_year"] == 2014
    assert "raw_pdf_year_ignored" in normalized["year_resolution_reason"]


def test_arxiv_source_file_year_beats_older_copyright_year() -> None:
    metadata = {
        "title": "arXiv:2002.00085v1 [q-fin.ST] 31 Jan 2020",
        "authors": [],
        "doi": None,
        "raw_pdf_metadata": {"creationDate": "D:20200201120000Z"},
    }
    text = "\n".join(
        [
            "Copyright 2014 by Example Publisher",
            "Some intro text with older references.",
        ]
    )

    normalized = normalize_metadata(
        metadata,
        text_hint=text,
        source_file="2002.00085v1.pdf",
    )

    assert normalized["year"] == 2020
    assert normalized["year_resolution_reason"] == "preprint_header:2020"
