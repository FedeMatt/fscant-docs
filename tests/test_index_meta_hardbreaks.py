"""Guards: consecutive index meta **Label:** lines need Markdown hard breaks."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

LOCALES = ("en", "it", "de", "pl", "cs")
META_LINE = re.compile(r"^\*\*[^*].+:\*\*")


@pytest.mark.parametrize("locale", LOCALES)
def test_index_meta_lines_use_hard_breaks(repo_root: Path, locale: str) -> None:
    path = repo_root / "docs" / locale / "index.md"
    raw_lines = path.read_bytes().split(b"\n")
    text_lines = path.read_text(encoding="utf-8").splitlines()

    failures: list[str] = []
    for i in range(len(text_lines) - 1):
        a, b = text_lines[i], text_lines[i + 1]
        if not (META_LINE.match(a) and META_LINE.match(b)):
            continue
        raw = raw_lines[i]
        if raw.endswith(b"\r"):
            raw = raw[:-1]
        trailing_spaces = len(raw) - len(raw.rstrip(b" "))
        if trailing_spaces < 2:
            failures.append(
                f"{path.relative_to(repo_root)}:{i + 1} "
                f"needs two trailing spaces before next meta line "
                f"(found {trailing_spaces}): {a!r}"
            )

    assert not failures, "\n".join(failures)
