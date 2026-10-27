"""mkdocs-to-pdf hook: alternate PDF link only (header button lives in overrides)."""

from __future__ import annotations

from logging import Logger

from bs4 import BeautifulSoup
from mkdocs.structure.pages import Page


def inject_link(html: str, pdf_path: str, page: Page, logger: Logger) -> str:
    """Inject PDF head alternate link. Header control is in overrides/partials/header.html."""
    soup = BeautifulSoup(html, "html.parser")

    if soup.head is not None:
        soup.head.append(
            soup.new_tag(
                "link",
                href=pdf_path,
                rel="alternate",
                title="PDF",
                type="application/pdf",
            ),
        )
        logger.debug("inject PDF alternate link on %s → %s", page.title, pdf_path)

    return str(soup)
