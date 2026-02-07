from pathlib import Path

from pdf_pipeline.discover import build_jobs, discover_pdfs, slugify


def test_slugify_basic() -> None:
    assert slugify("A Test for Superior Predictive Ability") == "a-test-for-superior-predictive-ability"
    assert slugify("S0022109010000220") == "s0022109010000220"


def test_discover_skips_appledouble(tmp_path: Path) -> None:
    (tmp_path / "real.pdf").write_bytes(b"%PDF-1.4")
    (tmp_path / "._real.pdf").write_bytes(b"ignored")

    found = discover_pdfs(tmp_path)
    assert [path.name for path in found] == ["real.pdf"]


def test_build_jobs_handles_collisions(tmp_path: Path) -> None:
    first = tmp_path / "Test!.pdf"
    second = tmp_path / "Test?.pdf"
    first.write_bytes(b"%PDF-1.4")
    second.write_bytes(b"%PDF-1.4")

    jobs = build_jobs([first, second])
    assert len(jobs) == 2
    assert jobs[0].paper_id != jobs[1].paper_id
