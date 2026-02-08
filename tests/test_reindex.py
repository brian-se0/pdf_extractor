import json
from pathlib import Path

from pdf_pipeline.reindex import reindex_extracted_directory


def _write_manifest(folder: Path, payload: dict) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "manifest.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _write_paper_md(folder: Path, main_text: str) -> None:
    markdown = "\n".join(
        [
            "---",
            'paper_id: "x"',
            "---",
            "",
            "## Main Text",
            "",
            main_text,
            "",
            "## Tables",
            "",
            "None",
        ]
    )
    (folder / "paper.md").write_text(markdown, encoding="utf-8")


def test_reindex_backfills_years_and_marks_duplicate(tmp_path: Path) -> None:
    extracted_dir = tmp_path / "extracted"

    hhaa = extracted_dir / "hhaa041"
    _write_manifest(
        hhaa,
        {
            "paper_id": "hhaa041",
            "source_file": "hhaa041.pdf",
            "status": "success",
            "counts": {"words": 1000, "tables": 1, "figures": 1},
            "metadata": {
                "title": "OP-REVF200042",
                "authors": [],
                "year": 2019,
                "doi": "10.1093/rfs/hhaa041",
                "raw_pdf_metadata": {"creationDate": "D:20201215162743Z"},
            },
        },
    )
    _write_paper_md(
        hhaa,
        "\n".join(
            [
                "Received April 22, 2019; editorial decision January 20, 2020.",
                "The Review of Financial Studies 34 (2021) 394-450",
                "The Author(s) 2020. Published by Oxford University Press.",
                "doi:10.1093/rfs/hhaa041",
                "Advance Access publication March 30, 2020",
            ]
        ),
    )

    rfaf = extracted_dir / "rfaf016"
    _write_manifest(
        rfaf,
        {
            "paper_id": "rfaf016",
            "source_file": "rfaf016.pdf",
            "status": "success",
            "counts": {"words": 1000, "tables": 1, "figures": 1},
            "metadata": {
                "title": "Pricing event risk: evidence from concave implied volatility curves",
                "authors": [],
                "year": 1968,
                "doi": "10.1093/rof/rfaf016",
                "raw_pdf_metadata": {"creationDate": "D:20250628183807+05'30'"},
            },
        },
    )
    _write_paper_md(
        rfaf,
        "\n".join(
            [
                "Review of Finance, 2025, 29, 963-1007",
                "https://doi.org/10.1093/rof/rfaf016",
                "Advance Access Publication Date: 14 March 2025",
                "Ball and Brown (1968)",
            ]
        ),
    )

    canonical = extracted_dir / "2102-03945v1"
    _write_manifest(
        canonical,
        {
            "paper_id": "2102-03945v1",
            "source_file": "2102.03945v1.pdf",
            "status": "success",
            "counts": {"words": 5000, "tables": 3, "figures": 2},
            "metadata": {
                "title": "Variational Autoencoders:",
                "authors": [],
                "year": 2021,
                "doi": None,
                "raw_pdf_metadata": {"creationDate": "D:20210209020435Z"},
            },
        },
    )
    _write_paper_md(
        canonical,
        "\n".join(
            [
                "Variational Autoencoders: A Hands-Off Approach to Volatility",
                "Spring 2022",
                "A volatility surface is an important tool for pricing and hedging derivatives.",
                "The trained variational autoencoder can also be used to generate synthetic surfaces.",
            ]
        ),
    )

    ebsco = extracted_dir / "ebsco-fulltext-02-08-2026"
    _write_manifest(
        ebsco,
        {
            "paper_id": "ebsco-fulltext-02-08-2026",
            "source_file": "EBSCO-FullText-02_08_2026.pdf",
            "status": "success",
            "counts": {"words": 6000, "tables": 0, "figures": 10},
            "metadata": {
                "title": "Variational Autoencoders:",
                "authors": [],
                "year": 1973,
                "doi": None,
                "raw_pdf_metadata": {"creationDate": "D:20230802104305-04'00'"},
            },
        },
    )
    _write_paper_md(
        ebsco,
        "\n".join(
            [
                "Variational Autoencoders: A Hands-Off Approach to Volatility",
                "Spring 2022",
                "A volatility surface is an important tool for pricing and hedging derivatives.",
                "Black and Scholes (1973) introduced the model.",
                "The trained variational autoencoder can also be used to generate synthetic surfaces.",
            ]
        ),
    )

    summary = reindex_extracted_directory(extracted_dir=extracted_dir)

    hhaa_manifest = json.loads((hhaa / "manifest.json").read_text(encoding="utf-8"))
    rfaf_manifest = json.loads((rfaf / "manifest.json").read_text(encoding="utf-8"))
    ebsco_manifest = json.loads((ebsco / "manifest.json").read_text(encoding="utf-8"))

    assert hhaa_manifest["metadata"]["year"] == 2021
    assert rfaf_manifest["metadata"]["year"] == 2025

    assert ebsco_manifest["is_duplicate"] is True
    assert ebsco_manifest["duplicate_of"] == "2102-03945v1"
    assert ebsco_manifest["duplicate_reason"] is not None

    inventory = json.loads((extracted_dir / "canonical_inventory.json").read_text(encoding="utf-8"))
    assert inventory["exclude_duplicates"] is True
    assert inventory["duplicates_excluded"] == 1
    assert inventory["total"] == 3
    assert summary["inventory_summary"]["duplicates_excluded"] == 1

