"""Guards: Material thin scrollbars stay grey, never brand accent blue."""

from __future__ import annotations

import re
from pathlib import Path

BRAND_BLUE = re.compile(r"#1[Ff]40[Cc]8")
ACCENT_VAR = "--md-accent-fg-color"
GREY_VAR = "--md-default-fg-color--lighter"
REQUIRED_HOSTS = (
    ".md-sidebar__scrollwrap",
    ".md-search__scrollwrap",
    ".md-typeset pre > code",
    ".md-tooltip2__inner",
)
EXTRA_CSS_LINE = re.compile(
    r"^\s*-\s*(stylesheets/extra(?:\.[A-Za-z0-9]+)?\.css)\s*$",
    re.MULTILINE,
)
COMMENT = re.compile(r"/\*.*?\*/", re.DOTALL)
SCROLLBAR_DECL = re.compile(
    r"(?:scrollbar-color|::-webkit-scrollbar-thumb[^{]*\{[^}]*background-color)"
    r"[^;]*;",
    re.IGNORECASE,
)


def _extra_css_path(repo_root: Path) -> Path:
    text = (repo_root / "mkdocs.yml").read_text(encoding="utf-8")
    match = EXTRA_CSS_LINE.search(text)
    assert match, "mkdocs.yml must list a stylesheets/extra*.css under extra_css"
    path = repo_root / "docs" / match.group(1)
    assert path.is_file(), f"extra_css file missing: {path}"
    return path


def test_scrollbar_rules_stay_grey_not_brand_blue(repo_root: Path) -> None:
    path = _extra_css_path(repo_root)
    css = COMMENT.sub("", path.read_text(encoding="utf-8"))

    for host in REQUIRED_HOSTS:
        assert host in css, (
            f"{path.relative_to(repo_root)} must cover scrollbar host {host}"
        )

    decls = SCROLLBAR_DECL.findall(css)
    # Also catch multi-line background-color blocks for webkit thumbs.
    thumb_blocks = re.findall(
        r"::-webkit-scrollbar-thumb[^{]*\{([^}]*)\}",
        css,
        flags=re.IGNORECASE,
    )
    scrollbar_color_decls = re.findall(
        r"scrollbar-color\s*:[^;]+;",
        css,
        flags=re.IGNORECASE,
    )
    assert thumb_blocks or scrollbar_color_decls, (
        f"no scrollbar declarations found in {path.relative_to(repo_root)}"
    )

    checked = scrollbar_color_decls + [
        f"background-color:{body}" for body in thumb_blocks
    ]
    assert any(GREY_VAR in decl for decl in checked), (
        f"{path.relative_to(repo_root)} must use {GREY_VAR} for scrollbars"
    )

    failures: list[str] = []
    for decl in checked:
        if ACCENT_VAR in decl:
            failures.append(f"uses {ACCENT_VAR}: {decl.strip()}")
        if BRAND_BLUE.search(decl):
            failures.append(f"uses brand blue: {decl.strip()}")
    assert not failures, (
        f"{path.relative_to(repo_root)} scrollbar declarations must not use "
        f"accent/brand blue:\n" + "\n".join(failures)
    )
