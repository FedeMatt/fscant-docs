"""Fast guards: PDF links must not use the broken /fscant-docs/ absolute prefix."""

from __future__ import annotations

from pathlib import Path

import pytest

FORBIDDEN = "/fscant-docs/pdf/"
LOCALES = ("en", "it", "de", "pl", "cs")
EN_PAGES = (
    "index.md",
    "install.md",
    "connect.md",
    "connect-mac.md",
    "dirp.md",
    "analysis.md",
    "users.md",
    "settings.md",
)


@pytest.mark.parametrize(
    ("relpath", "must_contain"),
    [
        ("overrides/partials/header.html", "pdf/fscant-user-guide"),
        ("docs/en/index.md", "../pdf/fscant-user-guide.pdf"),
        ("docs/it/index.md", "../pdf/fscant-user-guide.it.pdf"),
        ("docs/de/index.md", "../pdf/fscant-user-guide.de.pdf"),
        ("docs/pl/index.md", "../pdf/fscant-user-guide.pl.pdf"),
        ("docs/cs/index.md", "../pdf/fscant-user-guide.cs.pdf"),
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


def test_header_uses_url_filter_for_all_locales(repo_root: Path) -> None:
    text = (repo_root / "overrides/partials/header.html").read_text(encoding="utf-8")
    assert "guide_pdf_path | url" in text
    for path in (
        "pdf/fscant-user-guide.pdf",
        "pdf/fscant-user-guide.it.pdf",
        "pdf/fscant-user-guide.de.pdf",
        "pdf/fscant-user-guide.pl.pdf",
        "pdf/fscant-user-guide.cs.pdf",
    ):
        assert path in text, f"header missing {path}"


def test_site_url_is_custom_domain(repo_root: Path) -> None:
    text = (repo_root / "mkdocs.yml").read_text(encoding="utf-8")
    assert "site_url: https://fscant-docs.fscan.com/" in text


@pytest.mark.parametrize("locale", LOCALES)
def test_locale_mirrors_en_pages(repo_root: Path, locale: str) -> None:
    folder = repo_root / "docs" / locale
    assert folder.is_dir(), f"missing docs/{locale}/"
    for name in EN_PAGES:
        assert (folder / name).is_file(), f"missing docs/{locale}/{name}"


def test_mkdocs_lists_all_locales(repo_root: Path) -> None:
    text = (repo_root / "mkdocs.yml").read_text(encoding="utf-8")
    for locale in LOCALES:
        assert f"locale: {locale}" in text
