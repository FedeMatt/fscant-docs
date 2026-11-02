"""Guards: install docs must not hard-code F-SCANT package version numbers."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

LOCALES = ("en", "it", "de", "pl", "cs")
# e.g. F-SCANT-windows-x64-1.0.11.0.exe or F-SCANT-macos-arm64-1.0.11.zip
VERSIONED_PACKAGE = re.compile(
    r"F-SCANT-(?:windows|macos)-[A-Za-z0-9]+-\d+\.\d+",
    re.IGNORECASE,
)


@pytest.mark.parametrize("locale", LOCALES)
def test_install_md_has_no_versioned_package_filenames(
    repo_root: Path, locale: str
) -> None:
    path = repo_root / "docs" / locale / "install.md"
    text = path.read_text(encoding="utf-8")
    hits = VERSIONED_PACKAGE.findall(text)
    assert not hits, (
        f"{path.relative_to(repo_root)} contains versioned package name(s): "
        f"{hits}"
    )
