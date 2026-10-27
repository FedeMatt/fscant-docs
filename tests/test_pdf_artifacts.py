"""Post-build checks for multilingual PDF artifacts and HTML hrefs."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urljoin, urlparse

import pytest

try:
    from pypdf import PdfReader
except ImportError:  # pragma: no cover
    PdfReader = None  # type: ignore[misc, assignment]

PDF_FILES = (
    "fscant-user-guide.pdf",
    "fscant-user-guide.it.pdf",
    "fscant-user-guide.de.pdf",
    "fscant-user-guide.pl.pdf",
    "fscant-user-guide.cs.pdf",
)

PAGE_PDF = (
    ("index.html", "/", "fscant-user-guide.pdf"),
    ("it/index.html", "/it/", "fscant-user-guide.it.pdf"),
    ("de/index.html", "/de/", "fscant-user-guide.de.pdf"),
    ("pl/index.html", "/pl/", "fscant-user-guide.pl.pdf"),
    ("cs/index.html", "/cs/", "fscant-user-guide.cs.pdf"),
)

COVERS = (
    ("fscant-user-guide.pdf", "Instruction manual"),
    ("fscant-user-guide.it.pdf", "Manuale di istruzioni"),
    ("fscant-user-guide.de.pdf", "Bedienungsanleitung"),
    ("fscant-user-guide.pl.pdf", "Instrukcja obsługi"),
    ("fscant-user-guide.cs.pdf", "Návod k použití"),
)


def _require_built(repo_root: Path) -> tuple[Path, Path]:
    docs_pdf = repo_root / "docs" / "pdf"
    site_pdf = repo_root / "site" / "pdf"
    missing = [name for name in PDF_FILES if not (site_pdf / name).is_file()]
    if missing:
        pytest.skip(
            "site/pdf missing "
            + ", ".join(missing)
            + " — run ./scripts/build.sh first",
        )
    return docs_pdf, site_pdf


@pytest.mark.parametrize("name", PDF_FILES)
def test_pdf_files_exist_in_docs_and_site(repo_root: Path, name: str) -> None:
    docs_pdf, site_pdf = _require_built(repo_root)
    for folder in (docs_pdf, site_pdf):
        path = folder / name
        assert path.is_file(), f"missing {path}"
        assert path.stat().st_size > 10_000, f"{path} looks empty"


def _hrefs_for_pdf(html: str) -> list[str]:
    return re.findall(
        r'href="([^"]*fscant-user-guide(?:\.(?:it|de|pl|cs))?\.pdf)"',
        html,
    )


def _resolve_under_site(site_root: Path, page_url: str, href: str) -> Path:
    assert "/fscant-docs/" not in href, f"broken absolute prefix in href: {href}"
    if href.startswith(("http://", "https://")):
        path = urlparse(href).path.lstrip("/")
        return site_root / path
    joined = urljoin(page_url, href)
    path = urlparse(joined).path.lstrip("/")
    return site_root / path


@pytest.mark.parametrize(("page_rel", "page_url", "expected_name"), PAGE_PDF)
def test_built_html_pdf_hrefs_resolve(
    repo_root: Path,
    page_rel: str,
    page_url: str,
    expected_name: str,
) -> None:
    _, site_pdf = _require_built(repo_root)
    site_root = repo_root / "site"
    page = site_root / page_rel
    assert page.is_file(), f"missing built page {page}"
    html = page.read_text(encoding="utf-8")
    hrefs = _hrefs_for_pdf(html)
    assert hrefs, f"no PDF hrefs in {page_rel}"
    matching = [h for h in hrefs if expected_name in h]
    assert matching, f"{page_rel} missing href for {expected_name}; got {hrefs}"
    for href in matching:
        target = _resolve_under_site(site_root, page_url, href)
        assert target.is_file(), f"{page_rel} href {href!r} → missing {target}"
        assert target.resolve() == (site_pdf / expected_name).resolve()


@pytest.mark.parametrize(("name", "needle"), COVERS)
def test_pdf_cover_subtitle(repo_root: Path, name: str, needle: str) -> None:
    if PdfReader is None:
        pytest.skip("pypdf not installed")
    _, site_pdf = _require_built(repo_root)
    path = site_pdf / name
    reader = PdfReader(str(path))
    text = "\n".join((page.extract_text() or "") for page in reader.pages[:2])
    assert needle in text, f"{name} cover missing {needle!r}"
