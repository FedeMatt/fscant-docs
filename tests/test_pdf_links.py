"""Fast guards: PDF links must not use the broken /fscant-docs/ absolute prefix."""

from __future__ import annotations

from pathlib import Path

import pytest

FORBIDDEN = "/fscant-docs/pdf/"


@pytest.mark.parametrize(
    ("relpath", "must_contain"),
    [
        ("overrides/partials/header.html", "pdf/fscant-user-guide"),
        ("docs/en/index.md", "../pdf/fscant-user-guide.pdf"),
        ("docs/it/index.md", "../pdf/fscant-user-guide.it.pdf"),
    ],
)
def test_pdf_sources_avoid_fscant_docs_prefix(
    repo_root: Path,
    relpath: str,
    must_contain: str,
) -> None:
    text = (repo_root / relpath).read_text(encoding="utf-8")
    assert FORBIDDEN not in text, f"{relpath} still hardcodes {FORBIDDEN}"
    assert must_contain in text, f"{relpath} missing expected PDF reference {must_contain!r}"


def test_header_uses_url_filter(repo_root: Path) -> None:
    text = (repo_root / "overrides/partials/header.html").read_text(encoding="utf-8")
    assert "guide_pdf_path | url" in text
    assert 'guide_pdf_path = "pdf/fscant-user-guide.pdf"' in text
    assert 'guide_pdf_path = "pdf/fscant-user-guide.it.pdf"' in text


def test_site_url_is_custom_domain(repo_root: Path) -> None:
    text = (repo_root / "mkdocs.yml").read_text(encoding="utf-8")
    assert "site_url: https://fscant-docs.fscan.com/" in text
