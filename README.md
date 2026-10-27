# F-SCANT user guide

Public instruction manual for the F-SCANT computer software (macOS and Windows). Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and [mkdocs-static-i18n](https://ultrabug.github.io/mkdocs-static-i18n/). PDF export via [mkdocs-to-pdf](https://mkdocs-to-pdf.readthedocs.io/en/stable/).

- **Published site (EN):** https://fscant-docs.fscan.com/
- **Published site (IT):** https://fscant-docs.fscan.com/it/
- **PDF (English):** https://fscant-docs.fscan.com/pdf/fscant-user-guide.pdf
- **PDF (Italian):** https://fscant-docs.fscan.com/pdf/fscant-user-guide.it.pdf
- **Sibling app repo (private):** `../fscapp`

## Languages

Pages live under language folders; shared media stays outside those folders:

```
docs/
  assets/       # shared images, videos, logo
  pdf/          # generated PDFs (gitignored binaries; run build.sh)
  stylesheets/
  en/           # English (default, site root)
  it/           # Italian (/it/)
```

English is the default language at `/`. Italian is at `/it/`. Further locales (DE, PL, CS) follow the same pattern — see `.cursor/skills/fscant-docs-i18n/`.

## Preview locally

Requires [uv](https://docs.astral.sh/uv/). Python **3.12+** (mkdocs-to-pdf needs ≥3.11).

```bash
cd /Users/federicomatteo/Developer/fscant/fscant-docs
uv python install 3.12
uv venv --python 3.12
uv pip install -r requirements.txt
uv pip install -r requirements-dev.txt   # tests
./scripts/build.sh                       # once: generate docs/pdf/*.pdf
uv run mkdocs serve
```

Open http://127.0.0.1:8000/ (English) or http://127.0.0.1:8000/it/ (Italian). PDF header/download links need `docs/pdf/*.pdf` present — run `./scripts/build.sh` first (or after pulling a fresh clone).

Header chrome: language selector (EN / IT), light/dark toggle, PDF button, no GitHub repo chip. Brand primary is `#1F40C8`.

## Build site + PDF

PDF generation is off during `mkdocs serve`. For a full production-style build (EN + IT site and both PDFs):

```bash
chmod +x scripts/build.sh   # once
./scripts/build.sh
# → docs/pdf/fscant-user-guide.pdf
# → docs/pdf/fscant-user-guide.it.pdf
# → site/ … (includes site/pdf/…)
```

`mkdocs-to-pdf` is not locale-aware with `mkdocs-static-i18n`, so the script builds each PDF in a single-locale pass (EN, then IT), installs them under `docs/pdf/`, then rebuilds the multilingual site so MkDocs copies those static files into `site/pdf/`. Do not use `ENABLE_PDF_EXPORT=1 uv run mkdocs build` with both languages enabled — that mixes or overwrites the PDF.

## Tests

```bash
uv run pytest tests/test_pdf_links.py          # fast: template/markdown guards
uv run pytest tests/test_pdf_artifacts.py -m "not slow"  # asserts existing build outputs if present
```

The deploy workflow runs the fast link tests, then `./scripts/build.sh`, then post-build artifact checks against `site/`.

## Deploy

Pushes to `main` that touch `docs/`, `mkdocs.yml`, `requirements.txt`, `templates/`, `overrides/`, or the workflow file build (with PDF) and deploy to GitHub Pages. You can also run the **Deploy docs** workflow manually.

In the GitHub repo: **Settings → Pages → Source: GitHub Actions**.

## Media

**Originals (local only):** drop master screenshots and MP4s into `videos-images/` (gitignored). Never commit that folder.

**Published assets:** only the files under `docs/assets/` are committed and deployed (shared across languages). Generated PDFs under `docs/pdf/` are gitignored and produced by CI/`build.sh`.

In markdown, reference images as `../assets/images/...` from locale pages. In raw HTML `<video>` tags, use site-root paths carefully (prefer paths that work on the custom domain root, not a `/fscant-docs/` prefix).

```bash
brew install ffmpeg   # once
uv run python scripts/compress_videos.py --force
```

That re-encodes MP4s from `videos-images/` into `docs/assets/videos/` (720p H.264 yuv420p High, ~1.2 Mbps, faststart — Safari- and Chrome-safe). Copy/rename PNGs into `docs/assets/images/` per the inventory READMEs (or the media mapping used when adding a batch).

Inventory / still-missing slots:

- `docs/assets/images/fscant-user-guide/` — see that folder’s README
- `docs/assets/images/connect-the-f-scan-on-mac/` — see that folder’s README
- `docs/assets/videos/` — see that folder’s README
